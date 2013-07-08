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

# RUNNING 

python -c
python running.py
./running.py (/usr/bin/env shebang)
