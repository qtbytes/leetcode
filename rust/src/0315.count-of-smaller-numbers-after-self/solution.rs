// Created by none at 2025/07/14 14:05
// leetgo: dev
// https://leetcode.com/problems/count-of-smaller-numbers-after-self/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;
use std::ops::*;

#[derive(Default)]
pub struct BIT<T> {
    v: Vec<T>,
}

impl<T> BIT<T>
where
    T: Default + Copy + AddAssign,
{
    pub fn new(n: usize) -> Self {
        Self {
            v: vec![T::default(); n + 1],
        }
    }

    pub fn from_vec(nums: &Vec<T>) -> Self {
        let mut bit = Self {
            v: vec![T::default(); nums.len() + 1],
        };
        for (i, x) in nums.iter().enumerate() {
            bit.add(i + 1, *x);
        }
        bit
    }

    pub fn lowbit(i: usize) -> usize {
        i & i.wrapping_neg()
    }

    pub fn add(&mut self, mut i: usize, delta: T) {
        assert!(i > 0 && i < self.v.len(), "Index {} out of bounds", i);
        while i < self.v.len() {
            self.v[i] += delta;
            i += Self::lowbit(i);
        }
    }

    pub fn query(&self, mut i: usize) -> T {
        assert!(i < self.v.len(), "Index {} out of bounds", i);
        let mut res = T::default();
        while i > 0 {
            res += self.v[i];
            i -= Self::lowbit(i);
        }
        res
    }
}

impl Solution {
    pub fn count_smaller(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut res = vec![0; n];
        let m = 1e4 as i32;
        let mut count = BIT::new(m as usize * 2 + 1);

        for i in (0..n).rev() {
            let x = (nums[i] + m) as usize + 1;
            res[i] = count.query(x - 1);
            count.add(x, 1);
        }

        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let ans: Vec<i32> = Solution::count_smaller(nums).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
