import os
import csv

#from PyPoll.Date import Date

# Path to collect data from the Resources folder
csvpath = os.path.join('.', 'Resources', 'election_data.csv')

#Read in the CSV file
with open (csvpath,'r') as csvfile:
    #split the date on comas
  csvreader=csv.reader(csvfile,delimiter=",")
  
  #Read the header row first
  csv_header=next(csvreader)

  #Initialize a total vote counter.
  total_votes = 0
  winnig_count=0
 
  #Setting Variables
  candidate_options = []
  candidate_votes = {}
  candidate_results=[]
  

  for row in csvreader:
  #The total number of votes cast
    total_votes=total_votes+1
  #Remove duplicates 
    candidate_name=row[2]
    if candidate_name not in candidate_options:
      candidate_options.append(candidate_name)  
      candidate_votes[candidate_name] = 0
   #Counting the votes for each candidate   
    candidate_votes[candidate_name] +=1

print("Election Results")
print("\n")
print("----------------------------")
print("\n")
print(f"Total Votes:{(total_votes)}")
print("\n")
print("----------------------------")


#Output file
output_file = os.path.join('..', 'PyPoll', 'Analysis', 'Election Results_Summary.txt')

with open(output_file,"w") as file:
    file.write("Election Results")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Votes:{(total_votes)}")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")


#Calculate the %
    for candidate_name in candidate_votes:
      votes = candidate_votes.get(candidate_name)
      vote_percentage = float(votes) / float(total_votes) * 100
      candidate_results = (f"{candidate_name}: {vote_percentage:.3f}% ({votes:,})\n")
      print (candidate_results)
      file.write(candidate_results)

    
#Find the Winner
      if (votes>winnig_count):
            winnig_count=votes
            winning_candidate = candidate_name

    print("\n")      
    print("----------------------------")
    print("\n")
    print(f"Winner: {winning_candidate}")
    print("\n")
    print("----------------------------")


    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Winner:{winning_candidate}")
    file.write("\n")
    file.write("----------------------------")