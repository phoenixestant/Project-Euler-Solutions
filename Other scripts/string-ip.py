#Takes 4 arguments - a: first number of ip (e.g. 192), b: second number, c: third number, and e (fourth number MAX/end of the IP range) and returns a list containing strings of all the ip addresses  within the range of the final number
#I wrote this script for creating custom rules relating to my LAN and Windows updates 
# I only wanted to download/send updates to my LAN and nothing over WAN as is done by Delivery Optimisation in Windows 10. Creating custom rules in Windows defender does not allow for ip ranges (eg with a colon), yet it does allow for IPs separated by a comma.
# Voila. For some fun the next step I do on this will be implementing the same feature for the first three digits of the IP, which, although generally useless, would be an interesting learning experience.

def listgen(a,b,c,e):
    a = str(a)
    b = str(b)
    c = str(c)
      
    maxval = [str(e) for e in range (1,e + 2)]
   
    i = -2
    
    while i < e + 1:    
        for item in maxval[i]:
            maxval[i] = (a + "." + b + "." + c + "." + str(i))
        i += 1

    z = -2   

    while z < e + 1:
         
        for item in maxval[z]:
            maxval[z] = maxval[z]
        z += 1
    
    # g = -2

    # while g < e-1:
         
    #     for item in maxval:
    #         isinstance(item, str)
    #         print(item + ",")
            
    #     g += 1
        
    return maxval





if __name__ == "__main__":
    print(listgen(192, 168, 1, 200))

    #It's annoying you can't change the commit discussion after it's pushed. Tried to replace the apostrophes and spaces in my array via numeous methods.
    #Even when I did turn them into integers, it assumed they were decimal places.
    #The closest I got is commented out above, but that has the unfortunate effect of placing each IP on a new line, they need no spaces, line breaks, or apostrophes.
    #I'm sure there is a way to print continuously on the next line but I was meant to be asleep hours ago. Damn you EMIL! *raises fist*.
    #Word find and replace did the trick with my list :)