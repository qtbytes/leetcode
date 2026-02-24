// Created by none at 2026/02/24 13:43
// leetgo: dev
// https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

use std::cell::RefCell;
use std::rc::Rc;

fn dfs(root: Option<Rc<RefCell<TreeNode>>>, mut value: i32) -> i32 {
    if let Some(root) = root {
        let root = root.borrow();
        value = (value << 1) | root.val;
        if root.left.is_none() && root.right.is_none() {
            value
        } else {
            dfs(root.left.clone(), value) + dfs(root.right.clone(), value)
        }
    } else {
        0
    }
}

impl Solution {
    pub fn sum_root_to_leaf(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        dfs(root, 0)
    }
}

// @lc code=end

fn main() -> Result<()> {
    let root: BinaryTree = deserialize(&read_line()?)?;
    let ans: i32 = Solution::sum_root_to_leaf(root.into()).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
