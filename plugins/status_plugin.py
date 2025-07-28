# plugins/status_plugin.py
import logging
import json
import os
from datetime import datetime

async def status_cmd(bot):
    logger = logging.getLogger("EmpireSyncBot")
    now = datetime.now().isoformat()
    queue_size = bot.command_queue.qsize() if hasattr(bot, "command_queue") else "n/a"
    STATE_FILE = os.path.abspath("empire_state.json")
    state = {}
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                state = json.load(f)
        except Exception:
            pass
    patches = state.get("applied_patches", [])
    last_patch = state.get("last_patch_applied", {})
    summary = (
        f"[STATUS] {now}\n"
        f"Queue: {queue_size}\n"
        f"Log Level: {logging.getLevelName(logger.level)}\n"
        f"Patches Applied: {len(patches)}\n"
        f"Last Patch: {last_patch.get('file','n/a')} at {last_patch.get('time','n/a')}\n"
    )
    print(summary)
    logger.info(summary)

def register(bot):
    bot.register_command("status", status_cmd)
