
class Opera:
    def __init__(self):
        self.left = None
        self.right = None

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
        return self.left.eval() + self.right.eval()
####################################################
class Minus(BinaryOperator):
    def __init__(self, left: any, right: any):
        super().__init__(left, right)

    def eval(self):
        return self.left.eval() - self.right.eval()
####################################################
class Multiply(BinaryOperator):
    def __init__(self, left: any, right: any):
        super().__init__(left, right)

    def eval(self):
        return self.left.eval() * self.right.eval()
####################################################
class Divide(BinaryOperator):
    def __init__(self, left: any, right: any):
        super().__init__(left, right)

    def eval(self):
        return self.left.eval() / self.right.eval()
####################################################
class Power(BinaryOperator):
    def __init__(self, left: any, right: any):
        super().__init__(left, right)

    def eval(self):
        return self.left.eval() ** self.right.eval()
####################################################
class Modulus(BinaryOperator):
    def __init__(self, left: any, right: any):
        super().__init__(left, right)

    def eval(self):
        return self.left.eval() % self.right.eval()

########################################################################################################################

########################################################################################################################
# All logical operators ################################################################################################
########################################################################################################################
class And(BinaryOperator):
    def __init__(self, left: any, right: any):
        super().__init__(left, right)

    def eval(self) -> bool:
        return self.left.eval() and self.right.eval()
####################################################
class Or(BinaryOperator):
    def __init__(self, left: any, right: any):
        super().__init__(left, right)

    def eval(self) -> bool:
        return self.left.eval() or self.right.eval()
####################################################
class Xor(BinaryOperator):
    def __init__(self, left: any, right: any):
        super().__init__(left, right)

    def eval(self) -> bool:
        lval = self.left.eval()
        rval = self.right.eval()
        return lval or rval and not(lval and rval)
####################################################
class BitWiseAnd(BinaryOperator):
    def __init__(self, left: any, right: any):
        super().__init__(left, right)

    def eval(self) -> bool:
        return self.left.eval() & self.right.eval()
####################################################
class BitWiseOr(BinaryOperator):
    def __init__(self, left: any, right: any):
        super().__init__(left, right)

    def eval(self) -> bool:
        return self.left.eval() | self.right.eval()
####################################################
class Not(UnaryOperator):
    def __init__(self, value: any):
        super().__init__(value)

    def eval(self) -> bool:
        return not self.value.eval()

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