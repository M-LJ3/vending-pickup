"""A tiny vending machine pickup line writer.

The program drops one funny, vending-machine-flavoured pickup
line into /output/entry.txt for the contest.
"""

from pathlib import Path

SNACK_PATH = Path("/output/entry.txt")


def vending_flirt():
    """Return one funny vending machine pickup line."""
    return (
        "Are you a vending machine? Because I keep putting coins in "
        "and all I get back is a crush on you."
    )


def check_snack_saved(expected):
    """Make sure the saved line is still the one we intended."""
    stored = SNACK_PATH.read_text(encoding="utf-8")
    assert stored == expected


def main():
    line = vending_flirt()
    SNACK_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Drop the line in exactly as written, no newline at the end.
    SNACK_PATH.write_text(line, encoding="utf-8")
    # Confirm what landed in the file matches the pickup line.
    check_snack_saved(line)


if __name__ == "__main__":
    main()
