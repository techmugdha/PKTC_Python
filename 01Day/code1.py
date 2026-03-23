import ast
import astpretty

code = "print('Hello world!')"
tree = ast.parse(code)
astpretty.pprint(tree)