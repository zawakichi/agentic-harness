#!/usr/bin/env python3
"""Advertise the optional autonomous workflow without enforcing a process."""
import json

print(json.dumps({"hookSpecificOutput": {
    "hookEventName": "SessionStart",
    "additionalContext": "For autonomous engineering work, the autonomous-run skill provides optional quality, contract and verification guidance. Follow the user's instructions and host permissions."
}}))
