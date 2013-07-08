echo -e "The whatchanged command is like the log command, but we'll see diffs by default as well.
These two are similar, and you'll probably end up using one far more than the other.\n"

cd clone2

echo "$ git checkout master"
git checkout master

echo "$ git pull"
git pull

echo "$ git whatchanged"
git whatchanged
