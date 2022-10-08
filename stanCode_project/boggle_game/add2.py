"""
File: add2.py
Name:
------------------------
TODO:
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def add_2_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    #######################
    #                     #
    #        TODO:        #
    #                     #
    #######################
    lst1 = []
    lst2 = []
    lst1_re = []
    lst2_re = []
    num1 = 0
    num2 = 0
    cur = l1
    while cur.next is not None:
        lst1.append(cur.val)
        cur = cur.next
    lst1.append(cur.val)

    cur = l2
    while cur.next is not None:
        lst2.append(cur.val)
        cur = cur.next
    lst2.append(cur.val)


    for i in range(len(lst1)-1, -1, -1):
        lst1_re.append(lst1[i])
    for i in range(len(lst2)-1, -1, -1):
        lst2_re.append(lst2[i])

    for i in range(len(lst2_re)):
        num2 += lst2_re[i]*10**(len(lst2_re)-1)/10**(i)
    for i in range(len(lst1_re)):
        num1 += lst1_re[i]*10**(len(lst1_re)-1)/10**(i)

    if num1 == 0 and num2 == 0:
        return ListNode(0, None)

    # we get the sum of the reverse (num1 + num2).
    num_ans = str(int(num1 + num2))
    while num_ans[0] == '0':
        num_ans = num_ans[1:]

     # making  new ListNode for the sum link_list.
    link_list_new = None
    for i in range(len(num_ans)-1, -1, -1):
        new_node = ListNode(int(num_ans[i]), None)
        if link_list_new is None:
            link_list_new = new_node
        else:
            cur = link_list_new
            while cur.next is not None:
                cur = cur.next
            cur.next = new_node
    return link_list_new
####### DO NOT EDIT CODE BELOW THIS LINE ########


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 add2.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(2, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l2 = ListNode(5, None)
            l2.next = ListNode(6, None)
            l2.next.next = ListNode(4, None)
            ans = add_2_numbers(l1, l2)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(9, None)
            l1.next = ListNode(9, None)
            l1.next.next = ListNode(9, None)
            l1.next.next.next = ListNode(9, None)
            l1.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next.next = ListNode(9, None)
            l2 = ListNode(9, None)
            l2.next = ListNode(9, None)
            l2.next.next = ListNode(9, None)
            l2.next.next.next = ListNode(9, None)
            ans = add_2_numbers(l1, l2)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test3':
            l1 = ListNode(0, None)
            l2 = ListNode(0, None)
            ans = add_2_numbers(l1, l2)
            print('---------test3---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 add2.py test1"')


if __name__ == '__main__':
    main()
