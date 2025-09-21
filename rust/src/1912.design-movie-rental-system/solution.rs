// Created by none at 2025/09/21 09:09
// leetgo: dev
// https://leetcode.com/problems/design-movie-rental-system/

#![allow(unused_imports)]

use anyhow::Result;
use leetgo_rs::*;

// @lc code=begin
use std::cmp::{Reverse, max, min};
use std::collections::*;
use std::mem::swap;

#[derive(Default)]
struct MovieRentingSystem {
    movie_to_shop: HashMap<i32, BTreeSet<(i32, i32)>>, // (moive: (price, shop))
    price: HashMap<(i32, i32), i32>,                   // ((shop,movie): price)
    rented: BTreeSet<(i32, i32, i32)>,                 // (price, shop, movie)
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MovieRentingSystem {
    fn new(_n: i32, entries: Vec<Vec<i32>>) -> Self {
        let mut mrs = MovieRentingSystem::default();
        for e in entries {
            let (shop, movie, price) = (e[0], e[1], e[2]);
            mrs.movie_to_shop
                .entry(movie)
                .or_default()
                .insert((price, shop));
            mrs.price.insert((shop, movie), price);
        }
        mrs
    }

    // - **Search**: Finds the **cheapest 5 shops** that have an **unrented copy** of a given movie. The
    // shops should be sorted by **price** in ascending order, and in case of a tie, the one with the
    // **smaller** `shopᵢ` should appear first. If there are less than 5 matching shops, then all of them
    // should be returned. If no shop has an unrented copy, then an empty list should be returned.
    fn search(&mut self, movie: i32) -> Vec<i32> {
        if let Some(root) = self.movie_to_shop.get(&movie) {
            return root.iter().take(5).map(|item| item.1).collect();
        }
        vec![]
    }

    // - **Rent**: Rents an **unrented copy** of a given movie from a given shop.
    fn rent(&mut self, shop: i32, movie: i32) {
        let price = self.price[&(shop, movie)];
        if let Some(root) = self.movie_to_shop.get_mut(&movie) {
            root.remove(&(price, shop));
        }
        self.rented.insert((price, shop, movie));
    }

    // - **Drop**: Drops off a **previously rented copy** of a given movie at a given shop.
    fn drop(&mut self, shop: i32, movie: i32) {
        let price = self.price[&(shop, movie)];
        self.movie_to_shop
            .get_mut(&movie)
            .unwrap()
            .insert((price, shop));
        self.rented.remove(&(price, shop, movie));
    }

    // - **Report**: Returns the **cheapest 5 rented movies** (possibly of the same movie ID) as a 2D list
    // `res` where `res[j] = [shopⱼ, movieⱼ]` describes that the `jᵗʰ` cheapest rented movie `movieⱼ` was
    // rented from the shop `shopⱼ`. The movies in `res` should be sorted by **price** in ascending order,
    // and in case of a tie, the one with the **smaller** `shopⱼ` should appear first, and if there is
    // still tie, the one with the **smaller** `movieⱼ` should appear first. If there are fewer than 5
    // rented movies, then all of them should be returned. If no movies are currently being rented, then an
    // empty list should be returned.

    fn report(&mut self) -> Vec<Vec<i32>> {
        self.rented
            .iter()
            .take(5)
            .map(|item| vec![item.1, item.2])
            .collect()
    }
}

// @lc code=end

fn main() -> Result<()> {
    let ops: Vec<String> = deserialize(&read_line()?)?;
    let params = split_array(&read_line()?)?;
    let mut output = Vec::with_capacity(ops.len());
    output.push("null".to_string());

    let constructor_params = split_array(&params[0])?;
    let n: i32 = deserialize(&constructor_params[0])?;
    let entries: Vec<Vec<i32>> = deserialize(&constructor_params[1])?;
    #[allow(unused_mut)]
    let mut obj = MovieRentingSystem::new(n, entries);

    for i in 1..ops.len() {
        match ops[i].as_str() {
            "search" => {
                let method_params = split_array(&params[i])?;
                let movie: i32 = deserialize(&method_params[0])?;
                let ans: Vec<i32> = obj.search(movie).into();
                output.push(serialize(ans)?);
            }
            "rent" => {
                let method_params = split_array(&params[i])?;
                let shop: i32 = deserialize(&method_params[0])?;
                let movie: i32 = deserialize(&method_params[1])?;
                obj.rent(shop, movie);
                output.push("null".to_string());
            }
            "drop" => {
                let method_params = split_array(&params[i])?;
                let shop: i32 = deserialize(&method_params[0])?;
                let movie: i32 = deserialize(&method_params[1])?;
                obj.drop(shop, movie);
                output.push("null".to_string());
            }
            "report" => {
                let ans: Vec<Vec<i32>> = obj.report().into();
                output.push(serialize(ans)?);
            }
            _ => panic!("unknown op"),
        }
    }

    println!("\noutput: {}", join_array(output));
    Ok(())
}
