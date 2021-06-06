#Takes 4 arguments - a: first number of ip (e.g. 192), b: second number, c: third number, and e (fourth number MAX/end of the IP range) and returns a list containing strings of all the ip addresses  within the range of the final number
#I wrote this script for creating custom rules relating to my LAN and Windows updates 
# I only wanted to download/send updates to my LAN and nothing over WAN as is done by Delivery Optimisation in Windows 10. Creating custom rules in Windows defender does not allow for ip ranges (eg with a colon), yet it does allow for IPs separated by a comma.
# Voila. For some fun the next step I do on this will be implementing the same feature for the first three digits of the IP, which, although generally useless, would be an interesting learning experience.

def listgen(a,b,c,e):
    a = str(a)
    b = str(b)
    c = str(c)
      
    maxval = [str(e) for e in range (1,e + 2)]
   
    i = 0
    
    while i < e + 1:    
        for item in maxval[i]:
            maxval[i] = (a + "." + b + "." + c + "." + str(i))
        i += 1

    z = 0   

    while z < e + 1:
         
        for item in maxval[i]:
            maxval[z] = int(maxval[z])
        z += 1
        
    return(maxval)

if __name__ == "__main__":
    print(listgen(192, 168, 1, 200))
    
