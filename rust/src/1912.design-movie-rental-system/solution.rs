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
    movie_to_shop: HashMap<i32, BinaryHeap<(i32, i32)>>, // (moive: (-price, -shop))
    deleted1: HashSet<(i32, i32)>, // store items need to delete for movie_to_heap
    shop_to_movie: HashMap<i32, HashMap<i32, i32>>, // (shop: (movie: price))
    rented_heap: BinaryHeap<(i32, i32, i32)>, // (-price, -shop, -movie)
    deleted2: HashSet<(i32, i32, i32)>, // store items need to delete for rented_heap
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MovieRentingSystem {
    fn new(_n: i32, entries: Vec<Vec<i32>>) -> Self {
        let mut mrs = MovieRentingSystem::default();
        //  `entries[i] = [shopᵢ, movieᵢ, priceᵢ]`
        for e in entries {
            let (shop, movie, price) = (e[0], e[1], e[2]);
            mrs.movie_to_shop
                .entry(movie)
                .or_default()
                .push((-price, -shop));
            mrs.shop_to_movie
                .entry(shop)
                .or_default()
                .insert(movie, price);
        }
        mrs
    }

    // - **Search**: Finds the **cheapest 5 shops** that have an **unrented copy** of a given movie. The
    // shops should be sorted by **price** in ascending order, and in case of a tie, the one with the
    // **smaller** `shopᵢ` should appear first. If there are less than 5 matching shops, then all of them
    // should be returned. If no shop has an unrented copy, then an empty list should be returned.
    fn search(&mut self, movie: i32) -> Vec<i32> {
        let mut res = vec![];
        let mut restore = vec![];
        if let Some(heap) = self.movie_to_shop.get_mut(&movie) {
            for _ in 0..5 {
                while let Some(m) = heap.pop() {
                    if self.deleted1.contains(&m) {
                        self.deleted1.remove(&m);
                        continue;
                    }
                    res.push(-m.1);
                    restore.push(m);
                    break;
                }
            }
            for m in restore {
                heap.push(m);
            }
        }
        res
    }

    // - **Rent**: Rents an **unrented copy** of a given movie from a given shop.
    fn rent(&mut self, shop: i32, movie: i32) {
        let price = self.shop_to_movie[&shop][&movie];

        self.deleted1.insert((-price, -shop));

        if !self.deleted2.remove(&(-price, -shop, -movie)) {
            self.rented_heap.push((-price, -shop, -movie));
        }
    }

    // - **Drop**: Drops off a **previously rented copy** of a given movie at a given shop.
    fn drop(&mut self, shop: i32, movie: i32) {
        let price = self.shop_to_movie[&shop][&movie];

        if !self.deleted1.remove(&(-price, -shop)) {
            self.movie_to_shop
                .entry(movie)
                .or_default()
                .push((-price, -shop));
        }

        self.deleted2.insert((-price, -shop, -movie));
    }

    // - **Report**: Returns the **cheapest 5 rented movies** (possibly of the same movie ID) as a 2D list
    // `res` where `res[j] = [shopⱼ, movieⱼ]` describes that the `jᵗʰ` cheapest rented movie `movieⱼ` was
    // rented from the shop `shopⱼ`. The movies in `res` should be sorted by **price** in ascending order,
    // and in case of a tie, the one with the **smaller** `shopⱼ` should appear first, and if there is
    // still tie, the one with the **smaller** `movieⱼ` should appear first. If there are fewer than 5
    // rented movies, then all of them should be returned. If no movies are currently being rented, then an
    // empty list should be returned.

    fn report(&mut self) -> Vec<Vec<i32>> {
        let mut res = vec![];
        let mut restore = vec![];

        for _ in 0..5 {
            while let Some(item) = self.rented_heap.pop() {
                if self.deleted2.contains(&item) {
                    self.deleted2.remove(&item);
                    continue;
                }
                let (_, shop, movie) = (-item.0, -item.1, -item.2);
                res.push(vec![shop, movie]);
                restore.push(item);
                break;
            }
        }

        for item in restore {
            self.rented_heap.push(item);
        }

        res
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
