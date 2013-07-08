echo -e "The branch command allows you to list, add, delete, and rename branches (among other things).
You'll most likely be using checkout -b in your daily work.\n"

cd clone2

echo "$ git branch nwe-branch"
git branch nwe-branch

echo "$ git branch"
git branch

echo "$ git branch -d nwe-branch"
git branch -d nwe-branch

echo "$ git branch"
git branch
