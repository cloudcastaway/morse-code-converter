class Convert():
    def __init__(self):
        self.word = ""
        self.morse_code = ""

        # alpha-numeric symbols and some special chars - morse code chart
        chart = {'A':'.-', 'B':'-...',
                 'C':'-.-.', 'D':'-..', 'E':'.',
                 'F':'..-.', 'G':'--.', 'H':'....',
                 'I':'..', 'J':'.---', 'K':'-.-',
                 'L':'.-..', 'M':'--', 'N':'-.',
                 'O':'---', 'P':'.--.', 'Q':'--.-',
                 'R':'.-.', 'S':'...', 'T':'-',
                 'U':'..-', 'V':'...-', 'W':'.--',
                 'X':'-..-', 'Y':'-.--', 'Z':'--..',
                 '1':'.----', '2':'..---', '3':'...--',
                 '4':'....-', '5':'.....', '6':'-....',
                 '7':'--...', '8':'---..', '9':'----.',
                 '0':'-----', ', ':'--..--', '.':'.-.-.-',
                 '?':'..--..', '/':'-..-.', '-':'-....-',
                 '(':'-.--.', ')':'-.--.-'}
    
    def encrypt(self, input_word):
        for char in input_word:
            self.morse_code += " "
            for key, value in self.chart.items():
                if char == key:
                    self.morse_code += value
                    break
        return self.morse_code
    
    def decrypt(self, input_morse_code):
        for char in input_morse_code:
            if char == " ":
                continue
            for key, value in self.char.items():
                if char == value:
                    self.word += key
                    break
        return self.word