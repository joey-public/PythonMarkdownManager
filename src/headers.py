MDX_HTML_HEADER = """
    <script id="MathJax-script" async
      src="https://cdn.jsdelivr.net/npm/mathjax@3.0.0/es5/tex-mml-chtml.js">
    </script>
    <script>
    MathJax = {
      tex: {
          inlineMath: [['$', '$'], ['\(', '\)']]
           }
    };
    </script>
"""

MERMAID_HTML_HEADER = """
<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';
  mermaid.initialize({ startOnLoad: true });
</script>
"""

GEOJSON_HEADER = """
"""

