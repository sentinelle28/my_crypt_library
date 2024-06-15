

def normalised_key(key,element_to_put):
    normalised_key_text = ""
    for object in key:
        normalised_key_text += str(object)
        normalised_key_text += str(element_to_put)
    print(normalised_key_text)
    return normalised_key_text
    
    
def unormalized(text,element_to_detect):
    extracted_list = []
    elements = text.split(str(element_to_detect))
    for element in elements:
        if element:
            extracted_list.append(element)
    return extracted_list
                    
            

test = [20,30,60]      
print(unormalized(normalised_key(test,534),534))
