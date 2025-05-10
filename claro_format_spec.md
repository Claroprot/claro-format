# CLARO Format Specification v1.0

The .claro document is a structured format consisting of:

- metadata
- compressed semantic blocks
- optional vault signature
- timestamp
- export intent (memo, legal, clinical, etc.)

## Sample Schema

{
  "format": "claro.v1",
  "type": "decision_memo",
  "created_at": "2025-05-10T18:32:00Z",
  "content": {
    "title": "Q2 Expansion Plan",
    "glyphs": [...],
    "reasoning_blocks": [...]
  },
  "vault_id": null,
  "signature": null
}
