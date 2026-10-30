# 03 CLI: plan

Stop after step 5 (per `CLAUDE.md`).

1. Create `tests/test_cli.py` with the cases from `validation.md`. Run it and expect failures.
2. Add `UNITS` and `main(argv=None)` to `convert.py`, plus the `__main__` entry point.
3. Run `pytest` until green. The temperature and pressure tests must still pass.
4. Run `python convert.py 100 C F` once by hand and check it prints `212.00`.
5. Confirm `answer_keys/` is unmodified (`git status`), then stop and report.
