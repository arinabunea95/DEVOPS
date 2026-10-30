import unittest

from AI_python_project import validate_deployment


class ValidateDeploymentTests(unittest.TestCase):
    def test_accepts_valid_staging_configuration(self):
        self.assertEqual(validate_deployment("staging", 8080, False), [])

    def test_rejects_invalid_port(self):
        errors = validate_deployment("development", 70000, False)
        self.assertIn("Port must be between 1 and 65535.", errors)

    def test_rejects_debug_mode_in_production(self):
        errors = validate_deployment("production", 443, True)
        self.assertIn("Debug mode must be disabled in production.", errors)

    def test_rejects_unknown_environment(self):
        errors = validate_deployment("test", 8080, False)
        self.assertIn(
            "Environment must be development, staging, or production.", errors
        )


if __name__ == "__main__":
    unittest.main()