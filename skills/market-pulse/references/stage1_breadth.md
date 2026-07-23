# Stage 1: Market Breadth (Background & Consensus)

## Objective
Identify the broad market consensus, market temperature, and the overarching narratives driving the day's action, while filtering out noise using professional investment logic.

## Execution Steps

1. **Macro & Heat Recap:**
   - How is the market overall today? (Evaluate macro, market heat, major indices, and sector performance).
   - Is the macro environment favorable for equities right now?
   - What is the market actively focusing on? How concentrated is this attention?

2. **The "Biggest Thing" & Emerging Themes:**
   - Identify the single biggest narrative/event in the market today, and emerging themes that might become trends in 1-3 months.
   - **Reverse Attribution:** Price surges or news hype are surface-level. Identify the real event capital is using as an excuse.
   - **2nd-Order Effects:** Good opportunities often lie in second-order transmission chains. Search deeper if necessary.

3. **Filter and Score via Investment Logic (投资逻辑):**
   Evaluate the raw events and themes against these criteria to find what truly matters:
   - **Capital Volume:** Does it affect massive industry capital or support massive capital deployment?
   - **Rarity:** Is it a major, rare opportunity?
   - **Foresight (CRITICAL):** Facts precede expectations, expectations precede prices. Identify the current stage (Early Stage / Hidden Stage / Trend Stage).
   - **Risk/Reward:** Is it a perfect storm (high certainty, early timing, mild capital validation) or just a good risk/reward?
   - **Scoring System:** Score the finalized themes based on:
     - *Capital Potential (资金盘潜力):* 5: 全盘狂欢, 4: 行业共振, 3: 大象起舞, 2: 中市值妖股制造机, 1: 市场边角料
     - *Game Stage (博弈阶段):* +1 (Left-side layout, early bird), 0 (Trend just starting), -1 (Already crowded)

4. **Under-priced Opportunities:**
   - Outside of the "Biggest Thing," what else is noteworthy but under-reacted to by the market based on the logic above?

## Search Strategy (Breadth)
- **Strict Time Limits:** Use `web_search` with `freshness="day"` or explicitly include today's date to get closing summaries (e.g., "A股 收评", "A股 复盘", "资金流").
- **Timestamp Verification:** Internally check the exact publication time of the events. Discard morning news that actually recaps *yesterday's* market.

## Output for Stage 1
Compile the answers and scores to the above points. Do not present this directly to the user as the final deliverable; hold it in your `<think>` block or output it as a raw intermediate summary to transition into Stage 2.