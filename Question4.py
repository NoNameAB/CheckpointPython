def missing_char(s,n):
             letters = []
             for i in s:
                          letters.append(i)
             if n > len(letters) - 1 :
                          print("N/A")
             else :
                          del letters[n]
                          print(''.join(letters))
x = input("Type a word : ")
y = int(input("Type a number : "))
missing_char(x, y)
