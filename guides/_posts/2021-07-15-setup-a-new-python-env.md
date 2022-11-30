---
title: Python Package Management, for the Node developer
summary: Python is cold.
date: 2021-07-15
layout: essay
tags:
  - python
---

This is going to be simple.

I started building an API in Python. And the first thing was to manage my packages - because, let's face it - installation hell is the worst kind of hell!

Here's how to do it,

- Use the command below to create a new environment. This will add a new folder in your project with `_environment_name`. Make sure to add this to `.gitignore`

```bash
python3 -m venv _environment_name_
```

- Activate this environment using,

```bash
source _environment_name_/bin/activate
```

- Now, if you want to install and freeze packages, i.e, the nodejs equivalent of `npm install package_name --save`, here's what you need

```bash
pip install package_name && pip freeze > requirements.txt
```

Might add more to this post later - but for now - adios!

Happy building!
