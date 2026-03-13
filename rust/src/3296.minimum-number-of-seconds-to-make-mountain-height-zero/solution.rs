// Created by none at 2026/03/13 15:15
// leetgo: dev
// https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn min_number_of_seconds(mountain_height: i32, worker_times: Vec<i32>) -> i64 {
        // we binary search the time to make the mountain height zero
        let mut l = 1;
        // we should get the minimum max time for r
        // look at example:  100000 [1000000]
        let mut r = 1e6 as i64 * ((1e5 as i64) * (1e5 as i64 + 1) / 2);

        fn check(t: i64, worker_times: &Vec<i32>, mountain_height: i32) -> bool {
            let mut height = 0;
            for &w in worker_times {
                let x = t / w as i64;
                // the time spend is 1, 2, 3, ...
                // h * (h+1) / 2 == x
                let h = ((-1.0 + (1.0 + 8.0 * x as f64).sqrt()) / 2.0) as i64;
                height += h as i32;
                if height >= mountain_height {
                    break;
                }
            }
            height >= mountain_height
        }

        while l < r {
            let mid = (l + r) >> 1;
            if check(mid, &worker_times, mountain_height) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }

        l as i64
    }
}

// @lc code=end

fn main() -> Result<()> {
    let mountain_height: i32 = deserialize(&read_line()?)?;
    let worker_times: Vec<i32> = deserialize(&read_line()?)?;
    let ans: i64 = Solution::min_number_of_seconds(mountain_height, worker_times).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
