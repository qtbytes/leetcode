// Created by none at 2025/12/04 12:56
// leetgo: dev
// https://leetcode.com/problems/count-collisions-on-a-road/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func countCollisions(directions string) int {
	res := 0
	cntR := 0
	hasS := false
	for _, ch := range directions {
		switch ch {
		case 'L':
			if cntR > 0 || hasS {
				res += cntR + 1
				cntR = 0
				hasS = true
			}
		case 'S':
			res += cntR
			cntR = 0
			hasS = true
		default:
			hasS = false
			cntR++

		}
	}
	return res
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	directions := Deserialize[string](ReadLine(stdin))
	ans := countCollisions(directions)

	fmt.Println("\noutput:", Serialize(ans))
}
