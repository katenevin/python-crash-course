#!/bin/bash

# INTRO
# #####

# this is a simple shell script that can teach you some important shell
#   concepts

# COMMENTS
# ########

# as you can tell by now, lines that start with a hash (#) are
#   considered comments

echo 'The contents of the tutorial are embedded in this file as comments.'
echo 'View this file using `nano` or `vim` to read the tutorial.'

# BASH vs SH
############

# this tutorial will teach you the basics of bash scripting

# most systems will come with a bash-compatible shell

# there is a simpler shell, called `sh`, that has more limited
#   features than `bash`. If you're writing a script that needs
#   to run universally, you may want to write it for `sh`. On
#   Ubuntu, `sh` is provided by a program called `dash`
# for more information:
#   http://www.gnu.org/software/bash/manual/bashref.html#Major-Differences-From-The-Bourne-Shell

# another popular shell is the Z-shell. This is what I use personally.
# for more information:
#   http://www.zsh.org/  
#   http://en.wikipedia.org/wiki/Z_shell

# SHEBANG 
# #######

# you may have noticed a special comment at the top of this and other files
# this is called a `shebang` line, since it starts with a hash character
#   followed by an exclamation point (called a `bang')

# shebang lines identify how a script can be run
# a plain-text file might be a bash script, a Python script, a Ruby script, &c.
# the shebang line, which must be the first line in the file
#   provides the exact path of the program which should run the script

# in this case, it's a bash script, so the shebang line points to /bin/bash

# ECHO
# ####

# the most basic shell script just prints out `hello world'

# to print to the screen, use `echo'
echo hello world
echo 'hello world'
echo "hello world"

# you can use any command in a shell script that you can use 
#   straight from the command line. The only difference will be
#   the state of the environment (e.g., $PATH may be different)

# QUOTES
# ######

# you will notice my use of quotes in the above
# in the case of `echo`, the arguments do not need to be quoted; however,
#   I can optionally quote them

# there are many cases in which quotes are not optional. For example,
#   if I want to move or copy a file that has spaces in the name:

# $ mv San Antonio Texas

# the shell is not able to determine which is the source and which
#   is the destination. Naively it thinks I want to move 
#   a file called `San' and a file called `Antonio' into a directory
#   called `Texas'

# By quoting these, I make things clearer:

# $ mv 'San Antonio' Texas

# in these cases, single quotes and double quotes are identical.
# they different in whether or not they `interpolate' variables

# to assign to a variable in shell, just type
source='San Antonio'
dest='Texas'

# note that there is NO space surrounding the equals sign

# now, I can use that variable. To use a variable, prepend it with a 
#   dollar-sign ($)

# $ mv $source $dest

# however, variables are substituted before the command is run. This means
#   that variables are substituted on the text, then the text is passed
#   to the shell to run.

# $ mv $source $dest
# becomes
# $ mv San Antonio Texas
# which is run

# I will run into the same problem I had before! I need to quote
#   the arguments to make things clearer. If I use single quotes, then
#   the shell will interpret the contents WITHOUT substitution.

# Variables in single-quotes are NOT substituted.
# Variables in double-quotes are substituted

# therefore, I want to do this:

# $ mv "$source" "$dest"

# PIPES & REDIRECTION
# ###################

# the real power of the shell is pipes and indirection

# this means that we can take the output of one of our programs and feed
#   it into the input of another program. This functionality is what
#   underlies the Unix mantra of "small programs that do one thing well."

# to see this in action, let's take the `find` command and pipe it to
#   the `grep` command

find .. -type f -iname '*.xml' | grep -i texas

# the `pipe' (|) operator takes the output of the command on the left
#   and passes it as the input to the command on the right

# there are better ways to accomplish the above using `find` but this
#   is one way to find all the .xml files from the parent directory
#   and up, and then filter that to filenames that have `Texas' in them

# for the purpose of this tutorial, there should just be the `info.xml`
#   in the `interacting-with-files` puzzle

# let's assign the results of the above command to a variable, then
#   check it. We'll use quotes in case the output has spaces

file="$( find .. -type f -iname '*.xml' | grep -i texas )"
if [[ $file == '../interacting-with-files/how-big-is-it/Texas/Houston/info.xml' ]]; then
	echo 'The file was right where we expected!'
else
	echo 'Weird; the file was not where we expected it to be.'
fi

# note that the above also shows the use of the Bash-ism, $()
# in the above, we assigned the variable `file' to the output of the 
#   command sequence in $()
# this is used for command substitution. In raw shell, the backtick operators `
#   accomplish the same purpose

# pipes work on the standard output and the standard input of programs

# there is also a standard error stream, but you may not run into it often

# in addition to being able to chain commands, you can also send the 
#   output of a command to a file, or use a file as the input to a command
# this is called `redirection'

ls -1 > contents

# after you run this script, you should see a new file in the directory
#   called `contents' that contains the contents of this directory

# in the above command, we ran `ls` then we sent the results of this
#   to the file contents instead of to the screen

# if we had wanted to APPEND to the file `contents` instead of writing anew
#   we would have written

ls -1 >> contents

# if we wanted to take the contents of this file then pass it to another
#   program, we could:

head < contents
