from js import document 
from pyodide.ffi import create_proxy

print('hello from main page!')

abstracts = {
    'High-Level Compiler Optimizations for Python Programs.': 
    '''
    As Python becomes the de facto high-level programming language for many data analytics and scientific computing domains, it becomes increasingly critical to build optimizing compilers that are able to generate efficient sequential and parallel code from Python pro- grams to keep up with the insatiable demands for performance in these domains. Programs written in high-level languages like Python often make extensive use of arrays as a core data type, and mathematical functions applied on the arrays, in conjunction with general loops and element-level array accesses. Such a programming style poses both challenges and opportunities for optimizing compilers. We recognize that current compilers are limited in their ability to make effective use of the high-level operator and loop semantics to generate efficient code on modern parallel architectures. This dissertation presents three pieces of work that demonstrate that compilers that leverage high-level operator and loop semantics can deliver improved performance for Python programs on CPUs and GPUs, relative to past work. On the CPU front, we present Intrepydd, a Python to C++ compiler that compiles a broad class of Python language constructs and NumPy array operators to sequential and parallel C++ code on CPUs. On the GPU front, we present APPy (Annotated Parallelism for Python), which enables users to parallelize generic Python loops and tensor expressions for execution on GPUs by simply adding compiler directives (annotations) to Python code. Then for programs consisting of sparse tensor operators, we introduce ReACT, which consists of a set of code generation techniques that achieve greater redundancy elimination than state-of-the-art.
    ''',

    'APPy: Annotated Parallelism for Python on GPUs.':
    '''
    GPUs are increasingly being used to speed up Python applications in the scientific computing and machine learning domains. Currently, the two common approaches to leveraging GPU acceleration in Python are 1) create a custom native GPU kernel, and import it as a function that can be called from Python; 2) use libraries such as CuPy, which provides pre-defined GPU-implementation-backed tensor operators. The first approach is very flexible but requires tremendous manual effort to create a correct and high performance GPU kernel. While the second approach dramatically improves productivity, it is limited in its generality, as many applications cannot be expressed purely using CuPy’s pre-defined tensor operators. Additionally, redundant memory access can often occur between adjacent tensor operators due to the materialization of intermediate results. In this work, we present APPy (Annotated Parallelism for Python), which enables users to parallelize generic Python loops and tensor expressions for execution on GPUs by adding simple compiler directives (annotations) to Python code. Empirical evaluation on 20 scientific computing kernels from the literature on a server with an AMD Ryzen 7 5800X 8-Core CPU and an NVIDIA RTX 3090 GPU demonstrates that with simple pragmas APPy is able to generate more efficient GPU code and achieves significant geometric mean speedup relative to CuPy (30× on average), and to three state-of-the-art Python compilers, Numba (8.3× on average), DaCe-GPU (3.1× on average) and JAX-GPU (18.8× on average).
    ''',

    'ReACT: Redundancy-Aware Code Generation for Tensor Expressions.':
    '''
    High-level programming models for tensor computations are becoming increasingly popular in many domains such as machine learning and data science. The index notation is one such model that is widely adopted for expressing a wide range of tensor computations algorithmically and also as input to programming systems. In programming systems, sparse tensors can be specified as type annotations, and a compiler can be employed to perform code generation for the specified tensor expressions and sparse formats. Different code generation strategies and optimization decisions can have a significant impact on the performance of the generated code. However, the code generation strategies used by current state-of-the-art tensor compilers can result in redundant computations being present in the output code. In this work, we identify four common types of redundancies that can occur when generating code for compound expressions, and introduce new techniques that can avoid these redundancies. Empirical evaluation on real-world compound kernels, such as Sampled Dense Dense Matrix Multiplication (SDDMM), Graph Neural Network (GNN) and Matricized-Tensor Times Khatri-Rao Product (MTTKRP) shows that our generated code with redundancy elimination can result in performance improvements of 1.1× to 25× relative to a state-of-the-art Tensor Algebra COmpiler (TACO) and up to 101× relative to library approaches such as the SciPy.sparse.
    ''',

    'Intrepydd: Performance, Productivity, and Portability for Data Science Application Kernels.':
    '''
    Major simultaneous disruptions are currently under way in both hardware and software. In hardware, extreme heterogeneity has become critical to sustaining cost and performance improvements after Moore's Law, but poses productivity and portability challenges for developers. In software, the rise of large-scale data science is driven by developers who come from diverse backgrounds and, moreover, who demand the rapid prototyping and interactive-notebook capabilities of high-productivity languages like Python. We introduce the Intrepydd programming system, which enables data scientists to write application kernels with high performance, productivity, and portability on current and future hardware. Intrepydd is based on Python, though the approach can be applied to other base languages as well. To deliver high performance, the Intrepydd toolchain uses ahead-of-time (AOT) compilation and high-level compiler optimizations of Intrepydd kernels. Intrepydd achieves portability by its ability to compile kernels for execution on different hardware platforms, and for invocation from Python or C++ main programs. An empirical evaluation shows significant performance improvements relative to Python, and the suitability of Intrepydd for mapping on to post-Moore accelerators and architectures with relative ease. We believe that Intrepydd represents a new direction of \"Discipline-Aware Languages\" (DiALs), which brings us closer to the holy grail of obtaining productivity and portability with higher performance than current Python-like languages, and with more generality than current domain-specific languages and libraries. <br><img src="pics/DiALs.jpg" alt="Discipline-Aware Languages" width="400" height="auto">
    ''',

    'Valence: Variable Length Calling Context Encoding.': 
    '''
    Many applications, including program optimizations, debugging tools, and event loggers, rely on calling context to gain additional insight about how a program behaves during execution. One common strategy for determining calling contexts is to use compiler instrumentation at each function call site and return sites to encode the call paths and store them in a designated area of memory. While recent works have shown that this approach can generate precise calling context encodings with low overhead, the encodings can grow to hundreds or even thousands of bytes to encode a long call path, for some applications. Such lengthy encodings increase the costs associated with storing, detecting, and decoding call path contexts, and can limit the effectiveness of this approach for many usage scenarios. 
    This work introduces a new compiler-based strategy that significantly reduces the length of calling context encoding with little or no impact on instrumentation costs for many applications. Rather than update or store an entire word at each function call and return, our approach leverages static analysis and variable length instrumentation to record each piece of the calling context using only a small number of bits, in most cases. We implemented our approach as an LLVM compiler pass, and compared it directly to the state-of-the-art calling context encoding strategy (PCCE) using a standard set of C/C++ applications from SPEC CPU 2017. Overall, our approach reduces the length of calling context encoding from 4.3 words to 1.6 words on average (> 60% reduction), thereby improving the efficiency of applications that frequently store or query calling contexts.
    ''',

    'MemBrain: Automated Application Guidance for Hybrid Memory Systems.':
    '''
    Computer systems with multiple tiers of memory devices with different latency, bandwidth, and capacity characteristics are quickly becoming mainstream. Due to cost and physical limitations, device tiers that enable better performance typically include less capacity. Such heterogeneous memory systems require alternative data management strategies to utilize the capacity-constrained resources efficiently. However, current techniques are often limited because they rely on inflexible hardware caching or manual modifications to source code. This paper introduces MemBrain, a new memory management framework that automates the production and use of data-tiering guidance for applications on hybrid memory systems. MemBrain employs program profiling and source code analysis to enable transparent and efficient data placement across different types of memory. It automatically clusters data with similar expected usage patterns into page-aligned regions of virtual addresses (arenas), and uses offline profile feedback to direct low-level tier assignments for each region. We evaluate MemBrain on an Intel Knights Landing server machine with an upper tier of limited capacity (but higher bandwidth) MCDRAM and a lower tier of conventional DDR4 using a selection of high-bandwidth benchmarks from SPEC CPU 2017 as well as two proxy apps (Lulesh and AMG), and one full scale scientific application (QMCPACK). Our evaluation shows that MemBrain can achieve significant performance and efficiency improvements compared to current guided and unguided management strategies.
    ''',

    'On Automated Feedback-Driven Data Placement in Multi-tiered Memory.':
    '''
    Recent emergence of systems with multiple performance and capacity tiers of memory invites a fresh consideration of strategies for optimal placement of data into the various tiers. This work explores a variety of cross-layer strategies for managing application data in multitiered memory. We propose new profiling techniques based on the automatic classification of program allocation sites, with the goal of using those classifications to guide memory tier assignments.We evaluate our approach with different profiling inputs and application strategies, and show that it outperforms other state-of-the-art management techniques.
    ''',
    
}

def toggle_abstract(event):
    event.preventDefault()  # this prevents cursor going back to head of the page on click
    p = event.target.parentElement
    title = p.firstElementChild
    ab = p.lastElementChild
    if ab.innerHTML == "":
        key = title.innerHTML.replace('<u>', '').replace('</u>', '')
        ab.innerHTML = abstracts[key]
        ab.style.borderStyle = "dashed"
        ab.style.borderWidth = "thin"
        ab.style.padding = "10px"
    else:
        ab.innerHTML = ""
        ab.style.borderStyle = ""
        ab.style.padding = ""