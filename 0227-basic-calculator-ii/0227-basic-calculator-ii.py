class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operator = '+'
        num = 0


        for i, val in enumerate(s):
            if val.isdigit():
                num = num * 10 + int(val)
            
            if val in ['+','-','*','/'] or i == len(s) - 1:
                if operator == '+':
                    stack.append(num)
                elif operator == '-':
                    stack.append(num * -1)
                elif operator == '*':
                    last = stack.pop()
                    stack.append(last * num)
                elif operator == '/':
                    last = stack.pop()
                    stack.append(int(last / num))
                
                operator = val
                num = 0
        return sum(stack)



        

        

            



        
        