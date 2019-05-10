# import os
#
#
# def reverse_words(string):
#
#     return ' '.join(string.split()[::-1])
#
#
# r = reverse_words('abc d e f')
# print(r)
#
# def count_extnames(file):
#     lis = []
#     for i in file:
#         suffix = os.path.splitext(i)[-1]
#         lis.append(suffix)
#
#     dic = {}
#     for x in lis:
#         dic[x] = lis.count(x)
#
#     suffix = [k for k,v in dic.items() if v == max(dic.values())]
#
#     return suffix
#
#
# lis = ['1.mp4','2.mp3','3.mp3','4.mp4','5.jpg','6.als']
# c = count_extnames(lis)
# print(c)




