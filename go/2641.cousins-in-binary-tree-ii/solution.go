// Created by none at 2024/10/23 14:00
// leetgo: 1.4.9
// https://leetcode.cn/problems/cousins-in-binary-tree-ii/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

const N = int(1e5)

func replaceValueInTree(root *TreeNode) *TreeNode {
	depth := make([]int, N)
	var dfs func(root *TreeNode, h int)
	dfs = func(root *TreeNode, h int) {
		if root == nil {
			return
		}
		depth[h] += root.Val
		dfs(root.Left, h+1)
		dfs(root.Right, h+1)
		if root.Left != nil && root.Right != nil {
			s := root.Left.Val + root.Right.Val
			root.Left.Val, root.Right.Val = s, s
		}
	}
	dfs(root, 0)

	// change root value
	var dfs2 func(root *TreeNode, h int)
	dfs2 = func(root *TreeNode, h int) {
		if root == nil {
			return
		}
		root.Val = depth[h] - root.Val
		dfs2(root.Left, h+1)
		dfs2(root.Right, h+1)
	}
	dfs2(root, 0)
	return root
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	root := Deserialize[*TreeNode](ReadLine(stdin))
	ans := replaceValueInTree(root)

	fmt.Println("\noutput:", Serialize(ans))
}
