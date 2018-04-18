#! /bin/bash

set -e

DEPLOY_REPO="https://github.com/akshatamohanty/akshatamohanty.github.io.git"

function main {
	clean
	# get_current_site
	build_site
}

function clean { 
	echo "cleaning _site folder"
	if [ -d "_site" ]; then rm -Rf _site; fi 
}

function get_current_site { 
	echo "getting latest site"
	git clone --depth 1 $DEPLOY_REPO _site 
}

function build_site { 
	echo "building site"
	bundle exec jekyll build 
	deploy
}

function deploy {
	echo "checkout master"
	git checkout master
	git checkout dev -- _site
	git add _site
	git add .
	git commit -m'new-build-deployed'
	echo "pushing master"
	git push origin master
}

main