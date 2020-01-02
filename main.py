#validday = True
#while validday:
#    dayarrive = str(input("What day did you arrive"))
#    if dayarrive == 'Sunday' or dayarrive == 'Monday' or dayarrive =='Tuesday' or dayarrive =='Wednesday' or dayarrive =='Thursday' or dayarrive =='Friday' or dayarrive =='Saturday':
#        validday = False
#    else:
#        validday = True



def pricemachine(dayarrive):
    print('Today is day: ' + str(dayarrive))
    validhour = True        
    while validhour:
        hourarrive = int(input("What time did you arrive? "))

        if hourarrive <= 24 and hourarrive >= 8:
         validhour = False


    validpark = True
    while validpark:
        parkHour = int(input("How long will you be leaving your car? "))
        if hourarrive <= 15:
            valid1 = '0'
            if dayarrive == 'Sunday':
                if parkHour <= 8:
                    valid1 = '22'
            if dayarrive == 'Monday' or dayarrive =='Tuesday' or dayarrive =='Wednesday' or dayarrive =='Thursday' or dayarrive =='Friday':
                if parkHour <= 2:
                    valid1 = '22'
            if dayarrive == 'Saturday':
                if parkHour <= 4:
                    valid1 = '22'
        else:
            valid1 = '22'
        if valid1 == '22':
                if parkHour + hourarrive <= 24:
                    validpark = False

    validparknum = True
    while validparknum:
        parknumyeno = str(input('do you have a parking number? '))
        if parknumyeno == 'yes':
            parkNum = int(input("What is your frequent parking number? "))
            parkNum = str(parkNum)
            if len(parkNum) == 5:
                validparknum = False
        else:
            validparknum = False



    discount = False

    if parknumyeno == 'yes':
        sum = (int(parkNum[0])*5) + (int(parkNum[1])*4) + (int(parkNum[2])*3) + (int(parkNum[3])*2) + int(parkNum[4])
        if sum%11 == 0:
            print("Discount applied")
            discount = True
        else:
            print("Discount not applied")

    if dayarrive == 'Sunday':
        price = parkHour * 2
        if discount:
            if hourarrive < 16:
                price = float(price * 0.9)
            else:
                price = float(price * 0.5)

    if dayarrive == 'Monday' or dayarrive =='Tuesday' or dayarrive =='Wednesday' or dayarrive =='Thursday' or dayarrive =='Friday':
        if hourarrive >= 16:
            price = parkHour * 2
        elif hourarrive <= 16:
            if hourarrive + parkHour > 16:
                hoursafter = (16 - (hourarrive + parkHour)) * -1
                price = (hoursafter * 2) + ((parkHour - hoursafter) * 10)
            else:
                price = parkHour * 10
        if discount:
            if hourarrive < 16:
                price = float(price * 0.9)
            else:
                price = float(price * 0.5)

   
    if dayarrive == 'Saturday':
        if hourarrive >= 16:
            price = parkHour * 2
        elif hourarrive <= 16:
            if hourarrive + parkHour > 16:
                hoursafter = (16 - (hourarrive + parkHour)) * -1
                price = (hoursafter * 2) + ((parkHour - hoursafter) * 3)
            else:
                price = parkHour * 3
        if discount:
            if hourarrive < 16:
                price = float(price * 0.9)
            else:
                price = float(price * 0.5)

    return price


dopp = True
while dopp:
    enterff = True
    ffdd = str(input("What is the day today? "))
    totalChange = 0.0
    while enterff:
        pricec = pricemachine(ffdd)
        print("This is your price: " + str(pricec))
        validpayment = True
        while validpayment:
            print("You have this much change: " + str(totalChange))
            payment = float(input("How much would you pay?"))
            if payment + totalChange >= pricec:
                validpayment = False
        totalChange = (totalChange + payment) - pricec
        isit = str(input("Is this today's final payment? "))
        if isit == 'yes':
            enterff = False
        else:
            print("enter more pls. ")
    isit2 = str(input("Is there anyother day you wanna pay? "))
    if isit2 == 'no':
            dopp = False
