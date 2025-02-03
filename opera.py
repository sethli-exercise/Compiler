
class Opera:
    def eval(self):
        pass

########################################################################################################################
# All mathematical operators ###########################################################################################
########################################################################################################################
class Operator(Opera):
    def __init__(self, left: any, right: any):
        self.left = left
        self.right = right

    def eval(self):
        pass

class Plus(Operator):
    def __init__(self, left: any, right: any):
        super().__init__(left, right)

    def eval(self):
        return self.left + self.right

class Minus(Operator):
    def __init__(self, left: any, right: any):
        super().__init__(left, right)

    def eval(self):
        return self.left - self.right

class Multiply(Operator):
    def __init__(self, left: any, right: any):
        super().__init__(left, right)

    def eval(self):
        return self.left * self.right

class Divide(Operator):
    def __init__(self, left: any, right: any):
        super().__init__(left, right)

    def eval(self):
        return self.left / self.right

class Power(Operator):
    def __init__(self, left: any, right: any):
        super().__init__(left, right)

    def eval(self):
        return self.left ** self.right

class Modulus(Operator):
    def __init__(self, left: any, right: any):
        super().__init__(left, right)

    def eval(self):
        return self.left % self.right

########################################################################################################################

########################################################################################################################
# All mathematical operands ############################################################################################
########################################################################################################################
class Operand(Opera):
    def __init__(self, value: any):
        self.value = value

    def eval(self):
        return self.value

########################################################################################################################