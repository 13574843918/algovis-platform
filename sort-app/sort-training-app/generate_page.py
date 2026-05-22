#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成排序实训中心页面"""

output_path = r'C:\Users\admin\WorkBuddy\20260331210244\sort-app\sort-training-app\index.html'

# ========== CSS ==========
css = """<style>
:root{--bg:#0f172a;--surface:#1e293b;--surface2:#263248;--border:#334155;--text:#e2e8f0;--text2:#94a3b8;--accent:#f59e0b;--accent2:#fb923c;--green:#34d399;--red:#f87171;--blue:#60a5fa;--purple:#a78bfa}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Segoe UI',system-ui,sans-serif;background:var(--bg);color:var(--text);min-height:100vh}
nav{background:rgba(15,23,42,.95);border-bottom:1px solid var(--border);position:sticky;top:0;z-index:100;backdrop-filter:blur(8px)}
.nav-inner{max-width:1200px;margin:0 auto;display:flex;align-items:center;gap:2px;padding:0 1rem;overflow-x:auto}
.nav-link{padding:.7rem 1rem;border:none;background:none;color:var(--text2);font-size:.85rem;white-space:nowrap;border-bottom:2px solid transparent;transition:all .2s;font-family:inherit;text-decoration:none;display:inline-block}
.nav-link:hover{color:var(--text);background:rgba(255,255,255,.05)}
.nav-link.active,.nav-link.current{color:var(--accent);border-bottom-color:var(--accent)}
.nav-link.current{background:rgba(245,158,11,.15);border:1px solid rgba(245,158,11,.4);border-radius:6px;margin:4px 2px}
.nav-home{margin-left:auto;padding:.5rem .9rem;background:rgba(245,158,11,.1);border:1px solid rgba(245,158,11,.3);border-radius:6px;color:var(--accent);text-decoration:none;font-size:.82rem;white-space:nowrap;transition:all .2s}
.nav-home:hover{background:rgba(245,158,11,.2)}
.hero{background:linear-gradient(135deg,#1a0f02 0%,#0f172a 50%,#1a0a02 100%);padding:2.5rem 1.5rem;text-align:center;border-bottom:1px solid var(--border);position:relative;overflow:hidden}
.hero::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse 60% 40% at 50% 50%,rgba(245,158,11,.08) 0%,transparent 70%)}
.hero h1{font-size:2rem;font-weight:700;background:linear-gradient(135deg,var(--accent),var(--accent2));-webkit-background-clip:text;-webkit-text-fill-color:transparent;position:relative}
.hero p{color:var(--text2);margin-top:.5rem;font-size:.95rem;position:relative}
.hero-badges{display:flex;gap:.5rem;justify-content:center;margin-top:1rem;flex-wrap:wrap;position:relative}
.badge{padding:.3rem .8rem;border-radius:20px;font-size:.75rem;font-weight:600;border:1px solid}
.badge-gold{background:rgba(245,158,11,.1);color:var(--accent);border-color:rgba(245,158,11,.3)}
.badge-green{background:rgba(52,211,153,.1);color:var(--green);border-color:rgba(52,211,153,.3)}
.badge-blue{background:rgba(96,165,250,.1);color:var(--blue);border-color:rgba(96,165,250,.3)}
.container{max-width:1200px;margin:0 auto;padding:1.5rem 1rem}
.task-overview{background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:1.5rem;margin-bottom:1.5rem}
.task-overview h2{color:var(--accent);font-size:1.1rem;margin-bottom:1rem}
.task-list-wrap{display:flex;flex-direction:column;gap:.6rem}
.task-item{background:var(--surface2);border:1px solid var(--border);border-radius:10px;overflow:hidden;transition:all .2s}
.task-item[open]{border-color:var(--accent)}
.task-item summary{display:flex;align-items:center;justify-content:space-between;padding:1rem 1.2rem;cursor:pointer;list-style:none;user-select:none;transition:background .2s}
.task-item summary::-webkit-details-marker{display:none}
.task-item summary:hover{background:rgba(255,255,255,.04)}
.task-item[open] summary{background:rgba(245,158,11,.08)}
.task-sum-left{display:flex;align-items:center;gap:.8rem}
.task-sum-left h3{color:var(--accent);font-size:.95rem;font-weight:600}
.task-sum-arrow{color:var(--text2);font-size:.9rem;transition:transform .3s;margin-left:auto}
.task-item[open] .task-sum-arrow{transform:rotate(180deg)}
.task-item-body{padding:.8rem 1.2rem 1.2rem;border-top:1px solid var(--border)}
.task-item-body p{color:var(--text2);font-size:.85rem;line-height:1.6;margin-bottom:.8rem}
.tag-basic{background:rgba(52,211,153,.15);color:var(--green);padding:.15rem .5rem;border-radius:10px;font-size:.7rem}
.tag-adv{background:rgba(96,165,250,.15);color:var(--blue);padding:.15rem .5rem;border-radius:10px;font-size:.7rem}
.tag-pro{background:rgba(167,139,250,.15);color:var(--purple);padding:.15rem .5rem;border-radius:10px;font-size:.7rem}
.task-detail{display:none}
.task-detail.active{display:block}
.back-btn{display:inline-flex;align-items:center;gap:.4rem;padding:.5rem 1rem;background:var(--surface);border:1px solid var(--border);border-radius:8px;color:var(--text2);text-decoration:none;font-size:.85rem;cursor:pointer;margin-bottom:1rem;transition:all .2s}
.back-btn:hover{border-color:var(--accent);color:var(--accent)}
.task-section{background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:1.5rem;margin-bottom:1.2rem}
.task-section h3{color:var(--accent);font-size:1rem;margin-bottom:1rem;display:flex;align-items:center;gap:.5rem}
.task-section h3 .num{width:24px;height:24px;border-radius:50%;background:rgba(245,158,11,.15);border:1px solid rgba(245,158,11,.3);color:var(--accent);font-size:.75rem;display:flex;align-items:center;justify-content:center}
.task-section p{color:var(--text2);font-size:.88rem;line-height:1.7;margin-bottom:.8rem}
.task-section p strong{color:var(--text)}
.task-section ul{margin:.5rem 0 .8rem 1.2rem}
.task-section li{color:var(--text2);font-size:.88rem;line-height:1.7;margin-bottom:.3rem}
.task-section li strong{color:var(--text)}
.code-block{background:#0d1117;border:1px solid var(--border);border-radius:8px;padding:1rem;margin:.8rem 0;overflow-x:auto;position:relative}
.code-block pre{font-family:'Consolas','Monaco',monospace;font-size:.82rem;line-height:1.7;color:#c9d1d9;white-space:pre}
.code-block .keyword{color:#ff7b72}
.code-block .type{color:#79c0ff}
.code-block .comment{color:#8b949e;font-style:italic}
.code-block .num-literal{color:#f0883e}
.copy-btn{position:absolute;top:.5rem;right:.5rem;padding:.3rem .6rem;background:rgba(245,158,11,.1);border:1px solid rgba(245,158,11,.3);border-radius:5px;color:var(--accent);font-size:.72rem;cursor:pointer;transition:all .2s}
.copy-btn:hover{background:rgba(245,158,11,.2)}
.viz-section{background:var(--surface2);border:1px solid var(--border);border-radius:10px;padding:1rem;margin:.8rem 0}
.viz-controls{display:flex;gap:.5rem;flex-wrap:wrap;margin-bottom:1rem}
.viz-btn{padding:.4rem 1rem;border:1px solid var(--border);background:var(--surface);color:var(--text2);border-radius:6px;cursor:pointer;font-size:.82rem;transition:all .2s;font-family:inherit}
.viz-btn:hover{border-color:var(--accent);color:var(--accent)}
.viz-btn.primary{background:rgba(245,158,11,.15);border-color:rgba(245,158,11,.4);color:var(--accent)}
.viz-btn:disabled{opacity:.4;cursor:not-allowed}
.viz-array{display:flex;gap:3px;margin:.8rem 0;flex-wrap:wrap}
.arr-cell{min-width:38px;height:44px;display:flex;flex-direction:column;align-items:center;justify-content:center;background:var(--surface);border:2px solid var(--border);border-radius:6px;font-size:.78rem;transition:all .3s}
.arr-cell .price{color:var(--text);font-weight:700;font-size:.85rem}
.arr-cell .brand{color:var(--text2);font-size:.62rem;margin-top:2px}
.arr-cell .idx{font-size:.58rem;color:var(--text2);margin-top:2px}
.arr-cell.comparing{background:rgba(245,158,11,.15);border-color:var(--accent)}
.arr-cell.comparing .price{color:var(--accent)}
.arr-cell.swapping{background:rgba(248,113,113,.15);border-color:var(--red)}
.arr-cell.swapping .price{color:var(--red)}
.arr-cell.sorted{background:rgba(52,211,153,.1);border-color:rgba(52,211,153,.3)}
.arr-cell.sorted .price{color:var(--green)}
.arr-cell.pivot{background:rgba(96,165,250,.15);border-color:rgba(96,165,250,.4)}
.arr-cell.pivot .price{color:var(--blue)}
.arr-cell.heap-root{background:rgba(167,139,250,.15);border-color:rgba(167,139,250,.4)}
.arr-cell.heap-root .price{color:var(--purple)}
.viz-log{background:#0d1117;border:1px solid var(--border);border-radius:6px;padding:.6rem;max-height:150px;overflow-y:auto;font-family:'Consolas',monospace;font-size:.78rem;color:#8b949e;margin-top:.8rem}
.viz-log .log-line{margin-bottom:3px}
.viz-log .log-op{color:#f0883e}
.viz-log .log-info{color:#79c0ff}
.viz-log .log-ok{color:#34d399}
.viz-progress{height:4px;background:var(--border);border-radius:2px;margin:.5rem 0}
.viz-progress-bar{height:100%;background:linear-gradient(90deg,var(--accent),var(--accent2));border-radius:2px;transition:width .3s;width:0%}
.data-table{width:100%;border-collapse:collapse;margin:.8rem 0;font-size:.85rem}
.data-table th{background:rgba(245,158,11,.1);color:var(--accent);padding:.5rem .8rem;text-align:left;border:1px solid rgba(245,158,11,.2);font-weight:600}
.data-table td{padding:.4rem .8rem;border:1px solid var(--border);color:var(--text2)}
.exercise-item{background:var(--surface2);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1rem}
.exercise-item .q-text{font-size:.9rem;color:var(--text);margin-bottom:.8rem;line-height:1.6}
.exercise-item .q-num{color:var(--accent);font-weight:700;margin-right:.4rem}
.exercise-item label{display:flex;align-items:flex-start;gap:.5rem;padding:.4rem .6rem;border-radius:6px;cursor:pointer;font-size:.85rem;color:var(--text2);transition:all .2s;margin:.2rem 0}
.exercise-item label:hover{background:rgba(245,158,11,.06);color:var(--text)}
.exercise-item input[type=radio]{accent-color:var(--accent);flex-shrink:0;margin-top:.15rem}
.exercise-item label.correct{background:rgba(52,211,153,.1);color:var(--green);border-radius:6px}
.exercise-item label.wrong{background:rgba(248,113,113,.1);color:var(--red);border-radius:6px}
.check-btn{padding:.5rem 1.5rem;background:rgba(245,158,11,.15);border:1px solid rgba(245,158,11,.4);border-radius:8px;color:var(--accent);font-size:.85rem;cursor:pointer;margin-top:.8rem;transition:all .2s;font-family:inherit}
.check-btn:hover{background:rgba(245,158,11,.25)}
.exercise-item .result{margin-top:.8rem;padding:.6rem 1rem;border-radius:6px;font-size:.85rem;display:none}
.exercise-item .result.show{display:block}
.result.pass{background:rgba(52,211,153,.1);border:1px solid rgba(52,211,153,.3);color:var(--green)}
.result.fail{background:rgba(248,113,113,.1);border:1px solid rgba(248,113,113,.3);color:var(--red)}
.answer-btn{padding:.4rem 1rem;background:var(--surface2);border:1px solid var(--border);border-radius:6px;color:var(--text2);font-size:.8rem;cursor:pointer;margin-top:.5rem;transition:all .2s;font-family:inherit}
.answer-btn:hover{border-color:var(--purple);color:var(--purple)}
.answer-box{display:none;background:rgba(167,139,250,.08);border:1px solid rgba(167,139,250,.2);border-radius:8px;padding:.8rem 1rem;margin-top:.5rem;font-size:.85rem;color:var(--purple)}
.answer-box.show{display:block}
@media(max-width:600px){.hero h1{font-size:1.4rem}.nav-inner{padding:.3rem .5rem}.nav-link{padding:.5rem .5rem;font-size:.75rem}}
</style>
"""

