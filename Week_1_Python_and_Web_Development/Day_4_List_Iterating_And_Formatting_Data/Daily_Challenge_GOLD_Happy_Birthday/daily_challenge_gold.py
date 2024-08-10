from datetime import datetime
user_input=input("Please input your birthdate ")
today=datetime.today()
birthdate=datetime.strptime(user_input,'%d/%m/%Y')
users_age=today.year-birthdate.year-((today.month,today.day)<(birthdate.month,birthdate.date))
candles="I"*(users_age%10)
creame=int((13-len(candles))/2)*"_"
cake=f"""
      {creame}{candles}{creame}
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
   """
print(cake)