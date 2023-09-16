SCORE =0

class Questions:

    def Data(self, Question, A, B, C, D, Answer):
        self.Question= Question
        self.A= A
        self.B= B
        self.C= C
        self.D= D
        self.Answer = Answer
    def Display (self):
        print(f'{self.Question}')
        print(f'A, {self.A}')
        print(f'B, {self.B}')
        print(f'C, {self.C}')
        print(f'D, {self.D}')


Question1= Questions()
Question1.Data('Who is the CEO of Google?','Sundar Pichai','Elon Musk','Mark Zuckerberg','None of the above','A')
Question1.Display()

# User_Answer= input("Enter Your Choice ").upper()
# if User_Answer== Question1.Answer:
#     SCORE= SCORE+1
#     print('Answer is correct')
#     print(f'Your score is {SCORE}/1')
# else:
#     print("Answer is wrong")
#     print(f'Your score is {SCORE}/1')

def Answer_check(Answer, Score, Question_count):
    User_Answer = input("Enter Your Choice ").upper()
    global Global_Score
    if User_Answer == Answer:

        Global_Score = Score + 1
        print('Answer is correct')
        print(f'Your score is {Global_Score}/{Question_count}')

    else:
        Global_Score = Score
        print("Answer is wrong")
        print(f'Your score is {Global_Score}/{Question_count}')


Answer_check(Question1.Answer,SCORE,1)
SCORE= Global_Score
Question2= Questions()
Question2.Data('Which of the following site is not a search engine ?','Google','BBC World','Microsoft Bing','Yahoo','B')
Question2.Display()
Answer_check(Question2.Answer,SCORE,2)
SCORE= Global_Score


