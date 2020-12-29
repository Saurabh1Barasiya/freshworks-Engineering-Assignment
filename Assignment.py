
import json
import os   

# Here i import os module to clear the screen.

def collect_keys(data):

    # This function collect keys from data .

    l = []
    for key in data.keys():
        l.append(key)
    return l
    

def reading_data():

    # This function perform reading operation.

    with open("data.json",'r') as f:
        data = json.load(f)
        print(f"{data}")  
        collect_keys(data)
        return data    
        

def writing_data(data):   

        # This function perform writing operation.

        inner_dict = {'Married':'','Name':'','Salary':''}
        keys = collect_keys(data)
        k = input("Enter your key here : ").title()    
        if k in keys:
            raise Exception("You can not write this key because this key is already present in json file. ")
        else:
            inner_dict['Married'] = bool(input("Enter value for Married  ( True or False ): ")) 
            inner_dict['Name'] = input("Enter value for Name : ").title()
            inner_dict['Salary'] = int(input("Enter value for Salary : "))
            with open('data.json', 'w') as f:
                new_data = {k:inner_dict}
                data.update(new_data) 
                new_data = data    
                json.dump(data,f,indent=4,sort_keys=True)   
                print("Data added successfully")     
                return new_data


def deleting_data(data):

    # This function perform delection operation.

    keys = collect_keys(data)
    print("Your options are",keys)   
    key = input("Please enter key that you want to delete : ").title()
    del data[key]    
    with open('data.json', 'w') as f:
        json.dump(data,f,indent=4,sort_keys=True)
        print("Delection performed successfully ")

def Clear():
    input("")
    return os.system('cls')  

if __name__ == "__main__":
    r_data = None
    # clear = lambda:os.system('cls')
    while True:
        print("\t ********** Welcome to Key-Value data store system ********** ")
        print("")
        print("\t \t 1. For Reading Json file. ")
        print("\t \t 2. For Writing in Json file. ")
        print("\t \t 3. For Deleting in Json file. ")
        print("\t \t 4. For Exit. ")

        choice = int(input("Please enter your choice : ")) 
        
        if  choice == 1:
           r_data = reading_data()
        
        elif choice == 2:
            if r_data == None:
                print(" You read data frist")
                continue
            else:
                r_data = writing_data(r_data)
             
        elif choice == 3:
            if r_data == None:
                print(" You read data frist")
                continue
            else:
                 deleting_data(r_data) 
        elif choice == 4:
            exit() 
        Clear()
        