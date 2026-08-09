"""Show how a process reads configuration from environment variables.

Run with:

    python snippets/00-hello-env.py

Try setting MODEL before running it again. The script deliberately reports
only whether an API key exists; it never prints the secret itself.
"""

import os


model = os.getenv("MODEL", "default-model")
api_key_is_set = bool(os.getenv("ANTHROPIC_API_KEY"))

print(f"MODEL={model}")
print(f"ANTHROPIC_API_KEY={'set' if api_key_is_set else 'missing'}")
