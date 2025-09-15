def greet():
    message = "Hello, world!"  # τοπική μεταβλητή
    print(message)             # χρησιμοποιείται μέσα στη συνάρτηση

greet()           # ✅ 
print(message)    # ❌ Error: NameError: name 'message' is not defined
