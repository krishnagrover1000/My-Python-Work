# Tuple - A Structured Data Type Which Can Not Be Changed Once Made

# Tuples Can Be Used For Multiple Things 
# Example:

Credit_Information = ("2467836574290478", "Jhon Doe", "09/20", "297")
Card_Number, Name, Expiry_Date, CVV = Credit_Information
print(Card_Number)
print(Name)
print(Expiry_Date)
print(CVV)

# Example Of Tuple Function

def Credit_Info ():
    Card_Number = int(input("Enter Card Number: "))
    Name = input("Enter Name On Card:").strip()
    Expiry_Date = input("Enter Expiry Date of Card MM/YY: ").strip()
    CVV = int(input("Enter Card CVV:"))

    Credit_Information = (Card_Number, Name, Expiry_Date, CVV)
    
    print(Card_Number)
    print(Name)
    print(Expiry_Date)
    print(CVV)

Credit_Info()

     