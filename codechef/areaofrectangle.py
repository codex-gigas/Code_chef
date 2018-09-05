L = int(raw_input())
B = int(raw_input())
area = L * B
peri = 2*(L + B)
if area > peri:
    print("Area")
    print(area)
else:
    print("Peri")
    print(peri)
