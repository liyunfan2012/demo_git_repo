# demo_git_repo

Framework for complex number series and dataframes.


## Description

This package contains classes for complex number series 
and dataframe and methods for calculating conjugates and 
rotating series or dataframes.

## Getting Started

### Dependencies

* Describe any prerequisites, libraries, OS version, etc., needed before installing program.
* ex. Windows 10

### Installing

* How/where to download your program
* Any modifications needed to be made to files/folders

### Executing program

* How to run the program
* Step-by-step bullets
```
code blocks for commands
```

## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Contributors names and contact info

ex. Dominique Pizzie  
ex. [@DomPizzie](https://twitter.com/dompizzie)

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the [MIT] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)

# Apendix - Tutorials for buiding the package.



## Sphinx Documentation.

The documentation in the `docs` folder is created from python code docstrings by Sphinx by the steps in [tutorial](https://www.youtube.com/watch?v=BWIrhgCAae0&t=627s). More tutorials

- [Python Documentation with Sphinx by Maksim E. Eren.](https://www.maksimeren.com/post/python-documentation-with-sphinx/)


### Python package
- sphinx
- sphinx_rtd_theme

### Steps for generating html documentation

1. Create Project Directory
* Make directory `docs`.
```shell
demo_git_repo % mkdir docs
```
* Generate configuration files.
```shell
demo_git_repo % cd docs
docs % sphinx-quickstart

> Separate source and build directories (y/n) [n]: y
> Project name: complexdf_processor
> Author name(s): Yunfan Li
> Project release []: 1.0

```

```shell
demo_git_repo % tree
.
├── Makefile
├── build
├── make.bat
└── source
    ├── _static
    ├── _templates
    ├── conf.py
    └── index.rst
```

2. Create base files
```shell
docs % sphinx-apidoc -o ./source -P -f ../impute --separate
Creating file ./source/impute.rst.
Creating file ./source/modules.rst.
```
The `-f` option is to overwrite existing rst files and `-P` is to include private files (filename begen with '_') in the src director.
`--separate` is to make one page for one module.

3. CSS

- Create `my_theme.css`, save in in `source/_static`.
- Add the following in `conf.py`
```python
html_static_path = ['_static']
html_css_files = ['my_theme.css']
```

4. Generate html files
* Modify `docs/source/conf.py`
Add
```python
import os
import sys
sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('../..'))
```
Add
```python
extensions = ["sphinx.ext.todo","sphinx.ext.viewcode","sphinx.ext.autodoc"]
```
Modify
```python
html_theme = 'sphinx_rtd_theme'
```
* Modify index.rst

Add string 'modules' with 3 leading space as
```
.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules
```
* Generate html files
```shell
docs % make clean
docs % make html
```
Copy html and doctree files to `docs` for publishing on github page
```shell
docs % cp -r build/html/* .
docs % cp -r build/doctrees/* .
```
To make Github bypass Jekyll, create an empty file `.nojekyll` in the `doc` folder.

5. View documentation html
- To browse local file, open `index.html` in browser.
- To browse github webpage, 


### Note
- For errors like `WARNING: undefined label: 'abcd'`, it is because `<abcd>` in docstrings. The target is not defined in a rst file. 
- Cross-ref of class ```:class:`~sklearn.impute.KNNImputer` ```, the symbol "~" is used to make the parents packages of `KNNImputer` hidden.
- In `/docs`, create an empty file named .nojekyll to make GitHub will use the Sphinx theme instead of the Jekyll theme.

## doctest