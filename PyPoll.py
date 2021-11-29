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


# Assign a file to a variable
file_to_load = os.path.join("Resources","election_results.csv")

with open(file_to_load) as election_data:

    # Perform the analysis
    file_reader = csv.reader(election_data)

    # Print the header rows
    headers = next(file_reader)
    print(headers)

    # for row in file_reader:
      # print(row[0])

# Assign output file to variable
file_to_save = os.path.join("Analysis","election_analysis.txt")

with open(file_to_save,"w") as election_output:

    # Write some data to output file
    election_output.write("Counties in the Election\n----------------------------\nArapahoe\nDenver\nJefferson")

