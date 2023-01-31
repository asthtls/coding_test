# 프로그래머스 입문 로그인 성공?

def solution(id_pw, db):
    
    for i in range(len(db)):
        if id_pw[0] in db[i] and id_pw[1] in db[i]:
            print(id_pw, db[i])
            return "login"
        elif id_pw[0] in db[i] and id_pw[1] not in db[i]:
            return "wrong pw"
    return "fail"

