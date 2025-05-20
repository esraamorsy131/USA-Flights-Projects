# Problem Statement:
Records for 5,000,000+ commercial airline flights in 2015, compiled for the U.S. DOT Air Travel Consumer Report. Each record represents a single flight, including the airline name, flight number, origin/destination airport and flight distance, as well as scheduled/actual departure and arrival times.

# Target
In this project, we perform a comprehensive analysis of all flights in 2015 across all major airports and air routes in the U.S. The goal is to obtain a complete overview of the aviation landscape, enabling us to make informed decisions based on detailed insights into flight patterns, delays, and route performance.
Displaying some insights acording to technical reqirements attached.

# Project Steps and Tools:

## Step1:Importing Data From KAGGLE using Api Credentials Method 

  ### 𝘛𝘰𝘰𝘭𝘴: Python Script 
      Ensuring Data Automation updates using KAGGLE TOKENS , We run Python code every time we need to upload recent data from kaggle.
      
   ## python Script
      
   ![Sales Data Analysis Dashboard](https://github.com/esraamorsy131/USA-Flights-Projects/blob/main/Python%20Script.PNG)

      
  
## Step2:Data Cleaning & Transformation

 ### 𝘛𝘰𝘰𝘭𝘴: 𝘔𝘪𝘤𝘳𝘰𝘴𝘰𝘧𝘵 𝘗𝘰𝘸𝘦𝘳 𝘘𝘶𝘦𝘳𝘺

   Ensuring data accuracy and consistency was crucial. 
         - We cleaned and transformed the data, addressing NULL values and other anomalies. This phase was all about improving data quality and reliability.
         - We adjusted time columns format to add calculated column for delay time and actually dealed with time zones differnces in this case 

## **Step3:𝗗𝗮𝘁𝗮 𝗠𝗼𝗱𝗲𝗹𝗶𝗻𝗴**

  ### 𝘛𝘰𝘰𝘭𝘴: 𝘔𝘪𝘤𝘳𝘰𝘴𝘰𝘧𝘵 𝘗𝘰𝘸𝘦𝘳 𝘉𝘐
  
   Designing a star schema to structure the data for optimal performance and ease of analysis was key. This modeling set the stage for effective and efficient reporting.

## **Step4: 𝗗𝗮𝘁𝗮 𝗩𝗶𝘀𝘂𝗮𝗹𝗶𝘇𝗮𝘁𝗶𝗼𝗻 & 𝗥𝗲𝗽𝗼𝗿𝘁𝗶𝗻𝗴**

  ### 𝘛𝘰𝘰𝘭𝘴: 𝘔𝘪𝘤𝘳𝘰𝘴𝘰𝘧𝘵 𝘗𝘰𝘸𝘦𝘳 𝘉𝘐, 𝘋𝘈𝘟.
  
    We created interactive dashboards and reports to visualize key metrics and provide actionable insights. We focused on customer analysis, product performance, and overall business insights.
    DAX was our tool of choice for dynamic calculations and real-time data insights.
    Modeling data as star schema to facilitate analysis. using active and inactive relations between fact table and dimension table

    Interactive Dashboard Link: https://app.powerbi.com/groups/02b66986-42c9-4a1b-9090-459956b4a268/reports/b384ba17-77f3-4372-a08f-0c1cd35f0e9a/78a3a69cbbbe6b3e3d6d?experience=power-bi


**This project was an exceptional opportunity to apply my theoretical knowledge in a real-world setting, enhancing my data integration, analysis, and visualization skills**

## Project Model

![Sales Data Analysis Dashboard](https://github.com/esraamorsy131/USA-Flights-Projects/blob/main/Model%20Diagram.PNG)

## Project Dashboard

![Sales Data Analysis Dashboard](https://github.com/esraamorsy131/USA-Flights-Projects/blob/main/Summary%20Dashboard.PNG)

![Sales Data Analysis Dashboard](https://github.com/esraamorsy131/USA-Flights-Projects/blob/main/Airlines%20Dahboard.PNG)

![Sales Data Analysis Dashboard](https://github.com/esraamorsy131/USA-Flights-Projects/blob/main/Airport%20Dahboard.PNG)

![Sales Data Analysis Dashboard](https://github.com/esraamorsy131/USA-Flights-Projects/blob/main/Detailed%20Delay%20Time%20Dashboard.PNG)


