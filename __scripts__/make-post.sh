#!/bin/bash
RED='\033[0;31m'
NC='\033[0m' # No Color

echo Post title?
read name
name=${name:="hello-world"}
echo Choose a category [blog, project, public]
read cate
cate=${cate:="blog"}
formattedDate=$(date +"%Y-%m-%d")
filename=${cate}/_posts/${formattedDate}-${name}.md
cat > ${filename} <<EOL
---
published: false

title: ${name}
summary:
date:  ${formattedDate}
image:
credits:
tags:
 - tag1
---

### for whom is this?

### why should they care? what is the problem?

### what is the idea/solution?

### headline 1

#### Subpoint 1
#### Subpoint 2

### headline 2

#### Subpoint 1
#### Subpoint 2

### headline 3

#### Subpoint 1
#### Subpoint 2

### takeaway - make it memorable!
EOL

echo -e "Happy Writing! Your post is here: ${RED}${filename}${NC}"