# pip install spoonacular
import spoonacular as sp

api = sp.API("668584543a0f48948d42408f93c840d7")
# Parse an ingredient

response = api.search_recipes_by_ingredients("apple")
data = response.json()
# print(len(data))
# print(data["title"])
# print(data["image"])

for recipe in data:
    print(recipe["title"])
    print(recipe["image"])

# response = api.parse_ingredients("3.5 cups King Arthur flour", servings=1) # ingridientlar orqali retseplarni qidirish
# data = response.json()
# print(data[0]['name'])


# # Detect text for mentions of food
# response = api.detect_food_in_text("I really want a cheeseburger.") # matndagi ovqatni topish
# data = response.json()
# print(data['annotations'][0])


# # Get a random food joke
# response = api.get_a_random_food_joke() # tasodify ovqat haqida xazl
# data = response.json()
# print(data['text'])