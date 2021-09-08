class Markdown:
    def __init__(self, f):
        self.f = f
        self.text = f.read()
    def add_code(self, code, language=""):
        self.text += f'\n```{language}\n{code}\n```'
    def add_header(self, text, level=1):
        self.text += f'\n{"#"*level} {text}'
    def add_text(self, text):
        self.text += '\n'+text
    def get_text(self):
        return self.text
    def save(self):
        self.f.write(self.text)
def load(f):
    return Markdown(f)
def new(path):
    with open(path, 'w') as f:
        return Markdown(f) 