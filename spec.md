# SRS for Product Data Pool + Odoo

![image](https://user-images.githubusercontent.com/7826363/235072695-37408f28-923c-469d-9934-01fcf959e165.png)

## 1. Introduction
This document describes the software requirements for the development of a two-part application for collecting product data from various large online shops and pooling it into a single large database called the "Product Data Pool". 
The application will integrate with Odoo and allow users to search for products and allow them to add specific products to their Odoo product catalog.

## 2. System Overview

### 2.1 Data Pool
The data pool is a MySQL database that stores product data from large wholesalers. The data is obtained from Sources (wholesaler websites) via three input mechanisms:

1. **CSV file uploads**: Wholesalers can provide a CSV file which can be uploaded over FTP or HTTP interfaces.
2. **API connections**: Each wholesaler has a dedicated API script to draw data from specific endpoints with proper authentication.
3. **Web scraping**: Custom web scrapers are written to scrape product data from different websites according to their structure.

### 2.2. Odoo Module
The Odoo module provides a user interface for searching the data pool and selecting products to add to the Odoo product catalog. The module communicates with the data pool via a REST API.

See section 5 below.

# 3. Data Pool Flask Application

## 3.1. Introduction

The Data Pool Flask application is a web-based application that consolidates product data from various large online shops into a single large database called the PDP. The application provides an interface to manage sources of data, users, and upload product data through CSV files. Admin users can add, edit, and deactivate sources, while authenticated users can upload CSV files and provide their API credentials to connect to Sources.

## 3.2. Features

### 3.2.1. Authentication

- Admin login using a master password
- Regular user login using a username and password

### 3.2.2. User Management

- Admins can create, edit, and view users
- Admins can grant or revoke admin access to users

### 3.2.3. Source Management

- Admins can add, edit, and deactivate sources
- Each source has an ID, URL, name, city, and postal code

### 3.2.4. CSV File Upload

- Authenticated users can upload CSV files containing product data
- CSV files are parsed and stored in the MySQL database
- CSV files structures differ for Sources

### 3.2.5. REST API

- A REST API is provided to access the data pool (for example from an Odoo instance)
- API authentication using an API key

## 4. Database Schema

### 4.1. Product Table

- Stores product data for photovoltaic components
- 10 most important fields for photovoltaic components
- Includes a last updated timestamp

### 4.2. Manufacturer Table

- Stores manufacturer data
- Includes a name and an ID

### 4.3. Source Table

- Stores the source of the data, typically a website
- Fields include ID, URL, name, city, and postal code
- Includes a last updated timestamp and an active status

## 4.4. Technologies

- Python Flask for the web application
- MySQL for the database
- SQLAlchemy as the Object Relational Mapper (ORM)
- WTForms for form handling
- Jinja2 for HTML templating
- REST API for data access

## 4.5. Installation and Setup

- Python 3.x
- MySQL Server
- Required Python packages (Flask, Flask-SQLAlchemy, Flask-WTF, etc.)
- Configuration files for database credentials and master password

## 4.6. Future Scope

- Support for additional input mechanisms such as API connections and web scraping
- Additional features and improvements to the REST API
- Expansion of the data model to support more product types and fields

# 5. Odoo Module

## 5.1 Search Feature
- The module must provide a search bar for users to search by keyword.
- The module must display search results in a standard Odoo list view.
- The list view must include columns for the article number, title, manufacturer, price (if available), and an "Add to catalog" button (5.3).

## 5.2 Product Details Pop-up
- The module must allow users to click on a search result and open a pop-up with further product details.
- The pop-up must display an image (if available), long descriptions, technical parameters, etc.
- A link to the original website is provided in the popup.

## 5.3 Add to Catalog
- The module must allow users to add products to their Odoo product catalog (product.product) by clicking the "add to catalog" button.

## 5.4. Pricing

1. It is not allowed to store prices in the PDP application, due to contractual and legal restrictions.
2. Prices are not available publicly on the Source websites. 
3. Odoo user company has the legal/contractual rights to obtain pricing-data from Sources directly (bypassing the PDP).
4. Odoo user company can obtain a username and password to Source website, in order to read pricing from respective website.
    1. This is purchase pricing (stored on the product for specific vendor).
    2. Login with the username/password with the respective scraper FROM ODOO, obtain price value and store in related Odoo field.
    3. Store currency.
    4. Show pricing in default currency of Odoo. Use default currency exhange mechanism in Odoo.
    5. Pricing can of course be different per Source/Vendor.
    6. Do not store username/password on PDP.
    7. User/Pass to Sources can be stored in Contact > Website-login (new tab)

### Coding Practice

- Write the scraper login code only once (DRY principle).

# 6. Non-Functional Requirements

## 6.1 Performance
- The system must be able to handle a large number of products in the data pool.
- The system must provide fast and efficient search results.

## 6.2 Scalability
- The system must be able to accommodate new wholesalers (Sources) and their data input mechanisms.
- The system must be able to handle a growing number of users and concurrent searches.

## 6.3 Security
- The system must ensure secure data storage and transfer.
- The system must enforce proper authentication for API connections and data access.

## 6.4 Maintainability
- The system must be easy to update and maintain.
- The system must support the addition of new features and enhancements without significant rework.

# 7. System Architecture
The system architecture consists of two main components: 

1. the Product Data Pool and 
2. the Odoo Module. 

The data pool is a MySQL database with associated Python scripts for data manipulation. The Odoo module communicates with the Data Pool via a REST API.

# 8. Languages

1. Odoo module and PDP are multilingual.
2. Translations can be maintained in language-files on command-lines/code-editor.


