// Created by none at 2025/11/07 13:32
// leetgo: dev
// https://leetcode.com/problems/maximize-the-minimum-powered-city/

package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func maxPower(stations []int, r int, k int) int64 {
	left := slices.Min(stations)
	right := k + 1
	for _, x := range stations {
		right += x
	}
	check := func(mid int) bool {
		a := slices.Clone(stations)
		s := 0
		need := 0
		l := 0
		for i := range r {
			s += a[i]
		}
		for i := r; i < len(a); i++ {
			s += a[i]
			for l < i-2*r {
				s -= a[l]
				l++
			}
			if s < mid {
				a[i] += mid - s
				need += mid - s
				s = mid
			}
		}
		// fmt.Println(mid, l)
		for i := len(a) - r; i < len(a); i++ {
			for l < i-r {
				s -= a[l]
				l++
			}
			if s < mid {
				a[i] += mid - s
				need += mid - s
				s = mid
			}
		}
		// fmt.Println(mid, need, a)
		return need <= k
	}
	for left < right {
		mid := (left + right + 1) >> 1
		if check(mid) {
			left = mid
		} else {
			right = mid - 1
		}
	}
	return int64(left)
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	stations := Deserialize[[]int](ReadLine(stdin))
	r := Deserialize[int](ReadLine(stdin))
	k := Deserialize[int](ReadLine(stdin))
	ans := maxPower(stations, r, k)

	fmt.Println("\noutput:", Serialize(ans))
}
