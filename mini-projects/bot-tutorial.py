# def mean(x : list):
#
#     mu = sum(x) / len(x)
#
#     return(mu)
# print(mean([1,2,3]))



def mean(arr):
    count = 0
    nums = 0
    for i in arr:
        nums += i
        count += 1
    result  = nums / count
    return result
print(mean([1,2,3]))