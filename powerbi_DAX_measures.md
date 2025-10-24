# Power BI / DAX measures (examples)

Below are common measures you can use in Power BI. Replace 'Facts' with your fact table name and column names to match your model.

1) Totals
Total Visits = SUM(Facts[visits])

Total Organic Visits = SUM(Facts[organic_visits])

2) Market share (by visits)
Market Share (%) =
DIVIDE(
    [Total Visits],
    CALCULATE([Total Visits], ALL(Facts[domain])),
    0
)

3) Month-over-Month growth (visits)
Visits MTD = CALCULATE([Total Visits], DATESMTD('Date'[Date]))

Visits MTD Prev = CALCULATE([Total Visits], DATEADD('Date'[Date], -1, MONTH))

Visits MoM Growth % =
DIVIDE(
    [Visits MTD] - [Visits MTD Prev],
    IF([Visits MTD Prev] = 0, BLANK(), [Visits MTD Prev])
)

4) Year-over-Year growth
Visits YoY = 
VAR ThisYear = [Total Visits]
VAR LastYear = CALCULATE([Total Visits], SAMEPERIODLASTYEAR('Date'[Date]))
RETURN DIVIDE(ThisYear - LastYear, LastYear)

5) Engagement rate (social)
Social Engagement Rate =
DIVIDE(
    SUM(Facts[social_engagement_last_30d]),
    SUM(Facts[social_followers]),
    0
)

6) Click-through rate (ads)
Ad CTR % =
DIVIDE(SUM(Facts[ad_clicks_last_30d]), SUM(Facts[ad_impressions_last_30d]), 0)

7) Weighted competitive score (example)
Weighted Score =
VAR VisitsScore = DIVIDE([Total Visits], MAXX(ALL(Facts), [Total Visits]))
VAR SocialScore = DIVIDE(SUM(Facts[social_followers]), MAXX(ALL(Facts), SUM(Facts[social_followers])))
VAR SEOScore = DIVIDE(SUM(Facts[top_keywords]), MAXX(ALL(Facts), SUM(Facts[top_keywords])))
RETURN
0.5 * VisitsScore + 0.3 * SocialScore + 0.2 * SEOScore

Tips
- Keep date table marked as Date table.
- Use calculated columns sparingly; prefer measures for aggregations.
- Normalize metrics when combining channels (z-scores or percent of max) if scales differ.
- Create a competitor dimension for names, regions, segments, and long descriptions.