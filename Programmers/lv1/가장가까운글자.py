"""
프로그래머스 Lv1 - 가장 가까운 글자 

"""


def solution(s):
    answer = []
    
    char_dict = {}
    
    
    for idx, char in enumerate(s):
        if char in char_dict:
            answer.append(idx - char_dict[char])
        else:
            answer.append(-1)
        
        char_dict[char] = idx
        
    
    return answer
    