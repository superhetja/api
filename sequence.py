#3+((1–0)+(2–1)+(3–2)) = 6      
# 6 +((2–1)+(3–2)+(6–3)) = 11   
#11 + ((3–2)+(6–3)+(11–6)) = 20
# 20 + ((6–3)+(11–6)+(20–11)) = 37
#37 + ((11–6)+(20–11)+(37–20) = 68
#68 + ((20–11)+(37–20)+(68–37)) = 125.
# 1,2,3,6,11,20,37
# 0 + 0 + 1 = 1
# 0 + 1 + 1 = 2
# 0 + 1 + 2 = 3
# 1 + 2 + 3 = 6
# 2 + 3 + 6 = 11



n = int(input("Enter the length of the sequence: ")) # Do not change this line

x = 0
y = 1
z = 0
number = 0
for a in range (0 , n):
    number = x + y + z
    x = y
    y = z
    z = number



print (number)

