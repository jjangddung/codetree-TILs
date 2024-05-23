n = int(input())



num_list = list(map(int, input().split()))



for i in range(n) :
    least = i

    for j in range(i+1,n) :
        if num_list[j] < num_list[least] :
            least = j
    
    num_list[i] , num_list[least] = num_list[least], num_list[i]

print(*num_list)