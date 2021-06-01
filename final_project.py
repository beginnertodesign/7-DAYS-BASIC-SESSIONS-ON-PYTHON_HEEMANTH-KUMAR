#final project by COLLABORATIVE LEARNING
#PROJECT NAME:checking my fav house before buying it and printing the details after the complete selection of house requirements

#VARIOUS REQUIRED LISTS AND DICTIONARIES 
area_list=["Quinton's colony","Zeberg's colony","Malkom's colony","Codybank's colony","Famous colony"]
budget_list=[2500000,3000000,5000000,10000000]
sq_ft_list=['200x400','600x800','1000x1200','1400x1600','1800x2000','100x300','500x700','900x1100','1300x1500','1700x1900']
direction_list=["EAST","WEST","NORTH","SOUTH"]
dictionary_rooms={'1':'2-bed_rooms,2-bath_rooms,1-kitchen_room,1-store_room,1-normal_room','2':'3-bed_rooms,2-bathroom,1-store_room,1-kitchen_room','3':'1-bed_room,1-bath_room,1-store_room,1-kitchen_room'}

#AREA FUNCTION TO SHOW WHICH AREA WAS SELECTED
def area(colony):
    print("hi welcome to: ",colony)
    print("----------------------------------------------------------------------")
    print("This is the area section in your selected colony")
    
    if(colony==area_list[0] or colony==area_list[1] or colony==area_list[2] or colony==area_list[3] or colony==area_list[4]):
        sq_ft()

#SELECT_NO_OF_ROOMS TYPE FUNCTION WHICH SHOWS ACCORDING TO SQ_FT
def select_no_of_rooms(sq_ft):
    print("/n")
    print("----------------------------------------------------------------------")
    print("SELECT_NO_OF_ROOMS")
    print("----------------------------------------------------------------------")
    print("No.of room designs available for your sq_ft: ",sq_ft)
    print('''1.2-bed_rooms,2-bath_rooms,1-kitchen_room,1-store_room,1-normal_room
2.3-bed_rooms,2-bathroom,1-store_room,1-kitchen_room
3.1-bed_room,1-bath_room,1-store_room,1-kitchen_room''')
    print("Select any one option from 1,2,3")
    print("----------------------------------------------------------------------")
    select_no_of_rooms.dic=input("Enter option: ")
    if(select_no_of_rooms.dic in dictionary_rooms):
        return select_no_of_rooms.dic
    else:
        print("THE SELECTED ROOMS ARE NOT THERE EVEN IF YOU ENTERED WRONG NUMBER THE SUMMARY WILL BE GIVEN BUT IT'S NOT ACCEPTED")


#THIS IS DIRECTION FUNCTION INVOKED BY SQ_FT
#DIRECTION FUNCTION TO SHOW YOUR RESPECTIVE CHOOSEN DIRECTION AND THE SENDING THIS TO SELECTION_OF_NO_OF_ROOMS
def direction(sq_ft):
    print("\n----------------------------------------------------------------------")
    print("SELECT HOUSE FACING")
    print("----------------------------------------------------------------------")
    print("Choose your facing from directions list: ")
    print(direction_list)
    print("----------------------------------------------------------------------")
    direction.directn=input("Enter your fav facing: ")
    if(direction.directn in direction_list):
        select_no_of_rooms(sq_ft)
    else:
        print("THE SELECTED DIRECTION IS NOT IN THE LIST")
    

#SQ_FT FUNCTION INVOKED AFTER SELECTING COLONY AREA
def sq_ft():
    
    print("\n----------------------------------------------------------------------")
    print("SELECT SQUARE FEET") 
    print("----------------------------------------------------------------------")
    print(sq_ft_list)
    print("----------------------------------------------------------------------")
    sq_ft.sq_ft=input("Enter square feet: ")
    if(sq_ft.sq_ft in sq_ft_list):
        direction(sq_ft)
    else:
        print("CHOSEN SQUARE FEET IS NOT IN OUR LIST")

#START OF HOUSING PLAN PROJECT

c="Welcome to new housing colony.\n we're so glad to meet you."
print(c)
print("""
----------------------------------------------------------------------
below are the areas that we're offering to you select you residency.
->Quinton's colony
->Zeberg's colony
->Malkom's colony
->Codybank's colony
->Famous colony
Enter any of your interested colony name to move forward else press 1 (or) 0 to exit from process""")
print("\n")
print("----------------------------------------------------------------------")
print("SELECT AREA")
print("----------------------------------------------------------------------")
colony=input("Enter area: ")


#CHECKING OF THE COLONY NAME IN LIST AND THEN PROCCEDING WITH PROCEDURE FURTHER
print("\n")
print("----------------------------------------------------------------------")
if(colony in area_list):
    print("SELECT BUDGET")
    print("----------------------------------------------------------------------")
    print("Here are budgets list for buying a house and the same budget follows for all colony areas: ")
    print(budget_list)
    print("----------------------------------------------------------------------")
    budget=int(input("Enter your budget: "))
    if(budget in budget_list):
        area(colony)
    else:
        print("THE ENTERED BUDGET DOESN'T MATCH OOPS!!!")
        

    
    #SUMMARY OF THE SELECTED HOUSING PLAN
    print("\n\n----------------------------------------------------------------------")
    print("THE SUMMARY OF YOUR HOUSE PLAN:")
    print("----------------------------------------------------------------------")
    print("YOUR COLONY: ",colony)
    print("YOUR BUDGET: ",budget)
    print("YOUR SQUARE FEET: ",sq_ft.sq_ft)
    print("YOUR FAV FACING: ",direction.directn)
    if(select_no_of_rooms.dic in dictionary_rooms):
        print("YOUR SELECTED ROOM TYPE: ",select_no_of_rooms.dic)
    else:
        print("YOUR SUMMARY NOT ACCEPTED BECAUSE THE NO.OF ROOMS TYPE YOU CHOSEN IS INVALID")
    
    print("----------------------------------------------------------------------")
    print("----------THANK YOU FOR BOOKING YOUR SLOT IN OUR HOUSING COLONY--------")
elif(colony=='1' or colony=='0'):
    print("Sorry if any mistakes from our side and your cancellation of process is successful")
else:
    print("THE WRITTEN COLONY IS NOT THERE IN OUR LIST")


