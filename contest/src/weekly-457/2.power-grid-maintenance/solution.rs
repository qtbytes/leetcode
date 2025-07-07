// Created by none at 2025/07/07 17:28
// leetgo: dev
// https://leetcode.com/problems/power-grid-maintenance/
// https://leetcode.com/contest/weekly-contest-457/problems/power-grid-maintenance/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::{HashMap, HashSet, VecDeque};

impl Solution {
    pub fn process_queries(c: i32, connections: Vec<Vec<i32>>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = c as usize;
        let mut g = vec![vec![]; n + 1];
        for e in connections {
            let (x, y) = (e[0] as usize, e[1] as usize);
            g[x].push(y);
            g[y].push(x);
        }

        let mut group_id = 0;
        let mut group = vec![];
        let mut map = HashMap::new();
        let mut visited = vec![false; n + 1];

        for x in 1..=n {
            if visited[x] {
                continue;
            }
            let mut dq = VecDeque::new();
            let mut v = vec![];
            dq.push_back(x);
            v.push(x);
            visited[x] = true;
            while let Some(x) = dq.pop_front() {
                for &y in &g[x] {
                    if !visited[y] {
                        visited[y] = true;
                        dq.push_back(y);
                        v.push(y);
                    }
                }
            }
            for &x in &v {
                map.insert(x, group_id);
            }
            v.sort_unstable_by_key(|&x| Reverse(x));
            group_id += 1;
            group.push(v);
        }

        let mut deleted = HashSet::new();
        let mut res = vec![];

        for q in queries {
            let x = q[1] as usize;
            let id = map[&x];
            if q[0] == 1 {
                if !deleted.contains(&x) {
                    res.push(x as i32);
                    continue;
                }
                while !group[id].is_empty() && deleted.contains(group[id].last().unwrap()) {
                    group[id].pop();
                }
                if !group[id].is_empty() {
                    res.push(group[id].last().map_or_else(|| -1, |x| (*x as i32)));
                } else {
                    res.push(-1);
                }
            } else {
                deleted.insert(x);
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
