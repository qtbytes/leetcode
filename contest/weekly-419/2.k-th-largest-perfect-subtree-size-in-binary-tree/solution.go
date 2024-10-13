// Created by none at 2024/10/13 15:11
// leetgo: 1.4.9
// https://leetcode.cn/problems/k-th-largest-perfect-subtree-size-in-binary-tree/
// https://leetcode.cn/contest/weekly-contest-419/problems/k-th-largest-perfect-subtree-size-in-binary-tree/

package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func kthLargestPerfectSubtree(root *TreeNode, k int) int {

	var dfs func(root *TreeNode) int

	size := []int{}
	dfs = func(root *TreeNode) int {
		if root == nil {
			return 0
		}
		left := dfs(root.Left)
		right := dfs(root.Right)
		if left == right && left != -1 {
			size = append(size, 2*left+1)
			return 2*left + 1
		}
		return -1
	}

	dfs(root)
	if len(size) < k {
		return -1
	}
	sort.Slice(size, func(i, j int) bool { return size[i] > size[j] })
	return size[k-1]

}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	root := Deserialize[*TreeNode](ReadLine(stdin))
	k := Deserialize[int](ReadLine(stdin))
	ans := kthLargestPerfectSubtree(root, k)

	fmt.Println("\noutput:", Serialize(ans))
}
