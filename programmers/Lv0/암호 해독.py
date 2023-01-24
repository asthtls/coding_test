# 프로그래머스 입문 암호 해독

def solution(cipher, code):
    return cipher[code-1::code]