# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 07:00:05 2016

@author: nathan
"""

import tarfile
import os
os.chdir("..")
tfile = tarfile.open("enron_mail_20150507.tgz", "r:gz")
tfile.extractall(".")