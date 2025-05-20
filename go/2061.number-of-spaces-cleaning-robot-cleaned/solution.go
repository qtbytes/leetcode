// Created by none at 2025/05/20 15:56
// leetgo: dev
// https://leetcode.com/problems/number-of-spaces-cleaning-robot-cleaned/

package main

import (
	"bufio"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin
type Pair struct {
	x, y, dx, dy int
}

func numberOfCleanRooms(room [][]int) int {
	visit := make(map[Pair]bool)
	m, n := len(room), len(room[0])
	x, y, dx, dy := 0, 0, 0, 1
	res := 0
	for !visit[Pair{x, y, dx, dy}] {
		fmt.Println(x, y, dx, dy)
		visit[Pair{x, y, dx, dy}] = true
		if room[x][y] != -1 {
			room[x][y] = -1
			res++
		}
		nx, ny := x+dx, y+dy
		if 0 <= nx && nx < m && 0 <= ny && ny < n && room[nx][ny] != 1 {
			x, y = nx, ny
		} else {
			dx, dy = dy, -dx
		}
	}
	return res

}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	room := Deserialize[[][]int](ReadLine(stdin))
	ans := numberOfCleanRooms(room)

	fmt.Println("\noutput:", Serialize(ans))
}
