def read_text(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def write_text(filename, text):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)