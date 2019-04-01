---
layout: post
group: blog
title:  Accessing Jupyter Notebook running on a Google Compute Instance
subtitle: Lorem ipsum
date:   2018-08-22
categories: post
type: post
tags: gcloud jupyter
---

### To acces Jupyter Notebook running in GCloud Instance
- Make the compute instance static from `External IP Addresses` in the VPC Network menu
- Add a Firewall rule for all instances
 -  0.0.0.0/0 for Source IP ranges and tcp:<port-number> for Specified protocols and ports where <port-number> is the number you used above.
- Hit create
Running jupyter-notebook --port=<specified-port>
