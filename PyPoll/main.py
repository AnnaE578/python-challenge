import csv

# Files to load and output (Remember to change these)
file_path = "PyPoll/Resources/election_data.csv"
output_file_path = "PyPoll/Resources/file_output.text"

# Function to analyze election data
def analyze_election(file_path, output_file_path):
    # Initialize variables
    total_votes = 0
    candidates = {}
    winner = ""
    winning_votes = 0

    # Read the CSV file
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)

        # Loop through each row in the CSV
        for row in reader:
            # Count total votes
            total_votes += 1

            # Count votes for each candidate
            candidate_name = row["Candidate"]
            if candidate_name in candidates:
                candidates[candidate_name] += 1
            else:
                candidates[candidate_name] = 1

    # Find the winner
    for candidate, votes in candidates.items():
        if votes > winning_votes:
            winner = candidate
            winning_votes = votes

    # Calculate the percentage of votes each candidate won
    percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidates.items()}

    # Print the results to the terminal
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for candidate, votes in candidates.items():
        print(f"{candidate}: {percentages[candidate]:.3f}% ({votes})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

    # Save the results to a text file
    with open(output_file_path, 'w') as output_file:
        output_file.write("Election Results\n")
        output_file.write("-------------------------\n")
        output_file.write(f"Total Votes: {total_votes}\n")
        output_file.write("-------------------------\n")
        for candidate, votes in candidates.items():
            output_file.write(f"{candidate}: {percentages[candidate]:.3f}% ({votes})\n")
        output_file.write("-------------------------\n")
        output_file.write(f"Winner: {winner}\n")
        output_file.write("-------------------------\n")

# Call the function to analyze the election and save results
analyze_election(file_path, output_file_path)
















# Files to load and output (Remember to change these)
filepath = os.path.join("PyPoll/Resources/election_data.csv")
output_filepath = os.path.join("PyPoll/Resources/file_output.text")

# Function to analyze election data
def analyze_election(filepath, output_filepath):
    # Initialize variables
    
    total_votes = 0
    candidate_votes = {}
    percent_candidates_votes = {}
    total_canditate_votes = 0
    winner = ""
    winning_count = 0

# Read the CSV file
    with open(filepath, 'w') as election_data:

    # CSV reader specifies delimiter and variable that holds contents
        filereader = csv.DictReader(filepath)
    
        print(filereader)


    # For each row...
    for row in filereader:

        # Add to the total vote count
        total_votes += 1

         # A complete list of candidates who received votes and The total number of votes each candidate won
        candidate_name = row["Candidate"]
        if candidate_name in candidate_votes:
                candidate_votes[candidate_name] += 1
        else:
                candidate_votes[candidate_name] = 1

        # The percentage of votes each candidate won
        for key, velue in candidate_votes.items():
            percent_candidates_votes[key] =round((velue/total_votes)* 100 , 3)
         # Total canditate votes
            total_canditate_votes += 1
         
         # The winner of the election based on popular vote.
        for candidate, votes in candidate.items():
            if votes > winning_count:
                winner = candidate
                winning_count = votes

   # print the result on terminal    
    print(f"Election Results")
    print(f"-------------------------")
    print(f"Total Votes: {total_votes}")
    print(f"-------------------------")
    for key, velue in candidate_votes.items():
        print(key,':' , str(percent_candidates_votes[key]),'%','  ','(',candidate_votes[key],')')
        print(f"-------------------------")
        print(f"Winner: {winner}")
        print(f"-------------------------")

# Save the results to a text file
with open(output_file_path, 'w') as output_file:
        output_file.write("Election Results\n")
        output_file.write("-------------------------\n")
        output_file.write(f"Total Votes: {total_votes}\n")
        output_file.write("-------------------------\n")
        for candidate, votes in candidates.items():
            output_file.write(f"{candidate}: {percentages[candidate]:.3f}% ({votes})\n")
        output_file.write("-------------------------\n")
        output_file.write(f"Winner: {winner}\n")
        output_file.write("-------------------------\n")
    # Save the final vote count to the text file
election_data.write(election_results)

       
    # Save the winning candidate's name to the text file
election_data.write(winning_candidate_summary)


