#!/usr/bin/env python3
"""
codecheck_run.py - the CODECHECK entry point, and the reason it exists.

THE PROBLEM. A CODECHECK manifest is validated against files the workflow
CREATES. `verify_paper.py` reads paper.tex and paper.pdf, recomputes every
numerical claim from first principles, prints one line per check to stdout,
and exits 0 or 1. It does not write anything: running it and hashing every
file in the tree before and after shows no file changed. With that, the
manifest would be empty and there would be nothing for a codechecker to
compare against.

THE RESOLUTION. `verify_paper.py` is not touched. This wrapper runs it as a
subprocess, captures what it printed, and writes that transcript to
`codecheck/report.txt`. The separation is the point:

    verify_paper.py    reads, compares, prints, exits. Writes nothing. Unchanged.
    codecheck_run.py   runs verify_paper.py and records what it said.

The artifact a codechecker compares is therefore a TRANSCRIPT OF THE
VERIFICATION, not an output of it.

The exit code is propagated, so a failing verification fails the CODECHECK.

Usage:
    python codecheck_run.py
"""

import io
import os
import subprocess
import sys
from datetime import datetime, timezone

AQUI = os.path.dirname(os.path.abspath(__file__))
SALIDA = os.path.join(AQUI, "codecheck")


def commit_actual():
    try:
        out = subprocess.run(
            ["git", "rev-parse", "HEAD"], stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL, cwd=AQUI, check=True)
        return out.stdout.decode("ascii", "replace").strip()
    except Exception:
        return "unknown (not a git checkout, or git unavailable)"


def main():
    if not os.path.isdir(SALIDA):
        os.makedirs(SALIDA)

    fecha = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    commit = commit_actual()

    proc = subprocess.run(
        [sys.executable, os.path.join(AQUI, "verify_paper.py")],
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=AQUI)
    texto = proc.stdout.decode("utf-8", "replace")
    sys.stdout.write(texto)

    resultado = "PASS" if proc.returncode == 0 else "FAIL (exit %d)" % proc.returncode

    ruta = os.path.join(SALIDA, "report.txt")
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write("# Transcript of `python verify_paper.py`, captured by codecheck_run.py.\n")
        f.write("# verify_paper.py itself writes nothing. This file is a record of what\n")
        f.write("# it printed, not an output of it. See the module docstring.\n")
        f.write("# date (UTC): %s\n" % fecha)
        f.write("# commit: %s\n" % commit)
        f.write("# result: %s\n" % resultado)
        f.write("#\n")
        f.write(texto)

    print("")
    print("codecheck_run.py: transcript written to codecheck/report.txt")
    print("codecheck_run.py: verify_paper.py exit status %d" % proc.returncode)
    return proc.returncode


if __name__ == "__main__":
    sys.exit(main())
