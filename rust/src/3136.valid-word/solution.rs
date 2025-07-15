// Created by none at 2025/07/15 12:09
// leetgo: dev
// https://leetcode.com/problems/valid-word/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn is_valid(word: String) -> bool {
        if word.len() < 3 {
            return false;
        }
        let (mut has_vowel, mut has_consonant) = (false, false);
        let vowels = "aeiou".to_string();

        for ch in word.chars() {
            if !ch.is_alphanumeric() {
                return false;
            }
            if ch.is_alphabetic() {
                if vowels.contains(ch.to_ascii_lowercase()) {
                    has_vowel = true
                } else {
                    has_consonant = true;
                }
            }
        }

        has_vowel && has_consonant
    }
}

// @lc code=end

fn main() -> Result<()> {
    let word: String = deserialize(&read_line()?)?;
    let ans: bool = Solution::is_valid(word).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
