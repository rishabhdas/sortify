#!/usr/bin/python

# Rishabh Das <rishabh5290@gmail.com>
#
# This program is a free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the license, or(at your option) any
# later version. See http://www.gnu.org/copyleft/gpl.html for the full text of
# the license.

import utils
import os
from argparse import ArgumentParser


def main():
    """
        This is the main function which calls utils, takes in user input and
        sorts the files in the destination directory.
    """
    # Create arguments
    parser = ArgumentParser(description='Get user input')
    parser.add_argument('-s', '--source', help='Source Directory')
    parser.add_argument('-d', '--destination', help='Destination Directory')
    parser.add_argument('-r', '--recursive', action='store_true',
                        help='Sort recursively')
    args = parser.parse_args()
    if args.destination is None:
        args.destination = args.source
    sortify = utils.Sortify()
    # Get a list of files from the source directory.
    files_to_sort = sortify.list_files(args.source, args.recursive)
    # Create directories in destination directory for sorting files.
    destination_dir = os.path.join(args.destination, 'sortify')
    for item in sortify.filetypes.keys():
        sortify.create_directory(destination_dir, item)
    # Finally sort files
    sortify.sort_files(files_to_sort, destination_dir)

if __name__ == '__main__':
    main()
