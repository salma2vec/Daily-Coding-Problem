func sumSubarrayMins(arr []int) int {
	mod := int(1e9) + 7
	var stack []int
	var res int

	arr = append(arr, 0) // Add sentinel element to handle last elements in array

	for i, num := range arr {
		for len(stack) > 0 && num < arr[stack[len(stack)-1]] {
			top := stack[len(stack)-1]
			stack = stack[:len(stack)-1]

			left := -1
			if len(stack) > 0 {
				left = stack[len(stack)-1]
			}

			res = (res + arr[top]*(i-top)*(top-left)) % mod
		}

		stack = append(stack, i)
	}

	return res
}
