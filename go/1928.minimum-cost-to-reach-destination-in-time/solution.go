// Created by none at 2024/10/03 12:16
// leetgo: 1.4.9
// https://leetcode.cn/problems/minimum-cost-to-reach-destination-in-time/

package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"os"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin

type Pair struct {
	y, t int
}

type Item struct {
	cost, t, x int
}
type Heap []Item

func (h Heap) Len() int { return len(h) }
func (h Heap) Less(i, j int) bool {
	return h[i].cost < h[j].cost || (h[i].cost == h[j].cost && h[i].t < h[j].t)
}

func (h Heap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }

func (h *Heap) Push(x any) {
	// Push and Pop use pointer receivers because they modify the slice's length,
	// not just its contents.
	*h = append(*h, x.(Item))
}

func (h *Heap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}
func minCost(maxTime int, edges [][]int, passingFees []int) int {

	n := len(passingFees)
	g := make([][]Pair, n)
	for i := range g {
		g[i] = make([]Pair, n)
	}

	for _, e := range edges {
		x, y, t := e[0], e[1], e[2]
		g[x] = append(g[x], Pair{y, t})
		g[y] = append(g[y], Pair{x, t})

	}

	const INF = int(1e9)

	dist := make([]int, n)
	for i := range dist {
		dist[i] = INF
	}

	dist[0] = 0

	q := &Heap{}
	heap.Init(q)
	heap.Push(q, Item{passingFees[0], 0, 0}) // (cost, t, x)
	for q.Len() > 0 {
		item := heap.Pop(q).(Item)
		if item.x == n-1 {
			return item.cost
		}
		for _, e := range g[item.x] {
			new_cost := item.cost + passingFees[e.y]
			new_time := item.t + e.t
			if new_time <= maxTime && new_time < dist[e.y] {
				dist[e.y] = new_time
				heap.Push(q, Item{new_cost, new_time, e.y})
			}
		}
	}
	return -1

}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	maxTime := Deserialize[int](ReadLine(stdin))
	edges := Deserialize[[][]int](ReadLine(stdin))
	passingFees := Deserialize[[]int](ReadLine(stdin))
	ans := minCost(maxTime, edges, passingFees)

	fmt.Println("\noutput:", Serialize(ans))
}
