# Hello World 

This is a test of my site generator. I still have a bit more work to do on this.

[link to another file](~/Documents/PythonMarkdownManager/markdown/hello2.md)

## Images

**Figure 1:** hello

**Figure 2:** world

## Latex Math

This is inline math $a^2 + b^2 = c^2$

And this is a math block

$$
\nabla \dot \bf{E} = \frac{\rho}{\epsilon_0} \tag{1}
$$

**Equation 1:** Maxwell's Equation for Guass's Law 

$$
\nabla \dot \bf{B} = 0 \tag{2}
$$

**Equation 2:** Maxwell's Equation for Guass's Law for Magnetism

$$
\int_{a}^{b} f^{'} (t) dt = f(b) - f(a) \tag{1}
$$

**Equation 3:** Fundamental Theorem of Calculus


## Mermaid Graphs

~~~mermaid
graph TB
A --> B
B --> C
~~~

**Figure 3:** Mermaid graph example

---config_start
{
    "renumber_all": 0,
    "renumber_figures": 0, 
    "renumber_tables": 0,
    "renumber_equations": 0,
    "output_md_path":'',
    "enable_latex_math": 1, 
    "enable_mermaid_graphs": 1,
    "css_style_path": "hello.css",
    "replace_md_file_links": 1,
    "output_html_file": '', 
    "html_dir": []
}
---config_end
