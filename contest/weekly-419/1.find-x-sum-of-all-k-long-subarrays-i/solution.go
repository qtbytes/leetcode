// Created by none at 2024/10/13 15:11
// leetgo: 1.4.9
// https://leetcode.cn/problems/find-x-sum-of-all-k-long-subarrays-i/
// https://leetcode.cn/contest/weekly-contest-419/problems/find-x-sum-of-all-k-long-subarrays-i/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func findXSum(nums []int, k int, x int) []int {

}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	nums := Deserialize[[]int](ReadLine(stdin))
	k := Deserialize[int](ReadLine(stdin))
	x := Deserialize[int](ReadLine(stdin))
	ans := findXSum(nums, k, x)

	fmt.Println("\noutput:", Serialize(ans))
}
