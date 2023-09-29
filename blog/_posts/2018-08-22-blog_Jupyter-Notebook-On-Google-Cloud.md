---
title: Publish your data findings as a website.
description: Use Jupyter Notebooks to directly launch your findings as an interactive website.
date: 2018-08-22
layout: post
---

### To acces Jupyter Notebook running in GCloud Instance

- Make the compute instance static from `External IP Addresses` in the VPC Network menu
- Add a Firewall rule for all instances
- 0.0.0.0/0 for Source IP ranges and tcp:<port-number> for Specified protocols and ports where <port-number> is the number you used above.
- Hit create
  Running jupyter-notebook --port=<specified-port>
