# coding: utf-8
from Data_Structure.stack import Stack
import operator


class BinaryTree:
    def __init__(self, root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.key = obj

    def get_root_val(self):
        return self.key


def build_parse_tree(fpexp):
    fplist = fpexp.split()
    p_stack = Stack()
    e_tree = BinaryTree('')
    p_stack.push(e_tree)
    current_tree = e_tree
    for i in fplist:
        if i == "(":
            current_tree.insert_left('')
            p_stack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif i not in "+-*/)":
            current_tree.set_root_val(eval(i))
            parent = p_stack.pop()
            current_tree = parent
        elif i in "+-*/":
            current_tree.set_root_val(i)
            current_tree.insert_right('')
            p_stack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif i == ")":
            current_tree = p_stack.pop()
        else:
            raise ValueError("Unknown Operator: " + i)
    return e_tree


def evaluate(parse_tree):
    opers = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }
    left_c = parse_tree.get_left_child()
    right_c = parse_tree.get_right_child()

    if left_c and right_c:
        fn = opers[parse_tree.get_root_val()]
        return fn(evaluate(left_c), evaluate(right_c))
    else:
        return parse_tree.get_root_val()


if __name__ == "__main__":
    print(evaluate(build_parse_tree('(3+(4*5))')))
