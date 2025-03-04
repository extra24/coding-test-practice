# Jaden Case - JadenCase 문자열 만들기

## 문제 정보

- **출처:** 프로그래머스 코딩테스트 문제
- **난이도:** Level 2
- **문제 링크:** [프로그래머스 - JadenCase 문자열 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/12951)

### 문제 설명

JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다. 단, 첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은 소문자로 쓰면 됩니다. (첫 번째 입출력 예 참고)
문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.

| s                       | return                  |
| ----------------------- | ----------------------- |
| "3people unFollowed me" | "3people Unfollowed Me" |
| "for the last week"     | "For The Last Week"     |

## 문제 풀이

### 문제 접근 방식

1. 공백을 기준으로 단어를 나눈 후, 각 단여의 첫 글자를 대문자로 변환
2. Python 문자열 메서드 활용 ( `capitalize()` , `title()` , `string.capwords()` )
3. 원본 문자열의 공백 개수를 유지하기 위해 `split(" ")` 을 사용하여 공백도 보존

### 첫 번째 풀이 (오답)

```python
import string

def solution(s):
    answer = string.capwords(s)
    return answer
```

- **오류 원인:** 문자열 앞 뒤에 있는 공백을 보존하지 못함

### 두 번째 풀이 (정답)

```python
def solution1(s):
    answer = ''
    arr = s.split(" ")  # 공백을 기준으로 단어 분리
    for i in arr:
        answer += i.capitalize()  # 첫 글자를 대문자로 변환
        answer += ' '  # 단어 사이 공백 추가
    return answer[:-1]  # 마지막 공백 제거 후 반환
```

- **수정 사항**
  - 문자열 앞 뒤에 있는 공백 보존 및 단어 사이의 공백 추가
  - 마지막 공백 제거 하는 슬라이싱 `[:-1]` 사용

## 개선할 점

- 문자열을 직접 + 연산으로 연결하는 방식으로 성능이 다소 비효율적
- 마지막 공백 제거를 위해 슬라이싱 `[:-1]` 을 사용해야 하는 불편함
- 위의 문제를 해결하기 위해 `join()` 을 대신 사용하여 메모리 낭비 최소화 가능

### 개선된 풀이

```python
def solution2(s):
    return " ".join(word.capitalize() for word in s.split(" "))
```
