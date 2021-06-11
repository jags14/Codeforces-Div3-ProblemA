t = int(input())


def count_moves(l):
    n = len(l)
    min_entry = min(l)
    max_entry = max(l)
    index_min = l.index(min_entry)
    index_max = l.index(max_entry)
    no_of_moves = 0

    if index_min <= (n - 1) / 2 and index_max <= (n - 1) / 2:
        no_of_moves += max(index_min + 1, index_max + 1)
    if index_min >= (n - 1) / 2 and index_max >= (n - 1) / 2:
        no_of_moves += n - min(index_min, index_max)
    if min(index_min, index_max) < (n - 1) / 2 < max(index_max, index_min):
        if index_min < index_max:
            no_of_moves += min(index_max + 1, index_min + n + 1 - index_max)
        if index_min > index_max:
            no_of_moves += min(index_min + 1, index_max + n + 1 - index_min)

    print(no_of_moves)


for i in range(t):
    list_length = int(input())
    my_list = input().split()
    for j in range(list_length):
        my_list[j] = int(my_list[j])
    count_moves(my_list)
