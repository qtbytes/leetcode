// Created by none at 2026/01/06 11:51
// leetgo: dev
// https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::io::Cursor;
use std::mem::swap;

// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
//
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::cell::RefCell;
use std::rc::Rc;
impl Solution {
    pub fn max_level_sum(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut level = 1;
        let mut ans = 1;
        let mut max_sum = i32::MIN;

        let mut q = VecDeque::new();
        q.push_back(root.unwrap());
        while q.len() > 0 {
            let n = q.len();
            let mut cur_sum = 0;
            for _ in 0..n {
                let root = q.pop_front().unwrap();
                cur_sum += root.borrow_mut().val;
                if root.borrow_mut().left.is_some() {
                    q.push_back(root.borrow_mut().left.take().unwrap());
                }
                if root.borrow_mut().right.is_some() {
                    q.push_back(root.borrow_mut().right.take().unwrap());
                }
            }

            if cur_sum > max_sum {
                ans = level;
                max_sum = cur_sum;
            }

            level += 1;
        }

        ans
    }
}

// @lc code=end

fn main() -> Result<()> {
    let root: BinaryTree = deserialize(&read_line()?)?;
    let ans: i32 = Solution::max_level_sum(root.into()).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
