import collections
import math
import xml.etree.cElementTree as ETree

import requests
from discord.ext import commands

from cogs import utils


class AnimeEntry(object):
    def __init__(self, id_number, title, english, episodes, score, synopsis, image):
        self.id = id_number
        self.title = title
        self.english = english
        self.episodes = episodes
        self.score = score
        self.synopsis = synopsis
        self.image_link = image


class MangaEntry(object):
    def __init__(self, id_number, title, english, episodes, score, synopsis, image, chapters, volume):
        self.id = id_number
        self.title = title
        self.english = english
        self.episodes = episodes
        self.score = score
        self.synopsis = synopsis
        self.image_link = image
        self.chapters = chapters
        self.volume = volume


class MalHandler(object):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.respond = ''

        self.cache = collections.OrderedDict()
        self.cache_size = 5

        self.content = None
        self.entries = []

        self.showed = False

    @commands.command(pass_context=True)
    async def searchMal(self, ctx):
        search_type = ctx.message.content[12:17].lower()
        search_query = ctx.message.content[18:]

        if search_query in self.cache:
            self.__print_content()
        else:
            if search_type == 'anime':
                self.__req_search(search_query, 0)
                self.__cache_req(search_query)

            elif search_type == 'manga':
                self.__req_search(search_query, 1)
                self.__cache_req(search_query)


    def __cache_req(self, search_query: str):
        if len(self.cache) > self.cache_size:
            self.cache.popitem(last=False)
            self.cache[search_query] = self.entries
        else:
            self.cache[search_query] = self.entries

    def __req_search(self, query, type_number: int):
        req_mess = utils.ml_search_link + utils.ml_type[type_number] + utils.ml_suffix + query
        self.respond = requests.get(req_mess, auth=(utils.ml_account[0], utils.ml_account[1])).text
        self.__parse_content(self.respond, type_number)

    def __parse_content(self, respond, entry_type):
        self.content = ETree.fromstring(respond)
        self.entries.clear()
        if entry_type == 0:
            for entity in self.content:
                self.entries.append(
                    AnimeEntry(
                        id_number=entity.find('id').text,
                        title=entity.find('title').text,
                        english=entity.find('english').text,
                        episodes=entity.find('episodes').text,
                        score=entity.find('score').text,
                        synopsis=entity.find('synopsis').text,
                        image=entity.find('image'),
                    )
                )
        else:
            for entity in self.content:
                self.entries.append(
                    MangaEntry(
                        id_number=entity.find('id').text,
                        title=entity.find('title').text,
                        english=entity.find('english').text,
                        episodes=entity.find('episodes').text,
                        score=entity.find('score').text,
                        synopsis=entity.find('synopsis').text,
                        image=entity.find('image'),
                        chapters=entity.find('chapters'),
                        volume=entity.find('volume')
                    )
                )

    def __print_content(self):

        # first, show them the titles, just 5 at the time, leave the rest for the next page. There's no need to spam
        # then let them choose the number: i.e 1. FMA, 2. FMA:B
        # //selectShow 1
        # print the result of entries[1]
        pass

    def __count_pages(self, entries):
        if entries > 1:
            pages = entries / 5 if math.gcd(entries, 5) == 0 else math.floor(entries / 5) + 1
        else:
            pages = 1
        return pages


def setup(bot):
    print("added Mal module")
    bot.add_cog(MalHandler(bot))

