def main():
    n, k = map(int, input().split())
    activities = []
    for _ in range(n):
        activities.append(tuple(map(float, input().split())))
    activities.sort(key=lambda act: act[1])
    print(activities)

    classrooms = [0] * k
    room = 0
    no_of_activities = 0
    # Implement 'earliest_finish' and test whether next activity starts after earliest_finish
    for activity in activities:
        for _ in range(k):
            if activity[1] > classrooms[room] and activity[0] > classrooms[room]:
                classrooms[room] = activity[1]
                no_of_activities += 1
                break
            else:
                room = (room + 1) % k
        print(classrooms)
    print(no_of_activities)

if __name__ == '__main__':
    main()
    