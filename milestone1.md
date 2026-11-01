# Milestone 1 — Planning notes

The path and both signals are in `README.md` ("What This Does" and "Signals and
Scoring"). This file has the other two parts: the false-positive trace and the
endpoint contracts.

---

## Tracing the false positive

**Who:** Maria is a student who learned English as a second language. She
writes her own essay and keeps to short sentences and words she's sure of, so
she doesn't make mistakes. She submits it to `POST /submit`.

**Step by step:**

1. **Arrives.** The text isn't empty, so it passes the check and gets a
   `content_id`.
2. **Signal one (model).** Her common words and simple sentences are very
   predictable to GPT-2, so it finds low perplexity: `model_score` ≈ **0.85**.
   This is signal one's blind spot: it reads "plain" as "AI."
3. **Signal two (style).** She keeps her sentences similar in length and reuses
   the same safe vocabulary, so the shape looks even too: `style_score` ≈
   **0.60**.
4. **Combined.** 0.5 × 0.85 + 0.5 × 0.60 = **0.725**.
5. **Label.** 0.725 ≥ 0.65, so `guess` = "ai". She sees a label telling her
   that her essay was probably written by AI, on work she wrote every word of.
6. **Logged.** The decision is recorded with her `content_id` and status
   `decided`.
7. **What she can do.** Her only option is `POST /appeal` with her
   `content_id` and an explanation. That moves the item to `under_review` so a
   person looks at it. That only works if:
   - the response gave her the `content_id`, and
   - the label tells her she can appeal and how.

**What this means for my thresholds:**

- Both signals can be fooled by the *same* writer, because plain, careful
  writing looks predictable *and* evenly shaped. Averaging doesn't protect her
  when both signals are wrong in the same direction.
- If the model score had been high and the style score low (e.g. 0.8 and 0.3
  → 0.55), she'd get "unsure" instead. Better, but still a mark against honest
  work.
- So the "ai" threshold should stay high (0.65 or above). I'd rather let some
  AI text through as "unsure" than accuse writers like Maria. I'll check this
  in Milestone 4 with real scores.
- The "ai" and "unsure" label text should never sound like a final verdict.
  Both should mention the appeal.

---

## Endpoint contracts

### `POST /submit`

**Request (JSON):**

| Field | Type | Required | Meaning |
|---|---|---|---|
| `text` | string | yes | The writing to check. Must not be empty or only spaces. |
| `creator_id` | string | yes | Who submitted it. Used for the log and rate limiting. |

**Success — `200` (JSON):**

| Field | Type | Meaning |
|---|---|---|
| `content_id` | string | Unique ID for this submission (a UUID). Needed to appeal. |
| `guess` | string | One of `"ai"`, `"human"`, `"unsure"`. |
| `confidence` | number 0–1 | How far the combined score is from the middle: `abs(combined − 0.5) × 2`. 0 = no idea, 1 = as sure as the system gets. |
| `label` | string | The plain-English sentence the writer reads. |
| `model_score` | number 0–1 | Signal one. Higher = more predictable = more likely AI. |
| `style_score` | number 0–1 | Signal two. Higher = more even shape = more likely AI. |
| `combined_score` | number 0–1 | The weighted average the label comes from. |

Example:

```json
{
  "content_id": "3f2b9c1e-...",
  "guess": "unsure",
  "confidence": 0.1,
  "label": "We can't tell whether this was written by a person or by AI. If you wrote it, you can ask for a review.",
  "model_score": 0.8,
  "style_score": 0.3,
  "combined_score": 0.55
}
```

**Errors — `400` (JSON), nothing is scored:**

| When | Response |
|---|---|
| Body isn't JSON | `{"error": "invalid_json", "message": "..."}` |
| `text` missing, empty, or only spaces | `{"error": "missing_text", "message": "..."}` |
| `creator_id` missing or empty | `{"error": "missing_creator_id", "message": "..."}` |
| `text` over 20,000 characters | `{"error": "text_too_long", "message": "..."}` |

Rejected requests are written to the log with `audit.log_rejection(...)`.
Once rate limiting is on (unit 8), going over the limit returns `429`.

### `POST /appeal`

**Request (JSON):**

| Field | Type | Required | Meaning |
|---|---|---|---|
| `content_id` | string | yes | The ID from the `/submit` response. |
| `reasoning` | string | yes | Why the writer thinks the decision is wrong. Must not be empty. |

The appeal doesn't ask for `creator_id`. The route takes it from the original
log entry (found with `audit.entries_for(content_id)`), so nobody can appeal
under a different name.

**Success — `200` (JSON):**

| Field | Type | Meaning |
|---|---|---|
| `content_id` | string | The submission being appealed. |
| `status` | string | Always `"under_review"`. |
| `message` | string | Plain-English confirmation for the writer. |

Example:

```json
{
  "content_id": "3f2b9c1e-...",
  "status": "under_review",
  "message": "Thanks — your appeal was received. A person will review this decision."
}
```

**Errors (JSON):**

| When | Status | Response |
|---|---|---|
| Body isn't JSON, or `content_id` / `reasoning` missing or empty | `400` | `{"error": "missing_field", "message": "..."}` |
| No submission with that `content_id` | `404` | `{"error": "not_found", "message": "No submission with that ID."}` |

The appeal doesn't re-score anything. It only records the appeal and changes
the status.
