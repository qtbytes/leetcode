// Created by none at 2024/11/11 14:03
// leetgo: 1.4.9
// https://leetcode.com/problems/prime-subtraction-operation/

package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin
const N int = 1001

var primes = []int{}

func init() {
	f := make([]bool, N)
	for i := 2; i < N; i++ {
		f[i] = true
	}
	for i := 2; i < N; i++ {
		if f[i] {
			for j := i + i; j < N; j += i {
				f[j] = false
			}
			primes = append(primes, i)
		}
	}
}

func primeSubOperation(nums []int) bool {
	start := 0
	for _, x := range nums {
		if x <= start {
			return false
		}
		// try to make x -> start + 1
		// find the max prime <= x - (start + 1)
		target := x - (start + 1)
		i := sort.Search(len(primes), func(i int) bool {
			return primes[i] > target
		})
		if i > 0 {
			start = x - primes[i-1]
		} else {
			start = x
		}
	}
	return true
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	nums := Deserialize[[]int](ReadLine(stdin))
	ans := primeSubOperation(nums)

	fmt.Println("\noutput:", Serialize(ans))
}
