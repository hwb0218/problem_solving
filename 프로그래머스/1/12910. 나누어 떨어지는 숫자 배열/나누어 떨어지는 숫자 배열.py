def solution(arr, divisor):
    answer = []
    for num in arr:
        if num % divisor == 0:
            answer.append(num)
    result = sorted(answer)
    
    if len(answer) == 0:
        result.append(-1)
    
    return result