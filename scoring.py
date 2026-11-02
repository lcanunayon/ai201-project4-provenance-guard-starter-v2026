"""
Turning two numbers into one, and one number into something a person can read.
← YOU BUILD THIS IN MILESTONES 4 AND 5

Two functions live here, and both are stubs.

`combine_signals` is where your false-positive decision from Milestone 1
actually gets made. Everything above it — the labels, the appeal path — is
downstream of a number this function produced.

`score_to_label` is where you stop writing for a machine and start writing for
a person. A score of 0.62 means nothing to a writer.

⚠️ Your README's **Signals and Scoring** section has to name the file and
function holding your combining rule. The grader checks your code against what
you claim, so that line should read `scoring.py::combine_signals`.
"""

import config


def combine_signals(model_score: float, style_score: float) -> float:
    """
    Combine two 0–1 signals into one 0–1 score. ← TODO (Milestone 4)

    Both inputs point the same way: higher means more likely AI. Your output
    should too.

    Args:
        model_score: from `detector.model_signal` — how predictable the text is.
        style_score: from `stylometry.style_signal` — the shape of the text.

    Returns:
        A float from 0.0 (confidently human) to 1.0 (confidently AI).

    ⚠️ **Write the rule down before you code it, and put the numbers in your
    README.** A weighted average is the obvious choice and it is not the only
    one. Things worth thinking about:

      - **What happens when they disagree?** One signal at 0.9 and the other at
        0.1 averages to 0.5 — "unsure". Is that what you want? It might be
        exactly right: two methods disagreeing IS uncertainty. Or you might
        decide one signal is more trustworthy when they split.

      - **Which way do you want to be wrong?** Weighting toward the signal that
        reads more human means fewer false accusations and more AI text
        getting through. There's no weighting that avoids the trade.

      - Milestone 4 asks you to find a case where your two signals split and
        write it down. That case is what this rule exists to handle.

    The weights in config.py are placeholders. Change them, or ignore them and
    write a different rule.
    """
    # The rule (README "The combining rule"): a plain weighted average, 50/50.
    # When the signals split, the average lands mid-range and the text reads
    # "unsure" — two methods disagreeing is uncertainty, and this system would
    # rather say so than accuse on one signal.
    score = (
        config.WEIGHT_MODEL_SIGNAL * model_score
        + config.WEIGHT_STYLE_SIGNAL * style_score
    )
    return round(min(max(score, 0.0), 1.0), 4)


def score_to_label(score: float) -> tuple[str, str]:
    """
    Turn a score into a guess and the text a reader actually sees.
    ← TODO (Milestone 5)

    Returns:
        (guess, label_text) — where `guess` is a short machine-readable string
        like "ai" / "human" / "unsure", and `label_text` is the full sentence
        shown to a person.

    ⚠️ Write the label text for someone who has never heard the word
    "threshold".

        ✗ "human, 0.81 confidence"
        ✓ "We think this was probably written by a person."

    All three labels have to be **reachable**. If no score can produce one of
    them, your ranges have a gap — and Milestone 5 asks you to submit text that
    produces each one, which is how you'd find out.

    The hardest one to write is "unsure". It has to admit uncertainty without
    sounding like an accusation, because the person reading it may well have
    written every word themselves. Your breakout asks your group what they'd
    think if they got it on their own work. That question is the whole
    milestone.
    """
    # Thresholds are in config.py. Both edges are inclusive: exactly
    # AI_THRESHOLD is "ai", exactly HUMAN_THRESHOLD is "human", so there's no gap.
    if score >= config.AI_THRESHOLD:
        return "ai", LABEL_AI
    if score <= config.HUMAN_THRESHOLD:
        return "human", LABEL_HUMAN
    return "unsure", LABEL_UNSURE


# The exact text a writer sees. Kept here so the README can quote them verbatim.
LABEL_HUMAN = "We think this was probably written by a person."

LABEL_UNSURE = (
    "We can't tell whether this was written by a person or by AI. "
    "This isn't a finding that you used AI — a lot of people's own writing "
    "lands here. If you'd like, you can ask a person to review it, and asking "
    "never counts against you."
)

LABEL_AI = (
    "Our check thinks this reads like text written by AI. That isn't proof, "
    "and the check makes mistakes — it sometimes flags writing people did "
    "entirely themselves. If you wrote this, you can ask a person to review "
    "it, and asking never counts against you."
)


def confidence(score: float) -> float:
    """
    How firmly a score sits inside the band it was labelled with, 0–1.

    0 means right on a cutoff, where a tiny change would flip the label.
    1 means as deep inside the band as it gets: 0.0 for "human", 1.0 for "ai",
    or the exact middle of the unsure band for "unsure".

    Measured against the label's own band, not against 0.5, because the bands
    aren't symmetric (0.35 and 0.82). Against 0.5, a score of 0.81 read as
    0.62 confident while being labelled "unsure" — the number contradicted
    the label it sat next to.
    """
    low, high = config.HUMAN_THRESHOLD, config.AI_THRESHOLD
    if score >= high:
        depth = (score - high) / (1.0 - high)
    elif score <= low:
        depth = (low - score) / low
    else:
        depth = min(score - low, high - score) / ((high - low) / 2)
    return round(min(max(depth, 0.0), 1.0), 4)


def label_ranges() -> list[tuple[str, str]]:
    """
    The score range each label covers. Your README needs these beside the
    label text — given to you so the numbers can't drift apart from config.py.
    """
    return [
        ("high-confidence human", f"0.00 – {config.HUMAN_THRESHOLD:.2f}"),
        ("unsure", f"{config.HUMAN_THRESHOLD:.2f} – {config.AI_THRESHOLD:.2f}"),
        ("high-confidence AI", f"{config.AI_THRESHOLD:.2f} – 1.00"),
    ]