# ========== HTML 模板 ==========
html = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>排序实训 | AlgoVis</title>
""" + css + """
</head>
<body>
<nav>
  <div class="nav-inner">
    <a class="nav-link" href="../index.html?tab=guide">&#128218; 导读</a>
    <a class="nav-link" href="../index.html?tab=simulator">&#127918; 模拟器</a>
    <a class="nav-link" href="../index.html?tab=operations">&#128736; 基本操作</a>
    <a class="nav-link" href="../index.html?tab=theory">&#128218; 理论知识</a>
    <a class="nav-link" href="../index.html?tab=exercises">&#9997; 练习题</a>
    <a class="nav-link current">&#128187; 实训</a>
    <a class="nav-home" href="../index.html">&#127968; 返回首页</a>
  </div>
</nav>

<div class="hero">
  <h1>&#127941; 排序实训中心</h1>
  <p>通过7个递进任务，深入掌握8种排序算法的核心原理与Java实现</p>
  <div class="hero-badges">
    <span class="badge badge-gold">7个实训任务</span>
    <span class="badge badge-green">10个商品数据</span>
    <span class="badge badge-blue">完整Java代码</span>
  </div>
</div>

<div class="container">
"""

# ========== 任务列表 ==========
task_list = """
<!-- ==================== 任务列表 ==================== -->
<div id="task-list" class="task-overview">
  <h2>&#128194; 选择实训任务（点击展开）</h2>
  <div class="task-list-wrap">

    <details class="task-item">
      <summary>
        <div class="task-sum-left">
          <h3>Task 1：直接插入排序</h3>
          <span class="tag-basic">基础</span>
        </div>
        <span class="task-sum-arrow">&#9660;</span>
      </summary>
      <div class="task-item-body">
        <p>理解哨兵思想，掌握有序区逐步扩展的核心原理。将无序区第一个元素插入有序区的正确位置。</p>
        <button class="viz-btn primary" onclick="showTask(1)">开始实训 &#8594;</button>
      </div>
    </details>

    <details class="task-item">
      <summary>
        <div class="task-sum-left">
          <h3>Task 2：希尔排序</h3>
          <span class="tag-basic">基础</span>
        </div>
        <span class="task-sum-arrow">&#9660;</span>
      </summary>
      <div class="task-item-body">
        <p>理解增量序列设计，掌握分组插入排序的分层优化思想。增量从大到小逐步缩减至 1。</p>
        <button class="viz-btn primary" onclick="showTask(2)">开始实训 &#8594;</button>
      </div>
    </details>

    <details class="task-item">
      <summary>
        <div class="task-sum-left">
          <h3>Task 3：直接选择排序</h3>
          <span class="tag-basic">基础</span>
        </div>
        <span class="task-sum-arrow">&#9660;</span>
      </summary>
      <div class="task-item-body">
        <p>理解简单直接的选择策略，掌握最小值查找与交换。每轮从无序区中找出最小值放到有序区末尾。</p>
        <button class="viz-btn primary" onclick="showTask(3)">开始实训 &#8594;</button>
      </div>
    </details>

    <details class="task-item">
      <summary>
        <div class="task-sum-left">
          <h3>Task 4：堆排序</h3>
          <span class="tag-adv">进阶</span>
        </div>
        <span class="task-sum-arrow">&#9660;</span>
      </summary>
      <div class="task-item-body">
        <p>理解大根堆性质，掌握建堆(createHeap)与堆调整的核心算法。利用堆结构实现 O(n log n) 的排序。</p>
        <button class="viz-btn primary" onclick="showTask(4)">开始实训 &#8594;</button>
      </div>
    </details>

    <details class="task-item">
      <summary>
        <div class="task-sum-left">
          <h3>Task 5：冒泡排序</h3>
          <span class="tag-basic">基础</span>
        </div>
        <span class="task-sum-arrow">&#9660;</span>
      </summary>
      <div class="task-item-body">
        <p>理解相邻比较交换，掌握提前终止优化的实现。若某趟没有发生交换，则说明数组已有序，提前结束。</p>
        <button class="viz-btn primary" onclick="showTask(5)">开始实训 &#8594;</button>
      </div>
    </details>

    <details class="task-item">
      <summary>
        <div class="task-sum-left">
          <h3>Task 6：快速排序</h3>
          <span class="tag-adv">进阶</span>
        </div>
        <span class="task-sum-arrow">&#9660;</span>
      </summary>
      <div class="task-item-body">
        <p>理解基准 pivot 选取，掌握递归分治策略与边界处理。通过分区使左侧均小于 pivot、右侧均大于 pivot。</p>
        <button class="viz-btn primary" onclick="showTask(6)">开始实训 &#8594;</button>
      </div>
    </details>

    <details class="task-item">
      <summary>
        <div class="task-sum-left">
          <h3>Task 7：归并与基数排序</h3>
          <span class="tag-pro">综合</span>
        </div>
        <span class="task-sum-arrow">&#9660;</span>
      </summary>
      <div class="task-item-body">
        <p>掌握两路归并的合并操作；理解按位分配收集的多关键字排序。归并稳定 O(n log n)，基数稳定 O(d·n)。</p>
        <button class="viz-btn primary" onclick="showTask(7)">开始实训 &#8594;</button>
      </div>
    </details>

  </div>
</div>
"""

html += task_list

# ========== 任务1: 插入排序 ==========
task1 = """
<!-- ==================== TASK 1: 插入排序 ==================== -->
<div id="task-1" class="task-detail">
  <a class="back-btn" onclick="showTaskList()">&#8592; 返回任务列表</a>
  <div class="task-section">
    <h3><span class="num">1</span> 算法原理</h3>
    <p>直接插入排序（Insert Sort）核心思想：<strong>将数组分为"有序区"和"无序区"，每次取无序区第一个元素，在有序区从后向前查找插入位置</strong>。</p>
    <p>将待插入元素缓存到临时变量 <code>tmp</code> 中，然后在循环中移动元素，最后将 <code>tmp</code> 插入到正确位置。</p>
    <p>时间复杂度：<strong>O(n²)</strong>，空间复杂度：<strong>O(1)</strong>，是<strong>稳定</strong>的排序算法。</p>
  </div>
  <div class="task-section">
    <h3><span class="num">2</span> 测试数据</h3>
    <p>使用10个商品数据，按价格排序：</p>
    <table class="data-table"><thead><tr><th>索引</th><th>品牌</th><th>型号</th><th>评论数</th><th>价格</th></tr></thead>
    <tbody id="data-1"></tbody></table>
  </div>
  <div class="task-section">
    <h3><span class="num">3</span> Java代码实现</h3>
    <div class="code-block">
      <button class="copy-btn" onclick="copyCode(this)">复制</button>
      <pre><span class="comment">/** 直接插入排序 时间复杂度: O(n2) 空间: O(1) 稳定: 是 */</span>
