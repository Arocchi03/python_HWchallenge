import csv 
import os 

Voter_ID = 0
County = 0
total_votes = 0 
percentage_votes = []
num_votes = []
Candidate_list = []
Candidate_winner=[]

#Reading data 
csvpath = os.path.join("PyPoll/Resources/election_data.csv")
with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') 
    csv_header = next(csvreader)

# Starting For loop
    for column in csvreader:
#print(row)
#The total number of votes cast

        Voter_ID = Voter_ID + 1
        #Voter_ID += 1
#The total amount of "Candidate" over the entire period
        #Candidate_list += int(column[2])
        #Candidate_list =  Candidate_list + int(column[2])
#         Candidate_list.append(str(column[2]))
#         my_final_list = set(Candidate_list)
# print(list(my_final_list))
#print(Candidate_list)
        candidate_name= column[2]
        if candidate_name not in Candidate_list:
            Candidate_list.append(candidate_name)
#print(Candidate_list)

#The percentage of votes each candidate won
    for votes in num_votes:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percentage_votes.append(percentage)
#print(percentage_votes)

#The winner of the election based on popular vote
    winner = max(num_votes)
    index = num_votes.index(winner)
    winning_candidate = Candidate_list[index] 
#print(Candidate_winner) 








