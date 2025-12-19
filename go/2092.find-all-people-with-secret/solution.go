// Created by none at 2025/12/19 12:05
// leetgo: dev
// https://leetcode.com/problems/find-all-people-with-secret/

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

func findAllPeople(n int, meetings [][]int, firstPerson int) []int {
	g := make(map[int][][]int)
	var ts []int

	for _, m := range meetings {
		g[m[2]] = append(g[m[2]], []int{m[0], m[1]})
		ts = append(ts, m[2])

	}

	sort.Ints(ts)
	ts = slices.Compact(ts)

	ans := make([]bool, n)
	ans[0] = true
	ans[firstPerson] = true
	all := n - 2

	for _, t := range ts {
		// try to split group
		group := g[t]
		edges := make(map[int][]int)
		seen := make(map[int]int)
		for _, e := range group {
			x, y := e[0], e[1]
			edges[x] = append(edges[x], y)
			edges[y] = append(edges[y], x)
			seen[x] = -1
			seen[y] = -1
		}

		t := -1
		var dfs func(x int, seen *map[int]int)
		dfs = func(x int, seen *map[int]int) {
			for _, y := range edges[x] {
				if (*seen)[y] == -1 {
					(*seen)[y] = t
					dfs(y, seen)
				}
			}
		}

		for x := range seen {
			if seen[x] == -1 {
				t++
				seen[x] = t
				dfs(x, &seen)
			}
		}

		ok := make([]bool, t+1)
		groups := make([][]int, t+1)
		for x, t := range seen {
			if ans[x] {
				ok[t] = true
			} else {
				groups[t] = append(groups[t], x)
			}
		}
		// fmt.Println(groups, ok)

		for t := range ok {
			if ok[t] {
				for _, x := range groups[t] {
					ans[x] = true
					all--
				}
			}
		}
		if all == 0 {
			break
		}
	}

	var res []int
	for x, ok := range ans {
		if ok {
			res = append(res, x)
		}
	}
	return res
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
