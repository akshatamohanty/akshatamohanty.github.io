---
layout: post
group: blog
marker: tutorial
title:  How to integrate Jasmine testing framework for Typescript
summary: Test-driven development (TDD) is a best practice for clean, robust production-grade code. However, setting up these testing frameworks can be daunting. Here are some of the lessons I learned while setting up Jasmine testing framework for Typescript
date:   2017-11-7
---

# Creating a package.json file

Use `npm init` to create the package.json file. It acts like a wizard and steps you through the entire file creation. Press enter to accept defaults (which will be in most cases). This file is what is used to configure the build process and run, build and test your application. 

<br />

# Folder Structure
This projects implements a folder structure as follows - 

Folder: `./`
  - `.config`: [Contains all the config files]
     - `karma.config.ts` : Karma Configuration File
     - `tsconfig.json`: Typscript Configuration File
  - `src`: [Containts all the source Typescript files]
  - `tests`: [Contains tests to be run on the src folder files]

<br />

# Packages to install 

Next, you'll need to install the packages required to compile and test typescript files. 
- `@types/nodes` - This is needed to allow you to script in nodejs and use keywords like require, export etc. 
- `karma-typescript` - To compile typescript files into Javascript which can be tested by Jasmine
- `karma-chrome-launcher` - To launch an instance of chrome. You have to install a launcher for each browser that you want to check against.
- `karma-jasmine-html-reporter` - This is required to display the Jasmine test results on Chrome; [Note: not karma-html-report]
- `@types/jasmine`- Required for Jasmine test to run and to get rid of errors with `describe` keyword etc
- `typescript` - Duh!
- `Jasmine Core`

<br />

# Karma Config Files 

Update the config file "files": [] property, to point to the test files as well as the imports. This is required for the karma-typescript-compiler to compile properly or it won't find the imported files, which you might be trying to check. 

If the tests are not visible, but Jasmine is, means there is problem with file paths in the karma.config file

Specify the module in the karmaTypescriptConfig options as "commonjs" or it will not accept export/import modules

<br />

# Running scripts with `package.json`

Update package.json to run 

```js
  { "test" : "karma start <karma_config_file_path>" }
``` 

Basically, this gets run whenever `npm test` is run

<br />

# Typedocs

For the docs - just the following script in `package.json` will do:

```js
  "build-docs": "typedoc --out ./docs ./src --module commonjs"
```