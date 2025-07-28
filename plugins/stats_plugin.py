import json
import os

def register(bot):
    async def stats_cmd(bot):
        state_file = os.path.abspath("empire_state.json")
        if not os.path.exists(state_file):
            print("[STATS] No empire state found.")
            return
        try:
            with open(state_file, "r", encoding="utf-8") as f:
                state = json.load(f)
            patches = state.get("applied_patches", [])
            print(f"[STATS] Patches applied: {len(patches)}")
            print(f"[STATS] Last patch: {state.get('last_patch_applied', 'N/A')}")
        except Exception as e:
            print(f"[STATS] Error reading state: {e}")

    bot.register_command("stats", stats_cmd)
