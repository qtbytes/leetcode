// Created by none at 2025/07/20 10:00
// leetgo: dev
// https://leetcode.com/problems/delete-duplicate-folders-in-system/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

#[derive(Default, Clone)]
pub struct Trie {
    children: HashMap<String, Trie>,
    name: String,
}

impl Solution {
    pub fn delete_duplicate_folder(paths: Vec<Vec<String>>) -> Vec<Vec<String>> {
        let mut paths = paths;
        paths.sort_unstable();

        let mut root = Trie::default();
        for p in &paths {
            let mut cur = &mut root;
            for node in p {
                cur = cur.children.entry(node.clone()).or_default();
            }
        }

        let mut freq = HashMap::new();

        fn gen_expr(node: &mut Trie, freq: &mut HashMap<String, usize>) {
            if node.children.is_empty() {
                return;
            }
            let mut expr = vec![];
            for (folder, child) in node.children.iter_mut() {
                gen_expr(child, freq);
                expr.push(format!("{}({})", folder, child.name));
            }
            expr.sort_unstable();
            node.name = expr.join("");
            *freq.entry(node.name.clone()).or_default() += 1
        }

        gen_expr(&mut root, &mut freq);

        let mut res = vec![];
        let mut path = vec![];

        fn dfs(
            root: &Trie,
            freq: &HashMap<String, usize>,
            res: &mut Vec<Vec<String>>,
            path: &mut Vec<String>,
        ) {
            if freq.get(&root.name).unwrap_or(&0) > &1 {
                return;
            }
            if !path.is_empty() {
                res.push(path.clone());
            }

            for (folder, child) in root.children.iter() {
                path.push(folder.clone());
                dfs(child, freq, res, path);
                path.pop();
            }
        }

        dfs(&root, &freq, &mut res, &mut path);

        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let paths: Vec<Vec<String>> = deserialize(&read_line()?)?;
    let ans: Vec<Vec<String>> = Solution::delete_duplicate_folder(paths).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
