import traceback

first_entryFlag = True #need this flag for subsequent "what else?"

while True:
    try:
        if first_entryFlag:
            user_input = input("What happened today?\n" )
            first_entryFlag = False # set to false after first entry prompt
        else: 
            user_input = input("What else? \n")

        if user_input.lower() == "done for now":
            print("Entry Saved. Byebye")
            #file.write(input + "\n")
            break #breaks out of while loop

        with open('diary.txt', 'a') as file:
            # w is overiding the file everytime, i am using a to see past recordings into .txt file
            file.write(user_input + "\n")
            # user_input = input("What else? \n")
            # file.write(user_input + "\n")
        

    except NameError as e:
        #NameError undetected indent errors are what are cuaseing my errors
        print(f"An exception occurred: {e}")
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")

        #keyBoard interrupt
    

    

    
  