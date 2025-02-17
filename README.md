# File: README.md
# Cedars-Sinai Job Scraper

A Python web scraper script that extracts job listings from Cedars-Sinai's career website and exports them to CSV.

## Features
- Scrapes detailed job information including:
  - Job title, location, and department
  - Req ID and working title
  - Business entity and job category
  - Job specialty and overtime status
  - Shift information and base pay
  - Full job description and qualifications
- Exports data to CSV with timestamp


## Requirements
```
beautifulsoup4>=4.9.3
requests>=2.25.1
```


The script will:
1. Scrape all available jobs from the Cedars-Sinai careers website
2. Show progress in the console
3. Create a CSV file with timestamp (e.g., `cedars_sinai_jobs_20250217_123456.csv`)

## Output
The CSV file includes the following columns:
- Title
- Location
- Department
- URL
- Description
- Qualifications
- Req ID
- Working Title
- Business Entity
- Job Category
- Job Specialty
- Overtime Status
- Primary Shift
- Shift Duration
- Base Pay





