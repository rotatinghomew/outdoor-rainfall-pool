import unittest

from inspect_inputs import read_tables


class SourceRecords(unittest.TestCase):
    def test_holdout_and_older_dates_have_multiple_venues(self):
        tables = read_tables()
        older = {row['day'] for row in tables['performances'] if row['day'] < '2025-09-01'}
        holdout = {row['day'] for row in tables['performances'] if row['day'] >= '2025-09-01'}
        self.assertGreater(len(older), 8)
        self.assertGreater(len(holdout), 8)
        self.assertEqual(3, len({row['station'] for row in tables['rain']}))

    def test_claims_reference_actual_agreements_and_performances(self):
        tables = read_tables()
        performances = {row['performance']: row for row in tables['performances']}
        agreements = {row['agreement']: row for row in tables['agreements']}
        options = {row['option']: row for row in tables['policy_options']}
        for claim in tables['settlements']:
            agreement = agreements[claim['agreement']]
            self.assertEqual('active', agreement['state'])
            self.assertEqual(options[agreement['option']]['site'], performances[claim['performance']]['site'])
        source = {row['record'] for row in tables['rain'] if row['revision']=='0'}
        for revision in (row for row in tables['rain'] if row['revision']=='1'):
            self.assertIn(revision['record'], source)
