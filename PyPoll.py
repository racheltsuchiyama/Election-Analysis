#create path to data
import csv, os
#print(dir(csv))

# Assign a variable for the file to load and the path
file_to_load = os.path.join('Resources', 'election_results.csv')
 # Create file for analysis
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:

    #To do: read and analyze the data here
    file_reader = csv.reader(election_data)

    # Print the header row
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file
    #for row in file_reader:
        #print(row)

#with open(file_to_save, "w") as txt_file:

    #txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")


# 1. Total number of votes cast

# 2. Complete list of candidates who recieved votes

# 3. Total number of votes each candidate received

# 4. Percentage of votes each candidate won

# 5. The winner of the election based on popular vote

