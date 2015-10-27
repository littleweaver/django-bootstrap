BOOTSTRAP_REPO="https://github.com/twbs/bootstrap.git"
if ! git ls-remote bootstrap_remote &> /dev/null ; then
	git remote add bootstrap_remote $BOOTSTRAP_REPO
fi
git fetch bootstrap_remote
git read-tree --prefix=bootstrap/static/bootstrap/ -um $1:scss/
