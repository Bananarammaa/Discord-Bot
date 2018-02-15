import discord
from discord.ext import commands
import random
try: # check if BeautifulSoup4 is installed
	from bs4 import BeautifulSoup
	soupAvailable = True
except:
	soupAvailable = False
import aiohttp

class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mycom(self):
        """This does stuff!"""

        #Your code will go here
        await self.bot.say("Eat shit scumbag")


    @commands.command()
    async def punch(self, user : discord.Member):
        """This punches people"""

        await self.bot.say("ONE PUNCH! And " + user.mention + " is out! ლ(ಠ益ಠლ)")
		"""@commands.command()
		async def love(self):
		case = random.randint(1,6)
		if (case == 1) await self.bot.say("I love you")
		elif (case == 2) await self.bot.say("Its okay to take breaks")
		elif (case == 3) await self.bot.say("You got a big dick")
		elif (case == 4) await self.bot.say("<3")
		else (case == 4) await self.bot.say("Dont forget to take your meds")"""
    @commands.command()
    async def dotanow(self):
        """How many players are online atm?"""

        #Your code will go here
        url = "https://steamdb.info/app/570/graphs/" #build the web adress
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            online = soupObject.find(class_='home-stats').find('li').find('strong').get_text()
            await self.bot.say(online + ' players are playing this game at the moment')
        except:
            await self.bot.say("Couldn't load amount of players. No one is playing this game anymore or there's an error.")


def setup(bot):
	if soupAvailable:
		bot.add_cog(Mycog(bot))
	else:
		raise RuntimeError("You need to run `pip3 install beautifulsoup4`")
