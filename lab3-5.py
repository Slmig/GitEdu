surname = input()
name = input()
group = input()
print("Привет, %s" % surname+" %s" % name+" из группы %s" % group)
mail = input("Введи свою электронную почту?")
print((surname[:5]+2*name[0:5]+3*mail[0:5]).lower())