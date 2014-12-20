__author__ = 'Stephanie'

locationOpen = open(r'C:\Users\Stephanie\locationid.txt', 'r')
locationText = locationOpen.readlines()
locationOpen.close()
locationInput = []
i = 0
for line in locationText:
    myLine = line.strip()
    locationInput.append(myLine)
    i += 1

productOpen = open(r'C:\Users\Stephanie\productid.txt', 'r')
productText = productOpen.readlines()
productOpen.close()
productInput = []
i = 0
for line in productText:
    myLine = line.strip()
    productInput.append(myLine)
    i += 1

queryString = []

for location in locationInput:
    for product in productInput:
        import random
        mystring = "INSERT INTO inventory_listing (productID,locationID,invQOH) VALUES ('" + product + "', '" + location + "', " + str(random.randrange(0, 100)) + ");"
        queryString.append(mystring)

for quString in queryString:
    print quString
