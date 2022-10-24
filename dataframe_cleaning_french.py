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
    
         print("######################################")
         print("#      Suppression des doublons      #")
         print("######################################")
         print()
         print()
         print("Veuillez patienter, analyse en cours...")
         
         dataframe_clear = dataframe.drop_duplicates()
         
         print(f"\n>>>>>>>> Un total de {len(dataframe)-len(dataframe_clear)} doublons ont été supprimées !\n")
    
    
    #
    # Daughter function for column processing
    #
    
    def by_column(dataframe):
        
        print("#################################")
        print("#      Analyse par colonne      #")
        print("#################################")
        print()
        print()
       
        
        # Column and menu presentation
        
        for index, column in dataframe.items():
            print(f"{separator}\nColonne {index}\n{separator}\n")
            print(f"{column}")
            print(f"{separator}\n")
            while True:
                choices_list = ["Afficher plus de lignes", "Afficher les valeurs uniques", "Chercher une valeur spécifique", "Remplacer toutes les NaN", "Remplacer des valeurs spécifiques", "Changer le type d'objet", "Supprimer les lignes avec une valeur spécifique", "Supprimer les lignes avec NaN", "Supprimer la colonne", "Passer à la colonne suivante", "Quitter le programme"]
                choices_answer = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
        
        
                # Actions menu
                
                print(f"{separator}\nNom de la colonne : {index} \nType de la colonne : {dataframe[index].dtype}\nValeurs manquantes: {round((dataframe[index].isnull().sum() / len(dataframe[index]) * 100), 6)} %\nLignes restantes : {len(dataframe[index])}\n")
                for index_list, value in enumerate(choices_list, 1):
                    print(index_list, value)
                choice = input(f"\nQuel est votre choix de 1 à {len(choices_list)}? ")
                while True:
                    if choice not in choices_answer:
                        choice = input(f"Veuillez faire un choix de 1 à {len(choices_list)} : ")
                    else:
                        choice = int(choice)
                        print()
                        break
        
        
                # Show more rows for this column
        
                if choice == 1:  
                    number_row = input("Combien de lignes voulez-vous afficher? ")
                    while True:
                        if number_row.isdigit():
                            number_row = int(number_row)
                            break
                        else:
                            number_row = input("Combien de lignes voulez-vous afficher? ")
                    
                    first_last = ["Du début de la colonne", "De la fin de la colonne"]
                    first_last_choice = ["1", "2"]
                    print("\nCes lignes doivent être celles :")
                    
                    for index_choice, element in enumerate(first_last, 1):
                        print(index_choice, element)
                    answer_2 = input(f"\nFaites un choix de 1 à {len(first_last_choice)} : ")
                    
                    while True:
                        if answer_2 not in first_last_choice:
                            answer_2 = input(f"Faites un choix de 1 à {len(first_last_choice)} : ")
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
                    
                    print("Analyse des valeurs uniques en cours...\n")    

                    unique_count = 0
                    
                    for i in dataframe[index].unique():
                        unique_count += 1
                        if unique_count == 500:
                            break
                    
                    if unique_count < 500:
                        print(dataframe[index].unique())
                        print()
                    else:
                        print(f">>>>>>>> Votre colonne a un nombre de valeurs uniques supérieure à {unique_count}, elles ne peuvent pas être affichés.\n\n")

        
                # Search for a specific value
        
                if choice == 3:
                
                    value_to_find = input("Les valeurs manquantes sont représentées par Na\nQuelle valeur cherchez-vous ? ")
                    result = (dataframe[index].eq(value_to_find)).any()
                    if result == True:
                        print(f"\n>>>>>>>> La valeur {value_to_find} est présente dans la colonne.\n")
                    else:
                        print(f"\n>>>>>>>> La valeur {value_to_find} est absente de la colonne.\n")
         
        
                # Replace NaN 
        
                if choice == 4:
                   
                    valeur = input("Par quelle valeur souhaitez-vous remplacer les valeurs manquantes? ")
                    dataframe[index] = dataframe[index].fillna(valeur)
                    print("\n>>>>>>>> Vos valeurs ont été rempalcées.\n")    
             
        
                # Replace a specific value      
        
                if choice == 5:
                
                    old_value = input("Quelle valeur souhaitez-vous remplacer? ")
                    new_value = input("Quelle sera la nouvelle valeur ? Si NaN, appuyez sur entrée pour aller à l'étape suivante. ")
                    
                    type_value = ["string", "integer", "float", "boolean", "NaN"]
                    type_value_choice = ["1", "2", "3", "4", "5"]
                    
                    print()
                    for type_value_number, type_value_element in enumerate(type_value, 1):
                        print(type_value_number, type_value_element)
                        
                    type_choice = input("\nVeuillez choisir le type de votre valeur de 1 à 5 : ")
                    
                    while True:
                        if type_choice not in type_value_choice:
                            type_choice = input("Veuillez choisir le type de votre valeur de 1 à 5 : ")
                        else:                           
                            type_choice = int(type_choice)
                            if type_choice == 1:
                                try:
                                    new_value = str(new_value)
                                except:
                                    print(">>>>>>>> Une erreur est survenue, il n'est pas possible d'utiliser ce type.")
                            elif type_choice == 2:
                                try:
                                    new_value = int(new_value)        
                                except:
                                    print(">>>>>>>> Une erreur est survenue, il n'est pas possible d'utiliser ce type.")                                    
                            elif type_choice == 3:
                                try:
                                    new_value = float(new_value)
                                except:
                                    print(">>>>>>>> Une erreur est survenue, il n'est pas possible d'utiliser ce type.")                                    
                            elif type_choice == 4:
                                try:
                                    new_value = bool(new_value)
                                except:
                                    print(">>>>>>>> Une erreur est survenue, il n'est pas possible d'utiliser ce type.")                                    
                            elif type_choice == 5:
                                try:
                                    new_value = np.nan
                                except:
                                    print(">>>>>>>> Une erreur est survenue, il n'est pas possible d'utiliser ce type.")  
                            break
                    
                    dataframe[index].replace(old_value, new_value, inplace = True)
                    
                    print("\n>>>>>>>> Vos valeurs ont été remplacées.\n\n")
        
        
                # Change the object type for the column
                        
                if choice == 6:
                    type_list = ["string", "integer", "float", "boolean", "Ne rien faire"]
                    type_choice = ["1", "2", "3", "4", "5"]
                    
                    for type_list, element in enumerate(type_list, 1):
                        print(type_list, element)
                    type_answer = input("\nFaites un choix de 1 à 5 : ")
                    
                    while True:
                        if type_answer not in type_choice:
                            type_answer = input("Faites un choix de 1 à 5 : ")
                        else:
                            type_answer = int(type_answer)
                            break
                    
                    if type_answer == 1:
                        try:
                            dataframe[index] = dataframe[index].astype('string')
                            print("\n>>>>>>>> Votre colonne est maintenant de type string\n")
                        except:
                            print("\n>>>>>>>> Une erreur est survenue, le type n'a pas été changé. Veuillez traiter cette colonne manuellement ou remplacer les valeurs manquantes avant de changer le type.\n")
                        
                    if type_answer == 2:
                        try:
                            dataframe[index] = dataframe[index].astype('int64')
                            print("\n>>>>>>>> Votre colonne est maintenant de type integer\n")                    
                        except:
                            print("\n>>>>>>>> Une erreur est survenue, le type n'a pas été changé. Veuillez traiter cette colonne manuellement ou remplacer les valeurs manquantes avant de changer le type.\n")
                        
                    if type_answer == 3:
                        try:
                            dataframe[index] = dataframe[index].astype('float')
                            print("\n>>>>>>>> Votre colonne est maintenant de type float\n")                    
                        except:
                            print("\n>>>>>>>> Une erreur est survenue, le type n'a pas été changé. Veuillez traiter cette colonne manuellement ou remplacer les valeurs manquantes avant de changer le type.\n")
                        
                    if type_answer == 4:
                        try:
                            dataframe[index] = dataframe[index].astype('bool')
                            print("\n>>>>>>>> Votre colonne est maintenant de type boolean\n")                    
                        except:
                            print("\n>>>>>>>> Une erreur est survenue, le type n'a pas été changé. Veuillez traiter cette colonne manuellement ou remplacer les valeurs manquantes avant de changer le type.\n")
                        
                    if type_answer == 5:
                        break
          

                # Delete rows with specific value
                
                if choice == 7:
                    row_with_value = input("Quelle valeur souhaitez-vous supprimer? ")
                    try:
                        dataframe.drop(dataframe.loc[ dataframe[index] == row_with_value].index, inplace = True)
                        print(f"\n>>>>>>>> Les lignes ayant la valeur '{row_with_value}' ont bien été supprimée de la colonne '{index}.'")                        
                    except:
                        print(f"\n>>>>>>>> La valeur '{row_with_value}' n'est pas présente dans la colonne '{index}'.")
 
                           
                # Delete lines with NaN
        
                if choice == 8:
                    number_of_rows = dataframe[index].isnull().sum()
                    dataframe.dropna(subset=[index], inplace = True)
                    print(f">>>>>>>> {number_of_rows} lignes ont été supprimées !\n")
            
            
                # Delete the column
            
                if choice == 9:
                    delete_list = ["Oui", "Non"]
                    delete_list_choices = ["1","2"]
                    
                    for delete_index, delete_value in enumerate(delete_list, 1):
                        print(delete_index, delete_value)
                    print()
                        
                    while True:                         
                        delete_choice = input("Êtes-vous sûr de vouloir supprimer cette colonne? ")
                        if delete_choice not in delete_list_choices:
                            delete_choice = input("Êtes-vous sûr de vouloir supprimer la colonne? ")
                        else:
                            delete_choice = int(delete_choice)
                            if delete_choice == 1:
                                del dataframe[index]
                                print(f"\n>>>>>>>> La colonne {index} a été supprimée !\n")
                                break
                            else:
                                print(f"\n>>>>>>>> La colonne {index} a été sauvée, ouf !\n")
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
                    print("Programme terminé.")
                    sys.exit()
         
                    
        print("Toutes les colonnes ont été analysées.\n\n")         
        print("###############################")
        print("#      Analyse DataFrame      #")
        print("###############################")
        print()
        print()
        print(f"Voici un aperçu de votre DataFrame : \n\n{dataframe}\n  ")


    #
    # Main menu for central commands
    #
    
    print("###############################")
    print("#      Analyse DataFrame      #")
    print("###############################")
    print()
    print()
    print(f"Voici un aperçu de votre DataFrame : \n\n{dataframe}\n  ")
    
    menu_1 = ["Afficher plus de lignes", "Supprimer les doublons", "Traiter les colonnes une à une", "Enregistrer votre tableau en CSV", "Quitter"]
    choice_1 = ["1", "2", "3", "4", "5"]
    
    
    while True:
        for index, element in enumerate(menu_1, 1):
            print(index, element)
    
        answer_1 = input(f"\nFaites un choix de 1 à {len(choice_1)} : ")
    
        while True:
            if answer_1 not in choice_1:
                answer_1 = input(f"Faites un choix de 1 à {len(choice_1)} : ")
                continue
            else:
                answer_1 = int(answer_1)
                print()
                print()
                break


        # Display of the first or last n lines
    
        if answer_1 == 1:  
            number_row = input("Combien de lignes voulez-vous afficher? ")
            while True:
                if number_row.isdigit():
                    number_row = int(number_row)
                    break
                else:
                    number_row = input("Combien de lignes voulez-vous afficher? ")
            
            first_last = ["Du début du tableau", "De la fin du tableau"]
            first_last_choice = ["1", "2"]
            print("\nCes lignes doivent être celles :")
            
            for index, element in enumerate(first_last, 1):
                print(index, element)
            answer_2 = input(f"Faites un choix de 1 à {len(first_last_choice)} : ")
            
            while True:
                if answer_2 not in first_last_choice:
                    answer_2 = input(f"Faites un choix de 1 à {len(first_last_choice)} : ")
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
            file_name = input("Sous quel nom voulez-vous enregistrer votre fichier? ")
            print("\nVeuillez patienter, enregistrement de votre fichier en cours...")
            dataframe.to_csv(f"{file_name}.csv", index = False)
            print(f"\n>>>>>>>> Votre fichier a bien été enregistré sous le nom suivant : {file_name}.csv\n>>>>>>>> Le séparateur pour ce fichier est ','.\n")            


        # Exit the program        

        elif answer_1 == 5:
            print("Fin du programme.")
            sys.exit()
