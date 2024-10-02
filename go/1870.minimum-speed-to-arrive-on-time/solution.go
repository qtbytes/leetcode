// Created by none at 2024/10/02 14:06
// leetgo: 1.4.9
// https://leetcode.cn/problems/minimum-speed-to-arrive-on-time/

package main

import (
	"bufio"
	"fmt"
	"math"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func minSpeedOnTime(dist []int, hour float64) int {
	n := len(dist)
	if hour <= float64(n-1) {
		return -1
	}

	h := int(math.Round(hour * 100.0))
	mx := 0
	for i := range dist {
		mx = max(mx, dist[i])
	}

	l, r := 1, mx*100
	var check = func(mid int) bool {
		res := 0
		for i := 0; i < n-1; i++ {
			if i < n-1 {
				res += (dist[i] + mid - 1) / mid
			}
		}
		return (res*mid+dist[n-1])*100 <= h*mid
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
	dist := Deserialize[[]int](ReadLine(stdin))
	hour := Deserialize[float64](ReadLine(stdin))
	ans := minSpeedOnTime(dist, hour)

	fmt.Println("\noutput:", Serialize(ans))
}
