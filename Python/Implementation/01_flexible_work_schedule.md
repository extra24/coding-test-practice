# Flexibgle Work Schedule - 유연근무제

## 문제 정보

- **출처:** 프로그래머스 코딩테스트 문제
- **난이도:** Level 1
- **문제 링크:** [프로그래머스 - 유연 근무제 문제](https://school.programmers.co.kr/learn/courses/30/lessons/388351)
- **문제 설명**
  프로그래머스 사이트를 운영하는 그렙에서는 재택근무와 함께 출근 희망 시각을 자유롭게 정하는 유연근무제를 시행하고 있습니다. 제도 정착을 위해 오늘부터 일주일 동안 각자 설정한 출근 희망 시각에 늦지 않고 출근한 직원들에게 상품을 주는 이벤트를 진행하려고 합니다.

직원들은 일주일동안 자신이 설정한 출근 희망 시각 + 10분까지 어플로 출근해야 합니다. 예를 들어 출근 희망 시각이 9시 58분인 직원은 10시 8분까지 출근해야 합니다. 단, 토요일, 일요일의 출근 시각은 이벤트에 영향을 끼치지 않습니다. 직원들은 매일 한 번씩만 어플로 출근하고, 모든 시각은 시에 100을 곱하고 분을 더한 정수로 표현됩니다. 예를 들어 10시 13분은 1013이 되고 9시 58분은 958이 됩니다.

당신은 직원들이 설정한 출근 희망 시각과 실제로 출근한 기록을 바탕으로 상품을 받을 직원이 몇 명인지 알고 싶습니다.

직원 n명이 설정한 출근 희망 시각을 담은 1차원 정수 배열 schedules, 직원들이 일주일 동안 출근한 시각을 담은 2차원 정수 배열 timelogs, 이벤트를 시작한 요일을 의미하는 정수 startday가 매개변수로 주어집니다. 이때 상품을 받을 직원의 수를 return 하도록 solution 함수를 완성해주세요.

## 문제 접근 방식

### 코드 설명

#### **첫 번째 풀이 (오답)**

```python
def solution(schedules, timelogs, startday):
    answer = 0
    day = startday
    for i in range(len(schedules)):
        sch = schedules[i] + 10
        flag = 0
        for j in range(7):
            time = timelogs[i][j]
            if (sch < time and day < 6):
                flag = 1
            if (day < 7):
                day += 1
            else:
                day = 1
        if (flag != 1):
            answer += 1
    return answer
```

- **오류 원인:** `schedules[i] + 10`으로 10분을 더하는 방식이 잘못되어 50분이 넘어가는 시간대는 제대로 처리하지 못함

#### **두 번째 풀이 (정답)**

```python
def solution(schedules, timelogs, startday):
    answer = 0
    day = startday
    for i in range(len(schedules)):
        sch = schedules[i] + 10 if schedules[i] % 100 < 50 else schedules[i] + 50
        flag = 0
        for j in range(7):
            time = timelogs[i][j]
            if (sch < time and day < 6):
                flag = 1
            if (day < 7):
                day += 1
            else:
                day = 1
        if (flag != 1):
            answer += 1
    return answer
```

- **수정 사항:**
  - `schedules[i] % 100 < 50`을 확인하여, 분 단위가 50 이상일 경우 시간을 올바르게 조정

## 개선할 점

- `day` 값을 매일 증가시키는 방식 대신, **주말을 미리 건너뛰는 방식**으로 개선 가능
- `schedules[i] + 10 if schedules[i] % 100 < 50 else schedules[i] + 50` 부분을 별도 함수로 분리하여 **가독성 향상**
- 현재 **이중 반복문을 사용하여 출근 기록을 검사**하는데, O(n^2) 복잡도를 줄이는 방법 고민 필요
- `if (day < 7): day += 1 else: day = 1` 부분을 **요일을 1~5(월~금)로 제한하는 방식으로 단순화 가능**
