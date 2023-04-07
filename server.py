from flask import Flask, render_template
#                                        redirect, request, session
app = Flask(__name__)


@app.route("/list", methods=["GET"])
def list_of_users():
    users = [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    return render_template("index.html", users = users)

if __name__ == "__main__":
    app.run(debug = True)


# **********************

#   Method: GET
#   grabbing everything in a list
#   URL: make it plural ex: "/todos"
#   Function: get_all_todos()
#             get_todos()

#   Method: GET
#   grabbing ONE of a particular list
#   URL: "/todo/<int:id>"
#        "/user/<int:id>"
#   Function: get_todo_by_id(id)
#             get_todo(id)

#   Method: GET
#   Displaying a form that will eventually refer to a list
#   URL: "/todo/form"
#   Function: display_todo_form()

#   Method: POST
#   Create a new item of a list
#   URL: "/todo/add"
#        "/todo/new"
#   Function: create_todo_list()
#             add_todo()
#             new_todo()

#   Method: POST-PUT
#   Updating an existing item of a list
#   URL: "/todo/update/<int:id>"
#        "/todo/edit/<int:id>"
#   Function: update_todo(id)
#             edit_todo(id)

#   Method: POST - DELETE
#   Deleting an existing item of a list
#   URL: "/todo/remove/<int:id>"
#        "/todo/delete/<int:id>"
#   Function: remove_todo(id)
#             delete_todo(id)

# **********************