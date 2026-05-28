# 第9章 用查找实现手机通讯录 — 教学素材

> 来源：《数据结构(Java语言版)(第2版·微课视频版)》第9章 + 配套PPT + 网络调研整合
> 整理日期：2026-05-28

---

## 一、项目概述

### 1.1 情境描述
手机通讯录是手机最基本的功能之一。打电话和接电话一般都先执行查找运算：
- **打电话**：先到通讯录中按姓名搜索联系人号码，找到后拨号
- **接电话**：系统先到通讯录查找该号码对应的联系人信息，有则显示姓名，无则显示号码

### 1.2 测试数据（表9-2 手机通讯录）

| 下标 | 姓名 | 电话号码 |
|------|------|----------|
| 0 | 铁路服务热线 | 12306 |
| 1 | 公共卫生健康热线 | 12320 |
| 2 | 旅游服务热线 | 12301 |
| 3 | 中国移动客服热线 | 10086 |
| 4 | 中国电信服务热线 | 10000 |
| 5 | 中国联通服务热线 | 10010 |
| 6 | 中国银行服务热线 | 95566 |
| 7 | 建设银行服务热线 | 95533 |
| 8 | 工商银行服务热线 | 95588 |

### 1.3 学习目标

| 序号 | 能力目标 | 知识要点 |
|------|----------|----------|
| 1 | 理解查找的基础知识 | 查找的基本概念、查找的分类、平均查找长度 |
| 2 | 理解查找算法的基本思想 | 静态查找：顺序查找、折半查找、分块查找；动态查找：二叉排序树查找、哈希表查找 |
| 3 | 能用Java实现查找算法 | 用Java实现顺序查找、折半查找、分块查找、二叉排序树查找、哈希表查找 |
| 4 | 能基于实际应用选择合适的查找算法 | 使用查找实现手机通讯录 |

---

## 二、基础知识

### 2.1 查找的定义
查找是指在一组给定的数据元素中寻找关键字等于某个给定值的数据元素。若存在，查找成功返回数据元素的信息或位置；否则查找失败，返回"空"值或-1。

### 2.2 关键字和主关键字
- **关键字**：数据元素中某个数据项的值（键值），可标识一个数据元素
- **主关键字**：可以唯一标识一个数据元素的关键字
- **次关键字**：可以标识多个数据元素的关键字

### 2.3 查找表的分类

| 类型 | 定义 | 代表算法 |
|------|------|----------|
| **静态查找表** | 只做查找操作 | 顺序查找、二分查找、分块查找 |
| **动态查找表** | 在查找的同时做插入、删除或修改操作 | 二叉排序树、平衡二叉树、B树、哈希表 |

### 2.4 三种查找技术

| 技术 | 存储结构 | 查找方法 |
|------|----------|----------|
| **线性表查找** | 线性表存储结构 | 顺序查找、折半查找、分块查找 |
| **树表查找** | 树存储结构 | 平衡二叉树、B树、二叉排序树 |
| **哈希表查找** | 哈希存储结构 | 哈希查找 |

### 2.5 平均查找长度(ASL)
ASL = Σ(Pi × Ci)，其中 n 是结点个数，Pi 是查找第i个结点的概率，Ci 是找到第i个结点所需比较次数。
等概率情况下 Pi = 1/n。

---

## 三、核心数据结构（原始Java代码）

### 3.1 Contacts 联系人类

```java
public class Contacts implements Comparable<Contacts> {
    String name;          // 联系人名称
    int phone;            // 联系人电话

    public Contacts(String name, int phone) {
        this.name = name;
        this.phone = phone;
    }

    @Override
    public String toString() {
        return "[" + name + "," + phone + "]";
    }

    @Override
    public int compareTo(Contacts o) {
        if (phone == o.phone) return 0;
        else if (phone > o.phone) return 1;
        else return -1;
    }
}
```

### 3.2 ContactsList 通讯录列表类

```java
public class ContactsList {
    Contacts[] cList;

    public ContactsList(Contacts[] cList) {
        this.cList = cList;
    }

    // ... 各查找算法方法在此 ...
}
```

