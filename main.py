import parserMachine
from parserMachine import ParserStateMachine

def getExpressions(filepath: str) -> list:
    file = open(filepath)
    content = file.read()

    return content.split("\n")

def main():
    expressions = getExpressions("expression.txt")
    expressionParser = ParserStateMachine()

    for expression in expressions:
        print(expressionParser.evalExpression(expression))
    return

if __name__ == "__main__":
    main()