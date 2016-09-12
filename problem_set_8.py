def product(list):
	"""
	Returns the product of integers in a given list
	"""
	product = 1	
	for i in list:
		product *= i
	return product

def largest_product(number, digits):
	"""
	Takes in the number as a string and the total number of digits
	Returns the highest product of 13 consecutive numbers in the string
	"""	
	start = 0 
	end = 13 # length of string to be clipped from total
	temp_list = []
	compare_list = []
	while end <= digits:
		for i in number[start:end]:
			temp_list.append(int(i))
		if compare_list and compare_list[0] < product(temp_list):
			compare_list.pop(0)
			compare_list.append(product(temp_list))
		if not compare_list:
			compare_list.append(product(temp_list))	
		del temp_list[:]
		start += 1 
		end += 1
	print compare_list

# def largest_product(number, digits):	
	# """
	# This may be a quicker solution as it checks to see if 0 is in the temp_list;
	# to avoid finding the product and bother appending it to the compare_list
	# """
# 	start = 0 
# 	end = 13 
# 	temp_list = []
# 	compare_list = []
# 	while end <= digits:
# 		for i in number[start:end]:
# 			temp_list.append(int(i))
# 		if 0 in temp_list:
# 			del temp_list[:]
# 			start += 1 
# 			end += 1
# 		else:
# 			if compare_list and compare_list[0] < product(temp_list):
# 				compare_list.pop(0)
# 				compare_list.append(product(temp_list))
# 			if not compare_list:
# 				compare_list.append(product(temp_list))	
# 			del temp_list[:]
# 			start += 1 
# 			end += 1
# 	print compare_list