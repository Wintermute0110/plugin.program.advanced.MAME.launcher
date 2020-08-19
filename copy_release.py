#!/usr/bin/python3 -B
# -*- coding: utf-8 -*-

# Replace installed stable AML with the development version in this directory.
# This script must be called from the AML development directory.
#
#   1) Call make_release.py to create a ./plugin.program.AML/ subdirectory.
#   2) Delete the current installed stable version of AML.
#   3) Move ./plugin.program.AML/ contents to correct location ../plugin.program.AML/
#   4) Clean ./plugin.program.AML/ directory.

# Copyright (c) 2016-2020 Wintermute0110 <wintermute0110@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.

# --- Python standard library ---
import os
import shutil
import sys

import make_release

# --- main ---------------------------------------------------------------------------------------
def main():
    print('--- Creating AML release directory ---')
    make_release.main()

    print('\n--- Deleting currently installed AML ---')
    current_dir = os.getcwd()
    addons_dir = os.path.abspath(os.path.join(current_dir, '..'))
    AML_target_dir = os.path.join(addons_dir, make_release.AML_ID)
    AML_source_dir = os.path.join(current_dir, make_release.AML_ID)
    print('Current directory is "{}"'.format(current_dir))
    print('Addons directory is  "{}"'.format(addons_dir))
    print('AML_target_dir       "{}"'.format(AML_target_dir))
    print('AML_source_dir       "{}"'.format(AML_source_dir))

    if os.path.isdir(AML_target_dir):
        print('Target dir "{}" exists'.format(AML_target_dir))
        print('Purging contents in "{}"'.format(AML_target_dir))
        shutil.rmtree(AML_target_dir)

    print('\n--- Moving AML from source to target directory ---')
    shutil.copytree(AML_source_dir, AML_target_dir)

    print('\n--- Purging AML source directory ---')
    shutil.rmtree(AML_source_dir)

if __name__ == "__main__":
    main()
    sys.exit()
