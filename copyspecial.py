#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "???"

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    name_dir = [
        os.path.abspath(os.path.join(dirname, f))
        for f in os.listdir(dirname)
        if re.search(r'__(\w+)__', f )]

    return name_dir


def copy_to(path_list, dest_dir):
    """copies path to a new directory"""
    try:
        os.makedirs(dest_dir)
    except OSError as e:
        print(e)    
        exit(1)
    for path in path_list:
        file_name = os.path.basename(path)
        current_path = os.path.dirname(path) 
        new_path = os.path.join(current_path, dest_dir, file_name)
        shutil.copyfile(path, new_path)   


def zip_to(path_list, dest_zip):
    """copies lis to a new zip file"""
    file_zip = []
    for path in path_list:
        file_zip.append(path)
    try:
        print(type(file_zip))
        subprocess.call(["zip", "-j", dest_zip] + file_zip)
    except OSError as e:
        print(e)
        exit(1) 

    return


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help= 'dir search for files')
    ns = parser.parse_args(args)

    if not ns:
        parser.print_usage()
        sys.exit(1)
    if ns.todir:
        copy_to(get_special_paths(ns.from_dir), ns.todir)
    if ns.tozip:
        zip_to(get_special_paths(ns.from_dir), ns.tozip) 
    
    path_list = get_special_paths(ns.from_dir)
    for path in path_list:
        print(path)

   


if __name__ == "__main__":
    main(sys.argv[1:])