from pyweb import pydom
import ast_comments as ast
from ast_comments import parse, dump
from js import getEditor

code = 'a = b   # parallel'

print('hello3')

#print(dump(parse(code)))


page_message = "This example is a code generator."
pydom["div#page-message"].html = page_message

def compile(event):
    code = pydom["textarea#input-code"][0].value
    print(code)
    print(getEditor().getValue())
    pydom["textarea#output-host-code"][0].value = code
