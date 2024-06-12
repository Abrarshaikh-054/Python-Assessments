''' Quiz Game with crud operation under software development principles and protocols'''

from Quiz_game import *

"""
Main function to run the Quiz Game
which provides options to select roles (Quiz Master or Quiz Cracker) and perform corresponding actions.
"""
def main():

    print("\t\t\t\t\t===================================")
    print("\t\t\t\t\t Welcome to the Quiz Game Challange")
    print("\t\t\t\t\t===================================")

    #Initialize the QuizGame class
    game = QuizGame()

    #loop to display the role selection menu
    while True:

        print("\n\t\t\t\t\t--> Select your role:\n")
        print("\t\t\t\t\t 1. Quiz Master   (press 1)")
        print("\t\t\t\t\t 2. Quiz Cracker  (press 2)")
        print("\t\t\t\t\t 3. Exit          (press 3)\n")


        try:
            
            # Get the role choice from the user
            rl_ch = int(input("> Enter your role: "))

        except ValueError:

              # Handle invalid input
            print("\n\t\t\t\t\t==============================")
            print("\t\t\t\t\t Invalid input, Try Again..!!")
            print("\t\t\t\t\t==============================")
            
            continue

        if rl_ch == 1:

            # if choice is 1 then display the Quiz Master menu
            while True:

                print("\n\t\t\t\t\t-------------------------")
                print("\t\t\t\t\t The Quiz Master Wizard")
                print("\t\t\t\t\t-------------------------")
                print("\n\t\t\t\t\t||======= MENU =======||\n")
                print("\t\t\t\t\t   1. Add Question")
                print("\t\t\t\t\t   2. View Question")
                print("\t\t\t\t\t   3. Update Question")
                print("\t\t\t\t\t   4. Delete Question")
                print("\t\t\t\t\t   5. Back to Main Menu\n")

                try:

                    #ask user to choose opeartion from Master Menu
                    qm_ch = int(input("> Choose an operation (1/2/3/4/5): "))

                except ValueError:

                    print("\n\t\t\t\t\t=============================")
                    print("\t\t\t\t\t Invalid input, Try Again..!!")
                    print("\t\t\t\t\t=============================")

                    continue

                if qm_ch == 1:

                    #call the function to add question
                    game.add_que()

                elif qm_ch == 2:
                    
                    while True:

                        try:
                            # Ask if the user wants to view all questions or a specific question
                            view_all = input("\n> Do you want to view all the questions (y/n): ").lower()

                            if view_all == 'y':

                                game.view_que()
                                break

                            elif view_all == 'n':

                                que_num = int(input("> Enter question number to view: "))
                                game.view_que(que_num)
                                break

                            else:

                                print("Invalid choice, please enter 'y' or 'n' ")

                        except ValueError:

                            print("Invalid input, Please enter a valid question number..!!")

                elif qm_ch == 3:

                    #call the function to update question
                    game.update_que()

                elif qm_ch == 4:

                    #call the function to delete question
                    game.delete_que()

                elif qm_ch == 5:

                    #return to tha main menu
                    break

                else:

                    print("\n\t\t\t\t\t==============================")
                    print("\t\t\t\t\t Invalid Choice, Try Again..!!")
                    print("\t\t\t\t\t==============================")
            
        elif rl_ch == 2:

            print("\t\t\t\t\t-------------------------")
            print("\t\t\t\t\t The Quiz Cracker Wizard")
            print("\t\t\t\t\t-------------------------")

            #call the fucntion to play the quiz
            game.play_quiz()


        elif rl_ch == 3:

            print("\nThanks for playing :) \n")
            break

        else:

            print("\n\t\t\t\t\t=============================")
            print("\t\t\t\t\t Invalid Choice, Try Again..!!")
            print("\t\t\t\t\t=============================")

if __name__ == "__main__":
    main()
