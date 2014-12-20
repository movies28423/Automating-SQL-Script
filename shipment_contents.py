sidarray = ['DEC0814','OCT2714', 'DEC1514','SEP2914']
sdate = ['08-DEC-14', '27-OCT-14', '15-DEC-14', '29-SEP-14']
s_ship = ['01379','01379','01379','04589']
arrayOpen = open(r'/Users/stephanieleeb/Desktop/location.txt', 'r')
arrayText = arrayOpen.readlines()
arrayText = arrayText[0].strip().split()

itemOpen = open(r'/Users/stephanieleeb/Desktop/items.txt', 'r')
itemText = itemOpen.readlines()
ship_cont_lines = []
for item in itemText:
    ship_line = item.split()
    order_id = sidarray[int(ship_line[0])]
    prod_id = ship_line[1]
    ship_cont_lines.append([order_id, prod_id, ship_line[2:]])

sids = []
for sid in ship_cont_lines:
    j = 0
    for at in sid[2]:
        print "INSERT INTO SHIPMENT_CONTENTS (shipmentID, productID, shipmentQuantity) VALUES ('" + sid[0] + arrayText[j][2:] + "', '" + sid[1] + "', " + at + ");"
        j += 1
queryString = []
