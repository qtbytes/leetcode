// Created by none at 2025/12/19 12:05
// leetgo: dev
// https://leetcode.com/problems/find-all-people-with-secret/

package main

import (
	"bufio"
	"fmt"
	"maps"
	"os"
	"slices"
	"sort"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func findAllPeople(n int, meetings [][]int, firstPerson int) []int {
	g := make(map[int][][]int)
	var ts []int

	for _, m := range meetings {
		g[m[2]] = append(g[m[2]], []int{m[0], m[1]})
		ts = append(ts, m[2])

	}

	sort.Ints(ts)
	ts = slices.Compact(ts)

	know := map[int]bool{}
	know[0] = true
	know[firstPerson] = true

	for _, t := range ts {
		// try to split group
		group := g[t]
		edges := make(map[int][]int)
		for _, e := range group {
			x, y := e[0], e[1]
			edges[x] = append(edges[x], y)
			edges[y] = append(edges[y], x)
		}

		seen := map[int]bool{}
		var dfs func(x int)
		dfs = func(x int) {
			seen[x] = true
			for _, y := range edges[x] {
				if !seen[y] {
					know[y] = true
					dfs(y)
				}
			}
		}

		for x := range edges {
			if !seen[x] && know[x] {
				dfs(x)
			}
		}
	}

	return slices.Collect(maps.Keys(know))
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	n := Deserialize[int](ReadLine(stdin))
	meetings := Deserialize[[][]int](ReadLine(stdin))
	firstPerson := Deserialize[int](ReadLine(stdin))
	ans := findAllPeople(n, meetings, firstPerson)

	fmt.Println("\noutput:", Serialize(ans))
}
