def solution(want, number, discount):
    # 할인 행사
# 입력값 크기 최대 100,000
# O(N^2) 불가능 / O(N)가능
        dict = {}
        for i, w in enumerate(want):
            dict[w] = number[i] 

        result = 0
        # 열흘씩 쇼핑하기 때문에 -9
        # 0 ~ 9(첫번째 날, 열번째 날), 1 ~ 10(둘째 날, 열한번째 날), 2 ~ 11(셋째 날, 열두번째 날)
        for i in range(len(discount) - 9):
            discount_dict = {}
            for j in range(i, i + 10):
                if discount[j] in dict:
                    discount_dict[discount[j]] = discount_dict.get(discount[j], 0) + 1
            if discount_dict == dict:
                result += 1
        return result