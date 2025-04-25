

def normalised_key(key:list,element_to_put:str)->str:
    normalised_key_text:str = ""
    for object in key:
        normalised_key_text += str(object)
        normalised_key_text += str(element_to_put)
    return normalised_key_text
    
    
def unormalized(text:str,element_to_detect:str)->list[str]:
    extracted_list:list[str] = []
    elements:list[str] = text.split(str(element_to_detect))
    for element in elements:
        if element:
            extracted_list.append(element)
    return extracted_list
                    
            