### 3.3 测试数据初始化

```java
public class TestContactsList {
    public static void main(String[] args) {
        Contacts[] data = {
            new Contacts("铁路服务热线", 12306),
            new Contacts("公共卫生健康热线", 12320),
            new Contacts("旅游服务热线", 12301),
            new Contacts("中国移动客服热线", 10086),
            new Contacts("中国电信服务热线", 10000),
            new Contacts("中国联通服务热线", 10010),
            new Contacts("中国银行服务热线", 95566),
            new Contacts("建设银行服务热线", 95533),
            new Contacts("工商银行服务热线", 95588)
        };
        int findphone = 10086;
        ContactsList cList = new ContactsList(data);
        // ... 调用各种查找方法测试 ...
    }
}
```

---

## 四、五种查找算法详解

### 算法1：顺序查找 (Sequential Search)

#### 基本思想
从表的一端开始，顺序扫描线性表，依次将扫描到的结点关键字与给定值Key比较。若相等则查找成功返回索引；若扫描结束仍未找到，返回-1。

#### 图9-3演示：查找10086（4次比较成功）
在原始顺序表中（下标0~8），从左到右依次比较：
- 第1次：12306 ≠ 10086 ✗
- 第2次：12320 ≠ 10086 ✗
- 第3次：12301 ≠ 10086 ✗
- 第4次：10086 = 10086 ✓ → 返回下标3

#### Java代码

```java
// 顺序查找
public int seqSearchByPhone(int phone) {
    for (int i = 0; i < cList.length; i++) {
        if (phone == cList[i].phone)
            return i;
    }
    return -1;
}
```

#### 性能分析
- **成功ASL**：(n+1)/2 ≈ n/2（约比较一半元素）
- **失败ASL**：n
- **时间复杂度**：O(n)
- **适用场景**：无序表、链式存储结构

---

### 算法2：二分查找/折半查找 (Binary Search)

#### 基本思想
要求线性表是有序表。将表中间位置记录的关键字与查找关键字比较：
- 若相等 → 查找成功
- 若中间值 > key → 查找前一子表（left部分）
- 若中间值 < key → 查找后一子表（right part）
重复此过程直到找到或子表为空。

#### ⚠️ 重要：二分查找需要有序表！
文档图9-4展示的数据是**按电话升序排列后的**：
| 下标 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|------|---|---|---|---|---|---|---|---|---|
| 号码 | 10000 | 10010 | 10086 | 12301 | 12306 | 12320 | 95533 | 95566 | 95588 |

#### 图9-4演示：查找10086（3次比较成功）

| 轮次 | low | high | mid | mid值 | 比较 | 操作 |
|------|-----|------|-----|-------|------|------|
| 1 | 0 | 8 | 4 | 12306 | 10086 < 12306 | high=3 |
| 2 | 0 | 3 | 1 | 10010 | 10086 > 10010 | low=2 |
| 3 | 2 | 3 | 2 | 10086 | 10086 = 10086 | ✓ 返回2 |

#### Java代码

```java
// 二分查找
public int binSearchByPhone(int phone) {
    // 对数组元素进行排序
    Arrays.sort(cList);
    int low = 0, high = cList.length - 1, mid;
    while (high >= low) {
        mid = (low + high) / 2;
        if (phone == cList[mid].phone) {
            return mid;
        } else if (phone > cList[mid].phone) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return -1;
}
```

#### 二叉判定树（图9-5）
对于n=9的有序表，判定树深度为⌈log₂(9+1)⌉=4层。查找10086路径：④→①→②（3次比较）。

#### 性能分析
- **时间复杂度**：O(log₂n)
- **成功ASL**：约 log₂(n+1) - 1
- **要求**：有序表 + 顺序存储结构
- **优点**：效率高，适合大表频繁查找
- **缺点**：需要排序，插入删除代价高

---

### 算法3：分块查找 (Block Search)

