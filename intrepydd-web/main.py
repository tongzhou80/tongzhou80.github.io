from pyweb import pydom
import ast_comments as ast
from ast_comments import parse, dump
from js import document 
from js import getInputCode, setInputCode, setHostCode, setDeviceCode
import intrepydd

print('hello from my script')

example_inputs = [
    '''
def fib(n: int32) -> int32:
    if n <= 1: 
        return n
    return fib(n - 1) + fib(n - 2)
    ''',

    '''
def mul_add(a: Array(float64, 1), b: Array(float64, 1)):
    return 0.5 * a + b 
    '''
]

setInputCode(example_inputs[0])

# page_message = "This example is a code generator."
# pydom["div#page-message"].html = page_message

def show_input(event):
    id = document.getElementById("input-examples").value
    setInputCode(example_inputs[int(id)-1])


def compile(event):
    dense_array_opt, sparse_array_opt, licm, slice_opt = [False] * 4
    if document.getElementById("dense-array-opt").checked:
        dense_array_opt = True

    # to add code for other opt flags

    code = getInputCode()
    cpp_code = intrepydd.compile_from_src(code, 
                    dense_array_opt=dense_array_opt,
                    sparse_array_opt=sparse_array_opt,
                    licm=licm,
                    slice_opt=slice_opt)
    setHostCode(cpp_code)
    