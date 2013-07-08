echo -e "The config command gets and sets information for use by the git suite about your environment.
Use the --global flag to set configuration system wide.\n"

cd clone1

echo "$ git config user.name \"Test User\""
git config user.name "Test User"
echo "$ git config user.name"
git config user.name

echo "$ git config user.email \"testuser@example.com\""
git config user.email "testuser@example.com"
echo "$ git config user.email"
git config user.email
