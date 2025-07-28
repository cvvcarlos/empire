# plugins/reload_plugin.py
def register(bot):
    async def reload_cmd(bot):
        print("[RELOAD] Reloading all plugins...")
        bot.command_registry.clear()
        bot.load_plugins()
        print("[RELOAD] Plugins reloaded!")
    bot.register_command("reload_plugins", reload_cmd)
