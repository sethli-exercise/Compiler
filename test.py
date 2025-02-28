def test1():
    def chop(string):
        string = string[1:]

    y = "hello"

    print(y)
    chop(y)
    print(y)

def test2():
    class a:
        def __init__(self):
            self.num = 10

    class b:
        def __init__(self):
            self.num = 100

    def change(object):
        object.num += 10

    def changeRef(object):
        object = b()

    obj = a()
    change(obj)
    changeRef(obj)
    print(obj.num)

def test3():
    string = "string"
    print(string[0:7])

def getExpressions(filepath: str) -> list:
    file = open(filepath)
    content = file.read()

    return content.split("\n")

def test4():
    print(getExpressions("expression.txt"))

def main():
    # test1()
    # test2()
    test4()
    return



if __name__ == "__main__":
    main()