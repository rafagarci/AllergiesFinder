# DO NOT INPUT MULTIPLE LINES, PUT EVERYTHING IN A SINGLE LINE. OTHERWISE MULTIPLE OUTPUTS ARE PRODUCED.
import re

# "DO NOT USE" CATEGORY
categories_Do_Not_Use = [

    #########################################################
    # you can add a new category for the Do not Use list here
    #########################################################
    ["Nickel", "Cobalt", "Neomycin", "Polymyxin-B-sulphate", "Balsam of Peru", "Cinnamic Aldehyde", "Benzoic acid"],

        # Nickel
        ["Nickel"],
        # Cobalt
        ["Cobalt", "Cobalt dichloride", "Cobalt chloride", "Cobaltous chloride",
         "Cobaltous chloride hexahydrate", "Cobalt dichloride hexahydrate", "Cobalt sulfate",
         "Cobalt sulfamate"],
        # Neomycin
        ["Neomycin", "Tobramycin", "Gentamicin", "Butirosin", "Paromomycin", "Framycetin ", "Kanamycin",
         "Amikacin", "Spectinomycin", "Streptomycin", "Dihydrostreptomycin", "Netilmicin", "Sisomicin ",
         "Ribostamycin "],
        # Polymyxin-B-sulphate
        ["Polymyxin-B-sulphate ", "Aerosporin", "EINECS 215-774-7", "Poly-RX",
         "Polymixin B sulfate", "Polymxin B Sulfate ", "Polymyxin B Sulfate"],
        # Balsam of Peru
        ["Balsam of peru", "Myroxylon pereirae", "Black balsam", "Toluifera pereira balsam ",
         "Honduras balsam ", "China oil ", "Benzoic acid ", "Benzyl acetate ", "Benzyl benzoate ",
         "Benzyl cinnamate ", "Cinnamic acid ", "Cinnamic alcohol ", "Cinnamic aldehyde",
         "Cinnamyl cinnamate ", "Benzyl alcohol"],
        # Cinnamic Aldehyde
        ["Cinnamic Aldehyde ", "Cinnamal ", "Cinnamyl aldehyde ", "3-phenyl-2-propenal ",
         "3-phenylacetaldehyde ", "Cassia aldehyde ", "Cinnamon"],
        # Benzoic Acid
        ["Benzoic acid ", "Benzenecarboxylic acid ", "Phenylformic acid ", "Benzene formic acid ",
         "Retarded ba ", "Benzenemethonic acid ", "Retardex ", "Carboxybenzene ", "Salvo",
         "Discyclic acid ", "Tennplas ", "Phenyl carboxylic acid ", "Oracylic acid "]


        ###############################################################
        # ADD A CORRESPONDING LIST OF INGREDIENTS TO THE NEW ADDED LIST
        # Don't forget to add a , after the previous array
        ###############################################################

]

# "AVOID" CATEGORY
categories_Avoid = [

    ##########################################################
    # you can add a new category for the "avoid" category here
    ##########################################################
    ["Nickel", "Cobalt", "Balsam of Peru", "Cinnamic aldehyde"],

        # Nickel
        ["Nickel sulfate", "White gold ", "Nickel silver", "Nickel bronze ", "Chrome", "Plated ", "German silver ",
         "Alpaca", "Sea water bronze ", "High-strength yellow brass ", "Palladium ", "Titanium alloy"],
        # Cobalt
        ["Apricot", "Bean", "Beer", "Beet", "Cabbage", "Chocolate ", "Cloves", "Cocoa ", "Coffee", "Liver", "B12",
         "Nut", "Scallop", "Tea", "Whole-grain flour "],
        # Balsam of Peru
        ["Eugenol ", "Farnesol ", "Isoeugenol ", "Nerolidol ", "Vanillin ", "Fragrance ", "Flavor", "Parfum ",
         "Perfume", "Scent", "Scented", "Citrus ", "Citric acid ", "Ascorbic acid ", "Vitamin C", "Zest", "Orange ",
         "Lemon", "Lime", "Grapefruit ", "Bitter orange ", "Tangerine ", "Mandarin orange ", "Marmalade ", "Juice ",
         "Tomato ", "Ketchup", "Tomato sauce ", "Red sauce ", "Pizza", "Chili", "Chili sauce ", "Barbeque sauce ",
         "Cinnamon ", "Cloves", "Vanilla", "Curry", "Nutmeg", "Allspice ", "Anise", "Ginger", "Chutney", "Pimento",
         "Pickled", "Pickle", "Wine", "Beer", "Gin", "Vermouth", "Benzaldehyde", "Benzoin", "Benzyl salicylate ",
         "Colophony ", "Coniferyl alcohol ", "Coniferyl benzoate ", "Coumarin ", "Diethylstilbestrol ",
         "Resorcin monobenzoate ", "Pesorcinol ", "Propolis ", "Storax", "Tolu balsam ", "Wood tar"],
        # Cinnamic aldehyde
        ["Cinamol ", "Cinnamol ", "Cola", "Vermouth ", "Bitters", "Chocolate ", "Ice cream", "Gum (chewing)", "Candy",
         "Spice"]

        ###############################################################
        # ADD A CORRESPONDING LIST OF INGREDIENTS TO THE NEW ADDED LIST
        # Don't forget to add a , after the previous array
        ###############################################################

]


