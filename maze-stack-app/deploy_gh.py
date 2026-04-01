# -*- coding: utf-8 -*-
"""
Deploy to GitHub Pages
1. Create a GitHub repo via API
2. Push files
3. Enable GitHub Pages
"""
import urllib.request, urllib.parse, json, base64, os, time

# GitHub token - user needs to provide their PAT
# For now, try to get from environment or use a placeholder
TOKEN = os.environ.get('GITHUB_TOKEN', '')

REPO_NAME = 'maze-stack-visualizer'
USER_AGENT = 'MazeStackApp/1.0'

def github_api(method, path, data=None, token=None):
    """Make GitHub API request"""
    url = f'https://api.github.com{path}'
    headers = {
        'Accept': 'application/vnd.github.v3+json',
        'User-Agent': USER_AGENT,
    }
    if token:
        headers['Authorization'] = f'token {token}'
    if data:
        headers['Content-Type'] = 'application/json'
        data = json.dumps(data).encode()

    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read()), resp.status
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        return {'error': body}, e.code

def create_or_get_repo(token):
    """Create repo or get existing one"""
    # Try to create new repo
    data, status = github_api('POST', '/user/repos', {
        'name': REPO_NAME,
        'description': '用栈实现迷宫探路 - 可视化教学工具',
        'homepage': 'https://username.github.io/maze-stack-visualizer/',
        'private': False,
        'auto_init': False,
        'has_pages': True
    }, token)
    if status == 201:
        return data['full_name'], True
    elif status == 422:
        # Repo already exists, get it
        data, _ = github_api('GET', f'/repos/{token[:20] if False else "me"}/{REPO_NAME}'.replace('/me/', '/user/'), token=token)
        # Try different approach
        data, _ = github_api('GET', f'/repos/{get_login(token)}/{REPO_NAME}', token=token)
        return data.get('full_name', REPO_NAME), False
    return None, False

def get_login(token):
    """Get GitHub username"""
    data, _ = github_api('GET', '/user', token=token)
    return data.get('login', '')

def upload_file(token, repo, path, content, message):
    """Upload a file to repo"""
    url = f'https://api.github.com/repos/{repo}/contents/{path}'
    headers = {
        'Accept': 'application/vnd.github.v3+json',
        'User-Agent': USER_AGENT,
        'Authorization': f'token {token}',
        'Content-Type': 'application/json',
    }
    # Encode content
    content_b64 = base64.b64encode(content.encode('utf-8')).decode()
    data = json.dumps({
        'message': message,
        'content': content_b64,
    }).encode()

    req = urllib.request.Request(url, data=data, headers=headers, method='PUT')
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        return {'error': e.read().decode()}

def enable_pages(token, repo):
    """Enable GitHub Pages"""
    url = f'https://api.github.com/repos/{repo}/pages'
    headers = {
        'Accept': 'application/vnd.github.v3+json',
        'User-Agent': USER_AGENT,
        'Authorization': f'token {token}',
        'Content-Type': 'application/json',
    }
    data = json.dumps({
        'source': {'branch': 'main', 'path': '/'}
    }).encode()
    req = urllib.request.Request(url, data=data, headers=headers, method='POST')
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        return {'error': e.read().decode()}

def main():
    html_file = r'c:\Users\admin\WorkBuddy\20260331210244\maze-stack-app\index.html'

    if not os.path.exists(html_file):
        print('ERROR: index.html not found')
        return

    if not TOKEN:
        print('No GitHub token found. Please provide GITHUB_TOKEN environment variable.')
        print('To get a token: https://github.com/settings/tokens')
        print('Required scopes: repo, workflow')
        return

    # Read HTML
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    print(f'HTML file size: {len(html_content)} bytes')

    # Get username
    login = get_login(TOKEN)
    print(f'GitHub username: {login}')

    # Create repo
    full_name, is_new = create_or_get_repo(TOKEN)
    if not full_name:
        print('Failed to create/get repo')
        return
    print(f'Repo: {full_name} (new={is_new})')

    # Upload index.html
    print('Uploading index.html...')
    result = upload_file(TOKEN, full_name, 'index.html', html_content, 'Deploy maze stack visualizer')
    if 'error' in result:
        print(f'Upload error: {result["error"][:200]}')
    else:
        print('Upload successful!')

    # Upload README
    readme = f'''# 迷宫探路可视化工具

用栈（Stack）实现迷宫探路 - 深度优先搜索（DFS）的可视化教学工具。

## 功能特性

- 交互式迷宫模拟器
- 栈的基本操作演示
- 25道练习题及解析
- 支持随机生成迷宫和手动编辑

## 访问地址

https://{login}.github.io/{REPO_NAME}/
'''
    upload_file(TOKEN, full_name, 'README.md', readme, 'Add README')

    # Enable pages
    print('Enabling GitHub Pages...')
    pages_result = enable_pages(TOKEN, full_name)
    if 'error' in pages_result:
        print(f'Pages error (may already be enabled): {pages_result["error"][:200]}')
    else:
        print('GitHub Pages enabled!')

    print(f'\n=== Deployment Complete ===')
    print(f'Repo: https://github.com/{full_name}')
    print(f'Website: https://{login}.github.io/{REPO_NAME}/')
    print(f'Note: GitHub Pages may take 1-2 minutes to activate')

if __name__ == '__main__':
    main()
