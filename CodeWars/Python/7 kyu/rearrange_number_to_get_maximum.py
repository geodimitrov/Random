def max_redigit(num):
    num = str(num)

    if num.isnumeric() and len(num) == 3:
	return int(''.join(reversed(sorted(str(num)))))
