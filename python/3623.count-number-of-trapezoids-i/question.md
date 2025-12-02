# [3623. Count Number of Trapezoids I][link] (Medium)

[link]: https://leetcode.com/problems/count-number-of-trapezoids-i/

You are given a 2D integer array `points`, where `points[i] = [xᵢ, yᵢ]` represents the coordinates
of the `iᵗʰ` point on the Cartesian plane.

A **horizontal** **trapezoid** is a convex quadrilateral with **at least one pair** of horizontal
sides (i.e. parallel to the x-axis). Two lines are parallel if and only if they have the same slope.

Return the  number of unique  **horizontaltrapezoids** that can be formed by choosing any four
distinct points from `points`.

Since the answer may be very large, return it **modulo** `10⁹ + 7`.

**Example 1:**

**Input:** points = \[\[1,0\],\[2,0\],\[3,0\],\[2,2\],\[3,2\]\]

**Output:** 3

**Explanation:**

![](https://assets.leetcode.com/uploads/2025/05/01/desmos-graph-
6.png)![](https://assets.leetcode.com/uploads/2025/05/01/desmos-graph-
7.png)![](https://assets.leetcode.com/uploads/2025/05/01/desmos-graph-8.png)

There are three distinct ways to pick four points that form a horizontal trapezoid:

- Using points `[1,0]`, `[2,0]`, `[3,2]`, and `[2,2]`.
- Using points `[2,0]`, `[3,0]`, `[3,2]`, and `[2,2]`.
- Using points `[1,0]`, `[3,0]`, `[3,2]`, and `[2,2]`.

**Example 2:**

**Input:** points = \[\[0,0\],\[1,0\],\[0,1\],\[2,1\]\]

**Output:** 1

**Explanation:**

![](https://assets.leetcode.com/uploads/2025/04/29/desmos-graph-5.png)

There is only one horizontal trapezoid that can be formed.

**Constraints:**

- `4 <= points.length <= 10⁵`
- `–10⁸ <= xᵢ, yᵢ <= 10⁸`
- All points are pairwise distinct.
