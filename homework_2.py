def check_braces(braces):
    checker = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    list = []
    for brace in braces:
        if brace in checker.values():
            list.append(brace)
        elif list and brace in checker.keys():
            if list[-1] == checker[brace]:
                list.pop()
            else:
                return 'Error %s' % brace
        elif not list and brace in checker.keys():
            return 'Error %s' % brace
print(check_braces('[( )]'))


#() ((([])))}