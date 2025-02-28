import parser
import opera

#       /------------------------\
#      /                /\        \
#     /   operand       ) -> operator
#    /   /             /
# start -> ( -> operand -> operator
#       \ \/ \
#        \    \
#         operator -> invalid

class ParserStateMachine:

    __FLAG_RIGHT_PARENTHESES = 0b0001
    __FLAG_LEFT_PARENTHESES = 0b0010
    __FLAG_OPERAND = 0b0100
    __FLAG_OPERATOR = 0b1000


    def __init__(self):
        # self.paranStack = []
        self.expressionTreeHead = None

        # mathematical operator parser instances
        self.Plus = parser.PlusParser()
        self.Minus = parser.MinusParser()
        self.Multiply = parser.MultiplyParser()
        self.Divide = parser.DivideParser()
        self.Power = parser.PowerParser()
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

    def parseToken(self, token: str, expressionNode: opera.Opera):
        flags = 0b0000

        flags = flags | self.Plus.parse(token, expressionNode)
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

        unparsed = expression.split(" ")

        for token in unparsed:
            expressionNode = opera.Opera()
            operaType = self.parseToken(token, expressionNode)

            tokens.append([operaType,expressionNode])

        return tokens

    def moreThanOneType(self, operaType: int) -> bool:
        digitCount = 0

        while operaType > 0:
            digit = operaType % 2
            if digit != 0:
                digitCount += 1

            operaType //= 2

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

    # recursively parse the tokens from left to right
    # if the current token is a left parentheses recurse
    # if the current token is a right parentheses exit the current recursion
    def parseTokensUntilRightParen(self, tokens: list, expectedOpera: int, index: int=0):

        prevOperator = None
        prevLeftOperand = None

        tmpExpressionTreeHead = None


        numTokens = len(tokens)
        while index < numTokens:

            operaType = tokens[index][0]
            expressionNode = tokens[index][1]

            if not self.isValidToken(operaType,expectedOpera):
                return None

            if operaType == ParserStateMachine.__FLAG_LEFT_PARENTHESES:
                expectedOpera = ParserStateMachine.__FLAG_LEFT_PARENTHESES | ParserStateMachine.__FLAG_RIGHT_PARENTHESES | ParserStateMachine.__FLAG_OPERAND
                index += 1

                # recursively parse the expression in the parentheses and set "i" past the right parentheses of the expression
                if tmpExpressionTreeHead is None:
                    tmpExpressionTreeHead, index, expectedOpera = self.parseTokensUntilRightParen(tokens,expectedOpera, index)
                else:
                    tmpExpressionTreeHead.right, index, expectedOpera = self.parseTokensUntilRightParen(tokens,expectedOpera, index)


            elif operaType == ParserStateMachine.__FLAG_RIGHT_PARENTHESES:
                # recursive base case
                expectedOpera = ParserStateMachine.__FLAG_OPERATOR | ParserStateMachine.__FLAG_RIGHT_PARENTHESES
                return tmpExpressionTreeHead, index, expectedOpera

            elif operaType == ParserStateMachine.__FLAG_OPERAND:
                expectedOpera = ParserStateMachine.__FLAG_OPERATOR | ParserStateMachine.__FLAG_RIGHT_PARENTHESES

                # if the last seen operator has an empty right side fill it with the current operand
                if prevOperator is not None and prevOperator.right is None:
                    prevOperator.right = expressionNode
                # otherwise save the operand for later
                elif prevLeftOperand is None:
                    prevLeftOperand = expressionNode

            elif operaType == ParserStateMachine.__FLAG_OPERATOR:
                expectedOpera = ParserStateMachine.__FLAG_OPERAND | ParserStateMachine.__FLAG_LEFT_PARENTHESES

                # if the expression is not empty set the left side to the head
                if tmpExpressionTreeHead is not None:
                    expressionNode.left = tmpExpressionTreeHead

                # if the left side is empty fill the left side with the last seen operand
                if prevLeftOperand is not None:
                    expressionNode.left = prevLeftOperand
                    prevLeftOperand = None
                # else:
                #     return #something went wrong

                # set the head pointer to the new node
                tmpExpressionTreeHead = expressionNode
                prevOperator = expressionNode

            index += 1



        return tmpExpressionTreeHead

    def evalExpression(self, expression: str):

        self.expressionTreeHead = None

        expectedOpera = ParserStateMachine.__FLAG_LEFT_PARENTHESES | ParserStateMachine.__FLAG_OPERAND

        tokens = self.tokenize(expression)

        # construct the tree recursively
        self.expressionTreeHead = self.parseTokensUntilRightParen(tokens, expectedOpera)

        # evaluate using DFS
        return self.expressionTreeHead.eval()