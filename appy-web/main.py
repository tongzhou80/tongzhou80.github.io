from js import document 
from js import getInputCode, setInputCode, setHostCode, setDeviceCode
from pyodide.ffi import create_proxy
import ast
import appy
from appy import compile_from_src

print('hello from my script')

example_inputs = [
'''
def add_two_vec(a, b):
    c = torch.empty_like(a)
    #pragma parallel for simd
    for i in range(a.shape[0]):
        c[i] = a[i] + b[i]
    return c
''',
'''
def vector_sum(a):
    ## Zero-initialize the output array
    b = torch.zeros(1, dtype=a.dtype)
    #pragma parallel for simd
    for i in range(a.shape[0]): 
        #pragma atomic
        b[0] += a[i]
    return b
''',
'''
def spmv(A_data, A_indptr, A_indices, x, M, N):
    y = torch.empty(M, dtype=x.dtype)
    #pragma parallel for
    for i in range(M):
        start, end = A_indptr[i], A_indptr[i+1]
        y[i] = 0.0
        #pragma simd
        for j in range(start, end):
            #col = A_indices[j]
            #y[i] += A_data[j] * x[col]
            y[i] += A_data[j] * x[A_indices[j]]
    return y
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
    newcode = compile_from_src(code)
    setHostCode(newcode)