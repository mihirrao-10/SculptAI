"""Example script for calling Herdora's Qwen VL endpoint with a motivational prompt."""

import argparse
import os
import sys
from typing import Optional

from openai import OpenAI

PROMPT = (
    "Describe this person's body picture from a fitness perspective. "
    "Talk in a David Goggins style. Give an estimated body fat percentage "
    "and workout tips. Most importantly, talk in a way that Goggins would do "
    "to incite motivation."
)


def create_client(api_key: Optional[str] = None) -> OpenAI:
    """Create an OpenAI-compatible client for the Herdora endpoint."""
    key = api_key or os.getenv("HERDORA_API_KEY")
    if not key:
        raise RuntimeError(
            "HERDORA_API_KEY is required. Set the environment variable or pass it explicitly."
        )

    return OpenAI(base_url="https://pygmalion.herdora.com/v1", api_key=key)


def generate_caption(image_url: str, client: Optional[OpenAI] = None) -> str:
    """Send the motivational fitness prompt for the provided image URL."""
    client = client or create_client()
    response = client.chat.completions.create(
        model="Qwen/Qwen3-VL-235B-A22B-Instruct",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": PROMPT},
                    {"type": "image_url", "image_url": {"url": image_url}},
                ],
            }
        ],
    )
    return response.choices[0].message.content  # type: ignore[return-value]


def parse_args(argv: Optional[list[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "image_url",
        nargs="?",
        default="https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-VL/assets/demo.jpeg",
        help="URL of the image to describe.",
    )
    parser.add_argument(
        "--api-key",
        dest="api_key",
        help="Herdora API key. If omitted, HERDORA_API_KEY env var is used.",
    )
    return parser.parse_args(argv)


def main(argv: Optional[list[str]] = None) -> int:
    args = parse_args(argv)

    try:
        client = create_client(args.api_key)
        message = generate_caption(args.image_url, client)
    except Exception as exc:  # pragma: no cover - CLI convenience
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(message)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
