# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# UEFA Euro 1988 Final
#Part 1
#1
Scorer_name1 = "Ruud Gullit"
Scorer_name2 = "Marco van Basten"
#2
goal_0 = 32
goal_1 = 54

#3
scorers = Scorer_name1 + ' ' + str(goal_0) + ',' + ' '+ Scorer_name2 + ' '+ str(goal_1)
#4
report = f'{Scorer_name1} scored in the {goal_0}nd minute\n'f'{Scorer_name2} scored in the {goal_1}th minute'

#Part 2
#1
player = 'Wim Kieft'
#2
first_name = player[:player.find(' ')]
#3
last_name_len = len(player) - player.find(' ') -1
#4
name_short = (player[0] + '.') + player[player.find(' '):]
#5
chant = (len(first_name) * (first_name + "!" + " ")).rstrip()
#6
chant[12]
chant[12]!= ' '
good_chant = chant[12] != ' '
