---
published: false
title: Building API products, quick and dirty.
description: It seemed intimidating but was surprisingly easy!
date: 2018-08-22
layout: post
---

### New Flask Project on Gcloud

- In GoDaddy, go to the DNS Management page
- Add an ANAME entry with host as the subdomain name and pointing to the compute instance IP

- Login to your instance using `gcloud compute ssh <instance-name>
- Go to the nginx sites config file: add the server_name <subdomain.domain.extension> entry into the file
- Restart nginx
- The site will be available on the subdomain.domain.ext URL
- Use certbot: `sudo certbot --nginx` with redirect option to add https to your website
- Create a .git folder with a post-recieve hook in the /home/git folder
- Make sure all the required folders are owned by the user who'll make the push
- `sudo chown -R user:user` and `ls -l` are helpful commands
