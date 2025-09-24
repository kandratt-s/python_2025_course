def solution(arr):

    n = len(arr)
    if n == 0:
        return []

    p1 = 0
    p2 = n - 1
    res = [0] * n
    idx = n - 1

    while p1 <= p2:
        if abs(arr[p1]) <= abs(arr[p2]):
            res[idx] = abs(arr[p2])
            p2 -= 1
        else:
            res[idx] = abs(arr[p1])
            p1 += 1
        idx -= 1

    return res


print(solution([-6, -3, -2, 0, 1, 2, 5]))  # 0 1 2 2 3 5 6
print(solution([]))  # []
print(solution([-2]))  # [2]
print(solution([-1, 1]))  # [1, 1]
print(solution([-1, 1, 2]))  # [1, 1, 2]