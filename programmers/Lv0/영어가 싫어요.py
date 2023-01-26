# 프로그래머스 입문 영어가 싫어요

def solution(numbers):
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for idx, word in enumerate(words):
        numbers = numbers.replace(word, str(idx))
    
    return int(numbers)