<span class="keyword">public void</span> <span class="type">insertSort</span>() {
    <span class="keyword">for</span> (<span class="keyword">int</span> i = <span class="num-literal">1</span>; i &lt; r.length; i++) {
        <span class="keyword">if</span> (r[i].price &lt; r[i - <span class="num-literal">1</span>].price) {
            Product tmp = r[i];
            <span class="keyword">int</span> j = <span class="num-literal">0</span>;
            <span class="keyword">for</span> (j = i - <span class="num-literal">1</span>; j &gt;= <span class="num-literal">0</span> &amp;&amp; tmp.price &lt; r[j].price; j--) {
                r[j + <span class="num-literal">1</span>] = r[j];
            }
            r[j + <span class="num-literal">1</span>] = tmp;
        }
    }
}</pre>
    </div>
    <p><strong>关键点：</strong></p>
    <ul>
      <li>只有当 <code>r[i].price &lt; r[i-1].price</code> 时才需要插入</li>
      <li>循环条件 <code>j &gt;= 0 &amp;&amp; tmp.price &lt; r[j].price</code></li>
      <li>插入位置是 <code>j+1</code></li>
    </ul>
  </div>
  <div class="task-section">
    <h3><span class="num">4</span> 逐步执行演示</h3>
    <div class="viz-section">
      <div class="viz-controls">
        <button class="viz-btn primary" onclick="insertSort_step(1)">&#9654; 单步执行</button>
        <button class="viz-btn" onclick="insertSort_reset(1)">&#8635; 重置</button>
        <button class="viz-btn" onclick="insertSort_auto(1)" id="auto-btn-1">&#9658; 自动播放</button>
        <select id="speed-1" style="padding:.4rem;border-radius:6px;border:1px solid var(--border);background:var(--surface);color:var(--text2);font-size:.82rem;">
          <option value="800">快速</option><option value="400" selected>中速</option><option value="150">慢速</option>
        </select>
      </div>
      <div class="viz-array" id="viz-1"></div>
      <div class="viz-progress"><div class="viz-progress-bar" id="prog-1"></div></div>
      <div class="viz-log" id="log-1"></div>
    </div>
  </div>
  <div class="task-section">
    <h3><span class="num">5</span> 实操练习</h3>
    <div class="exercise-item">
      <div class="q-text"><span class="q-num">1.</span> 在直接插入排序中，内层循环的退出条件是（ ）。</div>
      <label><input type="radio" name="q1_1" value="a"> A. j &lt; 0</label>
      <label><input type="radio" name="q1_1" value="b"> B. j &gt;= 0 且 tmp.price &lt; r[j].price</label>
      <label><input type="radio" name="q1_1" value="c"> C. tmp.price &gt;= r[j].price</label>
      <label><input type="radio" name="q1_1" value="d"> D. j &lt; i</label>
      <button class="check-btn" onclick="checkRadio(this,'b','q1_1')">检查答案</button>
      <div class="result" id="result-q1_1"></div>
    </div>
    <div class="exercise-item">
      <div class="q-text"><span class="q-num">2.</span> 直接插入排序是稳定的排序算法吗？为什么？</div>
      <button class="answer-btn" onclick="toggleAnswer(this.nextElementSibling)">显示答案</button>
      <div class="answer-box">
        <p><strong>是稳定排序。</strong>因为算法只进行"&lt;"比较，当 <code>tmp.price == r[j].price</code> 时不满足 <code>tmp.price &lt; r[j].price</code>，循环终止，tmp 插入到相等元素之后，不改变相等元素的相对顺序。</p>
      </div>
    </div>
  </div>
</div>
"""

html += task1

# ========== 任务2-7（简化版） ==========
# 任务2
task2 = """
<!-- ==================== TASK 2: 希尔排序 ==================== -->
<div id="task-2" class="task-detail">
  <a class="back-btn" onclick="showTaskList()">&#8592; 返回任务列表</a>
  <div class="task-section">
    <h3><span class="num">1</span> 算法原理</h3>
    <p>希尔排序（Shell Sort）是插入排序的改进版，核心思想：<strong>设置增量序列 d，将数组按间隔 d 分成若干组，对每组进行直接插入排序；然后缩小增量，重复上述过程，直到增量 d=1</strong>。</p>
    <p>时间复杂度：<strong>O(n^1.3~1.5)</strong>，空间复杂度：<strong>O(1)</strong>，是<strong>不稳定</strong>的排序算法。</p>
  </div>
  <div class="task-section">
    <h3><span class="num">2</span> 测试数据</h3>
    <table class="data-table"><thead><tr><th>索引</th><th>品牌</th><th>型号</th><th>评论数</th><th>价格</th></tr></thead>
    <tbody id="data-2"></tbody></table>
  </div>
  <div class="task-section">
    <h3><span class="num">3</span> Java代码实现</h3>
    <div class="code-block">
      <button class="copy-btn" onclick="copyCode(this)">复制</button>
      <pre><span class="comment">/** 希尔排序 时间复杂度: O(n^1.3~1.5) 空间: O(1) 稳定: 否 */</span>
<span class="keyword">public void</span> <span class="type">shellSort</span>() {
    <span class="keyword">int</span> i, j, d; Product tmp;
    <span class="keyword">int</span> increment = r.length / <span class="num-literal">3</span>;
    <span class="keyword">for</span> (<span class="keyword">int</span> m = increment; m &gt;= <span class="num-literal">1</span>; m--) {
        d = m;
        <span class="keyword">for</span> (i = d; i &lt; r.length; i++) {
            <span class="keyword">if</span> (r[i].price &lt; r[i - d].price) {
                tmp = r[i]; j = i;
                <span class="keyword">do</span> {
                    r[j] = r[j - d]; j = j - d;
                    <span class="keyword">if</span> (j - d &lt; <span class="num-literal">0</span>) <span class="keyword">break</span>;
                } <span class="keyword">while</span> (j &gt; <span class="num-literal">0</span> &amp;&amp; tmp.price &lt; r[j - d].price);
                r[j] = tmp;
            }
        }
    }
}</pre>
    </div>
  </div>
  <div class="task-section">
    <h3><span class="num">4</span> 逐步执行演示</h3>
    <div class="viz-section">
      <div class="viz-controls">
        <button class="viz-btn primary" onclick="shellSort_step(2)">&#9654; 单步执行</button>
        <button class="viz-btn" onclick="shellSort_reset(2)">&#8635; 重置</button>
        <button class="viz-btn" onclick="shellSort_auto(2)" id="auto-btn-2">&#9658; 自动播放</button>
        <select id="speed-2" style="padding:.4rem;border-radius:6px;border:1px solid var(--border);background:var(--surface);color:var(--text2);font-size:.82rem;">
          <option value="800">快速</option><option value="400" selected>中速</option><option value="150">慢速</option>
        </select>
      </div>
      <div style="font-size:.78rem;color:var(--text2);margin-bottom:.5rem;" id="shell-phase-2">当前增量 d = ?</div>
      <div class="viz-array" id="viz-2"></div>
      <div class="viz-progress"><div class="viz-progress-bar" id="prog-2"></div></div>
      <div class="viz-log" id="log-2"></div>
    </div>
  </div>
  <div class="task-section">
    <h3><span class="num">5</span> 实操练习</h3>
    <div class="exercise-item">
      <div class="q-text"><span class="q-num">1.</span> 希尔排序是稳定的排序算法吗？为什么？</div>
      <label><input type="radio" name="q2_1" value="a"> A. 稳定，因为是基于插入排序</label>
      <label><input type="radio" name="q2_1" value="b"> B. 不稳定，因为间隔跳跃可能改变相等元素的相对顺序</label>
      <button class="check-btn" onclick="checkRadio(this,'b','q2_1')">检查答案</button>
      <div class="result" id="result-q2_1"></div>
    </div>
  </div>
</div>
"""
html += task2

# 任务3-7类似处理...
task3 = """
<!-- ==================== TASK 3: 选择排序 ==================== -->
<div id="task-3" class="task-detail">
  <a class="back-btn" onclick="showTaskList()">&#8592; 返回任务列表</a>
  <div class="task-section">
    <h3><span class="num">1</span> 算法原理</h3>
    <p>直接选择排序（Select Sort）核心思想：<strong>在无序区中找出最小元素，将其与无序区第一个元素交换位置，然后缩小无序区范围</strong>。</p>
    <p>时间复杂度：<strong>O(n2)</strong>，空间复杂度：<strong>O(1)</strong>，是<strong>不稳定</strong>的排序算法。</p>
  </div>
  <div class="task-section">
    <h3><span class="num">2</span> 测试数据</h3>
    <table class="data-table"><thead><tr><th>索引</th><th>品牌</th><th>型号</th><th>评论数</th><th>价格</th></tr></thead>
    <tbody id="data-3"></tbody></table>
  </div>
  <div class="task-section">
    <h3><span class="num">3</span> Java代码实现</h3>
    <div class="code-block">
      <button class="copy-btn" onclick="copyCode(this)">复制</button>
      <pre><span class="comment">/** 直接选择排序 时间复杂度: O(n2) 空间: O(1) 稳定: 否 */</span>
<span class="keyword">public void</span> <span class="type">selectSort</span>() {
    <span class="keyword">int</span> k; Product tmp;
    <span class="keyword">for</span> (<span class="keyword">int</span> i = <span class="num-literal">0</span>; i &lt; r.length - <span class="num-literal">1</span>; i++) {
        k = i;
        <span class="keyword">for</span> (<span class="keyword">int</span> j = i + <span class="num-literal">1</span>; j &lt; r.length; j++) {
            <span class="keyword">if</span> (r[j].price &lt; r[k].price) k = j;
        }
        <span class="keyword">if</span> (k != i) { tmp = r[i]; r[i] = r[k]; r[k] = tmp; }
    }
}</pre>
    </div>
  </div>
  <div class="task-section">
    <h3><span class="num">4</span> 逐步执行演示</h3>
    <div class="viz-section">
      <div class="viz-controls">
        <button class="viz-btn primary" onclick="selectSort_step(3)">&#9654; 单步执行</button>
        <button class="viz-btn" onclick="selectSort_reset(3)">&#8635; 重置</button>
        <button class="viz-btn" onclick="selectSort_auto(3)" id="auto-btn-3">&#9658; 自动播放</button>
        <select id="speed-3" style="padding:.4rem;border-radius:6px;border:1px solid var(--border);background:var(--surface);color:var(--text2);font-size:.82rem;">
          <option value="800">快速</option><option value="400" selected>中速</option><option value="150">慢速</option>
        </select>
      </div>
      <div class="viz-array" id="viz-3"></div>
      <div class="viz-progress"><div class="viz-progress-bar" id="prog-3"></div></div>
      <div class="viz-log" id="log-3"></div>
    </div>
  </div>
  <div class="task-section">
    <h3><span class="num">5</span> 实操练习</h3>
    <div class="exercise-item">
      <div class="q-text"><span class="q-num">1.</span> 选择排序是稳定的排序算法吗？</div>
      <label><input type="radio" name="q3_1" value="a"> A. 稳定</label>
      <label><input type="radio" name="q3_1" value="b"> B. 不稳定</label>
      <button class="check-btn" onclick="checkRadio(this,'b','q3_1')">检查答案</button>
      <div class="result" id="result-q3_1"></div>
    </div>
  </div>
