def main():
    T = int(input())
    for j in range(T):
        n = int(input())
        v_1 = list(map(int, input().split()))
        v_2 = list(map(int, input().split()))

        v_1.sort()
        v_2.sort(reverse=True)

        minimum_scalar = 0
        for i in range(n):
            minimum_scalar += v_1[i] * v_2[i]
        case = j+1
        print(f"Case #{case}: {minimum_scalar}")

if __name__ == '__main__':
    main()
    