// Created by none at 2025/07/07 17:28
// leetgo: dev
// https://leetcode.com/problems/minimum-moves-to-reach-target-in-grid/
// https://leetcode.com/contest/weekly-contest-457/problems/minimum-moves-to-reach-target-in-grid/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin

impl Solution {
    pub fn min_moves(sx: i32, sy: i32, tx: i32, ty: i32) -> i32 {
        if sx == tx && sy == ty {
            return 0;
        }
        if sx > tx || sy > ty {
            return -1;
        }
        if sx & 1 == 0 && sy & 1 == 0 && (tx & 1 != 0 || ty & 1 != 0) {
            return -1;
        }
        if sx == 0 && sy == 0 {
            return -1;
        }
        let res;
        if tx == ty {
            res = match (sx, sy) {
                (0, _) => Solution::min_moves(sx, sy, 0, ty),
                (_, 0) => Solution::min_moves(sx, sy, tx, 0),
                _ => -1,
            }
        } else if tx < ty {
            if (tx * 2) < ty && ty & 1 == 1 {
                res = -1
            } else {
                res = Solution::min_moves(sx, sy, tx, ty - tx.max(ty >> 1));
            }
        } else {
            if (ty * 2) < tx && tx & 1 == 1 {
                res = -1
            } else {
                res = Solution::min_moves(sx, sy, tx - ty.max(tx >> 1), ty);
            }
        }
        if res == -1 { -1 } else { 1 + res }
    }
}

// @lc code=end

fn main() -> Result<()> {
    let sx: i32 = deserialize(&read_line()?)?;
    let sy: i32 = deserialize(&read_line()?)?;
    let tx: i32 = deserialize(&read_line()?)?;
    let ty: i32 = deserialize(&read_line()?)?;
    let ans: i32 = Solution::min_moves(sx, sy, tx, ty).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}
