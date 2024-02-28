import sys

input = sys.stdin.readline

n = int(input())


arr =[list(map(int,input().split())) for _ in range(n)]

result_list = []

for i in range(n) :
    for j in range(i+1, n) :
        for k in range(j+1,n) :
            if i == j or j == k or i == k :
                continue
            
            first_lane_x  = arr[i][0] - arr[j][0] 
            first_lane_y = arr[i][1] - arr[j][1]
            second_lane_x = arr[j][0] - arr[k][0]
            second_lane_y = arr[j][1] - arr[k][1]
            third_lane_x = arr[i][0] - arr[k][0]
            third_lane_y = arr[i][1] - arr[k][1]
            first_lane = [first_lane_x,first_lane_y]
            second_lane =[second_lane_x,second_lane_y]
            third_lane = [third_lane_x,third_lane_y]
            lane_list = [first_lane,second_lane,third_lane]

            count_1,count_2,count_3 = 0,0,0
            line_1, line_2 = 0,0

            for ele in lane_list :
                if ele[0] == 0 and ele[1] != 0 :
                    count_1 +=1
                    line_1 = abs(ele[1])
                    
                elif ele[0] !=0 and ele[1] == 0 :
                    count_2 +=1
                    line_2 = abs(ele[0])
                
                elif ele[0] != 0 and ele[1] != 0 :
                    count_1 += 1
            if count_1 == count_2 and count_2 == count_3 and count_3 == 1:
                result = line_1*line_2
                result_list.append(result)

print(max(result_list))