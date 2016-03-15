for i in range(10):
    stars=i
    for j in range(10):
        if j==stars:
            print('*', end='')
        else:
            print(' ', end='')
    print("\n")
