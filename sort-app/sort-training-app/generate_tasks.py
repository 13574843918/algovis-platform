#!/usr/bin/env python3
"""生成排序实训 Task 6(快速排序) 和 Task 7(归并+基数排序) 独立页面"""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TEMPLATE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | 排序实训</title>
<style>
:root {{
  --bg: #0f172a; --surface: #1e293b; --surface2: #263248; --border: #334155;
  --text: #e2e8f0; --text2: #94a3b8;
  --accent: #f59e0b; --accent2: #fb923c;
  --green: #34d399; --red: #f87171; --blue: #60a5fa; --purple: #a78bfa;
}}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font-family: 'Segoe UI', system-ui, sans-serif; background: var(--bg); color: var(--text); min-height: 100vh; }}

.nav {{ background: rgba(15,23,42,.95); border-bottom: 1px solid var(--border); position: sticky; top: 0; z-index: 100; backdrop-filter: blur(8px); }}
.nav-inner {{ max-width: 1100px; margin: 0 auto; display: flex; align-items: center; gap: 2px; padding: 0 1rem; overflow-x: auto; }}
.tab-btn {{ padding: .7rem .9rem; border: none; background: none; color: var(--text2); cursor: pointer; font-size: .82rem; white-space: nowrap; border-bottom: 2px solid transparent; transition: all .2s; font-family: inherit; }}
.tab-btn:hover {{ color: var(--text); background: rgba(255,255,255,.05); }}
.tab-btn.active {{ color: var(--accent); border-bottom-color: var(--accent); }}
.tab-btn.current {{ background: rgba(245,158,11,.15); color: var(--accent); border: 1px solid rgba(245,158,11,.4); border-radius: 6px; margin: 4px 2px; }}
.nav-home {{ margin-left: auto; padding: .45rem .8rem; background: rgba(245,158,11,.1); border: 1px solid rgba(245,158,11,.3); border-radius: 6px; color: var(--accent); text-decoration: none; font-size: .8rem; white-space: nowrap; transition: all .2s; }}
.nav-home:hover {{ background: rgba(245,158,11,.2); }}

.container {{ max-width: 1100px; margin: 0 auto; padding: 2rem 1.5rem; }}
.back-btn {{ display: inline-flex; align-items: center; gap: .4rem; padding: .5rem 1rem; background: var(--surface); border: 1px solid var(--border); border-radius: 8px; color: var(--text2); text-decoration: none; font-size: .85rem; cursor: pointer; margin-bottom: 1.5rem; transition: all .2s; }}
.back-btn:hover {{ border-color: var(--accent); color: var(--accent); }}

.section {{ background: var(--surface); border: 1px solid var(--border); border-radius: 12px; padding: 1.5rem; margin-bottom: 1.2rem; }}
.section h2 {{ color: var(--accent); font-size: 1.05rem; margin-bottom: 1rem; display: flex; align-items: center; gap: .5rem; }}
.section h2 .num {{ width: 26px; height: 26px; border-radius: 50%; background: rgba(245,158,11,.15); border: 1px solid rgba(245,158,11,.3); color: var(--accent); font-size: .75rem; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }}
.section p {{ color: var(--text2); font-size: .88rem; line-height: 1.7; margin-bottom: .6rem; }}
.section p strong {{ color: var(--text); }}
.section ul {{ margin: .5rem 0 .5rem 1.2rem; }}
.section li {{ color: var(--text2); font-size: .85rem; line-height: 1.7; margin-bottom: .3rem; }}
.section li strong {{ color: var(--text); }}
code {{ background: rgba(245,158,11,.1); color: var(--accent); padding: .1rem .35rem; border-radius: 4px; font-size: .82rem; }}

