#!/usr/bin/python

# Rishabh Das <rishabh5290@gmail.com>
#
# This program is a free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the license, or(at your option) any
# later version. See http://www.gnu.org/copyleft/gpl.html for the full text of
# the license.


import os
import shutil
import ConfigParser


class Sortify:

    """
        Sortify class contains function definitions.
        When an object is created, config file is parsed and filetypes variable
        is set.
        Functions:
            create_directory - create categroized directories in destination
            list_files - returns a list of files in source directory
            sort_files - contains main logic of sorting files
    """

    def __init__(self):
        """
            Initialize the class by reading the configuration file and set
            required variables which will then be consumed by other functions
        """
        # Read configuration file and store values
        config = ConfigParser.ConfigParser()
        config.read('sortify.conf')
        self.document = [x.strip() for x in config.get('filetype',
                                                       'document').split(',')]
        self.archive = [x.strip() for x in config.get('filetype',
                                                      'archive').split(',')]
        self.music = [x.strip() for x in config.get('filetype',
                                                    'music').split(',')]
        self.video = [x.strip() for x in config.get('filetype',
                                                    'video').split(',')]
        self.image = [x.strip() for x in config.get('filetype',
                                                    'image').split(',')]
        self.filetypes = {'Documents': self.document,
                          'Archive': self.archive,
                          'Music': self.music,
                          'Videos': self.video,
                          'Images': self.image,
                          'Misc': []}

    def create_directory(self, base_dir, new_dir):
        """
            Check if 'sorting' directories exist in the specified location. If
            not, create the directories.
        """
        # Check if the base_dir exists. If not, create base_dir
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)
        # Change to base_dir
        os.chdir(base_dir)
        # create categories (directories) in the base_dir
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)

    def sort_files(self, files_to_sort, target_dir):
        """
            Contains the main logic of sorting files based on their extension
        """
        for fpath in files_to_sort:
            # Get file extension and file name
            extension = ''
            extension = os.path.splitext(fpath)[1].lower()
            category = ''
            fname = fpath.split('/')[-1]
            # Check which file type the extension belongs to
            # If none, set category to Misc
            for ftype, ext in self.filetypes.iteritems():
                if extension in ext:
                    category = ftype
            if category is '':
                category = 'Misc'
            # Determine destination and move file to the new location
            destination = os.path.join(target_dir, category, fname)
            shutil.move(fpath, destination)

    def list_files(self, sort_dir, recursive):
        """
            Return a list of files which have to be sorted. If recursive is set
            to true, sortDir is searched recursively and list of all the files
            are returned. If recursive is set to false, it returns only the
            first level file list.
        """
        files_to_sort = []
        if recursive:
            for root_dir, sub_dir, files in os.walk(sort_dir):
                for elem in files:
                    fname = os.path.join(root_dir, elem)
                    files_to_sort.append(fname)
        else:
            for item in os.listdir(sort_dir):
                if os.path.isfile(os.path.join(sort_dir, item)):
                    files_to_sort.append(os.path.join(sort_dir, item))
        return files_to_sort
