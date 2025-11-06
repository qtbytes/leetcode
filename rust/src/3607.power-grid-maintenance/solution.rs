// Created by none at 2025/11/06 20:55
// leetgo: dev
// https://leetcode.com/problems/power-grid-maintenance/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn process_queries(c: i32, connections: Vec<Vec<i32>>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = c as usize + 1;
        let mut g = vec![vec![]; n];
        for c in connections {
            let x = c[0] as usize;
            let y = c[1] as usize;
            g[x].push(y);
            g[y].push(x);
        }
        let mut groups: Vec<BinaryHeap<Reverse<usize>>> = vec![];
        let mut map = vec![0; n];
        let mut visited = vec![false; n];
        for i in 1..n {
            if visited[i] {
                continue;
            }
            fn dfs(
                x: usize,
                fa: usize,
                g: &Vec<Vec<usize>>,
                visited: &mut Vec<bool>,
                cur: &mut Vec<usize>,
            ) {
                if visited[x] {
                    return;
                }
                cur.push(x);
                visited[x] = true;
                for &y in &g[x] {
                    if y == fa {
                        continue;
                    }
                    dfs(y, x, g, visited, cur);
                }
            }
            let mut cur: Vec<usize> = vec![];
            dfs(i, n + 1, &g, &mut visited, &mut cur);
            for &node in &cur {
                map[node] = groups.len();
            }
            groups.push(cur.iter().map(|&x| Reverse(x)).collect());
        }
        let mut res = vec![];
        let mut deleted = vec![false; n];
        for q in queries {
            let x = q[1] as usize;
            match q[0] {
                1 => {
                    if !deleted[x] {
                        res.push(x as i32);
                        continue;
                    }
                    let group = groups.get_mut(map[x]).unwrap();
                    while let Some(Reverse(y)) = group.peek() {
                        if deleted[*y] {
                            group.pop();
                        } else {
                            break;
                        }
                    }
                    if let Some(Reverse(y)) = group.peek() {
                        res.push(*y as i32);
                    } else {
                        res.push(-1);
                    }
                }
                2 => deleted[x] = true,
                _ => {}
            }
        }

        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let c: i32 = deserialize(&read_line()?)?;
    let connections: Vec<Vec<i32>> = deserialize(&read_line()?)?;
    let queries: Vec<Vec<i32>> = deserialize(&read_line()?)?;
    let ans: Vec<i32> = Solution::process_queries(c, connections, queries).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
