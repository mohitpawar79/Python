val = int(input())
 
# -------------------------------------------------------------------------------------------------------------------------------------------------

# *
# *  *
# *  *  *
# *  *  *  *
# *  *  *  *  *

# for i in range(val+True):
#     for j in range(i):
#         print("* ",end=" ")
#     print()


# -------------------------------------------------------------------------------------------------------------------------------------------------

# * * * * * 
# * * * *
# * * *
# * *
# *

# for i in range(val+True):
#     space = i 
#     star = (val- i )
#     line = ''
#     if(space >= i):
#         line += "* " * star
#         line += "  " * space 
        
#     print(line)





# -------------------------------------------------------------------------------------------------------------------------------------------------
# * * * * * * * * * * 
# * * * *     * * * *
# * * *         * * *
# * *             * *
# *                 *

# for i in range(val+True):
#     space = i 
#     star = (val- i )
#     line = ''
#     if(space >= i):
#         line += "* " * star
#         line += "  " * space 
#         line += "  " * space 
#         line += "* " * star
#     print(line)
    

# -------------------------------------------------------------------------------------------------------------------------------------------------
fullpatern = ''
for i in range(val+True):
    
    space = i 
    star = (val- i )
    line = ''
    if(space >= i):
        line += "* " * star
        line += "  " * space 
        line += "  " * space 
        line += "* " * star
    fullpatern +=line 
    

for i in range(val+True):
        space = (val- i ) 
        star = i
        line = ''
        line += "* " * star
        line += "  " * space 
        line += "  " * space 
        line += "* " * star
        fullpatern +=line
print(fullpatern)
