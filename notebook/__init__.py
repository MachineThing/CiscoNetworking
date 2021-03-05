import os
from shutil import copyfile

def init():
    try:
        os.mkdir('build')
    except FileExistsError:
        for root, dirs, files in os.walk('build'):
            for file in files:
                os.remove(os.path.join(root, file))
    copyfile('index.css', 'build/index.css')
    copyfile('index.html', 'build/index.html')

# popoptions are Pass Options
def generate(poptions, content):
    options = {}
    try:
        options['cat'] = poptions['cat'] # cat means CATegory
    except TypeError:
        options['cat'] = 'Cisco Networking Notebook'
    try:
        options['name'] = poptions['name']
    except TypeError:
        raise NameError('Your file must have a name!')
    try:
        options['exname'] = poptions['exname']
    except KeyError:
        options['exname'] = options['name']

    html = open('notebook/template.html', 'r')
    render = html.read().replace('{{ cat }}', options['cat'])
    render = render.replace('{{ name }}', options['name'])
    render = render.replace('{{ exname }}', options['exname'])
    render = render.replace('{{ data }}', content)
    filesafename = options['name'].replace(' ', '')
    file = open('build/'+filesafename+'.html', 'w')
    file.write(render)
    file.close()
