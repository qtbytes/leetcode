// Created by none at 2025/07/14 09:56
// leetgo: dev
// https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::mem::swap;

// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
//
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }

impl Solution {
    pub fn get_decimal_value(mut head: Option<Box<ListNode>>) -> i32 {
        let mut res = 0;
        while let Some(node) = head {
            res = (res << 1) | node.val;
            head = node.next;
        }

        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let head: LinkedList = deserialize(&read_line()?)?;
    let ans: i32 = Solution::get_decimal_value(head.into()).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
