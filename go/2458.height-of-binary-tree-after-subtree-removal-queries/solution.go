// Created by none at 2024/10/26 12:22
// leetgo: 1.4.9
// https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func treeQueries(root *TreeNode, queries []int) []int {
	height := make(map[int]int)

	var calcHeight func(root *TreeNode) int

	calcHeight = func(root *TreeNode) int {
		if root == nil {
			return -1
		}
		left := calcHeight(root.Left)
		right := calcHeight(root.Right)

		height[root.Val] = 1 + max(left, right)
		return height[root.Val]
	}

	calcHeight(root)

	n := len(height)
	res := make([]int, n+1)

	var dfs func(root *TreeNode, max_height int, h int)

	dfs = func(root *TreeNode, max_height int, h int) {
		if root == nil {
			return
		}
		// try remove root.left
		if root.Left != nil {
			ans := max(max_height, h)
			if root.Right != nil {
				ans = max(ans, h+1+height[root.Right.Val])
				dfs(root.Left, ans, h+1)
			} else {
				dfs(root.Left, ans, h+1)
			}
			res[root.Left.Val] = ans

		}
		// try remove root.right
		if root.Right != nil {
			ans := max(h, max_height)
			if root.Left != nil {
				ans = max(ans, h+1+height[root.Left.Val])
				dfs(root.Right, ans, h+1)
			} else {
				dfs(root.Right, ans, h+1)
			}
			res[root.Right.Val] = ans
		}
	}

	dfs(root, 0, 0)

	// fmt.Println(res)
	for i, q := range queries {
		queries[i] = res[q]
	}

	return queries

}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	root := Deserialize[*TreeNode](ReadLine(stdin))
	queries := Deserialize[[]int](ReadLine(stdin))
	ans := treeQueries(root, queries)

	fmt.Println("\noutput:", Serialize(ans))
}
