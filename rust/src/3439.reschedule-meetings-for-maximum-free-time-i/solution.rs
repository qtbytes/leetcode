// Created by none at 2025/07/09 10:29
// leetgo: dev
// https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn max_free_time(event_time: i32, k: i32, start_time: Vec<i32>, end_time: Vec<i32>) -> i32 {
        let mut q = vec![];
        let n = start_time.len();
        if start_time[0] != 0 {
            q.push(start_time[0]);
        }
        for i in 0..n - 1 {
            q.push(start_time[i + 1] - end_time[i]);
        }
        if end_time[n - 1] != event_time {
            q.push(event_time - end_time[n - 1]);
        }

        // println!("{q:?}");
        // you can select k + 1 continuous segments in q
        let k = k as usize + 1;

        let mut res: i32 = q[..k.min(q.len())].iter().sum();
        let mut s = res;
        for i in k..q.len() {
            s += q[i] - q[i - k];
            res = res.max(s)
        }
        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let event_time: i32 = deserialize(&read_line()?)?;
    let k: i32 = deserialize(&read_line()?)?;
    let start_time: Vec<i32> = deserialize(&read_line()?)?;
    let end_time: Vec<i32> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::max_free_time(event_time, k, start_time, end_time).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
