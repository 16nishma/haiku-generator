#Haiku generator
five_syllable_line=["There was a big dog","My cat wanted food","Birds flew in the sky",
"Flowers are pretty","Leaves blew in the wind","It was time to go"]
five_syllable_line2=["I saw a pig fly", "She wanted pizza","The drive was not fast",
"My phone rang 5 times"]
sev_syllable_line=["I ran 5 miles today","And I needed a burger","But I spilled hot, hot coffee",
"My mom said 'do the laundry!'"]
from random import *
rand_five=randint(0,len(five_syllable_line)-1)
rand_five2=randint(0,len(five_syllable_line2)-1)
rand_sev=randint(0,len(sev_syllable_line)-1)
print(five_syllable_line[rand_five])
print(sev_syllable_line[rand_sev])
print(five_syllable_line2[rand_five2])
