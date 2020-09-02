def main():
    N = int(input())
    intvls = []

    for _ in range(N):
        s, f = map(int, input().split())
        intvls.append((s, f))
    intvls.sort(key=lambda interval: interval[1])

    start = 0
    no_of_intervals = 0
    for (s, f) in intvls:
        if s >= start:
            no_of_intervals+=1
            start = f
    print(no_of_intervals)

if __name__ == '__main__':
    main()
