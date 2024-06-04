# using files concept to read txt files containing questions and answers
file1 = open('questions.txt', 'r')  
question_list = file1.readlines()   # using readlines() function to create a list of questions
file1.close()
file2 = open('answers.txt', 'r')    
answer_list = file2.readlines()     # using readline() function to create a list of answers
file2.close()