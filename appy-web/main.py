import micropip
await micropip.install("appyc")  # Always installs the latest version

from js import document 
from js import getInputCode, setInputCode, setHostCode, setDeviceCode
from pyodide.ffi import create_proxy
import ast
import appy
from appy import compile_from_src

print('hello from my script')

example_inputs = [
'''
# Note that arrays `a`, `b` and `c` need to be numerical types. 
# And the data needs to be on the GPU memory before calling the kernel.
# To transfer data between host and device, use `to_gpu()` and `to_cpu()`.

def vector_add(a, b, c):
    #pragma parallel for simd
    for i in range(a.shape[0]):
        c[i] = a[i] + b[i]
''',
'''
def vector_reduction(a):
    b = 0.0
    #pragma parallel for simd global(b)
    for i in range(a.shape[0]): 
        #pragma atomic
        b += a[i]
    return b
''',
'''
def spmv(A_data, A_indptr, A_indices, x, y, M, N):
    #pragma parallel for
    for i in range(M):
        y[i] = 0.0
        #pragma simd
        for j in range(A_indptr[i], A_indptr[i+1]):
            y[i] += A_data[j] * x[A_indices[j]]
''',
'''
def jacobi_2d(A, B):
    M, N = A.shape
    for t in range(1, 10):
        #pragma 1:M-1=>parallel 1:N-1=>parallel
        B[1:M-1, 1:N-1] = 0.2 * (A[1:M-1, 1:N-1] + A[1:M-1, :N-2] + A[1:M-1, 2:N] +
                                A[2:M, 1:N-1] + A[0:M-2, 1:N-1])
        #pragma 1:M-1=>parallel 1:N-1=>parallel
        A[1:M-1, 1:N-1] = 0.2 * (B[1:M-1, 1:N-1] + B[1:M-1, :N-2] + B[1:M-1, 2:N] +
                                B[2:M, 1:N-1] + B[0:M-2, 1:N-1])
    return A, B
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
    newcode = newcode.replace('__rewrite_for_range_var', '__range_var')
    setHostCode(newcode)
