from js import document 
from js import getInputCode, setInputCode, setHostCode, setDeviceCode
from pyodide.ffi import create_proxy
from compilerlib import apply_transform_on_src

print('hello from my script')

example_inputs = [
    '''
def foo(a: Array(2), b: Array(2)):
    return a * 0.2 + b * 0.8
    ''',
    '''
def foo(a: Array(2), b: Array(2), r: Array(2), iters: int):
    for i in range(iters):
        b = r @ (1.0 / (a @ b))
    return b
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
    newcode = code
    if document.getElementById("to_single_op_form").checked:
        newcode = apply_transform_on_src("to_single_op_form", newcode)
    if document.getElementById("replace_op_with_call").checked:
        newcode = apply_transform_on_src("replace_op_with_call", newcode)
    setHostCode(newcode)