#### 基本思想
把顺序表分成若干块，每块元素有相同特性（如前缀相同）。建立索引表保存各块的起始位置和关键字。查找时分两步：
1. 在索引表中确定待查记录所在块（索引表有序，可用二分查找）
2. 在确定的块内进行顺序查找

#### 图9-6演示：三块分块结构

**主表（按原始顺序）：**
| 下标 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|------|---|---|---|---|---|---|---|---|---|
| 号码 | 12306 | 12320 | 12301 | 10000 | 10010 | 10086 | 95566 | 95533 | 95588 |

**索引表：**
| 块索引关键字 | 块起始索引 | 块中元素数量 |
|-------------|-----------|-------------|
| 123 | 0 | 3 |
| 100 | 3 | 3 |
| 955 | 6 | 3 |

**各块内容：**
- Block[123]: [12306, 12320, 12301]
- Block[100]: [10000, 10010, 10086]
- Block[955]: [95566, 95533, 95588]

#### 演示：查找10086
1. 取前三位 "100"，在索引表中找到 blockIndex=1（关键字100）
2. 块起始位置=3，在主表[3..5]中顺序查找
3. 第1次：10000≠10086，第2次：10010≠10086，第3次：10086=10086 ✓

#### Java代码

```java
// 定义索引表结点类型
static class BlockInfo {
    int blockBeginIndex;   // 块的起始下标
    int blockKey;          // 块中关键字（前三位）
    int count;             // 块中元素的数量

    public BlockInfo(int blockKey) {
        this.blockBeginIndex = -1;
        this.blockKey = blockKey;
        this.count = 0;
    }
}

// 创建分块查找的索引表
public BlockInfo[] getIndexBlock() {
    BlockInfo[] blocks = {new BlockInfo(100), new BlockInfo(123), new BlockInfo(955)};
    for (int i = 0; i < cList.length; i++) {
        int tmp = Integer.parseInt(Integer.toString(cList[i].phone).substring(0, 3));
        switch (tmp) {
            case 100:
                if (blocks[0].blockBeginIndex == -1) blocks[0].blockBeginIndex = i;
                blocks[0].count++;
                continue;
            case 123:
                if (blocks[1].blockBeginIndex == -1) blocks[1].blockBeginIndex = i;
                blocks[1].count++;
                continue;
            case 955:
                if (blocks[2].blockBeginIndex == -1) blocks[2].blockBeginIndex = i;
                blocks[2].count++;
                continue;
            default:
                continue;
        }
    }
    return blocks;
}

// 分块查找
public int blockSearchByPhone(int phone) {
    int blockindex = -1;
    BlockInfo[] blocks = getIndexBlock();
    int key = Integer.parseInt(Integer.toString(phone).substring(0, 3));
    // 用顺序查找确定在哪一块
    for (int i = 0; i < blocks.length; i++) {
        if (key == blocks[i].blockKey) {
            blockindex = i;
            break;
        }
    }
    // 用顺序查找在指定块中查找元素
    if (blockindex != -1) {
        for (int i = blocks[blockindex].blockBeginIndex;
             i < blocks[blockindex].blockBeginIndex + blocks[blockindex].count; i++) {
            if (phone == cList[i].phone)
                return i;  // 找到，返回下标
        }
    }
    return -1;
}
```

#### 性能分析
- ASL_block = ASL_index + ASL_block（两部分之和）
- 当 s = √n 时取最小值：ASL ≈ √n
- 介于顺序查找 O(n) 和二分查找 O(log₂n) 之间
- **优点**：不需全局排序，插入删除只需调整对应块
- **缺点**：需要额外索引空间

---

### 算法4：二叉排序树查找 (Binary Search Tree)

#### BST定义
二叉排序树或是空树，或是具有以下性质的二叉树：
1. 若左子树非空，左子树所有结点关键字 < 根结点关键字
2. 若右子树非空，右子树所有结点关键字 > 根结点关键字
3. 左右子树也分别为二叉排序树
4. 没有关键字相等的结点

#### 图9-8构建过程（按原始顺序插入9个联系人）

