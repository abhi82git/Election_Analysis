# Pseudo Code
# Open the file election_results.csv.
# import date from election_results.csv.
# Count the total # of votes cast
# Unique names of all candidates who got votes
# Total of votes for each candidate
# % of votes for each candidate
# Winner based on who got most votes

# import modules
import csv
import os


# Assign input file to a variable
file_to_load = os.path.join("Resources","election_results.csv")

# Assign output file to variable
file_to_save = os.path.join("Analysis","election_analysis.txt")

# Total Votes Counter
Total_Votes = 0

# Initialize an empty list to later hold unique candidate names
Candidate_Name_List = []

# Initialize an empty dictionary to later hold ballots for each candidate
Candidate_Ballot_Dict = {}

with open(file_to_load) as election_data:

    # Perform the analysis
    file_reader = csv.reader(election_data)

    # Print the header rows
    headers = next(file_reader)

    for row in file_reader:
      Total_Votes += 1
      Candidate_Name = row[2]
      if Candidate_Name not in Candidate_Name_List:
          Candidate_Name_List.append(Candidate_Name)
          Candidate_Ballot_Dict[Candidate_Name] = 0
          print(f"Candidate in election: {Candidate_Name}")

      Candidate_Ballot_Dict[Candidate_Name] += 1

    print(f"\nTotal votes cast in the election: {Total_Votes}\n")
    for key,value in Candidate_Ballot_Dict.items():
      print(f"{key} secured {value} votes.\n")

with open(file_to_save,"w") as election_output:

    # Write some data to output file
    election_output.write("Counties in the Election\n----------------------------\nArapahoe\nDenver\nJefferson")

