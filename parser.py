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

class MinusParser(BinaryOperatorParser):
    def parse(self, expression: str, operator: opera.BinaryOperator):
        if expression[0:2] == "- ":
            operator.eval = opera.Minus.eval

class MultiplyParser(BinaryOperatorParser):
    def parse(self, expression: str, operator: opera.BinaryOperator):
        if expression[0:2] == "* ":
            operator.eval = opera.Multiply.eval

class DivideParser(BinaryOperatorParser):
    def parse(self, expression: str, operator: opera.BinaryOperator):
        if expression[0:2] == "/ ":
            operator.eval = opera.Divide.eval

class PowerParser(BinaryOperatorParser):
    def parse(self, expression: str, operator: opera.BinaryOperator):
        if expression[0:3] == "** ":
            operator.eval = opera.Power.eval

class ModulusParser(BinaryOperatorParser):
    def parse(self, expression: str, operator: opera.BinaryOperator):
        if expression[0:2] == "% ":
            operator.eval = opera.Modulus.eval

########################################################################################################################

########################################################################################################################
# All logical operator parsers #########################################################################################
########################################################################################################################
class AndParser(BinaryOperatorParser):
    def parse(self, expression: str, operator: opera.BinaryOperator):
        if expression[0:3] == "&& ":
            operator.eval = opera.And.eval

class OrParser(BinaryOperatorParser):
    def parse(self, expression: str, operator: opera.BinaryOperator):
        if expression[0:3] == "|| ":
            operator.eval = opera.Or.eval

class XorParser(BinaryOperatorParser):
    def parse(self, expression: str, operator: opera.BinaryOperator):
        if expression[0:3] == "X| ":
            operator.eval = opera.Xor.eval


class BitWiseAndParser(BinaryOperatorParser):
    def parse(self, expression: str, operator: opera.BinaryOperator):
        if expression[0:2] == "& ":
            operator.eval = opera.BitWiseAnd.eval


class BitWiseOrParser(BinaryOperatorParser):
    def parse(self, expression: str, operator: opera.BinaryOperator):
        if expression[0:2] == "| ":
            operator.eval = opera.Xor.eval

class NotParser(UnaryOperatorParser):
    def parse(self, expression: str, operator: opera.UnaryOperator):
        if expression[0:2] == "! ":
            operator.eval = opera.Not.eval
########################################################################################################################


class NumberParser(Parser):
    def isDigit(character: chr) -> bool:
        if 46 < ord(character) < 58:
            return True
        return False

    def parse(self, expression: str):
        decimal = False

        number = ""

        for i in range(len(expression)):
            if expression[i] == " ":
                break
            elif (expression[i] == "." and not decimal) or NumberParser.isDigit(expression[i]):
                number += expression[i]
            else:
                return None

        if decimal:
            return float(number)
        else:
            return int(number)


class BooleanParser(Parser):
    def parse(self, expression: str):
        if expression[0:2] == "T ":
            return True
        elif expression[0:2] == "F ":
            return False
        else:
            return None