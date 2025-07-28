# plugins/backup_plugin.py
import os
import shutil
from datetime import datetime

async def backup_cmd(bot):
    state_file = os.path.abspath("empire_state.json")
    dashboard_file = os.path.abspath("empire_dashboard.json")
    backup_dir = os.path.abspath("empire_state_backups")
    os.makedirs(backup_dir, exist_ok=True)
    now = datetime.now().strftime('%Y%m%d_%H%M%S')
    if os.path.exists(state_file):
        shutil.copy2(state_file, os.path.join(backup_dir, f"empire_state_{now}.json"))
    if os.path.exists(dashboard_file):
        shutil.copy2(dashboard_file, os.path.join(backup_dir, f"empire_dashboard_{now}.json"))
    print(f"[BACKUP] Empire state and dashboard backed up at {now}.")

def register(bot):
    bot.register_command("backup", backup_cmd)
