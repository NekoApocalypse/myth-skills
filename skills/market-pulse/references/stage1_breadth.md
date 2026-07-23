# Stage 1: Market Breadth (Background & Consensus)

## Objective
Identify the broad market consensus, market temperature, and the overarching narratives driving the day's action.

## Execution Steps

1. **Macro & Heat Recap:**
   - How is the market overall today? (Evaluate macro, market heat, major indices, and sector performance).
   - Is the macro environment favorable for equities right now?
   - What is the market actively focusing on? How concentrated is this attention?

2. **The "Biggest Thing":**
   - Identify the single biggest narrative/event in the market today.
   - Analyze it across three time horizons:
     - **Formed Trends:** What is already an established consensus?
     - **New Catalysts:** What are the fresh anomalies or triggers today?
     - **Emerging Themes:** What new narratives or rumors might become major trends in 1-3 months?

3. **Under-priced Opportunities:**
   - Outside of the "Biggest Thing," what else is noteworthy but under-reacted to by the market?

## Search Strategy (Breadth)
- **Strict Time Limits:** Use `web_search` with `freshness="day"` or explicitly include today's date to get closing summaries (e.g., "A股 收评", "A股 复盘", "资金流"). Physically eliminate old news.
- **Timestamp Verification:** Even with `freshness` enabled, internally check the exact publication time of the events. Discard news from the morning that actually recaps *yesterday's* market.
- **Focus:** The recap provides the baseline, but true alpha comes from discovering the latest catalysts, rumors, and resonances.

## Output for Stage 1
Compile the answers to the above points. Do not present this directly to the user as the final deliverable; hold it in your `<think>` block or output it as a raw intermediate summary to transition into Stage 2.