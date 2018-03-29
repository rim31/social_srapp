#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys
import re

class Useur(object):

    def __init__(self):
        self._online="non"

    def _get_online(self):
        print "Récupération du nombre de online"
        return self._online

    def _set_online(self, status):
        print "Changement du nombre de online"
        try:

            self._online  =  status
        except Exception as e:
            raise

    online=property(_get_online, _set_online)

#======================MAIN=========================
if len(sys.argv) == 2:
    testUser = Useur()
    print(testUser.online)
    testUser._set_online("oui")
    print(testUser.online)
else:
    print "please enter : hostingparty OR account_id OR account_handle OR account_url OR an Array"
