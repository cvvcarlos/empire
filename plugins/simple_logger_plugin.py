import logging

def register(bot):
    async def debug_on(bot):
        logging.getLogger("EmpireSyncBot").setLevel(logging.DEBUG)
        print("[LOGGING] Debug logging ENABLED")

    async def debug_off(bot):
        logging.getLogger("EmpireSyncBot").setLevel(logging.INFO)
        print("[LOGGING] Debug logging DISABLED")

    bot.register_command("debug on", debug_on)
    bot.register_command("debug off", debug_off)
