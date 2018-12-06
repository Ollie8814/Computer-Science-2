import webbrowser as wb
import pyautogui as pg
import time as t
points = 0
show = pg.prompt ("What is your favorite TV show? ")

if show == "The Office":
    pg.alert ("Bears. Beets. Battlestar Galactica.")
    t.sleep(.5)
    points += 1500000000000000000000000000000000
    wb.open ("https://www.youtube.com/watch?v=uyIVAm9PVrI")
elif show == "Parks and Rec":
    pg.alert ("Good Show")
    t.sleep(3)
    wb.open ("https://www.youtube.com/watch?v=ZbUf9mnm5TA")
    points += 100
elif show == "30 Rock":
    pg.alert ("You made a bad call. I fixed it. So I'm not apologizing for anything.")
    t.sleep(3)
    points += 75
elif show == ("The Office UK"):
    pg.alert == "Just Be Quiet."
    wb.open ("https://www.youtube.com/watch?v=aYmOqPFyJPw")
    t.sleep(3)
    points -= 150000000000000000000000000000
elif show == "The Flash":
    pg.alert ("Why are you the way that you are?")
    t.sleep(3)
    points -= 1000
elif show == "Friends":
    pg.alert ("You watch that show because you have none")
    wb.open ("https://www.youtube.com/watch?v=Niu9Zmrx0p8")
    t.sleep(3)
    points -= 100
else:
    pg.alert ("That's good")

MLB_team = pg.prompt ("What is your favorite MLB team? ")

if MLB_team == "The Yankees":
    t.sleep(3)
    pg.alert ("Yes!Yes!Yes!Yes!Yes!Yes!Yes!")
    wb.open ("https://www.youtube.com/watch?v=yhgXvWOosDE")
    points += 1500000000000000
elif MLB_team == "The Mets":
    pg.alert ("too bad for you")
    t.sleep(3)
    wb.open ("https://www.youtube.com/watch?v=mshKr1l4nm0")
    points += 100
elif MLB_team == "The Red Sox":
    wb.open ("https://www.youtube.com/watch?v=umDr0mPuyQc")
    t.sleep(3)
    pg.alert ("BOOOOOOOOOOOOOOOOOOOOOOOOOOOO.")
    points -= 15000000000000000000
elif MLB_team == "The Padres":
    pg.alert ("Oof.")
    t.sleep(3)
    wb.open ("https://www.youtube.com/watch?v=EuZeff2y32M")
elif MLB_team == "The Twins":
    pg.alert ("Hey, look! It's snowing")
    t.sleep(3)
elif MLB_team == "The Dodgers":
    pg.alert ("Good Luck. You will need it.")
    t.sleep(3)
else:
    pg.alert ("Ok, Ok")

Video_game = pg.prompt ("What is your favorite video game?")

if Video_game == "Fortnite":
    pg.alert ("A good mind, you have")
    points += 10000
elif Video_game == "Star Wars Battlefront":
    pg.alert ("A good game")
    points += 1000
elif Video_game == "PUBG":
    pg.alert ("No. Just stop. Stop Talking. I don't want to do any of that stuff.")
    wb.open ("https://media1.tenor.com/images/cb65908da07b3c3bf190aa3df0651ecf/tenor.gif?itemid=12104995")
    points -= 100000000000000000
elif Video_game == "Realm Royale":
    pg.alert ("Boooo")
    wb.open ("https://www.youtube.com/watch?v=VNfPPjSh4tE")
    points -= 1000000
elif Video_game == "Pokemon Sun":
    pg.alert ("I think I'm gonna throw up")
    wb.open ("https://www.youtube.com/watch?v=layc9CIvxCo")
    points -=100000000000000000000
elif Video_game == "Black Ops 4":
    pg.alert ("Let's just say I saw what both of you want me to see")
    wb.open ("https://www.youtube.com/watch?v=31g0YE61PLQ")
else:
    pg.alert ("NO GOD! NO GOD PLEASE NO! NO! NO! NOOOOOOOOOOOOOO!")
    t.sleep(3)

Food = pg.prompt ("What is your favorite food")

if Food == "Pizza":
    pg.alert ("Everybody loves pizza. Pizza is like the food that bonds all people")
    wb.open ("https://www.youtube.com/watch?v=TRgEeDR98X8")
    t.sleep(3)
    points += 10000000000000000
elif Food == "pasta":
    pg.alert ("Don't eat two much Pasta Alfredo before a 5k")
    wb.open ("https://www.youtube.com/watch?v=9-e5y-3dyUs")
    t.sleep(3)
    points += 100000000000000
elif Food == "Sushi":
    pg.alert ("I could really use some New York style sushi tonight. And you know what? I'm gonna get it")
    points += 10000000000
elif Food == "Brussels Sprouts":
    pg.alert ("Why are you the way that you are?")
    wb.open ("https://www.youtube.com/watch?v=37XeFwHi3mU")
    points -= 1000000000000 
elif Food == "Dumplings":
    pg.alert ("Take those home to your wife")
    points += 100000
elif Food == "Bacon":
    pg.alert ("Bacon. Just Bacon.")
    wb.open ("https://www.youtube.com/watch?v=cS9qCre_sv8")
    points += 1000000000
else:
    pg.alert ("You. You. You. You. You. Oughta Know")
    t.sleep(3)

movie = pg.prompt ("What is your favorite movie")

if movie == "Star Wars":
    pg.alert ("Mooooovie Monday!")
    wb.open ("https://www.youtube.com/watch?v=g1fIH6GMIJg")
    points += 1000000000000000000000000000000000000000
elif movie == "Star Trek":
    pg.alert ("That's what I hate about you. That's what I hate about you.")
    wb.open ("https://www.youtube.com/watch?v=hdjL8WXjlGI")
    points -= 1000000000000000000000000000000000000000000
elif movie == "Jaws":
    pg.alert ("Do I want people to fear me or love me? Both. I want people to be afraid of how much they love me.")
elif movie == "Frozen":
    pg.alert ("Now I know why Michael hated you so much")
    points -= 10000
elif movie == "Cars":
    pg.alert ("31! That's the new record!")
    wb.open ("https://www.youtube.com/watch?v=TohrGuod-H0")
elif movie == "Threat Level Midnight":
    pg.alert ("It's Michael Scarn")
    wb.open ("https://www.youtube.com/watch?v=FApPcYaVtx0")
    points += 100000000000000000000000000000000000000
else:
    pg.alert ("Do you know anything about film?")

pg.alert("You scored: " + str(points))
