# [2097. Valid Arrangement of Pairs][link] (Hard)

[link]: https://leetcode.com/problems/valid-arrangement-of-pairs/

You are given a **0-indexed** 2D integer array `pairs` where `pairs[i] = [startᵢ, endᵢ]`. An
arrangement of `pairs` is **valid** if for every index `i` where `1 <= i < pairs.length`, we have
`endᵢ₋₁ == startᵢ`.

Return **any** valid arrangement of  `pairs`.

**Note:** The inputs will be generated such that there exists a valid arrangement of `pairs`.

**Example 1:**

```
Input: pairs = [[5,1],[4,5],[11,9],[9,4]]
Output: [[11,9],[9,4],[4,5],[5,1]]
Explanation:
This is a valid arrangement since endᵢ₋₁ always equals startᵢ.
end₀ = 9 == 9 = start₁
end₁ = 4 == 4 = start₂
end₂ = 5 == 5 = start₃
```

**Example 2:**

```
Input: pairs = [[1,3],[3,2],[2,1]]
Output: [[1,3],[3,2],[2,1]]
Explanation:
This is a valid arrangement since endᵢ₋₁ always equals startᵢ.
end₀ = 3 == 3 = start₁
end₁ = 2 == 2 = start₂
The arrangements [[2,1],[1,3],[3,2]] and [[3,2],[2,1],[1,3]] are also valid.
```

**Example 3:**

```
Input: pairs = [[1,2],[1,3],[2,1]]
Output: [[1,2],[2,1],[1,3]]
Explanation:
This is a valid arrangement since endᵢ₋₁ always equals startᵢ.
end₀ = 2 == 2 = start₁
end₁ = 1 == 1 = start₂
```

**Constraints:**

- `1 <= pairs.length <= 10⁵`
- `pairs[i].length == 2`
- `0 <= startᵢ, endᵢ <= 10⁹`
- `startᵢ != endᵢ`
- No two pairs are exactly the same.
- There **exists** a valid arrangement of `pairs`.
