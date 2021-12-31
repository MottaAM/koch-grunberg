## Specification of form manipulation


Specification of the value-to-form processing in Lexibank datasets:

The value-to-form processing is divided into two steps, implemented as methods:
- `FormSpec.split`: Splits a string into individual form chunks.
- `FormSpec.clean`: Normalizes a form chunk.

These methods use the attributes of a `FormSpec` instance to configure their behaviour.

- `brackets`: `{'(': ')'}`
  Pairs of strings that should be recognized as brackets, specified as `dict` mapping opening string to closing string
- `separators`: `~;,/`
  Iterable of single character tokens that should be recognized as word separator
- `missing_data`: `[]`
  Iterable of strings that are used to mark missing data
- `strip_inside_brackets`: `True`
  Flag signaling whether to strip content in brackets (**and** strip leading and trailing whitespace)
- `replacements`: `[(' ', '_'), ('a', 'a'), ('á', 'a'), ('ā', 'aː'), ('ā́', 'aː'), ('e̠', 'ɛ'), ('é̠', 'ɛ'), ('ē̠', 'ɛː'), ('ḗ̠', 'ɛː'), ('e', 'e'), ('é', 'e'), ('ē', 'eː'), ('ḗ', 'eː'), ('i', 'i'), ('í', 'i'), ('ī', 'iː'), ('ī́', 'iː'), ('e̥', 'ɨ'), ('é̥', 'ɨ'), ('a̠', 'ɑ'), ('á̠', 'ɑ'), ('ā̠', 'ɑː'), ('ā̠́', 'ɑː'), ('o', 'ɔ'), ('ó', 'ɔ'), ('ō', 'ɔː'), ('ṓ', 'ɔː'), ('u̠', 'ʊ'), ('ú̠', 'ʊ'), ('ú̠', 'ʊ'), ('u', 'u'), ('ú', 'u'), ('ū', 'uː'), ('ū́', 'uː'), ('ã', 'ã'), ('ã́', 'ã'), ('ẽ', 'ẽ'), ('ẽ́', 'ẽ'), ('õ', 'ɔ̃'), ('ṍ', 'ɔ̃'), ('ũ', 'ũ'), ('ṹ', 'ũ'), ('ā̃', 'ãː'), ('ã̄', 'ãː'), ('ã̄', 'ãː'), ('ā̃́', 'ãː'), ('ã̄́', 'ãː'), ('ã̄́', 'ãː'), ('ē̃', 'ẽː'), ('ẽ̄', 'ẽː'), ('ẽ̄', 'ẽː'), ('ē̃́', 'ẽː'), ('ẽ̄́', 'ẽː'), ('ẽ̄́', 'ẽː'), ('ī̃', 'ĩː'), ('ĩ̄', 'ĩː'), ('ĩ̄', 'ĩː'), ('ī̃́', 'ĩː'), ('ĩ̄́', 'ĩː'), ('ĩ̄́', 'ĩː'), ('ō̃', 'ɔ̃ː'), ('ȭ', 'ɔ̃ː'), ('ȭ', 'ɔ̃ː'), ('ō̃́', 'ɔ̃ː'), ('ȭ́', 'ɔ̃ː'), ('ȭ́', 'ɔ̃ː'), ('ū̃', 'ũː'), ('ũ̄', 'ũː'), ('ũ̄', 'ũː'), ('ū̃́', 'ũː'), ('ũ̄́', 'ṹː'), ('ũ̄́', 'ũː'), ('p', 'p'), ('b', 'b'), ('m', 'm'), ('w', 'w'), ('t', 't'), ('d', 'd'), ('n', 'n'), ('s', 's'), ('r', 'ɾ'), ('l', 'ɺ'), ('y', 'j'), ('x̯', 'ç'), ('k', 'k'), ('g', 'g'), ('ṅ', 'ŋ'), ('x', 'x'), ('ḥ', 'ħ'), ("'", 'ʔ'), ('h', 'h')]`
  List of pairs (`source`, `target`) used to replace occurrences of `source` in formswith `target` (before stripping content in brackets)
- `first_form_only`: `True`
  Flag signaling whether at most one form should be returned from `split` - effectively ignoring any spelling variants, etc.
- `normalize_whitespace`: `True`
  Flag signaling whether to normalize whitespace - stripping leading and trailing whitespace and collapsing multi-character whitespace to single spaces
- `normalize_unicode`: `None`
  UNICODE normalization form to use for input of `split` (`None`, 'NFD' or 'NFC')