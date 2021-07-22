# get data from user and store it in a list, then
# display the most recent three entries nicely
# Final version based on trial #3
# Adds break loop and checks for empty list

# Set up empty list
all_calcualtions = []

# Get items of data and add to list
get_item = ""
while get_item != "zz":
    get_item = input("Enter an item: ")

    if get_item == "zz":
        break

    all_calcualtions.append(get_item)

print()

if len(all_calcualtions) == 0:
    print("Oops - the list is empty")

else:

    # Show that everything made it to the list...
    print()
    print("*** The Full List ***")
    print(all_calcualtions)

    # print items starting at the END of the list
    if len(all_calcualtions) >= 3:
        print("*** Most Recent 3 ***")
        for item in range(0, 3):
            print(all_calcualtions[len(all_calcualtions) - item - 1])

    else:
        print("*** Items from Newest to Oldest ****")
        for item in all_calcualtions:
            print(all_calcualtions[len(all_calcualtions) - all_calcualtions.index(item) - 1])
