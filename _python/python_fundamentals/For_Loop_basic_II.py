#1

# def biggie_size(arr):
#     for x in range(len(arr)):
#         if arr[x]>0:
#             arr[x]= "big"
#     return arr
# (biggie_size([5,3,-2,-5,-2]))


#2

# def count_positives(arr):
#     counter = 0
#     for x in range(len(arr)):
#         if arr[x]>0:
#             counter+=1
#     arr[-1]=counter
#     return arr
# print(count_positives([5,3,-2,-5,-2]))


#3

def sum_total(arr):
    sum = 0
    for x in range(len(arr)):
        sum+= arr[x]

    return sum
print(sum_total([2,6,1,]))
