echo -e "The commit command writes all of your changes (see: status) to your branch.
Commits make up the history of a git repository.
The current state of a branch is a sum of all of the commits that have been made.\n"

cd clone1

echo "$ git commit -am \"added hello.txt\""
git commit -am "added hello.txt"
echo "$ git status"
git status
