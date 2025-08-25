// Created by none at 2025/08/25 15:43
// leetgo: dev
// https://leetcode.com/problems/employee-importance/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

type Employee struct {
	Id           int
	Importance   int
	Subordinates []int
}

// @lc code=begin

func dfs(id int, employeeMap *map[int]*Employee) int {
	e := (*employeeMap)[id]
	res := e.Importance
	for _, sub := range e.Subordinates {
		res += dfs(sub, employeeMap)
	}
	return res

}
func getImportance(employees []*Employee, id int) int {
	employeeMap := make(map[int]*Employee)
	for _, e := range employees {
		employeeMap[e.Id] = e
	}
	return dfs(id, &employeeMap)

}

// @lc code=end

// Warning: this is a manual question, the generated test code may be incorrect.
func main() {
	stdin := bufio.NewReader(os.Stdin)
	employees := Deserialize[[]*Employee](ReadLine(stdin))
	id := Deserialize[int](ReadLine(stdin))
	ans := getImportance(employees, id)

	fmt.Println("\noutput:", Serialize(ans))
}