def to_lower(arr):
    # Takes a string array and converts its elements to lower case. Also removes leading and trailing empty spaces.
    for i in range(0, len(arr)):
        arr[i] = arr[i].lower().strip()
    return


for i in range(0, len(categories_Do_Not_Use)):
    # Changes all values in the "Do Not Use" list to lower case
    to_lower(categories_Do_Not_Use[i])

for i in range(0, len(categories_Avoid)):
    # Changes all values in the "Do Not Use" list to lower case
    to_lower(categories_Avoid[i])


# Initial hello message
print("Welcome to the food checker. Type or paste a list of ingredients you would like to check.\nType \"quit\" at "
      "any time to exit")

# Regex side values. This is important it will only match the words found that are surrounded by the below
# specified characters. No other character is allowed, for example bean is in the list by soyBean is not matched.
side = "([ ,.:-]|^|$|\n)"

# Main loop of execution
while True:
    # Changes current input to lower case
    curr = input()
    curr = curr.lower()

    # Checks quit condition
    if curr == "quit":
        print("Exiting now")
        exit(0)

    # First checks the values of the "DO NOT USE" list

    # This array contains one array for each subcategory in the DO NOT USE list
    # all the matches will be stored there for each subcategory respectively
    found_DONOTUSE = []
    for i in range(0, len(categories_Do_Not_Use[0])):
        # Appends new array to found_DONOTUSE
        found_DONOTUSE.append([])

        # Traverses through the list of the current subcategory
        for j in categories_Do_Not_Use[i + 1]:
            if bool(re.search(side + j + side, curr)):
                found_DONOTUSE[i].append(j)

    # Second loop checks the values of the "AVOID" list

    # This array contains one array for each subcategory in the AVOID list
    # all the matches will be stored there for each subcategory respectively
    found_AVOID = []
    for i in range(0, len(categories_Avoid[0])):
        # Appends new array to found_DONOTUSE
        found_AVOID.append([])

        # Traverses through the list of the current subcategory
        for j in categories_Avoid[i + 1]:
            if bool(re.search(side + j + side, curr)):
                found_AVOID[i].append(j)

    # Prints found results in DO NOT USE
    print("\nFound ingredients in the DO NOT USE list:")
    for i in range(0, len(found_DONOTUSE)):
        # Condition to avoid subcategories that are empty
        if len(found_DONOTUSE[i]) == 0:
            continue
        print(" " + categories_Do_Not_Use[0][i].upper())
        for j in found_DONOTUSE[i]:
            print("  " + j)

    # Prints found results in AVOID list
    print("Found ingredients in the AVOID list:")
    for i in range(0, len(found_AVOID)):
        # Condition to avoid subcategories that are empty
        if len(found_AVOID[i]) == 0:
            continue
        print(" " + categories_Avoid[0][i].upper())
        for j in found_AVOID[i]:
            print("  " + j)

    # Prints empty line
    print("\nType quit to exit\n")




