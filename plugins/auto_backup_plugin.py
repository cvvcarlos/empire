import asyncio
import os
import shutil
from datetime import datetime

def register(bot):
    async def auto_backup_loop():
        while True:
            now = datetime.now().strftime("%Y%m%d_%H%M%S")
            src_state = os.path.abspath("empire_state.json")
            src_dashboard = os.path.abspath("empire_dashboard.json")
            backup_dir = os.path.abspath("empire_state_backups")
            os.makedirs(backup_dir, exist_ok=True)
            if os.path.exists(src_state):
                shutil.copy2(src_state, os.path.join(backup_dir, f"empire_state_{now}.json"))
            if os.path.exists(src_dashboard):
                shutil.copy2(src_dashboard, os.path.join(backup_dir, f"empire_dashboard_{now}.json"))
            print(f"[AUTO BACKUP] Backup done at {now}")
            await asyncio.sleep(3600)  # wait one hour

    async def start_auto_backup(bot):
        bot.loop.create_task(auto_backup_loop())

    bot.register_command("start_auto_backup", start_auto_backup)
