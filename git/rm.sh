echo -e "The rm command removes a file from your git repository.\n"

cd clone1

echo "$ git rm goodbye.txt"
git rm goodbye.txt

echo "$ git commit -am \"removed goodbye.txt (with meaning, life goes on)\""
git commit -am "removed goodbye.txt (with meaning, life goes on)"

echo "$ git push origin master"
git push origin master
