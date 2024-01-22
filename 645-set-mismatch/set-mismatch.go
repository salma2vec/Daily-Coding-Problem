package main

import "fmt"

func findErrorNums(nums []int) []int {
	n := len(nums)
	counter := make(map[int]int)

	var duplicate, missing int

	for _, num := range nums {
		counter[num]++
		if counter[num] == 2 {
			duplicate = num
		}
	}

	for i := 1; i <= n; i++ {
		if counter[i] == 0 {
			missing = i
			break
		}
	}

	return []int{duplicate, missing}
}