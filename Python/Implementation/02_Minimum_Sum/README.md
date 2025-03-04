# Minimum Sum - 최솟값 만들기

## 문제 정보

- **출처:** 프로그래머스 코딩테스트 문제
- **난이도:** Level 2
- **문제 링크:** [프로그래머스 - 최솟값 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/12941)

### 문제 설명

길이가 같은 배열 A, B 두개가 있습니다. 각 배열은 자연수로 이루어져 있습니다.
배열 A, B에서 각각 한 개의 숫자를 뽑아 두 수를 곱합니다. 이러한 과정을 배열의 길이만큼 반복하며, 두 수를 곱한 값을 누적하여 더합니다. 이때 최종적으로 누적된 값이 최소가 되도록 만드는 것이 목표입니다. (단, 각 배열에서 k번째 숫자를 뽑았다면 다음에 k번째 숫자는 다시 뽑을 수 없습니다.)

예를 들어 A = [1, 4, 2] , B = [5, 4, 4] 라면

A에서 첫번째 숫자인 1, B에서 첫번째 숫자인 5를 뽑아 곱하여 더합니다. (누적된 값 : 0 + 5(1x5) = 5)
A에서 두번째 숫자인 4, B에서 세번째 숫자인 4를 뽑아 곱하여 더합니다. (누적된 값 : 5 + 16(4x4) = 21)
A에서 세번째 숫자인 2, B에서 두번째 숫자인 4를 뽑아 곱하여 더합니다. (누적된 값 : 21 + 8(2x4) = 29)
즉, 이 경우가 최소가 되므로 29를 return 합니다.

배열 A, B가 주어질 때 최종적으로 누적된 최솟값을 return 하는 solution 함수를 완성해 주세요.

## 문제 풀이

### 문제 접근 방식

1. A 배열은 오름차순으로 정렬
2. B 배열은 내림차순으로 정렬
3. 각각의 배열에서 같은 인덱스의 값을 곱한 후 누적하여 최솟값 구하기

### 첫 번째 풀이

```python
def solution(A,B):
    answer = 0
    sortedA = sorted(A)
    sortedB = sorted(B, reverse=True)
    result = [i*j for i, j in zip(sortedA,sortedB)]
    answer = sum(result)
    return answer
```

- **개선 필요:** 변수 선언 줄이고 메모리적으로 유리한지 고려 필요

## 개선할 점

- `sortedA`, `sortedB` 변수에 저장하지 않고 `zip(sorted(A), sorted(B, reverse=True)` 형태로 바로 사용
- 리스트를 따로 따로 생성하지 않고 `sum()` 을 직접 호출하여 `sum(a * b for a, b in zip(sorted(A), sorted(B, reverse=True)))` 와 같이 사용할 수 있음
