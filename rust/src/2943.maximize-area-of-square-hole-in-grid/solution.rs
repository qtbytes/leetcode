// Created by none at 2026/01/15 12:24
// leetgo: dev
// https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

// we should find the max gap when remove some bar
fn handle(mut bar: Vec<i32>) -> i32 {
    bar.sort_unstable();
    let mut max_gap = 1;
    let size = bar.len();
    let mut i = 0;
    while i < size {
        let mut j = i + 1;
        while j < size && bar[j] == bar[j - 1] + 1 {
            j += 1
        }
        let gap = (j - i) as i32 + 1;
        max_gap = max(max_gap, gap);
        i = j
    }

    max_gap
}

impl Solution {
    pub fn maximize_square_hole_area(_: i32, _: i32, h_bars: Vec<i32>, v_bars: Vec<i32>) -> i32 {
        let h = handle(h_bars);
        let v = handle(v_bars);

        let l = h.min(v);
        l * l
    }
}

// @lc code=end

fn main() -> Result<()> {
    let n: i32 = deserialize(&read_line()?)?;
    let m: i32 = deserialize(&read_line()?)?;
    let h_bars: Vec<i32> = deserialize(&read_line()?)?;
    let v_bars: Vec<i32> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::maximize_square_hole_area(n, m, h_bars, v_bars).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
