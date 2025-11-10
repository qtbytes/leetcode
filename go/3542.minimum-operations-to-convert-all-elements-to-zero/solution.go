// Created by none at 2025/11/10 20:01
// leetgo: dev
// https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/

package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
	"sort"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func minOperations(nums []int) int {
	index := make(map[int][]int)
	for i, x := range nums {
		index[x] = append(index[x], i)
	}
	// fmt.Println(index)
	var keys []int
	for key := range index {
		keys = append(keys, key)
	}
	sort.Ints(keys)
	slices.Reverse(keys)
	res := 0
	fa := make([]int, len(nums))
	for i := range fa {
		fa[i] = i
	}
	var find func(x int) int
	find = func(x int) int {
		if fa[x] != x {
			fa[x] = find(fa[x])
		}
		return fa[x]
	}
	union := func(x, y int) bool {
		fx, fy := find(x), find(y)
		if fx == fy {
			return false
		}
		fa[fy] = fx
		return true
	}
	used := make([]bool, len(nums))
	n := len(nums)
	for _, key := range keys {
		v := index[key]
		for _, i := range v {
			if i > 0 && used[i-1] {
				union(i, i-1)
			}
			if i+1 < n && used[i+1] {
				union(i+1, i)
			}
			used[i] = true
		}
		if key == 0 {
			continue
		}
		res++
		for i := range len(v) - 1 {
			if find(v[i]) != find(v[i+1]) {
				res++
			}
		}
	}

	return res
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	nums := Deserialize[[]int](ReadLine(stdin))
	ans := minOperations(nums)

	fmt.Println("\noutput:", Serialize(ans))
}
