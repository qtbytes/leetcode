// Created by none at 2024/11/15 14:25
// leetgo: 1.4.9
// https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func findLengthOfShortestSubarray(arr []int) int {
	n := len(arr)

	left := 0
	for i := 1; i < n; i++ {
		if arr[i] >= arr[i-1] {
			left = i
		} else {
			break
		}
	}
	if left == n-1 {
		return 0
	}
	right := n - 1
	for i := n - 2; i >= 0; i-- {
		if arr[i] <= arr[i+1] {
			right = i
		} else {
			break
		}
	}
	// 0..left  right..n
	res := min(n-left, right)
	r := right
	for l := range left + 1 {
		for r < n && arr[r] < arr[l] {
			r++
		}
		res = min(res, r-l-1)
	}
	return res

	/*
		return sort.Search(len(arr), func(i int) bool {
			if left+i+1 >= n || i >= right {
				return true
			}
			// 0 1 2 3 4 5
			for mid := right - i; mid <= left+1; mid++ {
				// delete mid..mid+i
				// 0..mid..mid+i..n
				if arr[mid+i] >= arr[mid-1] {
					return true
				}
			}
			return false
		})
	*/
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	arr := Deserialize[[]int](ReadLine(stdin))
	ans := findLengthOfShortestSubarray(arr)

	fmt.Println("\noutput:", Serialize(ans))
}
