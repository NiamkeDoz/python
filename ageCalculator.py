import datetime

print('What is your name?')
myName = input()
print('Nice to meet you ' + myName + '!')
print('What year were you born?')
birthYear = input()
# print('What Month were you born?')
# birthMonth = input()
# print('What day of the Month were you born?')
# birthDay = input()
current = datetime.datetime.now()
currentAge = current.year - int(birthYear)
print()
print(myName + ', you are ' + str(currentAge) + ' years old!')

