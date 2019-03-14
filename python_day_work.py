# a = ['c','d']
# b = [1,2]
# for i ,j in(list(zip(a,b))):
#     i = j
#     print(i)
#
# zoo1 = ('monkey', 'elephant')
# zoo2 = ('python', zoo1)
# for i in zoo2:
#     if not isinstance(i,tuple):
#         print(i)
#     else:
#         for j in list(i):
#             print(j)

# from collections import deque
# def foo():
#     for i in range(100):
#         yield i
# last_5 = list(deque(foo(),maxlen=5))

list1 = [[0, 4, 1, 5], [3, 1, 5], [4, 0, 1, 5]]
print(sorted(list1,key=lambda k:(len(k),k)))
min_len = len(list1[0])
# for index,value in enumerate(list1):
#     if len(value)<min_len:
#         list1[0] = value

