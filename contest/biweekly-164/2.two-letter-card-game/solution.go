// Created by none at 2025/09/11 20:52
// leetgo: dev
// https://leetcode.com/problems/two-letter-card-game/
// https://leetcode.com/contest/biweekly-contest-164/problems/two-letter-card-game/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin
type stat struct {
	cnt        map[string]int
	max, total int
}

func score(cards []string, x byte) int {
	left := stat{cnt: make(map[string]int)}
	right := stat{cnt: make(map[string]int)}
	both := 0
	for _, card := range cards {
		bit := 0
		for i, c := range card {
			if c == rune(x) {
				bit |= 1 << i
			}
		}
		switch bit {
		case 1:
			left.cnt[card]++
			left.max = max(left.max, left.cnt[card])
			left.total++
		case 2:
			right.cnt[card]++
			right.max = max(right.max, right.cnt[card])
			right.total++
		case 3:
			both++
		}
	}

	calc := func(s stat, b int) int {
		x, y := s.max, s.total-s.max
		if x <= y+b {
			return min(x+y, (x+y+b)/2)
		}
		return min(x, y+b)
	}
	res := 0
	for l := range both + 1 {
		r := both - l
		// use l to group 1, r to group 2
		res = max(res, calc(left, l)+calc(right, r))
	}
	return res

	// Wrong greedy solution: we don't know how to split both to 2 group

	// res := 0
	// for _, s := range [2]stat{left, right} {
	// 	x, y := s.max, s.total-s.max
	// 	// fmt.Println(both)
	// 	// use both first
	// 	if y+both < x {
	// 		res += y + both
	// 		both = 0
	// 	} else if both >= s.total {
	// 		res += s.total
	// 		both -= s.total
	// 	} else {
	// 		delta := min((s.total+both)/2, s.total)
	// 		res += delta
	// 		both -= max(0, 2*delta-s.total)
	// 	}
	// 	// fmt.Println(both)
	// 	// fmt.Println(s, both, res)
	// }
	// return res
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	cards := Deserialize[[]string](ReadLine(stdin))
	x := Deserialize[byte](ReadLine(stdin))
	ans := score(cards, x)

	fmt.Println("\noutput:", Serialize(ans))
}
