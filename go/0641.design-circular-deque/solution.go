// Created by none at 2024/09/28 13:38
// leetgo: 1.4.9
// https://leetcode.cn/problems/design-circular-deque/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

type MyCircularDeque struct {
	front []int
	end   []int
	size  int
}

func Constructor(k int) MyCircularDeque {
	front := []int{}
	end := []int{}

	return MyCircularDeque{front, end, k}
}

func (m *MyCircularDeque) InsertFront(value int) bool {
	if m.IsFull() {
		return false
	}
	m.front = append(m.front, value)
	return true
}

func (m *MyCircularDeque) InsertLast(value int) bool {
	if m.IsFull() {
		return false
	}
	m.end = append(m.end, value)
	return true

}

func (m *MyCircularDeque) DeleteFront() bool {
	if m.IsEmpty() {
		return false
	}
	if len(m.front) > 0 {
		m.front = m.front[:len(m.front)-1]
	} else {
		m.end = m.end[1:]
	}
	return true
}

func (m *MyCircularDeque) DeleteLast() bool {
	if m.IsEmpty() {
		return false
	}
	if len(m.end) > 0 {
		m.end = m.end[:len(m.end)-1]
	} else {
		m.front = m.front[1:]
	}
	return true
}

func (m *MyCircularDeque) GetFront() (ans int) {
	if m.IsEmpty() {
		return -1
	}
	if len(m.front) > 0 {
		ans = m.front[len(m.front)-1]
	} else {
		ans = m.end[0]
	}
	return
}

func (m *MyCircularDeque) GetRear() (ans int) {
	if m.IsEmpty() {
		return -1
	}
	if len(m.end) > 0 {
		ans = m.end[len(m.end)-1]
	} else {
		ans = m.front[0]
	}
	return
}

func (m *MyCircularDeque) IsEmpty() bool {
	return len(m.front)+len(m.end) == 0
}

func (m *MyCircularDeque) IsFull() bool {
	return len(m.front)+len(m.end) == m.size
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	ops := Deserialize[[]string](ReadLine(stdin))
	params := MustSplitArray(ReadLine(stdin))
	output := make([]string, 0, len(ops))
	output = append(output, "null")

	constructorParams := MustSplitArray(params[0])
	k := Deserialize[int](constructorParams[0])
	obj := Constructor(k)

	for i := 1; i < len(ops); i++ {
		switch ops[i] {
		case "insertFront":
			methodParams := MustSplitArray(params[i])
			value := Deserialize[int](methodParams[0])
			ans := Serialize(obj.InsertFront(value))
			output = append(output, ans)
		case "insertLast":
			methodParams := MustSplitArray(params[i])
			value := Deserialize[int](methodParams[0])
			ans := Serialize(obj.InsertLast(value))
			output = append(output, ans)
		case "deleteFront":
			ans := Serialize(obj.DeleteFront())
			output = append(output, ans)
		case "deleteLast":
			ans := Serialize(obj.DeleteLast())
			output = append(output, ans)
		case "getFront":
			ans := Serialize(obj.GetFront())
			output = append(output, ans)
		case "getRear":
			ans := Serialize(obj.GetRear())
			output = append(output, ans)
		case "isEmpty":
			ans := Serialize(obj.IsEmpty())
			output = append(output, ans)
		case "isFull":
			ans := Serialize(obj.IsFull())
			output = append(output, ans)
		}
	}
	fmt.Println("\noutput:", JoinArray(output))
}
