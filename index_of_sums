my_list = [1,3,4,5,7,10,11]

def sumy(numbers,target):
    l =0
    r = len(numbers)-1
    for i in range(len(numbers)):
        if (numbers[l] + numbers[r]) > target:
            r -= 1
        elif (numbers[l] + numbers[r]) < target:
            l += 1
        else:
            return(l+1,r+1)

print(sumy(my_list,12))
