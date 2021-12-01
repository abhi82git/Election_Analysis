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

# County Percent Votes Initialization
County_Percent_Votes = 0.0

# Candidate Percent Votes Counter
Candidate_Percent_Votes = 0.0

# Winning Vote Counter
Winner_Vote_count = 0

# Biggest turnout county counter
Biggest_Turnout_County_count = 0

# Initialize an empty list to later hold unique candidate names
Candidate_Name_List = []

# Initialize an empty list to later hold unique county names
County_Name_List = []

# Initialize an empty dictionary to later hold ballots for each candidate
Candidate_Ballot_Dict = {}

# Initialize an empty dictionary to later hold ballots for each county
County_Ballot_Dict = {}

with open(file_to_load) as election_data:

    # Perform the analysis
    file_reader = csv.reader(election_data)

    # Print the header rows
    headers = next(file_reader)

    for row in file_reader:
      Total_Votes += 1
      Candidate_Name = row[2]
      County_Name = row[1]
      if Candidate_Name not in Candidate_Name_List:
          Candidate_Name_List.append(Candidate_Name)
          Candidate_Ballot_Dict[Candidate_Name] = 0
          print(f"Candidate in election: {Candidate_Name}")

      if County_Name not in County_Name_List:
          County_Name_List.append(County_Name)
          County_Ballot_Dict[County_Name] = 0
          print(f"County in Election: {County_Name}")

      Candidate_Ballot_Dict[Candidate_Name] += 1
      County_Ballot_Dict[County_Name] += 1

    with open(file_to_save, "w") as election_output:

        Election_Summary = (
            f"--------------------------------------------\n"
            f"Election Results\n"
            f"--------------------------------------------\n"
            f"Total Votes: {Total_Votes:,}\n"
            f"--------------------------------------------\n"
        )
        election_output.write(Election_Summary)
        print(Election_Summary)

        County_Summary = (
            f"--------------------------------------------\n"
            f"County Votes:\n"
        )
        election_output.write(County_Summary)
        print(County_Summary)

        for key, value in County_Ballot_Dict.items():
            County_Percent_Votes = (value / Total_Votes) * 100
            County_Votes_Summary = (f"{key}: {County_Percent_Votes:.1f} % ({value:,}).\n")
            print(County_Votes_Summary)
            election_output.write(County_Votes_Summary)
            if value > Biggest_Turnout_County_count:
                Biggest_Turnout_County_count = value
                Biggest_Turnout_County = key
                Biggest_Turnout_County_Percent = County_Percent_Votes
        Biggest_Turnout_County_Summary = (
            f"---------------------------------------------\n"
            f"Largest County Turnout: {Biggest_Turnout_County}\n"
            f"---------------------------------------------\n"
        )
        election_output.write(Biggest_Turnout_County_Summary)
        print(Biggest_Turnout_County_Summary)

        for key, value in Candidate_Ballot_Dict.items():
            Candidate_Percent_Votes = (value / Total_Votes) * 100
            Candidate_Votes_Summary = (f"{key}: {Candidate_Percent_Votes:.1f} % ({value:,}).\n")
            print(Candidate_Votes_Summary)
            election_output.write(Candidate_Votes_Summary)
            if value > Winner_Vote_count:
                Winner_Vote_count = value
                Winner = key
                Winner_Percent = Candidate_Percent_Votes

        # Write the winner and vote count to output file
        Winning_Candidate_Summary = (
            f"---------------------------------------------\n"
            f"Winner Summary\n"
            f"---------------------------------------------\n"
            f"Winner: {Winner}\n"
            f"Winning Vote Count: {Winner_Vote_count:,}\n"
            f"Winning Percentage: {Winner_Percent:.1f} %\n"
            f"---------------------------------------------\n"
        )
        election_output.write(Winning_Candidate_Summary)
        print(Winning_Candidate_Summary)




