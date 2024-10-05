// Created by none at 2024/10/05 12:41
// leetgo: 1.4.9
// https://leetcode.cn/problems/minimum-time-to-complete-trips/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func minimumTime(time []int, totalTrips int) int64 {
	l, r := int64(1), int64(time[0])*int64(totalTrips)
	var check = func(mid int64) bool {
		res := int64(0)
		for _, t := range time {
			res += (mid / int64(t))
		}
		return res >= int64(totalTrips)
	}
	for l < r {
		mid := (l + r) >> 1
		if check(mid) {
			r = mid
		} else {
			l = mid + 1
		}
	}
	return l

}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	time := Deserialize[[]int](ReadLine(stdin))
	totalTrips := Deserialize[int](ReadLine(stdin))
	ans := minimumTime(time, totalTrips)

	fmt.Println("\noutput:", Serialize(ans))
}
