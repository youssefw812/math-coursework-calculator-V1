print("================================\n")
print("© 2026 Youssef Wael- 202500929 - All Rights Reserved❤️\n")
print ("Welcome to the Math Course Work")
print ("================================\n")
print ("Hello, Please enter Your First midterm mark\n")
x = float(input ("Your First midterm mark is: "))
print ("Please enter Your Second midterm mark")
y = float(input ("Your Second midterm mark is: "))
mid = 0
while x < 0 or x > 20 or y < 0 or y > 20:
    print ("❌Please enter a valid mark")
    x = float(input ("Your First midterm mark is: "))
    y = float(input ("Your Second midterm mark is: "))
else:
    if x > y :
        mid = ((y*0.3) + (x*0.7)) * 35/20
        print (f"\nYour midterm mark is: {mid} out of 35✅\n")
    elif x < y :
        mid = ((x*0.3) + (y*0.7)) * 35/20
        print (f"\nYour midterm mark is: {mid} out of 35✅\n")
    elif x == y :
        mid = x * 35/20
        print (f"\nYour midterm mark is: {mid} out of 35✅\n")

print("================================\n")

print ("Enter the best three assignment marks")
a = float(input ("Your First assignment mark is: "))
b = float(input ("Your Second assignment mark is: "))
c = float(input ("Your Third assignment mark is: "))
assignment = 0
while a < 0 or a > 10 or b < 0 or b > 10 or c < 0 or c > 10:
    print ("❌Please enter a valid mark")
    a = float(input ("Your First assignment mark is: "))
    b = float(input ("Your Second assignment mark is: "))
    c = float(input ("Your Third assignment mark is: "))
else:
    assignment = ((a+b+c) / 3)
    print (f"\nYour assignment mark is: {assignment} out of 10✅\n")
print("================================\n")

print ("Enter The best three quiz marks out of 15")
q1 = float(input ("Your First quiz mark is: "))
q2 = float(input ("Your Second quiz mark is: "))
q3 = float(input ("Your Third quiz mark is: "))
quiz = 0
while q1 < 0 or q1 > 15 or q2 < 0 or q2 > 15 or q3 < 0 or q3 > 15:
    print ("❌Please enter a valid mark")
    q1 = float(input ("Your First quiz mark is: "))
    q2 = float(input ("Your Second quiz mark is: "))
    q3 = float(input ("Your Third quiz mark is: "))
else : 
    quiz = (q1+q2+q3) / 3
    print (f"\nYour quiz mark is: {quiz} out of 15✅\n")
print("================================\n")
overall = mid + assignment + quiz
print (f"\nYour overall coursework is: {overall} out of 60✅\n")
print("Congratulations on completing the Math Course Work! 🎉\n")
print("================================")
print("   Coursework Calculator v1.0")
print("   © 2026 Youssef Wael")
print("================================\n")
input("Press Enter to exit...")