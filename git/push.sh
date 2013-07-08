echo -e "The push command sends your changes to the remote.
This is how you actually get your updates out to the world.
Your branch must be up to date with the remote to push, and your changes are pushed in the form of commits (i.e. files not tracked will not be pushed, all changes must be committed before pushing, etc.).\n"

cd clone1

echo "$ echo \"goodbye, cruel world!\" > goodbye.txt"
echo "goodbye, cruel world!" > goodbye.txt

echo "$ git add goodbye.txt"
git add goodbye.txt

echo "$ git commit -am \"added goodbye.txt\""
git commit -am "added goodbye.txt"

echo "$ git push origin master"
git push origin master
