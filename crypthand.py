import io

class Crypthand:
    """ takes an input .txt file and encrypts/decrypts
        text using anne lister's crypthand. """

    def __init__(self, input_file):
        with io.open(input_file, 'r', encoding = 'utf8') as f:
            self.lines = f.readlines()

        self.encrypt_cipher = {
            'a': '2',
            'b': '(',
            'c': ')',
            'd': 'o',
            'e': '3',
            'f': 'v',
            'g': 'n',
            'h': 'Q',
            'i': '4',
            'j': '4',
            'k': '|',
            'l': 'd',
            'm': '-',
            'n': '\\',
            'o': '5',
            'p': '+',
            'q': '‖',
            'r': 'p',        
            's': '=',
            't': '~',
            'u': '6',
            'v': 'g',
            'w': '8',
            'x': 'w',  
            'y': '7',
            'z': '9',  

            # common combo characters
            'th': '√',
            'sh': 'Λ',
            'ch': '∇',
            'bb': '∈',
            'cc': '∋',
            'ee': ';',
            'ff': 'φ',
            'll': ':',
            'nn': '⊥',
            'oo': '!',
            'pp': '≠',
            'rr': '⳨',
            'ss': '?',
            'tt': '⍭',
            
            # words
            'and': '\u00D7',  # '×'
            'mr': 'χ',
            'mrs': 'Ӿ',
        }  

    def encrypt(self, a_to_z_only, mode='e'):
        """ encrypts the contents of the input file. """
        result = ""

        if mode == 'e':
            cipher = self.encrypt_cipher
        else:
            # decrypt cipher
            cipher = {value: key for key, value  in self.encrypt_cipher.items()}

            # special case due to 'i' and 'j' both being mapped to '4'
            cipher['4'] = '[i/j]'

        for word in self.lines:
            if a_to_z_only is False:
                for key in cipher.keys():
                    if len(key) == 2 and key != 'mr':
                        word = word.replace(key, cipher[key])

                for w in word.split():
                    if w in cipher:
                        result += cipher.get(w) + " " 
                    else:
                        result += self.encrypt_string(w, cipher) + " " 
                result += "\n"
            else:
                result += self.encrypt_string(word, cipher)
        return result
    
    def encrypt_string(self, word, cipher):
        """ encrypts a string from the input file. """
        encrypted_string = ""
        
        for char in word:
            if char not in cipher:
                encrypted_string += char
            else:
                encrypted_string += cipher.get(char)
        return encrypted_string

    def decrypt(self, a_to_z_only):
        """ decrypts the contents of the input file by using self.encrypt()
            with the decrypt_cipher. """
        return self.encrypt(a_to_z_only, 'd')


def write_to_file(output_file, crypt, a_to_z_only):
    """ writes encrypted/decrypted output to a text file. """
    with open(output_file, 'w') as f:
        f.write(crypt.decrypt(a_to_z_only))


def main():
    input_file = "test.txt"

    # use only [a-z] cipher (True)
    # or include replacements for words or combo chars ['th', 'll', ...] (False)
    a_to_z_only = False

    result = Crypthand(input_file)
    
    print(result.encrypt(a_to_z_only))
    # print(result.decrypt(a_to_z_only))

    # output = "output.txt"
    # write_to_file(output, result, a_to_z_only)

if __name__ == '__main__':
    main()