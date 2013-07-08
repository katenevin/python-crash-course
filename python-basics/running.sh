#!/bin/bash

# OVERVIEW
# ########

# we can interact with python in three ways:
# 1. the interactive console: `python`
# 2. running a module directly: `python -m module`
# 3. running a sequence of commands directly: `python -c`
# 4. running a script: `./script.py` or `python script.py`

# INTERACTIVE CONSOLE ("REPL")
# ############################

# we can start the python interactive console, or "REPL" (read-eval-print-loop,)
#   by just typing `python` at the command line

# $ python

# this will give us an interactive session that will run python commands
#   sequentially:

# $ python
# >>> x = 10
# >>> print x
# 10
# >>> y = 20
# >>> print x + y
# 30

# RUNNING A MODULE DIRECTLY
# #########################

# python modules can be run directly as scripts with `python -m module`

# there are some common modules that you might want to run in this way:
#   timeit and SimpleHTTPServer

# timeit will run a sequence of commands and time how long it takes
#   for them to execute. You can use this for simple benchmarking

# see which way of concatenating short strings is faster
python -m timeit '"abc" "def" "ghi"' # implicit literal concatenation
python -m timeit '"abc" + "def" + "ghi"' 
python -m timeit '"".join(["abc", "def", "ghi"])'

# also, sometimes you might want to a quick&dirty HTTP server
#   to serve the files in some directory

# $ python -m SimpleHTTPServer 8080
# $ firefox localhost:8080

# RUNNING A COMMAND DIRECTLY
# ##########################

# sometimes you might want to use a Python to run a single, simple sequence
#   of commands. You can do this with `python -c`
# you can separate commands with a semicolon (;) but there are limits
#   to what you can stick into a single line

python -c 'from sys import argv; sum(map(int,argv[1:]))' 10 20 30
python -c 'print 10 + 20'
python -c 'from datetime import datetime; print datetime.now()'

# RUNNING A SCRIPT
# ################

# there are two ways to run a Python script:
#  $ python script.py
#  $ ./script.py

# the first way asks a specific python interpreter (whatever is in your
#    $PATH) to run a script named `script.py'

# the second way relies on the file containing a shebang line which
#   specifies the python interpreter to use to run the script
# the file must have its execute permission big set which you can do with:

# $ chmod +x script.py

# note that the shebang line of these Python scripts is:

#!/usr/bin/env python

# you might have expected it to be:

#!/usr/bin/python

# it turns out that Python can be installed in different places, and different
#   Linux distributions don't agree where to put it: /bin, /usr/bin, /opt
# to get around this and to ensure that your script is portable,
#   we use the standard program `env` which is always located at /usr/bin/env
# env will then find and run python for us
