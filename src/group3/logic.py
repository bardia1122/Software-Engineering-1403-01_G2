# from django.shortcuts import render
# from hazm import Normalizer # type: ignore
# from .models import TextOptimization

# def process_input(input_text):
#     normalizer = Normalizer()
#     optimized_text = normalizer.normalize(input_text)
#     return optimized_text

def fix_delimiters(input_text):
    stack = []
    output = []
    match = {')': '(', '}': '{', ']': '['}

    for c in input_text:
        if c in match.values():
            output.append(c)
            stack.append(c)
           
        elif c in match.keys():
            if stack and stack[-1] == match[c]:
                stack.pop()
                output.append(c)
        else:
            output.append(c)

    while stack:
        check = stack.pop()
        output.append(')' if check == '(' else 
                          '}' if check == '{' else ']')

    return ''+(str)(output)
print(fix_delimiters("uo)"))  

