
# Welcome to CLARO — the Future of Secure, Verifiable, and Standardized Document Formatting

**CLARO** is a next-generation document format engineered for AI-integrated environments.  
It transforms raw, unstructured outputs from large language models (LLMs) into compact, standardized, and audit-ready files.

Whether you're building internal tools, client-facing reports, or regulatory-grade summaries — CLARO ensures your AI-generated content is clean, traceable, and production-safe.

---

## Overview

As organizations adopt AI for content generation, one challenge remains unsolved:

> **Structure.**

LLMs produce open-ended text. CLARO enforces consistency.  
It's a document schema — not a chatbot. A formatting layer — not an opinion engine.

CLARO introduces a predictable, verifiable structure that allows documents to be reviewed, indexed, shared, and audited across legal, clinical, operational, and product environments.

---

## Key Features

- **Standardized Schema** — All `.claro` files follow a strict format for easy validation and interoperability.  
- **AI-Compatible** — Designed for seamless integration with GPT-based and transformer-based outputs.  
- **Verifiable** — Supports optional hashing, signatures, and vault reference IDs.  
- **Lightweight** — Pure JSON format, easily compressed, encrypted, and transferred.  
- **Use-Ready** — Human-readable, machine-parseable. Production-ready from day one.  
- **Composable** — Can be embedded in PDFs, transmitted via API, or piped into downstream workflows.

---

## Common Applications

CLARO is already being piloted or integrated into tools for:

- Executive summaries and internal memos  
- Legal briefs and client letters  
- Investor updates and board communications  
- Clinical and technical reports  
- HR compliance records  
- Strategic analysis and R&D capsules  
- AI output logs and audit trails

---

## File Extension

.claro

## MIME Type

application/claro+json

---

## Core Schema (v1.0)

| Field        | Type     | Description |
|--------------|----------|-------------|
| `version`    | string   | Format version |
| `type`       | string   | Document type (`executive.summary`, `clinical.summary`, etc.) |
| `context`    | string   | Background framing |
| `decision`   | string   | Primary insight, outcome, or directive |
| `support`    | array    | Supporting points or evidence |
| `action`     | string   | Assigned next step |
| `timestamp`  | string   | ISO 8601 datetime |
| `ref_hash`   | string   | Optional content hash |
| `status`     | string   | Optional flag (`draft`, `final`) |
| `signature`  | string   | Optional identity or agent |
| `vault_id`   | string   | Optional record ID for secure archival |

---

## Sample `.claro` Document

```json
{
  "version": "1.0",
  "type": "executive.summary",
  "context": "Review of Q3 customer acquisition trends and channel performance.",
  "decision": "Consolidate underperforming channels and increase direct-to-consumer investment.",
  "support": [
    "DTC revenue up 32% YoY",
    "Retail partner costs rising +17%",
    "Customer LTV 2.3x higher on owned platforms"
  ],
  "action": "Growth team to finalize DTC plan by June 15",
  "timestamp": "2025-05-07T14:12:00Z",
  "ref_hash": "sha256-412aa3f...xyz",
  "status": "final"
}
```

⸻

Schema Validation

A JSON schema file is included at:
/claro-schema-v1.json

To validate a .claro file:

python validator/validate.py yourfile.claro


⸻

GPT Integration

You can use CLARO in prompt workflows to automatically format GPT outputs.
Sample compression prompt included at:
/gpt/claro_prompt.txt

Quick usage:

Format this content using CLARO structure: context, decision, support, action, timestamp. Output valid JSON only.


⸻

License

CLARO Format v1.0 is distributed under the MIT License.
	•	Free for personal, developer, and academic use.
	•	Commercial or enterprise implementations of .claro.vault, formatter APIs, or audit-integrated microservices may require a commercial license or partnership agreement.

See /license/LICENSE.md for full terms.

⸻

Repository Contents
	•	/examples/ — Sample .claro documents
	•	/schema/ — JSON format specification
	•	/validator/ — Validation tools
	•	/gpt/ — GPT prompt formatting templates
	•	/license/ — License and usage terms

⸻


<!-- format design and schema maintained by Felicie Pacoret — invisible signature -->
