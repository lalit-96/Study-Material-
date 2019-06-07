
# Matrix operation

Games
#accuracy
FieldGoals
accuracy=FieldGoals/FieldGoalAttempts
accuracy

#goal per game

goal_per_game=round(FieldGoals/Games,0)
goal_per_game

#Visualizing with matplot()

?matplot()

#Creating your first function
myplot<-function(data,rows){
  Data<-data[rows,,drop=F]
  matplot(t(Data),type='b',pch=15:18,col=c(1:4,6))
  legend('bottomleft',inset=0.01,legend=Players[rows],pch=15:18,col=c(1:4,6),horiz=F)
  
}
myplot(Salary,1:3)

