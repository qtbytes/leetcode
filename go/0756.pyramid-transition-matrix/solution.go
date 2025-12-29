// Created by none at 2025/12/29 14:16
// leetgo: dev
// https://leetcode.com/problems/pyramid-transition-matrix/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func pyramidTransition(bottom string, allowed []string) bool {
	shape := map[string][]byte{}

	for _, a := range allowed {
		shape[a[:2]] = append(shape[a[:2]], a[2])
	}

	var dfs func(row string, i int, path *[]byte) bool
	dfs = func(row string, i int, path *[]byte) bool {
		// fmt.Println(row, i, path)
		if len(row) == 2 {
			_, ok := shape[row]
			return ok
		}
		if i == len(row)-1 {
			// goto next row
			return dfs(string(*path), 0, &[]byte{})
		}
		s := row[i : i+2]
		if v, ok := shape[s]; ok {
			for _, ch := range v {
				*path = append(*path, ch)
				if dfs(row, i+1, path) {
					return true
				}
				*path = (*path)[:len(*path)-1]
			}

		} else {
			return false
		}
		return false
	}

	// fmt.Println(shape)
	return dfs(bottom, 0, &[]byte{})
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	bottom := Deserialize[string](ReadLine(stdin))
	allowed := Deserialize[[]string](ReadLine(stdin))
	ans := pyramidTransition(bottom, allowed)

	fmt.Println("\noutput:", Serialize(ans))
}
