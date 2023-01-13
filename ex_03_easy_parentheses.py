#  https://leetcode.com/problems/valid-parentheses/ 

def isValid(s: str) -> bool:
    openings = '([{'
    stack = []
    checklist = False
    
    for p in s:
        if p in openings:
            stack.append(p)
        else:
            if len(stack) == 0:
                return False
            out_opening = stack.pop()
            if out_opening == '(' and p == ')':
                checklist = True
            elif out_opening == '[' and p == ']':
                checklist = True
            elif out_opening == '{' and p == '}':
                checklist = True
            else:
                checklist = False
    if len(stack) != 0:
        checklist = False

    return checklist

# change the string to test other scenarios
print(isValid("({}[])"))

pairs = {
    '(' : ')',
    '[' : ']',
    '{' : '}'
}