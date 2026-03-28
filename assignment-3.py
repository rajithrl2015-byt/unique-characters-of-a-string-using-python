#CHECK UNIQUE CHARECTERS IN A STRING
#-------------------------------------------------

#for entering our desired string into this programme we can use "input function"

g = input("enter your desired string:....")

print("-------------------------------")

def charecter(g):                              #declared a function in variable (g)
    result = ""

    for i in (g):        #repeate block of code for each item in our string --use for loop
        if i not in (result):
            result = result+i   #after excicution result will saved on the variable name result
    return result
    
charecter(g)                # call our function for excicution

print("your unique charecters in your string  \n.........................................\n",charecter(g))
