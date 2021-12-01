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

# Percent Votes Counter
Percent_Votes = 0.00

# Winning Vote Counter
Winner_Vote_count = 0

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

    print(f"\nTotal votes cast in the election: {Total_Votes:,}\n")
    print(f"--------------------------------------------")
    print(f"Election Summary")
    print(f"--------------------------------------------")

    for key,value in Candidate_Ballot_Dict.items():
     Percent_Votes = (value/Total_Votes)*100
     print(f"{key}: {Percent_Votes:.2f} % ({value:,}).")
     if value > Winner_Vote_count:
       Winner_Vote_count = value
       Winner = key
       Winner_Percent = Percent_Votes

    print(f"--------------------------------------------\n")

    # Print the winner and vote count
    Winning_Candidate_Summary = (
      f"---------------------------------------------\n"
      f"Winner Summary\n"
      f"---------------------------------------------\n"
      f"Winner: {Winner}\n"
      f"Winning Vote Count: {Winner_Vote_count:,}\n"
      f"Winning Percentage: {Winner_Percent:.2f} %\n"
      f"---------------------------------------------\n"
    )
    print(Winning_Candidate_Summary)

with open(file_to_save,"w") as election_output:

    # Write some data to output file
    # election_output.write("Counties in the Election\n----------------------------\nArapahoe\nDenver\nJefferson")
    Election_Summary = (
      f"--------------------------------------------\n"
      f"Election Results\n"
      f"--------------------------------------------\n"
      f"Total Votes: {Total_Votes:,}\n"
      f"--------------------------------------------\n"
    )
    election_output.write(Election_Summary)

    for key,value in Candidate_Ballot_Dict.items():
      Percent_Votes = (value/Total_Votes)*100
      Votes_Summary = (f"{key}: {Percent_Votes:.2f} % ({value:,}).\n")
      election_output.write(Votes_Summary)
      if value > Winner_Vote_count:
          Winner_Vote_count = value
          Winner = key
          Winner_Percent = Percent_Votes

