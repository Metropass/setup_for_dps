from setuptools import setup 

setup(
name = '', #place your module name here
version = '', #place the version number of your code here
install_requires = ['python_module1','python_module2',], # place any libraries you need here, if the user has missing modules, pip3 will handle it automatically.
py_modules = ['name_of_module'], #the name of the module itself

entry_points={
'console_scripts':
['name_of_keyword_in_cli = name_of_module : name_of_function_to_be_called']} # this entry point will allow your functions to be directly accessed by using a keyword in the cli
)
