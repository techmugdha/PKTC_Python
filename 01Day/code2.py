import dis 

code = "print('Hello world!')"
compiled_code = compile(code,'<string>','exec')
dis.dis(compiled_code)