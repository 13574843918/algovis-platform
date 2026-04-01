# -*- coding: utf-8 -*-
"""
Deploy script for GitHub Pages
Usage: set GITHUB_TOKEN env var, then run: python deploy.py
Get token: https://github.com/settings/tokens (scope: repo)
"""
import urllib.request, json, base64, os, sys

HTML_FILE = os.path.join(os.path.dirname(__file__), 'index.html')
TOKEN = os.environ.get('GITHUB_TOKEN', '')
REPO = 'maze-stack-visualizer'

def api(method, path, data=None):
    url = f'https://api.github.com{path}'
    h = {'Accept':'application/vnd.github.v3+json','Authorization':f'token {TOKEN}','User-Agent':'MazeApp/1.0'}
    if data: h['Content-Type']='application/json'; data=json.dumps(data).encode()
    req = urllib.request.Request(url, data=data, headers=h, method=method)
    try:
        with urllib.request.urlopen(req, 30) as r: return json.loads(r.read()), r.status
    except urllib.error.HTTPError as e:
        return {'err': e.read().decode()[:300]}, e.code

def main():
    if not TOKEN:
        print('ERROR: Set GITHUB_TOKEN env var first.')
        print('1. Go to https://github.com/settings/tokens')
        print('2. Generate new token (classic)')
        print('3. Select scope: repo')
        print('4. Run: $env:GITHUB_TOKEN="your_token"; python deploy.py')
        sys.exit(1)

    with open(HTML_FILE, 'r', encoding='utf-8') as f:
        html = f.read()

    # Get username
    user, _ = api('GET', '/user')
    login = user.get('login','')
    print(f'Logged in as: {login}')

    # Create repo
    _, s = api('POST', '/user/repos', {'name':REPO,'private':False,'has_pages':True})
    if s in (201, 422): print(f'Repo ready: github.com/{login}/{REPO}')
    else: print(f'Repo error: {_}')

    # Upload HTML
    b64 = base64.b64encode(html.encode()).decode()
    _, s = api('PUT', f'/repos/{login}/{REPO}/contents/index.html',
               {'message':'Deploy v1','content':b64})
    if 'err' in _: print(f'Upload error: {_}'); sys.exit(1)
    else: print('index.html uploaded!')

    # Upload README
    readme = f'# 迷宫探路可视化\n\n用栈实现迷宫探路的交互式可视化教学工具。\n\n:rocket: https://{login}.github.io/{REPO}/\n'
    b64r = base64.b64encode(readme.encode()).decode()
    api('PUT', f'/repos/{login}/{REPO}/contents/README.md',
        {'message':'Add README','content':b64r})

    # Enable pages
    api('POST', f'/repos/{login}/{REPO}/pages',
        {'source':{'branch':'main','path':'/'}})

    url = f'https://{login}.github.io/{REPO}/'
    print(f'\n========== DONE ==========')
    print(f'Repo:  https://github.com/{login}/{REPO}')
    print(f'URL:   {url}')
    print(f'Note:  GitHub Pages 激活需要 1-2 分钟')

if __name__ == '__main__':
    main()
