import os
print("""
[1] Programmer
[2] Artist
[3] Engineer
""")
choice = input("Choice one : ")
if choice == "1":
    os.system("python programmer/programmer.py")
elif choice== "2":
    os.system("python artist/artist.py")
elif choice == "3":
    os.system("python engineer/engineer.py")
else:
    print("What are you doing step user")
