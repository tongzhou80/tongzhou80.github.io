import micropip
await micropip.install("pydepcheck")

from js import document, editor
from pyodide.ffi import create_proxy
from pydepcheck import analyze_loop_dependences


DEFAULT_CODE = '''
for i in range(100):
    A[i+1] = A[i]
'''

editor.setValue(DEFAULT_CODE.strip())

def dependences_to_html_list(dependences):
    html = "<ul>"
    for dep in dependences:
        dep_type = type(dep).__name__
        html += f"<li>{dep_type}"

        html += "<ul>"
        html += f"<li>var: {dep.var}</li>"
        html += f"<li>source: {dep.source} (line {dep.source_node.lineno})</li>"
        html += f"<li>sink: {dep.sink} (line {dep.sink_node.lineno})</li>"

        # Handle unanalyzable_subscripts as a nested list
        if dep.unanalyzable_subscripts:
            html += "<li>unanalyzable_subscripts:<ul>"
            for subscript in dep.unanalyzable_subscripts:
                html += f"<li>{subscript}</li>"
            html += "</ul></li>"

        html += "</ul></li>"

    html += "</ul>"
    return html


def on_compile_click(event):
    code_input = editor.getValue()
    try:
        result = analyze_loop_dependences(code_input)
        if result.analyzable:
            if result.dependences:
                output = 'Code is analyzable, the loop dependences are:\n' + dependences_to_html_list(result.dependences)
            else:
                output = 'Code is analyzable, no loop dependences are found.'
        else:
            output = 'Code is not analyzable, the fail reason is:\n' + str(result.fail_reason)

        output += '<em>Note that the analyzer assumes there is no pointer aliasing!</em>'
    except Exception as e:
        output = 'Error: ' + repr(e)
    document.getElementById("analysis-output").innerHTML = output

document.getElementById("compile-button").addEventListener("click", create_proxy(on_compile_click))
