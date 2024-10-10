from pyweb import pydom
import ast_comments as ast
from ast_comments import parse, dump
from js import getInputCode, setHostCode, setDeviceCode

code = 'a = b   # parallel'

print('hello3')

#print(dump(parse(code)))


# page_message = "This example is a code generator."
# pydom["div#page-message"].html = page_message

def compile(event):
    code = getInputCode()
    setHostCode("Host code")
    setDeviceCode("Device code")
