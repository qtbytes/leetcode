// Created by none at 2026/01/09 12:39
// leetgo: dev
// https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;
use serde::de;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

use std::cell::RefCell;
use std::rc::Rc;
impl Solution {
    pub fn subtree_with_all_deepest(
        root: Option<Rc<RefCell<TreeNode>>>,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        // find the max depth
        // if root is the deepest node, return root
        // if left is not none and right is not none, return root
        // else return left or right
        //
        fn find_max_depth(root: &Option<Rc<RefCell<TreeNode>>>) -> i32 {
            if let Some(root) = root {
                let root = root.borrow();
                1 + max(find_max_depth(&root.left), find_max_depth(&root.right))
            } else {
                0
            }
        }

        let max_depth = find_max_depth(&root);
        // dbg!(max_depth);

        fn dfs(
            root: &Option<Rc<RefCell<TreeNode>>>,
            depth: i32,
            max_depth: i32,
        ) -> Option<Rc<RefCell<TreeNode>>> {
            if let Some(root) = root {
                let left = dfs(&root.borrow().left, depth + 1, max_depth);
                let right = dfs(&root.borrow().right, depth + 1, max_depth);
                if left.is_some() && right.is_some() || depth == max_depth {
                    Some(root.clone())
                } else {
                    if left.is_some() { left } else { right }
                }
            } else {
                None
            }
        }
        dfs(&root, 1, max_depth)
    }
}

// @lc code=end

fn main() -> Result<()> {
    let root: BinaryTree = deserialize(&read_line()?)?;
    let ans: BinaryTree = Solution::subtree_with_all_deepest(root.into()).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
