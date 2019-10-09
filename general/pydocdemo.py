'''
There are various tools for creating detailed documentation for the code we wrote. PyDoc is one of them.
You can use pydoc command line utility to generate documentation Ex: $pydoc <filename>.py
To generate documentation using program, just import pydoc module and call help() method
Other popular documentation generation tool is Sphinx - http://www.sphinx-doc.org/en/master/ . To install "pip install -U Sphinx"
'''
import pydoc

help('function1')
help("*.py")