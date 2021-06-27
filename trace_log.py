from builtins import str
import logging
import inspect
from shutil import copyfile
import os


def init(log_file_name):
    delete_backup(log_file_name)
    move_old_log(log_file_name)
    logger = set_up_logger()
    set_up_file_handler(logger, log_file_name)


def entry():
    logger = logging.getLogger('MERP')
    output_string = generate_output("Entry {")
    logger.info(output_string)


# noinspection PyShadowingBuiltins
def exit():
    logger = logging.getLogger('MERP')
    output_string = generate_output("} Exit")
    logger.info(output_string)


def flow(log_string):
    logger = logging.getLogger('MERP')
    output_string = generate_output(log_string)
    logger.info(output_string)


def detail(log_string):
    logger = logging.getLogger('MERP')
    output_string = generate_output(log_string)
    logger.info(output_string)


def generate_output(log_string):
    (frame, filename, line_number, function_name, lines, index) = inspect.stack()[2]
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


def delete_backup(logger_name):
    logger_backup = logger_name + ".bak"
    if os.path.isfile(logger_backup):
        os.remove(logger_backup)


def move_old_log(logger_name):
    logger_file = logger_name + ".log"
    logger_backup = logger_name + ".bak"
    if os.path.isfile(logger_file):
        copyfile(logger_file, logger_backup)
        os.remove(logger_file)


def set_up_logger():
    logger = logging.getLogger('MERP')
    logger.setLevel(logging.DEBUG)
    return logger


def set_up_file_handler(logger, log_file_name):
    log_file_name_suffix = log_file_name + ".log"
    fh = logging.FileHandler(log_file_name_suffix)
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    fh.setFormatter(formatter)
