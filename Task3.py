N = int(input("Enter the divisor: "))
Numbers = [1, 4, 5, 10, 9]


def division(Numbers, N):
    print("The numbers in ", Numbers, "that are divisible by ", N, "are: ")
    for i in Numbers:
        if i % N == 0:
            print(i, end="\n")


division(Numbers, N)
