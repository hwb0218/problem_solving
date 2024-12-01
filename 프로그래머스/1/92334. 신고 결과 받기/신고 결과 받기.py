def solution(id_list, report, k):
    # 신고당한 유저를 체크할 딕셔너리
    users = [r.split(" ") for r in report]
    reported_users = {}
    
    for user_id, reported_id in users:
        if reported_id not in reported_users:
            reported_users[reported_id] = set()
        reported_users[reported_id].add(user_id)
    
    # k번 이상 신고된 유저가 있을 경우 알림에 대한 횟수 카운트를 체크할 딕셔너리
    count = {}
    for reported_id, user_id_list in reported_users.items():
        if len(user_id_list) >= k:
            for uid in user_id_list:
                if uid not in count:
                    count[uid] = 1
                else:
                    count[uid] += 1

    answer = []
    for i in range(len(id_list)):
        if id_list[i] not in count:
            answer.append(0)
        else:
            answer.append(count[id_list[i]])
    
    return answer