</div>
"""
html += task3

# 任务4
task4 = """
<!-- ==================== TASK 4: 堆排序 ==================== -->
<div id="task-4" class="task-detail">
  <a class="back-btn" onclick="showTaskList()">&#8592; 返回任务列表</a>
  <div class="task-section">
    <h3><span class="num">1</span> 算法原理</h3>
    <p>堆排序基于<strong>大根堆</strong>（父节点大于等于子节点）。分为两个阶段：<strong>建堆</strong>（从最后一个非叶子节点开始调整）和<strong>排序</strong>（交换堆顶与堆尾，重新建堆）。</p>
    <p>时间复杂度：<strong>O(n log n)</strong>，空间复杂度：<strong>O(1)</strong>，是<strong>不稳定</strong>的排序算法。</p>
  </div>
  <div class="task-section">
    <h3><span class="num">2</span> 测试数据</h3>
    <table class="data-table"><thead><tr><th>索引</th><th>品牌</th><th>型号</th><th>评论数</th><th>价格</th></tr></thead>
    <tbody id="data-4"></tbody></table>
  </div>
  <div class="task-section">
    <h3><span class="num">3</span> Java代码实现</h3>
    <div class="code-block">
      <button class="copy-btn" onclick="copyCode(this)">复制</button>
      <pre><span class="comment">/** 堆排序 时间复杂度: O(nlogn) 空间: O(1) 稳定: 否 */</span>
<span class="keyword">public void</span> <span class="type">createHeap</span>(<span class="keyword">int</span> low, <span class="keyword">int</span> high) {
    <span class="keyword">int</span> j, k; Product tmp;
    <span class="keyword">for</span> (<span class="keyword">int</span> i = high/<span class="num-literal">2</span>; i &gt;= low; --i) {
        tmp = r[i]; k = i; j = <span class="num-literal">2</span>*k+<span class="num-literal">1</span>;
        <span class="keyword">while</span> (j &lt;= high) {
            <span class="keyword">if</span> ((j&lt;high) &amp;&amp; (r[j].price&lt;r[j+<span class="num-literal">1</span>].price)) ++j;
            <span class="keyword">if</span> (tmp.price &lt; r[j].price) { r[k]=r[j]; k=j; j=<span class="num-literal">2</span>*k+<span class="num-literal">1</span>; }
            <span class="keyword">else</span> <span class="keyword">break</span>;
        }
        r[k] = tmp;
    }
}
<span class="keyword">public void</span> <span class="type">heapSort</span>() {
    Product tmp;
    createHeap(<span class="num-literal">0</span>, r.length-<span class="num-literal">1</span>);
    <span class="keyword">for</span> (<span class="keyword">int</span> i = r.length-<span class="num-literal">1</span>; i &gt; <span class="num-literal">0</span>; --i) {
        tmp = r[<span class="num-literal">0</span>]; r[<span class="num-literal">0</span>] = r[i]; r[i] = tmp;
        createHeap(<span class="num-literal">0</span>, i-<span class="num-literal">1</span>);
    }
}</pre>
    </div>
  </div>
  <div class="task-section">
    <h3><span class="num">4</span> 逐步执行演示</h3>
    <div class="viz-section">
      <div class="viz-controls">
        <button class="viz-btn primary" onclick="heapSort_step(4)">&#9654; 单步执行</button>
        <button class="viz-btn" onclick="heapSort_reset(4)">&#8635; 重置</button>
        <button class="viz-btn" onclick="heapSort_auto(4)" id="auto-btn-4">&#9658; 自动播放</button>
        <select id="speed-4" style="padding:.4rem;border-radius:6px;border:1px solid var(--border);background:var(--surface);color:var(--text2);font-size:.82rem;">
          <option value="800">快速</option><option value="400" selected>中速</option><option value="150">慢速</option>
        </select>
      </div>
      <div class="viz-array" id="viz-4"></div>
      <div class="viz-progress"><div class="viz-progress-bar" id="prog-4"></div></div>
      <div class="viz-log" id="log-4"></div>
    </div>
  </div>
  <div class="task-section">
    <h3><span class="num">5</span> 实操练习</h3>
    <div class="exercise-item">
      <div class="q-text"><span class="q-num">1.</span> 堆排序建堆时，从哪个节点开始调整？（n为数组长度）</div>
      <label><input type="radio" name="q4_1" value="a"> A. 节点 0</label>
      <label><input type="radio" name="q4_1" value="b"> B. 节点 n/2 - 1</label>
      <label><input type="radio" name="q4_1" value="c"> C. 节点 n-1</label>
      <button class="check-btn" onclick="checkRadio(this,'b','q4_1')">检查答案</button>
      <div class="result" id="result-q4_1"></div>
    </div>
  </div>
</div>
"""
html += task4

# 任务5
task5 = """
<!-- ==================== TASK 5: 冒泡排序 ==================== -->
<div id="task-5" class="task-detail">
  <a class="back-btn" onclick="showTaskList()">&#8592; 返回任务列表</a>
  <div class="task-section">
    <h3><span class="num">1</span> 算法原理</h3>
    <p>冒泡排序从前往后比较相邻元素，如果顺序错误就交换。通过多次遍历，将最大的元素逐步"冒泡"到数组末端。</p>
    <p>教材实现了一个<strong>提前终止优化</strong>：使用 <code>exchange</code> 标志，如果某一轮没有发生任何交换，说明数组已经有序，可以提前结束。</p>
    <p>时间复杂度：<strong>O(n2)</strong>，空间复杂度：<strong>O(1)</strong>，是<strong>稳定</strong>的排序算法。</p>
  </div>
  <div class="task-section">
    <h3><span class="num">2</span> 测试数据</h3>
    <table class="data-table"><thead><tr><th>索引</th><th>品牌</th><th>型号</th><th>评论数</th><th>价格</th></tr></thead>
    <tbody id="data-5"></tbody></table>
  </div>
  <div class="task-section">
    <h3><span class="num">3</span> Java代码实现</h3>
    <div class="code-block">
      <button class="copy-btn" onclick="copyCode(this)">复制</button>
      <pre><span class="comment">/** 冒泡排序（带提前终止优化） 时间: O(n2) 空间: O(1) 稳定: 是 */</span>
<span class="keyword">public void</span> <span class="type">bubbleSort</span>() {
    <span class="keyword">boolean</span> exchange; Product tmp;
    <span class="keyword">int</span> n = r.length;
    <span class="keyword">for</span> (<span class="keyword">int</span> i = <span class="num-literal">1</span>; i &lt; n; i++) {
        exchange = <span class="keyword">false</span>;
        <span class="keyword">for</span> (<span class="keyword">int</span> j = <span class="num-literal">0</span>; j &lt; n-i; j++) {
            <span class="keyword">if</span> (r[j].price &gt; r[j+<span class="num-literal">1</span>].price) {
                tmp = r[j+<span class="num-literal">1</span>]; r[j+<span class="num-literal">1</span>] = r[j]; r[j] = tmp;
                exchange = <span class="keyword">true</span>;
            }
        }
        <span class="keyword">if</span> (!exchange) <span class="keyword">break</span>;
    }
}</pre>
    </div>
  </div>
  <div class="task-section">
    <h3><span class="num">4</span> 逐步执行演示</h3>
    <div class="viz-section">
      <div class="viz-controls">
        <button class="viz-btn primary" onclick="bubbleSort_step(5)">&#9654; 单步执行</button>
        <button class="viz-btn" onclick="bubbleSort_reset(5)">&#8635; 重置</button>
        <button class="viz-btn" onclick="bubbleSort_auto(5)" id="auto-btn-5">&#9658; 自动播放</button>
        <select id="speed-5" style="padding:.4rem;border-radius:6px;border:1px solid var(--border);background:var(--surface);color:var(--text2);font-size:.82rem;">
          <option value="800">快速</option><option value="400" selected>中速</option><option value="150">慢速</option>
        </select>
      </div>
      <div class="viz-array" id="viz-5"></div>
      <div class="viz-progress"><div class="viz-progress-bar" id="prog-5"></div></div>
      <div class="viz-log" id="log-5"></div>
    </div>
  </div>
  <div class="task-section">
    <h3><span class="num">5</span> 实操练习</h3>
    <div class="exercise-item">
      <div class="q-text"><span class="q-num">1.</span> 冒泡排序的提前终止优化作用是什么？</div>
      <button class="answer-btn" onclick="toggleAnswer(this.nextElementSibling)">显示答案</button>
      <div class="answer-box">
        <p>提前终止优化可以减少不必要的比较。当某一轮排序中没有任何交换发生时，说明数组已经有序，可以break提前终止。</p>
      </div>
    </div>
  </div>
</div>
"""
html += task5

# 任务6
task6 = """
<!-- ==================== TASK 6: 快速排序 ==================== -->
<div id="task-6" class="task-detail">
  <a class="back-btn" onclick="showTaskList()">&#8592; 返回任务列表</a>
  <div class="task-section">
    <h3><span class="num">1</span> 算法原理</h3>
    <p>快速排序是一种高效的<strong>分治</strong>排序算法：<strong>选基准（pivot）→ 划分（左边≤基准，右边≥基准）→ 递归处理左右两部分</strong>。</p>
    <p>时间复杂度：<strong>O(n log n)</strong>（最坏 O(n2)），空间复杂度：<strong>O(log n)</strong>，是<strong>不稳定</strong>的排序算法。</p>
  </div>
  <div class="task-section">
    <h3><span class="num">2</span> 测试数据</h3>
    <table class="data-table"><thead><tr><th>索引</th><th>品牌</th><th>型号</th><th>评论数</th><th>价格</th></tr></thead>
    <tbody id="data-6"></tbody></table>
  </div>
  <div class="task-section">
    <h3><span class="num">3</span> Java代码实现</h3>
    <div class="code-block">
      <button class="copy-btn" onclick="copyCode(this)">复制</button>
      <pre><span class="comment">/** 快速排序 时间: O(nlogn) 空间: O(logn) 稳定: 否 */</span>
