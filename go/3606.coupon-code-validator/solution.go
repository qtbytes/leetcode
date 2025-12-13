// Created by none at 2025/12/13 14:24
// leetgo: dev
// https://leetcode.com/problems/coupon-code-validator/

package main

import (
	"bufio"
	"cmp"
	"fmt"
	"os"
	"regexp"
	"slices"

	. "github.com/j178/leetgo/testutils/go"
)

// @lc code=begin
var alphanumericUnderscore = regexp.MustCompile(`^[a-zA-Z0-9_]+$`)

func isValid(s string) bool {
	return alphanumericUnderscore.MatchString(s)
}

func validateCoupons(code []string, businessLine []string, isActive []bool) []string {
	var index []int
	validBusinessLine := []string{"electronics", "grocery", "pharmacy", "restaurant"}

	for i := range code {
		if isActive[i] && slices.Contains(validBusinessLine, businessLine[i]) && isValid(code[i]) {
			index = append(index, i)
		}
	}

	slices.SortFunc(index, func(aIdx, bIdx int) int {
		return cmp.Or(
			cmp.Compare(businessLine[aIdx], businessLine[bIdx]),
			cmp.Compare(code[aIdx], code[bIdx]),
		)
	})

	var ans []string
	for _, i := range index {
		ans = append(ans, code[i])
	}

	return ans
}

// @lc code=end

func main() {
	stdin := bufio.NewReader(os.Stdin)
	code := Deserialize[[]string](ReadLine(stdin))
	businessLine := Deserialize[[]string](ReadLine(stdin))
	isActive := Deserialize[[]bool](ReadLine(stdin))
	ans := validateCoupons(code, businessLine, isActive)

	fmt.Println("\noutput:", Serialize(ans))
}
