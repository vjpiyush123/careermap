"""Psychology aptitude test question bank.

Each question is weighted toward specific career streams. The deterministic
scoring engine uses these weights to compute per-stream aptitude scores.
"""

from __future__ import annotations

from careerguide.models.psychology import PsychologyQuestion, PsychologyTest, TestOption


def _q(
    qid: int,
    text: str,
    category: str,
    options: list[tuple[str, dict[str, float]]],
) -> PsychologyQuestion:
    return PsychologyQuestion(
        id=qid,
        text=text,
        category=category,
        options=[TestOption(text=t, stream_weights=w) for t, w in options],
    )


# Shorthand stream name aliases for readability in weight dicts
_ET = "Engineering & Technology"
_MH = "Medical & Healthcare"
_LL = "Law & Legal Studies"
_SR = "Science & Research"
_ED = "Education & Teaching"
_CF = "Commerce, Finance & Business"
_AH = "Arts & Humanities"
_DC = "Design & Creative Arts"
_PA = "Performing & Fine Arts"
_SP = "Sports & Physical Education"
_CS = "Civil Services & Government Services"
_HT = "Hospitality, Travel & Tourism"
_AG = "Agriculture & Environmental Studies"
_DR = "Defence Research"


_QUESTIONS: list[PsychologyQuestion] = [
    # ── Analytical aptitude ──────────────────────────────────────────
    _q(1, "When faced with a complex problem, what is your first instinct?",
        "analytical", [
            ("Break it into smaller parts and solve step by step",
             {_ET: 3.0, _SR: 3.0, _CF: 2.0, _DR: 1.5}),
            ("Look for patterns and connections",
             {_SR: 3.0, _ET: 2.5, _CF: 2.0}),
            ("Discuss with others to get different perspectives",
             {_AH: 2.0, _ED: 2.5, _LL: 2.0, _CS: 1.5}),
            ("Trust my intuition and try a creative approach",
             {_DC: 3.0, _PA: 2.5, _AH: 1.5}),
        ]),
    _q(2, "How do you feel about mathematics?",
        "analytical", [
            ("I love solving equations and proofs",
             {_ET: 3.0, _SR: 3.0, _CF: 2.0}),
            ("I enjoy practical math like budgeting and statistics",
             {_CF: 3.0, _ET: 1.5, _CS: 1.5}),
            ("I prefer logic puzzles over pure math",
             {_LL: 2.0, _SR: 2.0, _ET: 1.5}),
            ("Math is not my strength; I prefer words and visuals",
             {_AH: 2.5, _DC: 2.5, _PA: 2.0, _ED: 1.0}),
        ]),
    _q(3, "Which best describes how you study for exams?",
        "analytical", [
            ("I make detailed notes and diagrams",
             {_ET: 2.0, _MH: 2.0, _SR: 2.5}),
            ("I discuss concepts with friends",
             {_ED: 2.5, _AH: 2.0, _LL: 1.5}),
            ("I memorize facts and formulas",
             {_MH: 2.0, _CF: 1.5, _CS: 1.5}),
            ("I use visual aids, colours, and creative methods",
             {_DC: 3.0, _PA: 2.0, _AH: 1.5}),
        ]),

    # ── Scientific curiosity ────────────────────────────────────────
    _q(4, "How interested are you in how the human body works?",
        "scientific", [
            ("Very — I want to heal people",
             {_MH: 3.0, _SP: 1.5}),
            ("Somewhat — I like biology but not medicine",
             {_AG: 2.5, _SR: 2.0, _MH: 1.0}),
            ("Not much — I prefer machines and technology",
             {_ET: 3.0, _DR: 2.0}),
            ("Not at all — I prefer social or creative fields",
             {_AH: 2.0, _DC: 2.0, _PA: 2.0}),
        ]),
    _q(5, "Which science experiment would excite you the most?",
        "scientific", [
            ("Building a robot",
             {_ET: 3.0, _DR: 2.0}),
            ("Growing plants under different conditions",
             {_AG: 3.0, _SR: 2.0}),
            ("Studying stars and galaxies",
             {_SR: 3.0, _DR: 1.5}),
            ("Mixing chemicals and observing reactions",
             {_MH: 2.0, _SR: 2.5, _AG: 1.5}),
        ]),
    _q(6, "Do you enjoy reading about scientific discoveries?",
        "scientific", [
            ("Yes, especially technology and engineering",
             {_ET: 3.0, _SR: 2.0}),
            ("Yes, especially medical breakthroughs",
             {_MH: 3.0, _SR: 1.5}),
            ("Sometimes, when it relates to environment/nature",
             {_AG: 3.0, _SR: 1.5}),
            ("Not really — I prefer news, stories, or art",
             {_AH: 2.5, _PA: 2.0, _DC: 1.5}),
        ]),

    # ── Social & leadership ─────────────────────────────────────────
    _q(7, "How comfortable are you speaking in front of a group?",
        "social", [
            ("Very comfortable — I enjoy public speaking",
             {_LL: 3.0, _CS: 2.5, _PA: 2.0, _ED: 2.0}),
            ("I can manage but prefer small groups",
             {_ED: 2.0, _CF: 1.5, _MH: 1.0}),
            ("I prefer one-on-one conversations",
             {_MH: 1.5, _AH: 1.5, _DC: 1.0}),
            ("I prefer working alone quietly",
             {_ET: 2.0, _SR: 2.5, _AG: 1.5}),
        ]),
    _q(8, "If you could lead a school project, what would it be?",
        "social", [
            ("Organizing a debate or Model UN",
             {_LL: 3.0, _CS: 2.5, _AH: 2.0}),
            ("Managing the school magazine or website",
             {_DC: 2.0, _AH: 2.5, _ET: 1.5}),
            ("Organising a sports tournament",
             {_SP: 3.0, _HT: 1.5}),
            ("Running a science exhibition or hackathon",
             {_ET: 3.0, _SR: 2.5, _DR: 1.0}),
        ]),
    _q(9, "Which role appeals to you most in a team?",
        "social", [
            ("Leader — I like making decisions",
             {_CS: 3.0, _CF: 2.0, _DR: 2.0}),
            ("Communicator — I explain ideas to others",
             {_ED: 3.0, _AH: 2.0, _LL: 1.5}),
            ("Creator — I come up with new ideas",
             {_DC: 3.0, _ET: 2.0, _PA: 2.0}),
            ("Executor — I get tasks done efficiently",
             {_ET: 2.0, _CF: 2.0, _MH: 1.5, _AG: 1.5}),
        ]),

    # ── Creative aptitude ───────────────────────────────────────────
    _q(10, "How do you spend your free time?",
        "creative", [
            ("Drawing, painting, or crafting",
             {_DC: 3.0, _PA: 2.0}),
            ("Playing music or acting",
             {_PA: 3.0, _DC: 1.5}),
            ("Playing sports or exercise",
             {_SP: 3.0, _DR: 1.0}),
            ("Reading, writing, or debating",
             {_AH: 3.0, _LL: 2.0, _ED: 1.5}),
        ]),
    _q(11, "Which of these would you enjoy creating?",
        "creative", [
            ("A mobile app or game",
             {_ET: 3.0, _DC: 2.0}),
            ("A short film or music video",
             {_PA: 3.0, _DC: 2.0}),
            ("A business plan or investment strategy",
             {_CF: 3.0, _CS: 1.5}),
            ("A garden or eco-friendly project",
             {_AG: 3.0, _SR: 1.5}),
        ]),
    _q(12, "Do you enjoy expressing yourself through art, writing, or performance?",
        "creative", [
            ("Yes — it's my passion",
             {_PA: 3.0, _DC: 2.5, _AH: 2.0}),
            ("Sometimes — when I'm inspired",
             {_AH: 2.0, _DC: 1.5, _ED: 1.0}),
            ("Not really — I prefer structured work",
             {_ET: 2.0, _CF: 2.0, _SR: 1.5}),
            ("No — I prefer physical activity or fieldwork",
             {_SP: 2.5, _AG: 2.0, _DR: 2.0}),
        ]),

    # ── Practical/vocational aptitude ───────────────────────────────
    _q(13, "Would you enjoy spending time in a laboratory?",
        "practical", [
            ("Yes — experiments fascinate me",
             {_SR: 3.0, _MH: 2.5, _AG: 2.0}),
            ("Only if it involves technology/gadgets",
             {_ET: 3.0, _DR: 2.0}),
            ("I prefer an office or studio environment",
             {_CF: 2.0, _DC: 2.0, _AH: 1.5}),
            ("I prefer outdoor activity",
             {_SP: 2.5, _AG: 2.0, _DR: 2.0, _HT: 2.0}),
        ]),
    _q(14, "How do you feel about travelling and meeting new people?",
        "practical", [
            ("Love it — I want a career that involves travel",
             {_HT: 3.0, _PA: 1.5, _CS: 1.0}),
            ("I enjoy it occasionally",
             {_AH: 1.5, _CF: 1.5, _ED: 1.0}),
            ("I prefer a stable location",
             {_ET: 1.5, _SR: 2.0, _MH: 2.0}),
            ("I'm adventurous — military/fieldwork excites me",
             {_DR: 3.0, _SP: 2.0, _AG: 1.5}),
        ]),
    _q(15, "If you had to pick one, which skill would you want to master?",
        "practical", [
            ("Coding and software development",
             {_ET: 3.0, _SR: 1.5}),
            ("Cooking and food science",
             {_HT: 3.0, _AG: 1.5}),
            ("Negotiation and argumentation",
             {_LL: 3.0, _CF: 2.0, _CS: 2.0}),
            ("First aid and medical procedures",
             {_MH: 3.0, _SP: 1.5}),
        ]),

    # ── Values & motivation ─────────────────────────────────────────
    _q(16, "What motivates you the most?",
        "values", [
            ("Making a difference in society",
             {_CS: 3.0, _MH: 2.0, _ED: 2.0, _AH: 1.5}),
            ("Financial success and stability",
             {_CF: 3.0, _ET: 2.0, _LL: 1.5}),
            ("Creative freedom and self-expression",
             {_DC: 3.0, _PA: 3.0, _AH: 2.0}),
            ("Protecting my country",
             {_DR: 3.0, _CS: 2.0}),
        ]),
    _q(17, "Which career environment appeals to you?",
        "values", [
            ("Hospital or clinic",
             {_MH: 3.0}),
            ("Corporate office or bank",
             {_CF: 3.0, _LL: 1.5}),
            ("School, university, or research lab",
             {_ED: 3.0, _SR: 2.5}),
            ("Film set, gallery, or design studio",
             {_PA: 3.0, _DC: 2.5}),
        ]),
    _q(18, "How important is job security to you?",
        "values", [
            ("Very important — I want a government/stable job",
             {_CS: 3.0, _ED: 2.0, _DR: 2.0}),
            ("Somewhat — but I also want growth",
             {_ET: 2.5, _CF: 2.5, _MH: 2.0}),
            ("Not much — I want freedom and creativity",
             {_DC: 3.0, _PA: 2.5, _AH: 2.0}),
            ("I want to build my own business",
             {_CF: 3.0, _HT: 2.0, _ET: 1.5}),
        ]),

    # ── Personality ─────────────────────────────────────────────────
    _q(19, "How would your friends describe you?",
        "personality", [
            ("Logical and methodical",
             {_ET: 2.5, _SR: 2.5, _CF: 2.0}),
            ("Caring and empathetic",
             {_MH: 2.5, _ED: 2.5, _AH: 1.5}),
            ("Bold and adventurous",
             {_DR: 2.5, _SP: 2.5, _HT: 2.0}),
            ("Creative and expressive",
             {_DC: 2.5, _PA: 2.5, _AH: 2.0}),
        ]),
    _q(20, "How do you handle pressure?",
        "personality", [
            ("Stay calm and plan systematically",
             {_ET: 2.0, _SR: 2.0, _CS: 2.5, _DR: 2.0}),
            ("Seek support from others",
             {_ED: 2.0, _AH: 1.5, _MH: 1.5}),
            ("Channel it into physical activity",
             {_SP: 3.0, _DR: 2.0}),
            ("Express it through art/music/writing",
             {_PA: 3.0, _DC: 2.0, _AH: 2.0}),
        ]),
]


