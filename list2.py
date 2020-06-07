# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.

nums = [1,2,2,3,3,5,5]
def remove_adjacent(nums):
    new = []
    for num in nums:
        if len(new) == 0 or num != new[-1]:
            new.append(num)
    return new
    


# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.


list1 = [5,6]
list2 = [1,2,5,6,8,9]
def linear_merge(list1, list2):
    new = []
 
    while len(list1) and len(list2):
        if list1[0] < list2[0]:
            new.append(list1.pop(0))
        else:
            new.append(list2.pop(0))

    new.extend(list1)
    new.extend(list2)
    return new
