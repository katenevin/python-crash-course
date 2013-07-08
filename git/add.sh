echo -e "The add command adds a file to your repository. A file is not "tracked" by git unless it is explicitly added.\n"

cd clone1

echo "$ echo \"hello, world\" > hello.txt"
echo "hello, world" > hello.txt
echo "$ git add hello.txt"
git add hello.txt
