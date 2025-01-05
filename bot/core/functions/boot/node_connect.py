import wavelink

async def node_connect(bot):
  await wavelink.NodePool.create_node(
    bot=bot,
    host='0.0.0.0',
    port=2333,
    password='youshallnotpass'
  ) 