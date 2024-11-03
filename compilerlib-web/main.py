from js import document 
from js import getInputCode, setInputCode, setHostCode, setDeviceCode
from pyodide.ffi import create_proxy
import ast
from compilerlib import *

print('hello from my script')

example_inputs = [
    '''
def foo(a: Array(2), b: Array(2)):
    return a * 0.2 + b * 0.8
    ''',
    '''
def foo(a: Array(2), b: Array(2), r: Array(2), iters: int):
    it = 0
    while it < iters:
        b = r @ (1.0 / (a @ b))
        it = it + 1
    return b
    ''',
    '''
def foo(b: int):
    a = 0
    if b > 0:
        a = b
        b = 100
    else:
        a = b + 1
        b = 200
    print(a)
    a = b + 1
    print(a)
    ''',
    '''
def gcd(a: int, b: int):
    c = a
    d = b
    if c == 0:
        return d
    while d != 0:
        if c > d:
            c = c - d
        else:
            d = d - c
    return c
    '''
]

setInputCode(example_inputs[0].strip())

# page_message = "This example is a code generator."
# pydom["div#page-message"].html = page_message

def show_input(event):
    id = document.getElementById("input-examples").value
    setInputCode(example_inputs[int(id)-1].strip())


def on_key_press(event):
    key = event.key
    if event.altKey and event.code == 'KeyC':
        compile()

document.addEventListener('keydown', create_proxy(on_key_press))

def compile(event=None):
    code = getInputCode()
    tree = code_to_ast(code)
    if document.getElementById("to_single_op_form").checked:
        tree = apply_transform_on_ast("to_single_op_form", tree)
    if document.getElementById("replace_op_with_call").checked:
        tree = apply_transform_on_ast("replace_op_with_call", tree)
    if document.getElementById("show_reaching_defs").checked:
        tree = apply_transform_on_ast("attach_preds_succs_exit_based", tree)
        tree = apply_transform_on_ast("attach_reaching_defs", tree)
        tree = apply_transform_on_ast("show_reaching_defs", tree)
    setHostCode(ast_to_code(tree))