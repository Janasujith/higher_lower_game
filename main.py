#import the title logo and vs

from art import logo, vs
import random
from game_data import data

#compare A
def get_choice():
  return random.choice(data)


  

def format_data(account):
  name=account["name"]
  description=account["description"]
  country=account["country"]
  return(f'{name},a {description} from {country}')

def guess_check(guess,x,y):
  if x>y:
    return guess =='a'
  else:
    return guess =='b'

def game():
  print(logo)
  score=0
  game_continue = True
  account_A=get_choice()
  account_B=get_choice()
  
  while game_continue:
    account_A = account_B
    account_B=get_choice()
  
  while account_A == account_B:
    account_B=get_choice()
  
  
  print(f'compare A:{format_data(account_A)}')
  print(vs)
  print(f'against B:{format_data(account_B)}')
  
  #input
  guess= input("Who has more followers Type 'A' OR 'B':").lower()
  a_followers=account_A["follower_count"]
  print(a_followers)
  b_followers=account_B["follower_count"]
  print(b_followers)
  is_correct=guess_check(guess,a_followers,b_followers)
  
  #compare the follower
  if is_correct:
    score+=1
    print(f'you are correct!,the score is{score}')
  else:
    game_continue = False
    print(f"Sorry, that's wrong. Final score:{score}")


game()

  



 
    
  

    

    

  
  


