import pytest
from seminar_2_scripts import *
import random
import copy


class TestFunctions:

    def test_has_cycle(self):
        not_cycle_lst = LinkedList()
        cycle_lst = LinkedList()
        for i in range(3):
            not_cycle_lst.append_back(random.randint(1, 10))
            cycle_lst.append_back(random.randint(1, 10))

        cycle_lst.head.next.next.next = cycle_lst.head

        assert not has_cycle(not_cycle_lst)
        assert has_cycle(cycle_lst)
        assert not has_cycle(LinkedList())

    def test_reverse_linked_list(self):
        input_values = [random.randint(1, 10) for i in range(10)]

        input_lst = LinkedList()
        expected_lst = LinkedList()

        for val in input_values:
            input_lst.append_front(val)
            expected_lst.append_back(val)

        assert reverse_linked_list(input_lst).display() == expected_lst.display()
        assert reverse_linked_list(LinkedList()).display() is None

    def test_middle_val(self):
        input_values_not_even = [random.randint(1, 10) for i in range(11)]
        input_values_even = [random.randint(1, 10) for i in range(10)]

        not_even_lst = LinkedList()
        even_lst = LinkedList()

        for val in input_values_not_even:
            not_even_lst.append_front(val)

        for val in input_values_even:
            even_lst.append_front(val)

        assert middle_val(not_even_lst) == input_values_not_even[5]
        assert middle_val(even_lst) == input_values_even[4]

    def test_remove_element(self):
        input_values_full = [random.randint(1, 10) for i in range(10)]
        deleted_value = input_values_full[random.randint(0, 9)]

        input_values_deleted = copy.copy(input_values_full)
        input_values_deleted.remove(deleted_value)

        full_lst = LinkedList()
        deleted_lst = LinkedList()

        for val in input_values_full:
            full_lst.append_front(val)

        for val in input_values_deleted:
            deleted_lst.append_front(val)

        assert remove_element(full_lst, deleted_value).display() == deleted_lst.display()
        assert remove_element(full_lst, 200).display() == full_lst.display()

    @pytest.mark.parametrize('test_input, expected', [(['abd', 'uabqd'], True),
                                                      (['abd', 'uabqc'], False),
                                                      ]
                             )
    def test_is_subsequence(self, test_input, expected):
        str1, str2 = test_input
        assert is_subsequence_queue(str1, str2) == expected
        assert is_subsequence_two_pointers(str1, str2) == expected

    @pytest.mark.parametrize('str, expected', [('aba', True),
                                               ('abba', True),
                                               ('abc', False),
                                               ('abcc', False)])
    def test_is_palindrome(self, str, expected):
        assert is_palindrome_stack(str) == expected
        assert is_palindrome_deque(str) == expected
        assert is_palindrome_two_pointers(str) == expected

    def test_merge_linked_lists(self):
        input_values_1 = [random.randint(1, 10) for _ in range(10)]
        input_values_2 = [random.randint(1, 10) for _ in range(10)]

        expected_values = sorted(input_values_2 + input_values_1)

        lst1 = LinkedList()
        lst2 = LinkedList()
        expected_lst = LinkedList()

        for i in range(10):
            lst1.append_front(input_values_1[i])
            lst2.append_front(input_values_2[i])
        for i in range(20):
            expected_lst.append_front(expected_values[i])

        assert merge_linked_lists(lst1, lst2).display() == expected_lst.display()