<span class="keyword">public void</span> <span class="type">quickSort</span>() { quickSort(<span class="num-literal">0</span>, r.length-<span class="num-literal">1</span>); }
<span class="keyword">private void</span> <span class="type">quickSort</span>(<span class="keyword">int</span> low, <span class="keyword">int</span> high) {
    <span class="keyword">int</span> pivot = r[low].price;
    <span class="keyword">int</span> i = low+<span class="num-literal">1</span>, j = high; Product tmp;
    <span class="keyword">while</span> (i &lt; j) {
        <span class="keyword">while</span> ((j&gt;i) &amp;&amp; (pivot &lt;= r[j].price)) --j;
        <span class="keyword">while</span> ((i&lt;j) &amp;&amp; (pivot &gt;= r[i].price)) ++i;
        <span class="keyword">if</span> (i &lt; j) { tmp = r[i]; r[i] = r[j]; r[j] = tmp; }
    }
    <span class="keyword">if</span> (r[j].price &lt; r[low].price) { tmp = r[low]; r[low] = r[j]; r[j] = tmp; }
    <span class="keyword">if</span> (i-low &gt; <span class="num-literal">1</span>) quickSort(low, i-<span class="num-literal">1</span>);
    <span class="keyword">if</span> (high-j &gt; <span class="num-literal">1</span>) quickSort(j+<span class="num-literal">1</span>, high);
}</pre>
    </div>
  </div>
  <div class="task-section">
    <h3><span class="num">4</span> 逐步执行演示</h3>
    <div class="viz-section">
      <div class="viz-controls">
        <button class="viz-btn primary" onclick="quickSort_step(6)">&#9654; 单步执行</button>
        <button class="viz-btn" onclick="quickSort_reset(6)">&#8635; 重置</button>
        <button class="viz-btn" onclick="quickSort_auto(6)" id="auto-btn-6">&#9658; 自动播放</button>
        <select id="speed-6" style="padding:.4rem;border-radius:6px;border:1px solid var(--border);background:var(--surface);color:var(--text2);font-size:.82rem;">
          <option value="800">快速</option><option value="400" selected>中速</option><option value="150">慢速</option>
        </select>
      </div>
      <div class="viz-array" id="viz-6"></div>
      <div class="viz-progress"><div class="viz-progress-bar" id="prog-6"></div></div>
      <div class="viz-log" id="log-6"></div>
    </div>
  </div>
  <div class="task-section">
    <h3><span class="num">5</span> 实操练习</h3>
    <div class="exercise-item">
      <div class="q-text"><span class="q-num">1.</span> 快速排序的基准（pivot）选择规则是？</div>
      <label><input type="radio" name="q6_1" value="a"> A. 随机选择</label>
      <label><input type="radio" name="q6_1" value="b"> B. 选择区间的第一个元素</label>
      <label><input type="radio" name="q6_1" value="c"> C. 选择区间的中点</label>
      <button class="check-btn" onclick="checkRadio(this,'b','q6_1')">检查答案</button>
      <div class="result" id="result-q6_1"></div>
    </div>
  </div>
</div>
"""
html += task6

# 任务7
task7 = """
<!-- ==================== TASK 7: 归并与基数排序 ==================== -->
<div id="task-7" class="task-detail">
  <a class="back-btn" onclick="showTaskList()">&#8592; 返回任务列表</a>
  <div class="task-section">
    <h3><span class="num">1</span> 归并排序原理</h3>
    <p>归并排序采用<strong>分治</strong>策略：先将数组分成两半，分别排序后再合并成一个有序数组。</p>
    <p>时间复杂度：<strong>O(n log n)</strong>，空间复杂度：<strong>O(n)</strong>，是<strong>稳定</strong>的排序算法。</p>
  </div>
  <div class="task-section">
    <h3><span class="num">2</span> 归并排序 Java代码</h3>
    <div class="code-block">
      <button class="copy-btn" onclick="copyCode(this)">复制</button>
      <pre><span class="comment">/** 归并排序 时间: O(nlogn) 空间: O(n) 稳定: 是 */</span>
<span class="keyword">public void</span> <span class="type">mergeSort</span>() {
    <span class="keyword">int</span> k = <span class="num-literal">1</span>;
    <span class="keyword">while</span> (k &lt; r.length) { merge(k); k *= <span class="num-literal">2</span>; }
}
<span class="keyword">public void</span> <span class="type">merge</span>(<span class="keyword">int</span> len) {
    <span class="keyword">int</span> m=<span class="num-literal">0</span>, l1=<span class="num-literal">0</span>, h1, l2, h2, i, j;
    Product[] tmp = <span class="keyword">new</span> Product[r.length];
    <span class="keyword">while</span> (l1+len &lt; r.length) {
        l2 = l1+len; h1 = l2-<span class="num-literal">1</span>;
        h2 = (l2+len-<span class="num-literal">1</span>&lt;r.length) ? l2+len-<span class="num-literal">1</span> : r.length-<span class="num-literal">1</span>;
        i = l1; j = l2;
        <span class="keyword">while</span> ((i&lt;=h1) &amp;&amp; (j&lt;=h2)) {
            <span class="keyword">if</span> (r[i].price&lt;=r[j].price) tmp[m++]=r[i++];
            <span class="keyword">else</span> tmp[m++]=r[j++];
        }
        <span class="keyword">while</span> (i&lt;=h1) tmp[m++]=r[i++];
        <span class="keyword">while</span> (j&lt;=h2) tmp[m++]=r[j++];
        l1 = h2+<span class="num-literal">1</span>;
    }
    <span class="keyword">for</span> (i=<span class="num-literal">0</span>; i&lt;r.length; ++i) r[i]=tmp[i];
}</pre>
    </div>
  </div>
  <div class="task-section">
    <h3><span class="num">3</span> 逐步执行演示（归并排序）</h3>
    <div class="viz-section">
      <div class="viz-controls">
        <button class="viz-btn primary" onclick="mergeSort_step(7)">&#9654; 单步执行</button>
        <button class="viz-btn" onclick="mergeSort_reset(7)">&#8635; 重置</button>
        <button class="viz-btn" onclick="mergeSort_auto(7)" id="auto-btn-merge-7">&#9658; 自动播放</button>
        <select id="speed-merge-7" style="padding:.4rem;border-radius:6px;border:1px solid var(--border);background:var(--surface);color:var(--text2);font-size:.82rem;">
          <option value="800">快速</option><option value="400" selected>中速</option><option value="150">慢速</option>
        </select>
      </div>
      <div class="viz-array" id="merge-viz-7"></div>
      <div class="viz-progress"><div class="viz-progress-bar" id="merge-prog-7"></div></div>
      <div class="viz-log" id="merge-log-7"></div>
    </div>
  </div>
  <div class="task-section">
    <h3><span class="num">4</span> 实操练习</h3>
    <div class="exercise-item">
      <div class="q-text"><span class="q-num">1.</span> 归并排序和快速排序的主要区别是什么？</div>
      <button class="answer-btn" onclick="toggleAnswer(this.nextElementSibling)">显示答案</button>
      <div class="answer-box">
        <p><strong>主要区别：</strong>快速排序就地划分，通过基准划分左右两部分；归并排序对半切分，先递归排序再合并。归并排序需要 O(n) 额外空间，快速排序只需 O(log n)。</p>
      </div>
    </div>
  </div>
</div>
"""
html += task7

html += """
</div><!-- /container -->

<script>
// ========== 全局数据 ==========
var PRODUCTS = [
  {brand:'inphic', type:'PB1P', reviews:20, price:30},
  {brand:'logitech', type:'M220', reviews:100, price:69},
  {brand:'rapoo', type:'M300G', reviews:20, price:59},
  {brand:'inphic', type:'PW1h', reviews:50, price:27},
  {brand:'mi', type:'Lite2', reviews:200, price:34},
  {brand:'logitech', type:'M187P', reviews:1, price:49},
  {brand:'inphic', type:'DR01', reviews:2, price:53},
  {brand:'logitech', type:'M330', reviews:100, price:99},
  {brand:'dareu', type:'EM915', reviews:50, price:89},
  {brand:'inphic', type:'PM6', reviews:100, price:28}
];

// ========== 通用函数 ==========
function showTaskList() {
  var tl = document.getElementById('task-list');
  if (tl) tl.style.display = 'block';
  for (var i = 1; i <= 7; i++) {
    var el = document.getElementById('task-' + i);
    if (el) { el.classList.remove('active'); el.style.display = 'none'; }
  }
}

function showTask(n) {
  var tl = document.getElementById('task-list');
  if (tl) tl.style.display = 'none';
  for (var i = 1; i <= 7; i++) {
    var el = document.getElementById('task-' + i);
    if (el) { el.classList.remove('active'); el.style.display = 'none'; }
  }
  var target = document.getElementById('task-' + n);
  if (target) { target.classList.add('active'); target.style.display = 'block'; }
  window.scrollTo(0, 0);
  initData(n);
}

function initData(taskId) {
  var tbody = document.getElementById('data-' + taskId);
  if (!tbody || tbody.children.length > 0) return;
  for (var i = 0; i < PRODUCTS.length; i++) {
    var p = PRODUCTS[i];
    var tr = document.createElement('tr');
    tr.innerHTML = '<td>' + i + '</td><td>' + p.brand + '</td><td>' + p.type + '</td><td>' + p.reviews + '</td><td>' + p.price + '</td>';
    tbody.appendChild(tr);
  }
}

