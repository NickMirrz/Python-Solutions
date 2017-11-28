codes = {'A':'%','a':'9','B':'@','b':'#','C':'1',
         'c':'2','D':'3','d':'4','E':'5','e':'6',
         'F':'7','f':'8','G':'0','g':'}','H':'{', 
         'h':']','I':'[','i':',','J':'.','j':'>',
         'K':'<','k':'/','L':'?','l':'\'','M':'\"',
         'm':':','N':';','n':'+','O':'$', 'o':'-',
         'P':'=', 'p':'!', \
         'Q':'$', 'q':'%','R':'^', 'r':'&','S':'*',
         's':'(','T':')', 't':'~', \
         'U':'`', 'u':'?','V':'\\', 'v':'i','W':'h',
         'w':'g','X':'f', 'x':'e', \
         'Y':'d', 'y':'c','Z':'b', 'z':'a'}

#Open a file named ‘file.txt’ which contains any important messages in read mode into a file object file1.

file1 = open('file.txt','r')


#Read the contents of file referred by file1 into file_read.

file_read = file1.read()


#Close the file referred by file1.

file1.close()

#Create or open a file named ‘encr.txt’ to save the characters of ‘file.txt’ in encrypted form that is
#characters’ codes into the file object encr_file.

encr_file = open('encr.txt','w')

#Run a loop for each character ch of the string referred by file_read.

for ch in file_read:
    
#If the character ch is found in dictionary codes, write its encrypted code that is the value in the
#dictionary at the specified key into the file referred by encr_file.

    if ch in codes:
       encr_file.write(codes[ch])

#If the character ch is not found in dictionary codes, write it as it is into the file referred by encr_file.

    else:
        encr_file.write(ch)

#Close the file referred by encr_file.
encr_file.close()

#Program to read encrypted file and display its decryption
#Now write a program to read encrypted file and display its decrypted message.
#Open the file ‘encr.txt’ in read mode into encr_file.

encr_file = open('encr.txt','r')

#Read its contents into file_read.
file_read = encr_file.read()

#Close the file referred by encr_file.
encr_file.close()

#Assign all the items of the dictionary codes to the tuple codes_items.
codes_items = codes.items()

#Run a loop for each character ch in file_read.
for ch in file_read:
    
#If the character is not found in the values of the dictionary referred by codes or ch is not equal to
#a full stop then print the character as it is on the screen.
    if not ch in codes.values() or ch=='.':
        print(ch)

else:
#If the character is found in the values of the dictionary referred by codes or ch is not equal to a
#full stop then print the key with which the value is associated.

    for k,v in codes_items:
        if ch == v and ch != '.':
            print(k, end='')
