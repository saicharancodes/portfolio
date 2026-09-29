check = "[{()}][]}"
stack = []
for el in check:
    if el in ['[','{','(']:
        stack.append(el)
    else:
        if not stack:
            print(False)
            break
        check_el = stack.pop()
        if el == ')':
            if not check_el == '(':
                print(False)
                break
        if el == '}':
            if not check_el == '{':
                print(False)
                break
        if el == ']':
            if not check_el == '[':
                print(False)
                break
if stack:
    print(False)


