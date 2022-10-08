"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	TODO:
	"""
	d = {}
	all_lst = read_dictionary()
	lst1 = []
	lst2 = []
	lst3 = []
	lst4 = []
	s1 = input('1 row of letters: ')
	if len(s1) != 7:
		print('Illegal input')
		return
	for i in range(7):
		if i % 2 == 0:
			if s1[i].isalpha is False:
				print('Illegal input')
				return
		if i % 2 == 1:
			if s1[i] == ' ' is False:
				print('Illegal input')
				return
	for ch in s1:
		if ch is not ' ':
			ch = ch.lower()
			lst1.append(ch)



	s2 = input('2 row of letters: ')
	if len(s2) != 7:
		print('Illegal input')
		return
	for i in range(7):
		if i % 2 == 0:
			if s2[i].isalpha is False:
				print('Illegal input')
				return
		if i % 2 == 1:
			if s2[i] == ' ' is False:
				print('Illegal input')
				return
	for ch in s2:
		if ch is not ' ':
			ch = ch.lower()
			lst2.append(ch)
	s3 = input('3 row of letters: ')
	if len(s3) != 7:
		print('Illegal input')
		return
	for i in range(7):
		if i % 2 == 0:
			if s3[i].isalpha is False:
				print('Illegal input')
				return
		if i % 2 == 1:
			if s3[i] == ' ' is False:
				print('Illegal input')
				return
	for ch in s3:
		if ch is not ' ':
			ch = ch.lower()
			lst3.append(ch)
	s4 = input('4 row of letters: ')
	if len(s4) != 7:
		print('Illegal input')
		return
	for i in range(7):
		if i % 2 == 0:
			if s4[i].isalpha is False:
				print('Illegal input')
				return
		if i % 2 == 1:
			if s4[i] == ' ' is False:
				print('Illegal input')
				return
	for ch in s4:
		if ch is not ' ':
			ch = ch.lower()
			lst4.append(ch)
	for i in range(4):
		d[0] = lst1
		d[1] = lst2
		d[2] = lst3
		d[3] = lst4
	ans_lst = []
	num = [0]
	start = time.time()
	find_boggle(d, '', 4, ans_lst, all_lst, [], num)
	print('There are ', num[0], ' words in total.')
	####################
	#                  #
	#       TODO:      #
	#                  #
	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_boggle(d, string, max_len, ans_lst, all_lst, index_lst, num):
	for x in range(4):
		for y in range(4):
			find_boggle_helper(d, string, max_len, ans_lst, all_lst, index_lst, num, x, y)


def find_boggle_helper(d, string, max_len, ans_lst, all_lst, index_lst, num, x, y):
	if (len(string) >= max_len) and string in all_lst and string not in ans_lst:		# base case
			ans_lst.append(string)
			print("Found: ", string)
			num[0] += 1
			find_boggle_helper(d, string, max_len, ans_lst, all_lst, index_lst, num, x, y)
	else:
		# self-similarity
		for i in range(-1, 2):
			for j in range(-1, 2):
				cur_x = x + i
				cur_y = y + j
				if (cur_x >= 0) and (cur_x <= 3) and (cur_y >= 0) and (cur_y <= 3):
					if (cur_x, cur_y) not in index_lst:
						index_lst.append((cur_x, cur_y))
						# choose
						string += d[cur_x][cur_y]
						# explore
						if has_prefix(string, all_lst):
							find_boggle_helper(d, string, max_len, ans_lst, all_lst, index_lst, num, cur_x, cur_y)
						# un-choose
						index_lst.pop()
						string = string[:-1]


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	lst = []
	with open(FILE, 'r') as f:
		for line in f:
			line = line.split('\n')
			for word in line:
				word = word.strip()
				lst.append(word)
	return lst


def has_prefix(sub_s, all_lst):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for s in all_lst:
		if s.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
