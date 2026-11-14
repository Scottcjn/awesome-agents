import unittest
from pathlib import Path

from scripts.check_catalog import (
    canonical_url,
    duplicate_targets,
    extract_catalog_entries,
    heading_anchors,
    validate_repository,
)


class CatalogChecksTest(unittest.TestCase):
    def test_heading_anchors_follow_github_slug_rules(self):
        readme = "# Overview\n## Agent Tools!\n## Agent Tools!\n```md\n## Ignored\n```\n"
        self.assertEqual(
            {"overview", "agent-tools", "agent-tools-1"},
            heading_anchors(readme),
        )

    def test_catalog_parser_accepts_nested_description_links(self):
        readme = (
            "## Platforms\n"
            "- [Example](https://example.com/) - Uses [documentation](https://example.com/docs).\n"
            "## Contributing\n"
        )
        entries, errors = extract_catalog_entries(readme)
        self.assertEqual([], errors)
        self.assertEqual([(2, "Example", "https://example.com/")], entries)

    def test_catalog_parser_requires_final_period(self):
        readme = "## Platforms\n- [Example](https://example.com) - Missing punctuation\n## Contributing\n"
        entries, errors = extract_catalog_entries(readme)
        self.assertEqual(1, len(entries))
        self.assertIn("catalog description must end with a period", errors[0])

    def test_duplicate_targets_normalize_host_case_and_trailing_slash(self):
        self.assertEqual(
            "https://example.com/project",
            canonical_url("HTTPS://EXAMPLE.COM/project/"),
        )
        duplicates = duplicate_targets(
            [
                (10, "First", "https://example.com/project/"),
                (20, "Second", "https://EXAMPLE.com/project"),
            ]
        )
        self.assertIn("https://example.com/project", duplicates)
        self.assertEqual([(10, "First"), (20, "Second")], duplicates["https://example.com/project"])

    def test_repository_catalog_is_consistent(self):
        root = Path(__file__).resolve().parents[1]
        self.assertEqual([], validate_repository(root))


if __name__ == "__main__":
    unittest.main()
