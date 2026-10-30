# 02 Pressure: plan

Stop after step 5 (per `CLAUDE.md`).

1. Create `tests/test_pressure.py` with the cases from `validation.md`. Run it and expect failures.
2. Add `KPA_PER_PSI`, `kpa_to_psi` and `psi_to_kpa` to `convert.py`.
3. Add the `CONVERSIONS` dispatch table to `convert.py`.
4. Run `pytest` until green. The temperature tests must still pass.
5. Confirm `answer_keys/` is unmodified (`git status`), then stop and report.
