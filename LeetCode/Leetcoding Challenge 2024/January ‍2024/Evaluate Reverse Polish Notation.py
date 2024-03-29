
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for i in range(len(tokens)):

            if tokens[i].isnumeric():
                stack.append(tokens[i])

            elif tokens[i][0]=='-' and len(tokens[i])>1:
                stack.append(tokens[i])

            else:
                num2 = stack.pop()
                num1 = stack.pop()

                if tokens[i]=='+':
                    stack.append(str(int(num1) + int(num2)))

                elif tokens[i]=='*':
                    stack.append(str(int(num1) * int(num2)))

                elif tokens[i]=='-':
                    stack.append(str(int(num1) - int(num2)))

                elif tokens[i]=='/':
                    temp = int(num1) / int(num2)

                    if temp<0:
                        temp = math.ceil(temp)
                        
                    elif temp>0:
                        temp = math.floor(temp)
                    stack.append(str(int(temp)))
                    
        return int(stack[0])
      
