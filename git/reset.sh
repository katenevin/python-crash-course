echo -e "The reset command is your eraser.
It allows you to bring your current working copy to the state of some other commit (often HEAD).
Use the --hard option to reset your actual working copy as well, not just the git index.
This is very useful if you've done something bad and want to forget it ever happened.\n"

cd clone2

echo "$ cat meaning.txt"
cat meaning.txt

echo -e "\nOh, no!\n"

echo "$ git reset"
git reset

echo "$ cat meaning.txt"
cat meaning.txt

echo "$ git status"
git status

echo "$ git reset --hard"
git reset --hard

echo "$ cat meaning.txt"
cat meaning.txt

echo "$ git status"
git status
