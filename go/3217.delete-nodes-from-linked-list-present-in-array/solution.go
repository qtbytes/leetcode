// Created by none at 2025/11/01 18:09
// leetgo: dev
// https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

func modifiedList(nums []int, head *ListNode) *ListNode {
	set := make(map[int]bool, len(nums))
	for _, x := range nums {
		set[x] = true
	}

	dummy := new(ListNode)
	dummy.Next = head
	p := dummy
	for p != nil && p.Next != nil {
		for p.Next != nil && set[p.Next.Val] {
			p.Next = p.Next.Next
		}
		p = p.Next
	}

	return dummy.Next
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	nums := Deserialize[[]int](ReadLine(stdin))
	head := Deserialize[*ListNode](ReadLine(stdin))
	ans := modifiedList(nums, head)

	fmt.Println("\noutput:", Serialize(ans))
}
