from collections import *


def problem_1_anagram_a_problem_1(s1, s2):
    if len(s1) != len(s2):
        return False
    freq1 = {}
    freq2 = {}

    for ch in s1:
        if ch in freq1:
            freq1[ch] += 1
        else:
            freq1[ch] = 1

    for ch in s2:
        if ch in freq2:
            freq2[ch] += 1
        else:
            freq2[ch] = 1

    for key in freq1:
        if key not in freq2 or freq1[key] != freq2[key]:
            return False
        return True


def problem_1_anagram_b_problem_1(s1, s2):
    if len(s1) != len(s2):
        return False
    return Counter(s1) == Counter(s2)


def first_and_last_problem_2_sorted(array, target):
    for i in range(len(array)):
        if array[i] == target:
            start = i
            print(f'The value of start is {start}')
            while i + 1 < len(array) and array[i + 1] == target:
                i += 1
                print(f'The value of end is {i}')
            return [start, i]
    return [1, -1]


def first_and_last_problem_2_unsorted(array, target):
    start, end = 0, 0
    for i in range(len(array)):
        if array[i] == target:
            start = i
            break
    for i in range(1, len(array)):
        if array[len(array) - i] == target:
            end = len(array) - i
            break
    return [start, end]
    # return [start, i]


def maximum_element(array):
    maximum = 0
    for i in range(len(array)):
        if maximum < array[i]:
            maximum = array[i]
            index_position = i
    return maximum, index_position


def k_maximum_element(array, k):
    # iterate over the element
    # maximum element ==> list and pop it
    kth = []
    for i in range(k):
        maxmimum, index_position = maximum_element(array)
        kth.append(maxmimum)
        array.pop(index_position)
    return kth[k-1]


def k_maximum_element_improved_1(array, k):
    for i in range(k-1):
        array.remove(max(array))
    return max(array)


def k_maximum_element_improved_2(array, k):
    n = len(array)
    array.sort()
    print(array)
    return array[n-k]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # print(problem_1_anagram_a_problem_1("danger", "gardedn"))
    # print(problem_1_anagram_b_problem_1("danger", "garden"))
    # print(first_and_last_problem_2_sorted([2, 3, 3, 5, 5, 3, 6, 7, 10], 3))
    # print(first_and_last_problem_2_unsorted([2, 3, 3, 5, 5, 3, 6, 7, 10], 3))
    print(k_maximum_element([2, 3, 3, 5, 5, 3, 6, 7, 10], 5))
    print(k_maximum_element_improved_1([2, 3, 3, 5, 5, 3, 6, 7, 10], 6))
    print(k_maximum_element_improved_2([2, 3, 3, 5, 5, 3, 6, 7, 10], 6))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
