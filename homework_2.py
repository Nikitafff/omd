def check_braces(braces):
    checker = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    list = []
    for index, brace in enumerate(braces):
        if brace in checker.values():
            list.append(brace)
            print(list)
        elif brace in checker.keys():
            if list[-1] == checker[brace]:
                list.pop()
            else:
                print(list)
                return 'Error %s' % brace
print(check_braces('() ((([])))}'))