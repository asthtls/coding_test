def solution(id_pw, db):
    
    for i in db:
        if id_pw == i:
            return "login"
        elif id_pw[0] == i[0]:
            return "wrong pw"
    
    return "fail"