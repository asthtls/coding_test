def solution(phone_number):
    for i in range(len(phone_number)- 4):
        phone_number = phone_number.replace(phone_number[i], '*', 1) 
    print(phone_number)
    return phone_number