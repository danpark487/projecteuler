def palindrome(final):
	start = 0
	end = len(str(final)) - 1
	final_list = [int(x) for x in str(final)]
	while start < end:
		if final_list[start] == final_list[end]:
			start += 1
			end -= 1
		else:
			return False
			break
	return True
