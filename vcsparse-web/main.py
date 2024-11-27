from js import document 
from js import getInputCode, setInputCode, setHostCode, setDeviceCode
from pyodide.ffi import create_proxy
import ast
from vcsparse import compile_from_src

example_inputs = [
'''
def kernel(alpha, x: Tensor('i'), y: Tensor('i')):
    return alpha * x + y
''',
'''
def kernel(alpha, A: Tensor('i,j')):
    return where(A < 0, alpha * A, A)
''',
'''
def kernel(A: Tensor('i,j')):
    b = sum(A, 1)
    return A / b[:, None]
''',
'''
def kernel(A: Tensor('i,k'), B: Tensor('k,j')):
    return matmul(A, B)
''',
'''
def f5(A: Tensor('i,k', 'csr')):
    b = sum(A, 1)
    return A / b[:, None]
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
    trie_fuse = parallelize = gen_numba_code = memory_opt = use_sparse_output = False
    if document.getElementById("trie-fusion").checked:
        trie_fuse = True
    if document.getElementById("parallelization").checked:
        parallelize = True
    if document.getElementById("gen-numba-code").checked:
        gen_numba_code = True
    if document.getElementById("memory-optimization").checked:
        memory_opt = True
    if document.getElementById("use-sparse-output").checked:
        use_sparse_output = True
    newcode = compile_from_src(code, trie_fuse=trie_fuse, 
                            parallelize=parallelize,
                            gen_numba_code=gen_numba_code,
                            memory_opt=memory_opt,
                            use_sparse_output=use_sparse_output)
    setHostCode(newcode)