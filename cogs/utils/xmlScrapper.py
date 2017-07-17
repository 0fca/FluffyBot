import re
class xmlScrapper(object):

    def __init__(self, keys: [], xml: str):
        self.keys = keys
        self.xml = xml
        self.result = {}
        self.splited = []

    def get_values(self):

        self.splited = re.split("[<>\]=\"]", self.xml)
        for i, item in enumerate(self.splited):
            if item in self.keys:
                try:
                    self.result[item].append(self.splited[i + 1].replace("\n", ''))
                except KeyError:
                    self.result[item] = list()
                    self.result[item].append(self.splited[i + 1].replace("\n", ''))
        return self.result

    def set_keys(self, new_keys: []):
        self.keys = new_keys

    def set_xml(self, new_xml):
        self.xml = new_xml

    def get_dict(self):
        return self.result
