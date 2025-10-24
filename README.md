# Competitor-Analysis-Dashboard


Project overview
This project tracks competitor data to compare digital marketing efforts, identify trends, and uncover opportunities. Students will build dashboards (Power BI or Excel) to visualize competitor performance across traffic, social, ads, and SEO metrics.

What’s included
- data/sample_competitor_data.csv — CSV template with example competitors
- scripts/collect_data.py — data-collection script skeleton (placeholders for APIs)
- powerbi/DAX_measures.md — common DAX measures and examples

High-level steps
1. Research and list competitors in data/sample_competitor_data.csv.
2. Provide API keys or credentials (SimilarWeb, SEMrush/Ahrefs, Google Analytics, Facebook/Meta Graph, Google Ads).
3. Run the data collection script to create an aggregated CSV (data/competitor_metrics.csv).
4. Load the aggregated CSV into Power BI or Excel and create visuals:
   - Market share (visits / total visits)
   - Growth rates (month-over-month, year-over-year)
   - Social engagement (likes, comments, shares, engagement rate)
   - SEO metrics (organic traffic, top keywords, SERP positions)
   - Ad metrics (estimated spend, impressions, CTR)
5. Analyze and document strengths, weaknesses, and opportunities.

Data sources (examples)
- SimilarWeb / Alexa (website traffic and referrals)
- SEMrush / Ahrefs / Moz (organic keywords, backlinks, ranking)
- Google Analytics (if you have access for your domain)
- Social platforms (Facebook Graph API, Twitter API / X API, Instagram APIs)
- Google Ads / Meta Ads (ad spend estimates, creative analytics)

Running the sample script
1. Create a Python virtualenv and install dependencies:
   python -m venv .venv
   source .venv/bin/activate
   pip install pandas requests python-dotenv

2. Create a `.env` file in the repo root with keys (example):
   SIMILARWEB_API_KEY=your_key
   SEMRUSH_API_KEY=your_key
   FACEBOOK_TOKEN=your_token
   GOOGLE_ANALYTICS_VIEW_ID=your_view_id
   OUTPUT_PATH=data/competitor_metrics.csv

3. Populate `data/sample_competitor_data.csv` with competitor rows.

4. Run:
   python scripts/collect_data.py

This script is a skeleton — replace placeholder fetch_xxx functions with real API calls.

Power BI tips
- Model: keep a fact table (competitor metrics by date) and a dimension table for competitors.
- Use calculated measures for market share and growth rates (see powerbi/DAX_measures.md).
- Use slicers for date range, market/country, or industry.
- Consider creating a composite index (weighted score) to rank competitors across channels.

Suggested repo issues
- Implement SimilarWeb connector
- Implement SEMrush / Ahrefs connector
- Add GitHub Actions to run the data collection weekly
- Build initial Power BI report with top-level KPIs and an overview page

License and contributors
Add a LICENSE file if needed, and list contributors in a CONTRIBUTORS.md if this is a group project.