def get_psychology_test() -> PsychologyTest:
    """Return the full psychology aptitude test (20 questions)."""
    return PsychologyTest(questions=_QUESTIONS, version="1.0")


def compute_psychology_scores(
    answers: list[tuple[int, int]],
) -> dict[str, float]:
    """Compute per-stream aptitude scores from submitted answers.

    Parameters
    ----------
    answers : list of (question_id, selected_option_index) tuples
        ``selected_option_index`` is 0-based.

    Returns
    -------
    dict mapping stream name → normalised score (0–100).
    """
    test = get_psychology_test()
    question_map = {q.id: q for q in test.questions}

    raw_scores: dict[str, float] = {}
    max_possible: dict[str, float] = {}

    # Compute max possible score per stream (if student picks best option each time)
    for q in test.questions:
        for stream in {s for opt in q.options for s in opt.stream_weights}:
            best = max(
                (opt.stream_weights.get(stream, 0.0) for opt in q.options),
                default=0.0,
            )
            max_possible[stream] = max_possible.get(stream, 0.0) + best

    # Accumulate actual scores
    for qid, opt_idx in answers:
        question = question_map.get(qid)
        if question is None:
            continue
        if opt_idx < 0 or opt_idx >= len(question.options):
            continue
        selected = question.options[opt_idx]
        for stream, weight in selected.stream_weights.items():
            raw_scores[stream] = raw_scores.get(stream, 0.0) + weight

    # Normalise to 0-100
    normalised: dict[str, float] = {}
    for stream in max_possible:
        mp = max_possible[stream]
        if mp > 0:
            normalised[stream] = round((raw_scores.get(stream, 0.0) / mp) * 100, 1)
        else:
            normalised[stream] = 0.0

    return normalised
