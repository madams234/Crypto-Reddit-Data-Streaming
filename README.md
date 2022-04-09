# Crypto-Reddit-Data-Streaming
Springboard Data Engineering Capstone Project

## Overview
This project streams reddit and yFinance data. The data is put into a visualization to allow analysis between how many subreddits are given in a timeframe and the price changes of the currency during the same period. We use kafka, python, Google Cloud Postgres, Faust, confluent plugins, websockets, docker containers, and plotly for visuals. 

## Data Source
We use kafka to stream the subreddits for our project. We use the landoop kafka docker container and add the conflunet kafka-connect plugin to the correct filepath within the docker container. We update the .property files with the correct subreddits we want to look at as well as directing the data to the correct kafka topic. We create this topic in kafka, then run kafka-connect to begin the data pipeline. Specific instructions are included in our shell command file. 

The yFinance data is streamed through a websocket created through our python file. We send this data directly to Google Cloud Postgres though PGAdmin. 

## Data Transformation
We use Faust to add a timestamp to the reddit data coming in through kafka. We then send this data into our Cloud database. The yFincance data gets sent to the cloud directly from our websocket.

## Data Storage
We create a Google Cloud Postgres Server noting the IP address, user, and password and install a local PGAdmin connecting to the server. We create tables, as well as a trigger to have created_at info. Specific instructions for this are included in the .sql file.  

## Data Visual
We use python and plotly.express to create visuals of the data for analysis. We create bar graphs of the number of occurances of subreddit posts over a given time and compare this to the line graph of the correlating stock price. The visuals are included in the slidedeck. 
