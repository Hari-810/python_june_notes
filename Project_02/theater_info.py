from winreg import EnumValue
import   user_info
class seats:
    global matrix,total_seats_booked
    matrix = []


    def __init__(self):
        self.no_of_rows = int(input("Enter the Number of Rows:"))
        self.no_of_seats = int(input("Enter the Number of Seats:"))
       

    def capacity(self):
        for i in range(self.no_of_rows + 1):
            a = []
            for j in range(self.no_of_seats + 1):
                a.append("S")
            matrix.append(a)

        total_seats = self.no_of_seats * self.no_of_rows
        return total_seats, self.no_of_rows,self.no_of_seats

    def show_the_seats(self):

        for i in range(0, self.no_of_rows + 1):
            if i == 0:
                for j in range(0, self.no_of_seats + 1):
                    print(j, end=" ")
            else:
                print(i, end=" ")
                for k in range(self.no_of_seats):
                    print(matrix[i - 1][k], end=" ")
            print()



class tickets:
    global price_each_ticket,p

    def __init__(self):
        self.book_row = int(input("Please enter the row no. you want to book: "))
        self.book_column = int(input("Please enter the column no. you want to book: "))


    def buy_ticket(self, total_seats, no_of_rows,total_income,total_seats_booked ):

        p = tickets.price_per_ticket(self,total_seats, no_of_rows,total_income)
        print(p)

        print("The Price of your ticket will be: ", p)
        confirmation = input("Please Confirm to book your ticket Yes/No")

        if confirmation == 'Yes' or confirmation=='yes':

            matrix[self.book_row - 1][self.book_column - 1] = "B"
            u=user_info.user_info()
            u.user(self.book_row,self.book_column)
            return True,p

        else:
            print("No ticket booked")
            return None,None

    def price_per_ticket(self, total_seats, no_of_rows,total_income):
        current_income=0
        if total_seats <= 60:
            current_income=10
            total_income=total_income + current_income
            return  10

        else:
            if self.book_row >= (no_of_rows / 2):
                current_income = 8

                return  8
            else:
                current_income = 10

                return 10

class statistics:
    def stats(self,total_seats_booked,total_seats,c,total_income):
        print("Number of Purchased Tickets: ",total_seats_booked)
        print("Percentage of Tickets Booked: ",(total_seats_booked/total_seats)*100)
        print("Current Income: ",c,"$")
        print("Total_income: ",total_income,"$")
        print(50*"-")   


# New class created 
class Theater:
    # Method
    def movie_name(self):
        print("please choose the movie:\n")
        movie_list = ["Aaa","Bbb","ccc"]  # list containg Movie names
        for i,value in enumerate (movie_list):
            print(i,":",value,"\n")       # Print the movie names
        self.user_movie =  int(input("Enter the Movie number: \n"))  # Get the input
 
        print(50*"-")   

    # Method
    def movie_language(self):
        print("Please choose the Lanuage")

        # Specific language for each movie
        if self.user_movie == 0:
            lang  = ["Tamil","English","Hindi","Kannada","Telugu"] # langugaes for movie Aaa (can add more languages)
            for i,value in enumerate (lang):
                print(i,":",value,"\n")
        elif self.user_movie == 1:  # langugaes for movie Bbb (can add more languages)
            lang  = ["Tamil","English","Kannada","Telugu"]
            for i,value in enumerate (lang):
                print(i,":",value,"\n")
        else:               #elif self.user_movie == 2:
            lang  = ["Tamil","English"] #  # langugaes for movie Ccc (can add more languages)
            for i,value in enumerate (lang):
                print(i,":",value,"\n")
        
        lang_val = int(input("choose the number: \n"))
        self.lang_flag  = True
        print(50*"-")   

    # Method
    def timing(self):
        value_time = ["09:00 Am", "11:00 AM","02:00 Am", "06:00 Am", "10:00 Am"] #Timings
        for i,value in enumerate (value_time):
            print(i,":",value,"\n")
        user_time =  int(input("Enter the Time slot: \n"))
        print(50*"-")   
    
