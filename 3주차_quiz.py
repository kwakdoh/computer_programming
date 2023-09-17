# 환율표 (1달러 = 1320원, 1엔 = 950원, 1위안 = 182원)
exchange_rates = {
    '달러': 1320,
    '엔화': 950,
    '위안': 182
}# 철수가 가진 돈 (달러, 엔화, 위안화 순서로)
money = [13, 200, 13]


# 각 통화를 원화로 변환하고 합산
total_won = money[0] * exchange_rates["달러"] + money[1] * exchange_rates["엔화"] + money[2] * exchange_rates["위안"]

# 결과 출력
print(f"철수가 가지고 있는 돈의 원화 가치는 {total_won}원 입니다")
