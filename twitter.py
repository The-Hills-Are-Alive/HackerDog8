from os import replace
from typing import TYPE_CHECKING, Optional
import tweepy
import random


PaVerb =["clapped","slapped","permited", "climbed", "destroyed", "corrupted", "snuck","flipped","flew","beat", "sniffled", "barked", "prowled", "growled", ""]
PrVerb = ["running ^pnoun","walking ^mnoun","permitting ^mnoun","gaming","breaking ^noun"]
Pverb=["slaps","permits","claps","runs","stands","crys","brakes","breaths","eats","creeps","likes ^mnoun","loves ^mnoun"]
Describe=["red","nice", "sad", "hot", "trendy", "wet", "damp", "broken","tasty","unhappy","yellow","green","purple","defiant","different","cute","lucky","victorious","adventureus","obvious","orange","euphoric","exemplary","angry"]
Adverb=["abnormally","absentmindedly","accidentally","actually","adventurously","afterwards","almost","always","annually","anxiously","arrogantly","awkwardly","bashfully","beautifully","bitterly","bleakly","blindly","blissfully","boastfully","boldly","bravely","briefly","brightly","briskly","broadly","busily","calmly","carefully","carelessly","cautiously","certainly","cheerfully","clearly","cleverly","closely","coaxingly","colorfully","commonly","continually","coolly","correctly","courageously","crossly","cruelly","curiously","daily","daintily","dearly","deceivingly","deeply","defiantly","deliberately","delightfully","diligently","dimly","doubtfully","dreamily","easily","elegantly","energetically","enormously","enthusiastically","equally","especially","even","evenly","eventually","exactly","excitedly","extremely","fairly","faithfully","famously","far","fast","fatally","ferociously","fervently","fiercely","fondly","foolishly","fortunately","frankly","frantically","freely","frenetically","frightfully","fully","furiously","generally","generously","gently","gladly","gleefully","gracefully","gratefully","greatly","greedily","happily","hastily","healthily","heavily","helpfully","helplessly","highly","honestly","hopelessly","hourly","hungrily","immediately","innocently","inquisitively","instantly","intensely","intently","interestingly","inwardly","irritably","jaggedly","jealously","jovially","joyfully","joyously","jubilantly","judgmentally","justly","keenly","kiddingly","kindheartedly","kindly","knavishly","knowingly","knowledgeably","kookily","lazily","les","lightly","likely","limply","lively","loftily","longingly","loosely","loudly","lovingly","loyally","madly","majestically","meaningfully","mechanically","merrily","miserably","mockingly","monthly","more","mortally","mostly","mysteriously","naturally","nearly","neatly","nervously","never","nicely","noisily","not","obediently","obnoxiously","oddly","offensively","officially","often","only","openly","optimistically","overconfidently","painfully","partially","patiently","perfectly","physically","playfully","politely","poorly","positively","potentially","powerfully","promptly","properly","punctually","quaintly","queasily","questionably","quicker","quickly","quietly","quirkily","quizzically","randomly","rapidly","rarely","readily","really","reassuringly","recklessly","regularly","reluctantly","repeatedly","reproachfully","restfully","righteously","rigidly","roughly","rudely","safely","scarcely","scarily","searchingly","sedately","seemingly","seldom","selfishly","separately","seriously","shakily","sharply","sheepishly","shrilly","shyly","silently","sleepily","slowly","smoothly","softly","solemnly","solidly","sometimes","soon","speedily","stealthily","sternly","strictly","successfully","suddenly","supposedly","surprisingly","suspiciously","sweetly","swiftly","sympathetically","tenderly","tensely","terribly","thankfully","thoroughly","thoughtfully","tightly","tomorrow","too","tremendously","triumphantly","truly","truthfully","ultimately","unabashedly","unaccountably","unbearably","unethically","unexpectedly","unfortunately","unimpressively","unnaturally","unnecessarily","upbeat","upright","upside-down","upward","urgently","usefully","uselessly","usually","utterly","vacantly","vaguely","vainly","valiantly","vastly","verbally","very","viciously","victoriously","violently","vivaciously","voluntarily","warmly","weakly","wearily","well","wetly","wholly","wildly","willfully","wisely","woefully","wonderfully","worriedly","wrongly","yawningly","yearly","yearningly","yesterday","yieldingly","youthfully","zealously","zestfully","zestily","drippaly"]
Pnoun=["Charlie", "Italy", "Japan", "Da Vinchi", "Harry Potter", "Rock", "him", "her", "them", "it", "i", "^pnoun and ^pnoun", "me", "she", "he","( ͡° ͜ʖ ͡°)"]
Noun=["beef", "girl", "dust", "kettle", "Legend of Zelda","phone", "Bone", "Leash", "burger", "boy", "dice", "love", "destruction", "loyalty", "corruption", "disease","Harry Potter and the Deathly Hallows Part 4 on DVD"]
Sentens=["i like ^noun", "much ^adj", "The best game is The ^noun", "^noun is pretty ^adj", "i like ^noun and ^noun", "you have ^a ^adj ^noun", "^pnoun is ^prverb", "^adv, ^pnoun ^paverb ^pnoun ^adj","^noun is just ^a ^adj ^noun", "i hate it when ^pnoun gets ^paverb", "^noun ^pverb ^adv and ^pnoun ^pverb ^adv","^mnoun ^pverb"] 
Mnoun=[Pnoun,Noun]#master noun


class RandomModule():
    def latername():
        sent=random.choice(Sentens)
        while True:
            sent=sent.replace("^paverb", random.choice(PaVerb),1)
            sent=sent.replace("^prverb", random.choice(PrVerb),1)
            sent=sent.replace("^pverb", random.choice(Pverb),1)
            sent=sent.replace("^adj", random.choice(Describe),1)
            sent=sent.replace("^adv", random.choice(Adverb),1)
            sent=sent.replace("^pnoun", random.choice(Pnoun),1)
            sent=sent.replace("^noun", random.choice(Noun),1)
            sent=sent.replace("^mnoun", random.choice(Mnoun[random.randint(0,1)]),1)
            if not sent.count("^paverb")+sent.count("^prverb")+sent.count("^adj")+sent.count("^adv")+sent.count("^pnoun")+sent.count("^noun")+sent.count("^mnoun")>0:
                while sent.count("^a") != 0:
                    pos=sent.find("^a")+3
                    if sent[pos].strip() in ["a","e","i","o","u"]:
                        sent=sent.replace("^a","an",1)
                    else:
                        sent=sent.replace("^a","a",1)
                    #print(sent)

                return sent



class Twitter():
    def __init__(self):
        auth = tweepy.OAuthHandler("YuzvvrQIgvosXVZ6jahFuTMO6", "IZbVE0LWVq9s0YoQkUpE8v35c0AiYSKCZrlaqJtLp6HR04WqOy")
        auth.set_access_token("1419262253065461763-aYVqg6bMSgc75gcWTCcHdYZ3MWCvR3", "CnikegAGLSZojqzfOeKGVA0tNisOwmAE90kudSnVpWdar")
        self.api = tweepy.API(auth)
        
    def tweet(self, message, media_ids):
        self.api.update_status(message, media_ids=media_ids)

    def do_funny(self, image_fp: Optional[str]): #add shit here img
        msg = RandomModule.latername()
        print(msg)

        # optional attachment
        media_ids = []
        if image_fp is not None:
            media = self.api.media_upload(image_fp)
            media_ids.append(media.media_id)

        self.tweet(msg, media_ids)


if __name__ == "__main__":
    t=Twitter()
    t.do_funny(None)
