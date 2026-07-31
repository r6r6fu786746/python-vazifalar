# orders = [
#     {
#         "id": 1,
#         "meal": "Plov",
#         "price": 10000
#     },
#     {
#         "id": 2,
#         "meal": "Mastava",
#         "price": 8000
#     },
#     {
#         "id": 3,
#         "meal": "Shashlik",
#         "price": 12000
#     },
#     {
#         "id": 4,
#         "meal": "Choy",
#         "price": 2000
#     },
#     {
#         "id": 5,
#         "meal": "Bread",
#         "price": 1000
#     }
# ]

# def monitort(name, *args, **kwargs):

#     print("Welcome!", name.upper())

#     for i in args:
#         for ii in orders:
#             if i == ii["meal"]:
#                 print(i)

# def check(name, *args, **kwargs):
#     print("*"*20)
#     print("Chek".center(20))
#     print("*"*20)
#     # print("Taomlar: ")

#     for i in args:
#         for ii in orders:
#             if i == ii["meal"]:
#                 print(i.center(20), ii["price"], "som")
#     print("\nJami narx:", sum(ii["price"] for i in args for ii in orders if i == ii["meal"]), "som")


# monitort("John", "Plov", "Mastava", service = True)
# check("John", "Plov", "Mastava", service = True)

# # if __name__ == "__main__":








# def user_valid(username, password, confirm_password):

#     def username_valid():
#         return username.strip()

#     def password_valid():
#         return len(password) > 8

#     def is_equal():
#         return password == confirm_password


#     print(username_valid())
#     print(password_valid())
#     print(is_equal())

#     return "So'rovingiz muvaffaqiyatli amalga oshirildi!"


# print(user_valid("     Hello   ", "fg63431", "fg63431"))








# def bank(kurs, valyuta):

#     def converter(som):
#         value = som / kurs
#         return f"{value}. {valyuta} {som}"

#     return converter()

# bt = bank(12000, "USD")
# print(bt, 30000)


"----------------------------------------------------------"
"----------------------------------------------------------"



