// Created by none at 2026/03/14 13:35
// leetgo: dev
// https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn get_happy_string(n: i32, k: i32) -> String {
        let n = n as u32;
        // we can know there are 3 * 2^(n-1) happy strings of length n
        if k > 3 * 2_i32.pow(n - 1) {
            return String::new();
        }
        // now we should find the k-th happy string
        // if the first char is a, will have 2^(n-1) happy strings starting with a
        // if the first char is b, will have 2^(n-1) happy strings starting with b
        // if the first char is c, will have 2^(n-1) happy strings starting with c

        // since the first char logic is diff with others, we need to handle it separately
        let mut res = vec![];
        let mut k = k;
        if k > 2 * 2_i32.pow(n - 1) {
            res.push('c');
            k -= 2 * 2_i32.pow(n - 1);
        } else if k > 2_i32.pow(n - 1) {
            res.push('b');
            k -= 2_i32.pow(n - 1);
        } else {
            res.push('a');
        }

        for i in 1..n as usize {
            let mut useable_char: Vec<char> = "abc".chars().collect();
            for j in 0..3 {
                if useable_char[j] == res[i - 1] {
                    useable_char.remove(j);
                    break;
                }
            }
            // now we know the useable_char is the remaining 2 chars
            if k > 2_i32.pow(n - 1 - i as u32) {
                res.push(useable_char[1]);
                k -= 2_i32.pow(n - 1 - i as u32);
            } else {
                res.push(useable_char[0]);
            }
        }

        res.into_iter().collect()
    }
}

// @lc code=end

fn main() -> Result<()> {
    let n: i32 = deserialize(&read_line()?)?;
    let k: i32 = deserialize(&read_line()?)?;
    let ans: String = Solution::get_happy_string(n, k).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
