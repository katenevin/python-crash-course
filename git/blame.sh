echo -e "The blame command give you historical information about your repository including commit hashes and author information.
SVN has an interesting command called praise that is simply an alias to it's blame.\n"

cd clone2

echo "$ git blame hello.txt"
git blame hello.txt

echo "$ git blame meaning.txt"
git blame meaning.txt
