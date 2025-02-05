import opera

class Parser:
    def __init__(self):
        return

    # def parse(self, expression: str):
    #     pass

class BinaryOperatorParser(Parser):
    def parse(self, expression: str, operator: opera.BinaryOperator):
        pass

class UnaryOperatorParser(Parser):
    def parse(self, expression: str, operator: opera.UnaryOperator):
        pass

########################################################################################################################
# All mathematical operator parsers ####################################################################################
########################################################################################################################
class PlusParser(BinaryOperatorParser):
    def parse(self, expression: str, operator: opera.BinaryOperator):
        if expression[0:2] == "+ ":
            operator.eval = opera.Plus.eval
            return 0b1000
        return 0b0000

class MinusParser(BinaryOperatorParser):
    def parse(self, expression: str, operator: opera.BinaryOperator):
        if expression[0:2] == "- ":
            operator.eval = opera.Minus.eval
            return 0b1000
        return 0b0000

class MultiplyParser(BinaryOperatorParser):
    def parse(self, expression: str, operator: opera.BinaryOperator):
        if expression[0:2] == "* ":
            operator.eval = opera.Multiply.eval
            return 0b1000
        return 0b0000

class DivideParser(BinaryOperatorParser):
    def parse(self, expression: str, operator: opera.BinaryOperator):
        if expression[0:2] == "/ ":
            operator.eval = opera.Divide.eval
            return 0b1000
        return 0b0000

class PowerParser(BinaryOperatorParser):
    def parse(self, expression: str, operator: opera.BinaryOperator):
        if expression[0:3] == "** ":
            operator.eval = opera.Power.eval
            return 0b1000
        return 0b0000

class ModulusParser(BinaryOperatorParser):
    def parse(self, expression: str, operator: opera.BinaryOperator):
        if expression[0:2] == "% ":
            operator.eval = opera.Modulus.eval
            return 0b1000
        return 0b0000

########################################################################################################################

########################################################################################################################
# All logical operator parsers #########################################################################################
########################################################################################################################
class AndParser(BinaryOperatorParser):
    def parse(self, expression: str, operator: opera.BinaryOperator):
        if expression[0:3] == "&& ":
            operator.eval = opera.And.eval
            return 0b1000
        return 0b0000

class OrParser(BinaryOperatorParser):
    def parse(self, expression: str, operator: opera.BinaryOperator):
        if expression[0:3] == "|| ":
            operator.eval = opera.Or.eval
            return 0b1000
        return 0b0000

class XorParser(BinaryOperatorParser):
    def parse(self, expression: str, operator: opera.BinaryOperator):
        if expression[0:3] == "X| ":
            operator.eval = opera.Xor.eval
            return 0b1000
        return 0b0000


class BitWiseAndParser(BinaryOperatorParser):
    def parse(self, expression: str, operator: opera.BinaryOperator):
        if expression[0:2] == "& ":
            operator.eval = opera.BitWiseAnd.eval
            return 0b1000
        return 0b0000


class BitWiseOrParser(BinaryOperatorParser):
    def parse(self, expression: str, operator: opera.BinaryOperator):
        if expression[0:2] == "| ":
            operator.eval = opera.Xor.eval
            return 0b1000
        return 0b0000

class NotParser(UnaryOperatorParser):
    def parse(self, expression: str, operator: opera.UnaryOperator):
        if expression[0:2] == "! ":
            operator.eval = opera.Not.eval
            return 0b1000
        return 0b0000

########################################################################################################################


class NumberParser(Parser):
    def isDigit(character: chr) -> bool:
        if 46 < ord(character) < 58:
            return True
        return False

    def parse(self, expression: str, operand: opera.Operand):
        decimal = False

        number = ""

        for i in range(len(expression)):
            if expression[i] == " ":
                break
            elif (expression[i] == "." and not decimal) or NumberParser.isDigit(expression[i]):
                number += expression[i]
            else:
                return 0b0000

        if decimal:
            operand.value = float(number)
        else:
            operand.value = int(number)
        return 0b0100

class BooleanParser(Parser):
    def parse(self, expression: str, operand: opera.Operand):
        if expression[0:2] == "T ":
            operand.value = True
            return 0b0100
        elif expression[0:2] == "F ":
            operand.value = True
            return 0b0100
        else:
            return 0b0000

class LeftParenParser(Parser):
    def parse(self, expression: str):
        if expression[0:2] == "( ":
            return 0b0010

class RightParenParser(Parser):
    def parse(self, expression: str):
        if expression[0:2] == ") ":
            return 0b0001