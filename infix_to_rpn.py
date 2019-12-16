#!/usr/bin/env python3

L, R = 'L', 'R'
 
NUM, LPAREN, RPAREN = 'NUMBER', '(', ')'

ops = {
    '^': (4, R),
    '*': (3, L),
    '/': (3, L),
    '+': (2, L),
    '-': (2, L),
    '(': (9, L),
    ')': (0, L),
}
 
 
def process_input(expression):
    tokens = expression.strip().split()
    tokenvals = []
    for token in tokens:
        if token in set('1234567890.'):
            tokenvals.append((NUM, token))
        elif token in ops:    
            tokenvals.append((token, ops[token]))
        else:
            raise ValueError("Invalid Token: {}".format(token))
    return tokenvals
 

def shunting(tokenvals):
    outq, stack = [], []
    for token, val in tokenvals:
        if token is NUM:
            outq.append(val)
        elif token in ops:
            t1, (p1, a1) = token, val
            while stack:
                t2, (p2, a2) = stack[-1]
                if (a1 == L and p1 <= p2) or (a1 == R and p1 < p2):
                    if t1 != RPAREN:
                        if t2 != LPAREN:
                            stack.pop()
                            outq.append(t2)
                        else:    
                            break
                    else:        
                        if t2 != LPAREN:
                            stack.pop()
                            outq.append(t2)
                        else:    
                            stack.pop()
                            break
                else:
                    break
            if t1 != RPAREN:
                stack.append((token, val))
    while stack:
        t2, (p2, a2) = stack[-1]
        stack.pop()
        outq.append(t2)
    return ' '.join(outq)
 

if __name__ == '__main__':
    expression = input('> ')
    rp = shunting(process_input(expression))
    print(rp)

