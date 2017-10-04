import re

def read_tabbed_line(input_file):
    last_pos = input_file.tell()
    read_line = input_file.readline()
    read_line = skip_commented_line(input_file, read_line)
    if is_keyword(read_line):
        input_file.seek(last_pos)
        return None
    stripped_line = read_line.strip()
    entry_list = re.split(r'\t+', stripped_line)
    output = [x.strip(' ') for x in entry_list]
    return output


def get_next_keyword(txt):
    read_line = txt.readline()
    while is_keyword(read_line) is False:
        read_line = txt.readline()
    keyword = read_line[3:].strip()
    return keyword


def skip_commented_line(txt, line):
    while ((is_keyword(line) is False) and
           (is_comment(line))):
        line = txt.readline()
    return line


def is_keyword(line):
    if line[:3] == '###':
        return True
    else:
        return False


def is_comment(line):
    if line[0] == '\n' or line[0] == '#':
        return True
    else:
        return False
