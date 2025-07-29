// Created by none at 2025/07/29 09:34
// leetgo: dev
// https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;
const N: usize = 31;

impl Solution {
    pub fn smallest_subarrays(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();

        let mut suf = vec![0; n];
        suf[n - 1] = nums[n - 1];
        for i in (0..n - 1).rev() {
            suf[i] = suf[i + 1] | nums[i]
        }

        let mut cnt = vec![0; N];

        fn update(cnt: &mut Vec<i32>, x: i32, delta: i32) {
            for i in 0..N {
                if x >> i & 1 != 0 {
                    cnt[i] += delta
                }
            }
        }

        fn calc(cnt: &Vec<i32>) -> i32 {
            let mut res = 0;
            for (i, &x) in cnt.iter().enumerate() {
                if x > 0 {
                    res |= 1 << i
                }
            }
            res
        }

        let mut r = 0;
        let mut res = vec![0; n];

        for (l, &x) in nums.iter().enumerate() {
            while r <= l || calc(&cnt) < suf[l] {
                update(&mut cnt, nums[r], 1);
                r += 1;
            }
            res[l] = (r - l) as i32;
            update(&mut cnt, x, -1);
        }

        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let ans: Vec<i32> = Solution::smallest_subarrays(nums).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
