
scanfile=open("circuit_ran30sff.v", "a")
total_ff=534
add_ff=161
ff_count=1
with open ("/content/circuit.v",'r') as outfile:
   line1= outfile.readlines()
   for i in range (0,191):
     linex= str(line1[i])
     listy= linex.split()
     if listy[0]=="DFFX1":
       new_str2="DFFX1 "+ listy[1]+" "+"(.CK(CK1),"+" "+ listy[3]+", "+listy[4]+"\n"
       scanfile.write(new_str2)
     else:
       a=line1[i]
       scanfile.write(a)
with open ("/content/circuit.v",'r') as outfile:
   linels=[]
   lines= outfile.readlines()
   si="SI"
   for x_var in range (191, len(lines)):


       line1= str(lines[x_var])
       list1= line1.split()
       if (list1[0]=="DFFX1"):
           if(ff_count<=add_ff):
               d=str(list1[3]).strip(".D(")
               d=d.strip("),")
               #print(d)


               q=str(list1[4]).strip(".Q(")
               q=q.strip("));")
               #print(q)
               print(list1[1])


               new_str="S_DFFX1"+" S_"+list1[1]+" "+"(.CK(CK2),"+" "+ list1[3]+" .SE(SE), .SI("+si+ "), "+list1[4]+"\n"
               si=q
               scanfile.write(new_str)
               ff_count=ff_count+1
               if(ff_count==add_ff+1):
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
