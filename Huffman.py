import heapq

class HeapNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.leftNode = None
        self.rightNode = None

    def __lt__(self, other):
        return self.freq < other.freq
    
    def __gt__(self, other):
        return self.freq > other.freq
    
    def __eq__(self, other):
        if(other == None):
            return False
        if(not isinstance(other, HeapNode)):
            return False
        return self.freq == other.freq
    
    def toString(self):
        return "{}\t{}".format(self.char, self.freq)
    
    
class iHuffman:
    
    def __init__(self, frequencies):
        
        self.frequencies = frequencies
        self.nodeArr = []
        self.huffmanCodes = {}
        
        self.createHeap()
        self.buildHuffmanTree()
        self.generateCode()

        
    def createHeap(self):
        for char in frequencies:
            heapq.heappush(self.nodeArr, HeapNode(char, frequency[char]))

            
    def buildHuffmanTree(self):
        while(len(self.nodeArr)>1):
            leftNode = heapq.heappop(self.nodeArr)
            rightNode = heapq.heappop(self.nodeArr)
            
            newMergedNode = HeapNode(None, leftNode.freq + rightNode.freq)
            
            newMergedNode.leftNode = leftNode
            newMergedNode.rightNode = rightNode
            
            heapq.heappush(self.nodeArr, newMergedNode)
    
    
    def traverseNode(self, headNode, code):
        if(headNode == None):
            return
        
        if(headNode.char != None):
            self.huffmanCodes[headNode.char] = code
            return

        self.traverseNode(headNode.leftNode, code + "0")
        self.traverseNode(headNode.rightNode, code + "1")

        
    def generateCode(self):
        headNode = heapq.heappop(self.nodeArr)
        code = ""
        self.traverseNode(headNode, code)
        
        
    def encode(self, inputFilePath):
        inputFile = open(inputFilePath, 'r')
        text = inputFile.read()
        text = text.rstrip()
        inputFile.close()
        
        output = ""
        for character in text:
            output = output + self.huffmanCodes[character]
        print(output)
            
        outputFile = open('output.txt', 'w') 
        outputFile.write(output)
        outputFile.close()        
        
        
    def decode(self, inputFilePath):
        inputFile = open(inputFilePath, 'r')
        text = inputFile.read()
        text = text.rstrip()
        inputFile.close()
        
        code = ""
        output = ""
        
        inverseHuffmanCodes = {v: k for k, v in self.huffmanCodes.items()}
        
        for char in text:
            code = code + char
            if(code in inverseHuffmanCodes):
                character = inverseHuffmanCodes[code]
                output = output + character
                code = ""
        print(output)
        
        outputFile = open('decoded.txt', 'w') 
        outputFile.write(output)
        outputFile.close()
        
        
        
        
frequencies = { "A": 8.167, "B": 1.492, "C": 2.782, "D": 4.253, "E": 12.702, "F": 2.228, "G": 2.015, "H": 6.094, "I": 6.966, "J": 0.153, "K": 3.872, "L": 4.025, "M": 2.406, "N": 6.749, "O": 7.507, "P": 1.929, "Q": 0.095, "R": 5.987, "S": 6.327, "T": 9.256, "U": 2.758, "V": 0.978, "W": 5.370, "X": 0.150, "Y": 3.978, "Z": 0.074}     


Commpressor = iHuffman(frequencies)

#Taking User input to choose Action
print('Choose an option:\n 1. Encode \n 2. Decode \n')
userChoice = int(input())

#Performing Action
if userChoice == 1:
    #takes an text file, creates encoded output.txt file and prints encoded string 
    Commpressor.encode('input.txt')
elif userChoice == 2:
    #takes an encoded text file, creates decoded.txt file and prints decoded string 
    Commpressor.decode('output.txt')
else:
    print("You did not choose a valid option!")
    
