import ujson


class jsonScrapper(object):

    def __init__(self, keys: [], json: str):
        self.keys = keys
        self.json_str = json
        self.result = {}
        self.spliced = []

# avalible parsers
        self.indexes = {"default": 0,
                        "e9": 1,
                        "e6": 2,
                        "dp": 3,
                        "imgur": 4}

# decide which to use, and get those values
    def get_values(self, site_index="default"):
        items = ujson.decode(self.json_str)
        length = len(items)
        self.result.clear()
        if site_index in self.indexes:
            type = self.indexes[site_index]

            if type == 0:
                print("Provide and index by which you want to parse your json")
            if type == 1:
                print("e9")
                self.__e9(items, length)
            if type == 2:
                print("e6")
                self.__e6(items, length)
            if type == 3:
                print("dp")
                self.__dp(items, length)
            if type == 4:
                print("imgur")

        else:
            print("Wrong index, please provide a valid index")

        return self.result

# actual parsers
    def __e9(self, items, lenght):
        for item in items:
            for key in self.keys:
                try:
                    self.result[key].append(item[key])
                except KeyError:
                    self.result[key] = []
                    self.result[key].append(item[key])

    def __e6(self, items, lenght):
        self.__e9(items, lenght)

    def __dp(self, items, lenght):
        for item in items['search']:
            for key in self.keys:
                try:
                    if key == 'image':
                        self.result[key].append("http:" + item[key])
                    else:
                        self.result[key].append(item[key])
                except KeyError:
                    self.result[key] = []
                    if key == 'image':
                        self.result[key].append("http:" + item[key])
                    else:
                        self.result[key].append(item[key])

    def imgur(self, items, lenght):
        for item in self.items:
            for key in self.keys:
                pass

# setters
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

    def get_site_indexes(self):
        return self.indexes
