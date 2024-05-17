n = int(input())


matrix = list(map(str, input().split()) for _ in range(n))

# print(matrix)

a_grade = 0
b_grade = 0

chai = b_grade - a_grade
count = 0

def change(num_1, num_2) :
    if num_1 * num_2 < 0 :
        return True
    elif num_1 *  num_2 > 0 :
        return False
    elif num_1  *num_2 == 0 :
        if num_1 == 0 and num_2 == 0 :
            return False
        else :
            return True



for ele in range(n) :
    who, num = matrix[ele]
    num = int(num)
    if who == 'A' :
       a_grade += num
    else :
        b_grade += num
    result = b_grade - a_grade

    if change(chai, result) :
        count +=1
    
    chai = result


print(count)