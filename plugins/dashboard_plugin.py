# plugins/dashboard_plugin.py
import json
import logging
import os
from datetime import datetime

async def dashboard_cmd(bot):
    DASHBOARD_FILE = os.path.abspath("empire_dashboard.json")
    STATE_FILE = os.path.abspath("empire_state.json")
    dashboard = {
        "last_sync_time": getattr(bot, "last_sync_time", None),
        "pending_command_count": bot.command_queue.qsize() if hasattr(bot, "command_queue") else "n/a",
        "logging_level": logging.getLevelName(logging.getLogger("EmpireSyncBot").level),
        "applied_patches": [],
        "last_patch": None,
        "bot_version": getattr(bot, "version", None) or "n/a",
        "generated_at": datetime.now().isoformat()
    }
    try:
        if os.path.exists(STATE_FILE):
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                state = json.load(f)
            dashboard["applied_patches"] = state.get("applied_patches", [])
            dashboard["last_patch"] = state.get("last_patch_applied", None)
    except Exception as e:
        dashboard["error"] = str(e)
    with open(DASHBOARD_FILE, "w", encoding="utf-8") as f:
        json.dump(dashboard, f, indent=2)
    print(f"[DASHBOARD] Empire dashboard written at {dashboard['generated_at']}")

def register(bot):
    bot.register_command("dashboard", dashboard_cmd)
