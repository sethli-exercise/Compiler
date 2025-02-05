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
    def __init__(self):
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
        flags = flags | self.LeftParen.parse(token, expressionNode)
        flags = flags | self.RightParen.parse(token, expressionNode)

        return flags

    def parseExpression(self, expression):

        expressionTreeHead = None
        paranQueue = []
        # 1st bit operators, 2nd bit operands 3rd bit left parentheses, 4th bit right parentheses
        expectedOpera = 0b0110
        prevLeftOperand = None
        prevRightOperand = None



        upperTokenIndex = 0
        lowerTokenIndex = 0
        while True:

            lowerTokenIndex = upperTokenIndex
            upperTokenIndex = self.getIndexOfFirstDelim(expression[lowerTokenIndex:], " ")

            if upperTokenIndex == -1:
                # could not find a delimiter
                return

            token = expression[lowerTokenIndex:upperTokenIndex]

            expressionNode = opera.Opera()

            operaType = self.parseToken(token,expressionNode)

            if operaType % 2 != 0 or operaType == 0b0000:
                # nothing was parsed or more than one thing was parsed out of the token
                return
            elif operaType | expectedOpera != expectedOpera:
                # got an unexpected token
                return

            #TODO save the parsed object in the tree in the correct spot

