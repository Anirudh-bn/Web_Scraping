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
2. Show progress in the console as shown in the image below
3. Create a CSV file with timestamp (e.g., `cedars_sinai_jobs_20250217_123456.csv`)

![image alt](https://github.com/Anirudh-bn/Web_Scraping/blob/4d8cda7bb11c59dbd1b36164739debfa7f450f7e/Code_output.jpeg)


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

![image alt](https://github.com/Anirudh-bn/Web_Scraping/blob/061075e997542fa59d222fb39e52de2138c29368/CSV_File.jpeg)





