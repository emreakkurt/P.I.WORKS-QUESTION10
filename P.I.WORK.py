def reverse_string(input_string):    
    words_list = input_string.split()    
 
    words_list.reverse()
    
    output_string = ' '.join(words_list)
    
    return output_string
input_string = "The weather is so sunny nowadays Life is so beautiful"
output_string = reverse_string(input_string)
print(output_string)
