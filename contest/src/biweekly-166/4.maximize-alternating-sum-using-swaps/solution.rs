// Created by none at 2025/09/30 21:53
// leetgo: dev
// https://leetcode.com/problems/maximize-alternating-sum-using-swaps/
// https://leetcode.com/contest/biweekly-contest-166/problems/maximize-alternating-sum-using-swaps/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn max_alternating_sum(nums: Vec<i32>, swaps: Vec<Vec<i32>>) -> i64 {
        let n = nums.len();
        let mut g = vec![vec![]; n];

        for s in swaps {
            let x = s[0] as usize;
            let y = s[1] as usize;
            g[x].push(y);
            g[y].push(x);
        }

        fn dfs(x: usize, fa: usize, group: &mut HashSet<usize>, g: &Vec<Vec<usize>>) {
            if group.contains(&x) {
                return;
            }
            group.insert(x);
            for &y in &g[x] {
                if y == fa {
                    continue;
                }
                dfs(y, x, group, g)
            }
        }

        fn handle(index: &HashSet<usize>, nums: &Vec<i32>) -> i64 {
            let mut value = vec![];
            let mut cnt = vec![0; 2];
            let n = index.len();

            for &i in index {
                value.push(nums[i] as i64);
                cnt[i & 1] += 1;
            }
            value.sort_unstable();
            // put bigger number to even
            value[n - cnt[0]..].iter().sum::<i64>() - value[..n - cnt[0]].iter().sum::<i64>()
        }

        let mut visited = HashSet::new();
        let mut res = 0;

        for x in 0..n {
            if visited.contains(&x) {
                continue;
            }
            let mut group = HashSet::new();
            dfs(x, n, &mut group, &g);
            res += handle(&group, &nums);
            visited.extend(group);
        }

        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let swaps: Vec<Vec<i32>> = deserialize(&read_line()?)?;
    let ans: i64 = Solution::max_alternating_sum(nums, swaps).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