function renderViz(taskId, arr, highlights) {
  var container = document.getElementById('viz-' + taskId);
  if (!container) return;
  container.innerHTML = '';
  for (var i = 0; i < arr.length; i++) {
    var item = arr[i];
    var cell = document.createElement('div');
    cell.className = 'arr-cell';
    if (highlights && highlights.comparing && highlights.comparing.indexOf(i) !== -1) cell.classList.add('comparing');
    if (highlights && highlights.swapping && highlights.swapping.indexOf(i) !== -1) cell.classList.add('swapping');
    if (highlights && highlights.sorted && highlights.sorted.indexOf(i) !== -1) cell.classList.add('sorted');
    if (highlights && highlights.pivot && highlights.pivot.indexOf(i) !== -1) cell.classList.add('pivot');
    cell.innerHTML = '<span class="price">' + item.price + '</span><span class="brand">' + item.brand.substring(0,3) + '</span><span class="idx">' + i + '</span>';
    container.appendChild(cell);
  }
}

function log(taskId, msg, type) {
  var logEl = document.getElementById('log-' + taskId);
  if (!logEl) return;
  var span = document.createElement('div');
  span.className = 'log-line';
  var cls = 'log-info';
  if (type === 'op') cls = 'log-op';
  if (type === 'ok') cls = 'log-ok';
  span.innerHTML = '<span class="' + cls + '">' + msg + '</span>';
  logEl.appendChild(span);
  logEl.scrollTop = logEl.scrollHeight;
}

function clearLog(taskId) {
  var logEl = document.getElementById('log-' + taskId);
  if (logEl) logEl.innerHTML = '';
}

function updateProg(taskId, pct) {
  var prog = document.getElementById('prog-' + taskId);
  if (prog) prog.style.width = pct + '%';
}

function copyCode(btn) {
  var pre = btn.parentElement.querySelector('pre');
  if (!pre || !navigator.clipboard) return;
  navigator.clipboard.writeText(pre.textContent).then(function() {
    btn.textContent = '已复制!';
    setTimeout(function() { btn.textContent = '复制'; }, 1500);
  });
}

function toggleAnswer(el) {
  if (!el) return;
  el.classList.toggle('show');
  var btn = el.previousElementSibling;
  if (btn && btn.classList) {
    btn.textContent = el.classList.contains('show') ? '隐藏答案' : '显示答案';
  }
}

function checkRadio(btn, correct, name) {
  var radios = document.getElementsByName(name);
  var result = btn.nextElementSibling;
  var selected = '';
  for (var i = 0; i < radios.length; i++) { if (radios[i].checked) selected = radios[i].value; }
  var isCorrect = (selected === correct);
  result.className = 'result show ' + (isCorrect ? 'pass' : 'fail');
  result.innerHTML = isCorrect ? '正确!' : '错误，正确答案是 ' + correct.toUpperCase();
  for (var i = 0; i < radios.length; i++) {
    radios[i].parentElement.classList.remove('correct', 'wrong');
    if (radios[i].value === correct) radios[i].parentElement.classList.add('correct');
    else if (radios[i].checked && radios[i].value !== correct) radios[i].parentElement.classList.add('wrong');
  }
}

// ========== TASK 1: 插入排序 ==========
var insertSortState = {};
var insertSortTimer = null;

function insertSort_reset(taskId) {
  if (insertSortTimer) { clearTimeout(insertSortTimer); insertSortTimer = null; }
  var btn = document.getElementById('auto-btn-' + taskId);
  if (btn) { btn.textContent = '▶ 自动播放'; btn.dataset.running = '0'; }
  insertSortState = { arr: JSON.parse(JSON.stringify(PRODUCTS)), i: 1, j: -1, tmp: null, phase: 'outer' };
  clearLog(taskId);
  updateProg(taskId, 0);
  log(taskId, '初始: ' + insertSortState.arr.map(function(p){return p.price}).join(', '));
  renderViz(taskId, insertSortState.arr, {});
}

function insertSort_step(taskId) {
  var s = insertSortState;
  if (s.phase === 'done') {
    log(taskId, '排序完成!', 'ok');
    renderViz(taskId, s.arr, {sorted: [0,1,2,3,4,5,6,7,8,9]});
    return;
  }
  if (s.phase === 'outer') {
    if (s.i >= s.arr.length) { s.phase = 'done'; insertSort_step(taskId); return; }
    var price = s.arr[s.i].price;
    var prevPrice = s.arr[s.i - 1].price;
    if (price < prevPrice) {
      s.tmp = JSON.parse(JSON.stringify(s.arr[s.i]));
      s.j = s.i - 1;
      s.phase = 'inner';
      log(taskId, 'i=' + s.i + ': ' + price + '<' + prevPrice + '，需要插入');
      renderViz(taskId, s.arr, {comparing: [s.i, s.i-1]});
    } else {
      log(taskId, 'i=' + s.i + ': ' + price + '>= ' + prevPrice + '，无需插入');
      s.i++;
      updateProg(taskId, Math.round(s.i / s.arr.length * 100));
      renderViz(taskId, s.arr, {sorted: Array.range(0, s.i)});
    }
    return;
  }
  if (s.phase === 'inner') {
    if (s.j >= 0 && s.tmp.price < s.arr[s.j].price) {
      log(taskId, 'j=' + s.j + ': 元素后移');
      s.arr[s.j + 1] = JSON.parse(JSON.stringify(s.arr[s.j]));
      renderViz(taskId, s.arr, {comparing: [s.j]});
      s.j--;
    } else {
      s.phase = 'insert';
      insertSort_step(taskId);
    }
    return;
  }
  if (s.phase === 'insert') {
    log(taskId, '插入位置 j=' + (s.j+1) + '，将 ' + s.tmp.brand + '@' + s.tmp.price + ' 放入');
    s.arr[s.j + 1] = JSON.parse(JSON.stringify(s.tmp));
    s.i++;
    s.phase = 'outer';
    s.tmp = null;
    updateProg(taskId, Math.round(s.i / s.arr.length * 100));
    renderViz(taskId, s.arr, {sorted: Array.range(0, s.i)});
    return;
  }
}

function insertSort_auto(taskId) {
  var btn = document.getElementById('auto-btn-' + taskId);
  if (!btn) return;
  if (btn.dataset.running === '1') { clearTimeout(insertSortTimer); btn.dataset.running = '0'; btn.textContent = '▶ 自动播放'; return; }
  btn.dataset.running = '1';
  btn.textContent = '⏸ 暂停';
  function autoStep() {
    if (insertSortState.phase === 'done') { btn.dataset.running = '0'; btn.textContent = '▶ 自动播放'; return; }
    insertSort_step(taskId);
    var speed = parseInt(document.getElementById('speed-' + taskId).value) || 400;
    insertSortTimer = setTimeout(autoStep, speed);
  }
  autoStep();
}

// ========== TASK 2: 希尔排序 ==========
var shellSortState = {};
var shellSortTimer = null;

function shellSort_reset(taskId) {
  if (shellSortTimer) { clearTimeout(shellSortTimer); shellSortTimer = null; }
  var btn = document.getElementById('auto-btn-' + taskId);
  if (btn) { btn.textContent = '▶ 自动播放'; btn.dataset.running = '0'; }
  shellSortState = { arr: JSON.parse(JSON.stringify(PRODUCTS)), increments: [3, 1], incIdx: 0, d: 0, i: 0, j: 0, tmp: null, phase: 'outer' };
  clearLog(taskId);
  updateProg(taskId, 0);
  log(taskId, '初始: ' + shellSortState.arr.map(function(p){return p.price}).join(', '));
  renderViz(taskId, shellSortState.arr, {});
}

function shellSort_step(taskId) {
  var s = shellSortState;
  if (s.phase === 'done') { log(taskId, '排序完成!', 'ok'); renderViz(taskId, s.arr, {sorted: [0,1,2,3,4,5,6,7,8,9]}); return; }
  if (s.phase === 'outer') {
    if (s.incIdx >= s.increments.length) { s.phase = 'done'; shellSort_step(taskId); return; }
    s.d = s.increments[s.incIdx];
    s.i = s.d;
    log(taskId, '=== 增量 d=' + s.d + ' ===');
    s.phase = 'find';
    return;
  }
  if (s.phase === 'find') {
    if (s.i >= s.arr.length) { s.incIdx++; s.phase = 'outer'; shellSort_step(taskId); return; }
    if (s.arr[s.i].price < s.arr[s.i - s.d].price) {
      s.tmp = JSON.parse(JSON.stringify(s.arr[s.i]));
      s.j = s.i;
      s.phase = 'shift';
      log(taskId, 'i=' + s.i + ': 开始插入');
      renderViz(taskId, s.arr, {comparing: [s.i, s.i-s.d]});
    } else { s.i++; }
    return;
  }
  if (s.phase === 'shift') {
    if (s.j - s.d >= 0 && s.tmp.price < s.arr[s.j - s.d].price) {
      s.arr[s.j] = JSON.parse(JSON.stringify(s.arr[s.j - s.d]));
      s.j -= s.d;
    } else { s.phase = 'insert'; shellSort_step(taskId); }
    return;
  }
  if (s.phase === 'insert') {
    s.arr[s.j] = JSON.parse(JSON.stringify(s.tmp));
    s.i++;
    s.tmp = null;
    s.phase = 'find';
    return;
  }
}

function shellSort_auto(taskId) {
  var btn = document.getElementById('auto-btn-' + taskId);
  if (!btn) return;
  if (btn.dataset.running === '1') { clearTimeout(shellSortTimer); btn.dataset.running = '0'; btn.textContent = '▶ 自动播放'; return; }
  btn.dataset.running = '1';
  btn.textContent = '⏸ 暂停';
  function autoStep() {
    if (shellSortState.phase === 'done') { btn.dataset.running = '0'; btn.textContent = '▶ 自动播放'; return; }
    shellSort_step(taskId);
    var speed = parseInt(document.getElementById('speed-' + taskId).value) || 400;
    shellSortTimer = setTimeout(autoStep, speed);
  }
  autoStep();
}

// ========== TASK 3: 选择排序 ==========
var selectSortState = {};
var selectSortTimer = null;

function selectSort_reset(taskId) {
  if (selectSortTimer) { clearTimeout(selectSortTimer); selectSortTimer = null; }
  var btn = document.getElementById('auto-btn-' + taskId);
  if (btn) { btn.textContent = '▶ 自动播放'; btn.dataset.running = '0'; }
  selectSortState = { arr: JSON.parse(JSON.stringify(PRODUCTS)), i: 0, k: 0, j: 0, phase: 'find' };
  clearLog(taskId);
  updateProg(taskId, 0);
  log(taskId, '初始: ' + selectSortState.arr.map(function(p){return p.price}).join(', '));
  renderViz(taskId, selectSortState.arr, {});
}

