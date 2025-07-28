# plugins/healthcheck_plugin.py
import logging
from datetime import datetime

async def healthcheck_cmd(bot):
    logger = logging.getLogger("EmpireSyncBot")
    info = f'[HEALTHCHECK] {datetime.now()} - Command Queue Size: {bot.command_queue.qsize()}'
    print(info)
    logger.info(info)

def register(bot):
    bot.register_command("healthcheck", healthcheck_cmd)
