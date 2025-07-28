import os
import sys

def register(bot):
    async def restart_cmd(bot):
        print("[RESTART] Restarting bot now...")
        python = sys.executable
        os.execv(python, [python] + sys.argv)

    bot.register_command("restart", restart_cmd)
