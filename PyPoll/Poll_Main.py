#Importing the dependencies
import os
import csv

#Setting the file location
poll_csv_path = os.path.join("election_data.csv")

#setting the variable to count total votes
total_votes = 0

#setting the variable to count votes for Khan
khan_votes = 0

#setting the variable to count votes for Correy votes
correy_votes = 0

#setting the variable to count votes for Li
li_votes = 0

#setting the variables to count votes for O'Tooley
otooley_votes = 0

#opening the file
with open(poll_csv_path,"r") as poll_csv_file:
    
    #reading the file
    poll_csv_reader = csv.reader(poll_csv_file, delimiter=',')
    
    #skip the header row
    poll_csv_header = next(poll_csv_reader)
    
    #loop to read each row of the file
    for row in poll_csv_reader:
        
        #Calculate total voters
        total_votes += 1

        #calcuate vote counts for each candidate
        if row[2] == "Khan":
           khan_votes += 1
        elif row[2] == "Correy":
            correy_votes += 1
        elif row[2] == "Li":
            li_votes += 1
        else:
            otooley_votes += 1

#cakuate the percentage of votes for each candidate
khan_votes_percent = round((khan_votes * 100 / total_votes),3)
correy_votes_percent = round(correy_votes * 100 / total_votes, 3)
li_votes_percent = round(li_votes * 100 / total_votes, 3)
otooley_votes_percent = round(otooley_votes * 100 / total_votes, 3)

#checking which candidate won with max votes
if khan_votes > correy_votes and khan_votes > li_votes and khan_votes > otooley_votes:
    winner = "Khan"
elif correy_votes > khan_votes and correy_votes > li_votes and correy_votes > otooley_votes:
    winner = "Correy"
elif li_votes > khan_votes and li_votes>correy_votes and li_votes > otooley_votes:
    winner = "Li"
else:
    winner = "O'Tooley"

#printing the output to the screen
print("===========================================================")
print("Election Results")
print("-----------------------------------------------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------------------------------------------")
print(f"Khan: {khan_votes_percent}% ({khan_votes})")
print(f"Correy : {correy_votes_percent}% ({correy_votes})")
print(f"Li : {li_votes_percent}% ({li_votes})")
print(f"O'Tooley: {otooley_votes_percent}% ({otooley_votes})")
print("-----------------------------------------------------------")
print(f"Winner: {winner}")
print("===========================================================")


#Specify the file to write the results
poll_output_path = os.path.join("poll_output.txt")

# Open the file to write using "write + " mode. 
with open(poll_output_path, 'w+') as poll_output_csv_file:
    # Initialize csv writer and writing the content
    poll_output_csv_file.write(
        f"===========================================================\n"
        f"Election Results\n"
        f"-----------------------------------------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-----------------------------------------------------------\n"
        f"Khan: {khan_votes_percent}% ({khan_votes})\n"
        f"Correy : {correy_votes_percent}% ({correy_votes})\n"
        f"Li : {li_votes_percent}% ({li_votes})\n"
        f"O'Tooley: {otooley_votes_percent}% ({otooley_votes})\n"
        f"-----------------------------------------------------------\n"
        f"Winner: {winner}\n"
        f"===========================================================\n")

#End of code
