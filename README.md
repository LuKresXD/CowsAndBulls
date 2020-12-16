# CowsAndBulls
Cow and bull game project. Implemented in python. (My first project)

Before using, write "pip install zalgo-text" in terminal

How to use:
When you enter the game, you are asked to register, although this is a one-time login. Next, you get a welcome message. Then you can write these commands: rules, account, shop, play. Now let's analyze each of the commands.

Rules) This command simply displays the rules of the game

Account) This command shows: the number of wins, the number of losses, your username, your nickname with your color and the number of points (currency)

Shop) This command will call the shop. In the store you can buy 1) the color of the entire text, 2) the color of your nickname and 3) a secret.
1) You will be given a choice of 6 colors:
  1) BLUE, 500
  2) CYAN, 1000
  3) GREEN, 2000
  4) MAGENTA, 5000
  5) RED, 10000
  6) YELLOW, 20,000
After choosing, provided that you have enough points, you will receive the goods.
2) You will also be given a choice of 6 colors:
  1) BLUE, 1000
  2) CYAN, 2000
  3) GREEN, 4000
  4) MAGENTA, 10000
  5) RED, 20000
  6) YELLOW, 40,000
After choosing, provided that you have enough points, you will receive the goods.
3) You will be written 3 times if you are sure, if you answer “yes” to all three times, then your “secret” will be activated, all the text will be with the “Glitch” effect (This can be turned off, since after the purchase this product changes and Disable secret is written on it. Disabling secret is also for points)

Play) After this command you will need to choose to play online or offline. In short, offline is a normal game with a bot, in which there is a check for a 4-digit number (after an error, it is explained what exactly is wrong), and no rewards are given for this game. Online is actually the same game with a bot, but with online simulation (waiting time, random nickname from 11000 variants with random color, thinking time, timeout, the enemy guesses in 10-30 attempts). Also, after this game, points are awarded (points formula: (your attempts - opponent's attempts) * 500).

Enjoy :)
