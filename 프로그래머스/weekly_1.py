def solution(price, money, count):
    ans = money - int((count**2 + count)/2) * price
    return 0 if ans >= 0  else abs(ans)

print(solution(3, 20, 4))