def double_char(string):
    for char in string:
        print(char * 2, end='')


double_char('this is the 2 best ice cream flavours')


def double_chars(string):
    to_return = ''
    for char in string:
        to_return += char * 2
    return to_return


double_chars('hello')
