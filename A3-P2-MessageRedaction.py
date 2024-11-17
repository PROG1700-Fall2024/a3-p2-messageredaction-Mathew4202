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
            break #if user types quit it ends the loop
        phrase.append(sentencePhrase) #This appends what the user inputs into a list
        redact = input("Type a comma-seperated list of letters to redact: ").replace(" ", "").split(',') # whatever the user inputs it replaces it and splits it equally
        redactedPhrase = ['_' if char in redact else char for char in sentencePhrase] # this just means that replace the charcters the user enters in redact with _ else leave the other characters as it is in the input sentencePhrace
        redactedCount = sum(sentencePhrase.count(letter) for letter in redact)
        print("Number of letters redacted: ",redactedCount)
        print("Redacted Phrase: ", ''.join(redactedPhrase))
    


    # YOUR CODE ENDS HERE

main()
