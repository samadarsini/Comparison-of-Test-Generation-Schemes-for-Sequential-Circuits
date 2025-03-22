scanfile=open("circuit_30sff.v", "a")
ff_c=1
with open ("/content/circuit.v",'r') as outfile:
   linels=[]
   lines= outfile.readlines()
   si="SI"
   for x_var in range (0, len(lines)):
       line1= str(lines[x_var])
       list1= line1.split()
       if (list1[0]=="DFFX1"):
           if(ff_c<=161):
               d=str(list1[3]).strip(".D(")
               d=d.strip("),")
               q=str(list1[4]).strip(".Q(")
               q=q.strip("));")
               new_str="S_DFFX1"+" S_"+list1[1]+" "+"(.CK(CK2),"+" "+ list1[3]+" .SE(SE), .SI("+si+ "), "+list1[4]+"\n"
               si=q
               scanfile.write(new_str)
               ff_c=ff_c+1
               if(ff_c==161+1):
                   buff_str="BUFX1 S_BUFX1_SO "+'(.A('+q+'), .Y(SO));\n'
                   scanfile.write(buff_str)
           else:
             if list1[0]=="DFFX1":
               new_str1="DFFX1 "+ list1[1]+" "+"(.CK(CK1),"+" "+ list1[3]+", "+list1[4]+"\n"
               scanfile.write(new_str1)
             else:
               scanfile.write(line1)
       else:
           scanfile.write(line1)
scanfile.close()