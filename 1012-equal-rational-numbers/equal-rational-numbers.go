var pattern = regexp.MustCompile(`([0-9]+)\.?([0-9]+)?(\(([0-9]+)\))?`)

func isRationalEqual(s string, t string) bool {
	normalize := func(s string) string {
		parts := pattern.FindStringSubmatch(s)
		a, _ := strconv.Atoi(parts[1])

		dec := parts[2]
		repeat := parts[4]

		if strings.Trim(repeat, "0") != "" {
			for len(dec) < 20 {
				dec += repeat
			}
			if len(dec) > 20 {
				dec = dec[:20]
			}

			if strings.TrimRight(repeat, "9") == "" {
				dec = strings.TrimRight(dec, "9")

				m := len(dec)
				if m == 0 {
					return fmt.Sprintf("%d.", a+1)
				}
				return fmt.Sprintf("%d.%s%c", a, dec[:m-1], dec[m-1]+1)
			}
		}

		return fmt.Sprintf("%d.%s", a, strings.TrimRight(dec, "0"))
	}
	s = normalize(s)
	t = normalize(t)
	return s == t
}