| 步骤 | 操作 | 树状态 |
|------|------|--------|
| 1 | 插入12306 | 12306为根 |
| 2 | 插入12320 | 12320 > 12306 → 右孩子 |
| 3 | 插入12301 | 12301 < 12306 → 左孩子 |
| 4 | 插入10086 | 10086 < 12306 → 左子树; 10086 > 12301 → 右孩子 |
| 5 | 插入10000 | 10000 < 12306 → 左; 10000 < 12301 → 左; 10000 < 10086 → 左 |
| 6 | 插入10010 | 同上路径 → 10086 的右孩子 |
| 7 | 插入95533 | 95533 > 12306 → 右; ... → 最终在10010的左边 |
| 8 | 插入95566 | 95566 > 95533 → 右孩子 |
| 9 | 插入95588 | 95588 > 95566 → 右孩子 |

#### 最终BST结构（图9-8d）：

```
              12306
             /     \
         12301     12320
           \
          10086
          /    \
       10000  10010
              /
            95533
            /    \
         95566  95588
```

#### Java完整代码

```java
// 二叉排序树结点类
public class TreeNode<T> {
    T key;
    TreeNode<T> parent;
    TreeNode<T> left;
    TreeNode<T> right;

    public TreeNode(T key) {
        this.key = key;
    }

    public TreeNode(T key, TreeNode<T> parent, TreeNode<T> left, TreeNode<T> right) {
        this.key = key;
        this.parent = parent;
        this.left = left;
        this.right = right;
    }
}

// 二叉排序树类
public class BinarySearchTree<T extends Comparable<? super T>> {
    private TreeNode root;

    public TreeNode getRoot() { return root; }

    public BinarySearchTree() { root = null; }

    // 判断是否为空
    public boolean isEmpty() { return root == null; }

    // 查找操作：若查找成功返回该结点，否则返回null
    public TreeNode<T> search(T key) {
        TreeNode<T> p = this.root;
        while (p != null && key.compareTo(p.key) != 0) {
            if (key.compareTo(p.key) < 0)
                p = p.left;      // 进入左子树
            else
                p = p.right;     // 进入右子树
        }
        return p;
    }

    // 插入操作：插入成功返回true，否则返回false
    public boolean insert(T key) {
        if (key == null) return false;

        if (this.root == null) {
            this.root = new TreeNode<T>(key);
            return true;
        }

        TreeNode<T> p = this.root, parent = null;
        while (p != null) {
            if (key.compareTo(p.key) == 0)
                return false;     // 不插入相同元素
            parent = p;
            if (key.compareTo(p.key) < 0)
                p = p.left;
            else
                p = p.right;
        }

        // 插入叶子结点作为parent的左/右孩子
        if (key.compareTo(parent.key) < 0)
            parent.left = new TreeNode<T>(key, parent, null, null);
        else
            parent.right = new TreeNode<T>(key, parent, null, null);
        return true;
    }

    // 删除操作：删除成功返回true，否则返回false
    public boolean remove(T key) {
        TreeNode<T> p = this.search(key);

        if (p != null && p.left != null && p.right != null) {
            // 寻找后继结点
            TreeNode<T> insucc = p.right;
            while (insucc != null && insucc.left != null)
                insucc = insucc.left;
            // 交换值
            T temp = p.key;
            p.key = insucc.key;
            insucc.key = temp;
            p = insucc;
        }

        // 删除1度或叶子结点
        if (p != null && p == this.root) {
            if (this.root.left != null)
                this.root = p.left;
            else
                this.root = p.right;
            if (this.root != null)
                this.root.parent = null;
            return p != null ? true : false;
        }

        if (p != null && p == p.parent.left) {
            if (p.left != null) {
                p.parent.left = p.left;
                p.left.parent = p.parent;
            } else {
                p.parent.left = p.right;
                if (p.right != null) p.right.parent = p.parent;
            }
        }

        if (p != null && p == p.parent.right) {
            if (p.left != null) {
                p.parent.right = p.left;
                p.left.parent = p.parent;
            } else {
                p.parent.right = p.right;
                if (p.right != null) p.right.parent = p.parent;
            }
        }
        return p != null ? true : false;
    }

    // 中序遍历（输出升序序列）
    public void traverse() {
        if (isEmpty()) {
            System.out.println("Empty tree");
        } else {
            traverse(root);
            System.out.println();
        }
    }

    private void traverse(TreeNode<T> t) {
        if (t != null) {
            traverse(t.left);
            System.out.print(t.key + " ");
            traverse(t.right);
        }
    }
}
```

