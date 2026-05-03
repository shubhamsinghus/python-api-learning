
    # from fastapi import FastAPI
    #
    # app = FastAPI()

#
# @app.get("/user/{user_id}")
# def get_user(user_id: int):
#     return {"user_id": user_id}
# @app.get("/")
# def home():
#     return {"message": "API is running"}

# from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# app = FastAPI()

# Fake database (in-memory)
users = {}

# Model
# class User(BaseModel):
#     name: str
#     age: int
#
# # Home
# @app.get("/")
# def home():
#     return {"message": "API is running"}
#
# # Create user
# @app.post("/users/{user_id}")
# def create_user(user_id: int, user: User):
#     if user_id in users:
#         raise HTTPException(status_code=400, detail="User already exists")
#     users[user_id] = user
#     return {"message": "User created", "data": user}
#
# # Get all users
# @app.get("/users")
# def get_users():
#     return users
#
# # Get single user
# @app.get("/users/{user_id}")
# def get_user(user_id: int):
#     if user_id not in users:
#         raise HTTPException(status_code=404, detail="User not found")
#     return users[user_id]
#
# # Update user
# @app.put("/users/{user_id}")
# def update_user(user_id: int, user: User):
#     if user_id not in users:
#         raise HTTPException(status_code=404, detail="User not found")
#     users[user_id] = user
#     return {"message": "User updated", "data": user}
#
# # Delete user
# @app.delete("/users/{user_id}")
# def delete_user(user_id: int):
#     if user_id not in users:
#         raise HTTPException(status_code=404, detail="User not found")
#     del users[user_id]
#     return {"message": "User deleted"}
import requests
# def get_random_users():
#     url="https://randomuser.me/api/"
#     response = requests.get(url)
#     data = response.json()
#     print(data)
#     if data ["success"] and "data" in data:
#         user_data= data["data"]
#         username=user_data["login"][1]["username"]
#         country=user_data["location"][1]["country"]
#         return username,country
#         print(response)
#     # print(data['results'][0]['name']['first'])
#     # print(data['results'][0]['location']['country'])
#     else:
#         raise HTTPException(status_code=404, detail="User not found")
#
# def main():
#     try:
#         username,country=get_random_users()
#         print(f"username:{username}\n country:{country}")
#     except Exception as e:
#         print(str(e))
# if __name__=="__main__" :
#     main()

# import requests
#     # The endpoint you want to call
# url = "https://randomuser.me/api/"
# response = requests.get(url)
#     # Check if the request was successful
# if response.status_code == 200:
#         data = response.json()  # Convert JSON response to a Python dictionary
#         print(data)
#         print(data['results'][0]['name']['first'])
#         print(data['results'][0]['location']['country'])
#
# else:
#         print(f"Error: {response.status_code}")
# import requests
# def get_random_users():
#     url = "https://randomuser.me/api/"
#     response = requests.get(url)
#     if response.status_code != 200:
#         raise Exception("Failed to fetch data")
#     data = response.json()
#
#     user_data = data["results"][0]
#     username = user_data["login"]["username"]
#     country = user_data["location"]["country"]
#
#     return username, country
#
#
# def main():
#         try:
#             username, country = get_random_users()
#             print(f"Username: {username}\nCountry: {country}")
#             # print(f"Country: {country}")
#         except Exception as e:
#             print("Error:", str(e))
#
#
# if __name__ == "__main__":
#         main()

# from quickapi import FastAPI
# from pydantic import BaseModel
#
# app = FastAPI()
#
# class Message(BaseModel):
#     message: str
#
# @app.get("/", response_model=Message)
# def root():
#     return {"Mantra": "Bum Bum Bhole"}



#joke api
import requests
import time

    # 1. The exact web address for the API endpoint
url = "https://official-joke-api.appspot.com/random_joke"

print("Contacting the Joke API...")

try:
    # 2. Send the GET request
    response = requests.get(url)

    # 3. Check for a 200 OK status
    response.raise_for_status()

    # 4. Convert the JSON text into a Python Dictionary
    joke_data = response.json()

    # 5. Extract our data using the dictionary keys
    setup = joke_data['setup']
    punchline = joke_data['punchline']

    # 6. Print the results to the screen!
    print("\nHere is your joke:")
    print("-" * 20)
    print(setup)

    # A fun 2-second dramatic pause before the punchline
    time.sleep(2)
    print(punchline)
    print("-" * 20)

except requests.exceptions.RequestException as e:
    print("\nOh no, we couldn't reach the API!")
    print("Error details:", e)