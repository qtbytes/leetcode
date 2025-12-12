// Created by none at 2025/12/12 14:22
// leetgo: dev
// https://leetcode.com/problems/count-mentions-per-user/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::mem::swap;
use std::{collections::*, vec};

impl Solution {
    pub fn count_mentions(number_of_users: i32, mut events: Vec<Vec<String>>) -> Vec<i32> {
        let n = number_of_users as usize;
        let mut cnt = vec![0; n];
        let mut live_time = vec![0; n];

        events.sort_unstable_by_key(|e| (e[1].parse::<i32>().unwrap(), e[0] != "OFFLINE"));

        for e in events {
            match e[0].as_ref() {
                "MESSAGE" => {
                    let t = e[1].parse::<i32>().unwrap();
                    match e[2].as_ref() {
                        "ALL" => {
                            for i in 0..n {
                                cnt[i] += 1
                            }
                        }
                        "HERE" => {
                            for (i, &lt) in live_time.iter().enumerate() {
                                if lt <= t {
                                    cnt[i] += 1
                                }
                            }
                        }
                        _ => {
                            for id in e[2]
                                .split_whitespace()
                                .map(|s| s[2..].parse::<usize>().unwrap())
                            {
                                cnt[id] += 1;
                            }
                        }
                    }
                }
                "OFFLINE" => {
                    let t = e[1].parse::<i32>().unwrap();
                    let id = e[2].parse::<usize>().unwrap();
                    live_time[id] = t + 60;
                }
                _ => unreachable!(),
            }
        }

        cnt
    }
}

// @lc code=end

fn main() -> Result<()> {
    let number_of_users: i32 = deserialize(&read_line()?)?;
    let events: Vec<Vec<String>> = deserialize(&read_line()?)?;
    let ans: Vec<i32> = Solution::count_mentions(number_of_users, events).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
