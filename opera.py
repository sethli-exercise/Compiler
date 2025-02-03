
class Opera:
    def eval(self):
        pass

class UnaryOperator(Opera):
    def __init__(self, value: any):
        self.value = value

    def eval(self):
        pass

class BinaryOperator(Opera):
    def __init__(self, left: any, right: any):
        self.left = left
        self.right = right

    def eval(self):
        pass

########################################################################################################################
# All mathematical operators ###########################################################################################
########################################################################################################################

class Plus(BinaryOperator):
    def __init__(self, left: any, right: any):
        super().__init__(left, right)

    def eval(self):
        return self.left + self.right
####################################################
class Minus(BinaryOperator):
    def __init__(self, left: any, right: any):
        super().__init__(left, right)

    def eval(self):
        return self.left - self.right
####################################################
class Multiply(BinaryOperator):
    def __init__(self, left: any, right: any):
        super().__init__(left, right)

    def eval(self):
        return self.left * self.right
####################################################
class Divide(BinaryOperator):
    def __init__(self, left: any, right: any):
        super().__init__(left, right)

    def eval(self):
        return self.left / self.right
####################################################
class Power(BinaryOperator):
    def __init__(self, left: any, right: any):
        super().__init__(left, right)

    def eval(self):
        return self.left ** self.right
####################################################
class Modulus(BinaryOperator):
    def __init__(self, left: any, right: any):
        super().__init__(left, right)

    def eval(self):
        return self.left % self.right

########################################################################################################################

########################################################################################################################
# All logical operators ################################################################################################
########################################################################################################################
class And(BinaryOperator):
    def __init__(self, left: any, right: any):
        super().__init__(left, right)

    def eval(self) -> bool:
        return self.left and self.right
####################################################
class Or(BinaryOperator):
    def __init__(self, left: any, right: any):
        super().__init__(left, right)

    def eval(self) -> bool:
        return self.left or self.right
####################################################
class Xor(BinaryOperator):
    def __init__(self, left: any, right: any):
        super().__init__(left, right)

    def eval(self) -> bool:
        return self.left or self.right and not(self.right and self.left)
####################################################
class BitWiseAnd(BinaryOperator):
    def __init__(self, left: any, right: any):
        super().__init__(left, right)

    def eval(self) -> bool:
        return self.left & self.right
####################################################
class BitWiseOr(BinaryOperator):
    def __init__(self, left: any, right: any):
        super().__init__(left, right)

    def eval(self) -> bool:
        return self.left | self.right
####################################################
class Not(UnaryOperator):
    def __init__(self, value: any):
        super().__init__(value)

    def eval(self) -> bool:
        return not self.value

########################################################################################################################


########################################################################################################################
# All operands #########################################################################################################
########################################################################################################################
class Operand(Opera):
    def __init__(self, value: any):
        self.value = value

    def eval(self):
        return self.value

########################################################################################################################