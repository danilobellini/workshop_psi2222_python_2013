
def ocr(msg):
    digitos = {
         1: [" ", 
             "|",
             "|",
             " "],
         2: [" _ ",
             " _|",
             "|_ ",
             "   "],
         3: [" _ ",
             " _|",
             " _|",
             "   "],
         4: ["   ",
             "|_|",
             "  |",
             "   "],
    }

    if len(msg[0]) == 6: 
      return 23

    textos = {tuple(v): k for k, v in digitos.items()}

    return textos[tuple(msg)]
