def solution1(s):
    answer = ''
    # capitalize() : 맨 첫글자만 대문자 변환
    # title() : 알파벳 외의 문자로 나뉘어져 있는 영단어들의 첫 글자를 모두 대문자로
    # string.capwords() : 문자열의 모든 단어의 첫 글자를 대문자로 바꾸고 숫자다음 문자는 소문자, 공백은 삭제
    arr = s.split(" ")
    for i in arr:
        answer += i.capitalize()
        answer += ' '
    return answer[:-1]

def solution2(s):
    return " ".join(word.capitalize() for word in s.split(" "))