from StackClass import ArrayStack

def checkBrackets(statement):
    stack = ArrayStack(100)
    for ch in statement:
        if ch in ('{', '[', '('):
            stack.push(ch)
        elif ch in ('}', ']', ')'):
            if stack.isempty():
                return False
            else:
                left = stack.pop()
                if (ch == "}" and left != "{") or \
                    (ch == "]" and left != "[") or \
                    (ch == ")" and left != "("):
                    return False
    
    return stack.isEmpty()

str1 = "{A[(i+1)]=0;}"
str2 = "if ((x<0) && (y<3)"
str3 = "while (n<8)) {n++;}"
str4 = "arr[(i+1])=0;"

print(str1, " ---> ", checkBrackets(str1))
print(str2, " ---> ", checkBrackets(str2))
print(str3, " ---> ", checkBrackets(str3))
print(str4, " ---> ", checkBrackets(str4))