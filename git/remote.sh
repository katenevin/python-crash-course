echo -e "The remote command allows you to manage your remote repository configuration.
This lets your local repository know about new remote resources and manages those resources (add, remove, rename, etc.).\n"

echo "$ cd ../
$ mkdir repo
$ cd repo
$ git init --bare"

mkdir repo
cd repo
git init --bare

echo "$ cd ../clone1
$ git remote add origin ../repo"
cd ../clone1
git remote add origin ../repo
