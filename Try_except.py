
# user malumot kur  


#  agar key aniqlanmasa, key qush, va value ni sora

# user = {
#     "name": "Jhon",
#     "age": "21",
#     "phone_number": +998778759898
# }

# def user_info(key):
#     try:
#         return user[key]
#     except KeyError:
#         n = input('Please enter value: ')

#         # add key and n as value
#         user[key] = n

#         # check the user dict
#         print(user)

# print(user_info('hello'))


# def user_info(key, **kwargs):
#     try:
#         return user[key]
#     except KeyError:
#         if key == 'create' or key == 'update':
#             user
#             return user
#         elif key == 'read':
#             return user
#         elif key == 'delete':
#             user.pop(kwargs)

# print(user_info('create', last_name = "Lirov"))

            
def calculator(a,b,amal):
    try:

        if not isinstance(a, (int, tuple)) or not isinstance(b, (int, tuple)) :
            raise TypeError('Enter only number')
        if amal == 'divide':
            if a == 0 or b == 0:
                raise ZeroDivisionError('0 ga bolina olmaydi')
            return f"{a} / {b} = {a / b}" 

        elif amal == 'plus':
            return f"{a} + {b} = {a + b}"

        elif amal == 'minus':
            return f"{a} - {b} = {a - b}"

        elif amal == 'power':
            if b == 0:
                return 1
            else:
                return f"{a} ning {b}-darajasi  = {a ** b}"

        elif amal == 'root':
            return a ** (1/b)

    except ZeroDivisionError as err:
        print(err)
    except TypeError as ty:
        print(ty)

print(calculator(4,2,'root'))


