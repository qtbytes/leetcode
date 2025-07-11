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
        let mut meetings: Vec<Vec<i64>> = meetings
            .into_iter()
            .map(|e| e.into_iter().map(|x| x as i64).collect())
            .collect();
        meetings.sort();
        // println!("{:?}", meetings);

        let mut free_room = BinaryHeap::from_iter((0..n).map(|i| Reverse(i)));
        let mut used_room: BinaryHeap<Reverse<(_, usize)>> = BinaryHeap::new();

        let m = meetings.len();
        let mut i = 0;
        let mut t = 0;

        // use room
        while i < m {
            let (start, end) = (meetings[i][0], meetings[i][1]);
            t = t.max(start);
            if free_room.is_empty() {
                // skip to earlier time can release room
                t = t.max(used_room.peek().unwrap().0.0)
            }
            // release room
            while let Some(Reverse((time, x))) = used_room.peek() {
                if *time > t {
                    break;
                }
                // println!("Release room {} at {t}", x);
                free_room.push(Reverse(*x));
                used_room.pop();
            }
            let x = free_room.pop().unwrap().0;
            // println!("Use room {} at {}", x, t);
            cnt[x] += 1;
            used_room.push(Reverse((t + end - start, x)));
            i += 1;
        }

        let mut i = 0;
        for j in 1..n {
            if cnt[j] > cnt[i] {
                i = j
            }
        }
        // println!("{cnt:?} {}", cnt[i]);
        assert_eq!(cnt.iter().sum::<i32>(), meetings.len() as i32);

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
