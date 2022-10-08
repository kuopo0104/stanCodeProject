"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():

    while True:
        your_target = input("Find anagrams for: ")
        if  your_target == EXIT:
            break
        print("Searching. . .")
        start = time.time()
        find_anagrams(your_target)
        ####################
        #                  #
        #       TODO:      #
        #                  #
        ####################
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    lst = []
    with open(FILE, 'r') as f:
        for line in f:
            for word in line:
                word = word.strip()
                lst.append(word)    # Append ---> memory storing in same address, backtracking is not available.
    return lst


def find_anagrams(s):
    """
    :param s:searching word
    :return:ans_lst
    """
    num_lst = [0]
    ans_lst = []
    index_lst = []
    # Using the function "read_dictionary" to get the all list of content.
    all_lst = read_dictionary()
    find_anagrams_helper(s, ans_lst, all_lst, '', index_lst, num_lst)
    print(ans_lst)
    print("Number: ", num_lst[0])


def find_anagrams_helper(s, ans_lst, all_lst, string, index_lst, num):

    if len(string) == len(s):
        if string in all_lst:
            if string not in ans_lst:
                print(string)
                print("Searching. . .")
                ans_lst.append(string)
                num[0] += 1
    else:
        for i in range(len(s)):
            if i not in index_lst:
                index_lst.append(i)
                string += s[i]
                if has_prefix(string, all_lst):
                    find_anagrams_helper(s, ans_lst, all_lst, string, index_lst, num)
                index_lst.pop()
                string = string[:-1]


def has_prefix(sub_s: str, all_lst: list) -> bool:
    """
    :param sub_s:
    :return: Boolean
    """
    # The boolean is to prune enormous recursion.
    for s in all_lst:
        if s.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
