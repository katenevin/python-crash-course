echo -e "The stash command gives you the option to set aside changes without committing them and revert your working copy back to your latest commit.
Useful for dropping your current work to switch to another branch without leaving your current branch in a bad state.\n"

cd clone2

echo "$ echo \"84\" > meaning.txt"
echo "84" > meaning.txt

echo "$ cat meaning.txt"
cat meaning.txt

echo "$ git stash"
git stash

echo "$ cat meaning.txt"
cat meaning.txt

echo "$ git stash apply"
git stash apply

echo "$ cat meaning.txt"
cat meaning.txt
