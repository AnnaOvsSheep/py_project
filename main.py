from funcs import sum_num, sub_num


def main():
    a = int(input())
    b = int(input())
    sum_ = sum_num(a, b)
    print(sum_)
    sub_ = sub_num(a, b)
    print(sub_)

if __name__ == "__main__":
    main()