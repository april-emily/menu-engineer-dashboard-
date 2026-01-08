# The Menu Engineer: Interactive Profitability Dashboard

Author: April Williams  
Status: Active / Demo Ready  
Tech Stack: Python, Streamlit, Pandas, Plotly

## Overview

The Menu Engineer is an interactive Business Intelligence tool designed to help hospitality managers optimise their menu profitability.

Drawing on the classic "Menu Engineering" matrix, this dashboard visualises the relationship between Item Popularity (Volume) and Profitability (Contribution Margin). It automatically categorises menu items into four strategic segments to guide decision-making:

* 🌟 Stars: High Profit, High Popularity (Promote & Protect)  
* 🐴 Plowhorses: Low Profit, High Popularity (Increase Price/Reduce Cost)  
* 🧩 Puzzles: High Profit, Low Popularity (Rebrand/Market)  
* 🐕 Dogs: Low Profit, Low Popularity (Remove/Rethink)

## Key Features

* Interactive Matrix: A quadrant-based scatter plot built with Plotly to visualise menu performance instantly.  
* Scenario Planning: Sidebar sliders allow users to simulate "What-If" scenarios (e.g., *"What happens to my margins if ingredient costs rise by 5%?"*).  
* Custom Data Upload: Users can upload their own sales data (CSV) to analyse real-world menus, or use the built-in demo data generator.  
* Actionable Insights: Automatic classification logic provides specific recommendations for each menu item.

## Repository Structure

* app.py: The main Streamlit application code.  
* generate\_data.py: A Python script to generate realistic dummy data for testing.  
* menu\_data.csv: Pre-generated sample data (created by the script above).  
* requirements.txt: List of dependencies required to run the app.

## How to Run Locally

1. Clone this repository:  
   git clone (https://github.com/your-username/menu-engineering-dashboard.git)  
   cd menu-engineering-dashboard-

2. Install dependencies:  
   pip install \-r requirements.txt

3. Run the app:  
   streamlit run app.py

4. View the Dashboard:  
   The app will open automatically in your browser at http://localhost:8501.

## Data Structure

If uploading your own data, the CSV file must contain the following columns:

* Item: Name of the dish (String)  
* Category: e.g., Breakfast, Lunch, Coffee (String)  
* Sales\_Price: Price sold to customer (Number)  
* Cost\_Price: Cost of goods sold/COGS (Number)  
* Number\_Sold: Quantity sold in a given period (Number)

*This project was developed as part of a professional portfolio demonstrating the application of Data Analytics to real-world Operational Management challenges.*
