# coding:utf-8
import string


class Stack:
    def __init__(self):
        self.items = []

    def is_Empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peak(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def parchecker(symbolstring):
    s = Stack()
    balanced = True
    index = 0
    left_symb = ['(', '{', '[']
    match_dict = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    while index < len(symbolstring) and balanced:
        symb = symbolstring[index]
        if symb in left_symb:
            s.push(symb)
        else:
            if s.is_Empty():
                balanced = False
            else:
                if match_dict[s.peak()] == symb:
                    s.pop()
                else:
                    balanced = False
        index += 1

    if s.is_Empty() and balanced:
        return True
    return False


def baseconverter(num, base):
    digits = '0123456789ABCDEF'
    remstack = Stack()
    while num > 0:
        rem = num % base
        remstack.push(rem)
        num //= base

    string = ''
    while not remstack.is_Empty():
        string += digits[remstack.pop()]
    return string


def infixtopostfix(infixexpre):
    prec = {
        "*": 3,
        "/": 3,
        "+": 2,
        "-": 2,
        "(": 1
    }
    opstack = Stack()
    postfixlist = []

    tokenlist = infixexpre.split()

    for token in tokenlist:
        if token in string.ascii_uppercase:
            postfixlist.append(token)
        elif token == "(":
            opstack.push(token)
        elif token == ")":
            top_token = opstack.pop()
            while top_token != "(":
                postfixlist.append(top_token)
                top_token = opstack.pop()
        else:
            while (not opstack.is_Empty()) and (prec[opstack.peak()] >= prec[token]):
                postfixlist.append(opstack.pop())
            opstack.push(token)

    while not opstack.is_Empty():
        postfixlist.append(opstack.pop())

    return " ".join(postfixlist)


def post_fix_eval(postfixexpr):
    operand_stack = Stack()
    token_list = postfixexpr.split()

    for token in token_list:
        if token in "0123456789":
            operand_stack.push(int(token))
        else:
            oprand2 = operand_stack.pop()
            oprand1 = operand_stack.pop()
            result = eval(str(oprand1) + token + str(oprand2))
            operand_stack.push(result)
    return operand_stack.pop()
