# get data from user and store it in a list, then
# display the most recent three entries nicely
# Trial #3 - prints list in reverse order
# (no need for extra code or importing extra libraries)

# Set up empty list
all_calcualtions = []

# Get five items of Data
for item in range(0, 5):
    get_item = input("Enter an item: ")
    all_calcualtions.append(get_item)

# Show that everything made it to the list...
print()
print("*** The Full List ***")
print(all_calcualtions)

print()

print("*** Most Recent 3 ***")
# print items starting at the END of the list
for item in range(0, 3):
    print(all_calcualtions[len(all_calcualtions) - item - 1])
