# [2787. Ways to Express an Integer as Sum of Powers][link] (Medium)

[link]: https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/

Given two **positive** integers `n` and `x`.

Return the number of ways  `n` can be expressed as the sum of the  `xᵗʰ` power of **unique**
positive integers, in other words, the number of sets of unique integers  `[n₁, n₂, ..., nₖ]` where
`n = n₁ˣ + n₂ˣ + ... + nₖˣ`.

Since the result can be very large, return it modulo `10⁹ + 7`.

For example, if `n = 160` and `x = 3`, one way to express `n` is `n = 2³ + 3³ + 5³`.

**Example 1:**

```
Input: n = 10, x = 2
Output: 1
Explanation: We can express n as the following: n = 3² + 1² = 10.
It can be shown that it is the only way to express 10 as the sum of the 2ⁿᵈ power of unique
integers.
```

**Example 2:**

```
Input: n = 4, x = 1
Output: 2
Explanation: We can express n in the following ways:
- n = 4¹ = 4.
- n = 3¹ + 1¹ = 4.
```

**Constraints:**

- `1 <= n <= 300`
- `1 <= x <= 5`
