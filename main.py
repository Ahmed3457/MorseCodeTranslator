raw_text = input("Input the text you want to translate to morse code: ")

output = []
for char in raw_text:
    if char.lower() == "a":
        output.append(".- / ")
    elif char.lower() == "b":
        output.append("-... / ")
    elif char.lower() == "c":
        output.append("-.-. / ")
    elif char.lower() == "d":
        output.append("-.. / ")
    elif char.lower() == "e":
        output.append(". / ")
    elif char.lower() == "f":
        output.append("..-. / ")
    elif char.lower() == "g":
        output.append("--. / ")
    elif char.lower() == "h":
        output.append(".... / ")
    elif char.lower() == "i":
        output.append(".. / ")
    elif char.lower() == "j":
        output.append(".--- / ")
    elif char.lower() == "k":
        output.append("-.- / ")
    elif char.lower() == "l":
        output.append(".-.. / ")
    elif char.lower() == "m":
        output.append("-- / ")
    elif char.lower() == "n":
        output.append("-. / ")
    elif char.lower() == "o":
        output.append("--- / ")
    elif char.lower() == "p":
        output.append(".--. / ")
    elif char.lower() == "q":
        output.append("--.- / ")
    elif char.lower() == "r":
        output.append(".-. / ")
    elif char.lower() == "s":
        output.append("... / ")
    elif char.lower() == "t":
        output.append("- / ")
    elif char.lower() == "u":
        output.append("..- / ")
    elif char.lower() == "v":
        output.append("...- / ")
    elif char.lower() == "w":
        output.append(".-- / ")
    elif char.lower() == "x":
        output.append("-..- / ")
    elif char.lower() == "y":
        output.append("-.-- / ")
    elif char.lower() == "z":
        output.append("--.. / ")
    elif char.lower() == "0":
        output.append("----- / ")
    elif char.lower() == "1":
        output.append(".---- / ")
    elif char.lower() == "2":
        output.append("..--- / ")
    elif char.lower() == "3":
        output.append("...-- / ")
    elif char.lower() == "4":
        output.append("....- / ")
    elif char.lower() == "5":
        output.append("..... / ")
    elif char.lower() == "6":
        output.append("-.... / ")
    elif char.lower() == "7":
        output.append("--... / ")
    elif char.lower() == "8":
        output.append("---.. / ")
    elif char.lower() == "9":
        output.append("----. / ")
    elif char.lower() == " ":
        output.append("  |  ")
    else:
        output.append(char)

final_output = " ".join(output)

print(f"Translated {raw_text} to morse code and the final result is\n {final_output}")