import re
class Evaluation:
    #decrypt the text (t) using key (k)
    def decrypt(k, t):
        #Sanitize the cipher and the key
        cipher = t.lower() #String
        cipher = re.sub("[^a-z]", "", cipher)
        cipher = re.sub("\\s", "", cipher)

        ke = k.lower() #String
        ke = re.sub("[^a-z]", "", ke)
        ke = re.sub("\\s", "", ke)

        key = list(ke) #Char[]
        for i in range(len(key)):
            key[i] = chr(ord(key[i])-97)
        
        #Run the decryption
        plain = "" #String
        keyPtr = 0 #int

        for i in range(len(cipher)):
            keyChar = chr(0)
            if(len(key) > 0):
                #Ignore any value not in the expected range
                while(ord(key[keyPtr]) >25 or ord(key[keyPtr]) < 0):
                    keyPtr = (keyPtr + 1)%(len(key))
                
                keyChar = key[keyPtr]
                keyPtr = (keyPtr + 1)%len(key)
            
            plain += (chr(((ord(cipher[i]) - 97 + 26 - ord(keyChar)) % 26) +97))
        
        return plain

    #Encrypt text (t) using the provided key (k) -- can use this for testing if needed
    def encrypt(k, t):
        #Sanitize the cipher and the key
        plain = t.lower() #String
        #plain = plain.replace("[^a-z]", "")
        plain = re.sub("[^a-z]", "", plain)
        #plain = plain.replace("\\s", "")
        plain = re.sub("\\s", "", plain)
        cipher = "" #String

        ke = k.lower() #String
        ke = ke.replace("[^a-z]", "")
        ke = ke.replace("\\s", "")

        key = list(ke) #Char[]
        for i in range(len(key)):
            key[i] = chr(ord(key[i])-97)

        #Encrypt the text
        keyPtr = 0 #Int
        for i in range(len(plain)):
            keyChar = chr(0)
            if(len(key) > 0):
                #Ignore any value not in the expected range
                while(ord(key[keyPtr]) >25 or ord(key[keyPtr]) < 0):
                    keyPtr = (keyPtr + 1)%len(key)
                
                keyChar = key[keyPtr]
                keyPtr = (keyPtr + 1)%len(key)
            cipher += (chr(((ord(plain[i]) -97 + ord(keyChar)) % 26) + 97))
        
        return cipher
    

    #This is a very simple fitness function based on the expected frequency of each letter in english 
      #There is lots of room for improvement in this function.
       # k is the key, and t is the encrypted text
    def fitness(k, t):
        #The expected frequency of each character in english language text according to
        #http://practicalcryptography.com/cryptanalysis/letter-frequencies-various-languages/english-letter-frequencies/
        expectedFrequencies = [] #Double[]
        expectedFrequencies.append(0.085) #Expected frequency of a
        expectedFrequencies.append(0.016) #Expected frequency of b
        expectedFrequencies.append(0.0316) #Expected frequency of c
        expectedFrequencies.append(0.0387) #Expected frequency of d
        expectedFrequencies.append(0.121) #Expected frequency of e
        expectedFrequencies.append(0.0218) #Expected frequency of f
        expectedFrequencies.append(0.0209) #Expected frequency of g
        expectedFrequencies.append(0.0496) #Expected frequency of h
        expectedFrequencies.append(0.0733) #Expected frequency of i
        expectedFrequencies.append(0.0022) #Expected frequency of j
        expectedFrequencies.append(0.0081) #Expected frequency of k
        expectedFrequencies.append(0.0421) #Expected frequency of l
        expectedFrequencies.append(0.0253) #Expected frequency of m
        expectedFrequencies.append(0.0717) #Expected frequency of n
        expectedFrequencies.append(0.0747) #Expected frequency of o
        expectedFrequencies.append(0.0207) #Expected frequency of p
        expectedFrequencies.append(0.001)  #Expected frequency of q
        expectedFrequencies.append(0.0633) #Expected frequency of r
        expectedFrequencies.append(0.0673) #Expected frequency of s
        expectedFrequencies.append(0.0894) #Expected frequency of t
        expectedFrequencies.append(0.0268) #Expected frequency of u
        expectedFrequencies.append(0.0106) #Expected frequency of v
        expectedFrequencies.append(0.0183) #Expected frequency of w
        expectedFrequencies.append(0.0019) #Expected frequency of x
        expectedFrequencies.append(0.0172) #Expected frequency of y
        expectedFrequencies.append(0.0011) #Expected frequency of z
    
        #Sanitize the cipher text and key
        d = t.lower() #String
        d = re.sub ("[^a-z]", "", d)
        d = re.sub ("\\s", "", d)
        cipher = [0] * len(t) #Int[]
        for x in range(len(t)): #Maybe len(d)?
            cipher[x] = (ord(d[x]) - 97)

        ke = k.lower() #String
        ke = re.sub ("[^a-z]", "", ke)
        ke = re.sub ("\\s", "", ke)

        key = list(ke) #Char[]
        for i in range (len(key)): 
            #print(i)
            #print(key[i])
            #print(ord(key[i]))
            key[i] = chr(ord(key[i])-97)

        charCounts = [0] * 26

        plain = [0] * len(cipher)

        #Decrypt each character
        keyPtr = 0 #Int
        for i in range(len(cipher)):
            keyChar = chr(0)
            if(len(key) > 0):
                #Ignore any value not in the expected range
                while(ord(key[keyPtr]) >25 or ord(key[keyPtr]) < 0):
                    keyPtr = (keyPtr + 1)%len(key)
                keyChar = key[keyPtr]
                keyPtr = (keyPtr + 1)%len(key)

            plain[i] = ((26 + cipher[i] - ord(keyChar))%26)
        
        #Count the occurences of each character
        for x in range(len(plain)):
            charCounts[plain[x]] += 1
        
        #Calculate the total difference between the expected frequencies and the actual frequencies 
        score = 0 #Double
        for y in range(len(charCounts)):
            score += abs(((float(charCounts[y]) / len(plain)) - expectedFrequencies[y]))
                
        return score
      
