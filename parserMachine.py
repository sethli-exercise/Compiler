import parser
import opera


'''
      /------------------------\
     /                /\        \   
    /   operand       ) -> operator
   /   /             /
start -> ( -> operand -> operator
      \ \/ \
       \    \
        operator -> invalid

'''

class ParserStateMachine:

    __FLAG_RIGHT_PARENTHESES = 0b0001
    __FLAG_LEFT_PARENTHESES = 0b0010
    __FLAG_OPERAND = 0b0100
    __FLAG_OPERATOR = 0b1000


    def __init__(self):
        self.paranStack = []
        self.expressionTreeHead = None

        # mathematical operator parser instances
        self.plus = parser.PlusParser()
        self.Minus = parser.MinusParser()
        self.Multiply = parser.MultiplyParser()
        self.Divide = parser.DivideParser()
        self.Power = parser.PowerParser
        self.Modulus = parser.ModulusParser()

        # logical operator parser instances
        self.And = parser.AndParser()
        self.Or = parser.OrParser()
        self.Xor = parser.XorParser()
        self.BitWiseAnd = parser.BitWiseAndParser()
        self.BitWiseOr = parser.BitWiseOrParser()
        # self.Not = parser.NotParser() # not used yet

        # operand parsers
        self.Number = parser.NumberParser()
        self.Boolean = parser.BooleanParser()

        # other parsers
        self.LeftParen = parser.LeftParenParser()
        self.RightParen = parser.RightParenParser()

        return

    def getIndexOfFirstDelim(self, expression: str, delim: chr):
        for i in range(len(expression)):
            if expression[i] == delim:
                # slice operator is right operand is exclusive so add 1
                return i + 1

        return -1

    def parseToken(self, token: str, expressionNode: opera.Opera):
        flags = 0b0000

        flags = flags | self.plus.parse(token, expressionNode)
        flags = flags | self.Minus.parse(token, expressionNode)
        flags = flags | self.Multiply.parse(token, expressionNode)
        flags = flags | self.Divide.parse(token, expressionNode)
        flags = flags | self.Power.parse(token, expressionNode)
        flags = flags | self.Modulus.parse(token, expressionNode)

        # logical operator parser instances
        flags = flags | self.And.parse(token, expressionNode)
        flags = flags | self.Or.parse(token, expressionNode)
        flags = flags | self.Xor.parse(token, expressionNode)
        flags = flags | self.BitWiseAnd.parse(token, expressionNode)
        flags = flags | self.BitWiseOr.parse(token, expressionNode)
        # self.Not = parser.NotParser() # not used yet

        # operand parsers
        flags = flags | self.Number.parse(token, expressionNode)
        flags = flags | self.Boolean.parse(token, expressionNode)

        # other parsers
        flags = flags | self.LeftParen.parse(token)
        flags = flags | self.RightParen.parse(token)

        return flags

    def tokenize(self, expression: str):

        tokens = []

        upperTokenIndex = 0
        lowerTokenIndex = 0
        while True:
            lowerTokenIndex = upperTokenIndex
            upperTokenIndex = self.getIndexOfFirstDelim(expression[lowerTokenIndex:], " ")

            if upperTokenIndex == -1:
                # could not find a delimiter
                return tokens

            token = expression[lowerTokenIndex:upperTokenIndex]
            expressionNode = opera.Opera()
            operaType = self.parseToken(token, expressionNode)

            tokens.append([operaType, expressionNode])

    def moreThanOneType(self, operaType: int) -> bool:
        digitCount = 0

        while operaType > 0:
            digit = operaType % 2
            if digit != 0:
                digitCount += 1

            operaType /= 2

        if digitCount > 1:
            return True
        else:
            return False

    def isValidToken(self, operaType, expectedOpera):
        if operaType < 1:
            # nothing was parsed
            return False
        elif self.moreThanOneType(operaType):
            # more than one type was parsed out of the token
            return False
        elif operaType | expectedOpera != expectedOpera:
            # got an unexpected token
            return False
        else:
            return True

    def parseTokensUntilRightParen(self, tokens: list, expectedOpera: int):

        prevOperator = None
        prevLeftOperand = None

        tmpExpressionTreeHead = None

        for i in range(len(tokens)):

            operaType = tokens[i][0]
            expressionNode = tokens[i][1]

            if not self.isValidToken(operaType,expectedOpera):
                return None

            if operaType == ParserStateMachine.__FLAG_LEFT_PARENTHESES:
                expectedOpera = ParserStateMachine.__FLAG_LEFT_PARENTHESES | ParserStateMachine.__FLAG_RIGHT_PARENTHESES | ParserStateMachine.__FLAG_OPERAND

                if tmpExpressionTreeHead is None:
                    tmpExpressionTreeHead = self.parseTokensUntilRightParen(tokens[i+1:],expectedOpera)
                else:
                    tmpExpressionTreeHead.right = self.parseTokensUntilRightParen(tokens[i+1:],expectedOpera)



            elif operaType == ParserStateMachine.__FLAG_RIGHT_PARENTHESES:
                return tmpExpressionTreeHead

            elif operaType == ParserStateMachine.__FLAG_OPERAND:
                expectedOpera = ParserStateMachine.__FLAG_OPERATOR | ParserStateMachine.__FLAG_RIGHT_PARENTHESES

                if prevOperator is not None and prevOperator.right is None:
                    prevOperator.right = expressionNode
                elif prevLeftOperand is None:
                    prevLeftOperand = expressionNode

                

            elif operaType == ParserStateMachine.__FLAG_OPERATOR:
                expectedOpera = ParserStateMachine.__FLAG_OPERAND | ParserStateMachine.__FLAG_LEFT_PARENTHESES

                if tmpExpressionTreeHead is not None:
                    expressionNode.left = tmpExpressionTreeHead

                if prevLeftOperand is not None:
                    expressionNode.left = prevLeftOperand
                    prevLeftOperand = None
                else:
                    return #something went wrong

                tmpExpressionTreeHead = expressionNode
                prevOperator = expressionNode



        return tmpExpressionTreeHead

    def parseExpression(self, expression: str):

        self.expressionTreeHead = None

        expectedOpera = ParserStateMachine.__FLAG_LEFT_PARENTHESES | ParserStateMachine.__FLAG_OPERAND

        tokens = self.tokenize(expression)

        # construct the tree recursively
        self.expressionTreeHead = self.parseTokensUntilRightParen(tokens, expectedOpera)

        # evaluate using DFS
        return self.expressionTreeHead.eval()