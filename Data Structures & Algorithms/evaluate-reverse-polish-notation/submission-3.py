class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ints = []

        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                ints.append(int(token))
            else:
                b = ints.pop()
                a = ints.pop()

                if token == "+":
                    ints.append(a + b)
                elif token == "-":
                    ints.append(a - b)
                elif token == "*":
                    ints.append(a * b)
                else:
                    ints.append(int(a / b))  

        return ints[0]