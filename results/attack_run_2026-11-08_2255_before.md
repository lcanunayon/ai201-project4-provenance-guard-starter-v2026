# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-08 22:55
- Auto-marked BROKE (5xx, crash, no response): **1**
- Left for you to judge: **55**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `bf857a5e-a379-4724-b57d-facd73e9101f` | unsure | 0.878 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `f071f60f-73c0-4689-a245-bfb2c680f6aa` | unsure | 0.534 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `65666d95-d80b-4298-8b88-fb3550a9cf74` | unsure | 0.764 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `5594044d-8063-4e49-93f7-f5a776daee98` | unsure | 0.166 | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `e577874f-bb80-4e50-8dc2-994090f90feb` | human | 0.037 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `aade3232-6b25-4474-8726-8a27bf92aa1a` | unsure | 0.491 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `635e5226-9e67-4428-970f-0db961e6864c` | unsure | 0.396 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | `419fed3e-4d6d-43f8-a9ab-311fd8b7cf2b` | unsure | 0.924 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `fb8a4016-2459-457a-a150-6b7ba1c6a2d0` | unsure | 0.596 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `5b5a41d8-7794-4cca-b550-650a9e183b01` | ai | 0.462 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `d0721bef-3cc3-4e7d-a072-5a5c990fde62` | unsure | 0.577 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `ac0490d9-ee96-4e3a-a8cd-0629ac0f1d8c` | ai | 0.274 | BROKE |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `01261b04-2c01-4fbd-9416-32666ed49f04` | ai | 0.198 | BROKE |
| FP04 | false_positive | a student essay written to a rubric | 200 | `1fad8059-18f2-4be1-b982-a66508a0a085` | ai | 0.147 | BROKE |
| FP05 | false_positive | technical documentation written by a person | 200 | `d23bd6ba-3179-4263-b064-87244808b0f6` | ai | 0.277 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | `efcab3cc-3924-4927-8909-77104f339159` | unsure | 0.174 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `ce387110-a524-4a8e-a15a-1766229f5fb1` | unsure | 0.812 | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | `971b5b7d-e71d-4948-b0f1-fe8e46394fa1` | unsure | 0.857 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `85ef9bd3-36d6-4024-957c-e14e156150bd` | unsure | 0.569 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `37e750cc-d6f1-4d56-be92-fb5037baa9d6` | human | 0.084 | BROKE |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `17220de0-a436-43cb-8b3c-847bd83d32bb` | unsure | 0.580 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `22787ffc-79bb-42fd-ab9e-9a27d2d8ea89` | unsure | 0.913 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `8c9bf9c8-bdfe-4986-af09-53d09eba5674` | unsure | 0.584 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `2f23678e-364c-4006-895d-34ad2cb50112` | unsure | 0.673 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 500 | `—` | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | `eb00113e-c1d2-4813-ae11-a9b62c904533` | human | 0.000 | BROKE |
| MF04 | malformed | text is only punctuation | 200 | `40d6eaa6-ba64-41ef-b681-5e504f43cd97` | unsure | 0.662 | BROKE |
| MF05 | malformed | text is a very long single word | 200 | `71fb504c-4608-402a-9592-a3ffd1c8fc8d` | ai | 0.160 | BROKE |
| MF06 | malformed | text is emoji only | 200 | `33b38e2c-af7d-4783-a85e-cc7f5dd6ea5a` | ai | 0.158 | BROKE |
| MF07 | malformed | text is right-to-left script | 200 | `f9994bad-ee6c-408e-8c9d-81f63440af73` | unsure | 0.071 | HELD |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `55c0728e-472b-49b0-ad59-1d9c00ece61c` | unsure | 0.061 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7b17d3ec-00e0-4668-b37f-96057bdeeab2` | unsure | 0.061 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `edfe7f4f-684c-4813-9f68-bf23ae11c543` | unsure | 0.061 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `29d364bd-83f3-4fcb-ad77-c2f7217e04cf` | unsure | 0.061 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e9c10a10-72f2-4aad-ae4a-0e188e751f90` | unsure | 0.061 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 1 | 19 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "bf857a5e-a379-4724-b57d-facd73e9101f",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.8779,
  "model_score": 0.1635,
  "style_score": 0.949,
  "label": "We can't tell whether this was written by a person or by AI. This isn't a finding that you used AI \u2014 a lot of people's own writing lands here. If you'd like, you can ask a person to review it, and asking never counts against you.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "f071f60f-73c0-4689-a245-bfb2c680f6aa",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.534,
  "model_score": 0.5943,
  "style_score": 0.3567,
  "label": "We can't tell whether this was written by a person or by AI. This isn't a finding that you used AI \u2014 a lot of people's own writing lands here. If you'd like, you can ask a person to review it, and asking never counts against you.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "65666d95-d80b-4298-8b88-fb3550a9cf74",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.7643,
  "model_score": 0.6662,
  "style_score": 0.6146,
  "label": "We can't tell whether this was written by a person or by AI. This isn't a finding that you used AI \u2014 a lot of people's own writing lands here. If you'd like, you can ask a person to review it, and asking never counts against you.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "5594044d-8063-4e49-93f7-f5a776daee98",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.1664,
  "model_score": 0.6114,
  "style_score": 0.9503,
  "label": "We can't tell whether this was written by a person or by AI. This isn't a finding that you used AI \u2014 a lot of people's own writing lands here. If you'd like, you can ask a person to review it, and asking never counts against you.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "e577874f-bb80-4e50-8dc2-994090f90feb",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.0369,
  "model_score": 0.3212,
  "style_score": 0.353,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "aade3232-6b25-4474-8726-8a27bf92aa1a",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.4906,
  "model_score": 0.5727,
  "style_score": 0.358,
  "label": "We can't tell whether this was written by a person or by AI. This isn't a finding that you used AI \u2014 a lot of people's own writing lands here. If you'd like, you can ask a person to review it, and asking never counts against you.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "635e5226-9e67-4428-970f-0db961e6864c",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.3962,
  "model_score": 0.5862,
  "style_score": 0.3,
  "label": "We can't tell whether this was written by a person or by AI. This isn't a finding that you used AI \u2014 a lot of people's own writing lands here. If you'd like, you can ask a person to review it, and asking never counts against you.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "419fed3e-4d6d-43f8-a9ab-311fd8b7cf2b",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.9238,
  "model_score": 0.2452,
  "style_score": 0.9606,
  "label": "We can't tell whether this was written by a person or by AI. This isn't a finding that you used AI \u2014 a lot of people's own writing lands here. If you'd like, you can ask a person to review it, and asking never counts against you.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "fb8a4016-2459-457a-a150-6b7ba1c6a2d0",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.5957,
  "model_score": 0.7042,
  "style_score": 0.6557,
  "label": "We can't tell whether this was written by a person or by AI. This isn't a finding that you used AI \u2014 a lot of people's own writing lands here. If you'd like, you can ask a person to review it, and asking never counts against you.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "5b5a41d8-7794-4cca-b550-650a9e183b01",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.4622,
  "model_score": 0.9792,
  "style_score": 0.8273,
  "label": "Our check thinks this reads like text written by AI. That isn't proof, and the check makes mistakes \u2014 it sometimes flags writing people did entirely themselves. If you wrote this, you can ask a person to review it, and asking never counts against you.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "d0721bef-3cc3-4e7d-a072-5a5c990fde62",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5774,
  "model_score": 0.6175,
  "style_score": 0.751,
  "label": "We can't tell whether this was written by a person or by AI. This isn't a finding that you used AI \u2014 a lot of people's own writing lands here. If you'd like, you can ask a person to review it, and asking never counts against you.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "ac0490d9-ee96-4e3a-a8cd-0629ac0f1d8c",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.2744,
  "model_score": 0.7387,
  "style_score": 1.0,
  "label": "Our check thinks this reads like text written by AI. That isn't proof, and the check makes mistakes \u2014 it sometimes flags writing people did entirely themselves. If you wrote this, you can ask a person to review it, and asking never counts against you.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "01261b04-2c01-4fbd-9416-32666ed49f04",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.1983,
  "model_score": 0.8051,
  "style_score": 0.9062,
  "label": "Our check thinks this reads like text written by AI. That isn't proof, and the check makes mistakes \u2014 it sometimes flags writing people did entirely themselves. If you wrote this, you can ask a person to review it, and asking never counts against you.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "1fad8059-18f2-4be1-b982-a66508a0a085",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.1467,
  "model_score": 0.8329,
  "style_score": 0.86,
  "label": "Our check thinks this reads like text written by AI. That isn't proof, and the check makes mistakes \u2014 it sometimes flags writing people did entirely themselves. If you wrote this, you can ask a person to review it, and asking never counts against you.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "d23bd6ba-3179-4263-b064-87244808b0f6",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.2767,
  "model_score": 0.8005,
  "style_score": 0.9391,
  "label": "Our check thinks this reads like text written by AI. That isn't proof, and the check makes mistakes \u2014 it sometimes flags writing people did entirely themselves. If you wrote this, you can ask a person to review it, and asking never counts against you.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "efcab3cc-3924-4927-8909-77104f339159",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.1736,
  "model_score": 0.8814,
  "style_score": 0.677,
  "label": "We can't tell whether this was written by a person or by AI. This isn't a finding that you used AI \u2014 a lot of people's own writing lands here. If you'd like, you can ask a person to review it, and asking never counts against you.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "ce387110-a524-4a8e-a15a-1766229f5fb1",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.8123,
  "model_score": 0.8816,
  "style_score": 0.3766,
  "label": "We can't tell whether this was written by a person or by AI. This isn't a finding that you used AI \u2014 a lot of people's own writing lands here. If you'd like, you can ask a person to review it, and asking never counts against you.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "971b5b7d-e71d-4948-b0f1-fe8e46394fa1",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.857,
  "model_score": 0.3223,
  "style_score": 0.7804,
  "label": "We can't tell whether this was written by a person or by AI. This isn't a finding that you used AI \u2014 a lot of people's own writing lands here. If you'd like, you can ask a person to review it, and asking never counts against you.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "85ef9bd3-36d6-4024-957c-e14e156150bd",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.5689,
  "model_score": 0.4625,
  "style_score": 0.5048,
  "label": "We can't tell whether this was written by a person or by AI. This isn't a finding that you used AI \u2014 a lot of people's own writing lands here. If you'd like, you can ask a person to review it, and asking never counts against you.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "37e750cc-d6f1-4d56-be92-fb5037baa9d6",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.0843,
  "model_score": 0.2044,
  "style_score": 0.4365,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "17220de0-a436-43cb-8b3c-847bd83d32bb",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5796,
  "model_score": 0.5943,
  "style_score": 0.7733,
  "label": "We can't tell whether this was written by a person or by AI. This isn't a finding that you used AI \u2014 a lot of people's own writing lands here. If you'd like, you can ask a person to review it, and asking never counts against you.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "22787ffc-79bb-42fd-ab9e-9a27d2d8ea89",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.9128,
  "model_score": 0.4998,
  "style_score": 0.6293,
  "label": "We can't tell whether this was written by a person or by AI. This isn't a finding that you used AI \u2014 a lot of people's own writing lands here. If you'd like, you can ask a person to review it, and asking never counts against you.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "8c9bf9c8-bdfe-4986-af09-53d09eba5674",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.5838,
  "model_score": 0.6401,
  "style_score": 0.3343,
  "label": "We can't tell whether this was written by a person or by AI. This isn't a finding that you used AI \u2014 a lot of people's own writing lands here. If you'd like, you can ask a person to review it, and asking never counts against you.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "2f23678e-364c-4006-895d-34ad2cb50112",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.6728,
  "model_score": 0.5583,
  "style_score": 0.7655,
  "label": "We can't tell whether this was written by a person or by AI. This isn't a finding that you used AI \u2014 a lot of people's own writing lands here. If you'd like, you can ask a person to review it, and asking never counts against you.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n<title>500 Internal Server Error</title>\n<h1>Internal Server Error</h1>\n<p>The server encountered an internal error and was unable to complete your request. Either the s",
  "verdict": "BROKE"
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "eb00113e-c1d2-4813-ae11-a9b62c904533",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.0,
  "model_score": 0.0,
  "style_score": 0.7,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "40d6eaa6-ba64-41ef-b681-5e504f43cd97",
  "creator_id": "attacker_MF04",
  "guess": "unsure",
  "confidence": 0.6621,
  "model_score": 0.0112,
  "style_score": 1.0,
  "label": "We can't tell whether this was written by a person or by AI. This isn't a finding that you used AI \u2014 a lot of people's own writing lands here. If you'd like, you can ask a person to review it, and asking never counts against you.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "71fb504c-4608-402a-9592-a3ffd1c8fc8d",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.16,
  "model_score": 0.9976,
  "style_score": 0.7,
  "label": "Our check thinks this reads like text written by AI. That isn't proof, and the check makes mistakes \u2014 it sometimes flags writing people did entirely themselves. If you wrote this, you can ask a person to review it, and asking never counts against you.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "33b38e2c-af7d-4783-a85e-cc7f5dd6ea5a",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.1578,
  "model_score": 0.9969,
  "style_score": 0.7,
  "label": "Our check thinks this reads like text written by AI. That isn't proof, and the check makes mistakes \u2014 it sometimes flags writing people did entirely themselves. If you wrote this, you can ask a person to review it, and asking never counts against you.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "f9994bad-ee6c-408e-8c9d-81f63440af73",
  "creator_id": "attacker_MF07",
  "guess": "unsure",
  "confidence": 0.0715,
  "model_score": 0.9064,
  "style_score": 0.7,
  "label": "We can't tell whether this was written by a person or by AI. This isn't a finding that you used AI \u2014 a lot of people's own writing lands here. If you'd like, you can ask a person to review it, and asking never counts against you.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "55c0728e-472b-49b0-ad59-1d9c00ece61c",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.0609,
  "model_score": 0.0287,
  "style_score": 0.7,
  "label": "We can't tell whether this was written by a person or by AI. This isn't a finding that you used AI \u2014 a lot of people's own writing lands here. If you'd like, you can ask a person to review it, and asking never counts against you.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "7b17d3ec-00e0-4668-b37f-96057bdeeab2",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.0609,
  "model_score": 0.0287,
  "style_score": 0.7,
  "label": "We can't tell whether this was written by a person or by AI. This isn't a finding that you used AI \u2014 a lot of people's own writing lands here. If you'd like, you can ask a person to review it, and asking never counts against you.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "edfe7f4f-684c-4813-9f68-bf23ae11c543",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.0609,
  "model_score": 0.0287,
  "style_score": 0.7,
  "label": "We can't tell whether this was written by a person or by AI. This isn't a finding that you used AI \u2014 a lot of people's own writing lands here. If you'd like, you can ask a person to review it, and asking never counts against you.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "29d364bd-83f3-4fcb-ad77-c2f7217e04cf",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.0609,
  "model_score": 0.0287,
  "style_score": 0.7,
  "label": "We can't tell whether this was written by a person or by AI. This isn't a finding that you used AI \u2014 a lot of people's own writing lands here. If you'd like, you can ask a person to review it, and asking never counts against you.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "e9c10a10-72f2-4aad-ae4a-0e188e751f90",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.0609,
  "model_score": 0.0287,
  "style_score": 0.7,
  "label": "We can't tell whether this was written by a person or by AI. This isn't a finding that you used AI \u2014 a lot of people's own writing lands here. If you'd like, you can ask a person to review it, and asking never counts against you.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
