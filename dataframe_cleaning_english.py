def dataframe_cleaning(dataframe):

    
    # Import of the necessary modules, variables and options

    import sys
    import numpy as np
    import pandas as pd
    
    pd.options.display.max_columns = 999
    separator = "*" * 30    


    #
    # Daughter function for deleting duplicates
    #
    
    def del_duplicates(dataframe):
    
         print("#################################")
         print("#      Removing duplicates      #")
         print("#################################")
         print()
         print()
         print("Please wait, analysis in progress...")
         
         dataframe_clear = dataframe.drop_duplicates()
         
         print(f"\n>>>>>>>> A total of  {len(dataframe)-len(dataframe_clear)} duplicates have been removed !\n")
    
    
    #
    # Daughter function for column processing
    #
    
    def by_column(dataframe):
        
        print("################################")
        print("#      Analysis by column      #")
        print("################################")
        print()
        print()
       
        
        # Column and menu presentation
        
        for index, column in dataframe.items():
            print(f"{separator}\Column {index}\n{separator}\n")
            print(f"{column}")
            print(f"{separator}\n")
            while True:
                choices_list = ["Show more rows", "Show single values", "Search for a specific value", "Replace all NaN", "Replace specific values", "Change object type", "Delete rows with a specific value", "Delete rows with NaN", "Delete column", "Go to next column", "Exit program"]
                choices_answer = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
        
        
                # Actions menu
                
                print(f"Name of the column : {index} \nColumn type : {dataframe[index].dtype}\nMissing data: {round((dataframe[index].isnull().sum() / len(dataframe[index]) * 100), 6)} %\nRemaining rows : {len(dataframe[index])}\n")
                for index_list, value in enumerate(choices_list, 1):
                    print(index_list, value)
                choice = input(f"\nWhat is your choice from 1 to {len(choices_list)}? ")
                while True:
                    if choice not in choices_answer:
                        choice = input(f"Please make a choice from 1 to {len(choices_list)} : ")
                    else:
                        choice = int(choice)
                        print()
                        break
        
        
                # Show more rows for this column
        
                if choice == 1:  
                    number_row = input("How many lines do you want to display? ")
                    while True:
                        if number_row.isdigit():
                            number_row = int(number_row)
                            break
                        else:
                            number_row = input("How many lines do you want to display? ")
                    
                    first_last = ["From the beginning of the column", "From the end of the column"]
                    first_last_choice = ["1", "2"]
                    print("\nThese lines must be those : ")
                    
                    for index_choice, element in enumerate(first_last, 1):
                        print(index_choice, element)
                    answer_2 = input(f"\nMake a choice from 1 to {len(first_last_choice)} : ")
                    
                    while True:
                        if answer_2 not in first_last_choice:
                            answer_2 = input(f"Make a choice from 1 to {len(first_last_choice)} : ")
                            continue
                        else:
                            answer_2 = int(answer_2)
                            print()
                            print()
                            break
                    
                    if answer_2 == 1:
                        pd.options.display.max_rows = number_row
                        print(dataframe[index].head(number_row))
                        pd.options.display.max_rows = 15
                        print()
                        print()
                    else:
                        pd.options.display.max_rows = number_row
                        print(dataframe[index].tail(number_row))
                        pd.options.display.max_rows = 15
                        print()
                        print()
         

                # Display unique values
                
                if choice == 2:
                    
                    print("Analysis of unique values in progress...\n")    

                    unique_count = 0
                    
                    for i in dataframe[index].unique():
                        unique_count += 1
                        if unique_count == 500:
                            break
                    
                    if unique_count < 500:
                        print(dataframe[index].unique())
                        print()
                    else:
                        print(f">>>>>>>> Your column has a number of unique values greater than {unique_count}, they cannot be displayed.\n\n")

        
                # Search for a specific value
        
                if choice == 3:
                
                    value_to_find = input("Missing values are represented as Na\nWhat value are you looking for? ")
                    result = (dataframe[index].eq(value_to_find)).any()
                    if result == True:
                        print(f"\n>>>>>>>> The value {value_to_find} is present in the column.\n")
                    else:
                        print(f"\n>>>>>>>> The value {value_to_find} is missing from the column.\n")
         
        
                # Replace NaN 
        
                if choice == 4:
                   
                    valeur = input("What value do you want to replace the missing values with? ")
                    dataframe[index] = dataframe[index].fillna(valeur)
                    print("\n>>>>>>>> Your values have been replaced.")    
             
        
                # Replace a specific value      
        
                if choice == 5:
                
                    old_value = input("What value do you want to replace? ")
                    new_value = input("What will be the new value? If NaN, press enter to go to the next step.")
                    
                    type_value = ["string", "integer", "float", "boolean", "NaN"]
                    type_value_choice = ["1", "2", "3", "4", "5"]
                    
                    print()
                    for type_value_number, type_value_element in enumerate(type_value, 1):
                        print(type_value_number, type_value_element)
                        
                    type_choice = input("\nPlease select your value type from 1 to 5: ")
                    
                    while True:
                        if type_choice not in type_value_choice:
                            type_choice = input("Please select your value type from 1 to 5: ")
                        else:                           
                            type_choice = int(type_choice)
                            if type_choice == 1:
                                try:
                                    new_value = str(new_value)
                                except:
                                    print(">>>>>>>> An error has occurred, it is not possible to use this type.")
                            elif type_choice == 2:
                                try:
                                    new_value = int(new_value)        
                                except:
                                    print(">>>>>>>> An error has occurred, it is not possible to use this type.")                                    
                            elif type_choice == 3:
                                try:
                                    new_value = float(new_value)
                                except:
                                    print(">>>>>>>> An error has occurred, it is not possible to use this type.")                                    
                            elif type_choice == 4:
                                try:
                                    new_value = bool(new_value)
                                except:
                                    print(">>>>>>>> An error has occurred, it is not possible to use this type.")                                    
                            elif type_choice == 5:
                                try:
                                    new_value = np.nan
                                except:
                                    print(">>>>>>>> An error has occurred, it is not possible to use this type.")  
                            break
                    
                    dataframe[index].replace(old_value, new_value, inplace = True)
                    
                    print("\n>>>>>>>> Your values have been replaced.\n\n")
        
        
                # Change the object type for the column
                        
                if choice == 6:
                    type_list = ["string", "integer", "float", "boolean", "Do nothing"]
                    type_choice = ["1", "2", "3", "4", "5"]
                    
                    for type_list, element in enumerate(type_list, 1):
                        print(type_list, element)
                    type_answer = input("\nMake a choice from 1 to 5: ")
                    
                    while True:
                        if type_answer not in type_choice:
                            type_answer = input("Make a choice from 1 to 5: ")
                        else:
                            type_answer = int(type_answer)
                            break
                    
                    if type_answer == 1:
                        try:
                            dataframe[index] = dataframe[index].astype('string')
                            print("\n>>>>>>>> Your column is now of type string\n")
                        except:
                            print("\n>>>>>>>> An error occurred, the type was not changed. Please edit this column manually or replace missing values before changing the type.\n")
                        
                    if type_answer == 2:
                        try:
                            dataframe[index] = dataframe[index].astype('int64')
                            print("\n>>>>>>>> Your column is now of type integer\n")                    
                        except:
                            print("\n>>>>>>>> An error occurred, the type was not changed. Please edit this column manually or replace missing values before changing the type.\n")
                        
                    if type_answer == 3:
                        try:
                            dataframe[index] = dataframe[index].astype('float')
                            print("\n>>>>>>>> Your column is now of type float\n")                    
                        except:
                            print("\n>>>>>>>> An error occurred, the type was not changed. Please edit this column manually or replace missing values before changing the type.\n")
                        
                    if type_answer == 4:
                        try:
                            dataframe[index] = dataframe[index].astype('bool')
                            print("\n>>>>>>>> Your column is now of type boolean\n")                    
                        except:
                            print("\n>>>>>>>> An error occurred, the type was not changed. Please edit this column manually or replace missing values before changing the type.\n")
                        
                    if type_answer == 5:
                        break
          

                # Delete rows with specific value
                
                if choice == 7:
                    row_with_value = input("What value would you like to delete? ")
                    try:
                        dataframe.drop(dataframe.loc[ dataframe[index] == row_with_value].index, inplace = True)
                        print(f"\n>>>>>>>> The lines with the value '{row_with_value}' have been removed from the column '{index}.'\n")
                        
                    except:
                        print(f"\n>>>>>>>> The value '{row_with_value}' is not present in the column '{index}'.\n")
 
                           
                # Delete lines with NaN
        
                if choice == 8:
                    number_of_rows = dataframe[index].isnull().sum()
                    dataframe.dropna(subset=[index], inplace = True)
                    print(f">>>>>>>> {number_of_rows} row have been removed!\n")
            
            
                # Delete the column
            
                if choice == 9:
                    delete_list = ["Yes", "No"]
                    delete_list_choices = ["1","2"]
                    
                    for delete_index, delete_value in enumerate(delete_list, 1):
                        print(delete_index, delete_value)
                    print()
                        
                    while True:                         
                        delete_choice = input("Are you sure you want to delete this column? ")
                        if delete_choice not in delete_list_choices:
                            delete_choice = input("Are you sure you want to delete this column? ")
                        else:
                            delete_choice = int(delete_choice)
                            if delete_choice == 1:
                                del dataframe[index]
                                print(f"\n>>>>>>>> The column {index} have been removed!\n")
                                break
                            else:
                                print(f"\n>>>>>>>> The column {index} have been saved, phew!\n")
                                break
                            
                    if delete_choice != 1:
                        continue
                    else:
                        break
                    break
                        
        
                # Go to the next column
        
                if choice == 10:
                    break
       
            
                # Exit the program
        
                if choice == 11:
                    print("Program finished.")
                    sys.exit()
                            
        print("All columns have been analyzed.\n\n")         
        print("################################")
        print("#      DataFrame Analysis      #")
        print("################################")
        print()
        print()
        print(f"Here is an overview of your DataFrame : \n\n{dataframe}\n  ")


    #
    # Main menu for central commands
    #
    
    print("################################")
    print("#      DataFrame Analysis      #")
    print("################################")
    print()
    print()
    print(f"Here is an overview of your DataFrame : \n\n{dataframe}\n  ")
    
    menu_1 = ["Show more rows", "Delete duplicates", "Process columns one by one", "Save your table in CSV file", "Exit"]
    choice_1 = ["1", "2", "3", "4", "5"]
    
    
    while True:
        for index, element in enumerate(menu_1, 1):
            print(index, element)
    
        answer_1 = input(f"\nMake a choice of 1 to {len(choice_1)} : ")
    
        while True:
            if answer_1 not in choice_1:
                answer_1 = input(f"Make a choice of 1 to {len(choice_1)} : ")
                continue
            else:
                answer_1 = int(answer_1)
                print()
                print()
                break


        # Display of the first or last n lines
    
        if answer_1 == 1:  
            number_row = input("How many rows would you like to display? ")
            while True:
                if number_row.isdigit():
                    number_row = int(number_row)
                    break
                else:
                    number_row = input("How many rows would you like to display? ")
            
            first_last = ["From the beginning of the dataframe", "From the end of the dataframe"]
            first_last_choice = ["1", "2"]
            print("\nThese lines must be those:")
            
            for index, element in enumerate(first_last, 1):
                print(index, element)
            answer_2 = input(f"Make a choice of 1 to {len(first_last_choice)} : ")
            
            while True:
                if answer_2 not in first_last_choice:
                    answer_2 = input(f"Make a choice of 1 to {len(first_last_choice)} : ")
                    continue
                else:
                    answer_2 = int(answer_2)
                    print()
                    print()
                    break
            
            if answer_2 == 1:
                pd.options.display.max_rows = number_row
                print(dataframe.head(number_row))
                pd.options.display.max_rows = 15
                print()
                print()
            else:
                pd.options.display.max_rows = number_row
                print(dataframe.tail(number_row))
                pd.options.display.max_rows = 15
                print()
                print()


        # Removing duplicates
            
        if answer_1 == 2:
            del_duplicates(dataframe)
            continue


        # Process the columns one by one
        
        if answer_1 == 3:
            by_column(dataframe)
            continue
                

        # Save the table     
        
        if answer_1 == 4:
            file_name = input("What name do you want to save your file under? ")
            print("\nPlease wait, your file is being saved...")
            dataframe.to_csv(f"{file_name}.csv", index = False)
            print(f"\n>>>>>>>> Your file has been saved under the following name : {file_name}.csv\nThe separator for this file is ','\n")            


        # Exit the program        

        elif answer_1 == 5:
            print("End of the program.")
            sys.exit()
