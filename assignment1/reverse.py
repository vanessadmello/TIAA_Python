string = input("Enter String: ")
reverse = list(string)
for i in range(0, int(len(reverse) / 2)):
    temp = reverse[i]
    reverse[i] = reverse[len(reverse) - 1 - i]
    reverse[len(reverse) - 1 - i] = temp
print("Reversed String = ", "".join(reverse))