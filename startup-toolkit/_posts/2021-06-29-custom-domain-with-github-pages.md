---
published: false
title: "DNS Detangling: Setting up a custom domain for Github pages"
description: Geeky excuse to mask good old domain squatting.
date: 2021-06-29
tags:
  - tag1
published: false
---

Buying domains is one of my guilty pleasures. I recently bought a new one to host this website. And here's what I learned while trying to setup it up.

This website, is hosted for free on [Github Pages](https://pages.github.com/). It is a really cool feature, that allows you to host static websites for free, directly from your repo. But, as with all dreams come true, the default domain that it points to is `<user>.github.io` which is not very user friendly. To correct that, Github pages does offer the ability to re-point this to your own custom domain.

Here's how to do it,

- Setup a `CNAME` entry in your Github repository with your custom domain. For eg, if you visit my repository for this website on Github, you'll notice a [CNAME file](https://github.com/akshatamohanty/akshatamohanty.github.io/blob/master/CNAME) with a domain entry. You can either create this manually or by using the Github UI at `Settings > Pages` page

- Now, we need to configure the DNS records on our hosting platform. I bought my domain using NameCheap - so I followed their guideliness to add A and CNAME records. I wanted `iamaatoh.com` to point directly to my website, not a subdomain. So I followed instructions to get the apex domain to point to the Github page. To do this,

  - Add A records to point to Github servers
  - Add CNAME record to point `www` host to my Github `<user>.github.io` path

- To test, I used the `dig` command and the Github UI. After a while, my website showed up here - right where you are reading this blog post.

### So, what's happening under the hood?

-- add diagram --
what is an apex domain
what does the github workflow look like? what's happening?
how does the dns resolve based on different records

### What do these records mean?

aname, cname records
DNS navigation - not sure what means what

### What is the `dig` command?

### setting up domains - https

https://letsencrypt.org/how-it-works/
https://docs.netlify.com/domains-https/https-ssl/
https://docs.netlify.com/domains-https/troubleshooting-tips/#certificates-and-https

```bash
akshata.mohanty@ASRHQV112  ~  dig www.iamaatoh.com +noall +answer
```

```bash
DiG 9.10.6 <<>> www.iamaatoh.com +noall +answer
;; global options: +cmd
www.iamaatoh.com.	1799	IN	CNAME	akshatamohanty.github.io.
akshatamohanty.github.io. 3599	IN	A	185.199.108.153
akshatamohanty.github.io. 3599	IN	A	185.199.109.153
akshatamohanty.github.io. 3599	IN	A	185.199.110.153
akshatamohanty.github.io. 3599	IN	A	185.199.111.153
```

#### Resources

- https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site#configuring-an-apex-domain
- https://kinsta.com/knowledgebase/namecheap-add-a-record/
- https://ap.www.namecheap.com/Domains/DomainControlPanel/iamaatoh.com/advancedns
- https://support.dnsimple.com/articles/differences-between-a-cname-alias-url/
- https://support.dnsimple.com/articles/differences-between-a-cname-alias-url/#understanding-the-differences
  https://www.netmeister.org/blog/dns-rrs.html
