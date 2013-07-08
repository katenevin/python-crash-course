echo -e "The checkout command switches between branches.
When the -b option is specified, a new branch is created with the provided name based on the contents of the current branch.\n"

cd clone2

echo "$ git checkout -b new-branch"
git checkout -b new-branch

echo "$ echo \"42\" > meaning.txt
$ git add meaning.txt"

echo "42" > meaning.txt
git add meaning.txt

echo "$ git commit -am \"added meaning to life (you're welcome)\""
git commit -am "added meaning to life (you're welcome)"

echo "$ git push origin new-branch"
git push origin new-branch

echo "$ git branch --set-upstream new-branch origin/new-branch"
git branch --set-upstream new-branch origin/new-branch
