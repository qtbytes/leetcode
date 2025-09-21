// Created by none at 2025/09/21 21:01
// leetgo: dev
// https://leetcode.com/problems/maximum-total-subarray-value-ii/
// https://leetcode.com/contest/weekly-contest-468/problems/maximum-total-subarray-value-ii/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn max_total_value(nums: Vec<i32>, k: i32) -> i64 {
        let m = nums.len();
        let mut index: HashMap<i32, Vec<usize>> = HashMap::new();
        for (i, &x) in nums.iter().enumerate() {
            index.entry(x).or_default().push(i);
        }
        let mut sorted: Vec<i32> = index.keys().cloned().collect();
        sorted.sort_unstable();
        let n = sorted.len();
        let mut heap: BinaryHeap<(i32, usize, usize)> = BinaryHeap::new();

        for i in 1..=n - 1 {
            heap.push((sorted[i] - sorted[0], 0, i));
        }
        let mut res = 0;

        let mut seg = BTreeSet::new();
        seg.insert(m);
        let mut k = k;
        while k > 0 {
            if heap.is_empty() {
                break;
            }
            let (value, i, j) = heap.pop().unwrap();
            if i + 1 < j {
                heap.push((sorted[j] - sorted[i + 1], i + 1, j));
            }

            let (mn, mx) = (sorted[i], sorted[j]);
            // insert index of mn to seg
            for &idx in index.get(&mn).unwrap() {
                if !seg.insert(idx) {
                    break;
                }
            }
            // insert index of mx to seg
            for &idx in index.get(&mx).unwrap() {
                if !seg.insert(idx) {
                    break;
                }
            }

            // calculate how many (l, r) can get mx - mn
            let mut cnt = 0;
            let mut l = -1;
            let mut p1 = -1; // pointer to min
            let mut p2 = -1; // pointer to max
            // l..p1..p2..r
            let tmp: Vec<&usize> = seg.iter().collect();
            for i in 0..tmp.len() - 1 {
                let r = *tmp[i];
                let x = nums[r];
                let r = r as i32;
                // border
                if x < mn || x > mx {
                    (l, p1, p2) = (r, r, r);
                } else if x == mx {
                    cnt += (*tmp[i + 1] as i32 - r) * (p1 - l);
                    p2 = r
                } else if x == mn {
                    cnt += (*tmp[i + 1] as i32 - r) * (p2 - l);
                    p1 = r
                } else {
                    cnt += (*tmp[i + 1] as i32 - r) * (min(p1, p2) - l);
                }
                // println!("{mn} {mx} {x} {l} {p1} {p2} {cnt}");
            }
            // println!("min {mn} max {mx} cnt {cnt}");
            if cnt < k {
                res += value as i64 * (cnt as i64);
                k -= cnt;
            } else {
                res += value as i64 * (k as i64);
                break;
            }
        }

        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let nums: Vec<i32> = deserialize(&read_line()?)?;
    let k: i32 = deserialize(&read_line()?)?;
    let ans: i64 = Solution::max_total_value(nums, k).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
