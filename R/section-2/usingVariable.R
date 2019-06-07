A<-10
B<-20
C<-A+B
C

var1<-2.5
var2<-4

result<-var1/var2

greeting<-'Hello'

name<-'Lalit'

message<-paste(greeting,name)
message

#========LOGICAL VARIABLES AND OPERATORS=======

#TRUE T
#FALSE F
4<10
10>20
4==5
#==
#!=
#<
#>
#<=
#>=
#! (OR)
#& (AND)
#isTRUE(x)


#========== WHILE LOOP=======

while(T){
  print('infinit loop')
}

counter<-1
while(counter<12){
  print(counter)
  counter=counter+1
}

#======for loop=====

for(i in 1:5){
  print('hello')
}


#======if statement=====

x<-rnorm(1)
x

if(x>1){
  answer<-'Greater than 1'
}else if (x>=-1){
  
  answer<-'Between -1 and 1'
}else{
  answer<-'Less than -1'
}
answer




