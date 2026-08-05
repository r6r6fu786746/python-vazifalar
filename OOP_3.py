# Final
import time



users = [
    {"name": "Ali"},
    {"name": "Bobur"},
    {"name": "Diyora"},
    {"name": "Malika"},
    {"name": "Nodir"},
]

davomat = [
    {"status":"keldi",
     "Ism": "Ali"
    },
]
def data_test(func):

    def wrapper(*args, **kwargs):
        counter = 1

        start = time.time()

        print("Started...")
        views = func(*args, **kwargs)
        counter += 1
        print("Ended")

        end = time.time()
        print(f"Code estimated in {round((end-start), 8)} seconds")

        if counter == 2:
            return "Sorov iktadan oshdi"
        else:
            return f"{views}"

        

    return wrapper

@data_test
def school_valid(valid_name):
    for user in users:
        print(user)
        if valid_name == user['name']:
            print("Buday student bor")
        else:
            print("Bunday student yoq")

    return f"Success!🎉"


school_valid("Ali")


# vazifa funksiya vaqitini qaniqlash
# Users listini toldirish
# Agar student maktabga kemagan bumasa telefoniga sms yuborsin
# 