def copy_string(num_of_copies, string):
    result = ""
    
    for i in range(num_of_copies):
        result = result + string
    
    return result

print(copy_string(3, "MyString"))
print(copy_string(5, "Hawk"))