function selectSort_step(taskId) {
  var s = selectSortState;
  if (s.phase === 'done') { log(taskId, '排序完成!', 'ok'); renderViz(taskId, s.arr, {sorted: [0,1,2,3,4,5,6,7,8,9]}); return; }
  if (s.phase === 'find') {
    if (s.i >= s.arr.length - 1) { s.phase = 'done'; updateProg(taskId, 100); selectSort_step(taskId); return; }
    s.k = s.i;
    s.j = s.i + 1;
    log(taskId, '=== 第 ' + (s.i+1) + ' 轮: 假设 min=' + s.arr[s.k].price);
    s.phase = 'scan';
    return;
  }
  if (s.phase === 'scan') {
    if (s.j >= s.arr.length) { s.phase = 'swap'; selectSort_step(taskId); return; }
    if (s.arr[s.j].price < s.arr[s.k].price) { s.k = s.j; log(taskId, '更新 min=' + s.arr[s.k].price + ' at ' + s.k); }
    s.j++;
    return;
  }
  if (s.phase === 'swap') {
    log(taskId, '交换 r[' + s.i + ']=' + s.arr[s.i].price + ' 和 r[' + s.k + ']=' + s.arr[s.k].price);
    var tmp = JSON.parse(JSON.stringify(s.arr[s.i]));
    s.arr[s.i] = JSON.parse(JSON.stringify(s.arr[s.k]));
    s.arr[s.k] = tmp;
    s.i++;
    updateProg(taskId, Math.round(s.i / (s.arr.length-1) * 100));
    s.phase = 'find';
    renderViz(taskId, s.arr, {sorted: Array.range(0, s.i)});
    return;
  }
}

function selectSort_auto(taskId) {
  var btn = document.getElementById('auto-btn-' + taskId);
  if (!btn) return;
  if (btn.dataset.running === '1') { clearTimeout(selectSortTimer); btn.dataset.running = '0'; btn.textContent = '▶ 自动播放'; return; }
  btn.dataset.running = '1';
  btn.textContent = '⏸ 暂停';
  function autoStep() {
    if (selectSortState.phase === 'done') { btn.dataset.running = '0'; btn.textContent = '▶ 自动播放'; return; }
    selectSort_step(taskId);
    var speed = parseInt(document.getElementById('speed-' + taskId).value) || 400;
    selectSortTimer = setTimeout(autoStep, speed);
  }
  autoStep();
}

// ========== TASK 4: 堆排序 ==========
var heapSortState = {};
var heapSortTimer = null;

function heapSort_reset(taskId) {
  if (heapSortTimer) { clearTimeout(heapSortTimer); heapSortTimer = null; }
  var btn = document.getElementById('auto-btn-' + taskId);
  if (btn) { btn.textContent = '▶ 自动播放'; btn.dataset.running = '0'; }
  heapSortState = { arr: JSON.parse(JSON.stringify(PRODUCTS)), phase: 'buildheap', buildIdx: 0, k: 0, j: 0, tmp: null, i: 0 };
  clearLog(taskId);
  updateProg(taskId, 0);
  log(taskId, '初始: ' + heapSortState.arr.map(function(p){return p.price}).join(', '));
  renderViz(taskId, heapSortState.arr, {});
}

function heapSort_step(taskId) {
  var s = heapSortState;
  if (s.phase === 'done') { log(taskId, '排序完成!', 'ok'); renderViz(taskId, s.arr, {sorted: [0,1,2,3,4,5,6,7,8,9]}); return; }
  if (s.phase === 'buildheap') {
    var lastNonLeaf = Math.floor(s.arr.length / 2) - 1;
    if (s.buildIdx > lastNonLeaf) { s.phase = 'sort'; s.i = s.arr.length - 1; log(taskId, '建堆完成!'); updateProg(taskId, 50); return; }
    s.k = s.buildIdx;
    s.tmp = JSON.parse(JSON.stringify(s.arr[s.buildIdx]));
    s.j = 2 * s.k + 1;
    log(taskId, '调整节点 ' + s.k);
    s.phase = 'heapDown';
    return;
  }
  if (s.phase === 'heapDown') {
    if (s.j > s.arr.length - 1) { s.arr[s.k] = JSON.parse(JSON.stringify(s.tmp)); s.buildIdx++; s.phase = 'buildheap'; }
    else {
      if (s.j + 1 < s.arr.length && s.arr[s.j].price < s.arr[s.j+1].price) s.j++;
      if (s.tmp.price < s.arr[s.j].price) { s.arr[s.k] = JSON.parse(JSON.stringify(s.arr[s.j])); s.k = s.j; s.j = 2*s.k+1; }
      else { s.arr[s.k] = JSON.parse(JSON.stringify(s.tmp)); s.buildIdx++; s.phase = 'buildheap'; }
    }
    return;
  }
  if (s.phase === 'sort') {
    if (s.i <= 0) { s.phase = 'done'; updateProg(taskId, 100); heapSort_step(taskId); return; }
    log(taskId, '交换堆顶 ' + s.arr[0].price + ' 和 r[' + s.i + ']');
    var tmp = JSON.parse(JSON.stringify(s.arr[0]));
    s.arr[0] = JSON.parse(JSON.stringify(s.arr[s.i]));
    s.arr[s.i] = tmp;
    s.tmp = JSON.parse(JSON.stringify(s.arr[0]));
    s.k = 0;
    s.j = 1;
    s.phase = 'heapDown2';
    return;
  }
  if (s.phase === 'heapDown2') {
    if (s.j > s.i - 1) { s.arr[s.k] = JSON.parse(JSON.stringify(s.tmp)); s.i--; updateProg(taskId, 50 + Math.round((s.arr.length-s.i)/s.arr.length*50)); s.phase = 'sort'; }
    else {
      if (s.j + 1 <= s.i - 1 && s.arr[s.j].price < s.arr[s.j+1].price) s.j++;
      if (s.tmp.price < s.arr[s.j].price) { s.arr[s.k] = JSON.parse(JSON.stringify(s.arr[s.j])); s.k = s.j; s.j = 2*s.k+1; }
      else { s.arr[s.k] = JSON.parse(JSON.stringify(s.tmp)); s.i--; updateProg(taskId, 50 + Math.round((s.arr.length-s.i)/s.arr.length*50)); s.phase = 'sort'; }
    }
    return;
  }
}

function heapSort_auto(taskId) {
  var btn = document.getElementById('auto-btn-' + taskId);
  if (!btn) return;
  if (btn.dataset.running === '1') { clearTimeout(heapSortTimer); btn.dataset.running = '0'; btn.textContent = '▶ 自动播放'; return; }
  btn.dataset.running = '1';
  btn.textContent = '⏸ 暂停';
  function autoStep() {
    if (heapSortState.phase === 'done') { btn.dataset.running = '0'; btn.textContent = '▶ 自动播放'; return; }
    heapSort_step(taskId);
    var speed = parseInt(document.getElementById('speed-' + taskId).value) || 400;
    heapSortTimer = setTimeout(autoStep, speed);
  }
  autoStep();
}

// ========== TASK 5: 冒泡排序 ==========
var bubbleSortState = {};
var bubbleSortTimer = null;

function bubbleSort_reset(taskId) {
  if (bubbleSortTimer) { clearTimeout(bubbleSortTimer); bubbleSortTimer = null; }
  var btn = document.getElementById('auto-btn-' + taskId);
  if (btn) { btn.textContent = '▶ 自动播放'; btn.dataset.running = '0'; }
  bubbleSortState = { arr: JSON.parse(JSON.stringify(PRODUCTS)), i: 1, j: 0, phase: 'compare', exchange: false };
  clearLog(taskId);
  updateProg(taskId, 0);
  log(taskId, '初始: ' + bubbleSortState.arr.map(function(p){return p.price}).join(', '));
  renderViz(taskId, bubbleSortState.arr, {});
}

function bubbleSort_step(taskId) {
  var s = bubbleSortState;
  if (s.phase === 'done') { log(taskId, '排序完成!', 'ok'); renderViz(taskId, s.arr, {sorted: [0,1,2,3,4,5,6,7,8,9]}); return; }
  if (s.phase === 'compare') {
    if (s.j >= s.arr.length - s.i) {
      if (!s.exchange) { log(taskId, '第 ' + s.i + ' 轮: 无交换，提前终止!'); s.phase = 'done'; updateProg(taskId, 100); bubbleSort_step(taskId); }
      else { s.i++; s.j = 0; s.exchange = false; updateProg(taskId, Math.round((s.i-1)/(s.arr.length-1)*100)); if (s.i >= s.arr.length) { s.phase = 'done'; updateProg(taskId, 100); bubbleSort_step(taskId); } }
      return;
    }
    log(taskId, '比较 r[' + s.j + ']=' + s.arr[s.j].price + ' 和 r[' + (s.j+1) + ']=' + s.arr[s.j+1].price);
    if (s.arr[s.j].price > s.arr[s.j + 1].price) {
      log(taskId, '  交换!');
      var tmp = JSON.parse(JSON.stringify(s.arr[s.j]));
      s.arr[s.j] = JSON.parse(JSON.stringify(s.arr[s.j + 1]));
      s.arr[s.j + 1] = tmp;
      s.exchange = true;
      renderViz(taskId, s.arr, {swapping: [s.j, s.j+1]});
    }
    s.j++;
    return;
  }
}

function bubbleSort_auto(taskId) {
  var btn = document.getElementById('auto-btn-' + taskId);
  if (!btn) return;
  if (btn.dataset.running === '1') { clearTimeout(bubbleSortTimer); btn.dataset.running = '0'; btn.textContent = '▶ 自动播放'; return; }
  btn.dataset.running = '1';
  btn.textContent = '⏸ 暂停';
  function autoStep() {
    if (bubbleSortState.phase === 'done') { btn.dataset.running = '0'; btn.textContent = '▶ 自动播放'; return; }
    bubbleSort_step(taskId);
    var speed = parseInt(document.getElementById('speed-' + taskId).value) || 400;
    bubbleSortTimer = setTimeout(autoStep, speed);
  }
  autoStep();
}

