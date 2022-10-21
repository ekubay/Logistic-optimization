# Logistic-Optimization

## Delivery drivers location optimisation with Causal Inference 

#### Initial system architecture design

![](screen_shots/solid-workflow-diagram.png)

**Table of contents**

- [Introduction](#introduction)
- [Overview](#overview)
- [Objective](#objective)
- [Data](#data)
- [Requirements](#requirements)
- [Install](#install)
- [Using the application](#examples)
- [Notebooks](#notebooks)
- [Scripts](#scripts)
- [Strategies](#strategies)
- [Test](#test)
- [Authors](#authors)

## Introduction

> The client for this week's challenge is Gokada - the largest last mile delivery service in Nigeria. Gokada works is partnered with motorbike owners and drivers to deliver parcels across Lagos, Nigeria. Gokada has completed more than a million deliveries in less than a year, with a fleet of over 1200 riders.
One key issue Gokada has faced as it expands its service is the sub-optimal placement of pilots (Gokada calls their motor drivers pilots) and clients who want to use Gokada to send their parcel. This has led to a high number of unfulfilled delivery requests. 


## Objective
>Gokada is asking 10 Academy trainees, to work on its data to help it understand the primary causes of unfulfilled requests as well as come up with solutions that recommend drivers locations that increase the fraction of complete orders. Since drivers are paid based on the number of requests they accept, your solution will help Gokada business grow both in terms of client satisfaction and increased business. 

## Data
There are two datasets available for this project.
- The first one is the table that contains information about the completed orders
>- Trip ID          
>- Trip Origin       
>- Trip Destination  
>- Trip Start Time   
>- Trip End Time    

- The second one is the table that contains delivery requests by clients (completed and unfulfilled) 
 >- id               
 >- order_id       
 >- driver_id        
 >- driver_action 
 >- lat            
 >- lng            
 >- created_at    
 >- updated_at  

> Basic features of the data sets:

## Requirements
> Pip

You can find the full list of requirements in the requirements.txt file

## Install

> It is recommended that to create a new virtual environment and install every required modules and libraries on the virtual evironment.

### Installing this application

- First clone this repo to your local machine using the command below

```
git clone https://github.com/ekubay/causal_inference.git
cd causal_inference
pip install -r requirements.txt
```

## Notebooks

> All the notebooks that are used in this project including EDA, data cleaning and summarization along with some machine learning model generations are found here in the Notebooks folder.

## Scripts

> All the scripts and modules used for this project relating to interactions with kafka, airflow, and other frameworks along with default parameters and values used will be found here, in the scripts folder.

## Tests

> All the unit and integration tests are found here in the tests folder.

## Author
> 👤 **Ekubazgi Gebremariam**
> - [Email](mailto:axutec14@gmail.com), [GitHub](https://github.com/ekubay), [LinkedIn](https://www.linkedin.com/in/ekubazgi-g-mariam-61507270)

## Show us your support

> Give ⭐ if you like this project, and also feel free to contact me at any moment.

![Contributors list](https://contrib.rocks/image?repo=Logistic-optimization)
