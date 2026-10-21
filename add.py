c=pd.DataFrame([[100,80,90],[90,89,99],[99,23,67]],index=['hema','suni','viju'],columns=['phy','chem','math'])
c["total"]=c["phy"]+c["chem"]+c["math"]
c
