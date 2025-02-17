import requests
from bs4 import BeautifulSoup
import time
import csv
from datetime import datetime

def extract(page):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.2 Safari/605.1.15'}
    url = f'https://careers.cshs.org/search-jobs'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def get_job_details(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.2 Safari/605.1.15'}
    try:
        r = requests.get(url, headers)
        job_soup = BeautifulSoup(r.content, 'html.parser')
        
        
        description = job_soup.find('div', class_='job-details__description-content')
        qualifications = job_soup.find_all('div', class_='job-details__description-content')[1]
        reg_id = job_soup.find('b', text='Req ID')
        working_title = job_soup.find('b', text='Working Title')
        department = job_soup.find('b', text='Department')
        business_entity = job_soup.find('b', text='Business Entity')
        job_category = job_soup.find('b', text='Job Category')
        job_specialty = job_soup.find('b', text='Job Specialty')
        overtime_status = job_soup.find('b', text='Overtime Status')
        primary_shift = job_soup.find('b', text='Primary Shift')
        shift_duration = job_soup.find('b', text='Shift Duration')
        base_pay = job_soup.find('b', text='Base Pay')

        details = {
            'description': description.text.strip() if description else "Not found",
            'qualifications': qualifications.text.strip() if qualifications else "Not found",
            'req_id': reg_id.find_next_sibling(text=True).strip().lstrip(': ') if reg_id else "Not found",
            'working_title': working_title.find_next_sibling(text=True).strip().lstrip(': ') if working_title else "Not found",
            'department': department.find_next_sibling(text=True).strip().lstrip(': ') if department else "Not found",
            'business_entity': business_entity.find_next_sibling(text=True).strip().lstrip(': ') if business_entity else "Not found",
            'job_category': job_category.find_next_sibling(text=True).strip().lstrip(': ') if job_category else "Not found",
            'job_specialty': job_specialty.find_next_sibling(text=True).strip().lstrip(': ') if job_specialty else "Not found",
            'overtime_status': overtime_status.find_next_sibling(text=True).strip().lstrip(': ') if overtime_status else "Not found",
            'primary_shift': primary_shift.find_next_sibling(text=True).strip().lstrip(': ') if primary_shift else "Not found",
            'shift_duration': shift_duration.find_next_sibling(text=True).strip().lstrip(': ') if shift_duration else "Not found",
            'base_pay': base_pay.find_next_sibling(text=True).strip().lstrip(': ') if base_pay else "Not found"
        }
        return details
    except Exception as e:
        print(f"Error fetching URL {url}: {e}")
        return None

def transform(soup):
    jobs = []
    section = soup.find('section', id='search-results-list')
    if section:
        listings = section.find_all('li')
        for item in listings:
            title_element = item.find('h2')
            if title_element:
                title = title_element.text.strip()
                location_element = item.find('span', class_='job-location')
                location = location_element.text.strip() if location_element else "Location not specified"
                department_element = item.find('i', class_='cat2')
                department = department_element.text.strip() if department_element else "Department not specified"
                
                url_element = item.find('a')
                job_url = url_element['href'] if url_element else "URL not found"
                if job_url and not job_url.startswith('http'):
                    job_url = 'https://careers.cshs.org' + job_url

                print(f"\nFetching details for: {title}")
                details = get_job_details(job_url)
                
                if details:
                    job = {
                        'title': title,
                        'location': location,
                        'department': department,
                        'url': job_url,
                        'description': details['description'],
                        'qualifications': details['qualifications'],
                        'req_id': details['req_id'],
                        'working_title': details['working_title'],
                        'business_entity': details['business_entity'],
                        'job_category': details['job_category'],
                        'job_specialty': details['job_specialty'],
                        'overtime_status': details['overtime_status'],
                        'primary_shift': details['primary_shift'],
                        'shift_duration': details['shift_duration'],
                        'base_pay': details['base_pay']
                    }
                else:
                    job = {
                        'title': title,
                        'location': location,
                        'department': department,
                        'url': job_url,
                        'description': "Not available",
                        'qualifications': "Not available",
                        'req_id': "Not available",
                        'working_title': "Not available",
                        'business_entity': "Not available",
                        'job_category': "Not available",
                        'job_specialty': "Not available",
                        'overtime_status': "Not available",
                        'primary_shift': "Not available",
                        'shift_duration': "Not available",
                        'base_pay': "Not available"
                    }
                
                jobs.append(job)
                
               
                print(f"Title: {title}")
                print(f"Location: {location}")
                print("-" * 50)
                
    return jobs

def export_to_csv(jobs):
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f'cedars_sinai_jobs_{timestamp}.csv'
    
    fieldnames = [
        'title', 'location', 'department', 'url', 'description', 'qualifications',
        'req_id', 'working_title', 'business_entity', 'job_category', 
        'job_specialty', 'overtime_status', 'primary_shift', 'shift_duration', 'base_pay'
    ]
    
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            
            for job in jobs:
                writer.writerow(job)
        
        print(f"\nSuccessfully exported {len(jobs)} jobs to {filename}")
        return filename
    except Exception as e:
        print(f"Error exporting to CSV: {e}")
        return None

def main():
    print("Starting job scraping process...")
    
    soup = extract(0)
    jobs = transform(soup)
    
    print(f"\nTotal jobs found: {len(jobs)}")
  
    if jobs:
        exported_file = export_to_csv(jobs)
        if exported_file:
            print(f"Data has been exported to: {exported_file}")
    else:
        print("No jobs were found to export.")

if __name__ == "__main__":
    main()