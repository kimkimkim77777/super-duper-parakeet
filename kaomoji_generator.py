#!/usr/bin/env python3
"""Simple random kaomoji generator."""
import argparse
import random

KAOMOJIS = [
    "(・`ω´・)",
    "ヽ(•‿•)ノ",
    "(◕‿◕✿)",
    "｡^‿^｡",
    "ヽ(´ー` )┌",
    "(╯°□°）╯︵ ┻━┻",
    "(￣o￣) . z Z",
    "¯\\_(ツ)_/¯",
    "(* ^ ω ^)",
    "(>_<)"
]


def generate(number: int = 1) -> str:
    """Return space-separated kaomojis."""
    return " ".join(random.choice(KAOMOJIS) for _ in range(number))


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate random kaomojis")
    parser.add_argument(
        "-n",
        "--number",
        type=int,
        default=1,
        help="Number of kaomojis to generate (default: 1)",
    )
    args = parser.parse_args()
    print(generate(args.number))


if __name__ == "__main__":
    main()

