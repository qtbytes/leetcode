# [862. Shortest Subarray with Sum at Least K][link] (Hard)

[link]: https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

Given an integer array `nums` and an integer `k`, return the length of the shortest non-empty
**subarray** of  `nums` with a sum of at least  `k`. If there is no such **subarray**, return `-1`.

A **subarray** is a **contiguous** part of an array.

**Example 1:**

```
Input: nums = [1], k = 1
Output: 1
```

**Example 2:**

```
Input: nums = [1,2], k = 4
Output: -1
```

**Example 3:**

```
Input: nums = [2,-1,2], k = 3
Output: 3
```

**Constraints:**

- `1 <= nums.length <= 10⁵`
- `-10⁵ <= nums[i] <= 10⁵`
- `1 <= k <= 10⁹`
