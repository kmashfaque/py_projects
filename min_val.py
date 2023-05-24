
# # for complexity O(n2)

arr = [6, 10, 2, 9, 4, 12, 9, 0]


# def min_val(arr):
#     for i in range(0, len(arr)-1):
#         curr_elem = arr[i]

#         for j in range(0, len(arr)):
#             next_elem = arr[j]

#             if curr_elem < next_elem:
#                 curr_elem = curr_elem

#             elif curr_elem == next_elem:
#                 curr_elem = next_elem

#             elif next_elem < curr_elem:
#                 curr_elem = next_elem
#     return curr_elem


# print(min_val(arr))


# complexity with O(n)
def min_val2(arr):
    curr_elem = arr[0]

    for i in range(0, len(arr)-1):

        minimum_val = 0

        if curr_elem < arr[i+1]:
            curr_elem = curr_elem

        elif arr[i+1] < curr_elem:
            curr_elem = arr[i+1]

    return curr_elem


print(min_val2(arr))
