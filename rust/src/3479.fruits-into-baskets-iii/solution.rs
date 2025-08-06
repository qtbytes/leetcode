// Created by none at 2025/08/06 12:25
// leetgo: dev
// https://leetcode.com/problems/fruits-into-baskets-iii/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

pub struct SegmentTree {
    seg: Vec<i32>,
}

impl SegmentTree {
    pub fn new(v: Vec<i32>) -> Self {
        let n = v.len();
        let mut st = SegmentTree {
            seg: vec![0; 4 * n + 1],
        };
        st.build(1, 0, n - 1, &v);
        st
    }
    pub fn maintain(&mut self, o: usize) {
        self.seg[o] = max(self.seg[o * 2], self.seg[o * 2 + 1])
    }

    pub fn build(&mut self, o: usize, l: usize, r: usize, v: &Vec<i32>) {
        if l == r {
            self.seg[o] = v[l];
            return;
        }
        let m = (l + r) / 2;
        self.build(o * 2, l, m, v);
        self.build(o * 2 + 1, m + 1, r, v);
        self.maintain(o);
    }
    pub fn find_first_and_update(&mut self, o: usize, l: usize, r: usize, x: i32) -> Option<usize> {
        if self.seg[o] < x {
            return None;
        }
        if l == r {
            self.seg[o] = -1;
            return Some(l);
        }
        let m = (l + r) >> 1;
        let res = if let Some(i) = self.find_first_and_update(o * 2, l, m, x) {
            Some(i)
        } else if let Some(i) = self.find_first_and_update(o * 2 + 1, m + 1, r, x) {
            Some(i)
        } else {
            None
        };
        self.maintain(o);
        res
    }
}

impl Solution {
    pub fn num_of_unplaced_fruits(fruits: Vec<i32>, baskets: Vec<i32>) -> i32 {
        let n = baskets.len();
        let mut st = SegmentTree::new(baskets);
        let mut res = 0;

        for &f in &fruits {
            if st.find_first_and_update(1, 0, n - 1, f).is_none() {
                res += 1;
            }
        }

        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let fruits: Vec<i32> = deserialize(&read_line()?)?;
    let baskets: Vec<i32> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::num_of_unplaced_fruits(fruits, baskets).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
