#Progress made until Day5: https://www.udemy.com/course/the-python-mega-course/learn/lecture/34603964#overview
todos = []
while True:
    user_input = input("What would you like to do with the todo list? Choose between 'add','edit', 'complete','show' and 'exit'")
    match user_input:
        case "add":
            item_todo = input("Sweet, let's hear it, tell me your task and i will add it to the list")
            todos.append(item_todo)
            print("Item added to to-do list!")
        case "edit":
            if len(todos) == 0:
                print("There's nothing in the todo list to edit, maybe add an item first?")
            else:
                id2edit = int(input(f"which item would you like to modify? choose among 1 ~ {len(todos)}"))
                todo_edited = input("What would you like to put in for the one you chose instead?")
                todos[id2edit-1] = todo_edited
                print("Item successfully modified!")
        case "show":
            #displaying all to-do items in the list with a preceding index followed by a dash
            if len(todos) == 0:
                print("Got nothing in your to-do list, kudos!")
            else:
                print("Displaying content in to-do list:")
                for ind,todo in enumerate(todos):
                    print(f"{ind + 1} - {todo}")

        case "complete":
            if len(todos) == 0:
                print("There's nothing to comlete, add an item to the list maybe?")
            else:
                #mark an item as complete and remove it out of the list
                id2edit = int(input(f"which item would you like to mark as completed? choose among 1 ~ {len(todos) + 1}"))
                todos.pop(id2edit-1)
                print("Item successfully marked as complete!")

        case "exit":
            break


print("Bye!")





