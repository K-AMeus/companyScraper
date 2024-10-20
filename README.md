# Estonian Company Scraper

A full-stack application built with Flask (Python) and Angular for scraping personnel, press news, and company activities. Users can input the name of an Estonian company, select a time range (last 3 months, 6 months, or 1 year), and the app generates a detailed 2-page report summarizing the company's personnel and recent events.

**_Note: This project is currently under development._**

## Project Overview

This project allows users to scrape and gather information about Estonian companies. By entering a company's name, the application retrieves:

- Personnel information
- Press news
- Recent activities within the last 3 months, 6 months, or 1 year

The result is a two-page PDF report that summarizes the company's details and recent events, helping professionals such as account managers and client relationship managers quickly stay updated on key companies.

## Technologies

### Backend
- **Flask (Python):** For handling API routes and scraping logic.
- **BeautifulSoup/Scrapy:** For scraping web content.
- **Google Search JSON API** for scraping google results.

### Frontend
- **Angular:** For handling user input, sending requests, and displaying results.
- **TypeScript:**

### Database
- **PostgreSQL:** Stores scraped data for future reference and historical comparison.
