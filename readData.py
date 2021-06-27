import re
import trace_log as trace


def read_tabbed_line(input_file):
    last_pos = input_file.tell()
    read_line = input_file.readline()
    read_line = skip_commented_line(input_file, read_line)
    if read_line is None or \
       is_keyword(read_line):
        input_file.seek(last_pos)
        return None
    stripped_line = read_line.strip()
    return read_tabbed_text(stripped_line)


def read_tabbed_text(input_text):
    return read_delimited_text(input_text, '\t+')


def read_semicolon_text(input_text):
    return read_delimited_text(input_text, ';')


def read_delimited_text(input_text, separator):
    entry_list = re.split("%s" % separator, input_text)
    return [x.strip(' ') for x in entry_list]


def get_next_keyword(txt):
    read_line = txt.readline()
    while is_keyword(read_line) is False:
        read_line = txt.readline()
    keyword = read_line[3:].strip()
    return keyword


def move_past_keyword(search_file, reqd_keyword):
    """
    Moves the cursor parsing a file to the next line after the specified keyword.
    :param search_file: File to search in.
    :param reqd_keyword: Keyword to search for.
    """
    keyword = opt_get_next_keyword(search_file, reqd_keyword)
    assert(keyword == reqd_keyword)


def opt_get_next_keyword(txt, reqd_keyword):
    last_pos = txt.tell()
    trace.detail("Look for %r" % reqd_keyword)
    read_line = txt.readline()
    while is_keyword(read_line) is False:
        read_line = txt.readline()
    keyword = read_line[3:].strip()
    if keyword == reqd_keyword:
        trace.flow("Found keyword")
        return keyword
    else:
        txt.seek(last_pos)
        trace.flow("Keyword not found")
        return None


def skip_commented_line(txt, line):
    while ((line is not None) and
           (is_keyword(line) is False) and
           (is_comment(line))):
        line = txt.readline()
    return line


def is_keyword(line):
    if line[:3] == '###':
        return True
    else:
        return False


def is_comment(line):
    if line is None:
        pass
    if line[0] == '\n' or line[0] == '#':
        return True
    else:
        return False
