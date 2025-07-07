// Created by none at 2025/07/07 10:54
// leetgo: dev
// https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::{cmp::Reverse, collections::BinaryHeap};

impl Solution {
    pub fn max_events(events: Vec<Vec<i32>>) -> i32 {
        let mut events = events;
        events.sort_unstable();
        let mut res = 0;
        let mut day = events[0][0];
        let mut q = BinaryHeap::new();

        let mut i = 0;
        let n = events.len();

        while i < n || !q.is_empty() {
            while i < n && events[i][0] <= day {
                q.push(Reverse(events[i][1]));
                i += 1;
            }
            while let Some(Reverse(x)) = q.pop() {
                if x >= day {
                    res += 1;
                    break;
                }
            }
            day += 1;
        }

        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let events: Vec<Vec<i32>> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::max_events(events).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
