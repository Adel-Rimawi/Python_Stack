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

# def sum_total(arr):
#     sum = 0
#     for x in range(len(arr)):
#         sum+= arr[x]

#     return sum
# print(sum_total([2,6,1,]))


#4
# def Average(arr):
#     max =0
#     for i in range(len(arr)):
#         max += arr[i]

#     return max/len(arr)

# print(Average([3,3,3]))



#5

# def Length(arr): #????
#     return len(arr)
# Length([5,6,1,3])


#6 

# def Minimum(arr):
#     min = arr[0]
#     if arr == []:
#         return False
#     for x in range (1,len(arr)):
#         if min > arr[x]:
#             min = arr[x]
#     return min

# print(Minimum([-1,-5,2,-3]))


#7

# def Maximum(arr):
#     max = arr[0]
#     if arr == []:
#         return False
#     for x in range (1,len(arr)):
#         if max < arr[x]:
#             max = arr[x]
#     return max

# print(Maximum([-1,-5,2,-3]))



#8 

# def Ultimate_Analysis(arr):
#     sum =0
#     max = arr[0]
#     min = arr[0]
#     for x in range (1,len(arr)):
#         if max < arr[x]:
#             max = arr[x]
#         if min>arr[x]:
#             min = arr[x]
#         sum += arr[x]
#     return f"sumTotal: {sum}  average: {sum/len(arr)}  minimum: {min}  maximum: {max} length: {len(arr)}"

# print(Ultimate_Analysis([1,3,-5,2,-3]))


#9 

def Reverse_List(arr):
    temp =0
    length = len(arr)
    for i in range(int(len(arr)/2)):
        arr[i],arr[-i-1]=arr[-i-1],arr[i]
        print(arr)


Reverse_List([6,5,4,3,2,1])