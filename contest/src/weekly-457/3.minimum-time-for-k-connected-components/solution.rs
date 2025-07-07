// Created by none at 2025/07/07 17:28
// leetgo: dev
// https://leetcode.com/problems/minimum-time-for-k-connected-components/
// https://leetcode.com/contest/weekly-contest-457/problems/minimum-time-for-k-connected-components/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin

impl Solution {
    pub fn min_time(n: i32, edges: Vec<Vec<i32>>, k: i32) -> i32 {
        let n = n as usize;
        let k = k as usize;
        let mut l = 0;
        let mut r = 10_i32.pow(9) + 1;
        let check = |mid: i32| -> bool {
            let mut fa: Vec<usize> = (0..n).collect();
            let mut size = n;

            fn find(x: usize, fa: &mut Vec<usize>) -> usize {
                let mut y = x;
                while fa[y] != y {
                    y = fa[y];
                }
                fa[x] = y;
                return y;
            }

            fn union(x: usize, y: usize, fa: &mut Vec<usize>) -> bool {
                let fx = find(x, fa);
                let fy = find(y, fa);
                if fx == fy {
                    return false;
                }
                fa[fy] = fx;
                true
            }

            for e in &edges {
                let (x, y, t) = (e[0] as usize, e[1] as usize, e[2]);
                if t > mid {
                    if union(x, y, &mut fa) {
                        size -= 1;
                    }
                }
            }

            size >= k
        };

        while l < r {
            let mid = (l + r) >> 1;
            if check(mid) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        l
    }
}
// @lc code=end

fn main() -> Result<()> {
    let n: i32 = deserialize(&read_line()?)?;
    let edges: Vec<Vec<i32>> = deserialize(&read_line()?)?;
    let k: i32 = deserialize(&read_line()?)?;
    let ans: i32 = Solution::min_time(n, edges, k).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
