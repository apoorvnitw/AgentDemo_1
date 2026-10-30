# 05 Answer-key test: requirements

- `tests/test_answer_keys.py` reads `answer_keys/conversion.csv` (columns `value,from,to,expected`) and checks every row end to end.
- End to end means running the real CLI: `python convert.py VALUE FROM TO` as a subprocess, comparing stdout to `expected` as strings (both are 2-decimal text).
- One pytest case per CSV row, so a failure names the row.
- The CSV is opened read-only. Rows come from the file, never copied into the test.
- No change to `convert.py` is expected. If a row fails, the code and the answer key disagree: stop and ask (`CLAUDE.md`), do not edit `answer_keys/`.

## Out of scope
- Editing, regenerating or reformatting `answer_keys/`.
- New conversion features.
