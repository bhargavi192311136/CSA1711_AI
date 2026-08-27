def vacuum_cleaner(room):
    for i in range(len(room)):
        if room[i] == 1:
            print(f"Cleaning room {i}")
            room[i] = 0
    print("All rooms clean:", room)

vacuum_cleaner([1,0,1,1])
