def alphabet_position(letter):
    letter = letter.lower()
    return (string.ascii_lowercase).index(letter)
#print(alphabet_position(letter))

def rotate_character(char, rot):
    if char.isalpha():
        shift = 97 if char.islower() else 65
        return chr((ord(char) + rot - shift) % 26 + shift)
    else:
        return char
def encrypt(text, rot):
	new=''
	for x in text:
		new= new + rotate_character(x, rot)
	return(new)
