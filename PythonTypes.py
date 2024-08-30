"""
Get understanding of type checking fastAPI
"""

def add(firstName: str | list[int] | None, seoondName : str | None):
    return firstName + " " + seoondName

# firstName = 34
firstName = "rishabh"
firstName.title()
secondName = "Gupta"
name = add(firstName, secondName)
print(name)