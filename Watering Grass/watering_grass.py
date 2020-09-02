import math


def main():
    try:
        while True:
            N, l, w = map(int, input().split())

            sprinklers = []
            for _ in range(N):
                x, r = map(float, input().split())
                if w/2 > r:
                    h, s_1 = w/2, r
                else:
                    h, s_1 = r, w/2
                s_2 = math.sqrt(h*h-s_1*s_1)
                sprinklers.append((x-s_2, x+s_2))

            sprinklers.sort(key=lambda cover: cover[0])
            # print(sprinklers)

            no_of_sprinklers = 0
            sprinkler_index = 0
            start = 0
            while sprinkler_index < len(sprinklers) and start < l:
                best_sprinkler = (0,0)
                # print(f"start = {start}")
                # print(f"sprinkler = {sprinklers[sprinkler_index]}")
                while sprinklers[sprinkler_index][0] <= start and sprinklers[sprinkler_index][1] > start:
                    if sprinklers[sprinkler_index][1] > best_sprinkler[1]:
                        best_sprinkler = sprinklers[sprinkler_index]
                    sprinkler_index += 1
                    if sprinkler_index >= len(sprinklers):
                        break
                if best_sprinkler == (0,0):
                    sprinkler_index += 1
                else:
                    no_of_sprinklers += 1
                    start = best_sprinkler[1]
            if no_of_sprinklers == 0:
                print(-1)
            else:
                print(no_of_sprinklers)
    except EOFError as err:
        exit()

if __name__ == '__main__':
    main()
    