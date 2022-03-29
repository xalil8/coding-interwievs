
def start_test(file):
    with open(file) as f:
        input_array = [list( map(int,line.split()) ) for line in f]
    print("answer = ", max_sum(input_array))
        
def prime_check(number):
    if number>1:    
        for i in range(2,number):
            if number % i == 0:
                return False
        return True
    else:
        if number == 1:
            return False
        else:
            return None


def max_sum(list):
    clean_list = [row[:] for row in list]
    for row in range(len(list)-2, -1, -1):
        for col in range(len(list[row])):
            if prime_check(clean_list[row][col]) or (prime_check(clean_list[row+1][col]) and prime_check(clean_list[row+1][col+1])):
                continue
            elif not (prime_check(clean_list[row+1][col]) and prime_check(clean_list[row+1][col+1])):
                list[row][col] += max(list[row+1][col], list[row+1][col+1])
            else:
                if prime_check(clean_list[row+1][col]):
                    list[row][col] += list[row+1][col]
                else:
                    list[row][col] += list[row+1][col+1]
    return list[0][0]

path = "text file path"
start_test("C:/Users/halil/Desktop/new.txt")