.code-block {{ background: #0d1117; border: 1px solid var(--border); border-radius: 8px; padding: 1rem; margin: .8rem 0; overflow-x: auto; position: relative; }}
.code-block pre {{ font-family: 'Consolas','Monaco',monospace; font-size: .82rem; line-height: 1.7; color: #c9d1d9; white-space: pre; }}
.code-block .keyword {{ color: #ff7b72; }}
.code-block .type {{ color: #d2a8ff; }}
.code-block .comment {{ color: #8b949e; font-style: italic; }}
.code-block .num-literal {{ color: #f0883e; }}
.copy-btn {{ position: absolute; top: .5rem; right: .5rem; padding: .25rem .6rem; background: rgba(245,158,11,.1); border: 1px solid rgba(245,158,11,.3); border-radius: 5px; color: var(--accent); font-size: .72rem; cursor: pointer; transition: all .2s; }}
.copy-btn:hover {{ background: rgba(245,158,11,.2); }}
.copy-btn.copied {{ background: rgba(52,211,153,.15); border-color: rgba(52,211,153,.3); color: var(--green); }}

.data-table {{ width: 100%; border-collapse: collapse; margin: .8rem 0; font-size: .85rem; }}
.data-table th {{ background: rgba(245,158,11,.1); color: var(--accent); padding: .5rem .8rem; text-align: left; border: 1px solid rgba(245,158,11,.2); font-weight: 600; }}
.data-table td {{ padding: .45rem .8rem; border: 1px solid var(--border); color: var(--text2); }}
.data-table tr:hover td {{ background: rgba(255,255,255,.03); }}

.viz {{ background: var(--surface2); border: 1px solid var(--border); border-radius: 10px; padding: 1rem; margin: .8rem 0; }}
.viz-controls {{ display: flex; gap: .5rem; flex-wrap: wrap; margin-bottom: 1rem; }}
.viz-btn {{ padding: .4rem 1rem; border: 1px solid var(--border); background: var(--surface); color: var(--text2); border-radius: 6px; cursor: pointer; font-size: .82rem; transition: all .2s; font-family: inherit; }}
.viz-btn:hover {{ border-color: var(--accent); color: var(--accent); }}
.viz-btn.primary {{ background: rgba(245,158,11,.15); border-color: rgba(245,158,11,.4); color: var(--accent); }}
.viz-btn:disabled {{ opacity: .4; cursor: not-allowed; }}
.speed-select {{ padding: .4rem .5rem; border-radius: 6px; border: 1px solid var(--border); background: var(--surface); color: var(--text2); font-size: .82rem; }}
.viz-info {{ font-size: .8rem; color: var(--text2); margin-bottom: .5rem; }}
.viz-array {{ display: flex; gap: 3px; margin: .8rem 0; flex-wrap: wrap; }}
.arr-cell {{ min-width: 40px; height: 46px; display: flex; flex-direction: column; align-items: center; justify-content: center; background: var(--surface); border: 2px solid var(--border); border-radius: 6px; font-size: .78rem; transition: all .3s; }}
.arr-cell .price {{ color: var(--text); font-weight: 700; font-size: .85rem; }}
.arr-cell .brand {{ color: var(--text2); font-size: .6rem; margin-top: 2px; }}
.arr-cell .idx {{ font-size: .52rem; color: rgba(255,255,255,.25); margin-top: 1px; }}
.arr-cell.comparing {{ background: rgba(245,158,11,.15); border-color: var(--accent); }}
.arr-cell.comparing .price {{ color: var(--accent); }}
.arr-cell.swapping {{ background: rgba(248,113,113,.15); border-color: var(--red); }}
.arr-cell.swapping .price {{ color: var(--red); }}
.arr-cell.sorted {{ background: rgba(52,211,153,.1); border-color: rgba(52,211,153,.3); }}
.arr-cell.sorted .price {{ color: var(--green); }}
.arr-cell.pivot {{ border-color: var(--blue); background: rgba(96,165,250,.15); }}
.arr-cell.pivot .price {{ color: var(--blue); }}
.arr-cell.heap-root {{ border-color: var(--blue); background: rgba(96,165,250,.15); }}
.arr-cell.heap-root .price {{ color: var(--blue); }}
.viz-progress {{ height: 4px; background: var(--border); border-radius: 2px; margin: .5rem 0; }}
.viz-progress-bar {{ height: 100%; background: linear-gradient(90deg,var(--accent),var(--accent2)); border-radius: 2px; transition: width .3s; width: 0%; }}
.viz-log {{ background: #0d1117; border: 1px solid var(--border); border-radius: 6px; padding: .6rem; max-height: 150px; overflow-y: auto; font-family: 'Consolas',monospace; font-size: .75rem; color: #8b949e; margin-top: .8rem; }}
.viz-log .log-line {{ margin-bottom: 2px; }}
.viz-log .log-op {{ color: #f0883e; }}
.viz-log .log-info {{ color: #79c0ff; }}
.viz-log .log-ok {{ color: #34d399; }}

.exercise {{ background: var(--surface2); border: 1px solid var(--border); border-radius: 10px; padding: 1.2rem; margin-bottom: 1rem; }}
.exercise .q-text {{ font-size: .9rem; color: var(--text); margin-bottom: .8rem; line-height: 1.6; }}
.exercise .q-num {{ color: var(--accent); font-weight: 700; margin-right: .4rem; }}
.exercise label {{ display: flex; align-items: flex-start; gap: .5rem; padding: .4rem .6rem; border-radius: 6px; cursor: pointer; font-size: .85rem; color: var(--text2); transition: all .2s; margin: .2rem 0; }}
.exercise label:hover {{ background: rgba(245,158,11,.06); color: var(--text); }}
.exercise input[type=radio] {{ accent-color: var(--accent); flex-shrink: 0; margin-top: .15rem; }}
.exercise label.correct {{ background: rgba(52,211,153,.1); color: var(--green); border-radius: 6px; }}
.exercise label.wrong {{ background: rgba(248,113,113,.1); color: var(--red); border-radius: 6px; }}
.check-btn {{ padding: .45rem 1.2rem; background: rgba(245,158,11,.15); border: 1px solid rgba(245,158,11,.4); border-radius: 8px; color: var(--accent); font-size: .85rem; cursor: pointer; margin-top: .8rem; transition: all .2s; font-family: inherit; }}
.check-btn:hover {{ background: rgba(245,158,11,.25); }}
.result {{ margin-top: .8rem; padding: .6rem 1rem; border-radius: 6px; font-size: .85rem; display: none; }}
.result.show {{ display: block; }}
.result.pass {{ background: rgba(52,211,153,.1); border: 1px solid rgba(52,211,153,.3); color: var(--green); }}
.result.fail {{ background: rgba(248,113,113,.1); border: 1px solid rgba(248,113,113,.3); color: var(--red); }}
.hint {{ background: rgba(167,139,250,.08); border: 1px solid rgba(167,139,250,.2); border-radius: 8px; padding: .8rem 1rem; margin: .8rem 0; }}
.hint h4 {{ color: var(--purple); font-size: .82rem; margin-bottom: .4rem; }}
.hint p {{ color: var(--text2); font-size: .82rem; line-height: 1.6; }}
.answer-btn {{ padding: .4rem 1rem; background: var(--surface2); border: 1px solid var(--border); border-radius: 6px; color: var(--text2); font-size: .8rem; cursor: pointer; margin-top: .5rem; transition: all .2s; font-family: inherit; }}
.answer-btn:hover {{ border-color: var(--purple); color: var(--purple); }}
.answer-box {{ display: none; background: rgba(167,139,250,.08); border: 1px solid rgba(167,139,250,.2); border-radius: 8px; padding: .8rem 1rem; margin-top: .5rem; font-size: .85rem; color: var(--purple); }}
.answer-box.show {{ display: block; }}
</style>
</head>
<body>

<nav class="nav">
  <div class="nav-inner">
    <button class="tab-btn" onclick="location.href='index.html?tab=guide'">&#128218; 导读</button>
    <button class="tab-btn" onclick="location.href='index.html?tab=simulator'">&#127918; 模拟器</button>
    <button class="tab-btn" onclick="location.href='index.html?tab=operations'">&#128736; 基本操作</button>
    <button class="tab-btn" onclick="location.href='index.html?tab=theory'">&#128218; 理论知识</button>
    <button class="tab-btn" onclick="location.href='index.html?tab=exercises'">&#9997; 练习题</button>
    <button class="tab-btn current" onclick="location.href='index.html'">&#128187; 实训</button>
    <a class="nav-home" href="index.html">&#127968; 返回实训列表</a>
  </div>
</nav>

<div class="container">
  <a class="back-btn" href="index.html">&#8592; 返回实训列表</a>
  {content}
</div>

<script>
const PRODUCTS = [
  {{brand:'inphic', type:'PB1P', reviews:20,  price:30}},
  {{brand:'logitech', type:'M220', reviews:100, price:69}},
  {{brand:'rapoo', type:'M300G', reviews:20,  price:59}},
  {{brand:'inphic', type:'PW1H', reviews:50,  price:27}},
  {{brand:'mi', type:'Lite2', reviews:200, price:34}},
  {{brand:'logitech', type:'M187P', reviews:1,   price:49}},
  {{brand:'inphic', type:'DR01', reviews:2,   price:53}},
  {{brand:'logitech', type:'M330', reviews:100, price:99}},
  {{brand:'dareu', type:'EM915', reviews:50,  price:89}},
  {{brand:'inphic', type:'PM6', reviews:100,  price:28}},
];

(function initTable(){{
  const tb = document.getElementById('dataTbody');
  if(!tb) return;
  PRODUCTS.forEach((p,i) => {{
    const tr = document.createElement('tr');
    tr.innerHTML = `<td>${{i}}</td><td>${{p.brand}}</td><td>${{p.type}}</td><td>${{p.reviews}}</td><td>${{p.price}}</td>`;
    tb.appendChild(tr);
  }});
}})();

// ============ 工具函数 ============
function copyCode(btn){{{
  const pre = btn.parentElement.querySelector('pre');
  if(!pre) return;
  navigator.clipboard.writeText(pre.textContent).then(() => {{
    btn.textContent = '已复制!';
    btn.classList.add('copied');
    setTimeout(() => {{ btn.textContent = '复制'; btn.classList.remove('copied'); }}, 1500);
  }});
}}

function toggleAnswer(btn){{{
  const box = btn.nextElementSibling;
  if(box.classList.contains('show')){{{
    box.classList.remove('show');
    btn.textContent = '显示答案';
  }}} else {{{
    box.classList.add('show');
    btn.textContent = '隐藏答案';
  }}}
}}

function checkAnswer(name, correct, btn){{{
  const radios = document.getElementsByName(name);
  const result = document.getElementById('result_' + name);
  let selected = '';
  for(let r of radios){{ if(r.checked) selected = r.value; }}
  const isCorrect = selected === correct;
  result.className = 'result show ' + (isCorrect ? 'pass' : 'fail');
  result.innerHTML = isCorrect ? '&#10004; 正确！' : '&#10006; 错误，正确答案是 ' + correct.toUpperCase() + '。';
  radios.forEach(r => {{
    r.parentElement.classList.remove('correct','wrong');
    if(r.value === correct) r.parentElement.classList.add('correct');
    else if(r.checked && r.value !== correct) r.parentElement.classList.add('wrong');
  }});
}}

{js_content}
</script>
</body>
</html>"""

# ========== Task 6: 快速排序 ==========
TASK6_CONTENT = """
  <div class="section">
    <h2><span class="num">1</span> 算法原理</h2>
    <p>快速排序是一种高效的<strong>分治</strong>排序算法：<strong>选基准（pivot）→ 划分（左边≤基准，右边≥基准）→ 递归处理左右两部分</strong>。</p>
    <p>时间复杂度：<strong>O(n log n)</strong>（最坏 O(n²)），空间复杂度：<strong>O(log n)</strong>，是<strong>不稳定</strong>的排序算法。</p>
  </div>

  <div class="section">
    <h2><span class="num">2</span> 测试数据</h2>
    <p>使用10个商品数据，按价格排序：</p>
    <table class="data-table">
      <thead><tr><th>索引</th><th>品牌</th><th>型号</th><th>评论数</th><th>价格</th></tr></thead>
      <tbody id="dataTbody"></tbody>
    </table>
  </div>

  <div class="section">
    <h2><span class="num">3</span> Java代码实现</h2>
    <div class="code-block">
      <button class="copy-btn" onclick="copyCode(this)">复制</button>
      <pre><span class="comment">// 快速排序  时间: O(nlogn)  空间: O(logn)  稳定: 否</span>
<span class="keyword">public void</span> <span class="type">quickSort</span>() {{{
    quickSort(0, r.length - 1);
}}
<span class="keyword">private void</span> <span class="type">quickSort</span>(<span class="keyword">int</span> low, <span class="keyword">int</span> high) {{{
    <span class="keyword">int</span> pivot = r[low].price;
    <span class="keyword">int</span> i = low + 1, j = high;
    Product tmp;
    <span class="keyword">while</span> (i &lt; j) {{{
        <span class="keyword">while</span> ((j &gt; i) &amp;&amp; (pivot &lt;= r[j].price)) --j;
        <span class="keyword">while</span> ((i &lt; j) &amp;&amp; (pivot &gt;= r[i].price)) ++i;
        <span class="keyword">if</span> (i &lt; j) {{{
            tmp = r[i]; r[i] = r[j]; r[j] = tmp;
        }}}
    }}}
    <span class="keyword">if</span> (r[j].price &lt; r[low].price) {{{
        tmp = r[low]; r[low] = r[j]; r[j] = tmp;
    }}}
    <span class="keyword">if</span> (i - low &gt; 1) quickSort(low, i - 1);
    <span class="keyword">if</span> (high - j &gt; 1) quickSort(j + 1, high);
}}}</pre>
    </div>
    <ul>
      <li>基准选择区间第一个元素</li>
      <li>i 从 low+1 向右，j 从 high 向左，双指针同时移动</li>
      <li>退出外层 while 后，需要将基准放到正确位置</li>
    </ul>
  </div>

  <div class="section">
    <h2><span class="num">4</span> 逐步执行演示</h2>
    <div class="viz">
      <div class="viz-controls">
        <button class="viz-btn primary" onclick="step()">&#9654; 单步执行</button>
        <button class="viz-btn" onclick="reset()">&#8635; 重置</button>
        <button class="viz-btn" onclick="toggleAuto()" id="autoBtn">&#9658; 自动播放</button>
        <select class="speed-select" id="speedSelect">
          <option value="800">快速</option>
          <option value="400" selected>中速</option>
          <option value="150">慢速</option>
        </select>
      </div>
      <div class="viz-info" id="vizInfo">点击"单步执行"开始</div>
      <div class="viz-array" id="vizArray"></div>
      <div class="viz-progress"><div class="viz-progress-bar" id="progressBar"></div></div>
      <div class="viz-log" id="logBox"></div>
    </div>
  </div>

  <div class="section">
    <h2><span class="num">5</span> 实操练习</h2>
    <div class="exercise">
      <div class="q-text"><span class="q-num">1.</span> 快速排序中，基准（pivot）的选择规则是（ ）。</div>
      <label><input type="radio" name="q1" value="a"> A. 随机选择一个元素</label>
      <label><input type="radio" name="q1" value="b"> B. 选择区间的第一个元素</label>
      <label><input type="radio" name="q1" value="c"> C. 选择区间的最后一个元素</label>
      <label><input type="radio" name="q1" value="d"> D. 选择区间的中点元素</label>
      <button class="check-btn" onclick="checkAnswer('q1','b',this)">检查答案</button>
      <div class="result" id="result_q1"></div>
    </div>
    <div class="exercise">
      <div class="q-text"><span class="q-num">2.</span> 快速排序的递归终止条件是什么？</div>
      <label><input type="radio" name="q2" value="a"> A. low == high</label>
      <label><input type="radio" name="q2" value="b"> B. i - low &gt; 1 或 high - j &gt; 1（区间长度大于1）</label>
      <label><input type="radio" name="q2" value="c"> C. r[j].price == pivot</label>
      <button class="check-btn" onclick="checkAnswer('q2','b',this)">检查答案</button>
      <div class="result" id="result_q2"></div>
    </div>
    <div class="hint">
      <h4>&#128161; 提示</h4>
      <p>快速排序的平均时间复杂度是 O(n log n)，但在最坏情况下（数组已有序）会退化到 O(n²)。选择好的 pivot 策略（如三数取中）可以避免最坏情况。</p>
    </div>
  </div>
"""

TASK6_JS = """
// ============ 快速排序可视化 ============
let state6 = {};
let timer6 = null;
let running6 = false;

function reset(){{{
  if(timer6){{ clearTimeout(timer6); timer6 = null; }}
  running6 = false;
  const btn = document.getElementById('autoBtn');
  if(btn) btn.textContent = '▶ 自动播放';
  state6 = {{
    arr: PRODUCTS.map(p => {{{...p}}}),
    stack: [{{ low: 0, high: PRODUCTS.length-1 }}],
    phase: 'partition',
    low: 0, high: PRODUCTS.length-1,
    i: 0, j: 0, pivot: 0,
    tmp: null, sorted: [],
    stepCount: 0
  }};
  document.getElementById('logBox').innerHTML = '';
  updateProgress(0);
  log('初始数组: ' + state6.arr.map(p=>p.price).join(', '));
  updateInfo();
  renderArray({{}});
}}

function step(){{{
  const s = state6;
  if(s.stack.length === 0){{{
    log('排序完成!', 'ok');
    renderArray({{ sorted: s.arr.map((_,i)=>i) }});
    updateProgress(100);
    return;
  }}
  if(s.phase === 'partition'){{{
    const ctx = s.stack.pop();
    s.low = ctx.low; s.high = ctx.high;
    if(s.low >= s.high){{ step(); return; }}
    s.pivot = s.arr[s.low].price;
    s.i = s.low + 1; s.j = s.high;
    log(`--- 区间 [${{s.low}}, ${{s.high}}] pivot=${{s.pivot}} ---`);
    s.phase = 'scan';
    updateInfo();
    renderArray({{ pivot: [s.low], sorted: s.sorted }});
    s.stepCount++;
    return;
  }}
  if(s.phase === 'scan'){{{
    if(s.i >= s.j){{{
      s.phase = 'placePivot';
      step();
      return;
    }}
    // j 向左
    if(s.arr[s.j].price < s.pivot){{{
      s.phase = 'placeI';
      step();
      return;
    }}
    s.j--;
    renderArray({{ pivot: [s.low], comparing: [s.j], sorted: s.sorted }});
    s.stepCount++;
    return;
  }}
  if(s.phase === 'placeI'){{{
    if(s.arr[s.i].price > s.pivot){{{
      s.phase = 'swap';
      step();
      return;
    }}
    s.i++;
    renderArray({{ pivot: [s.low], comparing: [s.i], sorted: s.sorted }});
    s.stepCount++;
    return;
  }}
  if(s.phase === 'swap'){{{
    log(`交换 r[${{s.i}}]=${{s.arr[s.i].price}} 和 r[${{s.j}}]=${{s.arr[s.j].price}}`);
    const tmp = {{{...s.arr[s.i]}}};
    s.arr[s.i] = {{{...s.arr[s.j]}}};
    s.arr[s.j] = tmp;
    s.i++; s.j--;
    renderArray({{ swapping: [s.i-1, s.j+1], pivot: [s.low], sorted: s.sorted }});
    s.phase = 'scan';
    s.stepCount++;
    return;
  }}
  if(s.phase === 'placePivot'){{{
    if(s.arr[s.j].price < s.arr[s.low].price){{{
      log(`交换 pivot 和 r[${{s.j}}]`);
      const tmp = {{{...s.arr[s.low]}}};
      s.arr[s.low] = {{{...s.arr[s.j]}}};
      s.arr[s.j] = tmp;
    }}} else {{{
      log('pivot 已在正确位置');
    }}}
    s.sorted.push(s.j);
    updateProgress(Math.round(s.sorted.length / s.arr.length * 100));
    if(s.low < s.j-1) s.stack.push({{ low: s.low, high: s.j-1 }});
    if(s.j+1 < s.high) s.stack.push({{ low: s.j+1, high: s.high }});
    s.phase = 'partition';
    step();
    return;
  }}
}}

function toggleAuto(){{{
  if(running6){{{
    running6 = false;
    if(timer6){{ clearTimeout(timer6); timer6 = null; }}
    const btn = document.getElementById('autoBtn');
    if(btn) btn.textContent = '▶ 自动播放';
    return;
  }}}
  running6 = true;
  const btn = document.getElementById('autoBtn');
  if(btn) btn.textContent = '⏸ 暂停';
  autoStep();
}}

function autoStep(){{{
  if(!running6 || state6.stack.length === 0){{{
    running6 = false;
    const btn = document.getElementById('autoBtn');
    if(btn) btn.textContent = '▶ 自动播放';
    return;
  }}}
  step();
  const speed = parseInt(document.getElementById('speedSelect').value);
  timer6 = setTimeout(autoStep, speed);
}}

function updateInfo(){{{
  const s = state6;
  const el = document.getElementById('vizInfo');
  if(s.stack.length === 0) el.textContent = '排序完成!';
  else if(s.phase === 'partition') el.textContent = '准备划分...';
  else el.textContent = `区间 [${{s.low}},${{s.high}}] pivot=${{s.pivot}}`;
}}}

function renderArray(hl){{{
  const container = document.getElementById('vizArray');
  container.innerHTML = '';
  state6.arr.forEach((item, i) => {{
    const cell = document.createElement('div');
    cell.className = 'arr-cell';
    if(hl.comparing && hl.comparing.includes(i)) cell.classList.add('comparing');
    if(hl.swapping && hl.swapping.includes(i)) cell.classList.add('swapping');
    if(hl.sorted && hl.sorted.includes(i)) cell.classList.add('sorted');
    if(hl.pivot && hl.pivot.includes(i)) cell.classList.add('pivot');
    cell.innerHTML = `<span class="price">${{item.price}}</span><span class="brand">${{item.brand.slice(0,4)}}</span><span class="idx">${{i}}</span>`;
    container.appendChild(cell);
  }});
  updateInfo();
}}}

function updateProgress(pct){{{
  const bar = document.getElementById('progressBar');
  if(bar) bar.style.width = pct + '%';
}}}

function log(msg, type){{{
  const box = document.getElementById('logBox');
  if(!box) return;
  const div = document.createElement('div');
  div.className = 'log-line';
  const cls = type==='ok' ? 'log-ok' : type==='op' ? 'log-op' : 'log-info';
  div.innerHTML = `<span class="${{cls}}">${{msg}}</span>`;
  box.appendChild(div);
  box.scrollTop = box.scrollHeight;
}}}

reset();
"""

# ========== Task 7: 归并与基数排序 ==========
TASK7_CONTENT = """
  <div class="section">
    <h2><span class="num">1</span> 归并排序原理</h2>
    <p>归并排序采用<strong>分治</strong>策略：先将数组分成两半，分别排序后再合并成一个有序数组。</p>
    <p>关键操作：<strong>两路归并</strong>——将两个有序数组合并为一个有序数组。</p>
    <p>时间复杂度：<strong>O(n log n)</strong>，空间复杂度：<strong>O(n)</strong>，是<strong>稳定</strong>的排序算法。</p>
  </div>

  <div class="section">
    <h2><span class="num">2</span> 归并排序 Java代码</h2>
    <div class="code-block">
      <button class="copy-btn" onclick="copyCode(this)">复制</button>
      <pre><span class="comment">// 归并排序  时间: O(nlogn)  空间: O(n)  稳定: 是</span>
<span class="keyword">public void</span> <span class="type">mergeSort</span>() {{{
    <span class="keyword">int</span> k = 1;
    <span class="keyword">while</span> (k &lt; r.length) {{{
        merge(k);
        k *= 2;
    }}}
}}}
<span class="keyword">public void</span> <span class="type">merge</span>(<span class="keyword">int</span> len) {{{
    <span class="keyword">int</span> m = 0, l1 = 0, h1, l2, h2, i, j;
    Product[] tmp = <span class="keyword">new</span> Product[r.length];
    <span class="keyword">while</span> (l1 + len &lt; r.length) {{{
        l2 = l1 + len; h1 = l2 - 1;
        h2 = (l2 + len - 1 &lt; r.length) ? l2 + len - 1 : r.length - 1;
        i = l1; j = l2;
        <span class="keyword">while</span> ((i &lt;= h1) &amp;&amp; (j &lt;= h2)) {{{
            <span class="keyword">if</span> (r[i].price &lt;= r[j].price) tmp[m++] = r[i++];
            <span class="keyword">else</span> tmp[m++] = r[j++];
        }}}
        <span class="keyword">while</span> (i &lt;= h1) tmp[m++] = r[i++];
        <span class="keyword">while</span> (j &lt;= h2) tmp[m++] = r[j++];
        l1 = h2 + 1;
    }}}
    i = l1;
    <span class="keyword">while</span> (i &lt; r.length) tmp[m++] = r[i++];
    <span class="keyword">for</span> (i = 0; i &lt; r.length; ++i) r[i] = tmp[i];
}}}</pre>
    </div>
  </div>

  <div class="section">
    <h2><span class="num">3</span> 基数排序原理</h2>
    <p>基数排序是<strong>多关键字排序</strong>，按照"个位→十位→百位"的顺序逐位分配和收集。</p>
    <p>核心操作：<strong>分配</strong>（按当前位数字放入对应桶）和<strong>收集</strong>（按桶顺序取出所有元素）。</p>
    <p>时间复杂度：<strong>O(d(n+r))</strong>，空间复杂度：<strong>O(n+r)</strong>，是<strong>稳定</strong>的排序算法。</p>
  </div>

  <div class="section">
    <h2><span class="num">4</span> 基数排序 Java代码</h2>
    <div class="code-block">
      <button class="copy-btn" onclick="copyCode(this)">复制</button>
      <pre><span class="comment">// 基数排序  时间: O(d(n+r))  空间: O(n+r)  稳定: 是</span>
<span class="keyword">static class</span> <span class="type">RadixNode</span> {{{
    <span class="keyword">public</span> Product data;
    <span class="keyword">public</span> RadixNode next;
}}}
<span class="keyword">public void</span> <span class="type">radixSort</span>() {{{
    <span class="keyword">int</span> k, power; RadixNode p, q;
    RadixNode[] head = <span class="keyword">new</span> RadixNode[10];
    power = 1;
    <span class="keyword">int</span> max = r[0].price;
    <span class="keyword">for</span> (<span class="keyword">int</span> i = 1; i &lt; r.length; i++) <span class="keyword">if</span>(r[i].price &gt; max) max = r[i].price;
    <span class="keyword">int</span> d = 0; <span class="keyword">while</span>(max &gt; 0) {{ d++; max /= 10; }}
    <span class="keyword">for</span> (<span class="keyword">int</span> i = 0; i &lt; d; i++) {{{
        <span class="keyword">for</span> (<span class="keyword">int</span> j = 0; j &lt; 10; j++) head[j] = <span class="keyword">new</span> RadixNode();
        <span class="keyword">for</span> (<span class="keyword">int</span> j = 0; j &lt; r.length; j++) {{{
            k = Math.floor(r[j].price / power) % 10;
            q = <span class="keyword">new</span> RadixNode(); q.data = r[j]; q.next = null;
            p = head[k].next;
            <span class="keyword">if</span>(p == null) head[k].next = q;
            <span class="keyword">else</span> {{ <span class="keyword">while</span>(p.next != null) p = p.next; p.next = q; }}
        }}}
        <span class="keyword">int</span> l = 0;
        <span class="keyword">for</span> (<span class="keyword">int</span> j = 0; j &lt; 10; j++) {{{
            p = head[j].next;
            <span class="keyword">while</span>(p != null) {{ r[l++] = p.data; p = p.next; }}
        }}}
        power *= 10;
    }}}
}}}</pre>
    </div>
  </div>

  <div class="section">
    <h2><span class="num">5</span> 实操练习</h2>
    <div class="exercise">
      <div class="q-text"><span class="q-num">1.</span> 归并排序和快速排序都是分治策略，它们的主要区别是什么？</div>
      <button class="answer-btn" onclick="toggleAnswer(this)">显示答案</button>
      <div class="answer-box">
        <p><strong>主要区别：</strong></p>
        <ul>
          <li><strong>分的方式</strong>：快速排序就地划分，通过基准划分左右；归并排序对半切分</li>
          <li><strong>治的位置</strong>：快速排序划分后递归处理；归并排序先递归排序，再合并</li>
          <li><strong>空间复杂度</strong>：快速排序 O(log n)，归并排序 O(n)</li>
          <li><strong>稳定性</strong>：快速排序不稳定，归并排序稳定</li>
        </ul>
      </div>
    </div>
    <div class="exercise">
      <div class="q-text"><span class="q-num">2.</span> 基数排序中，为什么要先按低位排序，再按高位排序？</div>
      <button class="answer-btn" onclick="toggleAnswer(this)">显示答案</button>
      <div class="answer-box">
        <p>基数排序是<strong>稳定</strong>的，所以可以按"低位优先"（LSD）的方式进行多关键字排序。先按个位排序，相等的元素保持原顺序；再按十位排序时，十位相等的元素会保持个位排序的顺序。</p>
      </div>
    </div>
  </div>
"""

TASK7_JS = """
// Task 7 的JS留空 - 归并和基数排序的可视化较复杂，可后续添加
console.log('Task 7: 归并与基数排序 - 页面已加载');
"""

def generate_file(filename, title, content, js_content):
    filepath = os.path.join(BASE_DIR, filename)
    html = TEMPLATE.format(title=title, content=content, js_content=js_content)
    # 处理CSS中的大括号转义（Python .format() 需要双层大括号）
    html = html.replace('{{', '{').replace('}}', '}')
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'已生成: {filepath}')

if __name__ == '__main__':
    generate_file('task6.html', 'Task 6：快速排序', TASK6_CONTENT, TASK6_JS)
    generate_file('task7.html', 'Task 7：归并与基数排序', TASK7_CONTENT, TASK7_JS)
    print('完成！')
