for i in range(40):
    for n in range(20):
        if i % 2 == 1:
            print("X", end=""), print("O", end=""),
        if i % 2 == 0:
            print("O", end=""), print("X", end=""),
    print()
