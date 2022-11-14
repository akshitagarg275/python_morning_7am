#importing todo helper utility file
import todo_helper


def main():
    run = 1 
    todo_helper.create_table()


    while run :
        print("Press 1: To read data")
        print("Press 2: To add data")
        print("Press 3: To update data")
        print("Press 4: To delete data")
        print("Press 5: To exit")

        ch = input("Enter your choice: ")

        if ch == "1":
            todo_helper.read_todos()
        elif ch == "2":
            add_todo = input("Enter the new task: ")
            todo_helper.add_todo(add_todo)
        elif ch == "3":
            idx = int(input("Enter the id of todo"))
            update_task = input("Enter the updated task: ")
            todo_helper.update_task(idx, update_task)
        
        elif ch == "4":
            idx = int(input("Enter the id of todo"))
            todo_helper.delete_task(idx)
        elif ch == "5":
            run = 0
    
    todo_helper.close_connection()

if __name__ == '__main__':
    main()