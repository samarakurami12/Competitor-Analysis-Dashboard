#!/usr/bin/env python3
"""
scripts/collect_data.py

Skeleton script to read a list of competitors and fetch metrics from multiple sources.
Replace placeholder functions with real API calls.

Outputs:
- data/competitor_metrics.csv
"""

import os
import csv
import time
from datetime import datetime
from dotenv import load_dotenv
import pandas as pd
import requests

load_dotenv()

# Config from ENV
SIMILARWEB_API_KEY = os.getenv("SIMILARWEB_API_KEY", "")
SEMRUSH_API_KEY = os.getenv("SEMRUSH_API_KEY", "")
FACEBOOK_TOKEN = os.getenv("FACEBOOK_TOKEN", "")
GOOGLE_ANALYTICS_VIEW_ID = os.getenv("GOOGLE_ANALYTICS_VIEW_ID", "")
OUTPUT_PATH = os.getenv("OUTPUT_PATH", "data/competitor_metrics.csv")

INPUT_COMPETITORS = "data/sample_competitor_data.csv"


def read_competitors(path=INPUT_COMPETITORS):
    df = pd.read_csv(path)
    return df.to_dict(orient="records")


def fetch_similarweb(domain):
    """
    Placeholder: fetch traffic estimates from SimilarWeb.
    Replace with actual API call and parsing.
    Example fields returned:
    {
      "visits": 123456,
      "bounce_rate": 0.45,
      "avg_visit_duration_seconds": 180,
      "pages_per_visit": 3.2
    }
    """
    # Example: simulate data for now
    time.sleep(0.1)
    return {
        "visits": int(10000 + (hash(domain) % 50000)),
        "bounce_rate": round(0.3 + ((hash(domain) % 40) / 200), 2),
        "avg_visit_duration_seconds": int(60 + (hash(domain) % 300)),
        "pages_per_visit": round(1.5 + ((hash(domain) % 50) / 20), 2),
    }


def fetch_seo_metrics(domain):
    """Placeholder: use SEMrush/Ahrefs/Moz to get organic traffic and keyword count."""
    time.sleep(0.1)
    return {
        "organic_visits": int(2000 + (hash(domain) % 20000)),
        "top_keywords": int(50 + (hash(domain) % 500)),
        "backlinks": int(100 + (hash(domain) % 5000)),
    }


def fetch_social_metrics(domain_or_handle):
    """Placeholder: fetch social engagement aggregated across channels."""
    time.sleep(0.05)
    return {
        "social_followers": int(500 + (hash(domain_or_handle) % 20000)),
        "social_posts_last_30d": int(1 + (hash(domain_or_handle) % 60)),
        "social_engagement_last_30d": int(10 + (hash(domain_or_handle) % 5000)),
    }


def fetch_ads_estimates(domain):
    """Placeholder: estimate ad spend/impressions from public tools or APIs."""
    time.sleep(0.05)
    return {
        "estimated_ad_spend_usd": float((hash(domain) % 10000) / 100),
        "ad_impressions_last_30d": int(1000 + (hash(domain) % 100000)),
        "ad_clicks_last_30d": int(50 + (hash(domain) % 5000)),
    }


def aggregate_for_competitor(row):
    domain = row.get("domain") or row.get("competitor")
    sw = fetch_similarweb(domain)
    seo = fetch_seo_metrics(domain)
    soc = fetch_social_metrics(domain)
    ads = fetch_ads_estimates(domain)

    aggregated = {
        "date_collected": datetime.utcnow().strftime("%Y-%m-%d"),
        "competitor": row.get("competitor"),
        "domain": domain,
        "country": row.get("country", ""),
        "industry": row.get("industry", ""),
        "notes": row.get("notes", ""),
        # SimilarWeb
        "visits": sw["visits"],
        "bounce_rate": sw["bounce_rate"],
        "avg_visit_duration_seconds": sw["avg_visit_duration_seconds"],
        "pages_per_visit": sw["pages_per_visit"],
        # SEO
        "organic_visits": seo["organic_visits"],
        "top_keywords": seo["top_keywords"],
        "backlinks": seo["backlinks"],
        # Social
        "social_followers": soc["social_followers"],
        "social_posts_last_30d": soc["social_posts_last_30d"],
        "social_engagement_last_30d": soc["social_engagement_last_30d"],
        # Ads
        "estimated_ad_spend_usd": ads["estimated_ad_spend_usd"],
        "ad_impressions_last_30d": ads["ad_impressions_last_30d"],
        "ad_clicks_last_30d": ads["ad_clicks_last_30d"],
    }
    return aggregated


def main():
    competitors = read_competitors()
    rows = []
    print(f"Found {len(competitors)} competitors — collecting metrics...")
    for r in competitors:
        print(f"Collecting for {r.get('competitor')} ({r.get('domain')})")
        try:
            agg = aggregate_for_competitor(r)
            rows.append(agg)
        except Exception as e:
            print(f"Error collecting for {r.get('domain')}: {e}")

    if not rows:
        print("No data collected — exiting.")
        return

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    df = pd.DataFrame(rows)
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"Wrote aggregated metrics to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()