taon = int(input("Enter year of service: "))
runtime = 1
if taon == 5:
    print("Bonus: 5%")
    runtime += 3

elif taon == 10:
    print("Bonus: 100%")
    runtime += 3

elif taon == 15:
    print("Bonus: 150%")
    runtime += 3
elif taon == 20:
    print("Bonus: 200%")
    runtime += 3

else:
    print("Ayos buhay nga")
runtime += 1

print(f"Running time:{runtime}(n)")

# Running time: 0(1)