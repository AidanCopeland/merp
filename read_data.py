"""
Data read utility functions.

Functions:
    read_tabbed_line(input_file)
    read_tabbed_text(input_text)
    read_semicolon_text(input_text)
    read_delimited_text(input_text, separator)
    get_next_keyword(txt)
    move_past_keyword(search_file, reqd_keyword)
    opt_get_next_keyword(txt, reqd_keyword)
    skip_commented_line(txt, line)
    is_keyword(line)
    is_comment(line)
"""
import re
import trace_log as trace


def read_tabbed_line(input_file):
    """
    Find the next non-commented line and parse it separated by tabs.
    :param input_file: The text file to read.
    :return: An array of strings, each entry being the text between each tab.
    """
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
    """
    Parse text separated by tabs
    :param input_text: The text to read.
    :return: An array of strings, each entry being the text between each tab.
    """
    return read_delimited_text(input_text, '\t+')


def read_semicolon_text(input_text):
    """
    Parse text separated by semicolons.
    :param input_text: The text to read.
    :return: An array of strings, each entry being the text between each semicolon.
    """
    return read_delimited_text(input_text, ';')


def read_delimited_text(input_text, separator):
    """
    Parse a set of delimited text.
    :param input_text: The text to read.
    :param separator: The separator in the text.
    :return: An array of strings, each entry being the text between each separator.
    """
    entry_list = re.split("%s" % separator, input_text)
    return [x.strip(' ') for x in entry_list]


def get_next_keyword(txt):
    """
    Find the next keyword in the text.
    :param txt: The text being read.
    :return: The keyword.
    """
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
    assert keyword == reqd_keyword


def opt_get_next_keyword(txt, reqd_keyword):
    """
    Look for the next instance of the specified keyword.
    :param txt: The text being read.
    :param reqd_keyword: The specified keyword.
    :return: The keyword, or None if the keyword is not present in the text.
    """
    last_pos = txt.tell()
    trace.detail("Look for %r" % reqd_keyword)
    read_line = txt.readline()
    while is_keyword(read_line) is False:
        read_line = txt.readline()
    keyword = read_line[3:].strip()
    if keyword == reqd_keyword:
        trace.flow("Found keyword")
        return keyword

    txt.seek(last_pos)
    trace.flow("Keyword not found")
    return None


def skip_commented_line(txt, line):
    """
    Skip past any lines that only contain comments.
    :param txt: The text to read from.
    :param line: The current line.
    :return: The next line that does not only contain comments.
    """
    while ((line is not None) and
           (is_keyword(line) is False) and
           (is_comment(line))):
        line = txt.readline()
    return line


def is_keyword(line):
    """
    Determine whether a line contains a keyword.
    :param line: The line to read.
    :return: True if the line starts with '###', False otherwise.
    """
    return bool(line[:3] == '###')


def is_comment(line):
    """
    Determine whether a line contains a comment.
    :param line: The line to read.
    :return: True if the line is blank or starts with '#', False otherwise
    """
    if line is None:
        pass
    return bool(line[0] == '\n' or line[0] == '#')
