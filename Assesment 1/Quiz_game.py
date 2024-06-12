from datetime import datetime

class QuizGame:

    def __init__(self):
        pass

        
    #Sets up an empty dictionary for questions and a log file for transactions.
        
    que_lst = {}
    log_file = "quiz_game_log.txt"

    #create function to log transaction with timestamp and message
    def log_transaction(self, message):
        with open(self.log_file, "a") as file:
            file.write(f"{datetime.now()} : {message}\n")

    #create function to add questions
    def add_que(self):
        
            #Prompts the Quiz Master to enter the question, options, and the correct answer.

            que_num = len(self.que_lst) + 1

            while True:

                que = input(f"\n> Enter the question {que_num}:")

                opt = {}
                for i in ['a','b','c']:

                    opt[i] = input(f"> Enter option {i}:")

                while True:
                
                    ans = input("> Enter correct option:")

                    if ans in opt:
                        break
                    else:
                        print("Invalid input, Please enter valid option (a/b/c)")


                self.que_lst[que_num] = {'que':que,
                                        'opt':opt,
                                        'ans':ans}
                
                #Logs the addition of the question.
                self.log_transaction(f"Question {que_num} added.")
                
                que_num += 1 

                #Check if the Quiz Master wants to add more questions
                while True:

                    con = input("\n> Do you want to continue adding questions (y/n):").lower()

                    if con == 'y':
                        break

                    elif con == 'n':

                        print("\n\t\t\t\t    =================================")
                        print("\t\t\t\t     Questions added successfully..!!")
                        print("\t\t\t\t    =================================")

                        return

                    else:
                        print("Invalid choice, please enter 'y' or 'n' ")
                
    #create a function to print question with options and answers
    def print_question(self, que_num, question, show_answer=True):

        print(f"\n> Question {que_num}")
        print('----------')
        print(f"Question: {question['que']}")

        print("Options:")
        for option, value in question['opt'].items():
            print(f"{option}: {value}")

        if show_answer:
            print(f"Answer: {question['ans']}")

    #create a function to view added questions
    def view_que(self, que_num=None):

        #Displays one question if specific question number is provided.
        if que_num is not None:

            if que_num in self.que_lst:

                question = self.que_lst[que_num]
                
                self.print_question(que_num,question)
                self.log_transaction(f"Viewed question {que_num} ({question})")

            else:

                print("\n\t\t\t\t     ===============================")
                print(f"\t\t\t\t      Error, question {que_num} not found..!!")
                print("\t\t\t\t     ===============================")

        #Displays all questions if no specific question number is provided.
        elif len(self.que_lst) != 0:

            print("\n> All Questions:")
        

            for que_num, question in self.que_lst.items():
                
                print(f"\nQuestion {que_num}")
                print('----------')
                print(f"Question: {question['que']}")
                print("Options:")

                for option, value in question['opt'].items():
                    print(f"{option}: {value}")
                print(f"Answer: {question['ans']}")
                self.log_transaction(f"Viewed question {que_num} ({question})")

        else:

            print("\n\t\t\t\t    ================================")
            print("\t\t\t\t     Error, No questions added..!!")
            print("\t\t\t\t    ================================")    

    #create a function to update existing question
    def update_que(self):

        while True:

            try:

                #accept number to update particular question
                que_num = int(input("\n> Enter question number to update: "))


                if que_num in self.que_lst:

                    self.print_question(que_num, self.que_lst[que_num])

                    #Prompts the Quiz Master to enter the new details for the questions
                    que = input(f"\n> Enter new question (leave blank to keep current): ")

                    opt = {}
                    for i in ['a', 'b', 'c']:
                        opt[i] = input(f"> Enter new option {i} (leave blank to keep current): ") or self.que_lst[que_num]['opt'][i]

                    while True:
                        ans = input("> Enter new correct option (a/b/c): ")

                        if ans in opt:
                            break
                        else:
                            print("Invalid option. Please enter a valid option (a/b/c).")

                    self.que_lst[que_num] = {'que': que or self.que_lst[que_num]['que'], 'opt': opt, 'ans': ans}

                    #log the updation of question
                    self.log_transaction(f"Question {que_num} updated.")

                    print("\n\t\t\t\t    ==================================")
                    print("\t\t\t\t     Question updated successfully..!!")
                    print("\t\t\t\t    ==================================")
                    break

                else:

                    print(f"Question {que_num} not found, Please try again..!!")

            except ValueError:

                print("Invalid input, Please enter a valid question number..!!")

    #define a function to delete question
    def delete_que(self):

        while True:
                
            try:

                que_num = int(input("\n> Enter question number to delete:"))

                if que_num in self.que_lst:
                    
                    #Prompts the Quiz Master to confirm the deletion
                    con = input(f"> Do you really want to delete Question {que_num} (y/n):").lower()

                    if con == 'y':

                        del self.que_lst[que_num]
                        self.log_transaction(f"Question {que_num} deleted.")

                        print("\n\t\t\t\t   ====================================")
                        print(f"\t\t\t\t    Question {que_num} deleted succesfully..!!")
                        print("\t\t\t\t   ====================================")
                        break

                    elif con == 'n':

                        print("\n\t\t\t\t   ===============================")
                        print("\t\t\t\t     Question deletion cancelled ")
                        print("\t\t\t\t   ===============================")

                        #log the deletion of question
                        self.log_transaction(f"Question {que_num} deletion aborted.")
                        break
                        
                else: 

                    print("\n\t\t\t\t     ================================")
                    print(f"\t\t\t\t      Error, question {que_num} not found..!!")
                    print("\t\t\t\t     ================================")

            except ValueError:

                print("Invalid input, Please enter a valid question number..!!")

    #define a function to play the quiz game
    def play_quiz(self):

        Questions = self.que_lst

        if not Questions:

            print("\n\t\t\t=========================================================")            
            print("\t\t\t No questions available..!! Please add some questions..!! ")
            print("\t\t\t==========================================================")
        
        else:

            self.log_transaction(f"Started playing quiz.")
            score = 0
            ttl_scr = len(Questions)

            #Prompts the Quiz Cracker to answer the questions.
            for que_num,question in Questions.items():

                print(f"{que_num}) {question['que']}")
                
                for opts,val in question['opt'].items():

                    print(f"{opts}:{val}")

                while True:

                    ans = input("> Choose your option (a/b/c): ")

                    if ans in question['opt']:
                        break
                    else:
                        print("Invalid input, Please enter a valid option (a/b/c).")

                if ans == question['ans']:

                    score += 1
                    print("\n=============================")
                    print(f" Correct answer..!! Score: {score}")
                    print("=============================\n")
                    self.log_transaction(f"Answered question {que_num} correctly.")

                else:
                    print("\n================================")
                    print(f" Incorect answer..!! Correct: {question['ans']}")
                    print("================================\n")
                    self.log_transaction(f"Answered question {que_num} Incorrectly.")

            #Displays the final score and logs the result in log file
            print(f"[ Quiz completed..!! Your final score: {score}/{ttl_scr} ]")
            self.log_transaction(f"Completed the quiz with score of {score}/{ttl_scr}")
        