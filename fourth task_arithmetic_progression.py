# Пока без функций и комментариев, просто не хотел тратить драгоценное время на такое оформление ;)
n = int(input())
our_list = [int(i) for i in input().split()]

arithmetic_counter = 0
for i in range(len(our_list) - 2):
    if our_list[i+1] - our_list[i] == our_list[i + 2] - our_list[i+1]:
        arithmetic_counter += n - (i + 3) + 1

print(arithmetic_counter)
