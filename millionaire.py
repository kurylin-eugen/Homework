while True:
   print("Hello")
   print("Это игра Кто хочет стать миллионером!")
   print("ответьте на 10 вопросов, что бы выиграть 1000000$")
   input('Нажмите ENTER для продолжения...')
   
   import os
   os.system('cls' if os.name == 'nt' else 'clear')
   

   print("первый вопрос на 100$!")
   bank = 0

   print("первый месяц весны?")
   print("варианты ответов:")
   print("A. июнь")
   print("B. Март")
   print("C. Октябрь")
   print("D. Июль")
   
   ans1= input("Ответ - ")
   if ans1 == "B" or ans1 == "b":
       print(" правильный ответ")
       bank +=100
       print("Ваш выйгрыш: " + str(bank))
   else:
      print("ответ не верный")
      print("game over")
      print("Ваш выйгрыш: " + str(bank))
      break
   
   import os
   os.system('cls' if os.name == 'nt' else 'clear')


   print("Второй  вопрос на 200$!")
   print("Как звали кота из мультфильма Трое из простокрвашино?")
   print("варианты ответов:")
   print("A. Базилио")
   print("B. Василий")
   print("C. Потап")
   print("D. Матроскин")
   
   
   ans2= input("Ответ - ")      
    
   if ans2 == "D" or ans2 == "d":
       print(" правильный ответ")
       bank =200
       print("Ваш выйгрыш: " + str(bank))
   else:
       print("ответ не верный")
       print("game over")
       bank =100
       print("Ваш выйгрыш: " + str(bank))
       break
   
   import os
   os.system('cls' if os.name == 'nt' else 'clear')

   print("Третий вопрос на 1000$!")
   print("За чем послала жена мужа в мультфильме Падал прошлогодний снег?")
   print("варианты ответов:")
   print("A. За елкой")
   print("B. За снегом")
   print("C. За водкой")
   print("D. За  сосной")

   ans3= input("Ответ - ")
   
   if ans3 == "A" or ans3 == "a":
       print(" правильный ответ")
       bank =1000
       print("Ваш выйгрыш: " + str(bank))
   else:
       print("ответ не верный")
       print("game over")
       bank =200
       print("Ваш выйгрыш: " + str(bank))
       break
   
   import os
   os.system('cls' if os.name == 'nt' else 'clear')

   print("Четвертый вопрос на 5000$!")
   print("Какой знак восточного гороскопа следует за знаком Дракона?")
   print("варианты ответов:")
   print("A.  кабана")
   print("B.  крысы")
   print("C.  змеи")
   print("D.  собаки")

   ans4= input("Ответ - ")
   
   if ans4 == "C" or ans4 == "c":
       print(" правильный ответ")
       bank =5000
       print("Ваш выйгрыш: " + str(bank))
   else:
       print("ответ не верный")
       print("game over")
       bank =1000
       print("Ваш выйгрыш: " + str(bank))
       break
   
   import os
   os.system('cls' if os.name == 'nt' else 'clear')

   print("Пятый  вопрос на 10000$!")
   print("Как называют период времени, когда солнце в северных широтах не опускается за горизонт?")
   print("варианты ответов:")
   print("A.  полярный день")
   print("B.  заполярный день")
   print("C.  затмение ")
   print("D.  ночь")

   ans5= input("Ответ - ")
   
   if ans5 == "A" or ans5 == "a":
       print(" правильный ответ")
       bank =10000
       print("Ваш выйгрыш: " + str(bank))
   else:
       print("ответ не верный")
       print("game over")
       bank =5000
       print("Ваш выйгрыш: " + str(bank))
       break
   
   import os
   os.system('cls' if os.name == 'nt' else 'clear')

   print("Шестой   вопрос на 50000$!")
   print("Какой танец исполнил Чарли Чаплин в фильме Золотая лихорадка?")
   print("варианты ответов:")
   print("A.  ламбада")
   print("B.  танец булочек")
   print("C.  танго")
   print("D.  брейк данс")

   ans6= input("Ответ - ")
   
   if ans6 == "B" or ans6 == "b":
       print(" правильный ответ")
       bank =50000
       print("Ваш выйгрыш: " + str(bank))
   else:
       print("ответ не верный")
       print("game over")
       bank =10000
       print("Ваш выйгрыш: " + str(bank))
       break
   
   import os
   os.system('cls' if os.name == 'nt' else 'clear')

   print("Седьмой   вопрос на 100000$!")
   print("Какое прозвище носил король Англии Ричард I?")
   print("варианты ответов:")
   print("A.  Львиное сердце")
   print("B.  Бычья кровь")
   print("C.  Мезинец")
   print("D.  Безмятежный")

   ans7= input("Ответ - ")
   
   if ans7 == "A" or ans7 == "a":
       print(" правильный ответ")
       bank =100000
       print("Ваш выйгрыш: " + str(bank))
   else:
       print("ответ не верный")
       print("game over")
       bank =50000
       print("Ваш выйгрыш: " + str(bank))
       break
   
   import os
   os.system('cls' if os.name == 'nt' else 'clear')

   print("Восьмой   вопрос на 250000$!")
   print("Каким предметом китайцы стараются не пользоваться в преддверии Нового года, чтобы не разрушить счастья?")
   print("варианты ответов:")
   print("A.  Вилка")
   print("B.  Пила")
   print("C.  Нож")
   print("D.  Топор")

   ans8= input("Ответ - ")
   
   if ans8 == "C" or ans8 == "c":
       print(" правильный ответ")
       bank =250000
       print("Ваш выйгрыш: " + str(bank))
   else:
       print("ответ не верный")
       print("game over")
       bank =100000
       print("Ваш выйгрыш: " + str(bank))
       break
   
   import os
   os.system('cls' if os.name == 'nt' else 'clear')

   print("Девятый   вопрос на 500000$!")
   print(" Изучение соединений какого элемента является основой органической химии?")
   print("варианты ответов:")
   print("A.  Кислород")
   print("B.  Углерод")
   print("C.  Водород")
   print("D.  Азот")

   ans9= input("Ответ - ")
   
   if ans9 == "B" or ans9 == "b":
       print(" правильный ответ")
       bank =500000
       print("Ваш выйгрыш: " + str(bank))
   else:
       print("ответ не верный")
       print("game over")
       bank =250000
       print("Ваш выйгрыш: " + str(bank))
       break
   
   import os
   os.system('cls' if os.name == 'nt' else 'clear')

   print("Десятый   вопрос на 1000000$!")
   print("Как звали невесту Эдмона Дантеса, будущего графа Монте-Кристо?")
   print("варианты ответов:")
   print("A.  София")
   print("B.  Мерседес")
   print("C.  Эсмиральда")
   print("D.  Мария")

   ans10= input("Ответ - ")
   
   if ans10 == "B" or ans10 == "b":
       print(" правильный ответ")
       bank =1000000
       print(" Вы выиграли " + str(bank))
   else:
       print("ответ не верный")
       print("game over")
       bank =500000
       print("Ваш выйгрыш: " + str(bank))
       break
   break  




   