def register(bot):
    async def help_cmd(bot):
        cmds = bot.command_registry.keys()
        print("[HELP] Available commands:")
        for c in sorted(cmds):
            print(f" - {c}")
    bot.register_command("help", help_cmd)
