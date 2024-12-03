# FinalProjectDSA

## Setting Up
The data set is very large so it will need to be downloaded separately. This takes only a couple of minutes, below are the instructions on how to do it. 
1. Go to https://amazon-reviews-2023.github.io/ to download the dataset.

2. Scroll down to Group By Category to find "Appliances", download the meta data.
<img width="1115" alt="Screenshot 2024-11-28 at 4 53 57 PM" src="https://github.com/user-attachments/assets/521e97bf-47b4-4c09-8d20-2734ab5e4b0f">

3. Once the data is downloaded, unzip the file and copy and past it into the "data" folder in the repository and then it is ready for use. 

## How to Use 
The results will be based on the information from our dataset.
1. User is prompted to enter titles they want to search for.
2. Type title you want to search for, then press enter. 
3. Continue until you've inputted all titles to search for. Type 'done' when you're finished.

## Analyzing Results
The results show the amount of time taken for searching through both our hashmap and trie data structures for each title. At the end, the average time taken and the accuracy in finding all the elements is displayed for both hashmap and trie searches. In the average case, the hashmap takes significantly less time to find the title than the trie, however the accuracy is greater for the trie. The hashmap searches for a complete title and if not found, nothing is returned. The trie structure can find a title based on partial input from the user, however it takes longer. 
