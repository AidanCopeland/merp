"""
Tracing functions.

Functions:
    init()
    entry()
    exit()
    flow(log_string)
    detail(log_string)
"""
from builtins import str
import logging
import inspect
from shutil import copyfile
import os


def init(log_file_name):
    """
    Initialize a log file.
    :param log_file_name: The log filename to initialize
    """
    __delete_backup(log_file_name)
    __move_old_log(log_file_name)
    logger = __set_up_logger()
    __set_up_file_handler(logger, log_file_name)


def entry():
    """
    Make a function entry trace.
    :return:
    """
    logger = logging.getLogger('MERP')
    output_string = __generate_output("Entry {")
    logger.info(output_string)


# noinspection PyShadowingBuiltins
def exit():
    """
    Make a function exit trace.
    """
    logger = logging.getLogger('MERP')
    output_string = __generate_output("} Exit")
    logger.info(output_string)


def flow(log_string):
    """
    Make a flow trace.
    :param log_string: The log information to output.
    """
    logger = logging.getLogger('MERP')
    output_string = __generate_output(log_string)
    logger.info(output_string)


def detail(log_string):
    """
    Make a detailed trace.
    :param log_string: The log information to output.
    """
    logger = logging.getLogger('MERP')
    output_string = __generate_output(log_string)
    logger.info(output_string)


def __generate_output(log_string):
    """
    Generate an output line to write to a log file.
    :param log_string: The log information to output.
    :return: The log information, plus the file name, function name and line number.
    """
    (_frame, filename, line_number, function_name, _lines, _index) = inspect.stack()[2]
    filename_separator_index = filename.rfind('\\')
    if filename_separator_index != -1:
        filename = filename[filename_separator_index:]
    joiner = ' '
    filename = '{0:{width}}'.format(filename, width=23)
    function_name = '{0:{width}}'.format(function_name, width=32)
    line_number = '{0:{width}}'.format(str(line_number), width=4)
    output_seq = (filename, function_name, line_number, log_string)
    output_string = joiner.join(output_seq)
    return output_string


def __delete_backup(logger_name):
    """
    Delete a backup log file.
    :param logger_name: The name of the log file to delete.
    """
    logger_backup = logger_name + ".bak"
    if os.path.isfile(logger_backup):
        os.remove(logger_backup)


def __move_old_log(logger_name):
    """
    Update the suffix of an existing log file from .log to .bak
    :param logger_name: The name of the log file to update.
    """
    logger_file = logger_name + ".log"
    logger_backup = logger_name + ".bak"
    if os.path.isfile(logger_file):
        copyfile(logger_file, logger_backup)
        os.remove(logger_file)


def __set_up_logger():
    logger = logging.getLogger('MERP')
    logger.setLevel(logging.DEBUG)
    return logger


def __set_up_file_handler(logger, log_file_name):
    log_file_name_suffix = log_file_name + ".log"
    file_handler = logging.FileHandler(log_file_name_suffix)
    file_handler.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    file_handler.setFormatter(formatter)
