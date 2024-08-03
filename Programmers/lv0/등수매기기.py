def solution(score):
    averages = [sum(s) / 2 for s in score]
    
    sorted_scores = sorted(averages, reverse=True)
    ranks = [sorted_scores.index(avg) + 1 for avg in averages]
    
    return ranks