#create path to data
import csv, os
#print(dir(csv))

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
#Why does it have to be before open, isnt before for loop good enough
#3.3.4 says next will skip first row and return next item in list
#but headers are in the first row and next(file) returns the header

# Open the election results and read the file
with open(file_to_load) as election_data:

    #To do: read and analyze the data here
    file_reader = csv.reader(election_data)

    # Print the header row
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:
        # 2. Add to the total vote count
        total_votes += 1
        # Print candidate name for each row
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            # Add candidate name to candidate list
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        #Add a vote to that candidate's count
        candidate_votes[candidate_name] +=1

    #Determine percentage of votes for each candidate
    for candidate_name in candidate_options:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes)/float(total_votes)*100
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

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


#with open(file_to_save, "w") as txt_file:

    #txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")


