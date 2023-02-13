## Scraping Bahamas

<p align="center">
    <img width="400" src="../main/images/bahamas.jpg" alt="cellular">
</p>


## Scraping Bahamas legislation with Scrapy Spider

## Instructions

1. Fork or clone project
2. Create virtual environment

    ``` python3 -m venv env ```
3. Activate virtual environment

    ``` source env/bin/activate ```
4. Dependencies are saved in the Pipfile. To install, run the following command:

    ``` pipenv install ```

## Running scraper

To run the scraper, navigate to the directory containing scrapy.cfg and run the following command:

```scrapy crawl scrapelegislation -o <filename>.json```

You can export data to json or csv.

## Moving between pages

There is no pagination or 'next page' button but there are alphabetical buttons A-Z,
so in the parse method I get all alphabetical button values (A-Z) and add each element
value as a param to the URL.

The updated URL is then sent to the parse_page method which iterates through each
row0 element using the get() method to scrape the title, source_url, and date. The
strip() method is used to remove whitespace.

## Saving data to Amazon AWS S3 Bucket

* Create AWS S3 bucket
* Generate access credentials
* Add and create user
* Install botocore
* Update settings.py with:

```
FEEDS = {
         "s3://scrapy-playbook/%(name)s/%(name)s_%(time)s.jsonl": {
         "format": "jsonlines",
         }
      }
AWS_ACCESS_KEY_ID = 'YOUR_AWS_ACCESS_KEY_ID'
AWS_SECRET_ACCESS_KEY = 'YOUR_AWS_SECRET_ACCESS_KEY'
```
* Scraped data saved in JSON files will now be saved to S3 bucket


## Technologies

* Python 3.8
* Scrapy 2.7

## To do

- Amend loop through tr.row0 to include all rows
- Save data in database
- Integrate with Django 
- Display scraped data on single page app
