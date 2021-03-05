class element:
    def __init__(self, tag, endtag):
        self.tag = tag
        self.endtag = endtag

class strbuffer:
    def __init__(self):
        self.buffer = ''
    def append(self, data, suffix='\n'):
        self.buffer = self.buffer + data + suffix

paragraph = element('<p>', '</p>')
command = element('<p class=\"command\">', '</p>')

class formatter:
    def __init__(self):
        self.buffer = []
    def append(self, type, text):
        text = text.replace('\n', '<br />')
        text = text.replace('        ', '')
        if type == 'p':
            self.buffer.append([paragraph, text])
        elif type == 'c':
            self.buffer.append([command, text])
        else:
            raise KeyError('Unknown type: \"'+type+'\"')
    def compile(self):
        cbuffer = strbuffer()
        key = None
        for text in self.buffer:
            if key != text[0]:
                if key != None:
                    cbuffer.append(key.endtag + '\n'+text[0].tag)
                    cbuffer.append(text[1] + '<br />')
                else:
                    cbuffer.append(text[0].tag + text[1])
                key = text[0]
            else:
                cbuffer.append(text[1] + '<br />')
        cbuffer.append(key.endtag)
        return cbuffer.buffer
