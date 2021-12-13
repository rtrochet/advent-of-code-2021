with open("input.txt") as f:
	lines = [line.strip() for line in f.readlines()]

def desired_digit(binary_arrays, index, find_most_popular, tie_breaking_digit):
	count_zeros = len([line for line in binary_arrays if line[index] == "0"])
	count_ones = len([line for line in binary_arrays if line[index] == "1"])
	if count_zeros == count_ones:
		return tie_breaking_digit
	elif (count_zeros > count_ones) == find_most_popular:
		return "0"
	elif (count_zeros < count_ones) == find_most_popular:
		return "1"
	else:
		raise Exception("oops logically impossible")


def find_best_match(binary_arrays, find_most_popular, tie_breaking_digit):
	possible_matches = binary_arrays
	match = None
	idx = 0
	while match is None:
		print(idx)
		digit = desired_digit(possible_matches, idx, find_most_popular, tie_breaking_digit)
		possible_matches = [value for value in possible_matches if value[idx] == digit]
		print(digit)
		print(possible_matches)
		if len(possible_matches) == 1:
			[match] =  possible_matches
		else:
			idx = idx + 1
	return match

o_gen_rating = find_best_match(lines, True, "1")
co2_scrub_rating = find_best_match(lines, False, "0")

print(o_gen_rating, int(o_gen_rating, 2))
print(co2_scrub_rating, int(co2_scrub_rating, 2))

print(int(o_gen_rating, 2) * int(co2_scrub_rating, 2))

