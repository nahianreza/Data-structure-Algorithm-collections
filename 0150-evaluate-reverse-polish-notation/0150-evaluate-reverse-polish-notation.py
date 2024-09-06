class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        valid = ['+', '-', '*', '/']
        for i in tokens:
            if i not in valid:
                stack.append(i)
            else:
                second_item = stack.pop()
                first_item = stack.pop()
                if i == '+':
                    stack.append(int(first_item) + int(second_item))
                elif i == '*':
                    stack.append(int(first_item) * int(second_item))
                elif i == '-':
                    stack.append(int(first_item) - int(second_item))
                elif i == '/':
                    stack.append(int(int(first_item) / int(second_item)))


        return int(stack[0])

                




        