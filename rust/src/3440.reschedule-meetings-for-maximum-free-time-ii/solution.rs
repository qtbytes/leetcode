// Created by none at 2025/07/10 10:18
// leetgo: dev
// https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn max_free_time(event_time: i32, start_time: Vec<i32>, end_time: Vec<i32>) -> i32 {
        let n = start_time.len();
        let mut a = vec![];
        a.push(start_time[0]);
        for i in 0..n - 1 {
            a.push(start_time[i + 1] - end_time[i]);
        }
        a.push(event_time - end_time[n - 1]);

        let mut sorted_a = a.clone();
        sorted_a.sort_unstable();
        // Only the 3 largest is needed
        sorted_a = sorted_a[sorted_a.len() - 3..].to_vec();

        // println!("{a:?}");

        // if we move event[i]
        // move i to other place => a[i+1] + event[i] + a[i]
        // move i to a[i] or a[i+1] => a[i+1] + a[i]

        let mut res = 0;

        for i in 0..n {
            let t = end_time[i] - start_time[i];
            res = res.max(a[i + 1] + a[i]);
            let mut end = sorted_a.len() - 1;
            let mut tmp = vec![a[i], a[i + 1]];
            tmp.sort_unstable();
            if sorted_a[end] == tmp[1] {
                end -= 1;
                if sorted_a[end] == tmp[0] {
                    end -= 1
                }
            }
            if t <= sorted_a[end] {
                res = res.max(a[i + 1] + a[i] + t);
            }
        }

        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let event_time: i32 = deserialize(&read_line()?)?;
    let start_time: Vec<i32> = deserialize(&read_line()?)?;
    let end_time: Vec<i32> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::max_free_time(event_time, start_time, end_time).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
