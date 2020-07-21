name=input('What is your name: ')
print( )
print('Hello',name,'Welcome to the quiz!!')
ans=input('Are you brave enough to play(yes/no): ')
score=0
totalq=5

print( )
if ans.lower()=='yes':
    print('Total no.of questions is 5')
    print( )
    
    ans=input('1.Which place is Jupiter in the Solar system?: ')
    if ans=='5' or ans.lower().strip()=='five':
        score+=1
        print('Your answer is Correct')
    else:
        print('Incorrect Answer')
        print('Correct answer is 5(Five)')
    print( )

    ans=input('2.Which Is the hottest Planet in the Solar System?: ')
    if ans.lower().strip()=='venus':
        score+=1
        print('Your answer is Correct')
    else:
        print('Incorrect Answer')
        print('Correct answer is Venus')
    print( )

    ans=input('3.How many planets in the Solar System have ring around them?: ')
    if ans=='4' or ans.lower().strip()=='four':
        score+=1
        print('Your answer is Correct')
    else:
        print('Incorrect Answer')
        print('Correct answer is 4')
    print( )

    ans=input('4.Which planet looks reddish in the sky?: ')
    if ans.lower().strip()=='mars':
        score+=1
        print('Your answer is Correct')
    else:
        print('Incorrect Answer')
        print('Correct answer is Mars')
    print( )

    ans=input('5.Which is the lightest planet in the Solar System: ')
    if ans.lower().strip()=='saturn':
        score+=1
        print('Your answer is Correct')
    else:
        print('Incorrect Answer')
        print('Correct answer is Saturn')
    print( )

    print('Game Over')
    print( )
print('Quiz analysis:')
print('You got',score,'question\'s correct')
mark=(score/totalq)*100
print('Mark: ',str(mark)+'%')
print('Remarks:')
if mark==0:
    print('Bad performance')
if mark==40:
    print('Ok performnace')
if mark==60:
    print('Moderate performance')
if mark==80:
    print('Very nice performance')
if mark==100:
    print('Excellent performance!!')
print('Good Bye',name,'and thank you for playing,see you again!!!')


    
          
    



