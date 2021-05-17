# Election-Analysis

## Project Overview
The Colorado Board of Elections wants an audit performed on the recent local congressional election. The election audit requires information about the candidates' vote totals and the voter turnout throughought the counties. Using the data provided in the **election_results.csv**, I will determine the total number of votes cast, the number of votes in each county, and the number of votes for each candidate. Using these values, I will calculate the percentage of votes each candidate recieved and the percentage of votes cast in each county.
### Software
Python 3.6.1
Visual Studio Code 1.38.1

## Election Audit Results

* **Total Votes** = 369,711

    Created a for loop to iterate through all the rows, excluding the header row containing the column names, and added up the total number of rows and therefore the total votes cast.

* **Candidates**

    Within the for loop, added the candidate names to a list called candidate_options if they were not already in the list.
    
    <img width="465" alt="Screen Shot 2021-05-16 at 4 21 02 PM" src="https://user-images.githubusercontent.com/83552696/118417585-8c80ba80-b669-11eb-9350-28c177869850.png">

    - Candidate votes:

        Used the candidate names as keys in the candidate_votes dictionary, and added the votes they received as the dictionary values (line 50).

    - Candidate percentage of votes:

        Converted the candidate votes and total votes to decimal floating point data types to calculate what percentage of the total votes each candidate recieved.
        
<img width="485" alt="Screen Shot 2021-05-16 at 4 27 29 PM" src="https://user-images.githubusercontent.com/83552696/118417656-fb5e1380-b669-11eb-8f36-03a68df799e3.png">

   **Candidate Results**
   
<img width="315" alt="Screen Shot 2021-05-16 at 5 14 35 PM" src="https://user-images.githubusercontent.com/83552696/118417741-50018e80-b66a-11eb-8b65-ba0fa3b9c774.png">


* **The Winning Candidate**

    Used conditionals to extract the candidate with the largest number of votes and the highest percentage of the votes.
    
    <img width="554" alt="Screen Shot 2021-05-16 at 5 16 46 PM" src="https://user-images.githubusercontent.com/83552696/118417787-8939fe80-b66a-11eb-9df9-0513225ad661.png">
    
    <img width="231" alt="Screen Shot 2021-05-16 at 5 14 42 PM" src="https://user-images.githubusercontent.com/83552696/118417768-7293a780-b66a-11eb-89eb-e33d9b3d8cb4.png">


* **Counties**

    The same methods as described above for the candidate analysis was used for the county analysis. Instead of finding the candidate names, the county names were found and used as keys in the county_votes dictionary. The number of votes within each county were stored as the values of the dictionary. Then, these values were used to calculate the percentage of votes in each county. The county with the highest percentage of votes was then determined using an if statement.

<img width="565" alt="Screen Shot 2021-05-16 at 5 22 25 PM" src="https://user-images.githubusercontent.com/83552696/118418040-a28f7a80-b66b-11eb-8824-80a1c73b4502.png">

<img width="423" alt="Screen Shot 2021-05-16 at 5 24 03 PM" src="https://user-images.githubusercontent.com/83552696/118418047-a58a6b00-b66b-11eb-81d9-acf4f7e2cb67.png">

   **County Results**

<img width="261" alt="Screen Shot 2021-05-16 at 5 14 25 PM" src="https://user-images.githubusercontent.com/83552696/118417796-922ad000-b66a-11eb-8d60-974814b6b0bc.png">

## Election Audit Summary

The audit was successful in providing the Colorado Board of Elections with the necessary information. The code printed the results in the terminal, while also saving it to a text file, for easy extraction. While this analysis was performed for a local congressional election, the code can be edited for larger scale elections like the US Presidential election. 

### Modifying the script for general election audit use
Depending on the structure of the dataset to be analysed, the candidate names and counties could be stored in a different column then the one specified in my code. Before performing analysis of other elections, check which columns contain the candidate names and counties and correct accordingly.
For country-wide elections, analysing the voter turnout per state would be more help. The code containing the county analysis can be altered to perform state analysis.
