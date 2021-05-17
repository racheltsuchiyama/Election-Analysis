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
        


* **The Winning Candidate**

    Used conditionals to extract the candidate with the largest number of votes and the highest percentage of the votes.

* **Counties**

    The same methods as described above for the candidate analysis was used for the county analysis. Instead of finding the candidate names, the county names were found and used as keys in the county_votes dictionary. The number of votes within each county were stored as the values of the dictionary. Then, these values were used to calculate the percentage of votes in each county. The county with the highest percentage of votes was then determined using an if statement.

## Election Audit Summary

The audit was successful in providing the Colorado Board of Elections with the necessary information. The code printed the results in the terminal, while also saving it to a text file, for easy extraction. While this analysis was performed for a local congressional election, the code can be edited for larger scale elections like the US Presidential election. 

### Modifying the script for general election audit use
Depending on the structure of the dataset to be analysed, the candidate names and counties could be stored in a different column then the one specified in my code. Before performing analysis of other elections, check which columns contain the candidate names and counties and correct accordingly.
For country-wide elections, analysing the voter turnout per state would be more help. The code containing the county analysis can be altered to perform state analysis.
