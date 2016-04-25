"""
https://www.interviewcake.com/question/python/merge-sorted-arrays
"""
import unittest

def merge_sorted_arrays(first, second):

    # setup our merged list
    merged_list_size = len(first) + len(second)
    merged_list = [None] * merged_list_size

    current_index_first = 0
    current_index_second = 0
    current_index_merged = 0

    while current_index_merged < merged_list_size:

        is_first_merged = current_index_first >= len(first)
        is_second_merged = current_index_second >= len(second)

        if not is_first_merged and (is_second_merged or \
            (first[current_index_first] < second[current_index_second])):
            merged_list[current_index_merged] = first[current_index_first]
            current_index_first += 1
        else:
            merged_list[current_index_merged] = second[current_index_second]
            current_index_second += 1

        current_index_merged += 1

    return merged_list

def my_merge_sorted_arrays(first, second):
    """O(n) implementation."""
    
    # just prepare the resulting list
    result_len = len(first) + len(second)
    result = [None] * result_len
    # decide what is the first element of our merged list
    
    for i in range(result_len):
        
        if first:
            s1 = first[0]
        else:
            break

        if second:
            s2 = second[0]
        else:
            break

        if s1 < s2:
            # save the least item in the result
            result[i] = s1
            # mark the item saved as merged by removing it in the list
            first = first[1:]
        else:
            result[i] = s2
            # mark the item as merged by removing it in the list
            second = second[1:]

    if first:
        for j in range(len(first)):
            result[i] = first[j]
            i += 1

    if second:
        for j in range(len(second)):
            result[i] = second[j]
            i += 1

    return result

def merge_sorted_arrays_2(first, second):
    return sorted(first + second)


def merge_sorted_arrays_1(first, second):
    """Used a built in sorting algorithm.
    Not much thinking done here.
    This is running O(n log n)"""
    
    result = []
    # merge the arrays into one array
    result.extend(first)
    result.extend(second)
    # sort the list and that's it!
    result.sort()
    return result

class TestMergeSortedArrays(unittest.TestCase):

    def callFn(self, first, second):
        return merge_sorted_arrays(first, second)

    def tests(self):
        first = [3, 4, 6, 10, 11, 15]
        second = [1, 5, 8, 12, 14, 19]
        self.assertEqual(self.callFn(first, second),
                         [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19])
        first = [10, 11]
        second = [12, 14, 19]
        self.assertEqual(self.callFn(first, second),
                         [10, 11, 12, 14, 19])

if __name__ == '__main__':
    unittest.main()