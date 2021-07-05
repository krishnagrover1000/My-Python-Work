# A Dict Can Be Used for Multiple Resaons 
# They Are Super Fast
# Variable_Name = {Key:Value}

# Creating A Dict For My Grocieries {"Fruit_Name:Dollars"}
Grocieries_Fruits = {"Bannans":3.00, "Orange":1.50, "Berrys":4.00}
# The Get Function Sees If .get("Str") is in There or Not
print(Grocieries_Fruits.get("Hello"))

# Example Of Contacts in Dict

Contacts = {
    "Aryan": "+1(905)-497-4474",
    "Ajay": "+1 (647) - 927 - 2529"
}
print(Contacts["Aryan"])
print(Contacts["Ajay"])

# This Function Prints Out The Keys And Values Of DICT
print(Grocieries_Fruits.items())

# This Function Prints Out The Keys (Key:Value)
print(Grocieries_Fruits.keys())

# This Function Prints Out The Values ("Str":"Value")
print(Grocieries_Fruits.values())

# This Function Removes A Key and Value Given To It
Grocieries_Fruits.pop("Berrys")
print(Grocieries_Fruits)

# This Function Clears The Dictionary
Grocieries_Fruits.clear()
print(Grocieries_Fruits)

