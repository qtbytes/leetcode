// Created by none at 2025/07/18 12:20
// leetgo: dev
// https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn minimum_difference(nums: Vec<i32>) -> i64 {
        /*
         * we can choose n smaller from 0..i
         * n larger from i..3n
         */

        let m = nums.len();
        let n = m / 3;

        let mut max_q = BinaryHeap::with_capacity(n + 1);
        let mut sum: i64 = 0;
        let mut first = vec![0; n + 1];
        for i in 0..2 * n {
            let x = nums[i];
            sum += x as i64;
            max_q.push(x);
            if max_q.len() > n {
                sum -= max_q.pop().unwrap() as i64;
            }
            if i >= n - 1 {
                first[i + 1 - n] = sum;
            }
        }

        let mut min_q = BinaryHeap::with_capacity(n + 1);
        sum = 0;
        let mut second = vec![0; n + 1];
        for i in (n..3 * n).rev() {
            let x = nums[i];
            sum += x as i64;
            min_q.push(Reverse(x));
            if min_q.len() > n {
                sum -= min_q.pop().unwrap().0 as i64;
            }
            if i <= 2 * n {
                second[2 * n - i] = sum;
            }
        }
        // println!("{:?} {:?}", first, second);
        (0..=n).map(|i| first[i] - second[n - i]).min().unwrap()
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let ans: i64 = Solution::minimum_difference(nums).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
