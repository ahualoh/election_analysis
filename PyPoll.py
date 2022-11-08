# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Create Accumulator Variable
total_votes = 0 
candidate_options = [] # decalre unique candidate options
candidate_votes = {} # declare an empty dictionary for tallying votes


# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read and analyze the data here.

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        
        # Add to the total vote count
        total_votes += 1

        # Printe the candidate name for each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
            
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
    
    # Print total votes
    print(candidate_votes)
