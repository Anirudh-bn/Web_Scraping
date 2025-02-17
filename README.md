# File: README.md
# Cedars-Sinai Job Scraper

A Python web scraper that extracts job listings from Cedars-Sinai's career website and exports them to CSV.

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

## Installation
1. Clone this repository:
```bash
git clone https://github.com/yourusername/cedars-sinai-scraper.git
cd cedars-sinai-scraper
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage
Run the script:
```bash
python job_scraper.py
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

## License
MIT License

---

# File: requirements.txt
beautifulsoup4>=4.9.3
requests>=2.25.1

---

# File: .gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# CSV files
*.csv

# Virtual Environment
venv/
ENV/

# IDE
.idea/
.vscode/
*.swp
*.swo

---

# File: LICENSE
MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
