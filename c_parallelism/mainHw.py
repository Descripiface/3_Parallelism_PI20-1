import multiprocessing


# Первое число - строка, второй - столбец, т.е A[0][1] имеет вид:
# . X .
# . . .
# . . .


def show_matrix(A, B):
    print("Матрица A: ")
    for _ in A:
        print(_)
    print()
    print("Матрица B: ")
    for _ in B:
        print(_)


def multiplication(a, B):
    res1 = a[0] * B[0][0] + a[1] * B[1][0] + a[2] * B[2][0]
    res2 = a[0] * B[0][1] + a[1] * B[1][1] + a[2] * B[2][1]
    res3 = a[0] * B[0][2] + a[1] * B[1][2] + a[2] * B[2][2]
    tmp = [res1, res2, res3]
    with open('matC.txt', 'a') as f:
        f.write(' '.join(map(str, tmp)) + "\n")


def main():
    with open("matA.txt") as matA:
        A = [list(map(int, row.split())) for row in matA.readlines()]
    with open("matB.txt") as matB:
        B = [list(map(int, row.split())) for row in matB.readlines()]
    with open('matC.txt', 'w') as f:  # Чтобы файл каждый раз перезаписывался
        f.write("")
    show_matrix(A, B)

    p1 = multiprocessing.Process(target=multiplication, args=[A[0], B])
    p2 = multiprocessing.Process(target=multiplication, args=[A[1], B])
    p3 = multiprocessing.Process(target=multiplication, args=[A[2], B])
    p1.start()
    p2.start()
    p3.start()


if __name__ == "__main__":
    main()
