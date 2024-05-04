n, m = map(int, input().split())

answer = []
# choose 에서 범위를 정해주기
# 0 혹은 1로 채움
# 첫 번째부터 curr num-1번째 까지 이미 채운 상태에서..
# curr_num번째부터 채울거고
# 지금 상탵는 1의 개수가 one_cnt인 상황
def choose(curr_num,one_cnt) :

    #종료 조건
    if curr_num == n + 1 :
        if one_cnt == m :
            for i in range(n) :
                if answer[i] == 1 :
                    print(i+1 , end= " ")
            print()
        return

    answer.append(1)
    choose(curr_num+1,one_cnt+1)
    answer.pop()

    answer.append(0)
    choose(curr_num+1,one_cnt)
    answer.pop()

    

choose(1,0)