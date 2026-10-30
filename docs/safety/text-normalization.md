# Unicode Text Normalization for Policy Matching

## Purpose

The `normalize_for_policy_match()` function creates a deterministic, normalized representation of text for policy matching.

It does not perform clinical decisions, detect personally identifiable information (PII), or modify the original clinical record.

## Transformation Order

The function applies the following operations:

1. Validate that the input is a string.
2. Reject inputs exceeding 10,000 Unicode code points.
3. Apply Unicode NFKC normalization.
4. Apply Unicode case folding using `str.casefold()`.
5. Normalize whitespace using `split()` and `" ".join()`.
6. Remove `U+200B` (ZERO WIDTH SPACE).
7. Reject normalized outputs exceeding 10,000 Unicode code points.
8. Return the normalized string.

## Zero-Width Character Policy

The current implementation removes only `U+200B`.

Other invisible characters, including `U+200C` (ZERO WIDTH NON-JOINER), `U+200D` (ZERO WIDTH JOINER), and `U+FE0F` (VARIATION SELECTOR-16), are not explicitly removed.

This narrow policy avoids indiscriminately deleting characters that may have linguistic or presentation significance.

## Safety and Limitations

- Uses only the Python standard library.
- Raises `TypeError` for non-string inputs.
- Raises `ValueError` when input or output exceeds the configured limit.
- Error messages do not include the input text.
- NFKC normalization can change compatibility distinctions, so the normalized representation must not replace the original clinical text.
- The output limit is checked after normalization; intermediate allocations are not separately bounded.
- The implementation has not been proven idempotent for every possible Unicode input.

## Testing

Run the unit tests from the repository root:

```bash
python -m unittest discover -s tests -p "test_text_policy_normalization.py" -v
```

Synthetic boundary cases are stored in `tests/fixtures/unicode_boundary_cases.json`.
