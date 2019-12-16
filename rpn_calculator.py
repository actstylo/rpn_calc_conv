#!/usr/bin/env python3
import operator


ops = { 
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.itruediv,
    '^': operator.pow
}


def eval_expression(tokens, stack=None):
    if stack is None:
        stack = []
    for token in tokens:
        if set(token).issubset(set("0123456789.")):
            stack.append(float(token))
        elif token in ops:
            if len(stack) < 2:
                raise ValueError('Must have at least two parameters to perform op')
            b = stack.pop()
            a = stack.pop()
            op = ops[token]
            stack.append(op(a, b))
        else:
            raise ValueError("Invalid token {token}".format(token))
    return stack


if __name__ == '__main__':
    expression = input('> ')
    stack = eval_expression(expression.split())
    print(stack[0])

