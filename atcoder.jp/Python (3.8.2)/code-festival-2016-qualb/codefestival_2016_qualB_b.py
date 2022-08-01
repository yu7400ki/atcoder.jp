def main():
    _, A, B = map(int,input().split())
    S = input()

    limit = A + B
    foreigner = 0
    passed = 0
    for s in S:
        if s == 'a':
            if passed < limit:
                print('Yes')
                passed += 1
                continue
        elif s == 'b':
            if passed < limit and foreigner < B:
                print('Yes')
                passed += 1
                foreigner += 1
                continue
        print('No')

if __name__ == '__main__':
    main()