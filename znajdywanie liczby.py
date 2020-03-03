s = 0
f = 100

while True:
    print("Czy to jest wieksze od  {}".format((s+f)/2))
    cmd = input("[y/n]: ")
    if cmd == "y":
        s = (s+f) // 2
    elif cmd == "n":
        f = (s+f) // 2
    else:
        break
