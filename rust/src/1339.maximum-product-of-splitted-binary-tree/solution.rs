// Created by none at 2026/01/07 13:48
// leetgo: dev
// https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cell::RefCell;
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;
use std::rc::Rc;

const MOD: i64 = 1e9 as i64 + 7;

impl Solution {
    pub fn max_product(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        // first, get total sum
        // then choose a sub tree, the answer is sum * (total - sum)

        fn calc_sum(root: &Option<Rc<RefCell<TreeNode>>>) -> i32 {
            if let Some(root) = root {
                let root = root.borrow();
                root.val + calc_sum(&root.left) + calc_sum(&root.right)
            } else {
                0
            }
        }

        let total = calc_sum(&root);

        fn dfs(root: &Option<Rc<RefCell<TreeNode>>>, total: i32, ans: &mut i64) -> i32 {
            // split root as a subtree
            if let Some(root) = root {
                let root = root.borrow();
                let sum = root.val + dfs(&root.left, total, ans) + dfs(&root.right, total, ans);
                *ans = max(*ans, sum as i64 * (total - sum) as i64);
                sum
            } else {
                0
            }
        }

        let mut ans = 0;
        dfs(&root, total, &mut ans);

        (ans % MOD) as _
    }
}

// @lc code=end

fn main() -> Result<()> {
    let root: BinaryTree = deserialize(&read_line()?)?;
    let ans: i32 = Solution::max_product(root.into()).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
