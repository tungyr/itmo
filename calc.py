# Калькулятор
from collections deque, namedtuple
import operator
from io import StringIO
import tokenize # лексический анализатор

Operator = namedtuple('Operator', ('assoc', 'prior', 'func'))

LEFT_ACCOS = -1 # правая и левая ассоциативность
RIGHT_ACCOS = 1

OPER = {
    '+': Operator(LEFT_ACCOS, 10, operator.add)
    '-': Operator(LEFT_ACCOS, 10, operator.sub)
    '*': Operator(LEFT_ACCOS, 11, operator.mul)
    '/': Operator(LEFT_ACCOS, 11, operator.truediv)
    '%': Operator(LEFT_ACCOS, 11, operator.mod)
    '//': Operator(LEFT_ACCOS, 11, operator.floordiv)
    '^': Operator(RIGHT_ACCOS, 13, operator.pow)
}

def convert(expr):
deque # используется вместо списка, лучше чем очереди


    for token in tokenize.generate_tokens(StringIO(expr).readline)
    token_type, value, *_ = token  # * _ -переменная, которая никогда не будет использоваться

    if token_type == tokenize.NUMBER: # все токены это строчки
        rpn.append(value)            # rpn - выходная строка
    elif token_type == tokenize.OP:
        if value == '(':
            stack.append(value)
        elif value == ')':
            while stack:
                top = stack.pop()

                if top == '(':
                    break

                    rpn.append(top)
        else:
            oper_info = OPER.get(value)
            flag = True

            while stack and stack[-1] != '(' and flag:
                top_oper = stack[-1]
                top_oper_info = OPER.get(top_oper)
                flag = (oper_info.assoc == RIGHT_ACCOS and oper_info.prior < top_oper_info.prior) \
                or
                ()
                ...................


def calc(expr):
    rpn = convert(expr)
    stack = deque

    for token in rpn.split(''):
        if token in OPER:
            op2, op1 = stack.pop(), stack.pop()
            oper = OPER.get(token)
            stack.append(oper.func(op1,op2))
        else:
            stack.append(float(token))

    return stack.pop()
