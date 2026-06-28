class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        for t in tokens:
            if t in operators:
                num2 = stack.pop()
                num1 = stack.pop()
                if t == '+':
                    res = num1 + num2
                elif t == '-':
                    res = num1 - num2
                elif t == '*':
                    res = num1*num2
                else:
                    res = int(num1/num2)
                stack.append(res)
            else:
                stack.append(int(t))
            print(stack)
        return stack[-1]