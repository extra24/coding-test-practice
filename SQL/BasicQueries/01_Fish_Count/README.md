# Fish Count - 특정 물고기를 잡은 총 수 구하기

## 문제 정보

- **출처:** 프로그래머스 코딩테스트 문제
- **난이도:** Level 2
- **문제 링크:** [프로그래머스 - 특정 물고기를 잡은 총 수 구하기 문제](https://school.programmers.co.kr/learn/courses/30/lessons/298518)

### 문제 설명

낚시앱에서 사용하는 FISH_INFO 테이블은 잡은 물고기들의 정보를 담고 있습니다. FISH_INFO 테이블의 구조는 다음과 같으며 ID, FISH_TYPE, LENGTH, TIME은 각각 잡은 물고기의 ID, 물고기의 종류(숫자), 잡은 물고기의 길이(cm), 물고기를 잡은 날짜를 나타냅니다.

| Column name | Type    | Nullable |
| ----------- | ------- | -------- |
| ID          | INTEGER | FALSE    |
| FISH_TYPE   | INTEGER | FALSE    |
| LENGTH      | FLOAT   | TRUE     |
| TIME        | DATE    | FALSE    |

단, 잡은 물고기의 길이가 10cm 이하일 경우에는 LENGTH 가 NULL 이며, LENGTH 에 NULL 만 있는 경우는 없습니다.

FISH_NAME_INFO 테이블은 물고기의 이름에 대한 정보를 담고 있습니다. FISH_NAME_INFO 테이블의 구조는 다음과 같으며, FISH_TYPE, FISH_NAME 은 각각 물고기의 종류(숫자), 물고기의 이름(문자) 입니다.

| Column name | Type    | Nullable |
| ----------- | ------- | -------- |
| FISH_TYPE   | INTEGER | FALSE    |
| FISH_NAME   | VARCHAR | FALSE    |

FISH_INFO 테이블에서 잡은 BASS와 SNAPPER의 수를 출력하는 SQL 문을 작성해주세요.
컬럼명은 'FISH_COUNT`로 해주세요.

## 문제 풀이

### 문제 접근 방식

1. `FISH_NAME_INFO` 테이블에서 **FISH_NAME** 이 **BASS** 또는 **SNAPPER** 인 물고기의 **FISH_TYPE** 을 조회
2. `FISH_INFO` 테이블에서 **FISH_TYPE** 이 위에서 찾은 값과 같은 데이터를 필터링
3. 해당 조건을 만족하는 행 개수를 **COUNT(\*)** 로 반환

### 첫 번째 풀이

```SQL
SELECT
    COUNT(*) AS FISH_COUNT
FROM FISH_INFO
WHERE FISH_TYPE = (SELECT FISH_TYPE FROM FISH_NAME_INFO WHERE FISH_NAME = 'BASS')
OR FISH_TYPE = (SELECT FISH_TYPE FROM FISH_NAME_INFO WHERE FISH_NAME = 'SNAPPER')
```

- **개선 필요:** OR 조건을 사용해서 두 번의 서브쿼리로 인해 쿼리 실행 속도 느림

### 두 번째 풀이

```SQL
SELECT COUNT(*) AS FISH_COUNT
FROM FISH_INFO
WHERE FISH_TYPE IN (
    SELECT FISH_TYPE
    FROM FISH_NAME_INFO
    WHERE FISH_NAME IN ('BASS', 'SNAPPER')
);
```

- **수정 사항**
  - 두 번의 서브쿼리를 **IN** 을 사용하여 한 번의 서브쿼리로 최적화하여 쿼리 실행 속도 최적화

## 개선할 점

- **JOIN** 을 사용하여 직접 **FISH_TYPE** 을 직접 매핑하여 서브쿼리를 줄일 수 있는 방법도 고려해서 테이블 크기가 크다면 이에 맞게 사용할 수 있도록 하기
  -> solution.sql에 해당 쿼리 추가 완료
