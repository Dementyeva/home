# def reverse(strs):
#     for i in range(len(strs)-1, -1, -1):
#         yield strs[i]
#
# print(''.join(reverse('hello')))
#
# def numb(x):
#     if x > 127:
#         return
#     print(x)
#     return numb(x+1)
# print(numb(11))
#
#
# def divisible_by_left(n):
#     n = str(n)
#     res = [False]
#     for i in range(1,len(n)):
#         if int(n[i-1]) == 0 or int(n[i]) % int(n[i-1]) != 0:
#             res.append(False)
#         else:
#             res.append(True)
#     return res
# print(divisible_by_left(73312))

#
#
# alist = ['5', '8', '9', '4', '3']
#
# def list_items():
#     for item in alist:
#         yield item
#
# gen = list_items()
#
# for item in gen:
#     print(item)
#
# def find_shorted_substring(s):
#     for i in range(1, len(s) + 1):
#         substring = s[:i]
#         repeats = len(s) // len(substring)
#
#         if substring * repeats == s:
#             return substring
# print(find_shorted_substring('pdefufuf'))
#
# for num in range(1,10000):
#     for i in range(2,num):
#         if num %i == 0:
#             break
#     else:
#         print(num)
#
