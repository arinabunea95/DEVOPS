"""Check basic deployment settings before a release."""

import argparse


def validate_deployment(environment: str, port: int, debug: bool) -> list[str]:
    """Return validation errors for a deployment configuration."""
    errors = []
    if environment not in {"development", "staging", "production"}:
        errors.append("Environment must be development, staging, or production.")
    if not 1 <= port <= 65535:
        errors.append("Port must be between 1 and 65535.")
    if environment == "production" and debug:
        errors.append("Debug mode must be disabled in production.")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate deployment settings.")
    parser.add_argument(
        "--environment",
        choices=("development", "staging", "production"),
        default="development",
    )
    parser.add_argument("--port", type=int, default=8080)
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()

    errors = validate_deployment(args.environment, args.port, args.debug)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(
        f"Deployment settings are valid: environment={args.environment}, "
        f"port={args.port}, debug={args.debug}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())