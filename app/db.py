import sqlite3
import random

DB_FILE = "database.db"

db = sqlite3.connect(DB_FILE)
c = db.cursor()

# parse data from json
with open('match_data.json') as f:
    file_stuff = f.read()
parsed_data = json.loads(file_stuff)


for match in parsed_data:
    c.execute("CREATE TABLE IF NOT EXISTS matches(MATCH_ID TEXT, \
    GAME_DURATION INTEGER, WIN INTEGER, BLUE_CHAMP_KILLS INTEGER, BLUE_BARON_KILLS INTEGER \
    BLUE_DRAGON_KILLS INTEGER, BLUE_INHIB_KILLS INTEGER, BLUE_TOWER_KILLS INTEGER, \
    BLUE_HERALD_KILLS INTEGER, BLUE_TOWER_KILLS INTEGER, RED_CHAMP_KILLS, RED_BARON_KILLS INTEGER \
    RED_DRAGON_KILLS INTEGER, RED_INHIB_KILLS INTEGER, RED_TOWER_KILLS INTEGER, \
    RED_HERALD_KILLS INTEGER, RED_TOWER_KILLS INTEGER;")

        
    c.execute("CREATE TABLE IF NOT EXISTS participants(MATCH_ID TEXT, PUUID TEXT, \
    ASSISTS INTEGER, BARON_KILLS INTEGER, BOUNTY_LEVEL INTEGER, CHAMP_EXPERIENCE INTEGER, CHAMP_LEVEL INTEGER \
,    CHAMPION_ID INTEGER, CHAMPION_NAME TEXT, consumablesPurchased INTEGER, DAMAGE_DEALT_TO_BUILDINGS INTEGER, DAMAGE_DEALT_TO_OBJECTIVES INTEGER 	
,damageDealtToTurrets INTEGER 	
,damageSelfMitigated INTEGER 	
,deaths INTEGER 
,detectorWardsPlaced INTEGER 	
,doubleKills INTEGER 	
,dragonKills INTEGER 	
,firstBloodAssist INTEGER 	
,firstBloodKill INTEGER 	
,firstTowerAssist INTEGER 	
,firstTowerKill INTEGER 	
,gameEndedInEarlySurrender INTEGER 	
,gameEndedInSurrender INTEGER 	
,goldEarned INTEGER 	
,goldSpent INTEGER 	
,individualPosition STRING 	
,inhibitorKills INTEGER 	
,inhibitorTakedowns INTEGER 	
,inhibitorsLost INTEGER 	
,item0 INTEGER 	
,item1 INTEGER 	
,item2 INTEGER 	
,item3 INTEGER 	
,item4 INTEGER 	
,item5 INTEGER 	
,item6 INTEGER 	
,itemsPurchased INTEGER 	
,killingSprees INTEGER 	
,kills INTEGER 	
,lane STRING 	
,largestCriticalStrike INTEGER 	
,largestKillingSpree INTEGER 	
,largestMultiKill INTEGER 	
,longestTimeSpentLiving INTEGER 	
,magicDamageDealt INTEGER 	
,magicDamageDealtToChampions INTEGER 	
,magicDamageTaken INTEGER 	
,neutralMinionsKilled INTEGER 	
,nexusKills INTEGER 	
,nexusTakedowns INTEGER 	
,nexusLost INTEGER 	
,objectivesStolen INTEGER 	
,objectivesStolenAssists INTEGER 	
,participantId INTEGER 	
,PENTA INTEGER 	
,PERKS PerksDto 	
,PHYS_DMG_DEALT INTEGER 	
,PHYS_DMG_TAKEN INTEGER 	
,PROFILE_ICON INTEGER 	
,PUUID STRING 	
,QUAD_KILLS INTEGER 	
,RIOT_ID_NAME STRING 	
,RIOT_ID_TAGlINE STRING 	
,ROLE STRING 	
,SIGHT_WARDS_BOUGHT INTEGER 	
,SPELL1_CASTS INTEGER 	
,SPELL2_CASTS INTEGER 	
,SPELL3_CASTS INTEGER 	
,SPELL4_CASTS INTEGER 	
,SUMMONER1_CASTS INTEGER 	
,sUMMONER1_ID INTEGER 	
,SUMMONER2_CASTS INTEGER 	
,SUMMONER2_ID INTEGER 	
,SUMMONER_ID STRING 	
,SUMMONDER_LEVEL INTEGER 	
,SUMMONER_NAME STRING 	
,TEAM_EARLY_SURRENDER INTEGER 	
,TEAM_ID INTEGER 	
,TEAM_POSITION STRING
,TIME_CCING_OTHERS INTEGER 	
,TIME_PLAYED INTEGER 	
,TOTAL_DAMAGE_DEALT INTEGER 	
,TOTAL_DAMAGE_DEALT_TO_CHAMPIONS INTEGER 	
,TOTAL_DAMAGE_SHIELDED_ON_TEAMMATES INTEGER 	
,TOTAL_DAMAGE_TAKEN INTEGER 	
,TOTAL_HEAL INTEGER 	
,TOTAL_HEALS_ON_TEAMMATES INTEGER 	
,TOTAL_MINIONS_KILLED INTEGER 	
,TOTAL_TIME_CC_DEALT INTEGER 	
,TOTAL_TIME_SPENT_DEAD INTEGER 	
,TOTAL_UNITS_HEALED INTEGER 	
,TRIPLE_KILLS INTEGER 	
,TRUE_DAMAGE_DEALT INTEGER 	
,TRUE_DAMAGE_DEALT_TO_CHAMPIONS INTEGER 	
,TRUE_DAMAGE_TAKEN INTEGER 	
,TURRET_KILLS INTEGER 	
,TURRET_TAKEDOWNS INTEGER 	
,TURRETS_LOST INTEGER 	
,UNREAL_KILLS INTEGER 	
,VISION_SCORE INTEGER 	
,VISION_WARDS_BOUGHT_IN_GAME INTEGER 	
,WARDS_KILLED INTEGER 	
,WARDS_PLACED INTEGER 	
,WIN INTEGER 
  )")

db.commit()
c.close()

def db_connect():
    global db
    db = sqlite3.connect(DB_FILE)
    return db.cursor()

def db_close():
    db.commit()
    db.close()

# def create_user(username, password):
#     c = db_connect()
#     c.execute('INSERT INTO users(username, password, Did_Questions) VALUES (?, ?, ?);', (username, password, False))
#     c.execute('INSERT INTO grassmeter(Quiz_Grass, Grass, Game_Grass) VALUES (?, ?, ?);', (0, 0, 0))
#     db.commit()
#     #db_close() Dont know what exactly the problem is but dont uncomment this for signup to work