#### 测试代码

```java
BinarySortTree<Contacts> contactsSortTree = new BinarySortTree<Contacts>(data);
contactsSortTree.traverse();                                    // 输出排序结果
System.out.println(contactsSortTree.search(new Contacts("", 10086)).key);  // 查找10086
contactsSortTree.remove(new Contacts("", 95566));               // 删除95566
contactsSortTree.traverse();                                    // 再次输出
```

#### 性能分析
- 平均时间复杂度：O(log₂n)
- 最坏情况（退化为单支树）：O(n)，ASL = (n+1)/2
- **优势**：动态维护方便（插入/删除无需移动元素）

---

### 算法5：哈希查找 (Hash Search)

#### 基本思想
通过哈希函数 H(key) 将关键字直接映射到存储地址 0~m-1，理想情况下可实现 O(1) 查找。

#### 构造哈希函数的方法

| 方法 | 说明 | 示例 |
|------|------|------|
| **除余法** | H(key) = key % p（p为≤m的最大质数） | 最常用 |
| **平方取中法** | key²后取中间几位 | 扩大相近数差别 |
| **折叠移位法** | 分段求和舍进位 | 适合超长关键字 |

#### 冲突及解决方法
两个不同关键字映射到同一地址称为**冲突**（同义词）。

**开放定址法**：
- 线性探测：d, d+1, d+2, ..., m-1, 0, 1, ..., d-1（循环）
- 二次探测：d, d+1², d+2², d+3², ...
- 双重哈希法：使用第二个哈希函数

**链表法（本文采用）**：
- 将同义词链接在同一单链表中
- 哈希表T[0..m-1]为指针数组
- 装填因子α可大于1

#### 本项目哈希表参数

**关键计算**：
- 元素个数 n = 9
- 求最大质数 ≤ 9：maxPrime = **7**
- 哈希函数：H(key) = key % 7

**哈希地址计算**：

| 电话号码 | phone % 7 | 哈希地址 |
|----------|-----------|----------|
| 12306 | 12306 ÷ 7 = 1758 余 0 | 0 |
| 12320 | 12320 ÷ 7 = 1760 余 0 | 0 |
| 12301 | 12301 ÷ 7 = 1757 余 2 | 2 |
| 10086 | 10086 ÷ 7 = 1440 余 6 | 6 |
| 10000 | 10000 ÷ 7 = 1428 余 4 | 4 |
| 10010 | 10010 ÷ 7 = 1430 余 0 | 0 |
| 95566 | 95566 ÷ 7 = 13652 余 2 | 2 |
| 95533 | 95533 ÷ 7 = 13647 余 4 | 4 |
| 95588 | 95588 ÷ 7 = 13655 余 3 | 3 |

#### 哈希表示意图（链地址法，size=7）

```
Slot 0: 12306 → 12320 → 10010 → Λ      (3个节点，冲突！)
Slot 1: Λ                              (空)
Slot 2: 12301 → 95566 → Λ             (2个节点，冲突！)
Slot 3: 95588 → Λ                     (1个节点)
Slot 4: 10000 → 95533 → Λ             (2个节点，冲突！)
Slot 5: Λ                              (空)
Slot 6: 10086 → Λ                     (1个节点)
```

#### Java完整代码

