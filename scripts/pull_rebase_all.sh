for i in 'mysql' 'scripts' 'bpy'; do
cd $i;
echo `pwd`;
git update-index -q --ignore-submodules --refresh;
b_stash=0
# Disallow unstaged changes in the working tree
if ! git diff-files --quiet --ignore-submodules --
then
  b_stash=1
fi;
# Disallow uncommitted changes in the index
if ! git diff-index --cached --quiet HEAD --ignore-submodules --
then
  b_stash=1
fi;

if [ $b_stash = 1 ]
then
  git stash;
fi;

git pull --rebase;

if [ $b_stash = 1 ]
then
  git stash pop;
fi;

cd ..;
done