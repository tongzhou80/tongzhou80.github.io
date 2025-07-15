

from js import document, editor
from pyodide.ffi import create_proxy

print('hello from my script')

DEFAULT_CODE = '''
for i in range(100):
    A[i] += 1
'''

editor.setValue(DEFAULT_CODE.strip())

def analyze_code(source_code: str) -> str:
    # Your logic using pyvectorizer goes here
    return "Analysis result... for \n" + source_code

def on_compile_click(event):
    code_input = editor.getValue()
    result = analyze_code(code_input)
    document.getElementById("analysis-output").innerText = result

document.getElementById("compile-button").addEventListener("click", create_proxy(on_compile_click))
