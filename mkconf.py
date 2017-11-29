#!/usr/bin/env python
#coding: utf-8
import sys

template = open("/root/scripts/www-mal.conf").read()

sitename=sys.argv[1]
user = group = sitename.replace(".", "-")
alias = sitename[4:] if "www" in sitename else sitename

print ( template % locals())
