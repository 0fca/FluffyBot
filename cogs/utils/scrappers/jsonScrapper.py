import re


class jsonScrapper(object):

    def __init__(self, keys: [], json: str):
        self.keys = keys
        self.json_str = json
        self.result = {}
        self.spliced = []

    def get_values(self,  additional_key=0):
        """
        method scraping out the needed values out of json string
        :return: dict containing all the needed values under specified keys
        """
        self.spliced = re.split("[,:]", self.json_str)

        print(self.spliced)

        for i , element in enumerate(self.spliced):
            self.spliced[i] = element.replace('"', '').replace('{', '').replace('}', '')

        for i, item in enumerate(self.spliced):
            if item in self.keys:
                try:
                    if additional_key > 0:
                        self.result[item].append(self.spliced[i + 1] + self.spliced[i + additional_key])
                    else:
                        self.result[item].append(self.spliced[i + 1])
                except KeyError:
                    self.result[item] = list()
                    if additional_key > 0:
                        self.result[item].append(self.spliced[i + 1] + self.spliced[i + additional_key])
                    else:
                        self.result[item].append(self.spliced[i + 1])
        return self.result

    def set_keys(self, new_keys: []):
        """
        new list of key, scrapper will search for them in the json string

        :param new_keys:
        :type list
        """
        self.keys = new_keys

    def set_json(self, new_json: str):
        """
        Method for setting new json string for scraping values out of it

        :param new_json:
        :type new_json: string
        """
        self.json = new_json

    def get_dict(self):
        return self.result
