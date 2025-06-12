# USA Flights Data Analysis – 2015

## Problem Statement

This dataset contains records for over 5,000,000 commercial airline flights in 2015, compiled by the U.S. Department of Transportation (DOT) for the Air Travel Consumer Report. Each record includes details such as airline name, flight number, origin and destination airports, flight distance, scheduled and actual departure/arrival times, and delay information.

## Project Objective 🎯

The goal of this project is to perform an in-depth analysis of flight data across all major U.S. airports and routes in 2015. By identifying patterns in flight delays, route performance, and airport efficiency, the project helps uncover valuable insights to support data-driven decision-making in the aviation industry.


🧰 Step-by-Step Tools & Process Section:

#### Step 1: Importing Data from Kaggle using API Credentials

**Tools Used:** Python

We automated the data retrieval process using Kaggle API tokens. This allowed us to seamlessly update the dataset by executing a Python script whenever new data is available.

📌 Script Example:

![Kaggle Python Script](https://github.com/esraamorsy131/USA-Flights-Projects/blob/main/Python%20Script.PNG)

    
  
### Step 2: Data Cleaning & Transformation

**Tools Used:** Power Query (Excel / Power BI)

- Removed missing and inconsistent values.
- Standardized column formats, especially time fields.
- Added calculated columns such as flight delay duration.
- Handled time zone differences to accurately compute scheduled vs actual times.

#### Step 3: Data Modeling

**Tools Used:** Power BI

We structured the data using a **star schema** to improve performance and simplify relationships between facts and dimensions. We leveraged **active/inactive relationships** to support advanced time intelligence using DAX.

### Step 4: Data Visualization & Reporting

**Tools Used:** Power BI, DAX

- Developed multiple interactive dashboards focused on airlines, airports, delay patterns, and detailed performance metrics.
- Used DAX for dynamic calculations and advanced KPIs.
- Enabled real-time filtering and drill-down insights for stakeholders.

🔗 **Interactive Dashboard Link**:  
[View in Power BI](https://app.powerbi.com/view?r=eyJrIjoiOWE1NDg0NjEtYTcwOS00OTU4LTlkNzEtZjhlM2U0NmIxYmY1IiwidCI6ImVhZjYyNGM4LWEwYzQtNDE5NS04N2QyLTQ0M2U1ZDc1MTZjZCIsImMiOjh9)



## Data Model

![Data Model](https://github.com/esraamorsy131/USA-Flights-Projects/blob/main/Model%20Diagram.PNG)

## Dashboards Preview

### Summary Dashboard  
![Summary](https://github.com/esraamorsy131/USA-Flights-Projects/blob/main/Summary%20Dashboard.PNG)

### Airlines Dashboard  
![Airlines](https://github.com/esraamorsy131/USA-Flights-Projects/blob/main/Airlines%20Dahboard.PNG)

### Airport Dashboard  
![Airports](https://github.com/esraamorsy131/USA-Flights-Projects/blob/main/Airport%20Dahboard.PNG)

### Delay Time Details  
![Delays](https://github.com/esraamorsy131/USA-Flights-Projects/blob/main/Detailed%20Delay%20Time%20Dashboard.PNG)


