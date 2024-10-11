from pyweb import pydom
import ast_comments as ast
from ast_comments import parse, dump
from js import getInputCode, setHostCode, setDeviceCode

print('hello from my script')

import intrepydd

#print(dump(parse(code)))


# page_message = "This example is a code generator."
# pydom["div#page-message"].html = page_message

def compile(event):
    code = getInputCode()
    cpp_code = intrepydd.compile_from_src(code)
    setHostCode(cpp_code)
    setDeviceCode("Device code")
