def FooBar(n):
    for i in range(1, n):
        if i % 3 == 0 and i % 5 == 0:
            print(i, "FooBar")
        elif i % 3 == 0:
            print(i, "Foo")
        elif i % 5 == 0:
            print(i, "Bar")
        else:
            print(i)


FooBar(20)