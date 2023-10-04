
N=int(input())
singular_noun=input("Enter the singular Noun:")
# fe="ves"
if N==1:
  print(f"{N} {singular_noun}")
else:
  if singular_noun[-2:]=="fe":
    str_1=singular_noun.replace("fe","ves")
    print(f"{N} {str_1}")
  elif singular_noun[-1]=="y":
    if singular_noun[-2]=="a"or singular_noun[-2]=="e"or singular_noun[-2]=="i"or singular_noun[-2]=="o"or singular_noun[-2]=="u":
      str_7=singular_noun+"s"
      print(f"{N} {str_7}")
    else:
      str_2=singular_noun.replace("y","ies")
      print(f"{N} {str_2}")
  elif singular_noun[-2:]=="sh" or singular_noun[-2:]=="ch":
    str_3=singular_noun+"es"
    print(f"{N} {str_3}")
  elif singular_noun[-2:]=="us":
    str_4=singular_noun.replace("us","i")
    print(f"{N} {str_4}")
  elif singular_noun[-2:]=="ay" or  singular_noun[-2:]=="oy" or  singular_noun[-2:]=="ey" or  singular_noun[-2:]=="uy":
    str_5=singular_noun+"s"
    print(f"{N} {str_5}")

  else:
    str_6=singular_noun+"s"
    print(f"{N} {str_6}")
    
    
    
  
