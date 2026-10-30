# 05 Answer-key test: plan

Stop after step 5 (per `CLAUDE.md`).

1. Create `tests/test_answer_keys.py` as described in `validation.md`.
2. Run `pytest`. Group 1-4 already implement everything, so the new tests are expected to pass straight away.
3. Prove the test can fail: temporarily change `KPA_PER_PSI` in `convert.py`, confirm the pressure rows fail, then restore the file with `git checkout convert.py`.
4. Re-run `pytest` and confirm it is green again.
5. Confirm `answer_keys/` and `convert.py` have no diff (`git status`), then stop and report.
