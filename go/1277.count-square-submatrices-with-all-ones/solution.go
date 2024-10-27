// Created by none at 2024/10/27 13:23
// leetgo: 1.4.9
// https://leetcode.com/problems/count-square-submatrices-with-all-ones/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

// func calc(f *[]int) int {
// 	n := len(*f)

// 	left := make([]int, n)
// 	right := make([]int, n)
// 	for i := range right {
// 		right[i] = n - 1
// 	}
// 	st := []int{}
// 	for i, x := range *f {
// 		for len(st) > 0 && x < (*f)[st[len(st)-1]] {
// 			j := st[len(st)-1]
// 			st = st[:len(st)-1]
// 			right[j] = i - 1
// 		}
// 		if len(st) > 0 {
// 			left[i] = st[len(st)-1] + 1
// 		}
// 		st = append(st, i)
// 	}

//		res := 0
//		for i, x := range *f {
//			res += x * (right[i] - left[i] + 1)
//		}
//		fmt.Println(left, right)
//		fmt.Println(f, res)
//		return res
//	}

func countSquares(matrix [][]int) int {
	m, n := len(matrix), len(matrix[0])
	f := make([][]int, m+1)
	for i := range f {
		f[i] = make([]int, n+1)
	}
	for i, row := range matrix {
		for j, x := range row {
			f[i+1][j+1] = x + f[i+1][j] + f[i][j+1] - f[i][j]
		}
	}

	check := func(i, j, k int) bool {
		x, y := i+k, j+k
		return f[x+1][y+1]-f[x+1][j]-f[i][y+1]+f[i][j] == (k+1)*(k+1)
	}

	res := 0
	for i, row := range matrix {
		for j, x := range row {
			if x == 1 {
				res++
				for k := 1; i+k < m && j+k < n; k++ {
					if check(i, j, k) {
						// fmt.Println(i, j, k)
						res++
					} else {
						break
					}
				}
			}
		}
	}
	return res
	// res := 0
	// f := make([]int, n)
	// for _, row := range matrix {
	// 	for j, x := range row {
	// 		if x == 1 {
	// 			f[j]++
	// 		} else {
	// 			f[j] = 0
	// 		}
	// 	}
	// 	res += calc(&f)
	// }

	// return res
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	matrix := Deserialize[[][]int](ReadLine(stdin))
	ans := countSquares(matrix)

	fmt.Println("\noutput:", Serialize(ans))
}
