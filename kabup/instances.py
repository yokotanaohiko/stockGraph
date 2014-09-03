# -*- coding: utf-8 -*-

class Instances(object):

    def __init__(self):
        self.instances = set()
        pass

    def addInstance(self,instance):
        self.instances.union(instance)
