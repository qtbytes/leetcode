// Created by none at 2025/10/24 13:40
// leetgo: dev
// https://leetcode.com/problems/next-greater-numerically-balanced-number/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn next_beautiful_number(n: i32) -> i32 {
        fn calc(path: Vec<i32>, n: i32) -> i32 {
            // use all numbers in path, return the first number greater than n
            // e.g: path=[2,2,3,3,3], n=4324
            // return 22333
            if path.len() > n.to_string().len() {
                return path.iter().fold(0, |a, b| a * 10 + b);
            }
            let max = path.iter().rev().fold(0, |a, b| a * 10 + b);
            if max <= n {
                return i32::MAX;
            }

            let target = (n + 1)
                .to_string()
                .chars()
                .map(|ch| ch as i32 - '0' as i32)
                .collect();

            fn dfs(
                i: usize,
                path: &Vec<i32>,
                used: &mut Vec<bool>,
                st: &mut Vec<i32>,
                limit: bool,
                res: &mut i32,
                target: &Vec<i32>,
            ) {
                // println!("{st:?}");
                if i == path.len() {
                    let t = st.iter().fold(0, |a, b| a * 10 + b);
                    *res = min(*res, t);
                    return;
                }
                for j in 0..used.len() {
                    if !used[j] {
                        if !limit || path[j] >= target[i] {
                            st.push(path[j]);
                            used[j] = true;
                            dfs(
                                i + 1,
                                path,
                                used,
                                st,
                                limit && path[j] == target[i],
                                res,
                                target,
                            );
                            used[j] = false;
                            st.pop().unwrap();
                        }
                    }
                }
            }
            let mut res = i32::MAX;

            dfs(
                0,
                &path,
                &mut vec![false; path.len()],
                &mut vec![],
                true,
                &mut res,
                &target,
            );

            res
        }

        let size = n.to_string().len();
        let mut ans = i32::MAX;

        fn dfs(x: usize, path: &mut Vec<i32>, size: usize, n: i32, ans: &mut i32) {
            let m = path.len();
            if x + m > size + 1 {
                return;
            }
            // skip x
            dfs(x + 1, path, size, n, ans);
            // use x
            path.extend(vec![x as i32; x]);
            if path.len() >= size {
                let t = calc(path.clone(), n);
                // println!("{path:?} {t} {n}");
                *ans = min(*ans, t)
            }
            dfs(x + 1, path, size, n, ans);
            path.truncate(m);
        }

        let mut path: Vec<i32> = vec![];
        dfs(1, &mut path, size, n, &mut ans);

        ans
    }
}

// @lc code=end

fn main() -> Result<()> {
    let n: i32 = deserialize(&read_line()?)?;
    let ans: i32 = Solution::next_beautiful_number(n).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
