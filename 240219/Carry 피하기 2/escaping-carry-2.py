import sys

input = sys.stdin.readline


n = int(input())



arr = [str(input()) for _ in range(n)]

final_list = []


for i in range(n-2) :
    chai = 5 - len(arr[i])

    result_1 = "0"*chai + arr[i]

    # print(result_)
    

    for j in range(i+1 , n-1) :
        chai = 5 - len(arr[j])
        result_2 = "0"*chai + arr[j]

        
        for k in range(j+1, n) :
            chai = 5 - len(arr[k])
            result_3 = "0"*chai + arr[k]

            # print(result_1,result_2,result_3)

            count = 0
            for p in range(4) :
                real = int(result_1[p]) + int(result_2[p]) + int(result_3[p])
                # print(real)

                if real >= 10 :
                    count +=1
                    break
                
            if count == 0 :
                final = int(arr[i]) + int(arr[j]) + int(arr[k])
                # print("final:",final)
                final_list.append(final)


if len(final_list) != 0 :
    print(max(final_list))

else :
    print(-1)