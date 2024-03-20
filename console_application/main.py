import time
import theater_info,user_info

user_input = 20
s = theater_info.seats()
total_seats, no_of_rows, no_of_seats= s.capacity()
st=theater_info.statistics()
total_seats_booked=0
total_income = 0
current_income=0

while user_input != 0:
    print("1: Show the Seats\n2: Choose the movie\n3: Choose movie language\n4: Show the time\n5: Buy a Ticket\n6: Statistics\n7: Show booked Tickets User Info\n0: Exit")
    print(50*"-")
    user_input = int(input())

    if user_input == 1:
        s.show_the_seats()
        time.sleep(2)
# New object is created for the Theater class in theater_info.py 
    elif user_input == 2:
    
        theater_class = theater_info.Theater() #Object created
        theater_class.movie_name() # call the movie method in Theater class with theater_class object
    
    elif user_input == 3:
            theater_class.movie_language()  # call the movie_language in Theater class with theater_class object
    

    elif user_input == 4:
            theater_class.timing() # call the movie timing in Theater class with theater_class object
    
  

    elif user_input == 5:
        t = theater_info.tickets()
        if t.book_row<=no_of_rows and t.book_column<=no_of_seats :
            b,current_income=t.buy_ticket(total_seats,no_of_rows,total_income,total_seats_booked)
            if b != None:
                total_income = total_income + current_income
            if b == True:
                total_seats_booked += 1
        else:
            print("you are trying to book the wrong seat")
            print(50*"-")   
        time.sleep(2)

    elif user_input == 6:
        t1=st.stats(total_seats_booked,total_seats,current_income,total_income)

    elif user_input == 7:
        u1=user_info.user_info()
        checkR = int(input("Enter the row you want to check: "))
        checkC = int(input("Enter the column you want to check: "))
        print(50*"-")
        u1.booked_tickets_user_info(checkR, checkC,current_income)

    elif user_input == 8:
        u1=user_info.user_info()


