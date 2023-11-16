import os 
import csv

from datetime import datetime
# determine file path
read_file= os.path.join("..","Resources","election_data.csv")

# Open and read file
with open(read_file) as csvfile:
    election_file=csv.reader(csvfile, delimiter=",")
    election_header= next(election_file)

# Create variables and dictionary to store candidate
    total_votes=0
    cand_votes_dict={}


    # # Iterate through rows
    for row in election_file:
    
       
        total_votes+=1
        candidate =row[2]

        if candidate not in cand_votes_dict:
            cand_votes_dict[candidate]=1
        
        else:
            cand_votes_dict[candidate]+=1

    perc_votes={}
    
    for candidate, votes in cand_votes_dict.items():

        percentage= (votes/total_votes)*100
        perc_votes[candidate]=percentage

winner=max(cand_votes_dict,key=cand_votes_dict.get)

# Print

print(f'Election Results')
print(f'----------------------------------------------')
print(f'Total Votes: {total_votes}')
print(f'----------------------------------------------')

# Calculate and print results
for cand, votes in cand_votes_dict.items():
    print(f'{cand}: {percentage:.2f}% ({votes})')

print(f'Winner: {winner}')
print(f'----------------------------------------------')


# Create output file in txt
output_file = os.path.join("..","analysis","PyPoll_results.txt")

# Write analysis print statements to file by adding ",file=datafile"
#  to same print statements
with open(output_file, "w") as datafile:

# Print

    print(f'Election Results', file=datafile)
    print(f'----------------------------------------------', file=datafile)
    print(f'Total Votes: {total_votes}', file=datafile)
    print(f'----------------------------------------------', file=datafile)

    # Calculate and print results
    for cand, votes in cand_votes_dict.items():
        print(f'{cand}: {percentage:.2f}% ({votes})', file=datafile)
        print(f'Winner: {winner}', file=datafile)
        print(f'----------------------------------------------', file=datafile)