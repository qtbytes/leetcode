# [2257. Count Unguarded Cells in the Grid][link] (Medium)

[link]: https://leetcode.com/problems/count-unguarded-cells-in-the-grid/

You are given two integers `m` and `n` representing a **0-indexed** `m x n` grid. You are also given
two 2D integer arrays `guards` and `walls` where `guards[i] = [rowᵢ, colᵢ]` and `walls[j] = [rowⱼ,
colⱼ]` represent the positions of the `iᵗʰ` guard and `jᵗʰ` wall respectively.

A guard can see **every** cell in the four cardinal directions (north, east, south, or west)
starting from their position unless **obstructed** by a wall or another guard. A cell is **guarded**
if there is **at least** one guard that can see it.

Return the number of unoccupied cells that are **not** **guarded**.

**Example 1:**

![](https://assets.leetcode.com/uploads/2022/03/10/example1drawio2.png)

```
Input: m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]
Output: 7
Explanation: The guarded and unguarded cells are shown in red and green respectively in the above
diagram.
There are a total of 7 unguarded cells, so we return 7.
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2022/03/10/example2drawio.png)

```
Input: m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]
Output: 4
Explanation: The unguarded cells are shown in green in the above diagram.
There are a total of 4 unguarded cells, so we return 4.
```

**Constraints:**

- `1 <= m, n <= 10⁵`
- `2 <= m * n <= 10⁵`
- `1 <= guards.length, walls.length <= 5 * 10⁴`
- `2 <= guards.length + walls.length <= m * n`
- `guards[i].length == walls[j].length == 2`
- `0 <= rowᵢ, rowⱼ < m`
- `0 <= colᵢ, colⱼ < n`
- All the positions in `guards` and `walls` are **unique**.
