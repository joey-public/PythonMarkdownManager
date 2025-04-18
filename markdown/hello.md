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

---config_start---
{
    "format_md": 0, 
    "format_md_args": {},
    "convert_to_html": 1, 
    "md2html_args": {
        "output_html_files": ["./test.html", "./test2.html"],
        "enable_latex_math": 0, 
        "enable_mermaid_graphs": 0,
        "css_style_path":""
    },
    "format_html": 1,
    "format_html_args": {
        "replace_md_links": 0
      }
}
---config_end---
