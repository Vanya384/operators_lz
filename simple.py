def simple_number(n):
    if n <= 1:
        print(f"{n}-не простое число")
        return -1
    if n > 25:
        print("Ошибка,диапозон значений n равен (1,25]")
        return -1
    for i in range(2,n):
        if n % i == 0:
            print(f"{n}-не простое")
            return -1
    print(f"{n}-простое число")
    return 1


def main():
    n = int(input("Введите n от 1 до 25"))
    simple_number(n)


main()
