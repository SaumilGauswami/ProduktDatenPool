# Software Requirement Specifications

## 1. Introduction
This document describes the software requirements for the development of a two-part application for collecting product data from various large online shops and pooling it into a single large database called the "data pool". The application will integrate with Odoo and allow users to search for products and add them to their Odoo product catalog.

## 2. System Overview

### 2.1 Data Pool
The data pool is a MySQL database that stores product data from large wholesalers. The data is obtained via three input mechanisms:

1. **CSV file uploads**: Wholesalers can provide a CSV file which can be uploaded over FTP or HTTP interfaces.
2. **API connections**: Each wholesaler has a dedicated API script to draw data from specific endpoints with proper authentication.
3. **Web scraping**: Custom web scrapers are written to scrape product data from different websites according to their structure.

### 2.2 Odoo Module
The Odoo module provides a user interface for searching the data pool and selecting products to add to the Odoo product catalog. The module communicates with the data pool via a REST API.

## 3. Functional Requirements

### 3.1 Data Pool

#### 3.1.1 CSV File Upload
- The system must provide FTP or HTTP interfaces for uploading CSV files.

#### 3.1.2 API Connections
- The system must support dedicated API scripts for each wholesaler.
- The system must provide proper authentication for API connections.

#### 3.1.3 Web Scraping
- The system must support custom web scrapers for different websites.

#### 3.1.4 REST API
- The system must provide a REST API for accessing data in the data pool.
- The system must require an API key for authentication.

### 3.2 Odoo Module

#### 3.2.1 Search Feature
- The module must provide a search bar for users to search by keyword.
- The module must display search results in a standard Odoo list view.
- The list view must include columns for the article number, title, manufacturer, price (if available), and an "add to catalog" button.

#### 3.2.2 Product Details Pop-up
- The module must allow users to click on a search result and open a pop-up with further product details.
- The pop-up must display an image (if available), long descriptions, technical parameters, etc.

#### 3.2.3 Add to Catalog
- The module must allow users to add products to their Odoo product catalog by clicking the "add to catalog" button.

## 4. Non-Functional Requirements

### 4.1 Performance
- The system must be able to handle a large number of products in the data pool.
- The system must provide fast and efficient search results.

### 4.2 Scalability
- The system must be able to accommodate new wholesalers and their data input mechanisms.
- The system must be able to handle a growing number of users and concurrent searches.

### 4.3 Security
- The system must ensure secure data storage and transfer.
- The system must enforce proper authentication for API connections and data access.

### 4.4 Maintainability
- The system must be easy to update and maintain.
- The system must support the addition of new features and enhancements without significant rework.

## 5. System Architecture
The system architecture consists of two main components: the data pool and the Odoo module. The data pool is a MySQL database with associated Python scripts for data manipulation. The Odoo module communicates with the data pool via a REST API.
