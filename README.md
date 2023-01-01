# To-Do-List-in-python
This is an attempt to create a simple yet effective and functional to do list app using python programming language and python notebook. 
There will be 2 versions of the code.
1. The first version will be a simple code of python program which will be functional and straight forward.
2. The second version will be a little upgrade with GUI and a bit user friendly.

##**To Do List V1.1**

The To Do List V1.1 is a simpler and straight forward version of the to do list code.
It has the following functions:
1. Add a new task
2. view tasks
3. Edit a task
4. Mark a task as complete
5. Delete an existing task
6. Set a reminder

###**1. Add a new task**

This function first run a function check_file(file_name) to see if the csv file with all the to do list task is already at the desired path, if not then this piece of code/function will create a new file with the required headers.
Then the Add_task() function will get the number of task to be inserted by the users followed by the loop to get the same number of inputs from users such as :
* TaskNo
* TaskName
* TargetDate (Targetted date to achieve the task by user)
* TaskDate (Date oin which the task was created)
* PercentageAch (% of which task has been achieved)
After taking above details from the user the function feeds these details in the To Do List.csv 

**2. view tasks**

Although currently there are not more than 5-10 task in the To Do List.csv but after a period of time user may have n number of task and so wants to view the details of a particular task. This function of the program helps in getting the detail of a single task for the convenience of the user it will print the list of the task available in the To Do List.csv sheet along with the details but if the user is aware of the task no. the user can ignore the lsit and go ahead and type in the task no. to get the details but if the user do not remember the task number then can look through the list and fetch the details of the particular task.

Note: Although the list will already have the details of all te task, this function is built with the vision of v3.0 or future version which will include some detailed analysis or charts of every task in comaprision to other tasks! and those details will not be available in the list that is printed by default and so this view_task function will be helpful to get those analyticals results of the desired task number.

**3. Edit a task**

Again for the convenience of the user this function will also print the list of task available in the To Do List.csv sheet before hand, then the user can put in the task number for wich they need to edit the task details.
After typing in the the task no., the code will ask the user updated details for the task such as :
* TaskNo
* TaskName
* TargetDate (Targetted date to achieve the task by user)
* TaskDate (Date oin which the task was created)
* PercentageAch (% of which task has been achieved)
The code is using the index of the task no and then updating all the values of all the columns of the record at that particular index.

**4. Mark a task as complete**

This function again for the convenience of the user will print the list of task available in the To Do List.csv sheet before hand, then the user can put in the task number wich they want to mark as complete.
The function will identify the index of the task number which the user wants to mark as complete, it will then use the at index functionality of pandas dataframe to update the PercentageAch column as 100% and save this dataframe as the To Do List.csv in the original path replacing the old sheet.

**5. Delete an existing task**

This function again for the convenience of the user will print the list of task available in the To Do List.csv sheet before hand, then the user can put in the task number wich they want to delete. The function will use the dataframe.loc functionality of the pandas dataframe and will ommit the row/datawhich matches with the mentioned task number and the new dataframe is saved as To Do List.csv in the original path replacing the old sheet.

**6. Set a reminder**

At the moment this function isnot developed to keep the codes simple, this function will be addressed in the V3.0 or future version of the codes.
