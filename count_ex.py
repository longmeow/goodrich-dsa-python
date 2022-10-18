def module(group: int, total: int) -> int:
    return [i for i in range(1, total+1) if i%6 == group]


def main():
    group = int(input("Nhóm nào bạn êy (1-6): "))
    total = int(input("Tổng số bài: "))
    if group == 6:
        group = 0
    print('Bài của đồng chí đây nhé =)): {}'.format(module(group, total)))


if __name__ == "__main__":
    main()