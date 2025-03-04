def solution(A,B):
    answer = 0
    # 1. 배열의 길이만큼 반복하여 A, B 배열에서 각각 한 개의 숫자를 뽑아 두 수를 곱한 값을 더하여 누적값의 최솟값을 구한다.
    # 2. A 배열은 작은 수 부터 정렬, B 배열은 큰 수부터 차례대로 정렬 후 한 수씩 곱해새 더하면 최솟값 될 거 같음
    
    sortedA = sorted(A)                 # A 배열은 오름차순으로 정렬
    sortedB = sorted(B, reverse=True)   # B 배열은 내림차순으로 정렬
    
    result = [i*j for i, j in zip(sortedA,sortedB)]     # 정렬된 배열의 값을 순서대로 곱하기
    answer = sum(result)                # result 값을 모두 더하기

    return answer