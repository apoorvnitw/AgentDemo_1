# 04 Error handling: plan

Stop after step 5 (per `CLAUDE.md`).

1. Create `tests/test_errors.py` with the cases from `validation.md`. Run it and expect failures.
2. Add `ConvertError`, the `ArgumentParser` subclass and the checks to `convert.py`; make `main` catch `ConvertError`.
3. Run `pytest` until green. All earlier tests must still pass.
4. Run two bad commands by hand (`python convert.py abc C F`, `python convert.py 100 C psi`) and check the output is one `error:` line with exit code 1.
5. Confirm `answer_keys/` is unmodified (`git status`), then stop and report.
