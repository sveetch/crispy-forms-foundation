import os
import io


def read_output(filepath, filename):
    destination = os.path.join(filepath, filename)

    with io.open(destination, 'r', encoding='utf-8') as f:
        content = f.read()

    return content


def write_output(filepath, filename, content):
    if filepath and filepath != '.' and not os.path.exists(filepath):
        os.makedirs(filepath)

    destination = os.path.join(filepath, filename)

    with io.open(destination, 'w', encoding='utf-8') as f:
        f.write(content)

    return destination
