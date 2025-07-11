// Created by none at 2025/07/11 09:57
// leetgo: dev
// https://leetcode.com/problems/meeting-rooms-iii/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn most_booked(n: i32, meetings: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut cnt = vec![0; n];
        let mut meetings = meetings;
        meetings.sort_unstable();
        // println!("{:?}", meetings);

        let mut free_room = BinaryHeap::from_iter((0..n).map(|i| Reverse(i)));
        let mut used_room: BinaryHeap<Reverse<(i64, usize)>> = BinaryHeap::new();

        for m in &meetings {
            while let Some(Reverse((end, i))) = used_room.peek() {
                if *end <= m[0] as i64 {
                    free_room.push(Reverse(*i));
                    used_room.pop();
                } else {
                    break;
                }
            }
            let i;
            let end;
            if free_room.is_empty() {
                // skip to first time can release room
                let room = used_room.pop().unwrap().0;
                end = room.0 + (m[1] - m[0]) as i64;
                i = room.1;
            } else {
                i = free_room.pop().unwrap().0;
                end = m[1] as i64;
            }
            cnt[i] += 1;
            used_room.push(Reverse((end, i)));
        }

        let mut i = 0;
        for j in 1..n {
            if cnt[j] > cnt[i] {
                i = j
            }
        }
        // println!("{cnt:?} {}", cnt[i]);
        // assert_eq!(cnt.iter().sum::<i32>(), meetings.len() as i32);

        i as i32
    }
}

// @lc code=end

fn main() -> Result<()> {
    let n: i32 = deserialize(&read_line()?)?;
    let meetings: Vec<Vec<i32>> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::most_booked(n, meetings).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
