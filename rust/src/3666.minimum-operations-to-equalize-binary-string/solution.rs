// Created by none at 2026/02/27 15:54
// leetgo: dev
// https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn min_operations(s: String, k: i32) -> i32 {
        let a = s.chars().filter(|&ch| ch == '0').count();
        let n = s.len();
        // 0's range: [max(0, k-(n-a)), min(a, k)]

        if a == 0 {
            return 0;
        }

        if a & 1 == 1 && (2 * min(a as i32, k) - k) & 1 == 0 {
            return -1;
        }

        // since the change of zero is step by 2
        // so we use 2 set, one for odd, one for even
        let mut not_visit = vec![BTreeSet::new(); 2];
        for i in 0..n {
            not_visit[i & 1].insert(i as i32);
        }
        let mut q = VecDeque::new();
        q.push_back(a as i32);
        not_visit[a & 1].remove(&(a as i32));
        let mut t = 0;
        while q.len() > 0 {
            t += 1;
            let size = q.len();
            for _ in 0..size {
                let a = q.pop_front().unwrap();
                let mn = 2 * max(0, k - (n as i32 - a)) - k;
                let mx = 2 * min(a as i32, k) - k;
                let i = ((a + mx) & 1) as usize;

                // dbg!(a, &not_visit[i], a + mn, a + mx);
                // a+mn,a+mx
                let range: Vec<i32> = not_visit[i].range(a - mx..=a - mn).copied().collect();
                // dbg!(&range);
                for x in range {
                    if x == 0 {
                        return t;
                    }
                    not_visit[i].remove(&x);
                    q.push_back(x);
                }
            }
            // dbg!(&not_visit);
        }

        -1
    }
}

// @lc code=end

fn main() -> Result<()> {
    let s: String = deserialize(&read_line()?)?;
    let k: i32 = deserialize(&read_line()?)?;
    let ans: i32 = Solution::min_operations(s, k).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
