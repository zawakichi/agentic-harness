#!/usr/bin/env python3
"""Supply lightweight context; the skill provides the detailed workflow."""
import json

print(json.dumps({"hookSpecificOutput": {
    "hookEventName": "SessionStart",
    "additionalContext": "For tasks requesting autonomous execution, use the autonomous-run skill if available. Define acceptance criteria, verify results, and report blockers honestly. Respect the user's instructions and the environment's permissions."
}}))
