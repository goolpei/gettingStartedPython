from typing import List

def evalRPN(tokens: List[str]) -> int:
        if not tokens: return 0
        stack = []

        def calculate(p2, p1, op):
            if op == '+':
                return p2 + p1
            elif op == '-':
                return p2 - p1
            elif op == '*':
                return p2 * p1
            else:
                return int(p2 / p1)

        for token in tokens:
            if token not in ('+', '-', '*', '/'):
                stack.append(int(token))
            else:
                operation = token
                pop1 = stack.pop()
                pop2 = stack.pop()

                stack.append(calculate(pop2, pop1, operation))
        return stack[0]

print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))