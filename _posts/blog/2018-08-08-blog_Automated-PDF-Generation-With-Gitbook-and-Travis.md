---
published: false
layout: post
group: blog
title:  Generate PDFs from Gitbook automatically, with Travis.CI
subtitle: Gitbook is an open-source utility that makes it easy to generate well-formatted documentation and e-books. Combining the workflow with Travis is easy too. Trying to generate a PDF automatically though, inside the Travis.CI environment had some hiccups. This is how to get around it. 
date:   2018-08-08
categories: post
type: post
tags: travis gitbook
---

### What is Gitbook?
Gitbook is an excellent opensource platform to generate awesome looking documentation and books from simple markdown files. They also have a paid version with an editor. However, the open source free version can easily be paired with Github and Travis to pretty much provide a nice workflow.  

### The Requirement
The book in question was hosted on Github as Markdowns organised into folders in the `master` branch. Travis was then configured to run a command `gitpub` that automatically generated the Gitbook, cleans it up and commits it to the `gh-pages` branch, from which the github.io page is served. However, we also needed the `master` branch to have a directly downloadable PDF version of the latest Gitbook output.  

### The Problem
Generating a PDF with Gitbook is fairly straightforward using the `gitbook pdf <gitbook-folder-location> <pdf-location>.pdf` command. However, running this command inside Travis.CI throws the following Runtime Error.

```
File "/usr/bin/ebook-convert", line 20, in <module>
    sys.exit(main())
...
...
...
RuntimeError: X server required. If you are running on a headless machine, use xvfb
```

As is obvious from the error, the error comes from the ebook-convert plugin, that is required by Gitbook for the PDF generation. However, the command `ebook-convert` needs to have prepended with `xbvf` to run in a headless environment like Travis. 

And ... 

There is no direct way to prepend the `ebook-convert` because that is getting called by Gitbook internally. Trying to change that, would mean modifying Gitbook for yourself. 


### The Solution
I found this [gold nugget](https://www.systutorials.com/241364/how-to-run-gitbook-on-a-headless-server-make-calibre-run-in-headless-server/) which didn't work for me but definitely led me to my current solution. The workaround was to 'wrap' the `ebook-convert` command so that when Gitbook calls `ebook-convert`, it is actually calling the wrapper command, that calls the actual command prepended with `xbvf`. 

Steps: 
- Create a wrapper shell script in the repository (script provided below)
- Rename the ebook-covert in your `/usr/bin` folder to ebook-convert2 (or something else!)
- Move your script to the `/usr/bin` folder as `ebook-convert`
- Allow the script to be excutable (the command will exit with an error if you don't do this)

And that's it! Enjoy your automatic PDFs

### Files


#### wrapper-script
```
#!/bin/bash
echo "Run xvfb-run /usr/bin/ebook-convert2 $@"
sudo xvfb-run /usr/bin/ebook-convert2 "$@"
```



#### .travis.yml

```
language: node_js
node_js:
  - "6"
before_install:
  - sudo apt-get install -y calibre
  - sudo apt-get install xvfb
before_script:
  - npm install gitbook-cli
  - npm install gitbook-publish@latest
  - npm install ebook-convert
  - sudo mv /usr/bin/ebook-convert /usr/bin/ebook-convert2
  - sudo cp ./ebook-wrapper.sh /usr/bin/ebook-convert
  - sudo chmod +x /usr/bin/ebook-convert
script: 
  - git config --global user.email "akshatamohanty@gmail.com"
  - git config --global user.name "Akshata"
  - gitbook pdf ./ ./published/urban-prototyping.pdf
  - git add ./published/urban-prototyping.pdf
  - git status
  - git commit -m"Published PDF" 
  - git status
  - git push "https://{USER_NAME}:${GITHUB_TOKEN}@github.com/${GITHUB_REPO}" master
  - gitpub
  - git branch
  - git remote -v
  - git push --force "https://{USER_NAME}:${GITHUB_TOKEN}@github.com/${GITHUB_REPO}" gh-pages 

```
