import config


async def start_bot(bot):
    await bot.start(config.token)
