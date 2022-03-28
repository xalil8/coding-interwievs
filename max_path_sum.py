
def start_test(file):
    with open(file) as f:
        array_speacial = []
        for line in f:
            array_speacial.append(list(map(int, line.split(" "))))
    a = max_sum(array_speacial)
    print("total sum is = ", a[0][0])
        
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
    #kick_primes_out(list)
    clean_list = [row[:] for row in list]
    for row in range(len(list)-2, -1, -1):
        print("///////////////row = ", row)
        for col in range(len(list[row])):
            print(list[row][col])
            if prime_check(clean_list[row][col]):
                print("first if worked for ",list[row][col])
                continue
            else:
                print(list[row+1][col], list[row+1][col+1])
                if (prime_check(clean_list[row+1][col]) and prime_check(clean_list[row+1][col+1])):
                    print("if worked")
                    continue
                elif not (prime_check(clean_list[row+1][col]) and prime_check(clean_list[row+1][col+1])):
                    print("elif worked")
                    list[row][col] += max(list[row+1][col], list[row+1][col+1])
                else:
                    print("else worked")
                    if clean_list[row+1][col] > clean_list[row+1][col+1]:
                        if prime_check(clean_list[row+1][col]):
                            list[row][col] += list[row+1][col+1]
                        else:
                            list[row][col] += list[row+1][col]
                    else:
                        if prime_check(clean_list[row+1][col+1]):
                            list[row][col] += list[row+1][col]
                        else:
                            list[row][col] += list[row+1][col+1] 
    for i in clean_list:
        print(i)
    for i in list:
        print(i)
    return list

