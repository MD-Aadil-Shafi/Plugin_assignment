input_list = [1,0,'1wd',0,3,2,0,0,'2nb','0wkt',6,1,0,4]

p1,p2,p3 = 0,0,0
out = False
total,wicket,extra = 0,0,0
active = p1

for i in input_list:
    if type(i) == int:
        total += i
        if i == 0:
            continue
        elif i%2 != 0:
            if active == p1 and out == False:
                p1 += i
                active = p2
            elif active == p2 and out == False:
                p2 += i
                active = p1
            elif active == p3 and out == True:
                p3 += i
                active = p2
            elif active == p2 and out == True:
                p2 += i
                active = p3
            
        else:
            if active == p1:
                p1 += i
            elif active == p2:
                p2 += i
            elif active == p3:
                p3 += i

    elif type(i) == str:
        if i == "1wd":
            total += 1
            extra += 1
        elif i == "2nb":
            total += 2
            extra += 2
        elif i == "0wkt":
            active = p3
            out = True
            wicket += 1

        


     


print("Player 1 Score : ", str(p1))
print("Player 2 Score : ", str(p2))
print("Player 3 Score : ", str(p3))

print('extra : ', str(extra))
print('total : ',str(total))
print('wicket fall : ', str(wicket))