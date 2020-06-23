def recursive_compute_sum(list):
    if len(list) == 0:
        return 0
    else:
        first = list[0]
        rest = list[1:]
        sum = first + recursive_compute_sum(rest)
        return sum


marbles = [10, 13, 39, 14, 41, 9, 3]

sum = recursive_compute_sum(marbles)
print('The total sum is', sum)