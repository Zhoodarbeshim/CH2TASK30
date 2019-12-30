def get_similar():
    a = input("enter the some text: ")
    b = input("enter similar word: ")
    c = 0
    for i in a:
        if i == b:
            c += 1
    return c
print(get_similar())