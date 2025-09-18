// Created by none at 2025/09/18 09:18
// leetgo: dev
// https://leetcode.com/problems/design-task-manager/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

// @lc code=begin
use std::cmp::{Ordering, Reverse, max, min};
use std::collections::*;
use std::mem::swap;

#[derive(Default)]
struct TaskManager {
    q: BinaryHeap<(i32, i32)>,
    map: HashMap<i32, (i32, i32)>,
}

impl TaskManager {
    fn new(tasks: Vec<Vec<i32>>) -> Self {
        let mut manager = Self::default();
        for t in tasks {
            manager.add(t[0], t[1], t[2]);
        }
        manager
    }

    fn add(&mut self, user_id: i32, task_id: i32, priority: i32) {
        self.q.push((priority, task_id));
        self.map.insert(task_id, (priority, user_id));
    }

    fn edit(&mut self, task_id: i32, new_priority: i32) {
        let user_id = self.map[&task_id].1;
        self.add(user_id, task_id, new_priority);
    }

    fn rmv(&mut self, task_id: i32) {
        *self.map.get_mut(&task_id).unwrap() = (-1, -1);
    }

    fn exec_top(&mut self) -> i32 {
        while let Some((priority, task_id)) = self.q.pop() {
            if priority == self.map[&task_id].0 {
                let user_id = self.map[&task_id].1;
                self.rmv(task_id);
                return user_id;
            }
        }
        return -1;
    }
}

// @lc code=end

fn main() -> Result<()> {
    let ops: Vec<String> = deserialize(&read_line()?)?;
    let params = split_array(&read_line()?)?;
    let mut output = Vec::with_capacity(ops.len());
    output.push("null".to_string());

    let constructor_params = split_array(&params[0])?;
    let tasks: Vec<Vec<i32>> = deserialize(&constructor_params[0])?;
    #[allow(unused_mut)]
    let mut obj = TaskManager::new(tasks);

    for i in 1..ops.len() {
        match ops[i].as_str() {
            "add" => {
                let method_params = split_array(&params[i])?;
                let user_id: i32 = deserialize(&method_params[0])?;
                let task_id: i32 = deserialize(&method_params[1])?;
                let priority: i32 = deserialize(&method_params[2])?;
                obj.add(user_id, task_id, priority);
                output.push("null".to_string());
            }
            "edit" => {
                let method_params = split_array(&params[i])?;
                let task_id: i32 = deserialize(&method_params[0])?;
                let new_priority: i32 = deserialize(&method_params[1])?;
                obj.edit(task_id, new_priority);
                output.push("null".to_string());
            }
            "rmv" => {
                let method_params = split_array(&params[i])?;
                let task_id: i32 = deserialize(&method_params[0])?;
                obj.rmv(task_id);
                output.push("null".to_string());
            }
            "execTop" => {
                let ans: i32 = obj.exec_top().into();
                output.push(serialize(ans)?);
            }
            _ => panic!("unknown op"),
        }
    }

    println!("\noutput: {}", join_array(output));
    Ok(())
}
