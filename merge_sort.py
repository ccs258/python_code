def mergeSort(nums):
    # 归并过程
    def merge(left, right):
        result = []  # 保存归并后的结果
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result = result + left[i:] + right[j:] # 剩余的元素直接添加到末尾
        return result
    # 递归过程
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])
    return merge(left, right)

print(mergeSort([2,1,4]))
# class mergeSort(object):
#     # def __init__(self,nums):
#     #     self.nums = nums
#     def merge(self,left,right):
#         result = []
#         i = j =0
#         while i<len(left) and j<len(right):
#             if left[i] <= right[j]:
#                 result.append(left[i])
#                 i += 1
#             else:
#                 result.append(right[j])
#                 j= j+1
#         result = result + left[i:] +right[j:]
#         return result
#
# if __name__ == '__main__':
#     nums = [1]
#     merge_sort = mergeSort()
#     mid = len(nums)
#     left = mergeSort(nums[:mid])
#     right = mergeSort(nums[mid:])

