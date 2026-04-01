# -*- coding: utf-8 -*-
"""
AlgoVis 平台一键部署脚本
支持：根目录 index.html（首页）+ maze-stack-app/ 子模块
使用：设置 GITHUB_TOKEN 环境变量后运行 python deploy.py
获取 Token: https://github.com/settings/tokens → Generate new token (classic) → 勾选 repo
"""
import urllib.request
import urllib.error
import json
import base64
import os
import sys

# ========== 配置区 ==========
TOKEN = os.environ.get('GITHUB_TOKEN', '')
REPO = 'algovis-platform'       # 仓库名（可修改）
# =============================

BASE = os.path.dirname(os.path.abspath(__file__))
APP_DIR = os.path.join(BASE, 'maze-stack-app')
TRAINING_APP_DIR = os.path.join(BASE, 'training-app')
ROOT_HTML = os.path.join(BASE, 'index.html')
LOGIN = ''

def api(method, path, data=None):
    url = f'https://api.github.com{path}'
    h = {
        'Accept': 'application/vnd.github.v3+json',
        'Authorization': f'token {TOKEN}',
        'User-Agent': 'AlgoVis/1.0'
    }
    if data:
        h['Content-Type'] = 'application/json'
        data = json.dumps(data).encode()
    req = urllib.request.Request(url, data=data, headers=h, method=method)
    try:
        with urllib.request.urlopen(req, 60) as r:
            return json.loads(r.read()), r.status
    except urllib.error.HTTPError as e:
        return {'err': e.read().decode()[:500]}, e.code

def upload_file(content, path, msg):
    """通过 GitHub Contents API 上传/更新单个文件（支持已存在文件自动携带 SHA）"""
    b64_content = base64.b64encode(content.encode()).decode()
    # 先查 SHA
    data, status = api('GET', f'/repos/{LOGIN}/{REPO}/contents/{path}')
    sha = data.get('sha', '') if status == 200 else ''
    payload = {'message': msg, 'content': b64_content}
    if sha:
        payload['sha'] = sha
    body = json.dumps(payload).encode()
    req = urllib.request.Request(
        f'https://api.github.com/repos/{LOGIN}/{REPO}/contents/{path}',
        data=body,
        headers={
            'Accept': 'application/vnd.github.v3+json',
            'Authorization': f'token {TOKEN}',
            'Content-Type': 'application/json',
            'User-Agent': 'AlgoVis/1.0'
        },
        method='PUT'
    )
    try:
        with urllib.request.urlopen(req, 60) as r:
            res = json.loads(r.read())
            return 'ok', res.get('commit', {}).get('sha', '')[:8]
    except urllib.error.HTTPError as e:
        return 'err', e.read().decode()[:200]

def scan_files(directory, prefix=''):
    files = []
    for entry in os.scandir(directory):
        rel = os.path.join(prefix, entry.name)
        if entry.is_file():
            files.append((rel, entry.path))
        elif entry.is_dir():
            if entry.name in ('node_modules', '.git', '__pycache__', '.cache'):
                continue
            files.extend(scan_files(entry.path, rel))
    return files

def main():
    global LOGIN
    if not TOKEN:
        print('=' * 50)
        print('  错误：未设置 GITHUB_TOKEN')
        print('=' * 50)
        print()
        print('  第 1 步：获取 GitHub Token（1 分钟）')
        print('  1) 打开: https://github.com/settings/tokens')
        print('  2) 点击 "Generate new token (classic)"')
        print('  3) Description 填: algovis-deploy')
        print('  4) 勾选: repo  （完全控制仓库）')
        print('  5) 点击 "Generate token"，复制字符')
        print()
        print('  第 2 步：运行部署（30 秒）')
        print('  $env:GITHUB_TOKEN = "你的Token"')
        print('  python deploy.py')
        print()
        sys.exit(1)

    print('正在登录 GitHub...')
    user, s = api('GET', '/user')
    if 'err' in user:
        print(f'登录失败: {user["err"]}')
        sys.exit(1)
    LOGIN = user.get('login', '')
    print(f'已登录: @{LOGIN}')

    # 创建仓库
    print(f'创建仓库 {REPO}...')
    _, s = api('POST', '/user/repos', {
        'name': REPO,
        'private': False,
        'has_pages': True,
        'description': 'AlgoVis 算法可视化学习平台'
    })
    if s == 201:
        print('新仓库已创建')
    elif s == 422:
        print('仓库已存在，跳过创建')
    else:
        print(f'仓库状态: {_}')

    # 收集文件
    all_files = []
    if os.path.exists(ROOT_HTML):
        all_files.append(('index.html', ROOT_HTML))
        print('发现: index.html（首页）')
    if os.path.isdir(APP_DIR):
        subs = scan_files(APP_DIR, 'maze-stack-app')
        all_files.extend(subs)
        print(f'发现: maze-stack-app/  ({len(subs)} 个文件)')
    if os.path.isdir(TRAINING_APP_DIR):
        subs = scan_files(TRAINING_APP_DIR, 'training-app')
        all_files.extend(subs)
        print(f'发现: training-app/  ({len(subs)} 个文件)')

    print(f'\n开始上传 {len(all_files)} 个文件...')
    for i, (rel, abspath) in enumerate(all_files, 1):
        try:
            with open(abspath, 'r', encoding='utf-8') as f:
                content = f.read()
            status, info = upload_file(content, rel, f'Add {rel}')
            icon = 'ok' if status == 'ok' else 'err'
            print(f'  [{i:02d}/{len(all_files)}] {icon} {rel}  ({len(content):,}b)')
        except Exception as e:
            print(f'  [{i:02d}/{len(all_files)}] err {rel}: {e}')

    # 启用 Pages
    print('\n启用 GitHub Pages...')
    _, s = api('POST', f'/repos/{LOGIN}/{REPO}/pages', {
        'source': {'branch': 'main', 'path': '/'}
    })
    if s in (201, 204):
        print('GitHub Pages 已启用')
    else:
        print(f'Pages 状态: {s}（可能已启用）')

    url = f'https://{LOGIN}.github.io/{REPO}/'
    print()
    print('=' * 50)
    print('  部署完成！')
    print('=' * 50)
    print(f'  仓库: https://github.com/{LOGIN}/{REPO}')
    print(f'  网站: {url}')
    print()
    print('  GitHub Pages 需要 1-2 分钟激活')
    print('=' * 50)

if __name__ == '__main__':
    main()
