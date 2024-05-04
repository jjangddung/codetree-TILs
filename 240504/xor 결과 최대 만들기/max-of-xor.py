n, m = map(int, input().split())
num_list = list(map(int, input().split()))


maxi_list = []



answer = []
# choose 에서 범위를 정해주기

def choose(num,p) :
    if num == m + 1 :
        result = 0
        for value in answer :
            result ^=num_list[value]
        
        maxi_list.append(result)
        return
        
    for i in range(p, n ) :
        answer.append(i)
        choose(num +1,i+1)
        answer.pop()

choose(1,0)


print(max(maxi_list))