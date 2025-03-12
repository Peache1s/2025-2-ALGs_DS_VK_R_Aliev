import pytest
import random
from seminar_1_scripts import *


class TestFunctions:
    """
    Класс тестов
    """

    @pytest.mark.parametrize('test_input, expected', [([[3, 8, 9, 11, 16, 18, 19, 21], 25], [2, 4]),
                                                      ([[3, 8, 9, 11, 16, 18, 19, 21], 1], []),
                                                      ([[4, 12, 3, 11], 15], [0, 3]),
                                                      ([[], random.randint(1, 100)], []), ]
                             )
    def test_two_sum(self, test_input, expected):
        nums, target = test_input
        assert two_sum(nums, target) == expected

    @pytest.mark.parametrize('array, expected', [([3, 8, 6, 9, 9, 8, 6], [6, 8, 9, 9, 6, 8, 3]),
                                                 ([], []),
                                                 ([1], [1])]
                             )
    def test_reverse_array(self, array, expected):
        assert reverse_array(array) == expected

    @pytest.mark.parametrize('test_input, expected', [([[1, 2, 3, 4, 5, 6, 7], 3], [5, 6, 7, 1, 2, 3, 4]),
                                                      ([[], 5], []),
                                                      ([[5, 2, 3], 4], [3, 5, 2]),
                                                      ([[1], 5], [1])]
                             )
    def test_reverse_array_part(self, test_input, expected):
        array, k = test_input

        if len(array) == 0:
            with pytest.raises(ZeroDivisionError):
                reverse_array_part(array, k)
        else:
            assert reverse_array_part(array, k) == expected

    @pytest.mark.parametrize('input_arrays, merged_array', [([[3, 8, 10, 11], [1, 7, 9]], [1, 3, 7, 8, 9, 10, 11]),
                                                            ([[1, 7, 9], [3, 8, 10, 11]], [1, 3, 7, 8, 9, 10, 11]),
                                                            ([[1, 7, 9], [1, 7, 9]], [1, 1, 7, 7, 9, 9]),
                                                            ([[1, 7, 9], []], [1, 7, 9]),
                                                            ([[], [1, 7, 9]], [1, 7, 9]),
                                                            ([[], []], []),
                                                            ])
    def test_merge_with_alloc(self, input_arrays, merged_array):
        arr1, arr2 = input_arrays
        assert merge_sorted_arrays_with_alloc(arr1, arr2) == merged_array

    @pytest.mark.parametrize('input_arrays, merged_array',
                             [([[3, 8, 10, 11, 0, 0, 0], [1, 7, 9]], [1, 3, 7, 8, 9, 10, 11]),
                              ([[1, 7, 9, 0, 0, 0, 0], [3, 8, 10, 11]], [1, 3, 7, 8, 9, 10, 11]),
                              ([[1, 7, 9, 0, 0, 0], [1, 7, 9]], [1, 1, 7, 7, 9, 9]),
                              ([[1, 7, 9], []], [1, 7, 9]),
                              ([[0, 0, 0], [1, 7, 9]], [1, 7, 9]),
                              ([[], []], []),
                              ])
    def test_merge_without_alloc(self, input_arrays, merged_array):
        arr1, arr2 = input_arrays
        assert merge_sorted_arrays_without_alloc(arr1, arr2) == merged_array

    @pytest.mark.parametrize('input_array, sorted_array', [([0, 1, 1, 0, 1, 0, 1, 0], [0, 0, 0, 0, 1, 1, 1, 1]),
                                                           ([], []),
                                                           ([0, 0, 0, 1], [0, 0, 0, 1]),
                                                           ([0, 0, 0], [0, 0, 0]),
                                                           ([1, 1, 1], [1, 1, 1]),
                                                           ([0], [0]),
                                                           ([1], [1])
                                                           ]
                             )
    def test_sort_binary_array(self, input_array, sorted_array):
        assert sort_binary_array(input_array) == sorted_array

    @pytest.mark.parametrize('input_array, sorted_array', [([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
                                                           ([], []),
                                                           ([0, 0, 0], [0, 0, 0]),
                                                           ([1, 1, 1], [1, 1, 1]),
                                                           ([2, 2, 2], [2, 2, 2]),
                                                           ([1], [1]),
                                                           ([0, 1, 2], [0, 1, 2])])
    def test_sort_colors(self, input_array, sorted_array):
        assert sort_colors(input_array) == sorted_array

    @pytest.mark.parametrize('input_array, expected', [([3, 2, 4, 1, 11, 8, 9], [2, 4, 8, 1, 11, 3, 9]),
                                                       ([], []),
                                                       ([[2, 4, 8, 1, 11, 3, 9], [2, 4, 8, 1, 11, 3, 9]]),
                                                       ([8, 2, 10, 4], [8, 2, 10, 4]),
                                                       ([7, 1, 9, 3], [7, 1, 9, 3]),
                                                       ([1], [1]),
                                                       ([2], [2])
                                                       ])
    def test_even_first(self, input_array, expected):
        assert even_first(input_array) == expected

    @pytest.mark.parametrize('input_array, expected', [([0, 0, 1, 0, 3, 12], [1, 3, 12, 0, 0, 0]),
                                                       ([0, 33, 57, 88, 60, 0, 0, 80, 99], [33, 57, 88, 60, 80, 99, 0, 0, 0]),
                                                       ([0, 0, 0, 18, 16, 0, 0, 77, 99], [18, 16, 77, 99, 0, 0, 0, 0, 0]),
                                                       ([], []),
                                                       ([12, 10, 8], [12, 10, 8]),
                                                       ([0, 0, 0], [0, 0, 0]),
                                                       ([0], [0]),
                                                       ([67], [67]),
                                                       ([12, 10, 0, 0], [12, 10, 0, 0])
                                                       ])
    def test_zeros_last(self, input_array, expected):
        assert zeros_last(input_array) == expected
