#  https://leetcode.com/problems/valid-parentheses/ 

def isValid(string: str) -> bool:
    openings = '([{'
    stack = []
    checklist = False
    
    pairs = {
    '(' : ')',
    '[' : ']',
    '{' : '}'
    }

    for parenthese in string:
        if parenthese in openings:
            stack.append(parenthese)
        else:
            if len(stack) == 0:
                return False
            out_opening = stack.pop()
            if pairs[out_opening] == parenthese:
                checklist = True
            else:
                checklist = False
    if len(stack) != 0:
        checklist = False

    return checklist

# change the string to test other scenarios
print(isValid("({}[])"))
print(isValid("{}([])"))
print(isValid("{[])"))
print(isValid("({}"))
print(isValid("(){"))
