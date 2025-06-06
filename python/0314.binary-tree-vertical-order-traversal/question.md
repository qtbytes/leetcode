# [314. Binary Tree Vertical Order Traversal][link] (Medium)

[link]: https://leetcode.com/problems/binary-tree-vertical-order-traversal/

Given the `root` of a binary tree, return **the vertical order traversal** of its nodes' values.
(i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from **left to right**.

**Example 1:**

![](https://assets.leetcode.com/uploads/2024/09/23/image1.png)

```
Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2024/09/23/image3.png)

```
Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]
```

**Example 3:**

![](https://assets.leetcode.com/uploads/2024/09/23/image2.png)

```
Input: root = [1,2,3,4,10,9,11,null,5,null,null,null,null,null,null,null,6]
Output: [[4],[2,5],[1,10,9,6],[3],[11]]
```

**Constraints:**

- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`
