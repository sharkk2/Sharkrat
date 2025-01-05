from discord.ext import tasks, commands
import config
from core.functions.bot.status import change_status


class StatusChange(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.statuschange.start()

    @tasks.loop(seconds=20)
    async def statuschange(self):
        if not config.maintainance:
          await change_status(self.bot)     


async def setup(bot):
    global Bot 
    Bot = bot
    await bot.add_cog(StatusChange(bot))      