"""
python -m test.complext_float all
"""
import os,sys,xdoctest
sys.path.insert(0,os.path.abspath('..'))
print(__file__)
root_dir = os.join(os.path.abspath('..'),complexdf_processor)
pkg = 'complext_float'
pkg_dir = os.join(root_dir,pkg)

files = ['_base.py',
         '_complext_type.py']

for file in files:
    print(f'Doctesting for file {file}')
    xdoctest.doctest_module(os.join())