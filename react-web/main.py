from js import document 
from js import getInputCode, setInputCode, setHostCode, setDeviceCode
from pyodide.ffi import create_proxy
import ast
import react
from react import compile_from_src

print('loaded react: ', react.__file__)

example_inputs = [
'''
def kernel(alpha, x: Index('i'), y: Index('i')):
    return alpha * x + y
''',
'''
def kernel(A: Index('i,j'), b: Index('j')):
    return relu(A + b)
''',
'''
def kernel(alpha, A: Index('i,j')):
    return where(A < 0, alpha * A, A)
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
    if event.code == 'F1':
        compile()

document.addEventListener('keydown', create_proxy(on_key_press))

def compile(event=None):
    code = getInputCode()
    trie_fuse = parallelize = False
    if document.getElementById("trie-fusion").checked:
        trie_fuse = True
    if document.getElementById("parallelization").checked:
        parallelize = True
    newcode = compile_from_src(code, trie_fuse=trie_fuse, parallelize=parallelize)
    setHostCode(newcode)