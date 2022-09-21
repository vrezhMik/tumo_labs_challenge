import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv, 
    '%' : operator.mod,
}

def calc(num1, op, num2):
    num1, num2 = int(num1), int(num2)
    return ops[op](num1, num2)

print(calc(1,"+",1))