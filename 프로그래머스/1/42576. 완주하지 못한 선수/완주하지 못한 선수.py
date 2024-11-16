from collections import defaultdict

def solution(participant, completion):
    hash = defaultdict(int)
    for p in participant:
        hash[p] += 1
    for c in completion:
        if hash[c] >= 1:
            hash[c] -= 1
    for key in hash:
        if hash[key] > 0:
            return key