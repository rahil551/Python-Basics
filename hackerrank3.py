def time(s):
    if s[-2]=='P':
        # print('yes')
        if s[0:2] == "12":
            # print('yes')
            return s[:-2]
        else:
                x = int(s[0:2]) + 12
                s =  s.replace(s[:2],str(x))
                return s[:-2]   
    else:
        if s[1]== '2':
            return "00" + s[2:-2]
        else: 
            return s[:-2]
           


s = "12:00:00PM"

print(time(s))
