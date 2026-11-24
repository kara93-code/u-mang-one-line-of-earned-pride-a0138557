"""One Line of Earned Pride.

The program builds one quiet, earned moment of pride and writes it to
/output/entry.txt. A grandmother who taught herself to read by lamplight
after the children slept finally reads her grandson to sleep, every word
landing where it belongs. No trophy, no podium, no graduation: the pride
is in the effort the line itself carries, and it arrives at the last word.
"""

import os
import sys

OPENING = "For seven years she taught herself to read by lamplight"
MIDDLE = "after the children slept, and tonight her grandson fell asleep"
CLOSING = "to her voice reading his bedtime story, every word landing where it belonged."

GATE_MIN = 1
GATE_MAX = 240


def build_line():
    """Assemble the single line from its three beats."""
    parts = [OPENING, MIDDLE, CLOSING]
    return " ".join(parts)


def find_problems(line):
    """List every way the line breaks the sealed gate."""
    problems = []
    if not line.strip():
        problems.append("line is blank")
    if len(line) < GATE_MIN:
        problems.append("line is shorter than 1 character")
    if len(line) > GATE_MAX:
        problems.append("line is longer than 240 characters")
    if "\n" in line:
        problems.append("line is more than one line")
    return problems


def output_path():
    """Where the entry goes: the harness dir, or /output by default."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(base, "entry.txt")


def main():
    line = build_line()
    problems = find_problems(line)
    if problems:
        for problem in problems:
            print("invalid entry: " + problem, file=sys.stderr)
        return 1
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")
    os.chmod(path, 0o644)
    with open(path, "r", encoding="utf-8") as handle:
        saved = handle.read()
    if saved != line + "\n":
        print("invalid entry: saved file does not match", file=sys.stderr)
        return 1
    print(line)
    print("characters: %d" % len(line))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
