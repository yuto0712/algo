n = int(input())
A = [int(input()) for i in range(n)]

L = [float('inf') for _ in range(n)]

L[0] = A[0]
length = 1

def binary_search(value, data):
    left = 0            # 探索する範囲の左端を設定
    right = len(data) - 1            # 探索する範囲の右端を設定
    while left <= right:
        mid = (left + right) // 2            # 探索する範囲の中央を計算
        if data[mid] == value:
            # 中央の値と一致した場合は位置を返す
            return mid
        elif data[mid] < value:
            # 中央の値より大きい場合は探索範囲の左を変える
            left = mid + 1
        else:
            # 中央の値より小さい場合は探索範囲の右を変える
            right = mid - 1
    return left

for i in range(1,n):
    if A[i] > L[length-1]:
        length += 1
        L[length-1] = A[i]
    else:
        L[binary_search(A[i],L)] = A[i]
print(length)