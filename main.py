from js import document 
from pyodide.ffi import create_proxy

print('hello from main page!')

abstracts = {
    'High-Level Compiler Optimizations for Python Programs.': 
    """
    As Python becomes the de facto high-level programming language for many data analytics and scientific computing domains, it becomes increasingly critical to build optimizing compilers that are able to generate efficient sequential and parallel code from Python pro- grams to keep up with the insatiable demands for performance in these domains. Programs written in high-level languages like Python often make extensive use of arrays as a core data type, and mathematical functions applied on the arrays, in conjunction with general loops and element-level array accesses. Such a programming style poses both challenges and opportunities for optimizing compilers. We recognize that current compilers are limited in their ability to make effective use of the high-level operator and loop semantics to generate efficient code on modern parallel architectures. This dissertation presents three pieces of work that demonstrate that compilers that leverage high-level operator and loop semantics can deliver improved performance for Python programs on CPUs and GPUs, relative to past work. On the CPU front, we present Intrepydd, a Python to C++ compiler that compiles a broad class of Python language constructs and NumPy array operators to sequential and parallel C++ code on CPUs. On the GPU front, we present APPy (Annotated Parallelism for Python), which enables users to parallelize generic Python loops and tensor expressions for execution on GPUs by simply adding compiler directives (annotations) to Python code. Then for programs consisting of sparse tensor operators, we introduce ReACT, which consists of a set of code generation techniques that achieve greater redundancy elimination than state-of-the-art.
    """
}

def toggle_abstract(event):
    event.preventDefault()  # this prevents cursor going back to head of the page on click
    p = event.target.parentElement
    title = p.firstElementChild
    ab = p.lastElementChild
    if ab.innerHTML == "":
        ab.innerHTML = abstracts[title.innerHTML]
        ab.style.borderStyle = "dashed"
        ab.style.borderWidth = "thin"
        ab.style.padding = "10px"
    else:
        ab.innerHTML = ""
        ab.style.borderStyle = ""
        ab.style.padding = ""