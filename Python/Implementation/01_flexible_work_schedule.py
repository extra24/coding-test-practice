def solution(schedules, timelogs, startday):
    answer = 0
    day = startday
    for i in range(len(schedules)):
        # 출근 가능 시간을 계산 (분이 50 이상일 경우 다음 시로 올림)
        sch = schedules[i] + 10 if schedules[i] % 100 < 50 else schedules[i] + 50
        flag = 0
        for j in range(7):
            time = timelogs[i][j]
            if sch < time and day < 6:  # 주말(토,일)은 체크하지 않음
                flag = 1
            # 요일 업데이트 (월~일 : 1~7)
            day = day + 1 if day < 7 else 1
        if flag != 1:
            answer += 1        
    return answer