from collections import Counter

def solution(array):
    count = Counter(array)
    
    max_frequency = max(count.values())
    
    mode = [num for num, freq in count.items() if freq == max_frequency]
    
    return mode[0] if len(mode) == 1 else -1