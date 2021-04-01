def gen_game(size, num_bomb):
    from random import randint as rand

    # size = 8
    # num_bomb = 10
    temp_num_bomb = 0

    n = 0
    fl = [[0 for x in range(0, size + 2)] for y in
          range(0, size + 2)]  # на два размера больше рабочего поля, чтобы не делать
    # исключения для обработки значений у краёв поля

    while 1:
        i1 = rand(1, size - 1)  # размещение бомб(бомба = 9)
        i2 = rand(1, size - 1)
        if fl[i1][i2] != -1:
            fl[i1][i2] = -1
            temp_num_bomb += 1
        if temp_num_bomb == num_bomb:
            break

    # for idx in range(len(fl)):
    #   print(fl[idx])

    for idx in range(1, size + 1):  # просмотр соседних ячеек и подсчёт зачения ячейки(если она не бомба)
        for idx2 in range(1, size + 1):
            temp = 0
            if fl[idx][idx2] == 0:
                for i in range(-1, 2):
                    for g in range(-1, 2):
                        if fl[idx + i][idx2 + g] == -1:
                            temp += 1
                            fl[idx][idx2] = temp
    print(" ")
    for idx in range(len(fl)):
        print(fl[idx])
    return fl



