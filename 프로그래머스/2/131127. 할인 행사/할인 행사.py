# 할인 행사
# 입력값 크기 최대 100,000
# O(N^2) 불가능 / O(N)가능
def solution(want, number, discount):
  dict = {}
  for i, w in enumerate(want):
    dict[w] = number[i] 

  result = 0
  # 열흘씩 쇼핑하기 때문에 -9
  # 0 ~ 9(첫번째 날, 열번째 날), 1 ~ 10(둘째 날, 열한번째 날), 2 ~ 11(셋째 날, 열두번째 날)
  for i in range(len(discount) - 9):
    discount_dict = {}
    # i번째 시작일로 부터 +10일
    for j in range(i, i + 10):
      if discount[j] in dict:
        # 만약, "apple"이라는 key가 있으면 +1을 하고, 없다면 "apple"에 1 할당
        discount_dict[discount[j]] = discount_dict.get(discount[j], 0) + 1
    if discount_dict == dict:
      result += 1
  return result