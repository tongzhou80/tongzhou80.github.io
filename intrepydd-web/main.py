from js import document 
from js import getInputCode, setInputCode, setHostCode, setDeviceCode
from pyodide.ffi import create_proxy
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
    ''',
    '''
def sinkhorm_wmd(K: Array(float64, 2), M: Array(float64, 2), r: Array(float64, 1), x: Array(float64, 2), max_iter: int32, values: Array(float64, 1), columns: Array(int32, 1), indexes: Array(int32, 1), ncols_c: int32) -> Array(float64, 1):

    c = csr_to_spm(values, columns, indexes, ncols_c)
    it = 0
    while it < max_iter:
        u = 1.0 / x
        v = c.spm_mul(div(1.0, K.T @ u))
        x = spmm_dense(div(1.0, r).mul(K), v)

        it += 1

    u = 1.0 / x    
    v = c.spm_mul(div(1.0, K.T @ u))
    return mul(u, spmm_dense(mul(K, M), v)).sum(0)
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
    #if event.altKey and event.code == 'KeyC':
    if event.code == 'F1':
        compile()

document.addEventListener('keydown', create_proxy(on_key_press))

def compile(event=None):
    dense_array_opt, sparse_array_opt, licm, slice_opt, dumppy = [False] * 5
    if document.getElementById("dense-array-opt").checked:
        dense_array_opt = True

    if document.getElementById("sparse-array-opt").checked:
        sparse_array_opt = True

    if document.getElementById("licm").checked:
        licm = True

    if document.getElementById("dumppy").checked:
        dumppy = True

    # if document.getElementById("slice-opt").checked:
    #     slice_opt = True

    # to add code for other opt flags

    code = getInputCode()
    cpp_code, pycode = intrepydd.compile_from_src(code, 
                    dense_array_opt=dense_array_opt,
                    sparse_array_opt=sparse_array_opt,
                    licm=licm,
                    slice_opt=slice_opt,
                    dumppy=True)
    if dumppy:
        setHostCode(pycode)
    else:
        setHostCode(cpp_code)