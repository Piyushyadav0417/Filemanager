import os

def Creat_file(Filename):
    try:
        with open(Filename, 'x') as f:
            print(f"{Filename} is created successfuly!")
    except FileExistsError:
        print(f"{Filename} is all ready exists!")
    except Exception as e:
        print("An error occured")
        
    
def View_files(Filename):
    try:
        files = os.listdir()
        if not files:
            print("No file found")
        else:
            print("Files in directory!")
            for file in files:
                print(file)
    except Exception as e:
        print("An error occurred")    
def Delet_file(Filename):
    try:
        os.remove(Filename)
        print(f"{Filename} Deleted Succefully !!")
    except FileNotFoundError:
        print("{Filename} not found")
    except Exception as e:
        print("An error occurred") 
    
def Read_file(Filename):
    try:
        with open(Filename, 'r') as f:
            content = f.read()
            print(f"The{Filename} Content is:\n {content}")
    except FileNotFoundError:
        print("{Filename} not found")
    except Exception as e:
        print("An error occurred")   
    
    
def Edit_file(Filename):
    try:
        with open(Filename, 'a') as f:
            content = int(input("Write in file"))
            f.write(content)
    except FileNotFoundError:
        print("{Filename} not found")
    except Exception as e:
        print("An error occurred") 
        
          
def main():
    while True:
        print("FILE MANAGEMENT APP: ")
        print("1: Create File: ")
        print("2: View Files: ")
        print("3: Delete File: ")
        print("4: Read File: ")
        print("5: Edit File: ")
        print("6: Exist: ")
        try:
            choice = int(input("Enter Your choice: ))
            if choice == 1:
					Filename = input("Enter The file name: )		   
                    Create_file(Filename)
            elif choice == 2:
                    View_files()
            elif choice == 3:
					Filename = input("Enter The file name: )				 
                    Delet_file(Filename)
            elif choice == 4:
					Filename = input("Enter The file name: )	
                    Read_file(Filename)
            elif choice == 5:
					Filename = input("Enter The file name: )					 	
                    Edit_file(Filename)
            elif choice == 6:
                    print("Closing The App..............)
		    else:
					print("Please Enter an valid Syntax")
