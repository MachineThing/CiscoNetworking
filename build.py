import glob
import notebook.format
import notebook

notebook.init()

manuals = 'man'
for pyfile in glob.glob('man/**/*.py', recursive=True):
    py = open(pyfile, 'r')
    comp = compile(py.read(), '/', 'exec')
    exec(comp)
    py.close()
