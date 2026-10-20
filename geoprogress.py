def sum_geometry_progress(b,q,n):
    if b < -10_000 or b > 10_000:
        print("Ошибка,b принадлежит промежутку [-10_000,10_000] ")
        return -1
    if q <= 1 or q > 50:
        print("Ошибка,q принадлежит промежутку (1,50]")
        return -1
    if n < 2 or n > 100:
        print("Ошибка,n принадлежит промежутку [2,100]")
        return -1
    return (b * (1 - q**n)) / (1 - q)

def main():
    b=int(input("Введите b от -10_000 до 10_000"))
    q=int(input("Введите q от 1 до 50"))
    n=int(input("Введите n от 2 до 100"))
    print(sum_geometry_progress(b,q,n))


main()