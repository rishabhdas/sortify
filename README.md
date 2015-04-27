# Sortify

Sortify is a file sorting application which sorts files based on file extensions.
This can help you clean the mess up and organize directories like 'Downloads' which contain a lot of random files and organizing them in a proper way.

Application reads file extensions from a configuration file 'sortify.conf'. This can be customized and new extensions can be added to existing categories. If no match is found, it moves the files to a 'Misc' directory.

usage: sortify.py [-h] [-s SOURCE] [-d DESTINATION] [-r]

optional arguments:
  -h, --help            show this help message and exit
  -s SOURCE, --source SOURCE
                        Source Directory
  -d DESTINATION, --destination DESTINATION
                        Destination Directory
  -r, --recursive       Sort recursively

--source - source directory which needs to be organized / sorted.
--destination - destination directory where files from source directory are
sorted. If not specified, it by default uses source directory.
--recursive - if this flag is passed, application will search the source
directory recursively.

