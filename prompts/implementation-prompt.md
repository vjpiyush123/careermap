# You are a responsible parent who want to select the subject stream to have the growth career path in future

═══════════════════════════════════
REQUIREMENTS — READ ALL BEFORE CODING
═══════════════════════════════════

The system is defined across a **Masterplan PRD** and **2 supporting PRDs**. You must read ALL of them before writing any code — they are fully cross-referenced. No single PRD contains the full picture.

| PRD | Scope | File |
|-----|-------|------|

| **Masterplan** | Vision, capabilities | `docs/masterplan-prd.md` |
| **UI & Interaction** | User personas, report presentation, explainability, drill-down, baseline comparison UX | `docs/ui-interaction-prd.md` |
| **Student Profile** | Refer [StudentAnalysis](../docs/student_profile.md) | use this for anlaysis
| **Psychology test** | User should go through the psychogy test for better predibility of the subject stream| `docs/psychology_test.md` |
| **Classification of option of stream for student** | Student career options | `docs/careermap-prd.md` |  

You must implement the system exactly as defined across these documents.

═══════════════════════════════════
CRITICAL NON-NEGOTIABLE RULES
═══════════════════════════════════

1. Do NOT assume missing requirements.
2. If anything is ambiguous or missing, STOP and ask clarifying questions before proceeding.
3. Do NOT invent requirements.
4. Do NOT create placeholders or TODOs.
5. Do NOT provide partial implementations within a stage.
6. Every feature in the current stage must be fully implemented before moving to the next.
7. All cross-referenced requirements across documents must be honored.
8. All edge cases defined in the Validation & Quality document must be handled.
9. If a requirement is not implemented, explicitly list it and explain why.

═══════════════════════════════════
TEST-FIRST DEVELOPMENT — MANDATORY
═══════════════════════════════════

This project follows **strict test-first development**. For every stage:

1. **First**: Generate BDD test scenarios (Gherkin `.feature` files) derived from PRD requirements
2. **Second**: Implement step definitions and unit test code that exercises those scenarios
3. **Third**: Run tests — they must FAIL (red) because the implementation does not exist yet
4. **Fourth**: Write the production code to make all tests pass (green)
5. **Fifth**: Refactor if needed — tests must still pass

> **No production code may be written before its corresponding tests exist.**

BDD scenarios are the **executable specification**. They serve as:

- Living documentation of system behavior
- Acceptance criteria verification
- Regression safety net
- Communication bridge between PRD requirements and implementation

Every capability, rule, edge case, and UI interaction in the PRDs must have a corresponding BDD scenario BEFORE the implementation that satisfies it.

═══════════════════════════════════
CORE ARCHITECTURAL INVARIANT
═══════════════════════════════════

This is the #1 design constraint — enforced structurally, not by convention:

> **AI (LLM) never alters analytical conclusions. The deterministic engine must produce complete, correct results without any LLM involvement. LLM enrichment is additive — it generates human-readable narratives from completed deterministic output only.**

- All analytical computations (Career stream , industries , jobs, growth aspects ) are deterministic pure functions. Same input → same output. Always.
- LLM generates only: executive summary narrative, per-entity recommendations, dependency impact explanations.
- If LLM is unavailable: system produces full analysis with template-based fallback narratives. Zero loss of analytical accuracy.
- LLM output is validated before inclusion — every entity key and numeric value mentioned must exist in the deterministic output.

Enforce this boundary at the type/interface level — not by convention.

═══════════════════════════════════
TECH STACK
═══════════════════════════════════

| Component | Technology |
|-----------|------------|

| Language | Python >= 3.13 |
| Pipeline Orchestration | LangGraph (StateGraph) |
| LLM Integration | Local ollama instance | refer [Config](../config/settings.yaml)
| Data Models | Pydantic v2 BaseModel |
| HTTP Client | httpx (async) for external API |
| Output Formats | html report , pdf downloadable |

## UI Deliverable Specificity

The UI is not "a frontend." Each page is a concrete deliverable with specific functionality:

| Page | Route | Must Include |
|------|-------|--------------|

| **Dashboard** | `/` | Summary cards (Number of student done did the analysis, cards based on the Stream of students who did the anlysis)

| **Carrer Options** | `/careeroptions` | Create a tree structure to navigate the different subject stream.

| **Student details** | `/studentdetails` | Create a form to create the student profile & have a option to generate the report based on the career path selected. Give the top 10 college list of that subject stream, top companies hires from that school etc, average salary when you get hired in those companies.

  Student Name
  Standard : 10th , 12th
  Board: State board, CBSE , ICSE etc
  State: in which studies are going on
  Year: Year of studies
  Percentage 10th
  Percentage 12th.
  Student Career path: Maths , Commerce, Biology etc

  Add few more question to understand the psychology of that student which can help you do the good anlaysis to understand which branch can be good for the student.

  save all the data to retrive later point of this, student can generate multiple report for different stream and compare.

| **Analysis** | `/analysis` | Parents / student should have the option to generate the anlaysis report & download

═══════════════════════════════════
Application start stop
═══════════════════════════════════

The Admin should be able to start , stop & get the status of the application.
it should also summarize which AI application is being used.
For start of application should failue its unable to reach the AI application.
Provide the details

- list the PID
- list the log file details

Create a single script to start , stop , status of application
