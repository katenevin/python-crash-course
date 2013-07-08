echo -e "The merge command combines two branches.
The history of both branches is joined to create the current state of the target branch.
When merging, you'll bring changes from one branch into your current branch.\n"

cd clone1

echo "$ git checkout new-branch"
git checkout new-branch

echo "$ git checkout master"
git checkout master

echo "$ git merge new-branch"
git merge new-branch
