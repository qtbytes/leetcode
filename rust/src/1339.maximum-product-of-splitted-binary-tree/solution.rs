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
            let mut ans = 0;
            if let Some(root) = root {
                ans += root.borrow().val;
                if let Some(left) = root.borrow().left.clone() {
                    ans += calc_sum(&Some(left))
                }
                if let Some(right) = root.borrow().right.clone() {
                    ans += calc_sum(&Some(right))
                }
            }
            ans
        }

        let total = calc_sum(&root);

        fn dfs(root: &Option<Rc<RefCell<TreeNode>>>, total: i64, ans: &mut i64) -> i64 {
            let mut sum = 0;
            if let Some(root) = root {
                sum += root.borrow().val as i64;
                // split left as subtree
                if let Some(left) = root.borrow().left.clone() {
                    let sub = dfs(&Some(left), total, ans) as i64;
                    *ans = max(*ans, sub * (total - sub));
                    sum += sub;
                }
                if let Some(right) = root.borrow().right.clone() {
                    let sub = dfs(&Some(right), total, ans) as i64;
                    *ans = max(*ans, sub * (total - sub));
                    sum += sub;
                }
            }
            sum
        }

        let mut ans = 0;
        dfs(&root, total as i64, &mut ans);

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