// ========== TASK 6: 快速排序 ==========
var quickSortState = {};
var quickSortTimer = null;

function quickSort_reset(taskId) {
  if (quickSortTimer) { clearTimeout(quickSortTimer); quickSortTimer = null; }
  var btn = document.getElementById('auto-btn-' + taskId);
  if (btn) { btn.textContent = '▶ 自动播放'; btn.dataset.running = '0'; }
  quickSortState = { arr: JSON.parse(JSON.stringify(PRODUCTS)), stack: [{low:0, high:PRODUCTS.length-1}], phase: 'partition', low:0, high:0, i:0, j:0, pivot:0 };
  clearLog(taskId);
  updateProg(taskId, 0);
  log(taskId, '初始: ' + quickSortState.arr.map(function(p){return p.price}).join(', '));
  renderViz(taskId, quickSortState.arr, {});
}

function quickSort_step(taskId) {
  var s = quickSortState;
  if (s.phase === 'done') { log(taskId, '排序完成!', 'ok'); renderViz(taskId, s.arr, {sorted: [0,1,2,3,4,5,6,7,8,9]}); return; }
  if (s.phase === 'partition') {
    if (s.stack.length === 0) { s.phase = 'done'; updateProg(taskId, 100); quickSort_step(taskId); return; }
    var ctx = s.stack.pop();
    s.low = ctx.low;
    s.high = ctx.high;
    if (s.low >= s.high) { quickSort_step(taskId); return; }
    s.pivot = s.arr[s.low].price;
    s.i = s.low + 1;
    s.j = s.high;
    log(taskId, '区间 [' + s.low + ',' + s.high + '] pivot=' + s.pivot);
    s.phase = 'scan';
    return;
  }
  if (s.phase === 'scan') {
    if (s.i >= s.j) { s.phase = 'placePivot'; quickSort_step(taskId); return; }
    if (s.arr[s.j].price < s.pivot) { s.phase = 'placeI'; }
    else { s.j--; }
    return;
  }
  if (s.phase === 'placeI') {
    if (s.arr[s.i].price > s.pivot) { s.phase = 'swap'; quickSort_step(taskId); return; }
    s.i++;
    return;
  }
  if (s.phase === 'swap') {
    log(taskId, '交换 r[' + s.i + '] 和 r[' + s.j + ']');
    var tmp = JSON.parse(JSON.stringify(s.arr[s.i]));
    s.arr[s.i] = JSON.parse(JSON.stringify(s.arr[s.j]));
    s.arr[s.j] = tmp;
    s.i++;
    s.j--;
    s.phase = 'scan';
    return;
  }
  if (s.phase === 'placePivot') {
    if (s.arr[s.j].price < s.arr[s.low].price) {
      log(taskId, '交换 pivot 到 r[' + s.j + ']');
      var tmp = JSON.parse(JSON.stringify(s.arr[s.low]));
      s.arr[s.low] = JSON.parse(JSON.stringify(s.arr[s.j]));
      s.arr[s.j] = tmp;
    }
    if (s.low < s.j - 1) s.stack.push({low:s.low, high:s.j-1});
    if (s.j + 1 < s.high) s.stack.push({low:s.j+1, high:s.high});
    s.phase = 'partition';
    updateProg(taskId, Math.round((10 - s.stack.length) / 10 * 100));
    quickSort_step(taskId);
    return;
  }
}

function quickSort_auto(taskId) {
  var btn = document.getElementById('auto-btn-' + taskId);
  if (!btn) return;
  if (btn.dataset.running === '1') { clearTimeout(quickSortTimer); btn.dataset.running = '0'; btn.textContent = '▶ 自动播放'; return; }
  btn.dataset.running = '1';
  btn.textContent = '⏸ 暂停';
  function autoStep() {
    if (quickSortState.phase === 'done') { btn.dataset.running = '0'; btn.textContent = '▶ 自动播放'; return; }
    quickSort_step(taskId);
    var speed = parseInt(document.getElementById('speed-' + taskId).value) || 400;
    quickSortTimer = setTimeout(autoStep, speed);
  }
  autoStep();
}

// ========== TASK 7: 归并排序 ==========
var mergeSortState = {};
var mergeSortTimer = null;

function renderMergeViz(taskId, arr, highlights) {
  var container = document.getElementById('merge-viz-' + taskId);
  if (!container) return;
  container.innerHTML = '';
  for (var i = 0; i < arr.length; i++) {
    var item = arr[i];
    var cell = document.createElement('div');
    cell.className = 'arr-cell';
    if (highlights && highlights.sorted && highlights.sorted.indexOf(i) !== -1) cell.classList.add('sorted');
    cell.innerHTML = '<span class="price">' + item.price + '</span><span class="brand">' + item.brand.substring(0,3) + '</span><span class="idx">' + i + '</span>';
    container.appendChild(cell);
  }
}

function mergeSort_reset(taskId) {
  if (mergeSortTimer) { clearTimeout(mergeSortTimer); mergeSortTimer = null; }
  var btn = document.getElementById('auto-btn-merge-7');
  if (btn) { btn.textContent = '▶ 自动播放'; btn.dataset.running = '0'; }
  var n = PRODUCTS.length;
  mergeSortState = { arr: JSON.parse(JSON.stringify(PRODUCTS)), n: n, k: 1, phase: 'outer', l1: 0, len: 0, l2: 0, h1: 0, h2: 0, m: 0, i: 0, j: 0, tmp: [] };
  var logEl = document.getElementById('merge-log-7');
  if (logEl) logEl.innerHTML = '';
  var prog = document.getElementById('merge-prog-7');
  if (prog) prog.style.width = '0%';
  log('merge', '初始: ' + mergeSortState.arr.map(function(p){return p.price}).join(', '));
  renderMergeViz(taskId, mergeSortState.arr, {});
}

function logMerge(taskId, msg, type) {
  var logEl = document.getElementById('merge-log-' + taskId);
  if (!logEl) return;
  var span = document.createElement('div');
  span.className = 'log-line';
  var cls = 'log-info';
  if (type === 'op') cls = 'log-op';
  if (type === 'ok') cls = 'log-ok';
  span.innerHTML = '<span class="' + cls + '">' + msg + '</span>';
  logEl.appendChild(span);
  logEl.scrollTop = logEl.scrollHeight;
}

function mergeSort_step(taskId) {
  var s = mergeSortState;
  if (s.phase === 'done') { logMerge(taskId, '排序完成!', 'ok'); renderMergeViz(taskId, s.arr, {sorted:[0,1,2,3,4,5,6,7,8,9]}); return; }
  if (s.phase === 'outer') {
    if (s.k >= s.n) { s.phase = 'done'; var prog = document.getElementById('merge-prog-7'); if (prog) prog.style.width = '100%'; mergeSort_step(taskId); return; }
    s.l1 = 0;
    s.len = s.k;
    logMerge(taskId, '=== len=' + s.k + ' ===');
    s.phase = 'findMerge';
    return;
  }
  if (s.phase === 'findMerge') {
    if (s.l1 + s.len >= s.n) { s.k *= 2; s.phase = 'outer'; mergeSort_step(taskId); return; }
    s.l2 = s.l1 + s.len;
    s.h1 = s.l2 - 1;
    s.h2 = Math.min(s.l2 + s.len - 1, s.n - 1);
    s.m = 0;
    s.tmp = [];
    logMerge(taskId, '合并 [' + s.l1 + ',' + s.h1 + '] 和 [' + s.l2 + ',' + s.h2 + ']');
    s.phase = 'mergeInit';
    return;
  }
  if (s.phase === 'mergeInit') {
    s.i = s.l1;
    s.j = s.l2;
    s.phase = 'mergeLoop';
    return;
  }
  if (s.phase === 'mergeLoop') {
    if (s.i <= s.h1 && s.j <= s.h2) {
      if (s.arr[s.i].price <= s.arr[s.j].price) { s.tmp.push(JSON.parse(JSON.stringify(s.arr[s.i]))); s.i++; }
      else { s.tmp.push(JSON.parse(JSON.stringify(s.arr[s.j]))); s.j++; }
      return;
    }
    if (s.i <= s.h1) { s.tmp.push(JSON.parse(JSON.stringify(s.arr[s.i]))); s.i++; return; }
    if (s.j <= s.h2) { s.tmp.push(JSON.parse(JSON.stringify(s.arr[s.j]))); s.j++; return; }
    s.phase = 'copyBack';
    mergeSort_step(taskId);
    return;
  }
  if (s.phase === 'copyBack') {
    for (var x = 0; x < s.tmp.length; x++) { s.arr[s.l1 + x] = s.tmp[x]; }
    logMerge(taskId, '复制回: ' + s.tmp.map(function(p){return p.price}).join(','));
    s.l1 = s.h2 + 1;
    s.phase = 'findMerge';
    var prog = document.getElementById('merge-prog-7');
    if (prog) prog.style.width = Math.round(s.k / s.n * 100) + '%';
    return;
  }
}

function mergeSort_auto(taskId) {
  var btn = document.getElementById('auto-btn-merge-7');
  if (!btn) return;
  if (btn.dataset.running === '1') { clearTimeout(mergeSortTimer); btn.dataset.running = '0'; btn.textContent = '▶ 自动播放'; return; }
  btn.dataset.running = '1';
  btn.textContent = '⏸ 暂停';
  function autoStep() {
    if (mergeSortState.phase === 'done') { btn.dataset.running = '0'; btn.textContent = '▶ 自动播放'; return; }
    mergeSort_step(taskId);
    var speed = parseInt(document.getElementById('speed-merge-7').value) || 400;
    mergeSortTimer = setTimeout(autoStep, speed);
  }
  autoStep();
}

// ========== 工具函数补充 ==========
// Array.range polyfill
if (!Array.range) {
  Array.range = function(start, end) {
    var result = [];
    for (var i = start; i < end; i++) result.push(i);
    return result;
  };
}
</script>
</body>
</html>
"""

# 写入文件
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html)

print('Done! File written to:', output_path)
print('File size:', len(html), 'chars')
