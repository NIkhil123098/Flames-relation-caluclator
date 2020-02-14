
g="RELATION CALUCLATOR                    $nikhil$";
print (g.center(80));
print ("NOTE:There is no space between letters");
x=input("Enter your name:");
y=input("Enter another person name:");
z="flames";
a1=x.count('a',0,len(x));
b1=x.count('b',0,len(x));
c1=x.count('c',0,len(x));
d1=x.count('d',0,len(x));
e1=x.count('e',0,len(x));
f1=x.count('f',0,len(x));
g1=x.count('g',0,len(x));
h1=x.count('h',0,len(x));
i1=x.count('i',0,len(x));
j1=x.count('j',0,len(x));
k1=x.count('k',0,len(x));
l1=x.count('l',0,len(x));
m1=x.count('m',0,len(x));
n1=x.count('n',0,len(x));
o1=x.count('o',0,len(x));
p1=x.count('p',0,len(x));
q1=x.count('q',0,len(x));
r1=x.count('r',0,len(x));
s1=x.count('s',0,len(x));
t1=x.count('t',0,len(x));
u1=x.count('u',0,len(x));
v1=x.count('v',0,len(x));
w1=x.count('w',0,len(x));
x1=x.count('x',0,len(x));
y1=x.count('y',0,len(x));
z1=x.count('z',0,len(x));
a2=y.count('a',0,len(x));
b2=y.count('b',0,len(x));
c2=y.count('c',0,len(x));
d2=y.count('d',0,len(x));
e2=y.count('e',0,len(x));
f2=y.count('f',0,len(x));
g2=y.count('g',0,len(x));
h2=y.count('h',0,len(x));
i2=y.count('i',0,len(x));
j2=y.count('j',0,len(x));
k2=y.count('k',0,len(x));
l2=y.count('l',0,len(x));
m2=y.count('m',0,len(x));
n2=y.count('n',0,len(x));
o2=y.count('o',0,len(x));
p2=y.count('p',0,len(x));
q2=y.count('q',0,len(x));
r2=y.count('r',0,len(x));
s2=y.count('s',0,len(x));
t2=y.count('t',0,len(x));
u2=y.count('u',0,len(x));
v2=y.count('v',0,len(x));
w2=y.count('w',0,len(x));
x2=y.count('x',0,len(x));
y2=y.count('y',0,len(x));
z2=y.count('z',0,len(x));
a3=min(a1,a2);
b3=min(b1,b2);
c3=min(c1,c2);
d3=min(d1,d2);
e3=min(e1,e2);
f3=min(f1,f2);
g3=min(g1,g2);
h3=min(h1,h2);
i3=min(i1,i2);
j3=min(j1,j2);
k3=min(k1,k2);
l3=min(l1,l2);
m3=min(m1,m2);
n3=min(n1,n2);
o3=min(o1,o2);
p3=min(p1,p2);
q3=min(q1,q2);
r3=min(r1,r2);
s3=min(s1,s2);
t3=min(t1,t2);
u3=min(u1,u2);
v3=min(v1,v2);
w3=min(w1,w2);
x3=min(x1,x2);
y3=min(y1,y2);
z3=min(z1,z2);
nt=len(x)+len(y)-2*(a3+b3+c3+d3+e3+f3+g3+h3+i3+j3+k3+l3+m3+n3+o3+p3+q3+r3+s3+t3+u3+v3+w3+x3+y3+z3)-1;
t=""
if(z[nt%6]==z[0]) :
 for i in range(1,6) :
  t=t+z[i%6];
elif(z[nt%6]==z[1]) :
 for i in range(2,7) :
  t=t+z[i%6];
elif(z[nt%6]==z[2]) :
 for i in range(3,8) :
  t=t+z[i%6];
elif(z[nt%6]==z[3]) :
 for i in range(4,9) :
  t=t+z[i%6];
elif(z[nt%6]==z[4]) :
 for i in range(5,10) :
  t=t+z[i%6];
else :
 for i in range(6,11) :
  t=t+z[i%6];
n=t;
t="";
if(n[nt%5]==n[0]) :
 for i in range(1,5) :
  t=t+n[i%5];
elif(n[nt%5]==n[1]) :
 for i in range(2,6) :
  t=t+n[i%5];
elif(n[nt%5]==n[2]) :
 for i in range(3,7) :
  t=t+n[i%5];
elif(n[nt%5]==n[3]) :
 for i in range(4,8) :
  t=t+n[i%5];
else :
 for i in range(5,9) :
  t=t+n[i%5];
a=t;
t="";
if(a[nt%4]==a[0]) :
 for i in range(1,4) :
  t=t+a[i%4];
elif(a[nt%4]==a[1]) :
 for i in range(2,5) :
  t=t+a[i%4];
elif(a[nt%4]==a[2]) :
 for i in range(3,6) :
  t=t+a[i%4];
else :
 for i in range(4,7) :
  t=t+a[i%4];
b=t;
t="";
if(b[nt%3]==b[0]) :
 for i in range(1,3) :
  t=t+b[i%3];
elif(b[nt%3]==b[1]) :
 for i in range(2,4) :
  t=t+b[i%3];
else :
 for i in range(3,5) :
  t=t+b[i%3];
c=t;
t="";
if(c[nt%2]==c[0]) :
 for i in range(1,2) :
  t=t+c[i%2];
else :
 for i in range(2,3) :
  t=t+c[i%2];
if(t=='f') :
 print ("<------    The relation between",x,"and",y,"is:-Friendship    ----->");
elif(t=='l') :
 print ("<-----   The relation between",x,"and",y,"is:-Love   ----->");
elif(t=='a') :
 print ("<-----   The relation betwwen",x,"and",y,"is:-Affection Love   ----->");
elif(t=='m') :
 print ("<-----   The relation between",x,"and",y,"is:-Marriage or mother like love   ----->");
elif(t=='e') :
 print ("<------   The relation between",x,"and",y,"is:-Enemies   ------>");
else :
 print ("<-----   The relation between",x,"and",y,"is:-siblings(i.e.,brother-brother or sister-sister or brother-sister   ----->");










