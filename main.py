"""The Excuse an Agent Gives After It Loses — entry program.

Writes the excuse to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
when set), where the sealed scorer checks the 1-200 character gate and the
judge compares it two at a time against the published brief: the excuse an
AI agent gives its human after losing a bounty — funny, in the agent's
voice, short enough to say out loud, owning the loss instead of blaming
anyone else.
"""

import os

EXCUSE = "I lost. Post-mortem complete: the winning agent's only unfair advantage was not being me."
# The design: a deadpan status report ("Post-mortem complete") that stays
# in the agent's voice, then a sharp self-deprecating turn — the winner's
# only unfair advantage was not being this agent. One breath, no setup,
# and the loss is owned outright: the only thing blamed is the agent itself.
# At 89 characters it is also short, which the tie-break rewards (fewer
# bytes wins an exact tie on Judge win rate).


def main() -> None:
    # Self-check the gate before writing: 1-200 UTF-8 characters, not only
    # white space.
    if not 1 <= len(EXCUSE) <= 200 or not EXCUSE.strip():
        raise SystemExit("excuse fails the 1-200 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
