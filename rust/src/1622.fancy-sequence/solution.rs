// Created by none at 2026/03/15 13:31
// leetgo: dev
// https://leetcode.com/problems/fancy-sequence/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;
use std::ops::{Add, Mul};

const MOD: i64 = 1_000_000_007;

/// Computes a^b % MOD
fn mod_pow(mut a: i64, mut b: i64) -> i64 {
    let mut res = 1;
    a %= MOD;

    while b > 0 {
        if b & 1 == 1 {
            res = res * a % MOD;
        }
        a = a * a % MOD;
        b >>= 1;
    }

    res
}

/// Computes the modular inverse of `a` modulo 1e9+7
fn mod_inv(a: i64) -> i64 {
    mod_pow(a, MOD - 2)
}

// y = kx + b
struct Fancy {
    k: i64,
    b: i32,
    vals: Vec<i32>,
}

impl Fancy {
    fn new() -> Self {
        Self {
            k: 1,
            b: 0,
            vals: Vec::new(),
        }
    }

    fn append(&mut self, val: i32) {
        // now we should get x from y
        // y = (kx + b) % MOD => x = (y - b) / k => x = (y - b) * inv(k) % MOD
        let mut x = (val as i64 - self.b as i64 + MOD) % MOD;
        x = (x * mod_inv(self.k)) % MOD;
        self.vals.push(x as i32);
    }

    fn add_all(&mut self, inc: i32) {
        self.b = (self.b + inc) % MOD as i32;
    }

    fn mult_all(&mut self, m: i32) {
        self.k = (self.k * m as i64) % MOD;
        self.b = ((self.b as i64 * m as i64) % MOD) as i32;
    }

    fn get_index(&self, idx: i32) -> i32 {
        let i = idx as usize;
        if i >= self.vals.len() {
            return -1;
        }
        let mut x = self.vals[i] as i64;
        x = (x * self.k as i64 + self.b as i64) % MOD;
        x as i32
    }
}

// @lc code=end

fn main() -> Result<()> {
    let ops: Vec<String> = deserialize(&read_line()?)?;
    let params = split_array(&read_line()?)?;
    let mut output = Vec::with_capacity(ops.len());
    output.push("null".to_string());

    #[allow(unused_mut)]
    let mut obj = Fancy::new();

    for i in 1..ops.len() {
        match ops[i].as_str() {
            "append" => {
                let method_params = split_array(&params[i])?;
                let val: i32 = deserialize(&method_params[0])?;
                obj.append(val);
                output.push("null".to_string());
            }
            "addAll" => {
                let method_params = split_array(&params[i])?;
                let inc: i32 = deserialize(&method_params[0])?;
                obj.add_all(inc);
                output.push("null".to_string());
            }
            "multAll" => {
                let method_params = split_array(&params[i])?;
                let m: i32 = deserialize(&method_params[0])?;
                obj.mult_all(m);
                output.push("null".to_string());
            }
            "getIndex" => {
                let method_params = split_array(&params[i])?;
                let idx: i32 = deserialize(&method_params[0])?;
                let ans: i32 = obj.get_index(idx).into();
                output.push(serialize(ans)?);
            }
            _ => panic!("unknown op"),
        }
    }

    println!("\noutput: {}", join_array(output));
    Ok(())
}
