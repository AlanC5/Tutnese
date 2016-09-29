import re

# Dictionaries to hold coding specifics
# Double vowels are left alone
# Throw an exception if input text contains a '|'


encodeInstruct = {
    'B' : 'bub',
    'C' : 'coch',
    'D' : 'dud',
    'F' : 'fuf',
    'G' : 'gug',
    'H' : 'hash',
    'J' : 'jug',
    'K' : 'kuck',
    'L' : 'lul',
    'M' : 'mum',
    'N' : 'nun',
    'P' : 'pup',
    'Q' : 'quack',
    'R' : 'rur',
    'S' : 'sus',
    'T' : 'tut',
    'V' : 'vuv',
    'W' : 'wack',
    'X' : 'xux',
    'Y' : 'yub',
    'Z' : 'zug'
}


# Before encoding upper case it and make sure its not a vowel (AIEOU)
def encode(text):
    try:
        # if | is found throw exception
        matchObj = re.search(re.escape("|"), text)

        if matchObj is not None and matchObj.group(0) == "|":
            raise Exception

        encodedString = text.upper();
        # Replaced all the constants in the text
        for code in encodeInstruct:
            encodedString = re.sub(code, encodeInstruct.get(code), encodedString);

        encodedString = encodedString.lower();

        # Detect all the repeated constants and replace with 'squa' + constant
        for code in encodeInstruct:
            repeat = encodeInstruct.get(code) + encodeInstruct.get(code);
            encodedString = re.sub(repeat, 'squa' + code.lower() ,encodedString)

        return encodedString;

    except Exception:
        print("| found in input")



# Before decoding lower case it and make sure its not a vowel
def decode(text):
    try:
        # if | is found throw exception
        matchObj = re.search(re.escape("|"), text)

        if matchObj is not None and matchObj.group(0) == "|":
            raise Exception

        # reverse encodeInstruct res = dict((v,k) for k,v in a.iteritems())
        decodedString = text.lower();

        # Detect 'squa' + constant and replace with constant
        for code in encodeInstruct:
            decodedString = re.sub('squa' + code.lower(), code.lower() + code.lower(), decodedString)

        # Detect values and replace with key
        for code in encodeInstruct:
            decodedString = re.sub(encodeInstruct.get(code), code.lower(), decodedString)

        decodedString = decodedString.lower();

        return decodedString;

    except Exception:
        print("| found in input")


# Testing for encoding for provided string
# print(encode("Over hill, over dale, Thorough bush, thorough brier, Over park, over pale, Thorough flood, thorough fire!") == "ovuverur hashisqual, ovuverur dudalule, tuthashorurougughash bubusushash, tuthashorurougughash bubrurierur, ovuverur puparurkuck, ovuverur pupalule, tuthashorurougughash fufluloodud, tuthashorurougughash fufirure!");

# Testing for decoding for provided string
# print(decode("ovuverur hashisqual, ovuverur dudalule, tuthashorurougughash bubusushash, tuthashorurougughash bubrurierur, ovuverur puparurkuck, ovuverur pupalule, tuthashorurougughash fufluloodud, tuthashorurougughash fufirure!") == "over hill, over dale, thorough bush, thorough brier, over park, over pale, thorough flood, thorough fire!")

# Testing for '|' for encoding
# print(encode("Over hill, over dale, Thorough bush, thorough brier, Over park, over pale, Thorough flo|od, thorough fire!"))

# Testing for '|' for decoding
# print(decode("ovuverur hash|isqual, ovuverur dudalule, tuthashorurougughash bubusushash, tuthashorurougughash bubrurierur, ovuverur puparurkuck, ovuverur pupalule, tuthashorurougughash fufluloodud, tuthashorurougughash fufirure!"))
