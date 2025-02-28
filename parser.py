import opera

class Parser:
    def __init__(self):
        return

    # def parse(self, expression: str):
    #     pass

class BinaryOperatorParser(Parser):
    def parse(self, expression: str, operator: opera.Opera):
        pass

class UnaryOperatorParser(Parser):
    def parse(self, expression: str, operator: opera.UnaryOperator):
        pass

########################################################################################################################
# All mathematical operator parsers ####################################################################################
########################################################################################################################
class PlusParser(BinaryOperatorParser):
    def parse(self, expression: str, operator: opera.Opera):
        if expression[0:2] == "+":
            operator.__class__ = opera.Plus
            return 0b1000
        return 0b0000

class MinusParser(BinaryOperatorParser):
    def parse(self, expression: str, operator: opera.Opera):
        if expression[0:2] == "-":
            operator.__class__ = opera.Minus
            return 0b1000
        return 0b0000

class MultiplyParser(BinaryOperatorParser):
    def parse(self, expression: str, operator: opera.Opera):
        if expression[0:2] == "*":
            operator.__class__ = opera.Multiply
            return 0b1000
        return 0b0000

class DivideParser(BinaryOperatorParser):
    def parse(self, expression: str, operator: opera.Opera):
        if expression[0:2] == "/":
            operator.__class__ = opera.Divide
            return 0b1000
        return 0b0000

class PowerParser(BinaryOperatorParser):
    def parse(self, expression: str, operator: opera.Opera):
        if expression[0:3] == "**":
            operator.__class__ = opera.Power
            return 0b1000
        return 0b0000

class ModulusParser(BinaryOperatorParser):
    def parse(self, expression: str, operator: opera.Opera):
        if expression[0:2] == "%":
            operator.__class__ = opera.Modulus
            return 0b1000
        return 0b0000

########################################################################################################################

########################################################################################################################
# All logical operator parsers #########################################################################################
########################################################################################################################
class AndParser(BinaryOperatorParser):
    def parse(self, expression: str, operator: opera.Opera):
        if expression[0:3] == "&&":
            operator.__class__ = opera.And
            return 0b1000
        return 0b0000

class OrParser(BinaryOperatorParser):
    def parse(self, expression: str, operator: opera.Opera):
        if expression[0:3] == "||":
            operator.__class__ = opera.Or
            return 0b1000
        return 0b0000

class XorParser(BinaryOperatorParser):
    def parse(self, expression: str, operator: opera.Opera):
        if expression[0:3] == "X|":
            operator.__class__ = opera.Xor
            return 0b1000
        return 0b0000


class BitWiseAndParser(BinaryOperatorParser):
    def parse(self, expression: str, operator: opera.Opera):
        if expression[0:2] == "&":
            operator.__class__ = opera.BitWiseAnd
            return 0b1000
        return 0b0000


class BitWiseOrParser(BinaryOperatorParser):
    def parse(self, expression: str, operator: opera.Opera):
        if expression[0:2] == "|":
            operator.__class__ = opera.Xor
            return 0b1000
        return 0b0000

class NotParser(UnaryOperatorParser):
    def parse(self, expression: str, operator: opera.Opera):
        if expression[0:2] == "!":
            operator.__class__ = opera.Not
            return 0b1000
        return 0b0000

########################################################################################################################


class NumberParser(Parser):
    def isDigit(character: chr) -> bool:
        if 46 < ord(character) < 58:
            return True
        return False

    def parse(self, expression: str, operand: opera.Opera):
        decimal = False

        number = ""

        for i in range(len(expression)):
            if expression[i] == " ":
                break
            elif (expression[i] == "." and not decimal) or NumberParser.isDigit(expression[i]):
                number += expression[i]
            else:
                return 0b0000

        if len(number) < 1:
            return 0b0000
        elif decimal:
            operand.__class__ = opera.Operand
            operand.value = float(number)
        else:
            operand.__class__ = opera.Operand
            operand.value = int(number)
        return 0b0100

class BooleanParser(Parser):
    def parse(self, expression: str, operand: opera.Opera):
        if expression[0:2] == "T":
            operand.__class__ = opera.Operand
            operand.value = True
            return 0b0100
        elif expression[0:2] == "F":
            operand.__class__ = opera.Operand
            operand.value = True
            return 0b0100
        else:
            return 0b0000

class LeftParenParser(Parser):
    def parse(self, expression: str):
        if expression[0:2] == "(":
            return 0b0010
        return 0b0000

class RightParenParser(Parser):
    def parse(self, expression: str):
        if expression[0:2] == ")":
            return 0b0001
        return 0b0000