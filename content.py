def reverse_word(old_word):
   word = ''   
   for index in range(len(old_word)-1, -1, -1):
       word += old_word[index]
   return word
print(reverse_word("nohtyP"))
