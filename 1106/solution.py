class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []

        for ch in expression:
            if ch in ('t', 'f', '!', '&', '|'):
                stack.append(ch)

            elif ch == ')':
                values = []

                # collect until operator
                while stack[-1] in ('t', 'f'):
                    values.append(stack.pop())

                op = stack.pop()

                if op == '!':
                    stack.append('t' if values[0] == 'f' else 'f')
                elif op == '&':
                    stack.append('t' if all(v == 't' for v in values) else 'f')
                elif op == '|':
                    stack.append('t' if any(v == 't' for v in values) else 'f')

        return stack[0] == 't'

