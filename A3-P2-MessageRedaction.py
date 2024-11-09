#Program 2 – Message Redaction
#Description:   Design and write a program that counts and removes all desired letters from 
#               any user-entered sentence or phrase.

#Student #:     W0461513
#Student Name:  Mathew Akunyili

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    sentencePhrase = ""
    phrase = []
    
    while (sentencePhrase != "quit"):
        sentencePhrase = input("Type a phrase (or quit to exit program): ").lower()
        if sentencePhrase == "quit":
            break
        phrase.append(sentencePhrase)
        redact = input("Type a comma-seperated list of letters to redact: ").replace(" ", "").split(',')
        redactedPhrase = ['_' if char in redact else char for char in sentencePhrase]
        redactedCount = sum(sentencePhrase.count(letter) for letter in redact)
        print("Number of letters redacted: ",redactedCount)
        print("Redacted Phrase: ", ''.join(redactedPhrase))
    


    # YOUR CODE ENDS HERE

main()
