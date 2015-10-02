#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'nick'

import optparse
import ConfigParser

def readIniFile(file='python_config.ini'):
    Config = ConfigParser.ConfigParser()
    Config.read(file)
    sections = Config.sections()
    # for section in sections:
    return Config.items('Section Parse_XML_IVI')
        # phrase = Config.items(section)
    # print phrase
    # return phrase

def main():
    pass
    readIniFile()
    p = optparse.OptionParser()
    p.add_option('--sysadmin', '-s', default='BOFH')
    p.add_option('--config', '-c', action='store_true')
    p.add_option('--section', '-p', default='BOFH')
    options, arguments = p.parse_args()
    # print options
    if options.config:
        print readIniFile()
    if options.section:
        print options.section
    else:
        print 'Hello %s' % (options.sysadmin)

if __name__ == '__main__':
    main()
