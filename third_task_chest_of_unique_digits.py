# Пока без функций и комментариев, просто не хотел тратить драгоценное время на такое оформление ;)
n = int(input())
our_list = list(map(int, input().split()))
unique_digits = set()
flag = False
while flag is False:
    for x in range(len(our_list)):
        unique_digits.add(our_list[x])
        our_list[x] = our_list[x] // 2
        if sum(our_list) == 0:
            flag = True
            break

print(len(unique_digits))