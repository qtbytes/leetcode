// Created by none at 2024/10/24 21:16
// leetgo: 1.4.9
// https://leetcode.cn/problems/flip-equivalent-binary-trees/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func flipEquiv(root1 *TreeNode, root2 *TreeNode) bool {
	if root1 == nil && root2 == nil {
		return true
	}
	if root1 == nil || root2 == nil {
		return false
	}
	return root1.Val == root2.Val &&
		(flipEquiv(root1.Left, root2.Right) && flipEquiv(root1.Right, root2.Left) ||
			flipEquiv(root1.Left, root2.Left) && flipEquiv(root1.Right, root2.Right))
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	root1 := Deserialize[*TreeNode](ReadLine(stdin))
	root2 := Deserialize[*TreeNode](ReadLine(stdin))
	ans := flipEquiv(root1, root2)

	fmt.Println("\noutput:", Serialize(ans))
}
