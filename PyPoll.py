#create path to data
import csv, os

# Assign a variable for the file to load and the path
file_to_load = os.path.join('Resources', 'election_results.csv')
 # Create file for analysis
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize variables
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 1. Create a county list and county votes dictionary
county_list = []
county_votes = {}

# 2. Track the largest county and county voter turnout
county_name = ""
county_count = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

    # read csv and convert it into a list of dictionaries
    reader = csv.reader(election_data)

    # Read the header
    headers = next(reader)

    # Print each in the CSV file
    for row in reader:
        # Add to the total vote count
        total_votes += 1
        # Print candidate name for each row
        candidate_name = row[2]

        # 3. Extract the county name from each row
        county = row[1]

        if candidate_name not in candidate_options:
            # Add candidate name to candidate list
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        #Add a vote to that candidate's count
        candidate_votes[candidate_name] +=1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list
        if county not in county_list:
        
            # 4b: Add the existing county to the list of counties
            county_list.append(county)

            #4c: Begin tracking the county's vote count
            county_votes[county]=0

        # 5: Add a vote to that county's vote count.
        county_votes[county] += 1

    # Save results to our text file       
    with open(file_to_save, "w") as txt_file:

        election_results = (
           f"\nElection Results\n"
           f"-------------------------\n" 
           f"Total Votes: {total_votes:,}\n"
           f"-------------------------\n\n"
           f"County Votes:\n")
        print(election_results, end="")
        txt_file.write(election_results)
       
       # 6a: Write a for loop to get the county from the county dictionary
        for county in county_votes.keys():

            # 6b: Retrieve the county vote count.
            county_vote = county_votes[county]

            # 6c: Calculate the percentage of votes for the county.
            county_percentage = float(county_vote)/float(total_votes) * 100

            # 6d: Print the county results to the terminal.
            county_results = (
                f"{county}: {county_percentage:.1f}% ({county_vote:,})\n")
            print(county_results)

            # 6e: Save the county votes to a text file.
            txt_file.write(county_results)

            # 6f: Write an if statement to determine the winning county and get its vote count.
            if (county_vote > county_count):
                county_name = county
                county_count = county_vote

        # 7: Print the county with the largest turnout to the terminal.
        winning_county = (
            f"\n-------------------------\n"
            f"Largest County Turnout: {county_name}\n"
            f"-------------------------\n")
        print(winning_county)

        # 8: Save the county with the largest turnout to a text file.
        txt_file.write(winning_county)

        #Determine percentage of votes for each candidate
        for candidate_name in candidate_options:
            votes = candidate_votes[candidate_name]
            vote_percentage = float(votes)/float(total_votes)*100
            print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            candidate_results = (
                f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            txt_file.write(candidate_results)

            #Determine winning vote count and candidate
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_percentage = vote_percentage 
                winning_candidate = candidate_name

        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)
