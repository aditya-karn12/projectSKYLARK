# Decision Log

## 1. Assumptions and interpretation

We interpreted the assignment as a prototype for a founder-facing BI agent that can answer strategic questions using operational project data and sales pipeline data. Since the project only provided local Excel exports and no live Monday.com credentials, the design assumes a read-only architecture where the app can work from local files by default and can switch to Monday.com if an API key and board IDs are configured. We also assumed the user wants a solution that is useful without endless setup, so we prioritized a working prototype over a fully production-grade system.

## 2. Trade-offs chosen

We used a pragmatic mix of a FastAPI backend and a Streamlit front end. This keeps the app easy to run locally and test quickly while still supporting a real API layer for future scaling. We used Python and pandas because the dataset is spreadsheet-driven and messy, which makes this toolchain a natural fit. The BI layer is intentionally rule-based rather than fully language-model driven because we wanted predictable, explainable answers under the time constraint and without external API access.

We also chose to separate the data contract from the source system. In practice, the app normalizes workbook fields into a common schema before running the analytics layer. That means the same logic can support Monday.com rows or local spreadsheets without rewriting the business logic. This is the right trade-off for a six-hour assignment: lower technical risk, faster iteration, and a cleaner evaluation experience.

## 3. Handling messy data

The real-world spreadsheets contain missing values, inconsistent capitalization, multiple label names, and numeric text embedded in strings. We normalized to a resilient pattern: treat missing values as `Unknown` for text and as zero for numeric fields when they are not recoverable. We flagged quality issues in the UI instead of silently hiding them. This is important because founder questions are often strategic, and the leader should know when the data quality is limiting the answer.

## 4. Leadership updates interpretation

For the “leadership updates” requirement, we interpreted this as an executive-ready summary that blends pipeline, revenue, collections, and sector performance into a short decision-oriented narrative. The app can surface a headline summary with top sectors, risk flags, and digits that are easy to understand in a meeting. This gives a better answer than raw numbers alone.

## 5. What we would do with more time

If we had more time, we would do three things:

1. Add a true LLM planning layer with OpenAI/Azure OpenAI to convert free-form founder questions into structured analytical steps.
2. Build a full field-mapping schema for Monday.com so each board column is mapped semantically, not just by name.
3. Add richer reporting exports, dashboards, and downloadable summaries for leadership decks.

## 6. Final assessment

This prototype is designed to be clear, explainable, and deployable quickly. It does not pretend to be a full enterprise BI platform, but it is a credible first version: it reads real data, handles messy fields, answers founder-level questions, and communicates quality caveats without breaking on bad rows.