```java
// 哈希结点
private static class Node {
    Contacts data;
    Node next;            // 下一个同义词
}

// 求最接近哈希表表长的质数
public int getMaxPrime() {
    int maxprime = 1;
    for (int i = cList.length; i > 1; i--) {
        int j;
        for (j = 2; j <= Math.sqrt(i); j++) {
            if (i % j == 0) break;
        }
        if (j > Math.sqrt(i)) {
            maxprime = i;
            break;
        }
    }
    return maxprime;
}

// 用除余、链表法构建哈希表
public Node[] createHashTable() {
    int maxPrime = getMaxPrime();           // = 7
    Node[] hashtable = new Node[maxPrime];
    int hash;
    for (int i = 0; i < cList.length; i++) {
        Node node = new Node();
        node.data = cList[i];
        node.next = null;
        hash = cList[i].phone % maxPrime;
        if (hashtable[hash] == null) {
            hashtable[hash] = node;
        } else {
            Node p = hashtable[hash];
            while (p.next != null) {
                p = p.next;
            }
            p.next = node;
        }
    }
    return hashtable;
}

// 在哈希表中查找关键字key
public Contacts HashSearch(int key) {
    // 构建哈希表
    Node[] hashtable = createHashTable();
    // 查找 key 是否在哈希表中
    int hash = getHash(key, getMaxPrime());
    Node p = hashtable[hash];
    while (p != null && p.data.phone != key) {
        p = p.next;
    }
    return p != null ? p.data : null;
}
```

#### 性能分析
- **理想情况**：O(1)
- **实际**：取决于哈希函数质量和冲突处理方式
- **优点**：查找速度极快，编码简单
- **缺点**：占用更多内存（以空间换时间）
- **装填因子**α = n/m，通常 α ≤ 1（链表法可>1）

---

## 五、五种算法对比总结

| 对比项 | 顺序查找 | 二分查找 | 分块查找 | BST查找 | 哈希查找 |
|--------|----------|----------|----------|---------|----------|
| 时间复杂度 | O(n) | O(log₂n) | O(√n) | O(log₂n) | O(1)* |
| 前提条件 | 无 | 有序表 | 分块有序 | BST结构 | 哈希函数 |
| 存储结构 | 顺序/链式 | 仅顺序 | 顺序/链式 | 链式 | 任意 |
| 支持动态操作 | × | × | △ | ✓ | ✓ |
| 额外空间 | O(1) | O(1) | O(索引) | O(n) | O(m) |
| 本项目演示数据 | 查找10086，4次比较 | 查找10086，3次比较 | 查找10086，1次索引+3次块内 | 查找10086沿路径 | 10086→slot[6] |

*哈希查找理想O(1)，实际取决于冲突程度

---

## 六、模拟器设计规范

### 数据一致性要求（与教材完全一致）
1. **测试数据**：必须使用表9-2中的9条手机通讯录（不可更改）
2. **顺序查找演示**：还原图9-3，查找10086需4次比较
3. **二分查找演示**：还原图9-4，排序后查找10086需3次比较（low/high/mid轨迹完全一致）
4. **分块查找演示**：还原图9-6，3块结构(123/100/955)，索引表+块内查找两步走
5. **BST演示**：还原图9-8，按原始顺序插入构建树，最终结构与文档图一致
6. **哈希表演示**：phone%7=7槽位，链地址法，冲突分布与上述计算完全一致

### 交互要求
- 单步执行 / 自动播放 / 速度控制
- 高亮当前比较元素
- 显示比较次数和当前状态
- 支持9条数据中任意一条的查找演示

---

## 七、实训任务设计（4个递进任务）

| 任务 | 名称 | 内容 | 知识点 |
|------|------|------|--------|
| Task1 | 顺序查找实训 | 实现seqSearchByPhone，手动模拟+完整源码+解析 | 静态查找基础 |
| Task2 | 二分查找实训 | 实现binSearchByPhone，含判定树分析 | 有序表高效查找 |
| Task3 | 分块查找实训 | 实现getIndexBlock+blockSearchByPhone | 索引表+块查找 |
| Task4 | 哈希查找实训 | 实现createHashTable+HashSearch，链地址法 | 动态查找/哈希技术 |
