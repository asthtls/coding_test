def solution(hp):
    g_ant = 5
    s_ant = 3
    w_ant = 1
    
    cnt = 0
    
    cnt += hp // g_ant
    hp%=g_ant
    
    cnt += hp // s_ant
    hp%=s_ant
    
    cnt += hp // w_ant
    
    return cnt