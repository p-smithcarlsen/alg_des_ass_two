def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        customers = []
        for _ in range(N):
            c = input().split(' ', 1)
            customers.append(sum(list(map(float, c[1].split()))))
        customers.sort(reverse=True)
        
        min_ave_wait = 0
        abs_wait = 0
        for i in range(N):
            min_ave_wait += (i+1)*customers[i]
        min_ave_wait = min_ave_wait / N

        print(min_ave_wait)


if __name__ == '__main__':
    main()
    