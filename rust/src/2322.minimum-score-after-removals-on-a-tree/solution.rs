// Created by none at 2025/07/24 10:24
// leetgo: dev
// https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn minimum_score(nums: Vec<i32>, edges: Vec<Vec<i32>>) -> i32 {
        let n = nums.len();

        let mut g = vec![vec![]; n];

        for e in &edges {
            let x = e[0] as usize;
            let y = e[1] as usize;
            g[x].push(y);
            g[y].push(x);
        }

        let total = nums.iter().fold(0, |x, y| x ^ y);

        let mut xor_sum = vec![0; n];
        let mut depth = vec![0; n];
        let mut parent = vec![0; n];

        fn dfs(
            x: usize,
            fa: usize,
            g: &Vec<Vec<usize>>,
            nums: &Vec<i32>,
            xor_sum: &mut Vec<i32>,
            depth: &mut Vec<i32>,
            parent: &mut Vec<usize>,
        ) -> i32 {
            let mut res = nums[x];
            for &y in &g[x] {
                if y == fa {
                    continue;
                }
                depth[y] = depth[x] + 1;
                parent[y] = x;
                res ^= dfs(y, x, g, nums, xor_sum, depth, parent);
            }
            xor_sum[x] = res;
            res
        }
        // println!("{}", total);
        dfs(0, n, &g, &nums, &mut xor_sum, &mut depth, &mut parent);
        // println!("{:?} {:?}", xor_sum, depth);

        fn is_sub(x: usize, y: usize, depth: &Vec<i32>, parent: &Vec<usize>) -> bool {
            if depth[x] < depth[y] {
                false
            } else if depth[x] == depth[y] {
                x == y
            } else {
                is_sub(parent[x], y, depth, parent)
            }
        }

        let mut res = i32::MAX;

        for i in 0..edges.len() {
            let e1 = &edges[i];
            let (mut x, mut y) = (e1[0] as usize, e1[1] as usize);
            if depth[x] > depth[y] {
                swap(&mut x, &mut y);
            }
            let xor_1 = xor_sum[y];

            for j in 0..i {
                let e2 = &edges[j];
                let (mut u, mut v) = (e2[0] as usize, e2[1] as usize);
                if depth[u] > depth[v] {
                    swap(&mut u, &mut v);
                }
                let mut xor_1 = xor_1;
                let mut xor_2 = xor_sum[v];
                if is_sub(y, v, &depth, &parent) {
                    xor_2 ^= xor_1;
                } else if is_sub(v, y, &depth, &parent) {
                    xor_1 ^= xor_2;
                }
                let xor_3 = total ^ xor_1 ^ xor_2;
                // println!("{} {} {} {:?} {:?}", xor_1, xor_2, xor_3, e1, e2);

                let mut v = vec![xor_1, xor_2, xor_3];
                v.sort_unstable();
                res = res.min(v[2] - v[0])
            }
        }

        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let edges: Vec<Vec<i32>> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::minimum_score(nums, edges).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
