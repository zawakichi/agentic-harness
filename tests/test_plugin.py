"""Packaging acceptance checks; behavior and host integration require separate evaluation."""
import json
import os
from pathlib import Path
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PluginAcceptance(unittest.TestCase):
    def test_manifests_identify_same_plugin_and_marketplace_resolves(self):
        codex = json.loads((ROOT / '.codex-plugin/plugin.json').read_text())
        claude = json.loads((ROOT / '.claude-plugin/plugin.json').read_text())
        market = json.loads((ROOT / '.agents/plugins/marketplace.json').read_text())
        self.assertEqual(codex['name'], claude['name'])
        self.assertEqual(codex['version'], claude['version'])
        entry = next(x for x in market['plugins'] if x['name'] == codex['name'])
        self.assertEqual((ROOT / entry['source']['path']).resolve(), ROOT)
        self.assertTrue((ROOT / codex['skills'] / 'autonomous-run/SKILL.md').is_file())

    def test_hook_command_returns_session_context(self):
        hooks = json.loads((ROOT / 'hooks/hooks.json').read_text())
        cmd = hooks['hooks']['SessionStart'][0]['hooks'][0]['command']
        env = dict(os.environ, CLAUDE_PLUGIN_ROOT=str(ROOT))
        result = subprocess.run(['/bin/sh', '-c', cmd], env=env, input='{}',
                                text=True, capture_output=True, check=True, timeout=5)
        output = json.loads(result.stdout)['hookSpecificOutput']
        self.assertEqual(output['hookEventName'], 'SessionStart')
        self.assertIn('autonomous-run', output['additionalContext'])

    def test_skill_reference_targets_exist(self):
        import re
        skill = ROOT / 'skills/autonomous-run/SKILL.md'
        for path in re.findall(r'\]\((references/[^)]+)\)', skill.read_text()):
            self.assertTrue((skill.parent / path).is_file(), path)


if __name__ == '__main__':
    unittest.main()
