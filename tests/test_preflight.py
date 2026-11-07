import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('preflight', ROOT / 'scripts/preflight.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class TaskValidation(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / 'tasks/candidates.json').read_text())

    def test_valid(self):
        self.assertEqual(module.validate_tasks(self.data), [])

    def test_duplicate(self):
        self.data['tasks'].append(copy.deepcopy(self.data['tasks'][0]))
        self.assertTrue(module.validate_tasks(self.data))

    def test_missing_field(self):
        del self.data['tasks'][0]['owner']
        self.assertTrue(module.validate_tasks(self.data))

    def test_invalid_status(self):
        self.data['tasks'][0]['status'] = 'won'
        self.assertTrue(module.validate_tasks(self.data))

    def test_blocked_without_reason(self):
        self.data['tasks'][0]['blockers'] = []
        self.assertTrue(module.validate_tasks(self.data))

    def test_submitted_without_url(self):
        self.data['tasks'][0]['status'] = 'submitted'
        self.assertTrue(module.validate_tasks(self.data))

    def test_done_without_evidence(self):
        self.data['tasks'][0]['status'] = 'done'
        self.data['tasks'][0]['evidence'] = []
        self.assertTrue(module.validate_tasks(self.data))

if __name__ == '__main__':
    unittest.main()
