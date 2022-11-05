#!/usr/bin/env python
# coding: utf-8

# In[2]:


from flask import Flask, request, jsonify

app = Flask(__name__)

PORT = 8000
HOST = "127.0.0.1"

# Example User Data
users_data = [
    {"id": 1, "name": "Kane", "type": "admin"}
]

# Example Recipes Data
recipes = [
    {"id": 1, "user_id": 1, "steps": "bake cookies"},
    {"id": 2, "user_id": 1, "steps": "cook rice"}
]


# GET ENDPOINT for /users/:user_id
@app.get("/users/<int:user_id>")
def get_user(user_id: int):
    # Iterate through the users_data list
    for user in users_data:
        # If user id found
        if user["id"] == user_id:
            # Return the user data as JSON
            return jsonify(user)
    # If user not found, return a JSON containing error message, and status code
    return jsonify({"error": "User Not Found !!!"}), 415


# POST ENDPOINT for /users/:user_id
@app.post("/users/<int:user_id>")
def post_user(user_id: int):
    # If request data is a JSON data
    if request.is_json:
        # Get response data
        response = request.get_json()

        # Put ID into the response
        response["id"] = user_id

        # Check response have valid fields
        if len(response.keys()) == 3                 and "id" in response.keys()                 and "name" in response.keys()                 and "type" in response.keys():
            # Insert this data into users_data list
            users_data.append(response)
            # Return the response as JSON with status code
            return jsonify(response), 200
        else:
            return jsonify({"error": "JSON has invalid fields !!!"}), 400
    # If response was not JSON, return a JSON containing
    # error message, and status code
    return jsonify({"error": "Request must be JSON !!!"}), 415


# PUT ENDPOINT for /users/:user_id
@app.put("/users/<int:user_id>")
def put_user(user_id: int):
    # If request data is a JSON data
    if request.is_json:
        # Get response data
        response = request.get_json()

        # Check if user_id exists in the users_data list
        index = -1
        for i, user in enumerate(users_data):
            # If user found
            if user["id"] == user_id:
                index = i
                break
        # If user not found
        if index == -1:
            return jsonify({"error": f"No data found for ID {user_id}"}), 400

        # Check response have valid fields
        if "name" not in response.keys() and "type" not in response.keys():
            return jsonify({"error": "Malformed request."}), 400

        # Insert this data into users_data list
        users_data[index]["name"] = request.json.get("name")
        users_data[index]["type"] = request.json.get("type")

        # Return the updated user data as JSON with status code
        return jsonify(users_data[index]), 200

    # If response was not JSON, return a JSON containing
    # error message, and status code
    return jsonify({"error": "Request must be JSON !!!"}), 415


# DELETE ENDPOINT for /users/:user_id
@app.delete("/users/<int:user_id>")
def delete_user(user_id: int):
    # Check if user_id exists in the users_data list
    index = -1
    for i, user in enumerate(users_data):
        # If user found
        if user["id"] == user_id:
            index = i
            break
    # If user not found
    if index == -1:
        return jsonify({"error": f"No data found for ID {user_id}"}), 400
    else:
        # Store the user data to send
        del_data = users_data[index]

        # Delete the user data
        del users_data[index]

        # Return the deleted user data as JSON with status code
        return jsonify(del_data), 200


# GET ENDPOINT for /users/:user_id/recipes/:recipe_id
@app.get("/users/<int:user_id>/recipes/<int:recipe_id>")
def get_recipe(user_id: int, recipe_id: int):
    # Iterate through the recipes list
    for recipe in recipes:
        # If user id and recipe id found
        if recipe["id"] == recipe_id and recipe["user_id"] == user_id:
            # Return the recipe data as JSON
            return jsonify(recipe)
    # If user not found, return a JSON containing error message, and status code
    return jsonify({"error": "Recipe Not Found !!!"}), 415


# POST ENDPOINT for /users/:user_id/recipes/:recipe_id
@app.post("/users/<int:user_id>/recipes/<int:recipe_id>")
def post_recipe(user_id: int, recipe_id: int):
    # If request data is a JSON data
    if request.is_json:
        # Get response data
        response = request.get_json()

        # Put recipe ID and user ID into the response
        response["id"] = recipe_id
        response["user_id"] = user_id

        # Check response have valid fields
        if len(response.keys()) == 3                 and "id" in response.keys()                 and "user_id" in response.keys()                 and "steps" in response.keys():
            # Insert this data into recipes list
            recipes.append(response)
            # Return the response as JSON with status code
            return jsonify(response), 200
        else:
            return jsonify({"error": "JSON has invalid fields !!!"}), 400
    # If response was not JSON, return a JSON containing
    # error message, and status code
    return jsonify({"error": "Request must be JSON !!!"}), 415


# PUT ENDPOINT for /users/:user_id/recipes/:recipe_id
@app.put("/users/<int:user_id>/recipes/<int:recipe_id>")
def put_recipe(user_id: int, recipe_id: int):
    # If request data is a JSON data
    if request.is_json:
        # Get response data
        response = request.get_json()

        # Check if recipe_id and user_id exists in the recipes list
        index = -1
        for i, recipe in enumerate(recipes):
            # If recipe found
            if recipe["id"] == recipe_id and recipe["user_id"] == user_id:
                index = i
                break
        # If recipe not found
        if index == -1:
            return jsonify({"error": f"No data found for Recipe ID {recipe_id} and User ID {user_id}"}), 400

        # Check response have valid fields
        if "steps" not in response.keys() and "type" not in response.keys():
            return jsonify({"error": "Malformed request."}), 400

        # Insert this data into recipes list
        recipes[index]["steps"] = request.json.get("steps")

        # Return the updated user data as JSON with status code
        return jsonify(recipes[index]), 200

    # If response was not JSON, return a JSON containing
    # error message, and status code
    return jsonify({"error": "Request must be JSON !!!"}), 415


# DELETE ENDPOINT for /users/:user_id/recipes/:recipe_id
@app.delete("/users/<int:user_id>/recipes/<int:recipe_id>")
def delete_recipe(user_id: int, recipe_id: int):
    # Check if recipe_id and user_id exists in the recipes list
    index = -1
    for i, recipe in enumerate(recipes):
        # If recipe found
        if recipe["id"] == recipe_id and recipe["user_id"] == user_id:
            index = i
            break
    # If recipe not found
    if index == -1:
        return jsonify({"error": f"No data found for Recipe ID {recipe_id} and User ID {user_id}"}), 400
    else:
        # Store the recipe data to send
        del_data = recipes[index]

        # Delete the recipe data
        del recipes[index]

        # Return the deleted recipe data as JSON with status code
        return jsonify(del_data), 200


if __name__ == '__main__':
    app.run(host=HOST, port=PORT)


# In[ ]:




