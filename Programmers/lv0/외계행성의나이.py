def solution(age):
    age_dict = {str(i): chr(97 + i) for i in range(10)}
    return ''.join(age_dict[digit] for digit in str(age))