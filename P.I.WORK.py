def reverse_string(input_string):
    # Girdi stringini boşluk karakterine göre kelimelere ayır
    words_list = input_string.split()
    
    # Kelime listesini tersine çevir
    words_list.reverse()
    
    # Tersine çevrilmiş kelime listesini aralarında boşluk karakteri olan bir stringe dönüştür
    output_string = ' '.join(words_list)
    
    return output_string
input_string = "The weather is so sunny nowadays Life is so beautiful"
output_string = reverse_string(input_string)
print(output_string)
