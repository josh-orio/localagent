# Daily Reporting Task Instructions

**Objective:** Generate a daily report covering weather, stocks, and global news, then compile and email it.

**Execution Steps:**
1.  **Weather Report Generation:**
    *   Generate a 12-hour weather forecast using current coordinates.
    *   The report must include:
        *   Current conditions (temperature and windspeed).
        *   A summary of expected changes (temperature evolution, wind changes, and any adverse weather).

2.  **SPY & VOO Reports:**
    *   For both SPY and VOO, report the following metrics: Open, High, Low, Close, and Volatility.
    *   Include all important news stories associated with each symbol.
    *   **Constraint:** Eliminate duplicate news stories. Each story must include a URL.

3.  **Global News Fetching:**
    *   Fetch news from `bbc.com/news` using `ofetch("bbc.com/news")`.
    *   Filter the results to include only stories that may impact markets or global relations, excluding insignificant topics (e.g., sports, missing pets).
    *   Format: Title - Byline (omit source).

4.  **Finalization and Delivery:**
    *   **Compilation:** Compile all generated reports into a single plain text body.
    *   **Delivery:** Send the final report using the `notify` function to [withheld].
    *   **Email Details:**
        *   Subject: "Daily Report"
        *   Body: The compiled plain text report.

---

## Required Report Structure

Weather (Area name)
    Current conditions: temperature and windspeed
    Forecast summary: temperature evolution, wind changes, and adverse weather

---

S&P 500 Report
    Metrics: Open, High, Low, Close, Volatility
    News:
    1. Title - Summary (url)
    ...
    n. Title - Summary (url)

---

VOO Report
    Metrics: Open, High, Low, Close, Volatility
    News:
    1. Title - Summary  (url)
    ...
    n. Title - Summary  (url)

---

BBC News Stories
    1. Title - Summary  (url)
    ...
    n. Title - Summary  (url)
