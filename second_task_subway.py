# Пока без функций и комментариев, просто не хотел тратить драгоценное время на такое оформление ;)
n1 = int(input())
subway_branch = [tuple(map(int, input().split())) for _ in range(n1)]
n2 = int(input())
request_branch = [tuple(map(int, input().split())) for _ in range(n2)]


for i in range(len(request_branch)):
    need_time = 0
    flag = False
    requested_branch = request_branch[i][0] - 1  # Запрашиваемая ветка
    guys_arrival_time = request_branch[i][1]  # Секунда, когда ребята прибудут в метро
    if subway_branch[requested_branch][0] >= guys_arrival_time:
        print(subway_branch[requested_branch][0])
    else:
        need_time += subway_branch[requested_branch][0]
        while flag is False:
            need_time += subway_branch[requested_branch][1]
            if need_time >= guys_arrival_time:
                print(need_time)
                flag = True
