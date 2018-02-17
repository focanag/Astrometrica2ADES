#!/usr/bin/env python

from __future__ import print_function
try:
    import configparser
except ImportError:
    import ConfigParser as configparser

def parse_header(header_lines):

    version_string = "# version=2017"
    observatory = ''

    if type(header_lines) != list:
        header_lines = [header_lines,]
    for line in header_lines:
        if line[0:3] == 'COD':
            observatory = parse_obscode(line[4:])
    header = version_string + '\n' + observatory
    return header

def parse_obscode(code_line):
    config = configparser.ConfigParser()
    config.read('config.ini')

    site_name = config.get('OBSERVATORY', 'SITE_NAME')
    observatory = ( "# observatory" + "\n"
                    "! mpcCode " + code_line.strip() + "\n")
    if site_name:
        observatory += "! name " + site_name +"\n"

    return observatory