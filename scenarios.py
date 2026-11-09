"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

# ── Criterion 1 — five pieces I wrote myself, one deliberately plain ──────────
# Also the human half of criterion 2.
MY_WRITING = [
    "D’Eramo in “The pig and the skyscraper” describe the Pullman town to show that "
    "the language of benevolence and social improvement can mask systems of total "
    "economic and social control over the workers; essentially monopolizing the ways "
    "they are able to live. This system essentially monopolized not only their basic "
    "needs but also monopolized who workers may receive “good deeds” from, with a "
    "worker in D’Eramo’s analysis of events calling it a philanthropic monopoly.",

    "Another aspect was philanthropy being subordinated in Pullman town to its main "
    "goal, profit. Although wanting to seem just and generous with its amenities, "
    "workers, for example, could not buy their own house.",

    "The Haymarket trial was not really about a bomb – it was about ideas, class, "
    "capital, and who gets to define American ideals.",

    "The proliferation of American corporations and monopolies after the onset of the "
    "Civil War drastically changed the social and business landscape of America, "
    "accumulating massive fortunes to a few privileged people, done by thousands of "
    "underpaid workers",

    "Warnings of this situation were mentioned before as well as stated by Henry "
    "Adams, brother of historian Charles Francis Adams Jr, quote, “warned of the day "
    "when great corporations, ‘swaying power such as has never in the world’s history "
    "been trusted in the hands of mere private citizens,’ would be controlled by one "
    "man or combinations of men who would use these new leviathans to become masters "
    "of the nation.",
]

# ── Criterion 2 — five clearly-AI texts ─────────────────────────────────────
# Written by an AI (Claude) in its default assistant register, unedited.
CLEARLY_AI = [
    "Remote work has fundamentally transformed the modern workplace. It offers "
    "employees greater flexibility and allows them to achieve a better work-life "
    "balance. Additionally, companies can benefit from reduced overhead costs and "
    "access to a wider talent pool. However, remote work also presents several "
    "challenges. Communication can become more difficult, and employees may feel "
    "isolated from their colleagues. It is important for organizations to invest in "
    "the right tools and strategies to support their remote teams.",

    "Social media has had a profound impact on the way people communicate and share "
    "information. It allows individuals to connect with friends and family across the "
    "globe and provides a platform for diverse voices. However, it also raises "
    "important concerns about privacy, misinformation, and mental health. Studies "
    "have shown that excessive use can contribute to feelings of anxiety and "
    "isolation. Ultimately, it is essential for users to approach social media "
    "mindfully and to strike a healthy balance between online and offline life.",

    "Regular physical activity offers numerous benefits for both physical and mental "
    "health. Exercise helps to strengthen the heart, improve circulation, and "
    "maintain a healthy weight. In addition, it can reduce stress and improve mood by "
    "releasing endorphins. Experts generally recommend at least 150 minutes of "
    "moderate activity per week. By incorporating exercise into their daily "
    "routines, individuals can significantly enhance their overall well-being and "
    "reduce the risk of chronic disease.",

    "Renewable energy sources, such as solar and wind power, play a crucial role in "
    "addressing climate change. Unlike fossil fuels, they produce little to no "
    "greenhouse gas emissions during operation. Furthermore, advances in technology "
    "have made renewable energy more affordable and efficient than ever before. "
    "However, challenges remain, including energy storage and grid integration. By "
    "investing in research and infrastructure, governments and businesses can "
    "accelerate the transition to a more sustainable energy future.",

    "Reading is one of the most valuable habits a person can develop. It expands "
    "knowledge, improves vocabulary, and enhances critical thinking skills. "
    "Moreover, reading fiction can foster empathy by allowing readers to experience "
    "the world from different perspectives. In today's fast-paced digital world, "
    "setting aside time for reading can also provide a welcome escape from screens. "
    "Overall, making reading a regular part of one's routine can lead to lifelong "
    "personal and intellectual growth.",
]

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        "texts": MY_WRITING,
    },
    {
        "name": "spread: AI side",
        "criterion": 2,
        "texts": CLEARLY_AI,
    },
    {
        "name": "spread: human side",
        "criterion": 2,
        # The same five pieces as criterion 1 — they're the human writing I'm
        # surest about. Sent again under their own creator_ids.
        "texts": MY_WRITING,
    },
    {
        "name": "label coverage",
        "criterion": 3,
        # One input aimed at each label, all from the Milestone 4 calibration:
        # clearly AI (0.848 -> ai), Twain (0.262 -> human), Lincoln (0.671 -> unsure).
        "texts": [
            CLEARLY_AI[0],
            # Mark Twain, Adventures of Huckleberry Finn (1884). Public domain.
            "You don't know about me without you have read a book by the name of The "
            "Adventures of Tom Sawyer; but that ain't no matter. That book was made by "
            "Mr. Mark Twain, and he told the truth, mainly. There was things which he "
            "stretched, but mainly he told the truth. That is nothing. I never seen "
            "anybody but lied one time or another, without it was Aunt Polly, or the "
            "widow, or maybe Mary. Aunt Polly - Tom's Aunt Polly, she is - and Mary, and "
            "the Widow Douglas is all told about in that book, which is mostly a true "
            "book, with some stretchers, as I said before.",
            # Abraham Lincoln, Gettysburg Address (1863). Public domain.
            "Four score and seven years ago our fathers brought forth on this continent, "
            "a new nation, conceived in Liberty, and dedicated to the proposition that "
            "all men are created equal. Now we are engaged in a great civil war, testing "
            "whether that nation, or any nation so conceived and so dedicated, can long "
            "endure. We are met on a great battle-field of that war. We have come to "
            "dedicate a portion of that field, as a final resting place for those who "
            "here gave their lives that that nation might live. It is altogether "
            "fitting and proper that we should do this.",
        ],
    },
    {
        "name": "appeal path",
        "criterion": 4,
        # Handled by run_eval.py::run_appeals: submit each, appeal it, check the
        # log. Then appeal an id that was never issued.
        "appeals": [
            "I wrote this paragraph about my weekend for the appeal test.",
            "The bus was late again this morning, so I walked the last mile.",
            "My sister and I argued about whose turn it was to do the dishes.",
            "We planted tomatoes in the spring and most of them came up.",
            "I finished the book on the train and nearly missed my stop.",
        ],
        "fake_ids": ["00000000-0000-0000-0000-000000000000"],
    },
    {
        "name": "bad input",
        "criterion": 5,
        # The cases criterion 5 names, sent as whole bodies.
        "bodies": [
            {"creator_id": "eval_bad_missing"},                   # no text field
            {"text": "", "creator_id": "eval_bad_empty"},
            {"text": "     ", "creator_id": "eval_bad_spaces"},
            {"text": "word " * 4001, "creator_id": "eval_bad_huge"},  # 20,005 chars
            {"text": None, "creator_id": "eval_bad_null"},
        ],
    },
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if scenario.get("appeals"):
            # Criterion 4's own shape: texts to submit and then appeal.
            continue

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
