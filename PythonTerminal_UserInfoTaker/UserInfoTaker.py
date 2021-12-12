'''
Name: UserInfoDisplayer.py
Author: Karm Binning
Date Created: March 01, 2021

Description: 
An information program allowing a customer to fill out information then display it back in a nice format. It will take the all the customer's personal and order information.

Developer Information:
I started learning Python (Beginner's Level). Cleaned code a lot for better readability and understanding.
'''


#show welcome screen - functions

def showWelcomeScreen():
    welcomeScreen = initializeWelcomeScreen()
    show(welcomeScreen)

def initializeWelcomeScreen():
    welcomeScreen = addWelcomeScreen() + "\n\n"

    return welcomeScreen

def addWelcomeScreen():
    headerText = "   USER INPUT INFO DISPLAYER   "
    descriptionText = "   We just collect your personal data...   "
    descriptionCharacterLength = calculateCharacterLength(descriptionText)

    border = createWelcomeScreenBorder(borderLength=descriptionCharacterLength)
    text = createWelcomeScreenText(descriptionText, headerText)

    welcomeScreenDescription = border + text + border

    return welcomeScreenDescription

def createWelcomeScreenBorder(borderLength):
    return (newLine() + newLine()) + (borderLength * "*") + "\n\n"

def createWelcomeScreenText(descriptionText, headerText):
    return headerText + "\n\n\n\n" + descriptionText


#prompt and get user input - variables (static)
promptTitleFirstName = "CUSTOMER - FIRST NAME"
promptTitleLastName = "CUSTOMER - LAST NAME"
promptTitleFullName = "CUSTOMER - FULL NAME"
promptTitlePhoneNumber = "CUSTOMER - PHONE NUMBER"
promptTitleSpecialInstructions = "CUSTOMER - SPECIAL INSTRUCTIONS"

promptTitleAddressStreetNumber = "ADDRESS - STREET NUMBER"
promptTitleAddressStreetName = "ADDRESS - STREET NAME"
promptTitleAddressUnitNumber = "ADDRESS - UNIT NUMBER"
promptTitleAddressCity = "ADDRESS - CITY"
promptTitleAddressProvince = "ADDRESS - PROVINCE"
promptTitleAddressPostalCode = "ADDRESS - POSTAL CODE"
promptTitleFullAddress = "ADDRESS"


#prompt and get user input - functions

def getCustomerInformationInput():
    personalInfoInstructions = "Please fill out the following personal information:\n"

    show(personalInfoInstructions)


def setCustomerPersonalInfo():
    getCustomerFullName()
    getCustomerFullAddress()
    getCustomerSpecialInstructions()
    getCustomerPhoneNumber()


def getCustomerFullName():
    customerFirstName = getFirstName()
    customerLastName = getLastName()

    return formatFullName(customerFirstName, customerLastName)

def formatFullName(firstName, lastName):
    return firstName + " " + lastName


def getCustomerFullAddress():
    customerAddressStreetNumber = getAddressStreetNumber()
    customerAddressStreetName = getAddressStreetName()
    customerAddressUnitNumber = getAddressUnitNumber()
    customerAddressCity = getAddressCity()
    customerAddressProvince = getAddressProvince()
    customerAddressPostalCode = getAddressPostalCode()

    customerFullAddress = formatFullAddress(customerAddressStreetNumber, customerAddressStreetName, customerAddressUnitNumber, customerAddressCity, customerAddressProvince, customerAddressPostalCode)

    return customerFullAddress

def formatFullAddress(streetNumber, streetName, unitNumber, city, province, postalcode):
    return streetNumber + " " + streetName + " Unit " + unitNumber + ", " + city + ", " + province + " " + postalcode


def getCustomerSpecialInstructions():
    specialInstructions= promptSpecificUserInput(promptTitleSpecialInstructions)

    return cleanSpecialInstructions(specialInstructions)

def cleanSpecialInstructions(specialInstructions):
    return cleanStringValue(specialInstructions)


def getCustomerPhoneNumber():
    phoneNumber = promptSpecificUserInput(promptTitlePhoneNumber)

    return cleanPhoneNumber(phoneNumber)

def cleanPhoneNumber(phoneNumber):
    return cleanStringValue(phoneNumber)


def getFirstName():
    firstName = promptSpecificUserInput(promptTitleFirstName)

    return cleanFirstName(firstName)

def cleanFirstName(firstName):
    return cleanStringValue(firstName)

def getLastName():
    lastName = promptSpecificUserInput(promptTitleLastName)

    return cleanLastName(lastName)

def cleanLastName(lastName):
    return cleanStringValue(lastName)

def getAddressStreetNumber():
    streetNumber = promptSpecificUserInput(promptTitleAddressStreetNumber)

    return cleanStreetNumber(streetNumber)

def cleanStreetNumber(streetNumber):
    return cleanStringValue(value=streetNumber)

def getAddressStreetName():
    streetName = promptSpecificUserInput(promptTitleAddressStreetName)

    return cleanStreetName(streetName)

def cleanStreetName(streetName):
    return cleanStringValue(value=streetName)

def getAddressUnitNumber():
    unitNumber = promptSpecificUserInput(promptTitleAddressUnitNumber)

    return cleanUnitNumber(unitNumber)

def cleanUnitNumber(unitNumber):
    return cleanStringValue(value=unitNumber)

def getAddressCity():
    city = promptSpecificUserInput(promptTitleAddressCity)

    return cleanCity(city)

def cleanCity(city):
    return cleanStringValue(value=city)

def getAddressProvince():
    province = promptSpecificUserInput(promptTitleAddressProvince)

    return cleanProvince(province)

def cleanProvince(province):
    return cleanStringValue(value=province)

def getAddressPostalCode():
    postalCode = promptSpecificUserInput(promptTitleAddressPostalCode)

    return cleanPostalCode(postalCode)

def cleanPostalCode(postalCode):
    return cleanStringValue(value=postalCode)


#general helper functions - functions

def calculateCharacterLength(text):
    return int(len(text))

def promptSpecificUserInput(promptTitle):
    return input(formatPromptTitle(promptTitle))

def formatPromptTitle(promptTitle):
    return "   " + promptTitle + ": "

def cleanStringValue(value):
    return removeWhitespaces(value)

def removeWhitespaces(value):
    return value.strip()


def newLine():
    return "\n"
def newLine2():
    return "\n" + "\n"


# output


def end():
    border = "\n\n************************\n\n"
    goodbyeMessage = border + "THANK YOU! HAVE A NICE DAY!" + border

    show(goodbyeMessage)


def show(text):
    print(text)


#start main application using the written above variables and functions

showWelcomeScreen()

getCustomerInformationInput()
setCustomerPersonalInfo()

end()


#END APPLICATION