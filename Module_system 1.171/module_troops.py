import random

from header_common import *
from header_items import *
from header_troops import *
from header_skills import *
from ID_factions import *
from ID_items import *
from ID_scenes import *

####################################################################################################################
#  Each troop contains the following fields:
#  1) Troop id (string): used for referencing troops in other files. The prefix trp_ is automatically added before each troop-id .
#  2) Troop name (string).
#  3) Plural troop name (string).
#  4) Troop flags (int). See header_troops.py for a list of available flags
#  5) Scene (int) (only applicable to heroes) For example: scn_reyvadin_castle|entry(1) puts troop in reyvadin castle's first entry point
#  6) Reserved (int). Put constant "reserved" or 0.
#  7) Faction (int)
#  8) Inventory (list): Must be a list of items
#  9) Attributes (int): Example usage:
#           str_6|agi_6|int_4|cha_5|level(5)
# 10) Weapon proficiencies (int): Example usage:
#           wp_one_handed(55)|wp_two_handed(90)|wp_polearm(36)|wp_archery(80)|wp_crossbow(24)|wp_throwing(45)
#     The function wp(x) will create random weapon proficiencies close to value x.
#     To make an expert archer with other weapon proficiencies close to 60 you can use something like:
#           wp_archery(160) | wp(60)
# 11) Skills (int): See header_skills.py to see a list of skills. Example:
#           knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2
# 12) Face code (int): You can obtain the face code by pressing ctrl+E in face generator screen
# 13) Face code (int)(2) (only applicable to regular troops, can be omitted for heroes):
#     The game will create random faces between Face code 1 and face code 2 for generated troops
# 14) Troop image (string): If this variable is set, the troop will use an image rather than its 3D visual during the conversations
#  town_1   Sargoth
#  town_2   Tihr
#  town_3   Veluca
#  town_4   Suno
#  town_5   Jelkala
#  town_6   Praven
#  town_7   Uxkhal
#  town_8   Reyvadin
#  town_9   Khudan
#  town_10  Tulga
#  town_11  Curaw
#  town_12  Wercheg
#  town_13  Rivacheg
#  town_14  Halmar
####################################################################################################################

# Some constant and function declarations to be used below... 
# wp_one_handed () | wp_two_handed () | wp_polearm () | wp_archery () | wp_crossbow () | wp_throwing ()
def wp(x):
  n = 0
  r = 10 + int(x / 10)
#  n |= wp_one_handed(x + random.randrange(r))
#  n |= wp_two_handed(x + random.randrange(r))
#  n |= wp_polearm(x + random.randrange(r))
#  n |= wp_archery(x + random.randrange(r))
#  n |= wp_crossbow(x + random.randrange(r))
#  n |= wp_throwing(x + random.randrange(r))
  n |= wp_one_handed(x)
  n |= wp_two_handed(x)
  n |= wp_polearm(x)
  n |= wp_archery(x)
  n |= wp_crossbow(x)
  n |= wp_throwing(x)
  return n

def wpe(m,a,c,t):
   n = 0
   n |= wp_one_handed(m)
   n |= wp_two_handed(m)
   n |= wp_polearm(m)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   return n

def wpex(o,w,p,a,c,t):
   n = 0
   n |= wp_one_handed(o)
   n |= wp_two_handed(w)
   n |= wp_polearm(p)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   return n
   
def wp_melee(x):
  n = 0
  r = 10 + int(x / 10)
#  n |= wp_one_handed(x + random.randrange(r))
#  n |= wp_two_handed(x + random.randrange(r))
#  n |= wp_polearm(x + random.randrange(r))
  n |= wp_one_handed(x + 20)
  n |= wp_two_handed(x)
  n |= wp_polearm(x + 10)
  return n

#Skills
knows_common = knows_riding_1|knows_trade_2|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1
knows_common_multiplayer = knows_trade_10|knows_inventory_management_10|knows_prisoner_management_10|knows_leadership_10|knows_spotting_10|knows_pathfinding_10|knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10
def_attrib = str_7 | agi_5 | int_4 | cha_4
tier_one_attrib = str_15 | agi_12 | int_8 | cha_8
tier_two_attrib = str_21 | agi_19 | int_12 | cha_12
tier_three_attrib = str_29 | agi_25 | int_16 | cha_16
def_attrib_multiplayer = int_30 | cha_30



knows_lord_1 = knows_riding_3|knows_trade_2|knows_inventory_management_2|knows_tactics_4|knows_prisoner_management_4|knows_leadership_7

knows_warrior_npc = knows_weapon_master_2|knows_ironflesh_1|knows_athletics_1|knows_power_strike_2|knows_riding_2|knows_shield_1|knows_inventory_management_2
knows_merchant_npc = knows_riding_2|knows_trade_3|knows_inventory_management_3 #knows persuasion
knows_tracker_npc = knows_weapon_master_1|knows_athletics_2|knows_spotting_2|knows_pathfinding_2|knows_tracking_2|knows_ironflesh_1|knows_inventory_management_2

lord_attrib = str_20|agi_20|int_20|cha_20|level(38)

knight_attrib_1 = str_15|agi_14|int_8|cha_16|level(22)
knight_attrib_2 = str_16|agi_16|int_10|cha_18|level(26)
knight_attrib_3 = str_18|agi_17|int_12|cha_20|level(30)
knight_attrib_4 = str_19|agi_19|int_13|cha_22|level(35)
knight_attrib_5 = str_20|agi_20|int_15|cha_25|level(41)
knight_skills_1 = knows_riding_3|knows_ironflesh_2|knows_power_strike_3|knows_athletics_1|knows_tactics_2|knows_prisoner_management_1|knows_leadership_3
knight_skills_2 = knows_riding_4|knows_ironflesh_3|knows_power_strike_4|knows_athletics_2|knows_tactics_3|knows_prisoner_management_2|knows_leadership_5
knight_skills_3 = knows_riding_5|knows_ironflesh_4|knows_power_strike_5|knows_athletics_3|knows_tactics_4|knows_prisoner_management_2|knows_leadership_6
knight_skills_4 = knows_riding_6|knows_ironflesh_5|knows_power_strike_6|knows_athletics_4|knows_tactics_5|knows_prisoner_management_3|knows_leadership_7
knight_skills_5 = knows_riding_7|knows_ironflesh_6|knows_power_strike_7|knows_athletics_5|knows_tactics_6|knows_prisoner_management_3|knows_leadership_9

#These face codes are generated by the in-game face generator.
#Enable edit mode and press ctrl+E in face generator screen to obtain face codes.


reserved = 0

no_scene = 0

swadian_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
swadian_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
swadian_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
swadian_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
swadian_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

swadian_face_younger_2 = 0x00000000000062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_young_2   = 0x00000003c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_middle_2  = 0x00000007c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_old_2     = 0x0000000bc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_older_2   = 0x0000000fc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000

vaegir_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
vaegir_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
vaegir_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
vaegir_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
vaegir_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

vaegir_face_younger_2 = 0x000000003f00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_young_2   = 0x00000003bf00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_middle_2  = 0x00000007bf00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_old_2     = 0x0000000cbf00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_older_2   = 0x0000000ff100230c4deeffffffffffff00000000001efff90000000000000000

khergit_face_younger_1 = 0x0000000009003109207000000000000000000000001c80470000000000000000
khergit_face_young_1   = 0x00000003c9003109207000000000000000000000001c80470000000000000000
khergit_face_middle_1  = 0x00000007c9003109207000000000000000000000001c80470000000000000000
khergit_face_old_1     = 0x0000000b89003109207000000000000000000000001c80470000000000000000
khergit_face_older_1   = 0x0000000fc9003109207000000000000000000000001c80470000000000000000

khergit_face_younger_2 = 0x000000003f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_young_2   = 0x00000003bf0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_middle_2  = 0x000000077f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_old_2     = 0x0000000b3f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_older_2   = 0x0000000fff0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000

nord_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
nord_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
nord_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
nord_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
nord_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

nord_face_younger_2 = 0x00000000310023084deeffffffffffff00000000001efff90000000000000000
nord_face_young_2   = 0x00000003b10023084deeffffffffffff00000000001efff90000000000000000
nord_face_middle_2  = 0x00000008310023084deeffffffffffff00000000001efff90000000000000000
nord_face_old_2     = 0x0000000c710023084deeffffffffffff00000000001efff90000000000000000
nord_face_older_2   = 0x0000000ff10023084deeffffffffffff00000000001efff90000000000000000

rhodok_face_younger_1 = 0x0000000009002003140000000000000000000000001c80400000000000000000
rhodok_face_young_1   = 0x0000000449002003140000000000000000000000001c80400000000000000000
rhodok_face_middle_1  = 0x0000000849002003140000000000000000000000001c80400000000000000000
rhodok_face_old_1     = 0x0000000cc9002003140000000000000000000000001c80400000000000000000
rhodok_face_older_1   = 0x0000000fc9002003140000000000000000000000001c80400000000000000000

rhodok_face_younger_2 = 0x00000000000062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_young_2   = 0x00000003c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_middle_2  = 0x00000007c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_old_2     = 0x0000000bc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_older_2   = 0x0000000fc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000

man_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
man_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
man_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
man_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
man_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

man_face_younger_2 = 0x000000003f0052064deeffffffffffff00000000001efff90000000000000000
man_face_young_2   = 0x00000003bf0052064deeffffffffffff00000000001efff90000000000000000
man_face_middle_2  = 0x00000007bf0052064deeffffffffffff00000000001efff90000000000000000
man_face_old_2     = 0x0000000bff0052064deeffffffffffff00000000001efff90000000000000000
man_face_older_2   = 0x0000000fff0052064deeffffffffffff00000000001efff90000000000000000

merchant_face_1    = man_face_young_1
merchant_face_2    = man_face_older_2

woman_face_1    = 0x0000000000000001000000000000000000000000001c00000000000000000000
woman_face_2    = 0x00000003bf0030067ff7fbffefff6dff00000000001f6dbf0000000000000000

swadian_woman_face_1 = 0x0000000180102006124925124928924900000000001c92890000000000000000
swadian_woman_face_2 = 0x00000001bf1000061db6d75db6b6dbad00000000001c92890000000000000000

khergit_woman_face_1 = 0x0000000180103006124925124928924900000000001c92890000000000000000
khergit_woman_face_2 = 0x00000001af1030025b6eb6dd6db6dd6d00000000001eedae0000000000000000

refugee_face1 = woman_face_1
refugee_face2 = woman_face_2
girl_face1    = woman_face_1
girl_face2    = woman_face_2

skeleton_face1 = 0x0000000180000000000000000000000000000000000000000000000000000000
skeleton_face2 = 0x0000000180000000000000000000000000000000000000000000000000000000

mercenary_face_1 = 0x0000000000000000000000000000000000000000001c00000000000000000000
mercenary_face_2 = 0x0000000cff00730b6db6db6db7fbffff00000000001efffe0000000000000000

vaegir_face1  = vaegir_face_young_1
vaegir_face2  = vaegir_face_older_2

bandit_face1  = man_face_young_1
bandit_face2  = man_face_older_2

undead_face1  = 0x00000000002000000000000000000000
undead_face2  = 0x000000000020010000001fffffffffff

#NAMES:
#

tf_guarantee_all = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_ranged
tf_guarantee_all_wo_ranged = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield


troops = [
  ["player","Player","Player",tf_hero|tf_unmoveable_in_party_window,no_scene,reserved,fac_player_faction,
   [],
   str_4|agi_4|int_4|cha_4,wp(15),0,0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["multiplayer_profile_troop_male","multiplayer_profile_troop_male","multiplayer_profile_troop_male", tf_hero|tf_guarantee_all, 0, 0,fac_commoners,
   [itm_leather_jerkin, itm_leather_boots],
   0, 0, 0, 0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["multiplayer_profile_troop_female","multiplayer_profile_troop_female","multiplayer_profile_troop_female", tf_hero|tf_female|tf_guarantee_all, 0, 0,fac_commoners,
   [itm_tribal_warrior_outfit, itm_leather_boots],
   0, 0, 0, 0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["temp_troop","Temp Troop","Temp Troop",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
##  ["game","Game","Game",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],
##  ["unarmed_troop","Unarmed Troop","Unarmed Troops",tf_hero,no_scene,reserved,fac_commoners,[itm_arrows,itm_short_bow],def_attrib|str_14,0,knows_common|knows_power_draw_2,0],

####################################################################################################################
# Troops before this point are hardwired into the game and their order should not be changed!
####################################################################################################################
  ["find_item_cheat","find_item_cheat","find_item_cheat",tf_hero|tf_is_merchant,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
  ["random_town_sequence","Random Town Sequence","Random Town Sequence",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
  ["tournament_participants","Tournament Participants","Tournament Participants",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
  ["tutorial_maceman","Maceman","Maceman",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_tutorial_club,itm_leather_jerkin,itm_hide_boots],
   str_6|agi_6|level(1),wp(50),knows_common,mercenary_face_1,mercenary_face_2],
  ["tutorial_archer","Archer","Archer",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
   [itm_tutorial_short_bow,itm_tutorial_arrows,itm_linen_tunic,itm_hide_boots],
   str_6|agi_6|level(5),wp(100),knows_common|knows_power_draw_4,mercenary_face_1,mercenary_face_2],
  ["tutorial_swordsman","Swordsman","Swordsman",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_tutorial_sword,itm_leather_vest,itm_hide_boots],
   str_6|agi_6|level(5),wp(80),knows_common,mercenary_face_1,mercenary_face_2],

  ["novice_fighter","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_6|agi_6|level(5),wp(60),knows_common,mercenary_face_1, mercenary_face_2],
  ["regular_fighter","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_8|agi_8|level(11),wp(90),knows_common|knows_ironflesh_1|knows_power_strike_1|knows_athletics_1|knows_riding_1|knows_shield_2,mercenary_face_1, mercenary_face_2],
  ["veteran_fighter","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,0,fac_commoners,
   [itm_hide_boots],
   str_10|agi_10|level(17),wp(110),knows_common|knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2|knows_shield_3,mercenary_face_1, mercenary_face_2],
  ["champion_fighter","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_12|agi_11|level(22),wp(140),knows_common|knows_ironflesh_4|knows_power_strike_3|knows_athletics_3|knows_riding_3|knows_shield_4,mercenary_face_1, mercenary_face_2],

  ["arena_training_fighter_1","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_6|agi_6|level(5),wp(60),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_2","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_7|agi_6|level(7),wp(70),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_3","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_8|agi_7|level(9),wp(80),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_4","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_8|agi_8|level(11),wp(90),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_5","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_9|agi_8|level(13),wp(100),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_6","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_10|agi_9|level(15),wp(110),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_7","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_10|agi_10|level(17),wp(120),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_8","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_11|agi_10|level(19),wp(130),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_9","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_12|agi_11|level(21),wp(140),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_10","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_12|agi_12|level(23),wp(150),knows_common,mercenary_face_1, mercenary_face_2],

  ["cattle","Cattle","Cattle",0,no_scene,reserved,fac_neutral, [], def_attrib|level(1),wp(60),0,mercenary_face_1, mercenary_face_2],


#soldiers:
#This troop is the troop marked as soldiers_begin
  ["farmer","Farmer","Farmers",tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_cleaver,itm_knife,itm_pitch_fork,itm_sickle,itm_club,itm_stones,itm_leather_cap,itm_felt_hat,itm_felt_hat,itm_linen_tunic,itm_coarse_tunic,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_old_2],
  ["townsman","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_cleaver,itm_knife,itm_club,itm_quarter_staff,itm_dagger,itm_stones,itm_leather_cap,itm_linen_tunic,itm_coarse_tunic,itm_leather_apron,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,mercenary_face_1, mercenary_face_2],
  ["watchman","Watchman","Watchmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_bolts,itm_mace_3,itm_mace_3,itm_fighting_pick,itm_sword_medieval_a,itm_spear,itm_hunting_crossbow,itm_light_crossbow,itm_shield_kite_k,itm_aketon_green,itm_shirt_a_padded_new,itm_red_gambeson,itm_cervelliere,itm_m_light_infantry_helmet_d,itm_m_light_infantry_helmet_e,itm_m_leather_boots_a,itm_m_swadia_milita_boots_a,itm_m_swadia_milita_boots_b,itm_m_swadia_leather_boots_a,itm_m_swadia_leather_boots_b,itm_leather_gloves,itm_m_gloves_a],
   def_attrib|level(9),wp(75),knows_common|knows_shield_1,mercenary_face_1, mercenary_face_2],
  ["caravan_guard","Caravan Guard","Caravan Guards",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield,no_scene,0,fac_commoners,
   [itm_fighting_pick,itm_sword_medieval_a,itm_sword_medieval_b,itm_sword_medieval_c_long,itm_sword_medieval_d_long,itm_spear,itm_shield_kite_k,itm_mail_tabard_heraldic,itm_m_light_infantry_helmet_d,itm_m_light_infantry_helmet_e,itm_m_leather_boots_a,itm_m_swadia_milita_boots_a,itm_m_swadia_milita_boots_b,itm_m_swadia_leather_boots_a,itm_m_swadia_leather_boots_b,itm_leather_gloves,itm_m_gloves_a,itm_saddle_horse],
   def_attrib|level(14),wp(85),knows_common|knows_riding_2|knows_ironflesh_1|knows_shield_3,mercenary_face_1, mercenary_face_2],
  ["mercenary_swordsman","Mercenary Swordsman","Mercenary Swordsmen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_scottish_sword,itm_grosse_messer_b,itm_crusader_sword,itm_longsword,itm_english_longsword,itm_german_bastard_sword,itm_shield_kite_k,itm_shield_heater_d,itm_mail_tabard_heraldic,itm_mail_long_surcoat_new_heraldic,itm_mail_short_surcoat_new_heraldic,itm_m_light_infantry_helmet_d,itm_m_light_infantry_helmet_e,itm_m_infantry_helmet_d,itm_m_infantry_helmet_e,itm_m_leather_boots_a,itm_m_swadia_milita_boots_a,itm_m_swadia_milita_boots_b,itm_m_swadia_leather_boots_a,itm_m_swadia_leather_boots_b,itm_leather_gloves,itm_m_gloves_a],
   def_attrib|level(20),wp(100),knows_common|knows_riding_3|knows_ironflesh_3|knows_shield_3|knows_power_strike_3,mercenary_face_1, mercenary_face_2],
  ["hired_blade","Hired Blade","Hired Blades",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_scottish_sword,itm_grosse_messer_b,itm_crusader_sword,itm_longsword,itm_english_longsword,itm_german_bastard_sword,itm_shield_kite_k,itm_shield_heater_d,itm_brigandine_b_heraldic,itm_heraldic_tunic_new,itm_m_knigh_helm_a,itm_m_knigh_helm_b,itm_m_knigh_helm_c,itm_m_knigh_helm_d,itm_m_knigh_helm_e,itm_m_knigh_helm_f,itm_m_leather_boots_a,itm_m_greaves_a,itm_m_greaves_b,itm_m_gloves_a,itm_m_gauntlets_a,itm_m_gauntlets_b],
   def_attrib|level(25),wp(130),knows_common|knows_riding_3|knows_athletics_5|knows_shield_5|knows_power_strike_5|knows_ironflesh_5,mercenary_face_1, mercenary_face_2],
  ["mercenary_crossbowman","Mercenary Crossbowman","Mercenary Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
   [itm_bolts,itm_mace_3,itm_mace_3,itm_fighting_pick,itm_side_sword,itm_longbowman_sword,itm_hunting_crossbow,itm_light_crossbow,itm_shield_kite_k,itm_aketon_green,itm_shirt_a_padded_new,itm_red_gambeson,itm_m_chapel_light_a,itm_m_chapel_light_b,itm_m_chapel_light_c,itm_m_kattle_a,itm_m_leather_boots_a,itm_m_swadia_milita_boots_a,itm_m_swadia_milita_boots_b,itm_m_swadia_leather_boots_a,itm_m_swadia_leather_boots_b,itm_leather_gloves,itm_m_gloves_a],
   def_attrib|level(19),wp_one_handed (90) | wp_two_handed (90) | wp_polearm (90) | wp_archery (90) | wp_crossbow (130) | wp_throwing (90),knows_common|knows_athletics_5|knows_shield_1,mercenary_face_1, mercenary_face_2],
  ["mercenary_horseman","Mercenary Horseman","Mercenary Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_espada_eslavona_b,itm_espada_eslavona_a,itm_lance,itm_shield_heater_d,itm_mail_tabard_heraldic,itm_mail_long_surcoat_new_heraldic,itm_mail_short_surcoat_new_heraldic,itm_m_cavalry_helmet_a,itm_m_cavalry_helmet_b,itm_m_cavalry_helmet_c,itm_m_cavalry_helmet_d,itm_m_cavalry_helmet_e,itm_m_cavalry_helmet_f,itm_m_cavalry_helmet_g,itm_m_leather_boots_a,itm_m_swadia_milita_boots_a,itm_m_swadia_milita_boots_b,itm_m_swadia_leather_boots_a,itm_m_swadia_leather_boots_b,itm_leather_gloves,itm_m_gloves_a,itm_hunter],
   def_attrib|level(20),wp(100),knows_common|knows_riding_4|knows_ironflesh_3|knows_shield_2|knows_power_strike_3,mercenary_face_1, mercenary_face_2],
  ["mercenary_cavalry","Mercenary Cavalry","Mercenary Cavalry",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_crusader_sword,itm_longsword,itm_english_longsword,itm_german_bastard_sword,itm_lance,itm_shield_heater_d,itm_mail_short_surcoat_new_heraldic,itm_heraldic_tunic_new,itm_m_crusader_helm_a,itm_m_crusader_helm_b,itm_m_crusader_helm_c,itm_m_crusader_helm_d,itm_m_crusader_helm_e,itm_m_crusader_helm_f,itm_m_leather_boots_a,itm_m_greaves_a,itm_m_greaves_b,itm_m_gloves_a,itm_m_gauntlets_a,itm_m_gauntlets_b,itm_warhorse,itm_charger],
   def_attrib|level(25),wp(130),knows_common|knows_riding_5|knows_ironflesh_4|knows_shield_5|knows_power_strike_4,mercenary_face_1, mercenary_face_2],

  ["delgay_mercenary","Delgay Mercenary","Delgay Mercenaries",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield,no_scene,0,fac_commoners,
   [itm_mkk_turban_a, itm_mkk_turban_b, itm_mkk_turban_c, itm_mkk_scale_vest_f, itm_mkk_scale_vest_alt_b, itm_mkk_leather_boots_a, itm_mkk_leather_boots_b, itm_mkk_gauntlets_sar_a, itm_mkk_gauntlets_sar_b, itm_maa_camel_rider_shield_a, itm_maa_camel_rider_shield_b, itm_maa_camel_rider_shield_c, itm_maa_camel_rider_shield_d, itm_maa_camel_rider_shield_e, itm_maa_camel_rider_shield_f, itm_sarranid_mace_1, itm_sarranid_axe_a, itm_sarranid_axe_b, itm_falshion_2, itm_falshion_1],
   def_attrib|level(14),wp(85),knows_common|knows_riding_2|knows_ironflesh_1|knows_shield_3,mercenary_face_1, mercenary_face_2],
  ["delgay_mercenary_assasin","Delgay Mercenary Assasin","Delgay Mercenaries Assasin",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield,no_scene,0,fac_commoners,
   [itm_mkk_turban_c, itm_mkk_infantry_armor_b, itm_mkk_infantry_armor_a, itm_mkk_leather_boots_a, itm_mkk_leather_boots_b, itm_mkk_gauntlets_sar_a, itm_mkk_gauntlets_sar_b, itm_maa_camel_rider_shield_a, itm_maa_camel_rider_shield_b, itm_maa_camel_rider_shield_c, itm_maa_camel_rider_shield_d, itm_maa_camel_rider_shield_e, itm_maa_camel_rider_shield_f, itm_falshion_2, itm_falshion_1, itm_throwing_daggers, itm_throwing_daggers],
   def_attrib|agi_25|level(24),wp(150)|wp_throwing(220),knows_common|knows_riding_2|knows_ironflesh_9|knows_power_strike_4|knows_power_throw_10|knows_athletics_10|knows_shield_3,mercenary_face_1, mercenary_face_2],
  ["delgay_mercenary_rajas_killer","Delgay Mercenary Rajas Killer","Delgay Mercenaries Rajas Killers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield,no_scene,0,fac_commoners,
   [itm_ms_helmet_assasin_a, itm_ms_helmet_assasin_a2, itm_mkk_black_scale_a, itm_mkk_black_scale_b, itm_mkk_black_scale_c, itm_mkk_leather_boots_a, itm_mkk_leather_boots_b, itm_mkk_gauntlets_sar_a, itm_mkk_gauntlets_sar_b, itm_maa_camel_rider_shield_a, itm_maa_camel_rider_shield_b, itm_maa_camel_rider_shield_c, itm_maa_camel_rider_shield_d, itm_maa_camel_rider_shield_e, itm_maa_camel_rider_shield_f, itm_falshion_2, itm_falshion_1, itm_throwing_daggers, itm_throwing_daggers],
   def_attrib|agi_30|str_30|level(34),wp(250)|wp_throwing(420),knows_common|knows_riding_2|knows_ironflesh_10|knows_power_strike_8|knows_power_throw_10|knows_athletics_10|knows_shield_3,mercenary_face_1, mercenary_face_2],

  ["mercenaries_end","mercenaries_end","mercenaries_end",0,no_scene,reserved,fac_commoners,
   [],
   def_attrib|level(4),wp(60),knows_common,mercenary_face_1, mercenary_face_2],

# nerpa troops
["nerpa_recruit","Nerpa Recruit","Nerpa Recruits",tf_guarantee_armor|tf_guarantee_boots,0,0,fac_kingdom_7, [itm_m_aketon_a, itm_m_hose_a, itm_m_hose_b, itm_m_hose_c, itm_m_hose_d, itm_m_hose_e, itm_arming_cap, itm_sword_medieval_c_small, itm_mace_2, itm_mace_4, itm_tab_shield_pavise_a], def_attrib|level(4),wp(60),knows_common,swadian_face_younger_1, swadian_face_middle_2],
["nerpa_footman","Nerpa Footman","Nerpa Footmen",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet,0,0,fac_kingdom_7, [itm_m_aketon_b, itm_m_aketon_a, itm_m_hauberk_a, itm_m_hose_a, itm_m_hose_b, itm_m_hose_c, itm_m_hose_d, itm_m_hose_e, itm_m_chapel_light_a, itm_m_chapel_light_b, itm_m_chapel_light_c, itm_m_kattle_a, itm_sword_medieval_c_small, itm_mace_2, itm_mace_4, itm_tab_shield_pavise_a], def_attrib|level(8),wp(90),knows_common,swadian_face_younger_1, swadian_face_middle_2],
["nerpa_soldier","Nerpa Soldier","Nerpa Soldiers",tf_guarantee_all,0,0,fac_kingdom_7, [itm_m_hauberk_a, itm_m_hauberk_b, itm_m_hauberk_c, itm_m_leather_boots_a, itm_m_sallet_light_a, itm_m_sallet_light_b, itm_m_sallet_light_c, itm_sword_medieval_c_small, itm_mace_2, itm_mace_4, itm_tab_shield_pavise_c], def_attrib|level(15),wp(130),knows_common,swadian_face_younger_1, swadian_face_middle_2],

["nerpa_yeoman","Nerpa Yeoman","Nerpa Yeomen",tf_guarantee_all,0,0,fac_kingdom_7, [itm_m_yeomen_a, itm_m_yeomen_b, itm_m_hose_a, itm_m_hose_b, itm_m_hose_c, itm_m_hose_d, itm_m_hose_e, itm_m_sallet_light_a, itm_sword_medieval_c_small, itm_mace_2, itm_mace_4, itm_long_bow, itm_arrows], def_attrib|level(15),wp(130),knows_common|knows_power_draw_3,swadian_face_younger_1, swadian_face_middle_2],
["nerpa_trickshot","Nerpa Trickshot","Nerpa Trickshots",tf_guarantee_all,0,0,fac_kingdom_7, [itm_m_trickshot_a, itm_m_hose_a, itm_m_leather_boots_a, itm_m_sallet_light_a, itm_sword_medieval_c_small, itm_mace_2, itm_mace_4, itm_long_bow, itm_arrows], def_attrib|level(21),wp(190),knows_common|knows_power_draw_6,swadian_face_younger_1, swadian_face_middle_2],

["nerpa_captain","Nerpa Captain","Nerpa Captains",tf_guarantee_all,0,0,fac_kingdom_7, [itm_m_hauberk_a, itm_m_hauberk_b, itm_m_hauberk_c, itm_m_leather_boots_a, itm_m_sallet_light_a, itm_m_sallet_light_b, itm_m_sallet_light_c, itm_sword_medieval_c_small, itm_mace_2, itm_mace_4, itm_tab_shield_pavise_c, itm_leather_gloves], def_attrib|level(21),wp(130),knows_common|knows_ironflesh_2|knows_power_strike_2|knows_athletics_3,swadian_face_younger_1, swadian_face_middle_2],
["nerpa_army_veteran","Nerpa Army Veteran","Nerpa Army Veterans",tf_guarantee_all,0,0,fac_kingdom_7, [itm_m_brigandine_f, itm_m_brigandine_g, itm_m_leather_boots_a, itm_m_sallet_light_a, itm_m_sallet_light_b, itm_m_sallet_light_c, itm_sword_medieval_c_small, itm_awlpike, itm_awlpike_long, itm_tab_shield_pavise_c, itm_m_gloves_a], def_attrib|level(25),wp(180)|wp_polearm(200),knows_common|knows_ironflesh_5|knows_power_strike_5|knows_athletics_3,swadian_face_old_1, swadian_face_old_2],
["nerpa_mounted_veteran","Nerpa Mounted Veteran","Nerpa Mounted Veterans",tf_guarantee_all,0,0,fac_kingdom_7, [itm_m_brigandine_f, itm_m_brigandine_g, itm_m_leather_boots_a, itm_m_sallet_heavy_a, itm_m_sallet_heavy_b, itm_m_sallet_heavy_c, itm_m_sallet_heavy_d, itm_sword_medieval_c_small, itm_awlpike, itm_awlpike_long, itm_steel_shield, itm_m_gloves_a, itm_hunter], def_attrib|level(29),wp(235)|wp_polearm(280),knows_common|knows_ironflesh_5|knows_power_strike_5|knows_athletics_3|knows_riding_5,swadian_face_old_1, swadian_face_old_2],
["nerpa_commader","Nerpa Commander","Nerpa Commanders",tf_guarantee_all,0,0,fac_kingdom_7, [itm_m_brigandine_f, itm_m_brigandine_g, itm_m_greaves_b, itm_m_sallet_heavy_a, itm_m_sallet_heavy_b, itm_m_sallet_heavy_c, itm_m_sallet_heavy_d, itm_sword_medieval_c_small, itm_awlpike, itm_awlpike_long, itm_steel_shield, itm_m_gloves_a, itm_m_gauntlets_a, itm_warhorse], def_attrib|level(35),wp(335)|wp_polearm(400),knows_common|knows_ironflesh_6|knows_power_strike_6|knows_athletics_3|knows_riding_8,swadian_face_old_1, swadian_face_old_2],
["nerpa_black_head","Nerpa Black Head","Nerpa Black Heads",tf_guarantee_all,0,0,fac_kingdom_7, [itm_m_brigandine_a, itm_m_greaves_b, itm_m_greaves_a, itm_m_sallet_black_a, itm_m_sallet_black_b, itm_m_sallet_black_c, itm_m_sallet_black_d, itm_military_cleaver_c, itm_tab_shield_pavise_d, itm_m_gloves_a, itm_m_gauntlets_b, itm_m_gauntlets_a], def_attrib|level(35),wp(400)|wp_one_handed(560),knows_common|knows_ironflesh_10|knows_power_strike_10|knows_athletics_8,swadian_face_old_1, swadian_face_old_2],

["nerpa_ranger","Nerpa Ranger","Nerpa Rangers",tf_guarantee_all,0,0,fac_kingdom_7, [itm_m_hauberk_a, itm_m_hauberk_b, itm_m_hauberk_c, itm_m_leather_boots_a, itm_m_greaves_b, itm_m_chapel_heavy_a, itm_m_chapel_heavy_b, itm_m_chapel_heavy_c, itm_sword_medieval_c_small, itm_war_darts, itm_tab_shield_pavise_c, itm_m_gloves_a], def_attrib|level(21),wp(120)|wp_throwing(145),knows_common|knows_ironflesh_3|knows_power_throw_4|knows_athletics_2,swadian_face_younger_1, swadian_face_middle_2],
["nerpa_master_ranger","Nerpa Master Ranger","Nerpa Master Rangers",tf_guarantee_all,0,0,fac_kingdom_7, [itm_m_hauberk_a, itm_m_brigandine_f, itm_m_brigandine_g, itm_m_leather_boots_a, itm_m_greaves_b, itm_m_chapel_heavy_a, itm_m_chapel_heavy_b, itm_m_chapel_heavy_c, itm_sword_medieval_c_small, itm_throwing_spears, itm_tab_shield_pavise_c, itm_m_gloves_a], def_attrib|level(25),wp(150)|wp_throwing(220),knows_common|knows_ironflesh_5|knows_power_throw_7|knows_athletics_4,swadian_face_old_1, swadian_face_old_2],

# hairako
["hairako_nomad","Hairako Nomad","Hairako Nomads",tf_guarantee_armor|tf_guarantee_boots,0,0,fac_kingdom_8, [itm_mh_armor_cuirass_a, itm_khergit_leather_boots, itm_leather_covered_round_shield, itm_scimitar, itm_mh_helmet_light_a], def_attrib|level(4),wp(60),knows_common,khergit_face_young_1, khergit_face_young_2],
["hairako_footman","Hairako Footman","Hairako Footmans",tf_guarantee_armor|tf_guarantee_boots,0,0,fac_kingdom_8, [itm_mh_armor_leather_a, itm_mh_armor_leather_b, itm_mh_armor_leather_c, itm_khergit_leather_boots, itm_leather_covered_round_shield, itm_sword_khergit_1, itm_mh_helmet_a, itm_mh_helmet_b], def_attrib|level(10),wp(100),knows_common,khergit_face_young_1, khergit_face_young_2],
["hairako_infantry","Hairako Infantry","Hairako Infantries",tf_guarantee_armor|tf_guarantee_boots,0,0,fac_kingdom_8, [itm_mh_armor_chest_a, itm_mh_armor_chest_b, itm_mh_armor_chest_c, itm_khergit_leather_boots, itm_plate_covered_round_shield, itm_mace_1, itm_mh_spear_a, itm_mh_pike_a, itm_mh_pike_b, itm_mh_helmet_c, itm_mh_helmet_d, itm_leather_gloves], def_attrib|level(18),wp(130),knows_common,khergit_face_young_1, khergit_face_young_2],
["hairako_infantry_veteran","Hairako Infantry Veteran","Hairako Infantry Veterans",tf_guarantee_all,0,0,fac_kingdom_8, [itm_mh_armor_lamellar_a, itm_mh_armor_lamellar_b, itm_mh_armor_lamellar_c, itm_khergit_leather_boots, itm_plate_covered_round_shield, itm_mace_1, itm_mh_spear_a, itm_mh_pike_a, itm_mh_pike_b, itm_mh_helmet_c, itm_mh_helmet_d, itm_leather_gloves, itm_m_gloves_a], def_attrib|level(23),wp(195),knows_common|knows_athletics_5|knows_power_strike_4,khergit_face_middle_1, khergit_face_old_2],
["hairako_shaitan","Hairako Shaitan","Hairako Shaitans",tf_guarantee_all,0,0,fac_kingdom_8, [itm_mh_armor_heavy_a, itm_khergit_leather_boots, itm_steel_shield, itm_mh_sword_a, itm_mh_spear_a, itm_mh_pike_a, itm_mh_pike_b, itm_mh_helmet_heavy_a, itm_leather_gloves, itm_m_gloves_a], def_attrib|level(29),wp(260),knows_common|knows_athletics_10|knows_power_strike_9|knows_ironflesh_10,khergit_face_middle_1, khergit_face_old_2],

["hairako_rider","Hairako Rider","Hairako Riders",tf_guarantee_all,0,0,fac_kingdom_8, [itm_mh_armor_chest_a, itm_mh_armor_chest_b, itm_mh_armor_chest_c, itm_khergit_leather_boots, itm_plate_covered_round_shield, itm_sword_khergit_2, itm_mh_spear_a, itm_mh_helmet_e, itm_mh_helmet_f, itm_leather_gloves, itm_steppe_horse], def_attrib|level(18),wp(130),knows_common|knows_riding_2,khergit_face_young_1, khergit_face_young_2],
["hairako_experienced_rider","Hairako Experienced Rider","Hairako Experienced Riders",tf_guarantee_all,0,0,fac_kingdom_8, [itm_mh_armor_mail_a, itm_mh_armor_mail_b, itm_mh_armor_mail_c, itm_khergit_leather_boots, itm_plate_covered_round_shield, itm_sword_khergit_2, itm_mh_spear_a, itm_mh_helmet_j, itm_mh_helmet_g, itm_leather_gloves, itm_mh_horse_e], def_attrib|level(25),wp(190),knows_common|knows_riding_5|knows_ironflesh_4,khergit_face_old_1, khergit_face_old_2],
["hairako_mounted_shaitan","Hairako Mounted Shaitan","Hairako Mounted Shaitans",tf_guarantee_all,0,0,fac_kingdom_8, [itm_mh_armor_heavy_a, itm_khergit_leather_boots, itm_steel_shield, itm_mh_sword_a, itm_mh_spear_a, itm_mh_helmet_heavy_a, itm_m_gloves_a, itm_mh_horse_a, itm_mh_horse_b, itm_mh_horse_c], def_attrib|level(33),wp(290),knows_common|knows_riding_8|knows_ironflesh_10|knows_power_strike_7, khergit_face_old_1, khergit_face_old_2],

["hairako_archer","Hairako Archer","Hairako Archers",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,0,0,fac_kingdom_8, [itm_mh_armor_leather_a, itm_mh_armor_leather_b, itm_mh_armor_leather_c, itm_khergit_leather_boots, itm_leather_covered_round_shield, itm_sword_khergit_1, itm_strong_bow, itm_arrows, itm_mh_helmet_c, itm_mh_helmet_d], def_attrib|level(10),wp(100),knows_common|knows_power_draw_4,khergit_face_young_1, khergit_face_young_2],
["hairako_sniper","Hairako Sniper","Hairako Snipers",tf_guarantee_all,0,0,fac_kingdom_8, [itm_mh_armor_lamellar_a, itm_mh_armor_lamellar_b, itm_mh_armor_lamellar_c, itm_khergit_leather_boots, itm_leather_covered_round_shield, itm_sword_khergit_1, itm_mh_bow_a, itm_barbed_arrows, itm_mh_helmet_k, itm_mh_helmet_l], def_attrib|level(18),wp(130)|wp_archery(190),knows_common|knows_power_draw_6,khergit_face_young_1, khergit_face_young_2],
["hairako_sniper_elite","Hairako Sniper Elite","Hairako Sniper Elites",tf_guarantee_all,0,0,fac_kingdom_8, [itm_mh_armor_mail_a, itm_mh_armor_mail_b, itm_mh_armor_mail_c, itm_khergit_leather_boots, itm_leather_covered_round_shield, itm_sword_khergit_1, itm_mh_bow_a, itm_barbed_arrows, itm_mh_helmet_medium_a, itm_mh_helmet_medium_b], def_attrib|level(25),wp(220)|wp_archery(290),knows_common|knows_power_draw_9|knows_athletics_5|knows_ironflesh_4,khergit_face_old_1, khergit_face_old_2],

# tauria
# TODO: battle priest and spearman/helbardier
["tauria_recruit","Tauria Recruit","Tauria Recruits",tf_guarantee_armor|tf_guarantee_boots,0,0,fac_kingdom_9, [itm_mt_leather_armor_a, itm_m_hose_b, itm_mt_leather_gloves_a, itm_espada_eslavona_a, itm_espada_eslavona_b, itm_tab_shield_heater_a, itm_mt_bascinet_d], def_attrib|level(4),wp(60),knows_common,swadian_face_young_1, swadian_face_young_2],
["tauria_trooper","Tauria Trooper","Tauria Troopers",tf_guarantee_armor|tf_guarantee_boots,0,0,fac_kingdom_9, [itm_mt_leather_armor_a, itm_m_hose_b, itm_side_sword, itm_german_hunting_spear, itm_tab_shield_heater_a, itm_mt_bascinet_b, itm_mt_bascinet_b2, itm_mt_leather_gloves_a], def_attrib|level(8),wp(90),knows_common,swadian_face_young_1, swadian_face_young_2],
["tauria_soldier","Tauria Soldier","Tauria Soldiers",tf_guarantee_all,0,0,fac_kingdom_9, [itm_mt_hearldic_e, itm_mt_hearldic_e2, itm_mt_leather_boots_e, itm_side_sword, itm_english_bill, itm_poleaxe_a, itm_german_hunting_spear, itm_tab_shield_heater_b, itm_mt_bascinet_b, itm_mt_bascinet_b2, itm_mt_leather_gloves_a], def_attrib|level(15),wp(130),knows_common,swadian_face_young_1, swadian_face_young_2],
["tauria_foot_knight","Tauria Foot Knight","Tauria Foot Knights",tf_guarantee_all,0,0,fac_kingdom_9, [itm_mt_hearldic_d, itm_mt_hearldic_d2, itm_mt_mail_boots_a, itm_milanese_sword, itm_poleaxe_a, itm_elegant_poleaxe, itm_tab_shield_heater_b, itm_mt_bascinet_b, itm_mt_bascinet_b2, itm_mt_scale_gloves_a, itm_mt_scale_gloves_b], def_attrib|level(21),wp(170),knows_common,swadian_face_young_1, swadian_face_young_2],
["tauria_sword_master","Tauria Sword Master","Tauria Sword Masters",tf_guarantee_all,0,0,fac_kingdom_9, [itm_mt_hearldic_d, itm_mt_hearldic_d2, itm_mt_greaves_a, itm_longsword, itm_german_bastard_sword, itm_english_longsword, itm_tab_shield_heater_c, itm_mt_bascinet_b, itm_mt_bascinet_b2, itm_mt_gauntlets_a, itm_mt_gauntlets_a2, itm_mt_gauntlets_b], tier_one_attrib|level(26),wp(240),knows_common,swadian_face_young_1, swadian_face_young_2],
["tauria_man_at_arms","Tauria Man-at-Arms","Tauria Men-at-Arms",tf_guarantee_all,0,0,fac_kingdom_9, [itm_mt_heavy_plate_c, itm_mt_greaves_a, itm_longsword, itm_danish_greatsword, itm_german_bastard_sword, itm_english_longsword, itm_tab_shield_heater_d, itm_mt_bascinet_b, itm_mt_bascinet_b2, itm_mt_gauntlets_a, itm_mt_gauntlets_a2, itm_mt_gauntlets_b], tier_three_attrib|level(34),wp(240),knows_common|knows_ironflesh_7|knows_power_strike_7,swadian_face_old_1, swadian_face_old_2],

["tauria_horseman","Tauria Horseman","Tauria Horsemans",tf_guarantee_all,0,0,fac_kingdom_9, [itm_mt_hearldic_c4, itm_mt_mail_boots_a, itm_crusader_sword, itm_tab_shield_heater_cav_a, itm_mt_bascinet_d, itm_mt_scale_gloves_a, itm_mt_scale_gloves_b, itm_light_lance, itm_hunter], def_attrib|level(21),wp(170),knows_common|knows_riding_3,swadian_face_young_1, swadian_face_young_2],
["tauria_knight","Tauria Knight","Tauria Knights",tf_guarantee_all,0,0,fac_kingdom_9, [itm_mt_hearldic_c, itm_mt_hearldic_c2, itm_mt_hearldic_c3, itm_mt_greaves_a, itm_mt_gauntlets_a, itm_mt_gauntlets_a2, itm_crusader_sword, itm_tab_shield_heater_cav_a, itm_mt_full_helm_a, itm_lance, itm_mt_horse_c6, itm_mt_horse_c7, itm_mt_horse_c8, itm_mt_horse_c9, itm_mt_horse_c10], def_attrib|level(26),wp(210),knows_common|knows_riding_5|knows_ironflesh_4,swadian_face_young_1, swadian_face_young_2],
["tauria_noble_knight","Tauria Noble Knight","Tauria Noble Knights",tf_guarantee_all,0,0,fac_kingdom_9, [itm_mt_hearldic_c, itm_mt_hearldic_c2, itm_mt_hearldic_c3, itm_mt_greaves_a, itm_mt_gauntlets_a, itm_mt_gauntlets_a2, itm_crusader_sword, itm_tab_shield_heater_cav_b, itm_mt_knight_helm_a, itm_mt_knight_helm_b, itm_mt_knight_helm_c, itm_great_lance, itm_mt_horse_c11], tier_three_attrib|level(35),wp(300)|wp_melee(70),knows_common|knows_riding_8|knows_ironflesh_10|knows_power_strike_10,swadian_face_old_1, swadian_face_old_2],

["tauria_crossbowman","Tauria Crossbowman","Tauria Crossbowmans",tf_guarantee_all,0,0,fac_kingdom_9, [itm_mt_hearldic_a, itm_mt_hearldic_a2, itm_mt_leather_boots_e, itm_side_sword, itm_mt_siege_helm_b, itm_mt_siege_helm_c, itm_mt_siege_helm_d, itm_tab_shield_heater_b, itm_mt_leather_gloves_a, itm_heavy_crossbow, itm_bolts], def_attrib|level(15),wp(130)|wp_crossbow(60),knows_common,swadian_face_young_1, swadian_face_young_2],
["tauria_siege_crossbowman","Tauria Siege Crossbowman","Tauria Siege Crossbowmans",tf_guarantee_all,0,0,fac_kingdom_9, [itm_mt_hearldic_g, itm_mt_greaves_a, itm_italian_falchion, itm_grosse_messer, itm_mt_siege_helm_b, itm_mt_siege_helm_c, itm_mt_siege_helm_d, itm_tab_shield_heater_c, itm_mt_leather_gloves_a, itm_sniper_crossbow, itm_steel_bolts, itm_mt_gauntlets_b], def_attrib|level(21),wp(180)|wp_crossbow(60),knows_common,swadian_face_middle_1, swadian_face_old_2],

# elen
["elen_forester","Elen Forester","Elen Foresters",tf_guarantee_armor|tf_guarantee_boots,0,0,fac_kingdom_10, [itm_mt_coat_a, itm_mt_wrapping_a, itm_mt_wrapping_a2, itm_mt_leather_gloves_a, itm_milanese_sword, itm_mt_hood_a, itm_mt_hood_a2, itm_mt_hood_a3, itm_mt_hood_a4, itm_hunting_bow, itm_arrows, itm_tab_shield_kite_a, itm_tab_shield_kite_b], def_attrib|level(4),wp(60),knows_common|knows_power_draw_1,swadian_face_young_1, swadian_face_young_2],
["elen_footman","Elen Footman","Elen Footmans",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_10, [itm_mt_leather_armor_b, itm_mt_wrapping_a, itm_mt_wrapping_a2, itm_mt_leather_gloves_a, itm_milanese_sword, itm_mt_hood_a, itm_mt_hood_a2, itm_mt_hood_a3, itm_mt_hood_a4, itm_hunting_bow, itm_arrows, itm_tab_shield_kite_a, itm_tab_shield_kite_b], def_attrib|level(8),wp(90),knows_common|knows_power_draw_2,swadian_face_young_1, swadian_face_young_2],

["elen_fighter","Elen Fighter","Elen Fighters",tf_guarantee_all,0,0,fac_kingdom_10, [itm_mt_special_a, itm_mt_leather_boots_c, itm_m_gloves_a, itm_milanese_sword, itm_glaive_a, itm_glaive_b, itm_partisan, itm_mt_bascinet_c, itm_tab_shield_kite_b], def_attrib|level(15),wp(120),knows_common|knows_ironflesh_2,swadian_face_young_1, swadian_face_young_2],
["elen_light_infantry","Elen Light Infantry","Elen Light Infantries",tf_guarantee_all,0,0,fac_kingdom_10, [itm_mt_special_b, itm_mt_leather_boots_c, itm_m_gloves_a, itm_milanese_sword, itm_glaive_a, itm_glaive_b, itm_partisan, itm_mt_bascinet_c, itm_tab_shield_kite_b], def_attrib|level(19),wp(160),knows_common|knows_ironflesh_2,swadian_face_young_1, swadian_face_young_2],
["elen_heavy_infantry","Elen Heavy Infantry","Elen Heavy Infantries",tf_guarantee_all,0,0,fac_kingdom_10, [itm_mt_special_c, itm_mt_greaves_light_a, itm_mt_gauntlets_a, itm_milanese_sword, itm_glaive_a, itm_glaive_b, itm_partisan, itm_mt_sallet_a, itm_mt_sallet_a2, itm_tab_shield_kite_c], tier_one_attrib|level(25),wp(210),knows_common|knows_ironflesh_5|knows_power_strike_5,swadian_face_young_1, swadian_face_young_2],
["elen_cheif","Elen Cheif","Elen Cheifs",tf_guarantee_all,0,0,fac_kingdom_10, [itm_mt_special_c, itm_mt_greaves_a, itm_mt_gauntlets_a, itm_milanese_sword, itm_heavy_lance, itm_mt_armet_a2, itm_mt_armet_a, itm_tab_shield_kite_c, itm_mt_horse_a, itm_mt_horse_a2], tier_two_attrib|level(29),wp(300),knows_common|knows_ironflesh_9|knows_power_strike_9|knows_riding_8,swadian_face_young_1, swadian_face_young_2],

["elen_archer","Elen Archer","Elen Archers",tf_guarantee_all,0,0,fac_kingdom_10, [itm_mt_leather_armor_b, itm_mt_leather_boots_a, itm_m_gloves_a, itm_milanese_sword, itm_mt_hood_a, itm_mt_hood_a2, itm_mt_hood_a3, itm_tab_shield_kite_b, itm_long_bow, itm_arrows], def_attrib|level(15),wp(120),knows_common|knows_ironflesh_2|knows_power_draw_3,swadian_face_young_1, swadian_face_young_2],
["elen_experienced_archer","Elen Experienced Archer","Elen Experienced Archers",tf_guarantee_all,0,0,fac_kingdom_10, [itm_mt_leather_armor_b, itm_mt_leather_boots_a, itm_m_gloves_a, itm_milanese_sword, itm_mt_hood_a, itm_mt_hood_a2, itm_mt_hood_a3, itm_tab_shield_kite_b, itm_long_bow, itm_bodkin_arrows], def_attrib|level(20),wp(160),knows_common|knows_ironflesh_2|knows_power_draw_4,swadian_face_young_1, swadian_face_young_2],
["elen_sniper","Elen Sniper","Elen Snipers",tf_guarantee_all,0,0,fac_kingdom_10, [itm_mt_leather_armor_c2, itm_mt_leather_armor_c, itm_mt_leather_boots_a, itm_m_gloves_a, itm_milanese_sword, itm_mt_hood_a, itm_mt_hood_a2, itm_mt_hood_a3, itm_tab_shield_kite_b, itm_long_bow, itm_bodkin_arrows], tier_one_attrib|level(27),wp(250)|wp_archery(200),knows_common|knows_ironflesh_2|knows_power_draw_5,swadian_face_young_1, swadian_face_young_2],
["elen_white_hood","Elen White Hood","Elen White Hoods",tf_guarantee_all,0,0,fac_kingdom_10, [itm_mt_leather_armor_c3, itm_m_greaves_b, itm_m_gauntlets_b, itm_mt_hood_a4, itm_war_bow, itm_bodkin_arrows, itm_ms_metal_shield_a, itm_ms_metal_shield_a2, itm_ms_metal_shield_a3, itm_ms_metal_shield_a4, itm_side_sword], tier_three_attrib|level(34),wp(330)|wp_archery(200),knows_common|knows_ironflesh_7|knows_power_draw_10|knows_power_strike_5,swadian_face_old_1, swadian_face_old_2],

# Adid units
# Nomad Scout - Desert Vanguard - Sultanate Vanguard
["adid_nomad_scout","Nomad Scout","Nomad Scouts",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_11, [itm_headcloth,itm_turban,itm_desert_turban,itm_maa_coat_a,itm_maa_coat_a2,itm_wrapping_boots,itm_spiked_club,itm_long_spiked_club,itm_leather_covered_round_shield], def_attrib|level(4),wp(60),knows_common,swadian_face_younger_1, swadian_face_middle_2],
["adid_desert_vanguard","Desert Vanguard","Desert Vanguards",tf_guarantee_all,0,0,fac_kingdom_11, [itm_maa_light_helmet_a,itm_maa_mail_a,itm_maa_mail_b,itm_maa_mail_b2,itm_m_leather_boots_a,itm_scimitar,itm_maa_round_shield_a,itm_maa_round_shield_a2,itm_maa_round_shield_a3,itm_maa_round_shield_a4], def_attrib|level(9),wp(85),knows_common,swadian_face_young_1, swadian_face_middle_2],
["adid_sultanate_vanguard","Sultanate Vanguard","Sultanate Vanguards",tf_guarantee_all,0,0,fac_kingdom_11, [itm_maa_mail_coif_a,itm_maa_mail_coif_a2,itm_maa_mail_coif_a3,itm_maa_mail_a,itm_maa_mail_b,itm_maa_mail_b2,itm_m_leather_boots_a,itm_scimitar_b,itm_maa_shield_a,itm_maa_shield_a2,itm_maa_shield_a3,itm_maa_shield_a4,itm_maa_shield_a5,itm_maa_shield_a6,itm_maa_shield_a7,itm_maa_shield_a8,itm_maa_shield_a9,itm_maa_shield_a10,itm_maa_shield_a11,itm_maa_shield_a12,itm_bamboo_spear], def_attrib|level(15),wp(135),knows_common,swadian_face_young_1, swadian_face_middle_2],

# Sultanate Vanguard - Camel Rider - Sandstalker
["adid_camel_rider","Camel Rider","Camel Riders",tf_guarantee_all,0,0,fac_kingdom_11, [itm_maa_mail_coif_b,itm_maa_mail_a,itm_maa_mail_b,itm_maa_mail_b2,itm_m_leather_boots_a,itm_scimitar_b,itm_maa_camel_rider_shield_a,itm_maa_camel_rider_shield_b,itm_nomad_bow,itm_arrows,itm_maa_camel_light_a,itm_maa_camel_light_b,itm_maa_camel_light_c,itm_maa_camel_light_d], def_attrib|level(21),wp(155)|wp_archery(200),knows_common|knows_riding_5|knows_horse_archery_5,swadian_face_young_1, swadian_face_middle_2],
["adid_sandstalker","Sandstalker","Sandstalkers",tf_guarantee_all,0,0,fac_kingdom_11, [itm_maa_mail_coif_b,itm_maa_scale_a,itm_maa_scale_a2,itm_m_leather_boots_a,itm_sarranid_axe_b,itm_maa_camel_rider_shield_c,itm_maa_camel_rider_shield_d,itm_maa_camel_rider_shield_e,itm_maa_camel_rider_shield_f,itm_strong_bow,itm_barbed_arrows,itm_maa_camel_war_a,itm_maa_camel_war_b,itm_maa_camel_war_c,itm_maa_camel_war_d,itm_m_gloves_a], def_attrib|level(29),wp(255)|wp_archery(340),knows_common|knows_riding_5|knows_horse_archery_8,swadian_face_young_1, swadian_face_middle_2],

# Sultanate Vanguard - Serpent Guard - Oasis Acolyte
["adid_serpent_guard","Serpent Guard","Serpent Guards",tf_guarantee_all,0,0,fac_kingdom_11, [itm_maa_mail_coif_a,itm_maa_mail_coif_a2,itm_maa_mail_coif_a3,itm_maa_mail_coif_b,itm_maa_mail_coif_c,itm_maa_scale_a,itm_maa_scale_a2,itm_m_leather_boots_a,itm_sarranid_mace_1,itm_sarranid_axe_b,itm_sarranid_axe_a,itm_maa_shield_a,itm_maa_shield_a2,itm_maa_shield_a3,itm_maa_shield_a4,itm_maa_shield_a5,itm_maa_shield_a6,itm_maa_shield_a7,itm_maa_shield_a8,itm_maa_shield_a9,itm_maa_shield_a10,itm_maa_shield_a11,itm_maa_shield_a12,itm_m_gloves_a,itm_spear], def_attrib|level(21),wp(135)|wp_polearm(240),knows_common,swadian_face_young_1, swadian_face_middle_2],
["adid_oasis_acolyte","Oasis Acolyte","Oasis Acolytes",tf_guarantee_all,0,0,fac_kingdom_11, [itm_maa_mail_coif_a,itm_maa_mail_coif_a2,itm_maa_mail_coif_a3,itm_maa_mail_coif_b,itm_maa_mail_coif_c,itm_maa_scale_b,itm_m_leather_boots_a,itm_sarranid_mace_1,itm_sarranid_axe_b,itm_sarranid_axe_a,itm_maa_shield_a,itm_maa_shield_a2,itm_maa_shield_a3,itm_maa_shield_a4,itm_maa_shield_a5,itm_maa_shield_a6,itm_maa_shield_a7,itm_maa_shield_a8,itm_maa_shield_a9,itm_maa_shield_a10,itm_maa_shield_a11,itm_maa_shield_a12,itm_m_gloves_a,itm_war_spear,itm_throwing_spears], def_attrib|level(25),wp(195)|wp_polearm(260),knows_common|knows_ironflesh_4|knows_power_throw_4,swadian_face_young_1, swadian_face_middle_2],

# Oasis Acolyte - Oasis Priest - Oasis High Priest
["adid_oasis_priest","Oasis Priest","Oasis Priests",tf_guarantee_all,0,0,fac_kingdom_11, [itm_maa_mail_coif_a,itm_maa_mail_coif_a2,itm_maa_mail_coif_a3,itm_maa_mail_coif_b,itm_maa_mail_coif_c,itm_maa_heavy_scale_a,itm_m_greaves_a,itm_m_greaves_b,itm_sarranid_mace_1,itm_sarranid_axe_b,itm_sarranid_axe_a,itm_maa_shield_a,itm_maa_shield_a2,itm_maa_shield_a3,itm_maa_shield_a4,itm_maa_shield_a5,itm_maa_shield_a6,itm_maa_shield_a7,itm_maa_shield_a8,itm_maa_shield_a9,itm_maa_shield_a10,itm_maa_shield_a11,itm_maa_shield_a12,itm_m_gloves_a,itm_throwing_spears], def_attrib|str_24|agi_20|level(29),wp(260),knows_common|knows_ironflesh_9|knows_power_strike_5|knows_athletics_6,swadian_face_young_1, swadian_face_middle_2],
["adid_oasis_high_priest","Oasis High Priest","Oasis High Priests",tf_guarantee_all,0,0,fac_kingdom_11, [itm_maa_cavalry_a,itm_maa_heavy_scale_a,itm_m_greaves_a,itm_m_greaves_b,itm_polehammer,itm_m_gauntlets_a,itm_m_gauntlets_b,itm_throwing_spears], def_attrib|str_27|agi_23|level(33),wp(300),knows_common|knows_ironflesh_10|knows_power_strike_10|knows_athletics_6,swadian_face_young_1, swadian_face_middle_2],

# Oasis Acolyte - Royal Lancer - Golden Falcon
["adid_royal_lancer","Royal Lancer","Royal Lancers",tf_guarantee_all,0,0,fac_kingdom_11, [itm_maa_cavalry_a,itm_maa_cavalry_b,itm_maa_cavalry_c,itm_maa_cavalry_c2,itm_maa_scale_b,itm_m_greaves_a,itm_m_greaves_b,itm_sarranid_mace_1,itm_sarranid_axe_b,itm_sarranid_axe_a,itm_maa_round_shield_a,itm_maa_round_shield_a2,itm_maa_round_shield_a3,itm_maa_round_shield_a4,itm_m_gauntlets_a,itm_m_gauntlets_b,itm_lance,itm_arabian_horse_a,itm_arabian_horse_b], def_attrib|str_24|agi_20|level(29),wp(260),knows_common|knows_ironflesh_9|knows_power_strike_5|knows_riding_6,swadian_face_young_1, swadian_face_middle_2],
["adid_golden_falcon","Golden Falcon","Golden Falcons",tf_guarantee_all,0,0,fac_kingdom_11, [itm_maa_cavalry_a,itm_maa_cavalry_b,itm_maa_cavalry_c,itm_maa_cavalry_c2,itm_ms_armor_mamluke,itm_m_greaves_a,itm_m_greaves_b,itm_sarranid_mace_1,itm_sarranid_axe_b,itm_sarranid_axe_a,itm_maa_round_shield_a,itm_maa_round_shield_a2,itm_maa_round_shield_a3,itm_maa_round_shield_a4,itm_m_gauntlets_a,itm_m_gauntlets_b,itm_lance,itm_warhorse_sarranid], def_attrib|str_27|agi_23|level(33),wp(320),knows_common|knows_ironflesh_10|knows_power_strike_7|knows_riding_8,swadian_face_young_1, swadian_face_middle_2],

# Stormguard units
# Mountaineer - Thunderguard - Stormbringers - Avalanche Warriors
["stormguard_mountaineer","Stormguard Mountaineer","Stormguard Mountaineers",tf_guarantee_all,0,0,fac_kingdom_12, [itm_pilgrim_hood,itm_ms_gambeson_a,itm_ms_gambeson_b,itm_ms_gambeson_c,itm_wrapping_boots,itm_leather_gloves,itm_hatchet,itm_wooden_shield,itm_boar_spear], def_attrib|level(4),wp(60),knows_common,swadian_face_younger_1, swadian_face_middle_2],
["stormguard_thunderguard","Stormguard Thunderguard","Stormguard Thunderguards",tf_guarantee_all,0,0,fac_kingdom_12, [itm_m_light_infantry_helmet_a,itm_m_light_infantry_helmet_b,itm_m_light_infantry_helmet_c,itm_m_light_infantry_helmet_d,itm_m_light_infantry_helmet_e,itm_ms_byrnie_a,itm_m_leather_boots_a,itm_m_swadia_leather_boots_b,itm_m_swadia_leather_boots_a,itm_sword_viking_1,itm_tab_shield_round_b,itm_war_spear,itm_leather_gloves,itm_m_gloves_a], def_attrib|level(9),wp(85),knows_common,swadian_face_young_1, swadian_face_middle_2],
["stormguard_stormbringer","Srormguard Stormbringer","Srormguard Stormbringers",tf_guarantee_all,0,0,fac_kingdom_12, [itm_m_light_capelina_a,itm_m_light_capelina_b,itm_m_light_infantry_helmet_a,itm_m_light_infantry_helmet_b,itm_m_light_infantry_helmet_c,itm_m_light_infantry_helmet_d,itm_m_light_infantry_helmet_e,itm_ms_byrnie_a_light,itm_ms_byrnie_a_plated,itm_ms_byrnie_a_plated_mail,itm_ms_byrnie_a_plated_mail_pelt,itm_ms_byrnie_a_plated_mail_fur,itm_m_leather_boots_a,itm_m_swadia_leather_boots_b,itm_m_swadia_leather_boots_a,itm_one_handed_battle_axe_c,itm_tab_shield_round_c,itm_two_handed_battle_axe_2,itm_leather_gloves,itm_m_gloves_a], def_attrib|level(14),wp(110),knows_common,swadian_face_young_1, swadian_face_middle_2],
["stormguard_avalanche_warrior","Avalanche Warrior","Avalanche Warriors",tf_guarantee_all,0,0,fac_kingdom_12, [itm_m_infantry_helmet_a,itm_m_infantry_helmet_b,itm_m_infantry_helmet_c,itm_m_infantry_helmet_d,itm_m_infantry_helmet_e,itm_ms_byrnie_d,itm_ms_byrnie_d_plated,itm_ms_byrnie_d_plated_cloak,itm_ms_byrnie_d_plated_bevor,itm_ms_byrnie_d_plated_bevor_fur,itm_mt_mail_boots_a,itm_m_gauntlets_a,itm_m_gloves_a,itm_mace_4,itm_shield_heater_d,itm_sword_of_war,itm_throwing_spears], def_attrib|level(19),wp(135),knows_common,swadian_face_young_1, swadian_face_middle_2],

# Avalanche Warriors - Lightning Riders
["stormguard_lightning_rider","Lightning Rider","Lightning Riders",tf_guarantee_all,0,0,fac_kingdom_12, [itm_m_cavalry_helmet_e,itm_m_cavalry_helmet_f,itm_m_greaves_b,itm_m_greaves_a,itm_ms_byrnie_d_heavy,itm_ms_byrnie_d_heavy_plate,itm_m_gloves_a,itm_m_gauntlets_a,itm_m_gauntlets_b,itm_one_handed_battle_axe_c,itm_shield_heater_d,itm_light_lance,itm_throwing_spears,itm_warhorse], tier_two_attrib|level(24),wp(160),knows_common|knows_riding_5,swadian_face_young_1, swadian_face_middle_2],

# Avalanche Warriors - Tempest Sentinels - Elite Stormguard
["stormguard_tempest_sentinel","Tempest Sentinel","Tempest Sentinels",tf_guarantee_all,0,0,fac_kingdom_12, [itm_m_cavalry_helmet_g,itm_ms_mail_shirt_heavy_a,itm_ms_mail_shirt_heavy_b,itm_ms_mail_shirt_heavy_c,itm_m_greaves_b,itm_m_gauntlets_a,itm_m_gauntlets_b,itm_one_handed_battle_axe_c,itm_shield_kite_k,itm_ms_two_h_sword_c, itm_war_axe, itm_shortened_voulge,itm_throwing_spears], def_attrib|level(24),wp(180),knows_common|knows_power_throw_6,swadian_face_young_1, swadian_face_middle_2],
["stormguard_elite_stormguard","Elite Stormguard","Elite Stormguards",tf_guarantee_all,0,0,fac_kingdom_12, [itm_m_crusader_helm_f,itm_ms_mail_shirt_heavy_d,itm_ms_mail_shirt_heavy_e,itm_ms_greaves_a,itm_m_gauntlets_b,itm_sarranid_axe_b,itm_sarranid_axe_a,itm_shield_kite_k,itm_bec_de_corbin_a,itm_bec_de_corbin,itm_simple_poleaxe,itm_heavy_throwing_axes,itm_throwing_spears], tier_three_attrib|level(35),wp(400),knows_common|knows_power_throw_9,swadian_face_young_1, swadian_face_middle_2],



  ["silver_rose_novice","Silver Rose Novice","Silver Rose Novice",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_1,[itm_scythe,itm_hatchet,itm_pitch_fork,itm_stones,itm_pickaxe,itm_tab_shield_heater_a,itm_tab_shield_round_a,itm_m_aketon_silver_rose_a,itm_m_aketon_silver_rose_b,itm_m_leather_silver_rose_b,itm_woolen_cap_new_c,itm_woolen_cap_new_f,itm_m_arming_cap_b,itm_m_hose_d,itm_m_swadia_gloves_a], def_attrib|level(4),wp(60),knows_common,swadian_face_younger_1, swadian_face_middle_2],

#peasant - retainer - footman - man-at-arms -  knight
  ["silver_rose_levy","Silver Rose Levy","Silver Rose Levy",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_1,
   [itm_falshion_1, itm_crusader_sword_a,itm_crusader_sword_b,itm_crusader_sword_c,itm_swadia_oval_shield_1,itm_swadia_oval_shield_2,itm_m_swadia_recruit_a,itm_m_arming_cap_b,itm_leather_boots,itm_m_spiked_helmet_a,itm_footman_helmet,itm_silver_rose_footman_helmet,itm_leather_gloves],
   def_attrib|level(5),wp(65),knows_common,swadian_face_younger_1, swadian_face_middle_2],

  ["silver_rose_scout","Silver Rose Scout","Silver Rose Scouts",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_1,
   [itm_crusader_sword_a,itm_crusader_sword_b,itm_crusader_sword_c,itm_swadia_oval_shield_1,itm_swadia_oval_shield_2,itm_m_swadia_recruit_a,itm_leather_boots,itm_silver_rose_scout_helmet_a,itm_leather_gloves,itm_m_swadia_light_horse_a], def_attrib|level(9),wp(87),knows_common|knows_riding_3,swadian_face_young_1, swadian_face_old_2],

  ["silver_rose_milita","Silver Rose Militia","Silver Rose Militia",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_crusader_sword_a,itm_crusader_sword_b,itm_crusader_sword_c,itm_crusader_spear_inf_a,itm_crusader_spear_inf_b,itm_crusader_spear_inf_c,itm_swadia_oval_shield_1,itm_swadia_oval_shield_2,itm_m_swadia_recruit_plated_a,itm_m_swadia_recruit_plated_b,itm_m_swadia_recruit_plated_c,itm_leather_boots,itm_silver_rose_spiked_helmet_a,itm_silver_rose_spiked_helmet_b,itm_spiked_helmet,itm_silver_rose_footman_helmet,itm_leather_gloves, itm_m_gloves_a], def_attrib|level(9),wp(87),knows_common,swadian_face_young_1, swadian_face_old_2],
  ["silver_rose_footman","Silver Rose Footman","Silver Rose Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_crusader_long_sword_a,itm_shortened_bill,itm_winged_mace,itm_flanged_mace,itm_crusader_spear_inf_a,itm_swadia_footman_shield_1,itm_swadia_footman_shield_2,itm_m_silver_rose_mail_a,itm_m_silver_rose_mail_b,itm_leather_boots,itm_silver_rose_spiked_helmet_a,itm_silver_rose_spiked_helmet_b,itm_spiked_helmet,itm_silver_rose_footman_helmet_cloth,itm_silver_rose_footman_helmet,itm_silver_rose_mask,itm_leather_gloves, itm_m_gloves_a],
   def_attrib|level(14),wp_melee(98),knows_common|knows_ironflesh_3|knows_shield_2|knows_athletics_2|knows_power_strike_2,swadian_face_young_1, swadian_face_old_2],
  ["silver_rose_hacker","Silver Rose Hacker","Silver Rose Hackers",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1, [itm_shortened_bill,itm_m_mace_knight,itm_swadia_footman_shield_1,itm_swadia_footman_shield_2,itm_m_silver_rose_breastplate_heavy_a,itm_leather_boots,itm_silver_rose_mask,itm_m_infantry_coif_a,itm_silver_rose_mask_mail,itm_leather_gloves, itm_m_gloves_a], def_attrib|str_22|agi_25|level(25),wp_melee(235),knows_common|knows_ironflesh_5|knows_power_strike_4|knows_athletics_5,swadian_face_middle_1, swadian_face_old_2],
  ["silver_rose_infantry","Silver Rose Infantry","Silver Rose Infantry",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_pike,itm_fighting_pick,itm_bastard_sword_a,itm_sword_medieval_a,itm_sword_medieval_b_small,itm_swadia_footman_shield_1,itm_swadia_footman_shield_2,itm_swadia_footman_shield_3,itm_swadia_footman_shield_4, itm_m_silver_rose_brigandine_a,itm_silver_rose_mask_mail,itm_m_silver_rose_brigandine_b,itm_leather_boots,itm_m_leather_boots_a,itm_m_greaves_a,itm_m_swadia_mail_gloves_a,itm_m_gloves_a],
   def_attrib|level(21),wp_melee(179),knows_common|knows_riding_3|knows_ironflesh_4|knows_power_strike_3|knows_shield_3|knows_athletics_3,swadian_face_middle_1, swadian_face_old_2],
  ["silver_rose_sergeant","Silver Rose Sergeant","Silver Rose Sergeants",tf_mounted|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_axe_crusader_a,itm_axe_crusader_b,itm_crusader_long_sword_c,itm_crusader_long_sword_b,itm_crusader_spear_inf_a,itm_swadia_footman_shield_1,itm_swadia_footman_shield_2,itm_swadia_footman_shield_3,itm_swadia_footman_shield_4,
    itm_m_sergant_helmet_a,itm_m_silver_rose_breastplate_heavy_a,itm_m_silver_rose_breastplate_heavy_b,itm_m_greaves_a,itm_m_greaves_b,itm_m_gloves_a,itm_m_gauntlets_a],
   def_attrib|str_30|agi_20|level(25),wp_melee(278),knows_common|knows_shield_4|knows_ironflesh_4|knows_power_strike_4|knows_athletics_4,swadian_face_middle_1, swadian_face_older_2],
  ["silver_rose_crossbowman","Silver Rose Crossbowman","Silver Rose Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_bolts,itm_light_crossbow,itm_hunting_crossbow,itm_shortened_bill,itm_winged_mace,itm_flanged_mace,itm_swadia_oval_shield_1,itm_swadia_oval_shield_2,itm_m_silver_rose_gambeson_a,itm_m_arming_cap_b,itm_m_hose_d],
   def_attrib|level(14),wp(80),knows_common|knows_riding_2|knows_ironflesh_1,swadian_face_young_1, swadian_face_middle_2],
  ["silver_rose_trained_crossbowman","Silver Rose Trained Crossbowman","Silver Rose Trained Crossbowmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_1,
   [itm_bolts,itm_crossbow,itm_light_crossbow,itm_shortened_bill,itm_winged_mace,itm_flanged_mace,itm_crusader_sword_a,itm_crusader_sword_b,itm_crusader_sword_c,itm_swadia_oval_shield_1,itm_swadia_oval_shield_2,itm_m_silver_rose_gambeson_a,itm_silver_rose_capelina_a,itm_silver_rose_capelina_b,itm_m_hose_d, itm_leather_boots, itm_leather_gloves],
   def_attrib|level(19),wp_one_handed (90) | wp_two_handed (90) | wp_polearm (90) | wp_archery (90) | wp_crossbow (100) | wp_throwing (90),knows_common|knows_riding_2|knows_ironflesh_1|knows_athletics_1,swadian_face_young_1, swadian_face_old_2],
  ["silver_rose_sharpshooter","Silver Rose Sharpshooter","Silver Rose Sharpshooters",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_bolts,itm_crossbow,itm_crossbow,itm_heavy_crossbow,itm_shortened_bill,itm_m_mace_knight,itm_axe_crusader_1,itm_winged_mace,itm_flanged_mace,itm_crusader_sword_a,itm_crusader_sword_b,itm_crusader_sword_c,itm_swadia_oval_shield_1,itm_swadia_oval_shield_2,itm_m_silver_rose_breastplate_a,itm_silver_rose_capelina_mail_a,itm_silver_rose_capelina_mail_b,itm_m_hose_d, itm_leather_boots, itm_leather_gloves, itm_m_gloves_a],
   str_14 | agi_10 | int_4 | cha_4|level(24),wp_one_handed (100) | wp_two_handed (100) | wp_polearm (100) | wp_archery (100) | wp_crossbow (120) | wp_throwing (100),knows_common|knows_power_draw_3|knows_ironflesh_1|knows_power_strike_1|knows_athletics_2,swadian_face_middle_1, swadian_face_older_2],

  ["silver_rose_horseman","Silver Rose Horseman","Silver Rose Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_1,[itm_morningstar,itm_swadia_oval_shield_1,itm_swadia_oval_shield_2,itm_m_silver_rose_breastplate_a,itm_m_leather_boots_a,itm_m_cavalry_helmet_a,itm_m_cavalry_helmet_b,itm_m_cavalry_helmet_c,itm_m_cavalry_helmet_d,itm_m_cavalry_helmet_e,itm_m_cavalry_helmet_f,itm_m_cavalry_helmet_g,itm_m_swadia_light_horse_a,itm_m_swadia_light_horse_b,itm_m_swadia_light_horse_c,itm_m_swadia_light_horse_d,itm_m_swadia_light_horse_e,itm_m_swadia_light_horse_f,itm_m_gloves_a], def_attrib|level(21),wp_melee(150),knows_common|knows_riding_3|knows_ironflesh_4|knows_power_strike_4|knows_shield_3|knows_athletics_3,swadian_face_middle_1, swadian_face_old_2],
  ["silver_rose_man_at_arms","Silver Rose Man at Arms","Silver Rose Men at Arms",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_1,
   [itm_lance,itm_crusader_long_sword_a,itm_crusader_long_sword_b,itm_crusader_long_sword_c,itm_swadia_kite_shield_1,itm_swadia_kite_shield_2,itm_m_silver_rose_brigandine_a,itm_m_silver_rose_brigandine_b,itm_m_silver_rose_breastplate_a,itm_m_crusader_helm_a,itm_m_crusader_helm_b,itm_m_crusader_helm_c,itm_m_crusader_helm_d,itm_m_crusader_helm_e,itm_m_crusader_helm_f,itm_leather_boots,itm_m_gloves_a,itm_m_swadia_light_horse_a,itm_m_swadia_light_horse_b,itm_m_swadia_light_horse_c,itm_m_swadia_light_horse_d,itm_m_swadia_light_horse_e,itm_m_swadia_light_horse_f],
   def_attrib|str_20|agi_20|level(25),wp_melee(179),knows_common|knows_riding_4|knows_ironflesh_5|knows_shield_2|knows_power_strike_5,swadian_face_young_1, swadian_face_old_2],
  ["silver_rose_knight","Silver Rose Knight","Silver Rose Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_1,
   [itm_crusader_knight_spear_a,itm_k_long_sword_a,itm_k_long_sword_b,itm_k_long_sword_c,itm_swadia_heater_shield_1,itm_swadia_heater_shield_2,itm_m_silver_rose_breastplate_heavy_a,itm_m_silver_rose_breastplate_heavy_b,itm_m_knigh_helm_a,itm_m_knigh_helm_b,itm_m_knigh_helm_c,itm_m_knigh_helm_d,itm_m_knigh_helm_e,itm_m_knigh_helm_f,itm_m_swadia_mail_boots_a,itm_m_swadia_mail_boots_b,itm_m_gauntlets_a,itm_m_swadia_heavy_horse_a,itm_m_swadia_heavy_horse_b,itm_m_swadia_heavy_horse_c],
   def_attrib|str_25|agi_25|level(31),wp_one_handed (220) | wp_two_handed (220) | wp_polearm (300) | wp_archery (75) | wp_crossbow (75) | wp_throwing (75),knows_common|knows_riding_5|knows_shield_5|knows_ironflesh_8|knows_power_strike_8,swadian_face_middle_1, swadian_face_older_2],

  ["swadian_young_lion", "Swadian Young Lion", "Swadian Young Lions", tf_guarantee_all,0,0,fac_kingdom_1, [itm_grosse_messer,itm_grosse_messer_b, itm_irish_sword, itm_tab_shield_heater_cav_b,itm_shield_heater_c,itm_shield_heater_d,itm_mace_3,itm_mace_4, itm_m_swadia_elite_recruit_a,itm_m_swadia_elite_recruit_plated_a,itm_m_swadia_elite_recruit_plated_b,itm_m_swadia_elite_recruit_plated_c,itm_m_swadia_elite_recruit_plated_d,itm_m_swadia_elite_helmet_a,itm_m_light_infantry_helmet_e,itm_m_leather_boots_a,itm_m_swadia_leather_boots_a,itm_m_swadia_leather_boots_b,itm_m_gauntlets_a], def_attrib|str_17|agi_11|level(25),wp_melee(160),knows_common|knows_shield_5|knows_ironflesh_5|knows_power_strike_5,swadian_face_middle_1, swadian_face_older_2],
  ["swadian_guild_initiate", "Swadian Guild Initiate", "Swadian Guild Initiates", tf_guarantee_all,0,0,fac_kingdom_1, [itm_grosse_messer_b, itm_crusader_sword, itm_german_bastard_sword, itm_danish_greatsword, itm_longsword, itm_morningstar, itm_shield_heater_d, itm_m_swadia_elite_sergant_plated_a,itm_m_swadia_elite_sergant_plated_b,itm_m_swadia_elite_sergant_plated_c,itm_m_swadia_elite_sergant_plated_d,itm_m_swadia_elite_helmet_b, itm_m_knigh_helm_f,itm_m_swadia_elite_helmet_a,itm_m_leather_boots_a,itm_m_swadia_leather_boots_a,itm_m_swadia_leather_boots_b,itm_m_gauntlets_a,itm_leather_gloves, itm_m_gloves_a], def_attrib|str_18|agi_15|level(28),wp_melee(200),knows_common|knows_shield_7|knows_ironflesh_7|knows_power_strike_5,swadian_face_middle_1, swadian_face_older_2],
  ["swadian_guild_knight", "Swadian Guild Knight", "Swadian Guild Knights", tf_guarantee_all,0,0,fac_kingdom_1, [itm_lance, itm_grosse_messer_b, itm_morningstar, itm_shield_heater_d, itm_m_swadia_elite_knight_armor_a,itm_m_swadia_elite_knight_armor_b,itm_m_swadia_elite_knight_armor_c,itm_m_swadia_elite_helmet_c,itm_m_swadia_mail_boots_a,itm_m_swadia_mail_boots_b,itm_mt_gauntlets_b,itm_m_swadia_elite_horse_a,itm_m_swadia_elite_horse_b,itm_m_swadia_elite_horse_c], def_attrib|str_23|agi_19|level(31),wp_melee(240),knows_common|knows_shield_9|knows_ironflesh_9|knows_power_strike_7|knows_riding_5,swadian_face_middle_1, swadian_face_older_2],
  ["swadian_lionheart", "Swadian Lionheart", "Swadian Lionhearts", tf_guarantee_all,0,0,fac_kingdom_1, [itm_great_lance, itm_grosse_messer_b, itm_morningstar, itm_shield_heater_d, itm_m_swadia_elite_knight_armor_a_cloaked,itm_m_swadia_elite_knight_armor_b_cloaked,itm_m_swadia_elite_knight_armor_c_cloaked,itm_m_swadia_elite_knight_armor_d_cloaked,itm_m_swadia_elite_knight_armor_e_cloaked,itm_m_swadia_elite_knight_armor_f_cloaked,itm_m_swadia_lord_helmet_a,itm_m_swadia_mail_boots_a,itm_m_swadia_mail_boots_b,itm_mt_gauntlets_b,itm_m_swadia_lord_horse_a], def_attrib|str_28|agi_23|level(34),wp_melee(280),knows_common|knows_shield_10|knows_ironflesh_10|knows_power_strike_9|knows_riding_7,swadian_face_middle_1, swadian_face_older_2],

  ["swadian_messenger","Swadian Messenger","Swadian Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_1,
   [itm_sword_medieval_a,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_light_crossbow,itm_bolts],
   str_7 | agi_21 | int_4 | cha_4|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5,swadian_face_young_1, swadian_face_old_2],
  ["swadian_deserter","Swadian Deserter","Swadian Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_bolts,itm_light_crossbow,itm_hunting_crossbow,itm_dagger,itm_club,itm_voulge,itm_wooden_shield,itm_leather_jerkin,itm_padded_cloth,itm_hide_boots,itm_padded_coif,itm_nasal_helmet,itm_footman_helmet],
   def_attrib|level(14),wp(80),knows_common|knows_riding_2|knows_ironflesh_1,swadian_face_young_1, swadian_face_old_2],
  ["swadian_prison_guard","Prison Guard","Prison Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_awlpike,itm_pike,itm_great_sword,itm_morningstar,itm_sword_medieval_b,itm_tab_shield_heater_c,itm_coat_of_plates,itm_plate_armor,itm_plate_boots,itm_guard_helmet,itm_helmet_with_neckguard,itm_bascinet,itm_guard_helmet,itm_leather_gloves],
   def_attrib|level(25),wp(130),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
  ["swadian_castle_guard","Castle Guard","Castle Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_awlpike,itm_pike,itm_great_sword,itm_morningstar,itm_sword_medieval_b,itm_tab_shield_heater_c,itm_tab_shield_heater_d,itm_coat_of_plates,itm_plate_armor,itm_plate_boots,itm_guard_helmet,itm_helmet_with_neckguard,itm_bascinet,itm_guard_helmet,itm_leather_gloves],
   def_attrib|level(25),wp(130),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],

["vaegir_watchman","Vaegir Watchman","Vaegir Watchmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_2, [itm_boar_spear,itm_hatchet,itm_cudgel,itm_boar_spear,itm_shield_kite_g,itm_fur_coat, itm_m_vaegir_rus_shoes, itm_vaegir_fur_cap, itm_vaegir_fur_helmet, itm_vaegir_lamellar_helmet], def_attrib|level(4),wp(60),knows_common, vaegir_face_younger_1, vaegir_face_middle_2],
["vaegir_night_watch","Vaegir Night Watch","Vaegir Night Watch",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_2, [itm_boar_spear,itm_hatchet,itm_cudgel,itm_spear,itm_javelin,itm_shield_kite_g,itm_m_vaegir_padded_a, itm_m_vaegir_rus_shoes, itm_vaegir_fur_cap, itm_vaegir_fur_helmet, itm_vaegir_lamellar_helmet], def_attrib|level(9),wp(110),knows_common, vaegir_face_younger_1, vaegir_face_middle_2],
["vaegir_watch_cheif","Vaegir Watch Chief","Vaegir Watch Chiefs",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2, [itm_spear,itm_one_handed_war_axe_a,itm_one_handed_war_axe_b,itm_javelin,itm_shield_kite_i,itm_m_vaegir_mail_a, itm_m_leather_boots_a, itm_m_gloves_a, itm_m_vaegir_rus_shoes, itm_vaegir_fur_cap, itm_vaegir_fur_helmet, itm_vaegir_lamellar_helmet], def_attrib|level(15),wp(135),knows_common, vaegir_face_younger_1, vaegir_face_middle_2],

# Vaegir watchman?
  ["vaegir_recruit","Vaegir Recruit","Vaegir Recruits",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_2,
   [itm_scimitar,itm_hatchet,itm_cudgel,itm_boar_spear,itm_axe,itm_stones,itm_tab_shield_kite_a,itm_tab_shield_round_a,
    itm_m_vaegir_padded_a, itm_m_vaegir_rus_shoes, itm_vaegir_fur_cap, itm_vaegir_fur_helmet, itm_vaegir_lamellar_helmet],
   def_attrib|level(4),wp(60),knows_common, vaegir_face_younger_1, vaegir_face_middle_2],
  ["vaegir_footman","Vaegir Footman","Vaegir Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_winged_mace,itm_voulge_short,itm_tab_shield_kite_b,itm_m_vaegir_rus_helm,itm_m_vaegir_rus_shoes,itm_m_vaegir_padded_b],
   def_attrib|level(9),wp(75),knows_common, vaegir_face_young_1, vaegir_face_middle_2],
  ["vaegir_skirmisher","Vaegir Skirmisher","Vaegir Skirmishers",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_arrows,itm_one_handed_war_axe_a,itm_hunting_bow,itm_pilgrim_hood,itm_m_vaegir_rus_shoes,itm_m_vaegir_kuyak_a,itm_m_vaegir_kuyak_b,itm_leather_gloves],
   str_10 | agi_5 | int_4 | cha_4|level(14),wp(60),knows_ironflesh_1|knows_power_draw_1|knows_power_throw_1,vaegir_face_young_1, vaegir_face_old_2],
  ["vaegir_archer","Vaegir Archer","Vaegir Archers",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_arrows,itm_one_handed_war_axe_a,itm_strong_bow,itm_m_vaegir_rus_helm,itm_mt_leather_boots_e,itm_m_vaegir_kuyak_c,itm_leather_gloves],
   str_12 | agi_5 | int_4 | cha_4|level(19),wp_one_handed (70) | wp_two_handed (70) | wp_polearm (70) | wp_archery (110) | wp_crossbow (70) | wp_throwing (70),knows_ironflesh_1|knows_power_draw_3|knows_athletics_2|knows_power_throw_1,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_marksman","Vaegir Marksman","Vaegir Marksmen",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_barbed_arrows,itm_one_handed_war_axe_b,itm_war_bow,itm_m_vaegir_tagancha_helm_a,itm_tab_shield_kite_b,itm_m_vaegir_rus_splint_greaves,itm_m_vaegir_kuyak_d,itm_m_gloves_a],
   str_14 | agi_5 | int_4 | cha_4|level(24),wp_one_handed (80) | wp_two_handed (80) | wp_polearm (80) | wp_archery (140) | wp_crossbow (80) | wp_throwing (80),knows_ironflesh_2|knows_power_draw_5|knows_athletics_3|knows_power_throw_1,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_veteran","Vaegir Veteran","Vaegir Veterans",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_one_handed_war_axe_b,itm_tab_shield_kite_c,itm_spear,itm_m_vaegir_gnezdovo_helm_a,itm_m_vaegir_gnezdovo_helm_b,itm_mt_leather_boots_e,itm_m_leather_boots_a,itm_m_vaegir_rus_cav_boots,itm_m_vaegir_rus_lamellar_a,itm_m_vaegir_rus_lamellar_b,itm_leather_gloves,itm_m_gloves_a,itm_mt_scale_gloves_a,itm_mt_scale_gloves_b],
   def_attrib|level(14),wp_melee(85),knows_athletics_2|knows_ironflesh_1|knows_power_strike_2|knows_shield_2,vaegir_face_young_1, vaegir_face_old_2],

  ["vaegir_spearman","Vaegir Spearman","Vaegir Spearmen",tf_guarantee_all,0,0,fac_kingdom_2, [itm_spear,itm_shield_kite_g,itm_m_vaegir_gnezdovo_helm_a,itm_m_vaegir_gnezdovo_helm_b,itm_mt_leather_boots_e,itm_m_vaegir_rus_cav_boots,itm_m_vaegir_mail_a,itm_leather_gloves,itm_m_gloves_a,itm_mt_scale_gloves_a,itm_mt_scale_gloves_b], def_attrib|level(19),wp_melee(100),knows_athletics_5|knows_ironflesh_1|knows_power_strike_2|knows_shield_2,vaegir_face_young_1, vaegir_face_old_2],
  ["vaegir_bardiche_bearer", "Vaegir Bardiche Bearer", "Vaegir Bardiche Bearers", tf_guarantee_all, 0, 0, fac_kingdom_2, [itm_great_long_bardiche, itm_long_bardiche, itm_m_vaegir_nikolskoe_helm, itm_mt_leather_boots_e, itm_m_vaegir_rus_cav_boots, itm_m_vaegir_mail_long_a, itm_leather_gloves, itm_m_gloves_a, itm_mt_scale_gloves_a, itm_mt_scale_gloves_b], def_attrib | level(24), wp_melee(130), knows_athletics_5 | knows_ironflesh_6 | knows_power_strike_2 | knows_shield_2, vaegir_face_young_1, vaegir_face_old_2],

  ["vaegir_infantry","Vaegir Infantry","Vaegir Infantries",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_one_handed_war_axe_b,itm_war_axe,itm_tab_shield_kite_c,itm_spear,itm_m_vaegir_tagancha_helm_b,itm_m_vaegir_rus_splint_greaves,itm_mt_leather_boots_e,itm_m_leather_boots_a,itm_m_vaegir_rus_cav_boots,itm_m_vaegir_rus_lamellar_b,itm_m_vaegir_rus_lamellar_a,itm_leather_gloves,itm_m_gloves_a,itm_mt_scale_gloves_a,itm_mt_scale_gloves_b],
   def_attrib|level(19),wp_melee(100),knows_athletics_3|knows_ironflesh_2|knows_power_strike_3|knows_shield_2,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_guard","Vaegir Guard","Vaegir Guards",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_great_bardiche,itm_sarranid_axe_a,itm_sarranid_axe_b,itm_tab_shield_kite_d,itm_m_vaegir_nikolskoe_helm,itm_m_vaegir_rus_splint_greaves,itm_m_vaegir_rus_scale,itm_mt_scale_gloves_a,itm_mt_scale_gloves_b],
   def_attrib|level(24),wp_melee(130),knows_riding_2|knows_athletics_4|knows_shield_2|knows_ironflesh_3|knows_power_strike_4,vaegir_face_middle_1, vaegir_face_older_2],
  ["vaegir_horseman","Vaegir Horseman","Vaegir Horsemen",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_battle_axe,itm_sword_khergit_2,itm_lance,itm_tab_shield_kite_cav_a,itm_spear,
    itm_m_vaegir_tagancha_helm_b,itm_m_vaegir_rus_splint_greaves,itm_mt_leather_boots_e,itm_m_leather_boots_a,itm_m_vaegir_rus_cav_boots,itm_m_vaegir_rus_lamellar_b,itm_m_vaegir_rus_lamellar_a,itm_leather_gloves,itm_m_gloves_a,itm_mt_scale_gloves_a,itm_northerner_horse],
   def_attrib|level(21),wp(100),knows_riding_3|knows_ironflesh_3|knows_power_strike_3,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_knight","Vaegir Knight","Vaegir Knights",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_bardiche,itm_great_bardiche,itm_war_axe,itm_fighting_axe,itm_lance,itm_tab_shield_kite_cav_b,
    itm_m_vaegir_novogrod_helm,itm_m_vaegir_litchina_helm,itm_m_vaegir_rus_splint_greaves,itm_m_vaegir_rus_scale,itm_mt_scale_gloves_b,itm_mt_scale_gloves_a,itm_northerner_horse_hunter],
   def_attrib|level(26),wp_one_handed (120) | wp_two_handed (140) | wp_polearm (120) | wp_archery (120) | wp_crossbow (120) | wp_throwing (120),knows_riding_4|knows_shield_2|knows_ironflesh_4|knows_power_strike_4,vaegir_face_middle_1, vaegir_face_older_2],

  ["vaegir_gryden","Vaegir Gryden","Vaegir Gryden",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_bardiche,itm_great_bardiche,itm_war_axe,itm_fighting_axe,itm_norman_shield_1, itm_norman_shield_2, itm_norman_shield_3, itm_norman_shield_4, itm_mace_4,
    itm_m_vaegir_novogrod_helm,itm_m_vaegir_litchina_helm,itm_m_vaegir_rus_splint_greaves,itm_m_vaegir_rus_scale,itm_mt_scale_gloves_b,itm_mt_scale_gloves_a],
   def_attrib|str_25|agi_25|level(27),wp_melee(200),knows_athletics_6|knows_shield_2|knows_ironflesh_3|knows_power_strike_4,vaegir_face_middle_1, vaegir_face_older_2],
  ["vaegir_boyar", "Vaegir Boyar", "Vaegir Boyars", tf_guarantee_all,0,0,fac_kingdom_2,
    [itm_bardiche,itm_great_bardiche,itm_war_axe,itm_fighting_axe, itm_norman_shield_1, itm_norman_shield_2, itm_norman_shield_3, itm_norman_shield_4, itm_mace_4,
    itm_m_vaegir_novogrod_helm,itm_m_vaegir_litchina_helm,itm_ms_coat_of_plates_a,itm_m_gauntlets_a, itm_m_greaves_a, itm_m_greaves_b, itm_m_gauntlets_a],
    def_attrib|str_30|agi_30|level(32),wp_melee(300),knows_athletics_9|knows_shield_6|knows_ironflesh_10|knows_power_strike_9,vaegir_face_middle_1, vaegir_face_older_2],

  ["vaegir_zemskyi_boyar", "Vaegir Zemskyi Boyar", "Vaegir Zemskye Boyary", tf_guarantee_all,0,0,fac_kingdom_2,
    [itm_long_bardiche,itm_great_long_bardiche, itm_norman_shield_1, itm_norman_shield_2, itm_norman_shield_3, itm_norman_shield_4, itm_mace_4, itm_mace_3, itm_sarranid_mace_1, itm_sarranid_axe_a,
    itm_m_vaegir_novogrod_helm,itm_ms_coat_of_plates_b,itm_m_gauntlets_a, itm_m_greaves_a, itm_m_greaves_b, itm_m_gauntlets_a],
    tier_three_attrib|str_30|agi_30|level(38),wp_melee(400),knows_athletics_9|knows_shield_6|knows_ironflesh_10|knows_power_strike_9,vaegir_face_middle_1, vaegir_face_older_2],
  ["vaegir_knyazhiy_boyar", "Vaegir Knyazhiy Boyar", "Vaegir Knyazhie Boyary", tf_guarantee_all,0,0,fac_kingdom_2,
    [itm_war_axe,itm_fighting_axe,itm_lance, itm_norman_shield_1, itm_norman_shield_2, itm_norman_shield_3, itm_norman_shield_4, itm_mace_4, itm_strong_bow, itm_barbed_arrows,
    itm_m_vaegir_litchina_helm,itm_ms_coat_of_plates_b,itm_m_gauntlets_a, itm_m_greaves_a, itm_m_greaves_b, itm_m_gauntlets_a, itm_northerner_horse_hunter],
    tier_two_attrib|str_30|agi_30|level(38),wp(350),knows_athletics_9|knows_shield_6|knows_ironflesh_10|knows_power_strike_9,vaegir_face_middle_1, vaegir_face_older_2],  

  ["vaegir_messenger","Vaegir Messenger","Vaegir Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_2,
   [itm_sword_medieval_b,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_short_bow,itm_arrows],
   str_7 | agi_21 | int_4 | cha_4|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_deserter","Vaegir Deserter","Vaegir Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_arrows,itm_spiked_mace,itm_axe,itm_falchion,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_javelin,itm_javelin,itm_steppe_cap,itm_nomad_cap,itm_leather_vest,itm_leather_vest,itm_nomad_armor,itm_nomad_boots],
   str_10 | agi_5 | int_4 | cha_4|level(14),wp(80),knows_ironflesh_1|knows_power_draw_1,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_prison_guard","Prison Guard","Prison Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_ashwood_pike,itm_battle_fork,itm_bardiche,itm_battle_axe,itm_fighting_axe,itm_tab_shield_kite_b,itm_studded_leather_coat,itm_lamellar_armor,itm_mail_chausses,itm_iron_greaves,itm_nordic_helmet,itm_nordic_helmet,itm_nordic_helmet,itm_spiked_helmet,itm_leather_gloves],
   def_attrib|level(24),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,vaegir_face_middle_1, vaegir_face_older_2],
  ["vaegir_castle_guard","Castle Guard","Castle Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_ashwood_pike,itm_battle_fork,itm_bardiche,itm_battle_axe,itm_fighting_axe,itm_tab_shield_kite_d,itm_studded_leather_coat,itm_lamellar_armor,itm_mail_chausses,itm_iron_greaves,itm_nordic_helmet,itm_nordic_helmet,itm_nordic_helmet,itm_spiked_helmet,itm_leather_gloves],
   def_attrib|level(24),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,vaegir_face_middle_1, vaegir_face_older_2],

  ["khergit_slave","Khergit Slave","Khergit Slaves",tf_guarantee_horse,0,0,fac_kingdom_3,[itm_club, itm_wooden_stick, itm_cudgel,itm_stones, itm_wrapping_boots,itm_shirt,itm_burlap_tunic,itm_mt_wrapping_a, itm_mt_wrapping_a2], def_attrib|level(3),wp(30),knows_common,vaegir_face_middle_1, vaegir_face_older_2],
  ["khergit_frontliner","Khergit Frontliner","Khergit Frontliners",tf_guarantee_all|tf_guarantee_armor,0,0,fac_kingdom_3, [itm_mace_1, itm_mace_2, itm_mace_3, itm_mace_4, itm_tab_shield_heater_a, itm_shield_kite_g, itm_shield_kite_i, itm_boar_spear,itm_voulge_short,itm_leather_vest,itm_wrapping_boots, itm_m_leather_boots_a,itm_m_swadia_milita_boots_a,itm_m_swadia_milita_boots_b, itm_m_coif_alternate_c], def_attrib|level(8),wp(80),knows_common|knows_ironflesh_3|knows_power_strike_2|knows_athletics_2,vaegir_face_middle_1, vaegir_face_older_2],
  ["khergit_suicidal","Khergit Suicidal","Khergit Suicidals",tf_guarantee_all|tf_guarantee_armor,0,0,fac_kingdom_3, [itm_mace_1, itm_mace_2, itm_mace_3, itm_mace_4, itm_practice_board_shield, itm_tab_shield_heater_a, itm_shield_kite_g, itm_shield_kite_i, itm_boar_spear, itm_voulge_short, itm_m_leather_boots_a,itm_m_swadia_milita_boots_a, itm_m_swadia_milita_boots_b, itm_m_coif_alternate_c, itm_m_flat_top_a,itm_m_lamellar_armor_west_b, itm_leather_gloves, itm_m_gloves_a], def_attrib|level(15),wp(135),knows_common|knows_ironflesh_5|knows_power_strike_4|knows_athletics_5,vaegir_face_middle_1, vaegir_face_older_2],

  ["khergit_tribesman","Khergit Tribesman","Khergit Tribesmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_3,
   [itm_arrows,itm_club,itm_spear,itm_hunting_bow,
    itm_nomad_cap_b,itm_arena_tunic_d_nomad,itm_nomad_vest_new_a,itm_wrapping_boots],
   def_attrib|level(5),wp(50),knows_common|knows_riding_3|knows_power_draw_2|knows_horse_archery_2,khergit_face_younger_1, khergit_face_old_2],

  # hergit warrior -> khergit sworsman -> khergit veteran -> khergit champion
  ["khergit_warrior","Khergit Warrior","Khergit Warriors",tf_guarantee_all,0,0,fac_kingdom_3, [itm_m_lancer_helmet_light_a, itm_m_lancer_helmet_light_b,itm_m_lamellar_leather_a,itm_m_leather_boots_a, itm_tab_shield_round_a, itm_sword_khergit_1], def_attrib|level(10),wp_one_handed (80) | wp_two_handed (60) | wp_polearm (60) | wp_archery (60) | wp_crossbow (60) | wp_throwing (60),knows_shield_2|knows_ironflesh_4|knows_power_strike_4,khergit_face_younger_1, khergit_face_old_2],
  ["khergit_swordsman","Khergit Swordsman","Khergit Swordsmen",tf_guarantee_all,0,0,fac_kingdom_3, [itm_m_lancer_helmet_midi_a, itm_m_lancer_helmet_midi_b, itm_m_lancer_helmet_midi_c, itm_m_lancer_helmet_midi_d, itm_m_lancer_helmet_midi_e, itm_m_lancer_helmet_midi_f, itm_m_lamellar_leather_b,itm_m_leather_boots_a, itm_tab_shield_small_round_a , itm_sword_khergit_2, itm_leather_gloves], def_attrib|level(15),wp_one_handed (120) | wp_two_handed (60) | wp_polearm (60) | wp_archery (60) | wp_crossbow (60) | wp_throwing (60),knows_shield_3|knows_ironflesh_5|knows_power_strike_5,khergit_face_younger_1, khergit_face_old_2],
  ["khergit_veteran","Khergit Veteran","Khergit Veterans",tf_guarantee_all,0,0,fac_kingdom_3, [itm_m_lancer_helmet_heavy_a,itm_nomad_vest_lamellar,itm_m_greaves_b, itm_tab_shield_small_round_b, itm_sword_khergit_3, itm_m_gauntlets_b], def_attrib|level(20),wp_one_handed (160) | wp_two_handed (60) | wp_polearm (60) | wp_archery (60) | wp_crossbow (60) | wp_throwing (60),knows_shield_4|knows_ironflesh_6|knows_power_strike_6,khergit_face_younger_1, khergit_face_old_2],
  ["khergit_champion","Khergit Champion","Khergit Champions",tf_guarantee_all,0,0,fac_kingdom_3, [itm_m_lancer_helmet_heavy_a,itm_m_lamellar_champion_a,itm_m_greaves_a, itm_strange_sword,itm_m_gauntlets_a, itm_m_buckler_a, itm_m_buckler_b], def_attrib|str_20|agi_25|level(25),wp_one_handed (250) | wp_two_handed (250) | wp_polearm (60) | wp_archery (60) | wp_crossbow (60) | wp_throwing (60),knows_shield_5|knows_ironflesh_9|knows_athletics_8|knows_power_strike_10,khergit_face_younger_1, khergit_face_old_2],

  ["khergit_skirmisher","Khergit Skirmisher","Khergit Skirmishers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3, [itm_arrows,itm_sword_khergit_1,itm_winged_mace,itm_spear,itm_nomad_bow,itm_javelin,itm_tab_shield_small_round_a,itm_m_lancer_helmet_light_a,itm_m_lancer_helmet_light_b,itm_m_lamellar_armor_west_a,itm_m_lamellar_armor_a,itm_m_leather_boots_a, itm_leather_gloves, itm_m_gloves_a,itm_steppe_horse,itm_saddle_horse], def_attrib|level(10),wp_one_handed (60) | wp_two_handed (60) | wp_polearm (60) | wp_archery (80) | wp_crossbow (60) | wp_throwing (80),knows_common|knows_riding_4|knows_power_draw_3|knows_power_throw_1|knows_horse_archery_3,khergit_face_younger_1, khergit_face_old_2],
  ["khergit_horseman","Khergit Horseman","Khergit Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3, [itm_arrows,itm_light_lance,itm_nomad_bow,itm_sword_khergit_2,itm_tab_shield_small_round_a,itm_tab_shield_small_round_b,itm_spear, itm_m_lancer_helmet_midi_a, itm_m_lancer_helmet_midi_b, itm_m_lancer_helmet_midi_c, itm_m_lancer_helmet_midi_d, itm_m_lancer_helmet_midi_e, itm_m_lancer_helmet_midi_f,itm_m_lamellar_armor_west_b,itm_m_lamellar_armor_b,itm_m_leather_boots_a, itm_leather_gloves, itm_m_gloves_a,itm_steppe_horse,itm_hunter], def_attrib|level(14),wp(80),knows_common|knows_riding_5|knows_power_draw_4|knows_ironflesh_2|knows_power_throw_2|knows_horse_archery_3|knows_shield_1,khergit_face_young_1, khergit_face_older_2],
  ["khergit_horse_archer","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_arrows,itm_sword_khergit_2,itm_winged_mace,itm_spear,itm_khergit_bow,itm_tab_shield_small_round_a,itm_tab_shield_small_round_a,itm_tab_shield_small_round_b,itm_bodkin_arrows,itm_arrows,itm_javelin,
    itm_m_lancer_helmet_midi_a, itm_m_lancer_helmet_midi_b, itm_m_lancer_helmet_midi_c, itm_m_lancer_helmet_midi_d, itm_m_lancer_helmet_midi_e, itm_m_lancer_helmet_midi_f,itm_m_lancer_armor_a_long,itm_m_lancer_armor_b_long,itm_m_leather_boots_a, itm_lamellar_gauntlets, itm_scale_gauntlets, itm_leather_gloves, itm_m_gloves_a,itm_tab_shield_small_round_a,itm_tab_shield_small_round_b,itm_steppe_horse],
   def_attrib|level(14),wp_one_handed (80) | wp_two_handed (80) | wp_polearm (80) | wp_archery (110) | wp_crossbow (80) | wp_throwing (110),knows_riding_5|knows_power_draw_3|knows_ironflesh_1|knows_horse_archery_4|knows_power_throw_3,khergit_face_young_1, khergit_face_older_2],
  ["khergit_veteran_horse_archer","Khergit Veteran Horse Archer","Khergit Veteran Horse Archers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_m_dao_a, itm_m_dao_b,itm_winged_mace,itm_spear ,itm_m_rider_arrows,itm_m_rider_bow_a,itm_javelin,itm_tab_shield_small_round_b,itm_tab_shield_small_round_c,
    itm_m_lancer_helmet_midi_a, itm_m_lancer_helmet_midi_b, itm_m_lancer_helmet_midi_c, itm_m_lancer_helmet_midi_d, itm_m_lancer_helmet_midi_e, itm_m_lancer_helmet_midi_f,itm_m_lancer_armor_elite_a_long,itm_m_lancer_armor_elite_b_long,itm_m_leather_boots_a, itm_lamellar_gauntlets, itm_scale_gauntlets, itm_leather_gloves, itm_m_gloves_a,itm_steppe_horse,itm_courser],
   def_attrib|level(21),wp_one_handed (90) | wp_two_handed (90) | wp_polearm (90) | wp_archery (130) | wp_crossbow (90) | wp_throwing (130),knows_riding_7|knows_power_draw_5|knows_ironflesh_3|knows_horse_archery_7|knows_power_throw_4|knows_shield_1,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_lancer","Khergit Lancer","Khergit Lancers",tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac_kingdom_3,
   [itm_sword_khergit_4,itm_spiked_mace,itm_m_impaler_b,itm_m_impaler_a, itm_m_lancer_helmet_midi_a, itm_m_lancer_helmet_midi_b, itm_m_lancer_helmet_midi_c, itm_m_lancer_helmet_midi_d, itm_m_lancer_helmet_midi_e, itm_m_lancer_helmet_midi_f,itm_m_lancer_armor_a,itm_m_lancer_armor_b,itm_m_lancer_armor_c,itm_m_lancer_armor_d,itm_m_lancer_armor_e,itm_m_lancer_armor_f,itm_m_lancer_armor_g,itm_m_leather_boots_a, itm_lamellar_gauntlets, itm_scale_gauntlets, itm_leather_gloves, itm_m_gloves_a,itm_tab_shield_small_round_b,itm_tab_shield_small_round_c,itm_courser,itm_warhorse_steppe,itm_warhorse_steppe,itm_warhorse_steppe],
   def_attrib|level(23),wp_one_handed (110) | wp_two_handed (110) | wp_polearm (150) | wp_archery (110) | wp_crossbow (110) | wp_throwing (110),knows_riding_7|knows_power_strike_4|knows_power_draw_4|knows_power_throw_2|knows_ironflesh_4|knows_horse_archery_1|knows_shield_2,khergit_face_middle_1, khergit_face_older_2],

  ["khergit_khevtuul","Khergit Khevtuul","Khergit Khevtuuls",tf_guarantee_all,0,0,fac_kingdom_3, [itm_strange_sword, itm_practice_board_shield, itm_m_rider_bow_a, itm_m_rider_arrows, itm_m_lancer_helmet_midi_a, itm_m_lancer_helmet_midi_b, itm_m_lancer_helmet_midi_c, itm_m_lancer_helmet_midi_d, itm_m_lancer_helmet_midi_e, itm_m_lancer_helmet_midi_f,itm_m_lancer_armor_elite_a,itm_m_lancer_armor_elite_b,itm_m_lancer_armor_elite_c,itm_m_lancer_armor_elite_d,itm_m_lancer_armor_elite_e,itm_m_lancer_armor_elite_f,itm_m_lancer_armor_elite_g,itm_m_leather_boots_a, itm_lamellar_gauntlets, itm_scale_gauntlets, itm_leather_gloves, itm_m_gloves_a],def_attrib|str_20|agi_25|level(29),wp_one_handed (200) | wp_two_handed (230) | wp_polearm (150) | wp_archery (260) | wp_crossbow (110) | wp_throwing (110),knows_power_strike_9|knows_athletics_7|knows_power_draw_5|knows_ironflesh_7|knows_shield_2,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_kheshig","Khergit Kheshig","Khergit Kheshigs",tf_guarantee_all,0,0,fac_kingdom_3, [itm_strange_sword, itm_practice_board_shield, itm_m_rider_bow_a, itm_m_rider_arrows, itm_m_lancer_heavy_elite_a, itm_m_lancer_helmet_heavy_a, itm_lamellar_gauntlets, itm_scale_gauntlets, itm_m_gloves_a, itm_m_greaves_a, itm_khergit_leather_boots, itm_khergit_guard_boots],def_attrib|str_28|agi_30|level(35),wp_one_handed (300) | wp_two_handed (355) | wp_polearm (150) | wp_archery (400) | wp_crossbow (110) | wp_throwing (110),knows_power_strike_10|knows_power_draw_10|knows_ironflesh_10|knows_athletics_9|knows_shield_4,khergit_face_middle_1, khergit_face_older_2],

  ["khergit_messenger","Khergit Messenger","Khergit Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_3,
   [itm_sword_khergit_2,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_short_bow,itm_arrows],
   str_7 | agi_21 | int_4 | cha_4|level(25),wp(125),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,khergit_face_young_1, khergit_face_older_2],
  ["khergit_deserter","Khergit Deserter","Khergit Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_arrows,itm_spiked_mace,itm_axe,itm_sword_khergit_1,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_javelin,itm_javelin,itm_steppe_cap,itm_nomad_cap_b,itm_khergit_armor,itm_steppe_armor,itm_tribal_warrior_outfit,itm_nomad_boots],
   str_10 | agi_5 | int_4 | cha_4|level(14),wp(80),knows_ironflesh_1|knows_power_draw_1,khergit_face_young_1, khergit_face_older_2],
  ["khergit_prison_guard","Prison Guard","Prison Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_sword_khergit_3,itm_tab_shield_small_round_b,itm_tab_shield_small_round_a,itm_lamellar_vest_khergit,itm_lamellar_armor,itm_khergit_leather_boots,itm_iron_greaves,itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_leather_warrior_cap],
   def_attrib|level(24),wp(130),knows_athletics_5|knows_shield_2|knows_ironflesh_5,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_castle_guard","Castle Guard","Castle Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_sword_khergit_4,itm_tab_shield_small_round_b,itm_tab_shield_small_round_a,itm_lamellar_vest_khergit,itm_lamellar_armor,itm_khergit_leather_boots,itm_iron_greaves,itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_leather_warrior_cap],
   def_attrib|level(24),wp(130),knows_athletics_5|knows_shield_2|knows_ironflesh_5,khergit_face_middle_1, khergit_face_older_2],


  ["nord_recruit","Nord Recruit","Nord Recruits",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_4,
   [itm_axe,itm_voulge_short,itm_nordic_hand_axe_a,itm_nordic_hand_axe_b,itm_nordic_hand_axe_c,itm_nordic_spear_a,itm_spear,itm_tab_shield_round_a,itm_nord_lamellar_a,itm_nord_lamellar_b,itm_nord_lamellar_c,itm_m_swadia_milita_boots_a, itm_m_swadia_milita_boots_a, itm_m_leather_boots_a, itm_ms_conical_helmet_padded_a,itm_ms_spangen_helmet_c,itm_b_h1,itm_b_h1_1, itm_leather_gloves],def_attrib|level(6),wp(50),knows_power_strike_1|knows_power_throw_1|knows_riding_1|knows_athletics_1,nord_face_younger_1, nord_face_old_2],
  ["nord_footman","Nord Footman","Nord Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_4,[itm_fighting_axe,itm_nord_sword_a,itm_nord_sword_b,itm_one_handed_war_axe_a,itm_nordic_spear_a,itm_spear,itm_tab_shield_round_a,itm_tab_shield_round_b,itm_javelin,itm_throwing_axes,itm_ms_ridge_helmet_c,itm_ms_conical_helmet_padded_a,itm_ms_conical_helmet_mail_a,itm_nord_light_a,itm_nord_light_b,itm_nord_light_c,itm_mt_leather_boots_e,itm_leather_gloves, itm_m_gloves_a,itm_b_h1,itm_b_h1_1],def_attrib|level(10),wp(70),knows_ironflesh_2|knows_power_strike_2|knows_power_throw_2|knows_riding_2|knows_athletics_2|knows_shield_1,nord_face_young_1, nord_face_old_2],

  ["nord_trained_footman","Nord Trained Footman","Nord Trained Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_4,[itm_nord_sword_a,itm_nord_sword_b,itm_nord_sword_c,itm_nord_sword_d,itm_one_handed_war_axe_a,itm_one_handed_war_axe_b,itm_one_handed_battle_axe_a,itm_two_handed_axe,itm_two_handed_battle_axe_2,itm_javelin,itm_tab_shield_round_b,itm_ms_pointed_helmet_a,itm_ms_conical_helmet_padded_a,itm_ms_conical_helmet_mail_a,itm_ms_conical_helmet_mail_b,itm_nord_padded_a,itm_nord_padded_b,itm_nord_padded_c,itm_nord_padded_d,itm_nord_padded_lam_a,itm_m_leather_boots_a,itm_m_gloves_a],def_attrib|level(14),wp(100),knows_ironflesh_3|knows_power_strike_3|knows_power_throw_2|knows_riding_2|knows_athletics_3|knows_shield_2,nord_face_young_1, nord_face_old_2],
  ["nord_warrior","Nord Warrior","Nord Warriors",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_4,[itm_nord_sword_a,itm_nord_sword_b,itm_nord_sword_c,itm_nord_sword_d,itm_one_handed_war_axe_b,itm_one_handed_battle_axe_a,itm_two_handed_battle_axe_2,itm_war_spear,itm_tab_shield_round_c,itm_javelin,itm_ms_spangen_helmet_a,itm_ms_spangen_helmet_b,itm_ms_spangen_helmet_c,itm_m_greaves_a, itm_m_greaves_b, itm_m_leather_boots_a, itm_m_swadia_mail_gloves_a, itm_mt_scale_gloves_a, itm_mt_scale_gloves_b, itm_nord_mail_a,itm_nord_mail_b,itm_nord_mail_c],def_attrib|level(19),wp(115),knows_ironflesh_4|knows_power_strike_4|knows_power_throw_3|knows_riding_2|knows_athletics_4|knows_shield_3,nord_face_young_1, nord_face_older_2],
  ["nord_veteran","Nord Veteran","Nord Veterans",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_4,[itm_nord_sword_a,itm_nord_sword_b,itm_nord_sword_c,itm_nord_sword_d,itm_one_handed_battle_axe_b,itm_great_axe,itm_tab_shield_round_d,itm_javelin,itm_throwing_axes,itm_ms_spangen_helmet_a,itm_ms_spangen_helmet_a,itm_ms_conical_helmet_padded_a, itm_nord_plate_a, itm_nord_plate_b, itm_m_greaves_a, itm_m_greaves_b, itm_m_gauntlets_a, itm_m_gauntlets_b], def_attrib|level(24),wp(145),knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_riding_3|knows_athletics_5|knows_shield_4,nord_face_young_1, nord_face_older_2],
  ["nord_guard","Nord Guard","Nord Guards",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_4,[itm_voulge,itm_tab_shield_round_d,itm_throwing_axes,itm_ms_pointed_helmet_a, itm_nord_plate_a, itm_nord_plate_b, itm_m_greaves_a, itm_m_greaves_b, itm_m_gauntlets_a, itm_m_gauntlets_b], def_attrib|level(24),wp(145),knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_riding_3|knows_athletics_5|knows_shield_4,nord_face_young_1, nord_face_older_2],
  ["nord_champion","Nord Huscarl","Nord Huscarls",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_4,[itm_sword_viking_3,itm_sword_viking_3_small,itm_great_axe,itm_one_handed_battle_axe_c,itm_tab_shield_round_e,itm_throwing_spears,itm_heavy_throwing_axes,itm_heavy_throwing_axes,itm_ms_gjermundbu_helm_a,itm_ms_gjermundbu_helm_b,itm_banded_armor,itm_cuir_bouilli_with_pelt,itm_cuir_bouilli,itm_banded_armor_b,itm_banded_armor_c,itm_banded_armor_d,itm_m_greaves_a, itm_m_greaves_b, itm_m_gloves_a, itm_m_gauntlets_a, itm_m_gauntlets_b],def_attrib|level(28),wp(170),knows_ironflesh_7|knows_power_strike_7|knows_power_throw_5|knows_riding_2|knows_athletics_7|knows_shield_6,nord_face_middle_1, nord_face_older_2],
  ["nord_huntsman","Nord Huntsman","Nord Huntsmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_4,[itm_arrows,itm_nordic_hand_axe_a,itm_nordic_hand_axe_b,itm_nordic_hand_axe_c,itm_hunting_bow, itm_nord_lamellar_a,itm_nord_lamellar_b,itm_nord_lamellar_c,itm_nord_light_a,itm_nord_light_b,itm_m_swadia_leather_boots_a, itm_m_swadia_leather_boots_b, itm_ms_conical_helmet_padded_a,itm_ms_spangen_helmet_c],str_10 | agi_5 | int_4 | cha_4|level(11),wp_one_handed (60) | wp_two_handed (60) | wp_polearm (60) | wp_archery (70) | wp_crossbow (60) | wp_throwing (60),knows_ironflesh_1|knows_power_draw_1|knows_athletics_2,nord_face_young_1, nord_face_old_2],
  ["nord_archer","Nord Archer","Nord Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_4,[itm_arrows,itm_nordic_hand_axe_a,itm_nordic_hand_axe_b,itm_nordic_hand_axe_c,itm_short_bow,itm_ms_conical_helmet_padded_a,itm_ms_spangen_helmet_c, itm_b_h1, itm_b_h1_1, itm_m_gloves_a, itm_nord_padded_a, itm_nord_padded_c],str_11 | agi_5 | int_4 | cha_4|level(15),wp_one_handed (80) | wp_two_handed (80) | wp_polearm (80) | wp_archery (95) | wp_crossbow (80) | wp_throwing (80),knows_ironflesh_2|knows_power_draw_3|knows_athletics_5,nord_face_young_1, nord_face_old_2],
  ["nord_tracer","Nord Tracer","Nord Tracers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_4,[itm_barbed_arrows,itm_nord_sword_a,itm_nord_sword_b,itm_nord_sword_c,itm_nord_sword_d,itm_war_bow,itm_h_h2_1, itm_h_h2, itm_m_leather_boots_a, itm_m_gloves_a, itm_nord_archer_a, itm_nord_archer_b,itm_nord_archer_c],str_10 | agi_25 | int_4 | cha_4|level(25),wp_one_handed (80) | wp_two_handed (80) | wp_polearm (80) | wp_archery (160) | wp_crossbow (80) | wp_throwing (80),knows_ironflesh_2|knows_power_draw_6|knows_athletics_10,nord_face_young_1, nord_face_old_2],
  ["nord_veteran_archer","Nord Veteran Archer","Nord Veteran Archers",tf_guarantee_all,0,0,fac_kingdom_4,[itm_bodkin_arrows,itm_nord_sword_a,itm_nord_sword_b,itm_nord_sword_c,itm_nord_sword_d,itm_nordic_hand_axe_a,itm_nordic_hand_axe_b,itm_nordic_hand_axe_c,itm_long_bow,itm_b_h1, itm_b_h1_1,itm_b_h2,itm_b_h2_1, itm_m_gloves_a, itm_ms_conical_helmet_mail_b, itm_ms_conical_helmet_mail_a, itm_ms_conical_helmet_padded_a, itm_nord_padded_a, itm_nord_padded_b, itm_nord_padded_c, itm_nord_padded_d, itm_nord_padded_lam_a],str_12 | agi_5 | int_4 | cha_4|level(19),wp_one_handed (95) | wp_two_handed (95) | wp_polearm (95) | wp_archery (120) | wp_crossbow (95) | wp_throwing (95),knows_power_strike_3|knows_ironflesh_4|knows_power_draw_5|knows_athletics_7,nord_face_middle_1, nord_face_older_2],
  ["nord_messenger","Nord Messenger","Nord Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_4,
   [itm_sword_viking_2,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_short_bow,itm_arrows],
   str_7 | agi_21 | int_4 | cha_4|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,nord_face_young_1, nord_face_older_2],
  ["nord_deserter","Nord Deserter","Nord Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_arrows,itm_spiked_mace,itm_axe,itm_falchion,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_javelin,itm_javelin,itm_steppe_cap,itm_nomad_cap,itm_leather_vest,itm_leather_vest,itm_nomad_armor,itm_nomad_boots],
   str_10 | agi_5 | int_4 | cha_4|level(14),wp(80),knows_ironflesh_1|knows_power_draw_1,nord_face_young_1, nord_face_older_2],
  ["nord_prison_guard","Prison Guard","Prison Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_ashwood_pike,itm_battle_fork,itm_battle_axe,itm_fighting_axe,itm_tab_shield_round_d,itm_mail_hauberk,itm_mail_chausses,itm_iron_greaves,itm_nordic_helmet,itm_nordic_helmet,itm_nordic_helmet,itm_spiked_helmet,itm_leather_gloves],
   def_attrib|level(24),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,nord_face_middle_1, nord_face_older_2],
  ["nord_castle_guard","Castle Guard","Castle Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_ashwood_pike,itm_battle_fork,itm_battle_axe,itm_fighting_axe,itm_tab_shield_round_d,itm_tab_shield_round_e,itm_mail_hauberk,itm_heraldic_mail_with_tabard,itm_mail_chausses,itm_iron_greaves,itm_nordic_helmet,itm_nordic_helmet,itm_nordic_helmet,itm_spiked_helmet,itm_leather_gloves],
   def_attrib|level(24),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,nord_face_middle_1, nord_face_older_2],

  ["rhodok_peasant","Rhodok Peasant","Rhodok Peasants",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_5, [itm_pitch_fork, itm_tab_shield_pavise_a, itm_hatchet, itm_peasant_tunic_new, itm_arena_tunic_d, itm_arena_tunic_d_vest, itm_wrapping_boots, itm_felt_hat_b, itm_head_wrappings], def_attrib|level(4),wp(55),knows_common|knows_power_draw_2|knows_ironflesh_1,rhodok_face_younger_1, rhodok_face_old_2],
  ["rhodok_milita", "Rhodok Militia", "Rhodok Militia", tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_5, [itm_pitch_fork, itm_tab_shield_pavise_a, itm_hatchet, itm_mace_1, itm_voulge_short, itm_scythe, itm_peasant_tunic_new, itm_arena_tunic_d_leather, itm_m_leather_boots_a, itm_arming_cap], def_attrib|level(8),wp(90),knows_common|knows_power_draw_2|knows_ironflesh_1,rhodok_face_younger_1, rhodok_face_old_2],
  ["rhodok_hunter", "Rhodok Hunter", "Rhodok Hunters", tf_guarantee_all,0,0,fac_kingdom_5, [itm_fur_covered_shield, itm_hatchet, itm_mace_1, itm_falchion, itm_rawhide_coat_new_a, itm_rawhide_coat_leather_lamellar, itm_m_leather_boots_a, itm_pilgrim_hood, itm_hunting_crossbow, itm_bolts], def_attrib|level(8),wp(80)|wp_crossbow(100),knows_common|knows_power_draw_2|knows_ironflesh_1,rhodok_face_younger_1, rhodok_face_old_2],
  ["rhodok_bear_hunter", "Rhodok Bear Hunter", "Rhodok Bear Hunters", tf_guarantee_all,0,0,fac_kingdom_5, [itm_fur_covered_shield, itm_one_handed_war_axe_a, itm_mace_2, itm_grosse_messer, itm_rawhide_coat_lamellar, itm_m_leather_boots_a, itm_pilgrim_hood, itm_hunting_crossbow, itm_bolts, itm_m_gloves_a], def_attrib|level(15),wp(110)|wp_crossbow(140),knows_common|knows_power_draw_2|knows_ironflesh_1,rhodok_face_younger_1, rhodok_face_old_2],

  ["rhodok_tribesman","Rhodok Tribesman","Rhodok Tribesmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_5,[itm_pitch_fork,itm_voulge_short,itm_felt_hat_b, itm_headcloth, itm_head_wrappings, itm_arming_cap, itm_long_spiked_club, itm_tab_shield_pavise_a, itm_peasant_tunic_padded, itm_m_leather_boots_a, itm_m_gloves_a, itm_leather_gloves], def_attrib|level(4),wp(55),knows_common|knows_power_draw_2|knows_ironflesh_1,rhodok_face_younger_1, rhodok_face_old_2],

  ["rhodok_levy","Rhodok Levy","Rhodok Levy",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_5, [itm_spear, itm_arming_cap, itm_mace_2, itm_mace_3, itm_mace_4, itm_tab_shield_pavise_b, itm_shirt_a_padded_new, itm_aketon_green, itm_m_onion_bascinet_a, itm_m_onion_bascinet_b, itm_m_onion_bascinet_c, itm_m_gloves_a, itm_leather_gloves, itm_m_hose_a, itm_m_hose_b, itm_m_hose_c], def_attrib|level(6),wp(60),knows_common|knows_power_draw_2|knows_ironflesh_1,rhodok_face_young_1, rhodok_face_old_2],
  ["rhodok_foot_knight","Rhodok Foot Knight","Rhodok Foot Knights",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0, fac_kingdom_5, [itm_crusader_sword, itm_shield_kite_i, itm_shield_kite_k, itm_peasant_tunic_cuirass, itm_m_leather_boots_a, itm_m_gloves_a, itm_leather_gloves, itm_m_kattle_a], def_attrib|level(9),wp(80),knows_common|knows_ironflesh_2|knows_shield_1|knows_power_strike_2|knows_athletics_1,rhodok_face_young_1, rhodok_face_old_2],
  ["rhodok_swordmaster","Rhodok Swordmaster","Rhodok Swordmasters",tf_guarantee_all,0,0, fac_kingdom_5, [itm_crusader_sword, itm_morningstar, itm_grosse_messer_b, itm_german_bastard_sword, itm_shield_kite_i, itm_shield_kite_k, itm_m_corrazina_a, itm_m_corrazina_b, itm_m_corrazina_c, itm_m_greaves_a, itm_m_greaves_b, itm_m_gauntlets_a, itm_m_gauntlets_b, itm_m_bascinet_a, itm_m_bascinet_b], def_attrib|level(17),wp(130),knows_common|knows_ironflesh_5|knows_shield_1|knows_power_strike_5|knows_athletics_1,rhodok_face_young_1, rhodok_face_old_2],
  ["rhodok_brother_of_sword", "Brother of the Sword", "Brothers of the Sword", tf_guarantee_all,0,0,fac_kingdom_5, [itm_crusader_sword, itm_morningstar, itm_grosse_messer_b, itm_german_bastard_sword, itm_shield_kite_i, itm_shield_kite_k, itm_m_churburg_a, itm_m_churburg_b, itm_m_greaves_a, itm_m_greaves_b, itm_m_gauntlets_a, itm_m_gauntlets_b, itm_m_bascinet_a, itm_m_bascinet_b], def_attrib|level(25),wp(165),knows_common|knows_ironflesh_8|knows_shield_6|knows_power_strike_8|knows_athletics_5,rhodok_face_young_1, rhodok_face_old_2],
  
  ["rhodok_spearman","Rhodok Spearman","Rhodok Spearmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_5,
   [itm_spear,itm_pike,itm_spear,itm_tab_shield_pavise_a,itm_falchion, itm_m_flat_top_a, itm_m_coif_alternate_c,
    itm_peasant_tunic_lamellar, itm_m_leather_boots_a, itm_m_gloves_a, itm_leather_gloves, itm_m_pepperpot_a, itm_m_pepperpot_b],
   def_attrib|level(9),wp(80),knows_common|knows_ironflesh_2|knows_shield_1|knows_power_strike_2|knows_athletics_1,rhodok_face_young_1, rhodok_face_old_2],

  ["rhodok_executioner","Rhodok Executioner","Rhodok Executioners",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_5, [itm_war_axe, itm_plate_covered_round_shield, itm_military_sickle_a, itm_m_munitions_helm_a, itm_m_munitions_helm_b, itm_peasant_tunic_lamellar, itm_m_greaves_a, itm_m_gloves_a], def_attrib|level(19),wp(145),knows_common|knows_ironflesh_9|knows_shield_3|knows_power_strike_9|knows_athletics_3,rhodok_face_young_1, rhodok_face_old_2],
  ["rhodok_law_itself","Rhodok Law Itself","Rhodok Laws Themselves",tf_guarantee_all,0,0,fac_kingdom_5, [itm_war_axe, itm_shield_heater_d, itm_morningstar, itm_m_tower_helm_a, itm_peasant_tunic_lamellar, itm_m_greaves_b, itm_m_gauntlets_b], def_attrib|level(27),wp(235),knows_common|knows_ironflesh_10|knows_shield_7|knows_power_strike_10|knows_athletics_7,rhodok_face_young_1, rhodok_face_old_2],

  ["rhodok_trained_spearman","Rhodok Trained Spearman","Rhodok Trained Spearmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_5,
   [itm_guisarme, itm_side_sword, itm_grosse_messer,itm_tab_shield_pavise_b, itm_m_corrazina_a, itm_m_corrazina_b, itm_m_corrazina_c, itm_m_greaves_a, itm_m_gauntlets_a],
   def_attrib|level(14),wp_one_handed (105) | wp_two_handed (105) | wp_polearm (115) | wp_archery (105) | wp_crossbow (105) | wp_throwing (105),knows_common|knows_ironflesh_3|knows_shield_2|knows_power_strike_2|knows_athletics_2,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_veteran_spearman","Rhodok Veteran Spearman","Rhodok Veteran Spearmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_5,
   [itm_english_bill, itm_guisarme, itm_italian_sword, itm_italian_falchion, itm_side_sword, itm_grosse_messer,itm_tab_shield_pavise_c, itm_m_churburg_a, itm_m_churburg_b, itm_m_tower_helm_a, itm_m_greaves_b, itm_m_gauntlets_b],
   def_attrib|level(19),wp_one_handed (115) | wp_two_handed (115) | wp_polearm (130) | wp_archery (115) | wp_crossbow (115) | wp_throwing (115),knows_common|knows_ironflesh_5|knows_shield_3|knows_power_strike_4|knows_athletics_3,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_sergeant","Rhodok Sergeant","Rhodok Sergeants",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_5,
   [itm_swiss_halberd, itm_italian_sword, itm_italian_falchion, itm_side_sword, itm_grosse_messer,itm_tab_shield_pavise_d, itm_m_churburg_c, itm_m_tower_helm_b, itm_m_greaves_b, itm_m_gauntlets_b],
   def_attrib|level(25),wp_one_handed (130) | wp_two_handed (115) | wp_polearm (155) | wp_archery (115) | wp_crossbow (115) | wp_throwing (115),knows_common|knows_ironflesh_6|knows_shield_5|knows_power_strike_5|knows_athletics_5,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_crossbowman","Rhodok Crossbowman","Rhodok Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_kingdom_5,
   [itm_sword_medieval_a,itm_falchion,itm_club_with_spike_head,itm_tab_shield_pavise_a,itm_crossbow,itm_bolts,
    itm_arena_tunic_d_leather,itm_m_coif_alternate_a, itm_m_coif_alternate_b, itm_m_coif_alternate_c, itm_m_leather_boots_a, itm_mt_leather_gloves_a],
   def_attrib|level(10),wp(85),knows_common|knows_ironflesh_2|knows_shield_1|knows_power_strike_1|knows_athletics_2,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_trained_crossbowman","Rhodok Trained Crossbowman","Rhodok Trained Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_5,
   [itm_sword_medieval_a,itm_sword_medieval_b_small,itm_club_with_spike_head,itm_tab_shield_pavise_a,itm_crossbow,itm_bolts, itm_arena_tunic_d_lamellar, itm_arena_tunic_d_lamellar_variant, itm_m_conical_helmet_a, itm_m_flat_top_a, itm_m_greaves_a, itm_m_gloves_a],
   def_attrib|level(15),wp_one_handed (90) | wp_two_handed (90) | wp_polearm (90) | wp_archery (90) | wp_crossbow (105) | wp_throwing (90),knows_common|knows_ironflesh_1|knows_shield_2|knows_power_strike_2|knows_athletics_3,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_veteran_crossbowman","Rhodok Veteran Crossbowman","Rhodok Veteran Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_5,
   [itm_sword_medieval_a,itm_sword_medieval_b_small,itm_fighting_pick,itm_club_with_spike_head,itm_tab_shield_pavise_b,itm_tab_shield_pavise_c,itm_heavy_crossbow,itm_bolts, itm_arena_tunic_d_lamellar_variant, itm_m_pepperpot_c, itm_m_greaves_a, itm_m_gauntlets_a],
   def_attrib|level(20),wp_one_handed (100) | wp_two_handed (100) | wp_polearm (100) | wp_archery (100) | wp_crossbow (120) | wp_throwing (100),knows_common|knows_ironflesh_2|knows_shield_3|knows_power_strike_3|knows_athletics_4,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_sharpshooter","Rhodok Sharpshooter","Rhodok Sharpshooters",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_5,
   [itm_sword_medieval_b,itm_military_pick,itm_military_hammer,itm_tab_shield_pavise_c,itm_sniper_crossbow,itm_steel_bolts, itm_arena_tunic_d_mail, itm_arena_tunic_d_haubergeon, itm_m_pepperpot_c, itm_m_greaves_b, itm_m_gauntlets_b],
   str_14 | agi_5 | int_4 | cha_4|level(25),wp_one_handed (110) | wp_two_handed (110) | wp_polearm (110) | wp_archery (100) | wp_crossbow (140) | wp_throwing (100),knows_common|knows_ironflesh_3|knows_shield_4|knows_power_strike_4|knows_athletics_6,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_messenger","Rhodok Messenger","Rhodok Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_5,
   [itm_sword_medieval_b,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_short_bow,itm_arrows],
   def_attrib|agi_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_deserter","Rhodok Deserter","Rhodok Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_arrows,itm_spiked_mace,itm_axe,itm_falchion,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_javelin,itm_javelin,itm_steppe_cap,itm_nomad_cap,itm_leather_vest,itm_leather_vest,itm_nomad_armor,itm_nomad_boots],
   def_attrib|str_10|level(14),wp(80),knows_ironflesh_1|knows_power_draw_1,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_prison_guard","Prison Guard","Prison Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_5,
   [itm_ashwood_pike,itm_battle_fork,itm_battle_axe,itm_fighting_axe,itm_tab_shield_pavise_b,itm_bascinet_2,itm_surcoat_over_mail,itm_mail_chausses,itm_iron_greaves,itm_leather_gloves],
   def_attrib|level(24),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_castle_guard","Castle Guard","Castle Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_5,
   [itm_ashwood_pike,itm_battle_fork,itm_battle_axe,itm_fighting_axe,itm_tab_shield_pavise_c,itm_bascinet_2,itm_surcoat_over_mail,itm_mail_chausses,itm_iron_greaves,itm_leather_gloves],
   def_attrib|level(24),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,rhodok_face_middle_1, rhodok_face_older_2],
#peasant - retainer - footman - man-at-arms -  knight


 ["sarranid_recruit","Sarranid Recruit","Sarranid Recruits",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,[itm_scythe,itm_hatchet,itm_pickaxe,itm_club,itm_stones,itm_tab_shield_heater_a,itm_mkk_turban_a,itm_mkk_turban_b,itm_mkk_turban_c,itm_mkk_boots_common_a,itm_mkk_boots_common_b,itm_mkk_boots_common_c,itm_mkk_robe_a,itm_mkk_robe_b,itm_mkk_robe_c],def_attrib|level(4),wp(60),knows_common|knows_athletics_1,swadian_face_younger_1, swadian_face_middle_2],
 ["sarranid_footman","Sarranid Footman","Sarranid Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_6,[itm_bamboo_spear,itm_arabian_sword_a,itm_tab_shield_kite_a,
    itm_mkk_midi_robe_a,itm_mkk_midi_robe_b,itm_mkk_midi_robe_c,itm_mkk_midi_robe_d,itm_mkk_midi_robe_e,itm_mkk_midi_robe_f,itm_mkk_helm_warrior_a,itm_mkk_helm_warrior_b,itm_mkk_helm_warrior_c,itm_mkk_boots_common_b,itm_mkk_boots_common_a,itm_mkk_boots_common_c,itm_mkk_boots_b,itm_mkk_boots_a,itm_mkk_gloves_a],
   def_attrib|level(9),wp(75),knows_common|knows_athletics_2,swadian_face_young_1, swadian_face_old_2],
 ["sarranid_veteran_footman","Sarranid Veteran Footman","Sarranid Veteran Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_6,[itm_bamboo_spear,itm_arabian_sword_a,itm_arabian_sword_b,itm_tab_shield_kite_b,itm_mkk_leather_boots_a,itm_mkk_helm_warrior_a,itm_mkk_helm_warrior_b,itm_mkk_helm_warrior_c,itm_mkk_scale_vest_a,itm_mkk_scale_vest_b,itm_mkk_scale_vest_c,itm_mkk_scale_vest_d,itm_mkk_scale_vest_e,itm_mkk_scale_vest_f,itm_jarid,itm_arabian_sword_a,itm_mace_3,itm_mkk_gloves_a,itm_mkk_gauntlets_sar_a],def_attrib|level(14),wp_one_handed (85) | wp_two_handed (85) | wp_polearm (85) | wp_archery (75) | wp_crossbow (75) | wp_throwing (100),knows_common|knows_athletics_2|knows_power_throw_2|knows_ironflesh_1|knows_power_strike_2|knows_shield_2,swadian_face_young_1, swadian_face_old_2],
 ["sarranid_infantry","Sarranid Infantry","Sarranid Infantries",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_6,[itm_jarid,itm_sarranid_axe_a,itm_arabian_sword_b,itm_mace_3,itm_spear,itm_tab_shield_kite_c,itm_mkk_semi_heavy_helmet_a,itm_mkk_semi_heavy_helmet_b,itm_mkk_semi_heavy_helmet_c,itm_mkk_semi_heavy_helmet_d,itm_mkk_semi_heavy_helmet_e,itm_mkk_semi_heavy_helmet_f,itm_mkk_archer_armor_a,itm_mkk_archer_armor_b,itm_mkk_archer_armor_c,itm_mkk_archer_armor_d,itm_mkk_leather_boots_a,itm_mkk_leather_boots_b,itm_mkk_gauntlets_sar_a],def_attrib|level(20),wp_one_handed (105) | wp_two_handed (105) | wp_polearm (105) | wp_archery (75) | wp_crossbow (75) | wp_throwing (110),knows_common|knows_riding_3|knows_ironflesh_2|knows_power_strike_3|knows_shield_3 | knows_power_throw_3|knows_athletics_3,swadian_face_middle_1, swadian_face_old_2],
 ["sarranid_guard","Sarranid Guard","Sarranid Guards",tf_mounted|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_6,
   [itm_military_pick,itm_sarranid_two_handed_axe_a,itm_jarid,itm_scimitar_b,itm_war_spear,itm_mace_4,itm_tab_shield_kite_d,itm_mkk_semi_heavy_helmet_a,itm_mkk_semi_heavy_helmet_b,itm_mkk_semi_heavy_helmet_c,itm_mkk_semi_heavy_helmet_d,itm_mkk_semi_heavy_helmet_e,itm_mkk_semi_heavy_helmet_f,itm_mkk_infantry_armor_a,itm_mkk_infantry_armor_b,itm_mkk_heavy_boots_a,itm_mkk_gauntlets_sar_b],def_attrib|level(25),wp_one_handed (135) | wp_two_handed (135) | wp_polearm (135) | wp_archery (75) | wp_crossbow (75) | wp_throwing (140),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_4|knows_power_throw_4|knows_athletics_5,swadian_face_middle_1, swadian_face_older_2],
 ["sarranid_skirmisher","Sarranid Skirmisher","Sarranid Skirmishers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,[itm_jarid,itm_jarid,itm_arabian_sword_a,itm_spiked_club,itm_tab_shield_small_round_a,itm_mkk_helm_sar_a,itm_mkk_helm_light_sarranid,itm_mkk_boots_common_a,itm_mkk_boots_common_b,itm_mkk_boots_common_c,itm_mkk_robe_a,itm_mkk_robe_b,itm_mkk_robe_c],def_attrib|level(14),wp(80),knows_common|knows_riding_2|knows_power_throw_2|knows_ironflesh_1|knows_athletics_3,swadian_face_young_1, swadian_face_middle_2],
 ["sarranid_archer","Sarranid Archer","Sarranid Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,[itm_arrows,itm_arrows,itm_nomad_bow,itm_arabian_sword_a,itm_mkk_scale_vest_a,itm_mkk_scale_vest_b,itm_mkk_scale_vest_c,itm_mkk_scale_vest_d,itm_mkk_scale_vest_e,itm_mkk_scale_vest_f,itm_mkk_helm_mail_a,itm_mkk_helm_mail_b,itm_mkk_helm_mail_c,itm_mkk_helm_mail_d,itm_mkk_helm_mail_e,itm_mkk_leather_boots_a,itm_mkk_gloves_a],
   def_attrib|level(19),wp_one_handed (90) | wp_two_handed (90) | wp_polearm (90) | wp_archery (100) | wp_crossbow (90) | wp_throwing (100),knows_common|knows_power_draw_3|knows_ironflesh_2|knows_power_throw_3|knows_athletics_4,swadian_face_young_1, swadian_face_old_2],
 ["sarranid_master_archer","Sarranid Master Archer","Sarranid Master Archers",tf_guarantee_ranged|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_6,[itm_barbed_arrows,itm_barbed_arrows,itm_arabian_sword_b,itm_mace_3,itm_strong_bow,itm_nomad_bow,itm_mkk_helm_mail_a,itm_mkk_helm_mail_b,itm_mkk_helm_mail_c,itm_mkk_helm_mail_d,itm_mkk_helm_mail_e,itm_mkk_leather_boots_a,itm_mkk_gloves_a,itm_mkk_archer_armor_a,itm_mkk_archer_armor_b,itm_mkk_archer_armor_c,itm_mkk_archer_armor_d],str_14 | agi_5 | int_4 | cha_4|level(24),wp_one_handed (100) | wp_two_handed (100) | wp_polearm (100) | wp_archery (130) | wp_crossbow (100) | wp_throwing (130),knows_common|knows_power_draw_4|knows_power_throw_4|knows_ironflesh_3|knows_athletics_5,swadian_face_middle_1, swadian_face_older_2],
 ["sarranid_horseman","Sarranid Horseman","Sarranid Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_6,[itm_lance,itm_arabian_sword_b,itm_scimitar_b,itm_mace_4,itm_tab_shield_small_round_b,itm_saracin_hard_horses_a_v1,itm_saracin_hard_horses_b_v1,itm_saracin_hard_horses_c_v1,itm_saracin_hard_horses_d_v1,itm_mkk_scale_vest_alt_a,itm_mkk_scale_vest_alt_b,itm_mkk_gulam_helm_a,itm_mkk_gulam_helm_b,itm_mkk_gulam_helm_c,itm_mkk_gulam_helm_d,itm_mkk_gulam_helm_f,itm_mkk_gauntlets_sar_a,itm_mkk_gauntlets_mail_a,itm_mkk_leather_boots_a,itm_mkk_leather_boots_b],def_attrib|level(20),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
 ["sarranid_mamluke","Sarranid Mamluke","Sarranid Mamlukes",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_6,[itm_heavy_lance,itm_scimitar_b,itm_sarranid_two_handed_mace_1,itm_sarranid_cavalry_sword,itm_tab_shield_small_round_c,itm_saracin_hard_horses_a,itm_saracin_hard_horses_b,itm_saracin_hard_horses_c,itm_saracin_hard_horses_d,itm_mkk_heavy_boots_a,itm_mkk_heavy_boots_a,itm_mkk_mamluke_a,itm_mkk_mamluke_b,itm_mkk_mamluke_c,itm_mkk_gauntlets_sar_b,itm_mkk_gauntlets_sar_a,itm_mkk_heavy_helmet_a,itm_mkk_heavy_helmet_b,itm_mkk_heavy_helmet_c],def_attrib|level(27),wp_one_handed (150) | wp_two_handed (130) | wp_polearm (130) | wp_archery (75) | wp_crossbow (75) | wp_throwing (110),knows_common|knows_riding_6|knows_shield_5|knows_ironflesh_5|knows_power_strike_5,swadian_face_middle_1, swadian_face_older_2],

   ["sarranid_messenger","Sarranid Messenger","Sarranid Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_6,
   [itm_lance,itm_arabian_sword_b,itm_scimitar_b,itm_mace_4,itm_tab_shield_small_round_b,
    itm_sarranid_mail_shirt,itm_mail_chausses,itm_sarranid_helmet1,itm_courser,itm_hunter],
   def_attrib|level(20),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
  ["sarranid_deserter","Sarranid Deserter","Sarranid Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_lance,itm_arabian_sword_b,itm_scimitar_b,itm_mace_4,itm_tab_shield_small_round_b,
    itm_sarranid_mail_shirt,itm_mail_chausses,itm_desert_turban,itm_arabian_horse_a],
   def_attrib|level(20),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
  ["sarranid_prison_guard","Prison Guard","Prison Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_6,
   [itm_arabian_sword_b,itm_scimitar_b,itm_war_spear,itm_mace_4,itm_sarranid_boots_c,itm_arabian_armor_b,itm_sarranid_mail_coif,itm_sarranid_helmet1,itm_sarranid_horseman_helmet,itm_mail_boots,itm_iron_greaves,itm_mail_mittens,itm_leather_gloves,itm_tab_shield_kite_d],
   def_attrib|level(25),wp_melee(135)|wp_throwing(100),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,swadian_face_middle_1, swadian_face_older_2],
  ["sarranid_castle_guard","Castle Guard","Castle Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_6,
   [itm_arabian_sword_b,itm_scimitar_b,itm_war_spear,itm_mace_4,itm_sarranid_boots_c, itm_sarranid_boots_d,itm_arabian_armor_b,itm_sarranid_mail_coif,itm_sarranid_helmet1,itm_sarranid_horseman_helmet,itm_mail_boots,itm_iron_greaves,itm_mail_mittens,itm_leather_gloves,itm_tab_shield_kite_d],
   def_attrib|level(25),wp_melee(135)|wp_throwing(100),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,swadian_face_middle_1, swadian_face_older_2],

  #        Looter
  #        /        \
  #      Bandit   Outlaw
  #      /      \         /    
  # Pillager   Marauder  Highwayman
  #                     |
  #               Bandit Lord
  ["looter","Looter","Looters",tf_guarantee_armor|tf_guarantee_boots,0,0,fac_outlaws,
   [itm_m_hose_a, itm_m_hose_b, itm_m_hose_c, itm_m_hose_d, itm_m_hose_e, itm_mt_leather_boots_e, itm_leather_boots, itm_m_padded_dark_a, itm_m_padded_dark_b, itm_m_padded_dark_c, itm_m_aketon_a, itm_m_aketon_old_a, itm_m_aketon_old_b, itm_m_aketon_black_a, itm_m_aketon_black_b, itm_m_plain_round_shield_a, itm_m_plain_round_shield_b, itm_m_plain_round_shield_c, itm_m_plain_round_shield_d, itm_m_plain_round_shield_e, itm_grosse_messer, itm_falchion, itm_italian_falchion, itm_boar_spear, itm_head_wrappings, itm_leather_cap, itm_black_hood, itm_black_hood, itm_m_arming_cap_c, itm_m_arming_cap_a, itm_m_coif_cloth_a, itm_m_coif_cloth_b, itm_m_swadia_common_helmet_b, itm_m_padded_coif_a, itm_m_padded_coif_b, itm_leather_gloves],
   def_attrib|level(4),wp(20),knows_common,bandit_face1, bandit_face2],
  ["bandit","Bandit","Bandits",tf_guarantee_armor|tf_guarantee_boots,0,0,fac_outlaws, [itm_mt_leather_boots_e, itm_m_leather_boots_a, itm_leather_boots, itm_m_aketon_black_b, itm_m_aketon_old_c, itm_m_hauberk_black_a, itm_m_hauberk_old_a, itm_m_plain_round_shield_a, itm_m_plain_round_shield_b, itm_m_plain_round_shield_c, itm_m_plain_round_shield_d, itm_m_plain_round_shield_e,itm_grosse_messer_b, itm_italian_falchion, itm_partisan, itm_guisarme, itm_german_hunting_spear, itm_hunting_crossbow, itm_bolts, itm_m_swadia_common_helmet_b, itm_m_swadia_common_helmet_a, itm_m_swadia_common_helmet_c, itm_m_coif_alternate_a, itm_leather_gloves, itm_m_gloves_a], def_attrib|level(10),wp(60),knows_common|knows_power_draw_1,bandit_face1, bandit_face2],

  ["pillager","Pillager","Pillagers",tf_guarantee_all,0,0,fac_outlaws, [itm_m_leather_boots_a, itm_m_hauberk_a, itm_m_hauberk_b, itm_m_hauberk_c, itm_m_gloves_a, itm_tab_shield_heater_b, itm_grosse_messer, itm_italian_falchion, itm_italian_sword, itm_heavy_crossbow, itm_steel_bolts, itm_padded_coif, itm_mail_coif, itm_kettle_hat], def_attrib|level(12),wp(70),knows_common|knows_power_draw_1|knows_riding_2,bandit_face1, bandit_face2],
  
  ["marauder","Marauder","Marauders",tf_guarantee_all,0,0,fac_outlaws, [itm_m_greaves_b, itm_m_brigandine_b, itm_german_poleaxe, itm_simple_poleaxe, itm_elegant_poleaxe, itm_english_bill, itm_swiss_halberd, itm_ms_great_helmet_b], def_attrib|level(16),wp(90),knows_common|knows_power_draw_1|knows_riding_2,bandit_face1, bandit_face2],

  ["outlaw","Outlaw","Outlaws",tf_guarantee_all,0,0,fac_outlaws, [itm_m_hose_a, itm_m_hose_b, itm_m_hose_c, itm_m_hose_d, itm_m_hose_e, itm_m_aketon_a, itm_m_aketon_b, itm_m_hauberk_a, itm_tab_shield_small_round_a, itm_tab_shield_small_round_b, itm_grosse_messer, itm_espada_eslavona_a,itm_espada_eslavona_b, itm_milanese_sword, itm_spear, itm_hunting_crossbow, itm_bolts, itm_saddle_horse], def_attrib|level(10),wp(60),knows_common|knows_riding_2,bandit_face1, bandit_face2],
  ["highwayman","Highwayman","Highwaymen",tf_guarantee_all,0,0,fac_outlaws, [itm_m_leather_boots_a, itm_m_hauberk_a, itm_m_hauberk_b, itm_m_hauberk_c, itm_m_brigandine_c, itm_m_brigandine_e, itm_tab_shield_small_round_c, itm_grosse_messer_b, itm_italian_falchion, itm_italian_sword, itm_partisan, itm_guisarme, itm_lance, itm_hunting_crossbow, itm_bolts, itm_saddle_horse], def_attrib|level(16),wp(90),knows_common|knows_riding_5|knows_riding_2,bandit_face1, bandit_face2],
  ["bandit_lord","Bandit Lord","Bandit Lords",tf_guarantee_all,0,0,fac_outlaws, [itm_m_greaves_a, itm_m_gauntlets_a, itm_mt_heavy_plate_a2, itm_ms_flamberg_great, itm_mt_armet_b, itm_hunting_crossbow, itm_bolts, itm_warhorse], knight_attrib_5|level(25),wp(245),knows_common|knows_power_draw_1|knows_riding_5|knows_ironflesh_10|knows_power_strike_6,bandit_face1, bandit_face2],

  #                     Cultist Acolyte
  #                      /            \
  #              Dark Cultist     Occultist
  #               /               /        \
  #      Shadowblade  Dark Cavalier  Shadow Rider
  # TODO: Complete troop tree for cultists
  ["cultist_acolyte","Cultist Acolyte","Cultist Acolytes",tf_guarantee_all,0,0,fac_outlaws, [itm_mt_leather_boots_e, itm_mt_leather_gloves_a, itm_mt_hood_a3, itm_ms_armor_doom_cult_a, itm_ms_armor_doom_cult_b, itm_winged_mace, itm_one_handed_battle_axe_c, itm_tab_shield_heater_cav_a], def_attrib|str_15|agi_15|level(12),wp(100),knows_common|knows_ironflesh_3,bandit_face1, bandit_face2],
  ["dark_cultist","Dark Cultist","Dark Cultists",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_outlaws, [itm_ms_doom_cult_greaves_a, itm_ms_doom_cult_greaves_b, itm_ms_doom_cult_greaves_c, itm_ms_doom_cult_gauntlets_a, itm_ms_helmet_cult_a, itm_ms_helmet_cult_a2, itm_ms_armor_doom_cult_c, itm_ms_armor_doom_cult_c2, itm_ms_armor_doom_cult_c3, itm_ms_armor_doom_cult_c4, itm_ms_armor_doom_cult_c5, itm_winged_mace, itm_one_handed_battle_axe_c, itm_tab_shield_heater_cav_b, itm_ms_flamberg, itm_ms_flamberg_great], def_attrib|str_20|agi_20|level(24), wp(120), knows_common|knows_ironflesh_10, bandit_face1, bandit_face2],

  ["skeleton_newborn","Newborn Skeleton","Newborn Skeletons",tf_awakened|tf_allways_fall_dead|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_outlaws,[itm_m_swadia_common_helmet_a, itm_m_swadia_common_helmet_b, itm_m_swadia_common_helmet_c, itm_surcoat_over_mail_undead_a, itm_surcoat_over_mail_undead_b, itm_surcoat_over_mail, itm_m_swadia_gloves_a, itm_m_swadia_mail_gloves_a, itm_m_swadia_mail_boots_a, itm_m_swadia_mail_boots_b, itm_shield_heater_d, itm_shield_kite_k, itm_longsword, itm_english_longsword, itm_german_bastard_sword, itm_grosse_messer_b, itm_irish_sword],def_attrib|str_25|agi_25|level(25),wp(250),knows_common,0,0],

  ["brigand","Brigand","Brigands",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_outlaws,
   [itm_arrows,itm_spiked_mace,itm_sword_viking_1,itm_falchion,itm_wooden_shield,itm_hide_covered_round_shield,itm_long_bow,itm_leather_cap,itm_leather_jerkin,itm_nomad_boots,itm_saddle_horse],
   def_attrib|level(16),wp(90),knows_common|knows_power_draw_3,bandit_face1, bandit_face2],
  ["mountain_bandit","Mountain Bandit","Mountain Bandits",tf_guarantee_armor|tf_guarantee_boots,0,0,fac_outlaws,
   [itm_arrows,itm_sword_viking_1,itm_boar_spear,itm_hatchet,itm_hand_axe,itm_falchion,itm_short_bow,itm_javelin,itm_spiked_club,itm_fur_covered_shield,itm_hide_covered_round_shield,
    itm_m_arming_cap_c,itm_black_hood,itm_m_coif_cloth_a,itm_m_hauberk_mountain_a,itm_m_hauberk_mountain_b,itm_m_hauberk_mountain_c,itm_m_hauberk_mountain_d,itm_mt_leather_boots_e,itm_mt_mail_boots_a],
   def_attrib|level(11),wp(90),knows_common|knows_power_draw_2,rhodok_face_young_1, rhodok_face_old_2],
  ["forest_bandit","Forest Bandit","Forest Bandits",tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_boots,0,0,fac_outlaws,
   [itm_arrows,itm_shortened_voulge,itm_one_handed_battle_axe_a,itm_hunting_bow,
    itm_felt_hat_b, itm_itm_felt_hat_a, itm_itm_felt_hat_b, itm_itm_felt_hat_c, itm_itm_felt_hat_d, itm_m_aketon_forest_a, itm_m_aketon_forest_b, itm_m_aketon_forest_c, itm_m_hose_c, itm_m_leather_boots_a, itm_m_gloves_a, itm_leather_gloves],
   def_attrib|level(11),wp(90),knows_common|knows_power_draw_3,swadian_face_young_1, swadian_face_old_2],
  ["sea_raider","Sea Raider","Sea Raiders",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_outlaws,
   [itm_arrows,itm_sword_viking_1,itm_sword_viking_2,itm_fighting_axe,itm_war_axe,itm_battle_axe,itm_spear,itm_war_spear,itm_tab_shield_round_b,itm_tab_shield_round_c,itm_long_bow,itm_javelin,itm_throwing_axes,itm_ms_spangen_helmet_c, itm_ms_spangen_helmet_b, itm_ms_spangen_helmet_a,itm_m_hauberk_navy_a,itm_m_hauberk_navy_b,itm_m_hauberk_navy_c,itm_m_brigandine_navy_c,itm_m_leather_boots_a, itm_mt_leather_boots_e, itm_mt_leather_boots_b, itm_mt_leather_boots_c, itm_mt_mail_boots_a],
   def_attrib|level(16),wp(110),knows_ironflesh_2|knows_power_strike_2|knows_power_draw_3|knows_power_throw_2|knows_riding_1|knows_athletics_2,nord_face_young_1, nord_face_old_2],
  ["steppe_bandit","Steppe Bandit","Steppe Bandits",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged|tf_mounted,0,0,fac_outlaws,
   [itm_arrows,itm_sword_khergit_1,itm_winged_mace,itm_spear, itm_light_lance,itm_nomad_bow,itm_nomad_bow,itm_short_bow,itm_jarid,itm_leather_steppe_cap_a,itm_leather_steppe_cap_b,itm_nomad_cap,itm_nomad_cap_b,itm_khergit_armor,itm_steppe_armor,itm_leather_vest,itm_hide_boots,itm_nomad_boots,itm_leather_covered_round_shield,itm_leather_covered_round_shield,itm_saddle_horse,itm_steppe_horse,itm_steppe_horse],
   def_attrib|level(12),wp(100),knows_riding_4|knows_horse_archery_3|knows_power_draw_3,khergit_face_young_1, khergit_face_old_2],
  ["taiga_bandit","Taiga Bandit","Taiga Bandits",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_outlaws,
   [itm_arrows,itm_sword_khergit_1,itm_winged_mace,itm_spear, itm_light_lance,itm_nomad_bow,itm_nomad_bow,itm_short_bow,itm_jarid,itm_javelin,itm_vaegir_fur_cap,itm_leather_steppe_cap_c,itm_nomad_armor,itm_leather_jerkin,itm_hide_boots,itm_nomad_boots,itm_leather_covered_round_shield,itm_leather_covered_round_shield],
   def_attrib|level(15),wp(110),knows_common|knows_power_draw_4|knows_power_throw_3,vaegir_face_young_1, vaegir_face_old_2],
  ["desert_bandit","Piaktu Bandit","Piaktu Bandits",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_mounted,0,0,fac_outlaws,
   [itm_arrows,itm_arabian_sword_a,itm_winged_mace,itm_spear, itm_light_lance,itm_jarid,itm_nomad_bow,itm_short_bow,itm_jarid,itm_m_desert_bandit_a, itm_m_desert_bandit_b, itm_m_desert_bandit_c, itm_m_desert_bandit_d, itm_m_bandit_turban_a, itm_m_bandit_turban_b, itm_m_bandit_turban_c, itm_m_bandit_turban_d, itm_mkk_leather_boots_a, itm_civil_rich_boots_a, itm_civil_rich_boots_b, itm_leather_covered_round_shield,itm_leather_covered_round_shield,itm_arabian_horse_a],
   def_attrib|level(12),wp(100),knows_riding_4|knows_horse_archery_3|knows_power_draw_3,khergit_face_young_1, khergit_face_old_2],
  
  ["black_khergit_horseman","Black Khergit Horseman","Black Khergit Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_black_khergits,
   [itm_arrows,itm_sword_khergit_2,itm_scimitar,itm_scimitar,itm_winged_mace,itm_spear,itm_lance,itm_khergit_bow,itm_khergit_bow,itm_nomad_bow,itm_nomad_bow,itm_steppe_cap,itm_nomad_cap,itm_khergit_war_helmet,itm_khergit_war_helmet,itm_mail_hauberk,itm_lamellar_armor,itm_hide_boots,itm_plate_covered_round_shield,itm_plate_covered_round_shield,itm_saddle_horse,itm_steppe_horse],
   def_attrib|level(21),wp(100),knows_riding_3|knows_ironflesh_3|knows_horse_archery_3|knows_power_draw_3,khergit_face_young_1, khergit_face_old_2],

  ["manhunter","Manhunter","Manhunters",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_manhunters,
   [itm_mace_3,itm_winged_mace,itm_nasal_helmet,itm_padded_cloth,itm_aketon_green,itm_aketon_green,itm_wooden_shield,itm_nomad_boots,itm_wrapping_boots,itm_sumpter_horse],
   def_attrib|level(10),wp(50),knows_common,bandit_face1, bandit_face2],
##  ["deserter","Deserter","Deserters",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_swadian_deserters,
##   [itm_arrows,itm_spear,itm_fighting_pick,itm_short_bow,itm_sword,itm_voulge,itm_nordic_shield,itm_round_shield,itm_kettle_hat,itm_leather_cap,itm_padded_cloth,itm_leather_armor,itm_scale_armor,itm_saddle_horse],
##   def_attrib|level(12),wp(60),knows_common,bandit_face1, bandit_face2],

#fac_slavers
##  ["slave_keeper","Slave Keeper","Slave Keepers",tf_guarantee_armor ,0,0,fac_slavers,
##   [itm_cudgel,itm_club,itm_woolen_cap,itm_rawhide_coat,itm_coarse_tunic,itm_nomad_armor,itm_nordic_shield,itm_nomad_boots,itm_wrapping_boots,itm_sumpter_horse],
##   def_attrib|level(10),wp(60),knows_common,bandit_face1, bandit_face2],
  ["slave_driver","Slave Driver","Slave Drivers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse ,0,0,fac_slavers,
   [itm_club_with_spike_head,itm_segmented_helmet,itm_tribal_warrior_outfit,itm_nordic_shield,itm_leather_boots,itm_leather_gloves,itm_khergit_leather_boots,itm_steppe_horse],
   def_attrib|level(14),wp(80),knows_common,bandit_face1, bandit_face2],
  ["slave_hunter","Slave Hunter","Slave Hunters",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield ,0,0,fac_slavers,
   [itm_winged_mace,itm_maul,itm_kettle_hat,itm_mail_shirt,itm_tab_shield_round_c,itm_leather_boots,itm_leather_gloves,itm_courser],
   def_attrib|level(18),wp(90),knows_common,bandit_face1, bandit_face2],
  ["slave_crusher","Slave Crusher","Slave Crushers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield ,0,0,fac_slavers,
   [itm_sledgehammer,itm_spiked_mace,itm_mail_hauberk,itm_bascinet_2,itm_bascinet_3,itm_mail_mittens,itm_tab_shield_round_d,itm_mail_chausses,itm_splinted_leather_greaves,itm_hunter],
   def_attrib|level(22),wp(110),knows_common|knows_riding_4|knows_power_strike_3,bandit_face1, bandit_face2],
  ["slaver_chief","Slaver Chief","Slaver Chiefs",tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac_slavers,
   [itm_military_hammer,itm_warhammer,itm_brigandine_red,itm_steel_shield,itm_scale_gauntlets,itm_mail_mittens,itm_guard_helmet,itm_plate_boots,itm_mail_boots,itm_warhorse],
   def_attrib|level(26),wp(130),knows_common|knows_riding_4|knows_power_strike_5,bandit_face1, bandit_face2],

#Rhodok tribal, Hunter, warrior, veteran, warchief






#  ["undead_walker","undead_walker","undead_walkers",tf_undead|tf_allways_fall_dead,0,0,fac_undeads,
#   [], 
#   def_attrib|level(3),wp(60),knows_common,undead_face1, undead_face2],
#  ["undead_horseman","undead_horseman","undead_horsemen",tf_undead|tf_allways_fall_dead|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_undeads,
#   [], 
#   def_attrib|level(19),wp(100),knows_common,undead_face1, undead_face2],
#  ["undead_nomad","undead_nomad","undead_nomads",tf_undead|tf_allways_fall_dead|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_black_khergits,
#   [], 
#   def_attrib|level(21),wp(100),knows_common|knows_riding_4,khergit_face1, khergit_face2],
#  ["undead","undead","undead",tf_undead|tf_allways_fall_dead,0,0,fac_undeads,
#   [], 
#   def_attrib|level(3),wp(60),knows_common,undead_face1, undead_face2],
#  ["hell_knight","hell_knight","hell_knights",tf_undead|tf_allways_fall_dead|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_undeads,
#   [], 
#   def_attrib|level(23),wp(100),knows_common|knows_riding_3,undead_face1, undead_face2],

  ["follower_woman","Camp Follower","Camp Follower",tf_female|tf_guarantee_armor,0,0,fac_commoners,
   [itm_bolts,itm_light_crossbow,itm_short_bow,itm_crossbow,itm_nordic_shield,itm_hide_covered_round_shield,itm_hatchet,itm_hand_axe,itm_voulge,itm_fighting_pick,itm_club,itm_dress,itm_woolen_dress, itm_skullcap, itm_wrapping_boots],
   def_attrib|level(5),wp(70),knows_common,refugee_face1,refugee_face2],
  ["hunter_woman","Huntress","Huntresses",tf_female|tf_guarantee_armor,0,0,fac_commoners,
   [itm_bolts,itm_arrows,itm_light_crossbow,itm_short_bow,itm_crossbow,itm_nordic_shield,itm_hide_covered_round_shield,itm_hatchet,itm_hand_axe,itm_voulge,itm_fighting_pick,itm_club,itm_dress,itm_leather_jerkin, itm_skullcap, itm_wrapping_boots],
   def_attrib|level(10),wp(85),knows_common|knows_power_strike_1,refugee_face1,refugee_face2],
  ["fighter_woman","Camp Defender","Camp Defenders",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_bolts,itm_arrows,itm_light_crossbow,itm_short_bow,itm_crossbow,itm_fur_covered_shield,itm_hide_covered_round_shield,itm_hatchet,itm_voulge,itm_mail_shirt,itm_byrnie, itm_skullcap, itm_wrapping_boots],
   def_attrib|level(16),wp(100),knows_common|knows_riding_3|knows_power_strike_2|knows_athletics_2|knows_ironflesh_1,refugee_face1,refugee_face2],
  ["sword_sister","Sword Sister","Sword Sisters",tf_female|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_horse,0,0,fac_commoners,
   [itm_bolts,itm_sword_medieval_b,itm_sword_khergit_3,itm_plate_covered_round_shield,itm_tab_shield_small_round_c, itm_crossbow,itm_plate_armor,itm_coat_of_plates,itm_plate_boots,itm_guard_helmet,itm_helmet_with_neckguard,itm_courser,itm_leather_gloves],
   def_attrib|level(22),wp(140),knows_common|knows_power_strike_3|knows_riding_5|knows_athletics_3|knows_ironflesh_2|knows_shield_2,refugee_face1,refugee_face2],

  ["refugee","Refugee","Refugees",tf_female|tf_guarantee_armor,0,0,fac_commoners,
   [itm_knife,itm_pitch_fork,itm_sickle,itm_hatchet,itm_club,itm_dress,itm_robe,itm_woolen_dress, itm_headcloth, itm_woolen_hood, itm_wrapping_boots],
   def_attrib|level(1),wp(45),knows_common,refugee_face1,refugee_face2],
  ["peasant_woman","Peasant Woman","Peasant Women",tf_female|tf_guarantee_armor,0,0,fac_commoners,
   [itm_knife,itm_pitch_fork,itm_sickle,itm_hatchet,itm_club,itm_dress,itm_woolen_dress, itm_headcloth, itm_woolen_hood, itm_wrapping_boots],
   def_attrib|level(1),wp(40),knows_common,refugee_face1,refugee_face2],

 
  ["caravan_master","Caravan Master","Caravan Masters",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_commoners,
   [itm_sword_medieval_c,itm_fur_coat,itm_hide_boots,itm_saddle_horse,
    itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,
    itm_leather_jacket, itm_leather_cap],
   def_attrib|level(9),wp(100),knows_common|knows_riding_4|knows_ironflesh_3,mercenary_face_1, mercenary_face_2],

  ["kidnapped_girl","Kidnapped Girl","Kidnapped Girls",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_commoners,
   [itm_dress,itm_leather_boots],
   def_attrib|level(2),wp(50),knows_common|knows_riding_2,woman_face_1, woman_face_2],


#This troop is the troop marked as soldiers_end and town_walkers_begin
 ["town_walker_1","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_short_tunic, itm_linen_tunic,itm_fur_coat, itm_coarse_tunic, itm_tabard, itm_leather_vest, itm_arena_tunic_white, itm_leather_apron, itm_shirt, itm_arena_tunic_green, itm_arena_tunic_blue, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_hide_boots, itm_ankle_boots, itm_leather_boots, itm_fur_hat, itm_leather_cap, itm_straw_hat, itm_felt_hat],
   def_attrib|level(4),wp(60),knows_common,man_face_young_1, man_face_old_2],
 ["town_walker_2","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_blue_dress, itm_dress, itm_woolen_dress, itm_peasant_dress, itm_woolen_hose, itm_blue_hose, itm_wimple_a, itm_wimple_with_veil, itm_female_hood],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
 ["khergit_townsman","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [itm_sarranid_felt_hat,itm_turban,itm_wrapping_boots,itm_khergit_leather_boots,itm_sarranid_cloth_robe, itm_sarranid_cloth_robe_b],
   def_attrib|level(4),wp(60),knows_common,swadian_face_younger_1, swadian_face_middle_2],
 ["khergit_townswoman","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_blue_dress, itm_dress, itm_woolen_dress, itm_peasant_dress, itm_woolen_hose, itm_blue_hose, itm_wimple_a, itm_wimple_with_veil, itm_female_hood],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
 ["sarranid_townsman","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [itm_sarranid_felt_hat,itm_turban,itm_wrapping_boots,itm_sarranid_boots_a,itm_sarranid_cloth_robe, itm_sarranid_cloth_robe_b],
   def_attrib|level(4),wp(60),knows_common,swadian_face_younger_1, swadian_face_middle_2],
 ["sarranid_townswoman","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_sarranid_common_dress, itm_sarranid_common_dress_b,itm_woolen_hose,itm_sarranid_boots_a, itm_sarranid_felt_head_cloth, itm_sarranid_felt_head_cloth_b],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
  
#This troop is the troop marked as town_walkers_end and village_walkers_begin
 ["village_walker_1","Villager","Villagers",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_short_tunic, itm_linen_tunic, itm_coarse_tunic, itm_leather_vest, itm_leather_apron, itm_shirt, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_hide_boots, itm_ankle_boots, itm_leather_boots, itm_fur_hat, itm_leather_cap, itm_straw_hat, itm_felt_hat],
   def_attrib|level(4),wp(60),knows_common,man_face_younger_1, man_face_older_2],
 ["village_walker_2","Villager","Villagers",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_blue_dress, itm_dress, itm_woolen_dress, itm_peasant_dress, itm_woolen_hose, itm_blue_hose, itm_wimple_a, itm_wimple_with_veil, itm_female_hood],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],

#This troop is the troop marked as village_walkers_end and spy_walkers_begin
 ["spy_walker_1","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_short_tunic, itm_linen_tunic, itm_coarse_tunic, itm_tabard, itm_leather_vest, itm_robe, itm_leather_apron, itm_shirt, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_hide_boots, itm_ankle_boots, itm_leather_boots, itm_fur_hat, itm_leather_cap, itm_straw_hat, itm_felt_hat],
   def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_old_2],
 ["spy_walker_2","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_blue_dress, itm_dress, itm_woolen_dress, itm_peasant_dress, itm_woolen_hose, itm_blue_hose, itm_wimple_a, itm_wimple_with_veil, itm_female_hood],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
# Ryan END

#This troop is the troop marked as spy_walkers_end
# Zendar
  ["tournament_master","Tournament Master","Tournament Master",tf_hero, scn_zendar_center|entry(1),reserved,  fac_commoners,[itm_nomad_armor,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common,0x000000000008414401e28f534c8a2d09],
  ["trainer","Trainer","Trainer",tf_hero, scn_zendar_center|entry(2),reserved,  fac_commoners,[itm_leather_jerkin,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x00000000000430c701ea98836781647f],
  ["Constable_Hareck","Constable Hareck","Constable Hareck",tf_hero, scn_zendar_center|entry(5),reserved,  fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,0x00000000000c41c001fb15234eb6dd3f],

# Ryan BEGIN
  ["Ramun_the_slave_trader","Ramun, the slave trader","Ramun, the slave trader",tf_hero, no_scene,reserved, fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,0x0000000fd5105592385281c55b8e44eb00000000001d9b220000000000000000],

  ["guide","Quick Jimmy","Quick Jimmy",tf_hero, no_scene,0,  fac_commoners,[itm_coarse_tunic,itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x00000000000c318301f24e38a36e38e3],
# Ryan END

  ["Xerina","Xerina","Xerina",tf_hero|tf_female, scn_the_happy_boar|entry(5),reserved,  fac_commoners,[itm_leather_jerkin,itm_hide_boots],def_attrib|str_15|agi_15|level(39),wp(312),knows_power_strike_5|knows_ironflesh_5|knows_riding_6|knows_power_draw_4|knows_athletics_8|knows_shield_3,0x00000001ac0820074920561d0b51e6ed00000000001d40ed0000000000000000],
  ["Dranton","Dranton","Dranton",tf_hero, scn_the_happy_boar|entry(2),reserved,  fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|str_15|agi_14|level(42),wp(324),knows_power_strike_5|knows_ironflesh_7|knows_riding_4|knows_power_draw_4|knows_athletics_4|knows_shield_3,0x0000000a460c3002470c50f3502879f800000000001ce0a00000000000000000],
  ["Kradus","Kradus","Kradus",tf_hero, scn_the_happy_boar|entry(3),reserved,  fac_commoners,[itm_padded_leather,itm_hide_boots],def_attrib|str_15|agi_14|level(43),wp(270),knows_power_strike_5|knows_ironflesh_7|knows_riding_4|knows_power_draw_4|knows_athletics_4|knows_shield_3,0x0000000f5b1052c61ce1a9521db1375200000000001ed31b0000000000000000],


#Tutorial
  ["tutorial_trainer","Training Ground Master","Training Ground Master",tf_hero, 0, 0, fac_commoners,[itm_robe,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common,0x000000000008414401e28f534c8a2d09],
  ["tutorial_student_1","{!}tutorial_student_1","{!}tutorial_student_1",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_sword, itm_practice_shield, itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_ankle_boots,itm_padded_coif,itm_footman_helmet],
   def_attrib|level(2),wp(20),knows_common, swadian_face_young_1, swadian_face_old_2],
  ["tutorial_student_2","{!}tutorial_student_2","{!}tutorial_student_2",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_sword, itm_practice_shield, itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_ankle_boots,itm_padded_coif,itm_footman_helmet],
   def_attrib|level(2),wp(20),knows_common, swadian_face_young_1, swadian_face_old_2],
  ["tutorial_student_3","{!}tutorial_student_3","{!}tutorial_student_3",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_staff, itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_ankle_boots,itm_padded_coif,itm_footman_helmet],
   def_attrib|level(2),wp(20),knows_common, swadian_face_young_1, swadian_face_old_2],
  ["tutorial_student_4","{!}tutorial_student_4","{!}tutorial_student_4",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_staff, itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_ankle_boots,itm_padded_coif,itm_footman_helmet],
   def_attrib|level(2),wp(20),knows_common, swadian_face_young_1, swadian_face_old_2],

#Sargoth
  #halkard, hardawk. lord_taucard lord_caupard. lord_paugard

#Salt mine
  ["Galeas","Galeas","Galeas",tf_hero, 0, reserved, fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,0x000000000004718201c073191a9bb10c],

#Dhorak keep

  ["farmer_from_bandit_village","Farmer","Farmers",tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_linen_tunic,itm_coarse_tunic,itm_shirt,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_older_2],

  ["trainer_1","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_1|entry(6),reserved,  fac_commoners,[itm_leather_jerkin,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000d0d1030c74ae8d661b651c6840000000000000e220000000000000000],
  ["trainer_2","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_2|entry(6),reserved,  fac_commoners,[itm_nomad_vest,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000e5a04360428ec253846640b5d0000000000000ee80000000000000000],
  ["trainer_3","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_3|entry(6),reserved,  fac_commoners,[itm_padded_leather,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000e4a0445822ca1a11ab1e9eaea0000000000000f510000000000000000],
  ["trainer_4","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_4|entry(6),reserved,  fac_commoners,[itm_leather_jerkin,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000e600452c32ef8e5bb92cf1c970000000000000fc20000000000000000],
  ["trainer_5","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_5|entry(6),reserved,  fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000e77082000150049a34c42ec960000000000000e080000000000000000],

# Ransom brokers.
  ["ransom_broker_1","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_2","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_tabard,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_3","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_4","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_short_tunic,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_5","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_gambeson,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_6","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_blue_gambeson,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_7","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_red_gambeson,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_8","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_9","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_10","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],

# Tavern traveler.
  ["tavern_traveler_1","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_2","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_tabard,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_3","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_4","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_blue_gambeson,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_5","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_short_tunic,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_6","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_7","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_8","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_tabard,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_9","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_10","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],

# Tavern traveler.
  ["tavern_bookseller_1","Book_Merchant","Book_Merchant",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots,
               itm_book_tactics, itm_book_persuasion, itm_book_wound_treatment_reference, itm_book_leadership, 
               itm_book_intelligence, itm_book_training_reference, itm_book_surgery_reference],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_bookseller_2","Book_Merchant","Book_Merchant",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots,
               itm_book_wound_treatment_reference, itm_book_leadership, itm_book_intelligence, itm_book_trade, 
               itm_book_engineering, itm_book_weapon_mastery],def_attrib|level(5),wp(20),knows_common,merchant_face_1, merchant_face_2],

# Tavern minstrel.
  ["tavern_minstrel_1","Wandering Minstrel","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_leather_jacket, itm_hide_boots, itm_lute],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2], #lute
  ["tavern_minstrel_2","Wandering Bard","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_tunic_with_green_cape, itm_hide_boots, itm_lyre],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],  #early harp/lyre
  ["tavern_minstrel_3","Wandering Ashik","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_nomad_robe, itm_hide_boots, itm_lute],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2], #lute/oud or rebab
  ["tavern_minstrel_4","Wandering Skald","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_fur_coat, itm_hide_boots, itm_lyre],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2], #No instrument or lyre
  ["tavern_minstrel_5","Wandering Troubadour","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_short_tunic, itm_hide_boots, itm_lute],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2], #Lute or Byzantine/Occitan lyra
  
#NPC system changes begin
#Companions
  ["kingdom_heroes_including_player_begin",  "kingdom_heroes_including_player_begin",  "kingdom_heroes_including_player_begin",  tf_hero, 0,reserved,  fac_kingdom_1,[],          lord_attrib,wp(220),knows_lord_1, 0x000000000010918a01f248377289467d],

  ["npc1","Borcha","Borcha",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_khergit_armor,itm_nomad_boots,itm_knife],
   str_8|agi_7|int_12|cha_7|level(3),wp(60),knows_tracker_npc|
   knows_ironflesh_1|knows_power_strike_1|knows_pathfinding_3|knows_athletics_2|knows_tracking_1|knows_riding_2, #skills 2/3 player at that level
   0x00000004bf086143259d061a9046e23500000000001db52c0000000000000000],
  ["npc2","Marnid","Marnid", tf_hero|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,[itm_linen_tunic,itm_hide_boots,itm_club],
   str_7|agi_7|int_11|cha_6|level(1),wp(40),knows_merchant_npc|
   knows_trade_2|knows_weapon_master_1|knows_ironflesh_1|knows_wound_treatment_1|knows_athletics_2|knows_first_aid_1|knows_leadership_1,
   0x000000019d004001570b893712c8d28d00000000001dc8990000000000000000],
  ["npc3","Ymira","Ymira",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_dress,itm_woolen_hose,itm_knife],
   str_6|agi_9|int_11|cha_6|level(1),wp(20),knows_merchant_npc|
   knows_wound_treatment_1|knows_trade_1|knows_first_aid_3|knows_surgery_1|knows_athletics_1|knows_riding_1,
   0x0000000083040001583b6db8dec5925b00000000001d80980000000000000000],
  ["npc4","Rolf","Rolf",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_leather_jerkin,itm_nomad_boots, itm_sword_medieval_a],
   str_10|agi_9|int_13|cha_10|level(10),wp(110),knows_warrior_npc|
   knows_weapon_master_2|knows_power_strike_2|knows_riding_2|knows_athletics_2|knows_power_throw_2|knows_first_aid_1|knows_surgery_1|knows_tactics_2|knows_leadership_2,
   0x000000057f1074002c75c6a8a58ad72e00000000001e1a890000000000000000],
  ["npc5","Baheshtur","Baheshtur",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_nomad_vest,itm_nomad_boots, itm_sword_khergit_1],
   str_9|agi_9|int_12|cha_7|level(5),wp(90),knows_warrior_npc|
   knows_riding_2|knows_horse_archery_3|knows_power_draw_3|knows_leadership_2|knows_weapon_master_1,
   0x000000088910318b5c6f972328324a6200000000001cd3310000000000000000],
  ["npc6","Firentis","Firentis",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_tabard,itm_nomad_boots, itm_sword_medieval_a],
   str_10|agi_12|int_10|cha_5|level(6),wp(105),knows_warrior_npc|
   knows_riding_2|knows_weapon_master_2|knows_power_strike_2|knows_athletics_3|knows_trainer_1|knows_leadership_1,
  0x00000002050052036a1895d0748f3ca30000000000000f0b0000000000000000],
  ["npc7","Deshavi","Deshavi",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_ragged_outfit,itm_wrapping_boots, itm_hunting_bow, itm_arrows, itm_quarter_staff],
   str_8|agi_9|int_10|cha_6|level(2),wp(80),knows_tracker_npc|
   knows_tracking_2|knows_athletics_2|knows_spotting_1|knows_pathfinding_1|knows_power_draw_2,
   0x00000001fc08400533a15297634d44f400000000001e02db0000000000000000],
  ["npc8","Matheld","Matheld",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_tribal_warrior_outfit,itm_nomad_boots, itm_sword_viking_1],
   str_9|agi_10|int_9|cha_10|level(7),wp(90),knows_warrior_npc|
   knows_weapon_master_3|knows_power_strike_2|knows_athletics_2|knows_leadership_3|knows_tactics_1,
   0x00000005800c000637db8314e331e76e00000000001c46db0000000000000000],
  ["npc9","Alayen","Alayen",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_tabard,itm_nomad_boots, itm_sword_medieval_b_small],
   str_11|agi_8|int_7|cha_8|level(2),wp(100),knows_warrior_npc|
   knows_weapon_master_1|knows_riding_1|knows_athletics_1|knows_leadership_1|knows_tactics_1|knows_power_strike_1,
   0x000000030100300f499d5b391b6db8d300000000001dc2e10000000000000000],
  ["npc10","Bunduk","Bunduk",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_padded_leather,itm_nomad_boots, itm_crossbow, itm_bolts, itm_pickaxe],
   str_12|agi_8|int_9|cha_11|level(9),wp(105),knows_warrior_npc|
   knows_weapon_master_3|knows_tactics_1|knows_leadership_1|knows_ironflesh_3|knows_trainer_2|knows_first_aid_2,
   0x0000000a3f081006572c91c71c8d46cb00000000001e468a0000000000000000],
  ["npc11","Katrin","Katrin",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_leather_apron, itm_falchion, itm_wrapping_boots],
   str_8|agi_11|int_10|cha_10|level(8),wp(70),knows_merchant_npc|
   knows_weapon_master_1|knows_first_aid_1|knows_wound_treatment_2|knows_ironflesh_3|knows_inventory_management_5,
   0x0000000d7f0400035915aa226b4d975200000000001ea49e0000000000000000],
  ["npc12","Jeremus","Jeremus",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_pilgrim_disguise,itm_nomad_boots, itm_staff],
   str_8|agi_7|int_13|cha_7|level(4),wp(30),   knows_merchant_npc|
   knows_ironflesh_1|knows_power_strike_1|knows_surgery_4|knows_wound_treatment_3|knows_first_aid_3,
   0x000000078000500e4f8ba62a9cd5d36d00000000001e36250000000000000000],
  ["npc13","Nizar","Nizar",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_nomad_robe,itm_nomad_boots, itm_scimitar, itm_courser],
   str_7|agi_7|int_12|cha_8|level(3),wp(80),knows_warrior_npc|
   knows_riding_2|knows_leadership_2|knows_athletics_2|knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_1,
   0x00000004bf0475c85f4e9592de4e574c00000000001e369c0000000000000000],
  ["npc14","Lezalit","Lezalit",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_nobleman_outfit,itm_nomad_boots, itm_sword_medieval_b_small],
   str_9|agi_8|int_11|cha_8|level(5),wp(100),knows_warrior_npc|
   knows_trainer_4|knows_weapon_master_3|knows_leadership_2|knows_power_strike_1,
   0x00000001a410259144d5d1d6eb55e96a00000000001db0db0000000000000000],
  ["npc15","Artimenner","Artimenner",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_rich_outfit,itm_nomad_boots, itm_sword_medieval_b_small],
   str_9|agi_9|int_12|cha_8|level(7),wp(80),knows_warrior_npc|
   knows_tactics_2|knows_engineer_4|knows_trade_3|knows_tracking_1|knows_spotting_1,
   0x0000000f2e1021862b4b9123594eab5300000000001d55360000000000000000],
  ["npc16","Klethi","Klethi",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_peasant_dress,itm_nomad_boots, itm_dagger, itm_throwing_knives],
   str_7|agi_11|int_8|cha_7|level(2),wp(80),knows_tracker_npc|
   knows_power_throw_3|knows_athletics_2|knows_power_strike_1,
   0x00000000000c100739ce9c805d2f381300000000001cc7ad0000000000000000],
#NPC system changes end

# Special NPCs
  ["quartermaster","Quartermaster","Quartermaster",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_leather_jerkin,itm_hide_boots,itm_club],
    str_7|agi_7|int_7|cha_7|level(1),wp(40),knows_common,swadian_face_older_2,swadian_face_old_2],

#governers olgrel rasevas                                                                        Horse          Bodywear                Footwear_in                     Footwear_out                    Armor                       Weapon                  Shield                  Headwaer
  ["kingdom_1_lord",  "King Chamond II",  "Chamond",  tf_hero, 0,reserved,  fac_kingdom_1,[itm_m_swadia_lord_horse_a,   itm_rich_outfit,        itm_blue_hose,                  itm_mt_greaves_g,               itm_m_swadia_elite_knight_armor_e_cloaked, itm_mt_gauntlets_a,    itm_german_bastard_sword,      itm_shield_heater_d,       itm_mt_full_helm_f],          knight_attrib_5,wp(220),knight_skills_5|knows_trainer_5, 0x0000000f6d10244606db6db6db6dcafe00000000001db8fb0000000000000000,swadian_face_older_2],
  ["kingdom_2_lord",  "King Zbosek Jasnyi",  "Zbosek",  tf_hero, 0,reserved,  fac_kingdom_2,[itm_northerner_horse_hunter,    itm_courtly_outfit,      itm_leather_boots,              itm_mt_greaves_f,              itm_vaegir_elite_armor, itm_mt_gauntlets_a,      itm_german_bastard_sword,      itm_shield_kite_k,      itm_m_vaegir_litchina_helm, itm_great_bardiche],    knight_attrib_5,wp(220),knight_skills_5|knows_trainer_5, 0x0000000ec804450506db6db6db6ddb7f00000000001db6fb0000000000000000, vaegir_face_old_2],
  ["kingdom_3_lord",  "Damdu Khan",  "Damdu",  tf_hero, 0,reserved,  fac_kingdom_3,[itm_mt_horse_a2,   itm_nomad_robe,             itm_leather_boots,              itm_m_greaves_a,           itm_m_lancer_heavy_elite_a,  itm_mt_scale_gloves_a,       itm_ms_strange_sword,              itm_ms_doom,       itm_m_lancer_helmet_heavy_a],      knight_attrib_5,wp(220),knight_skills_5|knows_trainer_6, 0x0000000e400c529014c56db6db6dffff00000000001f76f80000000000000000,khergit_face_old_2],
  ["kingdom_4_lord",  "King Ognvar Vidison",  "Ognvar Vidison",  tf_hero, 0,reserved,  fac_kingdom_4,[itm_hunter,    itm_nobleman_outfit,    itm_leather_boots,              itm_mt_greaves_a,                 itm_cuir_bouilli_with_pelt,  itm_mt_scale_gloves_b,    itm_war_axe,           itm_tab_shield_round_e,    itm_ms_gjermundbu_helm_a, itm_one_handed_war_axe_a],            knight_attrib_5,wp(220),knight_skills_5|knows_trainer_5, 0x0000000e000c2191061b6ddde3227fff00000000001d033b0000000000000000, nord_face_older_2],
  ["kingdom_5_lord",  "King Graveth III",  "Graveth",  tf_hero, 0,reserved,  fac_kingdom_5,[itm_warhorse,  itm_tabard,             itm_leather_boots,              itm_mt_greaves_a,   itm_m_churburg_d,  itm_m_gauntlets_a,         itm_crusader_sword,         itm_shield_heater_d,        itm_m_tower_helm_b],         knight_attrib_5,wp(220),knight_skills_4|knows_trainer_5, 0x0000000eff10231106a46dda936dff3c00000000001fb63b0000000000000000, rhodok_face_old_2],
  ["kingdom_6_lord",  "Sultan Iman",  "Iman",  tf_hero, 0,reserved,  fac_kingdom_6,[itm_saracen_horse_sultan,     itm_mkk_sultan_armor,          itm_mkk_heavy_boots_b,       itm_mkk_sultan_helmet_a,  itm_mkk_gloves_c,      itm_sarranid_mace_1,    itm_maa_camel_rider_shield_f],         knight_attrib_4,wp(220),knight_skills_5|knows_trainer_5, 0x0000000a7f10311416db6ddedb6ddb6e00000000001dc6f90000000000000000, rhodok_face_old_2],
  ["kingdom_7_lord", "King Marko", "Marko", tf_hero, 0, reserved, fac_kingdom_7,[itm_mt_horse_b3, itm_tabard, itm_m_hose_a, itm_m_greaves_a, itm_m_brigandine_a, itm_m_gauntlets_b, itm_longsword, itm_steel_shield, itm_m_sallet_black_a, itm_jarid, itm_heavy_lance],knight_attrib_5,wp(350),knight_skills_5|knows_trainer_5|knows_ironflesh_10, 0x0000000eff10414936db6db6db6e3b7500000000001db6db0000000000000000,swadian_face_older_2],
  ["kingdom_8_lord", "Red Demon Hairako", "Hairako", tf_hero, 0, reserved, fac_kingdom_8,[itm_mh_horse_a, itm_tabard, itm_khergit_leather_boots, itm_mt_scale_gloves_a, itm_mh_armor_heavy_a, itm_mh_helmet_heavy_a, itm_javelin, itm_mh_spear_a, itm_plate_covered_round_shield, itm_mh_sword_a],knight_attrib_5,wp(350),knight_skills_5|knows_trainer_5|knows_ironflesh_10|knows_riding_10|knows_power_throw_10, 0x0000000e001051c736db6db6db6e3b7500000000001db6db0000000000000000,swadian_face_older_2],
  ["kingdom_9_lord", "King Anastas", "Anastas", tf_hero, 0, reserved, fac_kingdom_9,[itm_m_hose_b, itm_rich_outfit, itm_mt_greaves_g, itm_mt_heavy_plate_b, itm_mt_gauntlets_a, itm_mt_knight_helm_c, itm_mt_horse_b3, itm_great_lance, itm_shield_heater_d, itm_crusader_sword],knight_attrib_5,wp(350),knight_skills_5|knows_trainer_5|knows_ironflesh_10|knows_riding_10, 0x0000000e9310428636db6df8eb0dfd7500000000001db6db0000000000000000,swadian_face_older_2],
  ["kingdom_10_lord", "King Asmadias", "Asmadias", tf_hero, 0, reserved, fac_kingdom_10,[itm_m_hose_b, itm_mt_coat_a, itm_mt_greaves_a, itm_mt_special_c, itm_m_gauntlets_b, itm_mt_armet_a2, itm_mt_horse_a, itm_tab_shield_kite_d, itm_side_sword, itm_danish_greatsword],knight_attrib_5,wp(425),knight_skills_5|knows_trainer_5|knows_ironflesh_10, 0x0000000e801015c036db6db6db6e5d7f00000000001db6db0000000000000000,swadian_face_older_2],
  ["kingdom_11_lord", "Sultan Zahir al-Adid", "Zahir", tf_hero, 0, reserved, fac_kingdom_11,[itm_warhorse_sarranid,     itm_ms_armor_mamluke, itm_m_greaves_a, itm_maa_cavalry_a, itm_mt_gauntlets_b, itm_ms_flat_sword, itm_maa_camel_rider_shield_f, itm_lance],knight_attrib_5,wp(425),knight_skills_5|knows_trainer_5|knows_ironflesh_10, 0x0000000fff04644436db6db7d76dfced00000000001db6eb0000000000000000,swadian_face_older_2],
  ["kingdom_12_lord", "King Darius Stormbane", "Darius", tf_hero, 0, reserved, fac_kingdom_12,[itm_hunter,    itm_nobleman_outfit, itm_leather_boots, itm_mt_greaves_g, itm_ms_coat_of_plates_b, itm_mt_scale_gloves_a, itm_german_poleaxe, itm_ms_plain_shield_a, itm_grosse_messer_b, itm_ms_facemask_elite],knight_attrib_5,wp(350),knight_skills_5|knows_trainer_5|knows_ironflesh_10|knows_riding_10, 0x0000000e800441d236c36c379a6dff3f00000000001dc93b0000000000000000,swadian_face_older_2],

#    Imbrea   Belinda Ruby Qaelmas Rose    Willow 
#  Alin  Ganzo            Zelka Rabugti
#  Qlurzach Ruhbus Givea_alsev  Belanz        Bendina  
# Dunga        Agatha     Dibus Crahask
  
#                                                                               Horse                   Bodywear                Armor                               Footwear_in                 Footwear_out                        Headwear                    Weapon               Shield
  #Swadian civilian clothes: itm_courtly_outfit itm_gambeson itm_blue_gambeson itm_red_gambeson itm_nobleman_outfit itm_rich_outfit itm_short_tunic itm_tabard
  #Older knights with higher skills moved to top
  ["knight_1_1", "Count Gileon", "Gileon", tf_hero, 0, reserved,  fac_kingdom_1, [itm_m_swadia_elite_horse_c,   itm_rich_outfit,itm_blue_hose,itm_mt_greaves_a,itm_m_swadia_elite_knight_armor_b_cloaked, itm_m_gauntlets_a,    itm_longsword,itm_shield_heater_d,itm_mt_full_helm_e],   knight_attrib_5,wp(230),knight_skills_5|knows_trainer_1|knows_trainer_3, 0x0000000efe086192149e6cc71b6dff3f00000000001cd4f90000000000000000, swadian_face_older_2],
  ["knight_1_2", "Count Ander", "Ander", tf_hero, 0, reserved,  fac_kingdom_1, [itm_m_swadia_elite_horse_c,   itm_rich_outfit,itm_blue_hose,itm_mt_greaves_b,itm_m_swadia_elite_knight_armor_b_cloaked, itm_m_gauntlets_b,    itm_sarranid_mace_1,itm_shield_heater_d,itm_m_knigh_helm_f],       knight_attrib_5,wp(240),knight_skills_5, 0x0000000fb80064c004db6e355c6decff00000000001e26f80000000000000000, swadian_face_young_2],
  ["knight_1_3", "Count Wilhye Balley", "Wilhye Balley", tf_hero, 0, reserved,  fac_kingdom_1, [itm_m_swadia_elite_horse_a,   itm_rich_outfit,itm_blue_hose,itm_mt_greaves_a,itm_m_swadia_elite_knight_armor_a_cloaked, itm_m_gauntlets_b,    itm_crusader_sword,itm_shield_heater_d,itm_m_sergant_helmet_a],  knight_attrib_5,wp(260),knight_skills_5|knows_trainer_3, 0x0000000bbe0c428516db6db6db6dffff00000000001db6f90000000000000000, swadian_face_young_2],
  ["knight_1_4", "Count Rewis Bailey", "Rewis Bailey", tf_hero, 0, reserved,  fac_kingdom_1, [itm_m_swadia_elite_horse_b,   itm_rich_outfit,itm_blue_hose,itm_m_greaves_a,itm_m_swadia_elite_knight_armor_d_cloaked, itm_m_gauntlets_a,    itm_german_bastard_sword,itm_shield_heater_d,itm_m_knigh_helm_a],    knight_attrib_5,wp(180),knight_skills_5|knows_trainer_4, 0x0000000b3000101436db6db6db6ddd6e00000000001db6db0000000000000000, swadian_face_older_2],
  ["knight_1_5", "Count Chiles", "Chiles", tf_hero, 0, reserved,  fac_kingdom_1, [itm_m_swadia_elite_horse_a,   itm_rich_outfit,itm_blue_hose,itm_m_greaves_b,itm_m_swadia_elite_knight_armor_f_cloaked, itm_m_gauntlets_a,    itm_german_bastard_sword,itm_shield_heater_d,itm_m_knigh_helm_b],      knight_attrib_4,wp(200),knight_skills_4|knows_trainer_6, 0x0000000d7f00329136db6db6db6dfeff00000000001db6fb0000000000000000, swadian_face_older_2],
  ["knight_1_6", "Count Drobert", "Drobert", tf_hero, 0, reserved,  fac_kingdom_1, [itm_m_swadia_elite_horse_a,   itm_rich_outfit,itm_blue_hose,itm_m_greaves_a,itm_m_swadia_elite_sergant_armor_a, itm_m_gauntlets_a,    itm_grosse_messer_b,itm_shield_heater_d,itm_m_knigh_helm_f], knight_attrib_5,wp(240),knight_skills_4|knows_trainer_4, 0x0000000e3f08034920db6db6db6dfeff00000000001de6f80000000000000000, swadian_face_older_2],
  ["knight_1_7", "Count Richye Bexley", "Richye Bexley", tf_hero, 0, reserved,  fac_kingdom_1, [itm_m_swadia_elite_horse_a,   itm_rich_outfit,itm_blue_hose,itm_m_greaves_a,itm_m_swadia_elite_knight_armor_c, itm_m_gauntlets_a,    itm_danish_greatsword,itm_shield_heater_d,itm_irish_sword,itm_m_swadia_elite_helmet_c], knight_attrib_5,wp(290),knight_skills_4|knows_trainer_4, 0x0000000e4000354436db6db6db6dfeff00000000001dd6fb0000000000000000, swadian_face_young_2],
  ["knight_1_8", "Count Rancent", "Rancent", tf_hero, 0, reserved,  fac_kingdom_1, [itm_m_swadia_elite_horse_b,   itm_rich_outfit,itm_blue_hose,itm_mt_mail_boots_a,itm_m_swadia_elite_knight_armor_f_cloaked, itm_m_gauntlets_b,    itm_german_bastard_sword,itm_shield_heater_d,itm_ms_flamberg_great,itm_m_knigh_helm_b],  knight_attrib_4,wp(250),knight_skills_4, 0x0000000fb308349431db6db6db6dfeff00000000001fd6fb0000000000000000, swadian_face_older_2],

#Swadian younger knights  
  ["knight_1_9", "Count Ethes Tere", "Ethes Tere", tf_hero, 0, reserved,  fac_kingdom_1, [itm_m_swadia_heavy_horse_c,   itm_rich_outfit,itm_blue_hose,itm_mt_mail_boots_a,itm_m_swadia_knight_armor_b, itm_m_gauntlets_b,    itm_crusader_sword,itm_shield_kite_k,itm_m_cavalry_helmet_g],    knight_attrib_3,wp(160),knight_skills_3, 0x000000032b0c450f20c7b1b6db6dfeff00000000001c76f80000000000000000, swadian_face_old_2],
  ["knight_1_10", "Count Sterey Moore", "Sterey Moore", tf_hero, 0, reserved,  fac_kingdom_1, [itm_m_swadia_heavy_horse_a,   itm_rich_outfit,itm_blue_hose,itm_m_greaves_a,itm_m_swadia_knight_armor_b_cloaked, itm_m_gloves_a,    itm_italian_falchion,itm_shield_heater_d,itm_m_crusader_helm_f],   knight_attrib_3,wp(190),knight_skills_3, 0x0000000e4a0c634612e46edd29577eff00000000001c57380000000000000000, swadian_face_older_2],
  ["knight_1_11", "Count Gery Yourner", "Gery Yourner", tf_hero, 0, reserved,  fac_kingdom_1, [itm_m_swadia_heavy_horse_a,   itm_rich_outfit,itm_blue_hose,itm_mt_greaves_c,itm_m_swadia_knight_armor_a_cloaked, itm_leather_gloves,    itm_english_longsword,itm_shield_heater_d,itm_m_cavalry_helmet_f],       knight_attrib_3,wp(220),knight_skills_3, 0x0000000e540c259416936ea8e3adffbf00000000001e44fd0000000000000000, swadian_face_older_2],
  ["knight_1_12", "Count Symas Gelnne", "Symas Gelnne", tf_hero, 0, reserved,  fac_kingdom_1, [itm_m_swadia_heavy_horse_c,   itm_rich_outfit,itm_blue_hose,itm_mt_mail_boots_a,itm_m_swadia_knight_armor_a, itm_m_gauntlets_a,    itm_military_pick,itm_shield_kite_k,itm_m_cavalry_helmet_a],    knight_attrib_3,wp(130),knight_skills_3, 0x000000003f082286201b6db6db6dfefe00000000001e76f80000000000000000, swadian_face_older_2],
  ["knight_1_13", "Count Finy", "Finy", tf_hero, 0, reserved,  fac_kingdom_1, [itm_m_swadia_heavy_horse_c,   itm_rich_outfit,itm_blue_hose,itm_mt_leather_boots_e,itm_m_swadia_knight_armor_c, itm_m_gauntlets_b,    itm_morningstar,itm_shield_heater_d,itm_m_cavalry_helmet_b],   knight_attrib_2,wp(160),knight_skills_2, 0x00000000170833c520db6db6db6dfefe00000000001c56f80000000000000000, swadian_face_older_2],
  ["knight_1_14", "Count Froguy Warre", "Froguy Warre", tf_hero, 0, reserved,  fac_kingdom_1, [itm_m_swadia_heavy_horse_c,   itm_rich_outfit,itm_blue_hose,itm_m_swadia_leather_boots_b,itm_m_swadia_knight_armor_b, itm_m_gauntlets_a,    itm_crusader_sword,itm_shield_kite_k,itm_m_cavalry_helmet_e],    knight_attrib_2,wp(190),knight_skills_3|knows_trainer_6, 0x000000001708648021036db6db6dfefe00000000001df6380000000000000000, swadian_face_older_2],
  ["knight_1_15", "Count James", "James", tf_hero, 0, reserved,  fac_kingdom_1, [itm_m_swadia_heavy_horse_a,   itm_rich_outfit,itm_blue_hose,itm_mt_mail_boots_a,itm_m_swadia_sergant_armor_b, itm_m_gauntlets_b,    itm_irish_sword,itm_shield_kite_k,itm_m_cavalry_helmet_g,itm_crossbow, itm_bolts],      knight_attrib_4,wp(140),knight_skills_2, 0x00000000170804c736db6db6db6dbf3c00000000001db6ff0000000000000000, swadian_face_young_2],
  ["knight_1_16", "Count Gerey", "Gerey", tf_hero, 0, reserved,  fac_kingdom_1, [itm_m_swadia_heavy_horse_c,   itm_rich_outfit,itm_blue_hose,itm_mt_mail_boots_a,itm_m_swadia_knight_armor_b, itm_m_gauntlets_b,    itm_crusader_sword,itm_shield_heater_d,itm_m_knigh_helm_e],   knight_attrib_1,wp(130),knight_skills_2, 0x0000000ebf08251106db6dbe9b6dbf3c00000000001df6f80000000000000000, swadian_face_young_2],
  ["knight_1_17", "Count Arthur", "Arthur", tf_hero, 0, reserved,  fac_kingdom_1, [itm_m_swadia_heavy_horse_b,   itm_rich_outfit,itm_blue_hose,itm_m_swadia_leather_boots_b,itm_m_swadia_knight_armor_a, itm_m_gauntlets_b,itm_longsword,itm_shield_kite_k,itm_m_infantry_helmet_e],    knight_attrib_2,wp(190),knight_skills_1|knows_trainer_4, 0x000000019a0061543a4d44a8eb6edf3f00000000001d477d0000000000000000, swadian_face_young_2],
  ["knight_1_18", "Count Stiny Seve", "Stiny Seve", tf_hero, 0, reserved,  fac_kingdom_1, [itm_m_swadia_heavy_horse_c,   itm_rich_outfit,itm_blue_hose,itm_m_swadia_leather_boots_a,itm_m_swadia_knight_armor_b, itm_mt_scale_gloves_a,itm_lance,   itm_crusader_sword,itm_shield_kite_g,itm_m_cavalry_helmet_e],   knight_attrib_3,wp(210),knight_skills_1, 0x00000001a70c32c836db6db6db6dfefb00000000001db6fb0000000000000000, swadian_face_young_2],
  ["knight_1_19", "Count Edward", "Edward", tf_hero, 0, reserved,  fac_kingdom_1, [itm_m_swadia_heavy_horse_c,   itm_rich_outfit,itm_blue_hose,itm_mt_mail_boots_a,itm_m_swadia_knight_armor_c, itm_m_gauntlets_b,    itm_side_sword,itm_shield_kite_k,itm_bec_de_corbin,itm_m_cavalry_helmet_c],    knight_attrib_1,wp(120),knight_skills_1, 0x00000001be1035c636db6db7db6deb6d00000000001dd6f30000000000000000, swadian_face_young_2],
  ["knight_1_20", "Count Wilhye", "Wilhye", tf_hero, 0, reserved,  fac_kingdom_1, [itm_m_swadia_heavy_horse_c,   itm_rich_outfit,itm_blue_hose,itm_m_leather_boots_a,itm_m_swadia_sergant_armor_b, itm_m_gloves_a,    itm_irish_sword,itm_shield_kite_k,itm_m_light_infantry_helmet_e],   knight_attrib_2,wp(150),knight_skills_1, 0x00000001be1040c536db6dbd1b6deb6d00000000001dd6f30000000000000000, swadian_face_young_2],



  ["knight_2_1", "Boyar Vacla", "Vacla", tf_hero, 0, reserved,  fac_kingdom_2, [itm_northerner_horse_black,itm_fur_coat,itm_vaegir_elite_armor,itm_nomad_boots,itm_m_vaegir_nikolskoe_helm,itm_m_vaegir_rus_splint_greaves,    itm_mt_scale_gloves_a,itm_bardiche, itm_mace_3,itm_norman_shield_1],    knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x0000000cda1021c506db6db6db6dffbe00000000001db6ea0000000000000000, vaegir_face_middle_2],
  ["knight_2_2", "Boyar Zita", "Zita", tf_hero, 0, reserved,  fac_kingdom_2, [itm_northerner_horse_hunter,itm_fur_coat,itm_m_vaegir_rus_scale,itm_nomad_boots,itm_m_vaegir_nikolskoe_helm,itm_m_vaegir_rus_splint_greaves,    itm_mt_scale_gloves_a,itm_bardiche, itm_mace_3,itm_norman_shield_1],    knight_attrib_2,wp(160),knight_skills_2, 0x0000000cc004329236db6db6db6dbfff00000000001db6fb0000000000000000, vaegir_face_old_2],
  ["knight_2_3", "Boyar Besla", "Besla", tf_hero, 0, reserved,  fac_kingdom_2, [itm_northerner_horse_black,itm_fur_coat,itm_vaegir_elite_armor,itm_nomad_boots,itm_splinted_leather_greaves,itm_m_vaegir_rus_splint_greaves,    itm_mail_mittens,itm_war_axe, itm_one_handed_war_axe_a,itm_norman_shield_1],     knight_attrib_3,wp(190),knight_skills_3, 0x0000000cc004128906db6db92b6dffff00000000001e46f90000000000000000, vaegir_face_older_2],
  ["knight_2_4", "Boyar Mira", "Mira", tf_hero, 0, reserved,  fac_kingdom_2, [itm_northerner_horse_black,itm_fur_coat,itm_m_vaegir_rus_scale,itm_nomad_boots,itm_splinted_leather_greaves,itm_m_vaegir_rus_splint_greaves,    itm_mail_mittens,itm_war_axe, itm_one_handed_battle_axe_a,itm_norman_shield_1],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000ca40403d320047279ef6dcfbf00000000001ec6f90000000000000000, vaegir_face_older_2],
  ["knight_2_5", "Boyar Bisla", "Bisla", tf_hero, 0, reserved,  fac_kingdom_2, [itm_northerner_horse_black,itm_fur_coat,itm_m_vaegir_rus_lamellar_b,itm_nomad_boots,itm_splinted_leather_greaves,itm_m_vaegir_rus_splint_greaves,    itm_mail_mittens,itm_bardiche, itm_one_handed_war_axe_b,itm_norman_shield_1],       knight_attrib_5,wp(250),knight_skills_5, 0x0000000cb50411d406db6db71b6d9edf00000000001d36e30000000000000000, vaegir_face_older_2],
  ["knight_2_6", "Boyar Rivoi", "Rivoi", tf_hero, 0, reserved,  fac_kingdom_2, [itm_northerner_horse_black,itm_fur_coat,itm_m_vaegir_rus_scale,itm_nomad_boots,itm_splinted_leather_greaves,itm_m_vaegir_rus_splint_greaves,    itm_mail_mittens,itm_war_axe, itm_one_handed_battle_axe_b,itm_norman_shield_1],   knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x0000000c8600334520d36dd1116f1f3f00000000001db8fb0000000000000000, vaegir_face_middle_2],
  ["knight_2_7", "Boyar Bora", "Bora", tf_hero, 0, reserved,  fac_kingdom_2, [itm_northerner_horse_black,itm_fur_coat,itm_vaegir_elite_armor,itm_nomad_boots,itm_splinted_leather_greaves,itm_m_vaegir_rus_splint_greaves,    itm_mail_mittens,itm_great_bardiche, itm_one_handed_battle_axe_a,itm_norman_shield_1],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x0000000c800422cd22db69c75b88cfcf00000000001c46ba0000000000000000, vaegir_face_old_2],
  ["knight_2_8", "Boyar Bohda", "Bohda", tf_hero, 0, reserved,  fac_kingdom_2, [itm_northerner_horse_black,itm_fur_coat,itm_m_vaegir_rus_scale,itm_nomad_boots,itm_splinted_leather_greaves,itm_m_vaegir_rus_splint_greaves,    itm_mail_mittens,itm_war_axe, itm_one_handed_war_axe_a,itm_norman_shield_1],    knight_attrib_3,wp(200),knight_skills_3|knows_trainer_5, 0x00000004cb1015c6075c6d39686dbeff00000000001db6fb0000000000000000, vaegir_face_older_2],
  ["knight_2_9", "Boyar Rosta", "Rosta", tf_hero, 0, reserved,  fac_kingdom_2, [itm_northerner_horse_black,itm_fur_coat,itm_m_vaegir_rus_lamellar_a,itm_nomad_boots,itm_splinted_leather_greaves,itm_m_vaegir_rus_cav_boots,    itm_mail_mittens,itm_war_axe, itm_one_handed_war_axe_b,itm_norman_shield_1],    knight_attrib_4,wp(230),knight_skills_4, 0x00000004cb10354736db6db6db6ddaee00000000001db6db0000000000000000, vaegir_face_older_2],
  ["knight_2_10", "Boyar Rosla", "Rosla", tf_hero, 0, reserved,  fac_kingdom_2, [itm_northerner_horse_black,itm_fur_coat,itm_m_vaegir_rus_scale,itm_nomad_boots,itm_splinted_leather_greaves,itm_m_vaegir_rus_splint_greaves,    itm_mail_mittens,itm_war_axe, itm_mace_4,itm_norman_shield_1],      knight_attrib_5,wp(260),knight_skills_5|knows_trainer_6, 0x00000004eb0412d106db6db8ab6deede00000000001db6b00000000000000000, vaegir_face_older_2],
  ["knight_2_11", "Boyar Mira", "Mira", tf_hero, 0, reserved,  fac_kingdom_2, [itm_northerner_horse_black,itm_fur_coat,itm_vaegir_elite_armor,itm_nomad_boots,itm_splinted_leather_greaves,itm_m_vaegir_rus_splint_greaves,    itm_mail_mittens,itm_war_axe, itm_mace_4,itm_norman_shield_1],    knight_attrib_1,wp(130),knight_skills_1, 0x00000004c500028608d386449d6d4d3700000000001edaf20000000000000000, vaegir_face_middle_2],
  ["knight_2_12", "Boyar Zela", "Zela", tf_hero, 0, reserved,  fac_kingdom_2, [itm_northerner_horse_black,itm_fur_coat,itm_m_vaegir_rus_scale,itm_nomad_boots,itm_splinted_leather_greaves,itm_m_vaegir_rus_cav_boots,    itm_mail_mittens,itm_war_axe, itm_mace_4,itm_norman_shield_1],    knight_attrib_2,wp(170),knight_skills_2, 0x00000004da00014368db7259117fcf3f00000000001db6f20000000000000000, vaegir_face_old_2],
  ["knight_2_13", "Boyar Jara", "Jara", tf_hero, 0, reserved,  fac_kingdom_2, [itm_northerner_horse_black,itm_fur_coat,itm_m_vaegir_rus_lamellar_b,itm_nomad_boots,itm_splinted_leather_greaves,itm_m_vaegir_rus_cav_boots,    itm_mail_mittens,itm_war_axe, itm_mace_3,itm_norman_shield_4],     knight_attrib_3,wp(190),knight_skills_3, 0x00000004c30c254822db6ec69b6dfcff00000000001eb6ba0000000000000000, vaegir_face_older_2],
  ["knight_2_14", "Boyar Boha", "Boha", tf_hero, 0, reserved,  fac_kingdom_2, [itm_northerner_horse_black,itm_fur_coat,itm_m_vaegir_rus_lamellar_a,itm_nomad_boots,itm_splinted_leather_greaves,itm_m_vaegir_rus_cav_boots,    itm_mail_mittens,itm_bardiche, itm_mace_4,itm_norman_shield_4],    knight_attrib_4,wp(220),knight_skills_4|knows_trainer_6, 0x0000000dc40c22d4204769bedb6dfeff00000000001c66f80000000000000000, vaegir_face_older_2],
  ["knight_2_15", "Boyar Vata", "Vata", tf_hero, 0, reserved,  fac_kingdom_2, [itm_northerner_horse_black,itm_fur_coat,itm_m_vaegir_rus_lamellar_b,itm_nomad_boots,itm_splinted_leather_greaves,itm_m_vaegir_rus_cav_boots,    itm_mail_mittens,itm_one_handed_battle_axe_b,itm_norman_shield_4],       knight_attrib_5,wp(250),knight_skills_5, 0x0000000dc708000020dccdf5e7b67eff00000000001f70f80000000000000000, vaegir_face_older_2],
  ["knight_2_16", "Boyar Vojta", "Vojta", tf_hero, 0, reserved,  fac_kingdom_2, [itm_northerner_horse_black,itm_fur_coat,itm_m_vaegir_kuyak_a,itm_nomad_boots,itm_splinted_leather_greaves,itm_m_vaegir_rus_cav_boots,    itm_mail_mittens,itm_bardiche, itm_one_handed_battle_axe_a,itm_norman_shield_1],   knight_attrib_1,wp(120),knight_skills_1, 0x000000009610034f06c36db6db6decff00000000001dbf380000000000000000, vaegir_face_middle_2],
  ["knight_2_17", "Boyar Stecha", "Stecha", tf_hero, 0, reserved,  fac_kingdom_2, [itm_northerner_horse_black,itm_fur_coat,itm_m_vaegir_kuyak_b,itm_nomad_boots,itm_splinted_leather_greaves,itm_m_vaegir_rus_splint_greaves,    itm_mail_mittens,itm_bardiche, itm_mace_4,itm_norman_shield_3],     knight_attrib_2,wp(150),knight_skills_2, 0x00000000b90c008606db6db0dba1eb1f00000000001dd6c00000000000000000, vaegir_face_old_2],
  ["knight_2_18", "Boyar Lava", "Lava", tf_hero, 0, reserved,  fac_kingdom_2, [itm_northerner_horse_black,itm_fur_coat,itm_m_vaegir_mail_long_a,itm_nomad_boots,itm_splinted_leather_greaves,itm_m_vaegir_rus_cav_boots,    itm_mail_mittens,itm_spear, itm_grosse_messer,itm_norman_shield_1],    knight_attrib_3,wp(180),knight_skills_3, 0x00000000a70801c304146d8fe76eff7f00000000001eb6f80000000000000000, vaegir_face_older_2],
  ["knight_2_19", "Boyar Veko", "Veko", tf_hero, 0, reserved,  fac_kingdom_2, [itm_northerner_horse_black,itm_fur_coat,itm_m_vaegir_kuyak_c,itm_nomad_boots,itm_splinted_leather_greaves,itm_m_vaegir_rus_splint_greaves,    itm_mail_mittens,itm_bardiche, itm_one_handed_battle_axe_c,itm_norman_shield_2],    knight_attrib_4,wp(210),knight_skills_4|knows_trainer_4, 0x00000000850001c206db6db6d36deb3600000000001db6f80000000000000000, vaegir_face_older_2],
  ["knight_2_20", "Boyar Vojar", "Vojar", tf_hero, 0, reserved,  fac_kingdom_2, [itm_northerner_horse,itm_fur_coat,itm_m_vaegir_kuyak_d,itm_nomad_boots,itm_splinted_leather_greaves,itm_m_vaegir_rus_cav_boots,    itm_mail_mittens, itm_one_handed_battle_axe_a,itm_norman_shield_1],      knight_attrib_5,wp(240),knight_skills_5|knows_trainer_5, 0x000000003f0c000530db6db6db6d8efe00000000001c36fb0000000000000000, vaegir_face_older_2],

#khergit civilian clothes: itm_leather_vest, itm_nomad_vest, itm_nomad_robe, itm_lamellar_vest,itm_tribal_warrior_outfit
  ["knight_3_1", "Qari Noyan", "Qari", tf_hero, 0, reserved,  fac_kingdom_3, [itm_mt_horse_a2,itm_nomad_robe,itm_leather_boots,itm_m_greaves_a,itm_m_lancer_heavy_elite_a,  itm_mt_scale_gloves_a,       itm_strange_sword,itm_steel_shield,itm_m_lancer_helmet_midi_a],  knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3|knows_power_draw_4, 0x0000000e700031cd041f6db6db6dfeff00000000001df6f80000000000000000, khergit_face_middle_2],
  ["knight_3_2", "Gany Noyan",  "Gany", tf_hero, 0, reserved,  fac_kingdom_3, [itm_mt_horse_a,itm_nomad_robe,itm_leather_boots,itm_m_greaves_a,itm_m_lancer_armor_elite_a,  itm_mt_scale_gloves_b,       itm_sword_khergit_3,itm_strong_bow,itm_arrows,itm_steel_shield,itm_m_lancer_helmet_midi_b], knight_attrib_2,wp(160),knight_skills_2|knows_power_draw_4, 0x0000000e4900224c049c6db6db6dfeff00000000001df6f00000000000000000, khergit_face_old_2],
  ["knight_3_3", "Gune Noyan",  "Gune", tf_hero, 0, reserved,  fac_kingdom_3, [itm_mt_horse_a2,itm_nomad_robe,itm_leather_boots,itm_m_greaves_a,itm_m_lancer_armor_elite_b,  itm_mt_scale_gloves_b,       itm_sword_khergit_3,itm_strong_bow,itm_bodkin_arrows,itm_steel_shield,itm_m_lancer_helmet_midi_c],  knight_attrib_3,wp(190),knight_skills_3|knows_trainer_5|knows_power_draw_4, 0x0000000e7f002390049f85badb687eff00000000001cf7380000000000000000, khergit_face_older_2],
  ["knight_3_4", "Ssukai Noyan", "Ssukai", tf_hero, 0, reserved,  fac_kingdom_3, [itm_mt_horse_a2,itm_nomad_robe,itm_leather_boots,itm_m_greaves_b,itm_m_lancer_armor_elite_c,  itm_mt_scale_gloves_a,       itm_sword_khergit_3,itm_strong_bow,itm_bodkin_arrows,itm_steel_shield,itm_m_lancer_helmet_midi_d],  knight_attrib_4,wp(220),knight_skills_4|knows_power_draw_4, 0x000000095c003350048785badb687fff00000000001cf7380000000000000000, khergit_face_older_2],
  ["knight_3_5", "Magny Noyan",  "Magny", tf_hero, 0, reserved,  fac_kingdom_3, [itm_mt_horse_a,itm_nomad_robe,itm_leather_boots,itm_m_greaves_a,itm_m_lancer_armor_elite_d,  itm_mt_scale_gloves_a,       itm_sword_khergit_3,itm_strong_bow,itm_arrows,itm_steel_shield,itm_m_lancer_helmet_midi_e],  knight_attrib_5,wp(250),knight_skills_5|knows_power_draw_4, 0x000000095c003111048785badb695d7f00000000001df7380000000000000000, khergit_face_older_2],
  ["knight_3_6", "Bate Noyan", "Bate", tf_hero, 0, reserved,  fac_kingdom_3, [itm_mt_horse_a2,itm_nomad_robe,itm_leather_boots,itm_m_greaves_a,itm_m_lancer_armor_elite_e,  itm_mt_scale_gloves_a,       itm_sword_khergit_4,itm_nomad_bow,itm_m_rider_arrows,itm_steel_shield,itm_m_lancer_helmet_midi_f], knight_attrib_1,wp(130),knight_skills_1|knows_power_draw_4, 0x000000095c003192048785badb6d7d7f00000000001e77380000000000000000, khergit_face_middle_2],
  ["knight_3_7", "Tema Noyan","Tema", tf_hero, 0, reserved,  fac_kingdom_3, [itm_mt_horse_a2,itm_nomad_robe,itm_leather_boots,itm_m_greaves_a,itm_m_lancer_armor_elite_f,  itm_mt_scale_gloves_a,       itm_sword_khergit_3,itm_khergit_bow,itm_m_rider_arrows,itm_steel_shield,itm_m_lancer_helmet_midi_a], knight_attrib_2,wp(160),knight_skills_2|knows_power_draw_4, 0x000000095c0041d4048785badb6d7d7f00000000001e77380000000000000000, khergit_face_old_2],
  ["knight_3_8", "Ganua Noyan", "Ganua", tf_hero, 0, reserved,  fac_kingdom_3, [itm_mt_horse_a,itm_nomad_robe,itm_leather_boots,itm_m_greaves_a,itm_m_lancer_armor_elite_g,  itm_mt_leather_gloves_a,       itm_sword_khergit_4,itm_khergit_bow,itm_m_rider_arrows,itm_steel_shield,itm_m_lancer_helmet_midi_b],  knight_attrib_3,wp(190),knight_skills_3|knows_power_draw_4, 0x000000095c005280048785badb6d7d7f00000000001e77380000000000000000, khergit_face_older_2],
  ["knight_3_9", "Tera Noyan","Tera", tf_hero, 0, reserved,  fac_kingdom_3, [itm_mt_horse_a2,itm_nomad_robe,itm_leather_boots,itm_m_greaves_a,itm_m_lamellar_champion_a,  itm_mt_leather_gloves_a,       itm_sword_khergit_3,itm_khergit_bow,itm_m_rider_arrows,itm_steel_shield,itm_m_lancer_helmet_midi_c],  knight_attrib_4,wp(220),knight_skills_4|knows_power_draw_4, 0x000000095c00434d048785badb6d7d7f00000000001ff7380000000000000000, khergit_face_older_2],
  ["knight_3_10", "Mari Noyan","Mari", tf_hero, 0, reserved,  fac_kingdom_3, [itm_mt_horse_a2,itm_nomad_robe,itm_leather_boots,itm_m_greaves_a,itm_m_lamellar_armor_b,  itm_mt_leather_gloves_a,       itm_sword_khergit_2,itm_nomad_bow,itm_arrows,itm_steel_shield,itm_m_lancer_helmet_midi_a], knight_attrib_5,wp(250),knight_skills_5|knows_trainer_6|knows_power_draw_4, 0x000000095c00338c040c85badb6d7d7f00000000001de7380000000000000000, khergit_face_older_2],
  ["knight_3_11", "Hira Noyan", "Hira", tf_hero, 0, reserved,  fac_kingdom_3, [itm_mt_horse_a2,itm_nomad_robe,itm_leather_boots,itm_m_greaves_a,itm_m_lamellar_armor_west_b,  itm_mt_leather_gloves_a,       itm_sword_khergit_1,itm_nomad_bow,itm_arrows,itm_steel_shield,itm_m_lancer_helmet_midi_e],  knight_attrib_1,wp(150),knight_skills_1|knows_power_draw_4, 0x000000095c0054500acc85badb6d7d7f00000000001d47380000000000000000, khergit_face_middle_2],
  ["knight_3_12", "Qoyora Noyan", "Qoyora", tf_hero, 0, reserved,  fac_kingdom_3, [itm_mt_horse_a2,itm_nomad_robe,itm_leather_boots,itm_m_leather_boots_a,itm_m_lancer_armor_a_long,  itm_mt_scale_gloves_a,       itm_sword_khergit_2,itm_nomad_bow,itm_arrows,itm_steel_shield,itm_m_lancer_helmet_midi_b], knight_attrib_2,wp(190),knight_skills_2|knows_power_draw_4, 0x000000095c00301420cf85badb6d7d7f00000000001dc7380000000000000000, khergit_face_old_2],
  ["knight_3_13", "Unborj Noyan","Unborj", tf_hero, 0, reserved,  fac_kingdom_3, [itm_mt_horse_a,itm_nomad_robe,itm_leather_boots,itm_m_leather_boots_a,itm_m_lancer_armor_b_long,  itm_mt_scale_gloves_a,       itm_sword_khergit_3,itm_m_rider_bow_a,itm_arrows,itm_leather_covered_round_shield,itm_m_lancer_helmet_midi_a],  knight_attrib_3,wp(200),knight_skills_3|knows_trainer_3|knows_power_draw_4, 0x000000095c0045d320cf85badb6d7d7f00000000001dc7380000000000000000, khergit_face_older_2],
  ["knight_3_14", "Jinai Noyan",  "Jinai", tf_hero, 0, reserved,  fac_kingdom_3, [itm_mt_horse_a,itm_nomad_robe,itm_leather_boots,itm_m_leather_boots_a,itm_m_lancer_armor_elite_c,  itm_mt_scale_gloves_a,       itm_sword_khergit_4,itm_m_rider_bow_a,itm_arrows,itm_leather_covered_round_shield,itm_m_lancer_helmet_midi_a],  knight_attrib_4,wp(300),knight_skills_4|knows_trainer_6|knows_power_draw_4, 0x000000094000508020cf85badb6d7d7f00000000001dc7380000000000000000, khergit_face_older_2],
  ["knight_3_15", "Yemun Noyan", "Yemun", tf_hero, 0, reserved,  fac_kingdom_3, [itm_mt_horse_a,itm_nomad_robe,itm_leather_boots,itm_m_leather_boots_a,itm_m_lancer_armor_elite_b,  itm_mt_scale_gloves_a,       itm_sword_khergit_3,itm_nomad_bow,itm_arrows,itm_leather_covered_round_shield,itm_m_lancer_helmet_midi_b],  knight_attrib_5,wp(240),knight_skills_5|knows_trainer_4|knows_power_draw_4, 0x00000009400041d420cf85badb6d7d7f00000000001dc7380000000000000000, khergit_face_older_2],
  ["knight_3_16", "Bumbo Noyan","Bumbo", tf_hero, 0, reserved,  fac_kingdom_3, [itm_mt_horse_a2,itm_nomad_robe,itm_leather_boots,itm_m_leather_boots_a,itm_m_lancer_armor_elite_a,  itm_mt_scale_gloves_a,       itm_sword_khergit_1,itm_nomad_bow,itm_bodkin_arrows,itm_leather_covered_round_shield,itm_m_lancer_helmet_midi_c],  knight_attrib_1,wp(120),knight_skills_1|knows_power_draw_4, 0x000000094000328520cf85badb6d7d7f00000000001dc7380000000000000000, khergit_face_middle_2],
  ["knight_3_17", "Qara Noyan", "Qara", tf_hero, 0, reserved,  fac_kingdom_3, [itm_mt_horse_a2,itm_nomad_robe,itm_leather_boots,itm_m_leather_boots_a,itm_m_lancer_armor_elite_g,  itm_mt_scale_gloves_a,       itm_sword_khergit_2,itm_nomad_bow,itm_barbed_arrows,itm_leather_covered_round_shield,itm_m_lancer_helmet_midi_d],  knight_attrib_2,wp(150),knight_skills_2|knows_power_draw_4, 0x000000094000534620cf85badb6d7d7f00000000001ff7380000000000000000, khergit_face_old_2],
  ["knight_3_18", "Temay Noyan", "Temay", tf_hero, 0, reserved,  fac_kingdom_3, [itm_mt_horse_a2,itm_nomad_robe,itm_leather_boots,itm_m_leather_boots_a,itm_m_lancer_armor_elite_b_long,  itm_mt_scale_gloves_a,       itm_sword_khergit_3,itm_nomad_bow,itm_barbed_arrows,itm_leather_covered_round_shield,itm_m_lancer_helmet_light_a],   knight_attrib_3,wp(180),knight_skills_3|knows_trainer_4|knows_power_draw_4, 0x000000097f00338720cf85badb6d7d7f00000000001cf7380000000000000000, khergit_face_older_2],
  ["knight_3_19", "Bayari Noyan","Bayari", tf_hero, 0, reserved,  fac_kingdom_3, [itm_mt_horse_a2,itm_nomad_robe,itm_leather_boots,itm_m_leather_boots_a,itm_m_lancer_armor_elite_a_long,  itm_mt_scale_gloves_a,       itm_sword_khergit_3,itm_nomad_bow,itm_arrows,itm_leather_covered_round_shield,itm_m_lancer_helmet_light_b],  knight_attrib_4,wp(210),knight_skills_4|knows_trainer_5|knows_power_draw_4, 0x000000097f00434920cf85badb6d7d7f00000000001fd7380000000000000000, khergit_face_older_2],
  ["knight_3_20", "Atar Noyan","Atar", tf_hero, 0, reserved,  fac_kingdom_3, [itm_mt_horse_a2,itm_nomad_robe,itm_leather_boots,itm_m_leather_boots_a,itm_m_lancer_armor_elite_a_long,  itm_mt_scale_gloves_a,       itm_strange_sword,itm_leather_covered_round_shield,itm_m_lancer_helmet_light_a],  knight_attrib_5,wp(240),knight_skills_5|knows_power_draw_4, 0x000000097f00348d211f8dbfdb6d7f7f00000000001ff7780000000000000000, khergit_face_older_2],

  ["knight_4_1", "Jarl Jarni Authfrinson", "Jarni Authfrinson", tf_hero, 0, reserved,  fac_kingdom_4, [itm_rich_outfit,  itm_cuir_bouilli_with_pelt,   itm_woolen_hose,  itm_m_greaves_a,  itm_ms_gjermundbu_helm_a, itm_mail_mittens, itm_great_axe, itm_tab_shield_round_d, itm_throwing_axes], knight_attrib_1,wp(130),knight_skills_1, 0x0000000f9300229206db6db6db6dfef600000000001db6f00000000000000000, nord_face_middle_2],
  ["knight_4_2", "Jarl Arnvim", "Arnvim", tf_hero, 0, reserved,  fac_kingdom_4, [ itm_short_tunic,  itm_banded_armor_b, itm_blue_hose,  itm_m_greaves_b,  itm_ms_spangen_helmet_c, itm_scale_gauntlets, itm_one_handed_battle_axe_c,  itm_tab_shield_round_d, itm_throwing_axes],  knight_attrib_2,wp(160),knight_skills_2|knows_trainer_3, 0x0000000f8d04138436db6db6db6db6ff00000000001db6fb0000000000000000, nord_face_old_2],
  ["knight_4_3", "Jarl Vasti Ansgarson", "Vasti Ansgarson", tf_hero, 0, reserved,  fac_kingdom_4, [itm_warhorse, itm_rich_outfit,  itm_cuir_bouilli_with_pelt,   itm_nomad_boots,  itm_m_greaves_a, itm_scale_gauntlets,   itm_ms_spangen_helmet_b,   itm_great_axe, itm_tab_shield_round_e, itm_throwing_axes],  knight_attrib_3,wp(190),knight_skills_3, 0x0000000f8008128412dc6ca636513a7f00000000001f44f80000000000000000, nord_face_older_2],
  ["knight_4_4", "Jarl Hrabbi Laeingrieson", "Hrabbi Laeingrieson", tf_hero, 0, reserved,  fac_kingdom_4, [itm_hunter,   itm_leather_vest,   itm_banded_armor_c,   itm_woolen_hose,  itm_mail_boots, itm_scale_gauntlets,  itm_ms_gjermundbu_helm_a, itm_fighting_pick, itm_tab_shield_round_e, itm_throwing_axes],  knight_attrib_4,wp(210),knight_skills_4, 0x0000000fbb0c51c9345b6d36db6dfeff00000000001db6fb0000000000000000, nord_face_older_2],
  ["knight_4_5", "Jarl Stoste Elsnarson", "Stoste Elsnarson", tf_hero, 0, reserved,  fac_kingdom_4, [  itm_fur_coat,   itm_banded_armor_d,   itm_leather_boots,  itm_m_leather_boots_a,  itm_scale_gauntlets, itm_ms_gjermundbu_helm_a, itm_bastard_sword_b, itm_tab_shield_round_e, itm_throwing_axes, itm_throwing_axes], knight_attrib_5,wp(250),knight_skills_5, 0x0000000fae102307204469e91b6dfef700000000001e56f80000000000000000, nord_face_older_2],
  ["knight_4_6", "Jarl Holti Skellison", "Holti Skellison", tf_hero, 0, reserved,  fac_kingdom_4, [   itm_nomad_robe,   itm_banded_armor_b,  itm_nomad_boots,  itm_m_greaves_a,   itm_ms_pointed_helmet_a, itm_mail_mittens,   itm_war_axe, itm_tab_shield_round_d],   knight_attrib_1,wp(130),knight_skills_1, 0x00000004ae101349204469e91b6dfef700000000001d46f80000000000000000, nord_face_middle_2],
  ["knight_4_7", "Jarl Arlir", "Arlir", tf_hero, 0, reserved,  fac_kingdom_4, [  itm_fur_coat,   itm_banded_armor_d,   itm_nomad_boots,  itm_mt_greaves_a,  itm_ms_spangen_helmet_a, itm_m_gauntlets_a,   itm_sword_viking_3, itm_shortened_military_scythe,  itm_tab_shield_round_d],   knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x00000004ba0c0187128c4db6db6ddd3f00000000001db6f00000000000000000, nord_face_old_2],
  ["knight_4_8", "Jarl Asker", "Asker", tf_hero, 0, reserved,  fac_kingdom_4, [ itm_rich_outfit,  itm_banded_armor,   itm_woolen_hose,  itm_m_leather_boots_a,   itm_ms_spangen_helmet_a, itm_m_gauntlets_a, itm_war_axe,  itm_tab_shield_round_e, itm_throwing_axes],   knight_attrib_3,wp(190),knight_skills_3, 0x000000048a0c2354645469b91b6dbeff00000000001ec6fb0000000000000000, nord_face_older_2],
  ["knight_4_9", "Jarl Berglja", "Berglja", tf_hero, 0, reserved,  fac_kingdom_4, [itm_warhorse, itm_nomad_robe,   itm_cuir_bouilli, itm_blue_hose,  itm_m_leather_boots_a,  itm_ms_pointed_helmet_a, itm_m_gloves_a, itm_arrows, itm_long_bow,   itm_one_handed_battle_axe_c,  itm_tab_shield_round_e],  knight_attrib_4,wp(220),knight_skills_4|knows_trainer_5|knows_power_draw_4, 0x00000004b604229434a26934db6dbefb00000000001d36f10000000000000000, nord_face_older_2],
  ["knight_4_10", "Jarl Arikr", "Arikr", tf_hero, 0, reserved,  fac_kingdom_4, [itm_hunter,   itm_courtly_outfit,   itm_cuir_bouilli_with_pelt,   itm_nomad_boots,  itm_m_greaves_b, itm_m_gauntlets_a,  itm_winged_great_helmet,itm_great_axe, itm_tab_shield_round_e],  knight_attrib_5,wp(250),knight_skills_5|knows_trainer_6, 0x00000003c110128176db6db6db6dfeff00000000001c76fb0000000000000000, nord_face_older_2],
  ["knight_4_11", "Jarl Oslat", "Oslat", tf_hero, 0, reserved,  fac_kingdom_4, [ itm_rich_outfit,  itm_banded_armor_b,   itm_woolen_hose,  itm_m_greaves_a,  itm_nordic_helmet,  itm_m_gauntlets_b,  itm_great_bardiche, itm_tab_shield_round_d], knight_attrib_1,wp(140),knight_skills_1, 0x00000001ed102005211c45bb236e5efd00000000001ef2f80000000000000000, nord_face_middle_2],
  ["knight_4_12", "Jarl Berti Beinison", "Berti Beinison", tf_hero, 0, reserved,  fac_kingdom_4, [ itm_short_tunic,  itm_banded_armor_c, itm_blue_hose,  itm_m_greaves_b,  itm_nordic_huscarl_helmet,  itm_m_gauntlets_b,  itm_one_handed_battle_axe_c,  itm_tab_shield_round_d],  knight_attrib_2,wp(200),knight_skills_2, 0x00000001f3103252125b6db6db6dbeff00000000001dc6f80000000000000000, nord_face_old_2],
  ["knight_4_13", "Jarl Haukri Gadison", "Haukri Gadison", tf_hero, 0, reserved,  fac_kingdom_4, [itm_warhorse, itm_rich_outfit,  itm_cuir_bouilli,   itm_nomad_boots,  itm_mail_chausses, itm_scale_gauntlets,   itm_nordic_warlord_helmet,   itm_war_axe, itm_tab_shield_round_e],  knight_attrib_3,wp(250),knight_skills_3|knows_trainer_3, 0x00000001d71001c920db6db6db6ddff700000000001c56f80000000000000000, nord_face_older_2],
  ["knight_4_14", "Jarl Kari", "Kari", tf_hero, 0, reserved,  fac_kingdom_4, [  itm_leather_vest,   itm_banded_armor_d,   itm_woolen_hose,  itm_m_greaves_a,  itm_nordic_helmet, itm_scale_gauntlets, itm_fighting_pick, itm_tab_shield_round_e, itm_throwing_axes],  knight_attrib_4,wp(200),knight_skills_4, 0x00000001f800028712db6da55c6dfefe00000000001e46b80000000000000000, nord_face_older_2],
  ["knight_4_15", "Jarl Butre", "Butre", tf_hero, 0, reserved,  fac_kingdom_4, [itm_hunter,   itm_leather_jacket,   itm_heraldic_mail_with_tabard,   itm_leather_boots, itm_scale_gauntlets,  itm_splinted_leather_greaves,  itm_nordic_huscarl_helmet, itm_2h_claymore, itm_tab_shield_round_e], knight_attrib_5,wp(290),knight_skills_5|knows_trainer_6, 0x00000001f110435412db6db6946dfeff00000000001e26f10000000000000000, nord_face_older_2],
  ["knight_4_16", "Jarl Fastri Therison", "Fastri Therison", tf_hero, 0, reserved,  fac_kingdom_4, [   itm_nomad_robe,   itm_banded_armor,  itm_nomad_boots,  itm_mail_chausses,   itm_nordic_huscarl_helmet, itm_mail_mittens,   itm_war_axe, itm_tab_shield_round_d, itm_throwing_axes],   knight_attrib_1,wp(120),knight_skills_1, 0x00000001cc0c058420d35128dc6ddaf600000000001db6f90000000000000000, nord_face_middle_2],
  ["knight_4_17", "Jarl Kjarki", "Kjarki", tf_hero, 0, reserved,  fac_kingdom_4, [  itm_fur_coat,   itm_banded_armor,   itm_nomad_boots,  itm_m_greaves_a,  itm_nordic_warlord_helmet, itm_mail_mittens,   itm_sword_viking_3,  itm_tab_shield_round_d, itm_throwing_axes],   knight_attrib_2,wp(150),knight_skills_2|knows_trainer_4, 0x00000001e808028a36db6db6db6dfcf600000000001db6fb0000000000000000, nord_face_old_2],
  ["knight_4_18", "Jarl Thore Geirrison", "Thore Geirrison", tf_hero, 0, reserved,  fac_kingdom_4, [ itm_rich_outfit,  itm_a_h3_1,   itm_woolen_hose,  itm_b_h1,   itm_h_h1, itm_scale_gauntlets, itm_sword_viking_3, itm_2h_claymore,  itm_s_h2_2],   knight_attrib_3,wp(180),knight_skills_3, 0x00000001e808120836db6db6db6dfcf600000000001db6fb0000000000000000, nord_face_older_2],
  ["knight_4_19", "Jarl Grimi Thorstison", "Grimi Thorstison", tf_hero, 0, reserved,  fac_kingdom_4, [itm_warhorse, itm_nomad_robe,   itm_a_h3, itm_blue_hose,  itm_b_h1,  itm_ms_conical_helmet_mail_a, itm_scale_gauntlets,   itm_one_handed_battle_axe_c,  itm_tab_shield_round_e, itm_throwing_axes],  knight_attrib_4,wp(210),knight_skills_4|knows_trainer_5, 0x00000001c008314712db6db6db6ddefe00000000001cc6bb0000000000000000, nord_face_older_2],
  ["knight_4_20", "Jarl There Hognison", "There Hognison", tf_hero, 0, reserved,  fac_kingdom_4, [itm_hunter,   itm_courtly_outfit,   itm_a_h3_1,   itm_nomad_boots,  itm_splinted_greaves, itm_scale_gauntlets,  itm_ms_conical_helmet_mail_b,itm_great_axe, itm_tab_shield_round_e, itm_throwing_axes],  knight_attrib_5,wp(240),knight_skills_5, 0x00000001c0082191365b6db6db6d8ef600000000001db6ff0000000000000000, nord_face_older_2],

  ["knight_5_1", "Count Atris", "Atris", tf_hero, 0, reserved,  fac_kingdom_5, [itm_saddle_horse,itm_tabard,   itm_plate_armor,itm_m_hose_a,itm_m_greaves_a,itm_m_bascinet_a,itm_m_gauntlets_a, itm_morningstar,itm_shield_heater_d, itm_guisarme],     knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x000000079e00625116db6db6db6ddaed00000000001db6ea0000000000000000, rhodok_face_middle_2],
  ["knight_5_2", "Count Giersa", "Giersa", tf_hero, 0, reserved,  fac_kingdom_5, [itm_saddle_horse,itm_tabard,   itm_m_full_plate_b,itm_m_hose_b,itm_m_greaves_b,itm_m_tower_helm_a,itm_m_gauntlets_b, itm_crusader_sword,itm_shield_heater_d, itm_bec_de_corbin],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x00000007bc00019416db6db6db6ddaed00000000001db6ea0000000000000000, rhodok_face_old_2],
  ["knight_5_3", "Count Amartz", "Amartz", tf_hero, 0, reserved,  fac_kingdom_5, [itm_saddle_horse,itm_tabard,   itm_m_full_plate_a,itm_m_hose_c,itm_m_greaves_b,itm_m_houndskull_a,itm_m_gauntlets_b, itm_longsword,itm_shield_heater_d, itm_poleaxe_a],    knight_attrib_3,wp(190),knight_skills_3, 0x00000007bc00414916db6db6db6ddaed00000000001db6ea0000000000000000, rhodok_face_older_2],
  ["knight_5_4", "Count Resa", "Resa", tf_hero, 0, reserved,  fac_kingdom_5, [itm_saddle_horse,itm_tabard,   itm_ms_armor_plate_a,itm_m_hose_d,itm_m_greaves_b,itm_m_bascinet_a,itm_m_gauntlets_b, itm_longsword,itm_shield_heater_d, itm_elegant_poleaxe],    knight_attrib_4,wp(220),knight_skills_4, 0x00000007ac00300936db6db6db6decee00000000001db6f30000000000000000, rhodok_face_older_2],
  ["knight_5_5", "Count Jaufre", "Jaufre", tf_hero, 0, reserved,  fac_kingdom_5, [itm_saddle_horse,itm_tabard,   itm_m_full_plate_a,itm_m_hose_e,itm_m_greaves_a,itm_m_bascinet_b,itm_m_gauntlets_a, itm_morningstar,itm_shield_heater_d, itm_guisarme], knight_attrib_5,wp(250),knight_skills_5, 0x00000007860400cf049b6db6db6ddef700000000001db6e80000000000000000, rhodok_face_older_2],
  ["knight_5_6", "Count Ulis", "Ulis", tf_hero, 0, reserved,  fac_kingdom_5, [itm_saddle_horse,itm_tabard,   itm_ms_armor_plate_a,itm_m_hose_a,itm_m_greaves_a,itm_m_onion_bascinet_a,itm_m_gauntlets_a, itm_grosse_messer_b,itm_shield_heater_d, itm_poleaxe_a],    knight_attrib_1,wp(130),knight_skills_1, 0x00000007840405cf3edb6db6db6dbef600000000001e36fb0000000000000000, rhodok_face_middle_2],
  ["knight_5_7", "Count Girve", "Girve", tf_hero, 0, reserved,  fac_kingdom_5, [itm_saddle_horse,itm_tabard,   itm_plate_armor,itm_m_hose_b,itm_m_greaves_a,itm_m_onion_bascinet_a,itm_m_gauntlets_a, itm_grosse_messer_b,itm_shield_heater_d, itm_german_poleaxe],     knight_attrib_2,wp(160),knight_skills_2, 0x00000007bd10101316db69b6db6dbcf700000000001db6f00000000000000000, rhodok_face_old_2],
  ["knight_5_8", "Count Anaics", "Anaics", tf_hero, 0, reserved,  fac_kingdom_5, [itm_saddle_horse,itm_tabard,   itm_ms_armor_plate_a,itm_m_hose_c,itm_m_greaves_a,itm_m_onion_bascinet_b,itm_m_gloves_a, itm_grosse_messer_b,itm_shield_heater_d, itm_english_bill],    knight_attrib_3,wp(190),knight_skills_3|knows_trainer_3, 0x000000078b00019236db6db8d36dfefe00000000001d453b0000000000000000, rhodok_face_older_2],

  ["knight_5_9", "Count Robertr", "Robertr", tf_hero, 0, reserved,  fac_kingdom_5, [itm_saddle_horse,itm_tabard,   itm_m_churburg_e,itm_m_hose_d,itm_m_greaves_b,itm_m_onion_bascinet_c,itm_m_gauntlets_a, itm_morningstar,itm_shield_heater_d, itm_guisarme],   knight_attrib_4,wp(220),knight_skills_4|knows_trainer_6, 0x00000007ac10151436db6db6db6deeff00000000001db6f90000000000000000, rhodok_face_older_2],
  ["knight_5_10", "Count Tibalts", "Tibalts", tf_hero, 0, reserved,  fac_kingdom_5, [itm_saddle_horse,itm_tabard,   itm_m_churburg_a,itm_m_hose_e,itm_m_greaves_b,itm_m_bascinet_a,itm_m_gauntlets_a, itm_morningstar,itm_shield_heater_d, itm_english_bill],  knight_attrib_5,wp(250),knight_skills_5|knows_trainer_4, 0x000000079600609112ec40aad2b8ff7f00000000001e36f80000000000000000, rhodok_face_older_2],
  ["knight_5_11", "Count Jausa", "Jausa", tf_hero, 0, reserved,  fac_kingdom_5, [itm_saddle_horse,itm_tabard,   itm_m_churburg_b,itm_m_hose_a,itm_m_greaves_b,itm_m_tower_helm_a,itm_m_gauntlets_a, itm_german_bastard_sword,itm_shield_heater_d, itm_poleaxe_a],     knight_attrib_1,wp(130),knight_skills_1, 0x00000007a0001047208d723913adcd7700000000001d4cb80000000000000000, rhodok_face_middle_2],
  ["knight_5_12", "Count Seli", "Seli", tf_hero, 0, reserved,  fac_kingdom_5, [itm_saddle_horse,itm_tabard,   itm_m_churburg_c,itm_m_hose_b,itm_m_greaves_b,itm_m_tower_helm_a,itm_m_gauntlets_a, itm_side_sword,itm_shield_heater_d, itm_guisarme],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_5, 0x000000079d08420a12db6db6db6dff7f00000000001c76f80000000000000000, rhodok_face_old_2],
  ["knight_5_13", "Count Gauda", "Gauda", tf_hero, 0, reserved,  fac_kingdom_5, [itm_saddle_horse,itm_tabard,   itm_m_churburg_a,itm_m_hose_c,itm_m_greaves_a,itm_m_tower_helm_a,itm_m_gauntlets_a, itm_side_sword,itm_shield_heater_d, itm_german_poleaxe],    knight_attrib_3,wp(190),knight_skills_3, 0x000000078a04018158db6dd69c8decf600000000001db6f20000000000000000, rhodok_face_older_2],
  ["knight_5_14", "Count Girve", "Girve", tf_hero, 0, reserved,  fac_kingdom_5, [itm_saddle_horse,itm_tabard,   itm_m_churburg_b,itm_m_hose_d,itm_m_greaves_a,itm_m_bascinet_a,itm_m_gauntlets_a, itm_italian_sword,itm_shield_heater_d, itm_guisarme],    knight_attrib_4,wp(220),knight_skills_4, 0x00000007a00c3548491b72599b55ff3700000000001d58bb0000000000000000, rhodok_face_older_2],
  ["knight_5_15", "Count Ganeus", "Ganeus", tf_hero, 0, reserved,  fac_kingdom_5, [itm_saddle_horse,itm_tabard,   itm_m_churburg_a,itm_m_hose_e,itm_m_greaves_a,itm_m_bascinet_a,itm_m_gauntlets_a, itm_morningstar,itm_shield_heater_d, itm_poleaxe_a], knight_attrib_5,wp(250),knight_skills_5, 0x00000007ab08350512e46d299c3dff7f00000000001d36b80000000000000000, rhodok_face_older_2],
  ["knight_5_16", "Count Giri", "Giri", tf_hero, 0, reserved,  fac_kingdom_5, [itm_saddle_horse,itm_tabard,   itm_m_churburg_f,itm_m_hose_a,itm_m_greaves_a,itm_m_tower_helm_b,itm_m_gauntlets_a, itm_italian_sword,itm_shield_heater_d, itm_guisarme],    knight_attrib_1,wp(120),knight_skills_1, 0x000000079110124536eb71c6d36ddeff00000000001d36fb0000000000000000, rhodok_face_middle_2],
  ["knight_5_17", "Count Sego", "Sego", tf_hero, 0, reserved,  fac_kingdom_5, [itm_saddle_horse,itm_tabard,   itm_m_churburg_a,itm_m_hose_b,itm_m_greaves_a,itm_m_tower_helm_b,itm_m_gauntlets_a, itm_morningstar,itm_shield_heater_d, itm_english_bill],     knight_attrib_2,wp(150),knight_skills_2, 0x00000007860c554f201b6db6db6efeff00000000001ff6f10000000000000000, rhodok_face_old_2],
  ["knight_5_18", "Count Bove", "Bove", tf_hero, 0, reserved,  fac_kingdom_5, [itm_saddle_horse,itm_tabard,   itm_m_corrazina_b,itm_m_hose_b,itm_m_greaves_b,itm_m_tower_helm_b,itm_m_gauntlets_a, itm_side_sword,itm_shield_heater_d, itm_guisarme],    knight_attrib_3,wp(180),knight_skills_3, 0x00000007b40424460edb6db6db6ddafe00000000001db6b80000000000000000, rhodok_face_older_2],
  ["knight_5_19", "Count Giersa", "Giersa", tf_hero, 0, reserved,  fac_kingdom_5, [itm_saddle_horse,itm_tabard,   itm_m_corrazina_a_cloak,itm_m_hose_c,itm_m_greaves_b,itm_m_bascinet_a,itm_m_gauntlets_a, itm_german_bastard_sword,itm_shield_heater_d, itm_danish_greatsword],   knight_attrib_4,wp(210),knight_skills_4|knows_trainer_5, 0x00000007a70c40c8131b6db6db6dfcf600000000001cc5390000000000000000, rhodok_face_older_2],
  ["knight_5_20", "Count Reli", "Reli", tf_hero, 0, reserved,  fac_kingdom_5, [itm_saddle_horse,itm_tabard,   itm_m_corrazina_a,itm_m_hose_e,itm_m_greaves_b,itm_m_bascinet_a,itm_m_gauntlets_a, itm_morningstar,itm_shield_heater_d, itm_poleaxe_a],  knight_attrib_5,wp(240),knight_skills_5|knows_trainer_6, 0x00000007810042946d138ee50a71fcf700000000001ec7610000000000000000, rhodok_face_older_2],

  ["knight_6_1", "Emir Jaha", "Jaha", tf_hero, 0, reserved,  fac_kingdom_6, [itm_saracin_hard_horses_a_v1,itm_mkk_mamluke_a,itm_sarranid_boots_c,itm_mkk_heavy_boots_b,itm_mkk_heavy_helmet_a, itm_mkk_gauntlets_sar_b,itm_heavy_lance, itm_sarranid_cavalry_sword,itm_tab_shield_small_round_c],     knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x0000000af80c335420db6dcadb6dbef600000000001dd6f80000000000000000, rhodok_face_middle_2],
  ["knight_6_2", "Emir Khara", "Khara", tf_hero, 0, reserved,  fac_kingdom_6, [itm_saracin_hard_horses_b_v1,itm_mkk_mamluke_b,itm_sarranid_boots_c,itm_mkk_heavy_boots_a,itm_mkk_heavy_helmet_b, itm_mkk_gauntlets_sar_b,itm_heavy_lance, itm_sarranid_cavalry_sword,itm_tab_shield_small_round_c],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x0000000af80c544620db6dcadb6dbef600000000001dd6f80000000000000000, rhodok_face_old_2],
  ["knight_6_3", "Emir Khamra", "Khamra", tf_hero, 0, reserved,  fac_kingdom_6, [itm_saracin_hard_horses_c_v1,itm_mkk_mamluke_c,itm_sarranid_boots_c,itm_mkk_heavy_boots_a,itm_mkk_heavy_helmet_c, itm_mkk_gauntlets_sar_a,itm_heavy_lance, itm_sarranid_cavalry_sword,itm_tab_shield_small_round_c],    knight_attrib_3,wp(190),knight_skills_3, 0x0000000af80c628020db6dcadb6dbef600000000001dd6f80000000000000000, rhodok_face_older_2],
  ["knight_6_4", "Emir Raima", "Raima", tf_hero, 0, reserved,  fac_kingdom_6, [itm_saracin_hard_horses_c_v1,itm_mkk_mamluke_c,itm_sarranid_boots_c,itm_mkk_heavy_boots_a,itm_mkk_heavy_helmet_a, itm_mkk_gauntlets_sar_a,itm_heavy_lance, itm_sarranid_cavalry_sword,itm_tab_shield_small_round_c],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000ac00c229120db6dcadb6dbef600000000001dd6f80000000000000000, rhodok_face_older_2],
  ["knight_6_5", "Emir Taizzah", "Taizzah", tf_hero, 0, reserved,  fac_kingdom_6, [itm_saracin_hard_horses_b_v1,itm_mkk_mamluke_b,itm_sarranid_boots_c,itm_mkk_heavy_boots_a,itm_mkk_heavy_helmet_b, itm_mkk_gauntlets_sar_a,itm_heavy_lance, itm_sarranid_cavalry_sword,itm_tab_shield_small_round_c], knight_attrib_5,wp(250),knight_skills_5, 0x0000000ac00c421220db6dcadb6dbef600000000001dd6f80000000000000000, rhodok_face_older_2],
  ["knight_6_6", "Emir Rana", "Rana", tf_hero, 0, reserved,  fac_kingdom_6, [itm_saracin_hard_horses_c_v1,itm_mkk_mamluke_a,itm_sarranid_boots_c,itm_mkk_heavy_boots_b,itm_mkk_semi_heavy_helmet_a, itm_mkk_gauntlets_sar_b,itm_heavy_lance, itm_sarranid_cavalry_sword,itm_tab_shield_small_round_c],    knight_attrib_1,wp(130),knight_skills_1, 0x0000000ac00c525420db6dcadb6dbef600000000001dd6f80000000000000000, rhodok_face_middle_2],
  ["knight_6_7", "Emir Taquw", "Taquw", tf_hero, 0, reserved,  fac_kingdom_6, [itm_saracin_hard_horses_a_v1,itm_mkk_mamluke_b,itm_sarranid_boots_c,itm_mkk_heavy_boots_a,itm_mkk_semi_heavy_helmet_b, itm_mkk_gauntlets_sar_b,itm_heavy_lance, itm_sarranid_cavalry_sword,itm_tab_shield_small_round_c],     knight_attrib_2,wp(160),knight_skills_2, 0x0000000ac00c500520db6dcadb6dbef600000000001dd6f80000000000000000, rhodok_face_old_2],
  ["knight_6_8", "Emir Jizah", "Jizah", tf_hero, 0, reserved,  fac_kingdom_6, [itm_saracin_hard_horses_c_v1,itm_mkk_mamluke_c,itm_sarranid_boots_c,itm_mkk_heavy_boots_a,itm_mkk_semi_heavy_helmet_c, itm_mkk_gauntlets_mail_a,itm_heavy_lance, itm_sarranid_cavalry_sword,itm_tab_shield_small_round_c],    knight_attrib_3,wp(190),knight_skills_3|knows_trainer_3, 0x0000000ac00c75c620db6dcadb6dbef600000000001dd6f80000000000000000, rhodok_face_older_2],
  ["knight_6_9", "Emir Raha", "Raha", tf_hero, 0, reserved,  fac_kingdom_6, [itm_saracin_hard_horses_a_v1,itm_mkk_mamluke_a,itm_sarranid_boots_c,itm_mkk_heavy_boots_b,itm_mkk_semi_heavy_helmet_d, itm_mkk_gauntlets_mail_a,itm_heavy_lance, itm_sarranid_cavalry_sword,itm_tab_shield_small_round_c],   knight_attrib_4,wp(220),knight_skills_4|knows_trainer_6, 0x0000000ac00c710720db6dcadb6dbef600000000001dd6f80000000000000000, rhodok_face_older_2],
  ["knight_6_10", "Emir Nasla", "Nasla", tf_hero, 0, reserved,  fac_kingdom_6, [itm_saracin_hard_horses_d_v1,itm_mkk_mamluke_b,itm_sarranid_boots_c,itm_mkk_heavy_boots_b,itm_mkk_semi_heavy_helmet_a, itm_mkk_gauntlets_mail_a,itm_heavy_lance, itm_sarranid_cavalry_sword,itm_tab_shield_small_round_c],  knight_attrib_5,wp(250),knight_skills_5|knows_trainer_4, 0x0000000af80c114620db6dcadb6dbef600000000001dd6f80000000000000000, rhodok_face_older_2],
  ["knight_6_11", "Emir Bura", "Bura", tf_hero, 0, reserved,  fac_kingdom_6, [itm_saracin_hard_horses_d_v1,itm_mkk_infantry_armor_a,itm_sarranid_boots_c,itm_mkk_heavy_boots_b,itm_mkk_semi_heavy_helmet_b, itm_mkk_gauntlets_mail_a,itm_heavy_lance, itm_sarranid_cavalry_sword,itm_tab_shield_small_round_c],     knight_attrib_1,wp(130),knight_skills_1, 0x0000000af80c318420db6dcadb6dbef600000000001dd6f80000000000000000, rhodok_face_middle_2],
  ["knight_6_12", "Emir Majmi", "Majmi", tf_hero, 0, reserved,  fac_kingdom_6, [itm_saracin_hard_horses_a_v1,itm_mkk_infantry_armor_a,itm_sarranid_boots_c,itm_mkk_heavy_boots_a,itm_mkk_semi_heavy_helmet_c, itm_mkk_gloves_a,itm_heavy_lance, itm_sarranid_cavalry_sword,itm_tab_shield_small_round_c],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_5, 0x0000000af80c51c420db6dcadb6dbef600000000001dd6f80000000000000000, rhodok_face_old_2],
  ["knight_6_13", "Emir Madha", "Madha", tf_hero, 0, reserved,  fac_kingdom_6, [itm_saracin_hard_horses_a_v1,itm_mkk_infantry_armor_a,itm_sarranid_boots_c,itm_mkk_heavy_boots_a,itm_mkk_semi_heavy_helmet_d, itm_mkk_gloves_a,itm_heavy_lance, itm_sarranid_cavalry_sword,itm_tab_shield_small_round_c],    knight_attrib_3,wp(190),knight_skills_3, 0x0000000af80c728320db6dcadb6dbef600000000001dd6f80000000000000000, rhodok_face_older_2],
  ["knight_6_14", "Emir Qaiquw", "Qaiquw", tf_hero, 0, reserved,  fac_kingdom_6, [itm_saracin_hard_horses_b_v1,itm_mkk_infantry_armor_b,itm_sarranid_boots_c,itm_mkk_heavy_boots_a,itm_mkk_semi_heavy_helmet_e, itm_mkk_gloves_a,itm_heavy_lance, itm_sarranid_cavalry_sword,itm_tab_shield_small_round_c],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000af80c72c020db6dcadb6dbef600000000001dd6f80000000000000000, rhodok_face_older_2],
  ["knight_6_15", "Emir Maila", "Maila", tf_hero, 0, reserved,  fac_kingdom_6, [itm_saracin_hard_horses_a_v1,itm_mkk_infantry_armor_a,itm_sarranid_boots_c,itm_mkk_heavy_boots_b,itm_mkk_semi_heavy_helmet_f, itm_mkk_gloves_a,itm_heavy_lance, itm_sarranid_cavalry_sword,itm_tab_shield_small_round_c], knight_attrib_5,wp(250),knight_skills_5, 0x0000000ac00c029020db6dcadb6dbef600000000001dd6f80000000000000000, rhodok_face_older_2],
  
  ["knight_6_16", "Emir Shaira", "Shaira", tf_hero, 0, reserved,  fac_kingdom_6, [itm_saracin_hard_horses_a_v1,itm_mkk_infantry_armor_b,itm_sarranid_boots_c,itm_mkk_leather_boots_b,itm_mkk_gulam_helm_a, itm_mkk_gloves_a,itm_heavy_lance, itm_sarranid_cavalry_sword,itm_tab_shield_small_round_c],    knight_attrib_1,wp(120),knight_skills_1, 0x0000000aff0c630a20db6dcadb6dbef600000000001dd6f80000000000000000, rhodok_face_middle_2],
  ["knight_6_17", "Emir Arjah", "Arjah", tf_hero, 0, reserved,  fac_kingdom_6, [itm_saracin_hard_horses_d_v1,itm_mkk_infantry_armor_b,itm_sarranid_boots_c,itm_mkk_leather_boots_b,itm_mkk_gulam_helm_b, itm_mkk_gloves_a,itm_heavy_lance, itm_sarranid_cavalry_sword,itm_tab_shield_small_round_c],     knight_attrib_2,wp(150),knight_skills_2, 0x0000000aff0c034920db6dcadb6dbef600000000001dd6f80000000000000000, rhodok_face_old_2],
  ["knight_6_18", "Emir Sayli", "Sayli", tf_hero, 0, reserved,  fac_kingdom_6, [itm_saracin_hard_horses_c_v1,itm_mkk_archer_armor_a,itm_sarranid_boots_c,itm_mkk_leather_boots_a,itm_mkk_gulam_helm_c, itm_mkk_gloves_a,itm_heavy_lance, itm_sarranid_cavalry_sword,itm_tab_shield_small_round_c],    knight_attrib_3,wp(180),knight_skills_3, 0x0000000aff0c134820db6dcadb6dbef600000000001dd6f80000000000000000, rhodok_face_older_2],
  ["knight_6_19", "Emir Bami", "Bami", tf_hero, 0, reserved,  fac_kingdom_6, [itm_saracin_hard_horses_b_v1,itm_mkk_archer_armor_b,itm_sarranid_boots_c,itm_mkk_leather_boots_a,itm_mkk_gulam_helm_d, itm_mkk_gloves_a,itm_heavy_lance, itm_sarranid_cavalry_sword,itm_tab_shield_small_round_c],   knight_attrib_4,wp(210),knight_skills_4|knows_trainer_5, 0x0000000aff0c328720db6dcadb6dbef600000000001dd6f80000000000000000, rhodok_face_older_2],
  ["knight_6_20", "Emir Makka", "Makka", tf_hero, 0, reserved,  fac_kingdom_6, [itm_saracin_hard_horses_a_v1,itm_mkk_archer_armor_c,itm_sarranid_boots_c,itm_mkk_leather_boots_b,itm_mkk_gulam_helm_a, itm_mkk_gloves_a,itm_heavy_lance, itm_sarranid_cavalry_sword,itm_tab_shield_small_round_c],  knight_attrib_5,wp(240),knight_skills_5|knows_trainer_6, 0x0000000ac00c624620db6dcadb6dbef600000000001dd6f80000000000000000, rhodok_face_older_2],

  ["knight_7_1", "Duke Evelyn Silvermoor", "Evelyn", tf_hero, 0, reserved, fac_kingdom_7, [itm_mt_horse_b3, itm_tabard, itm_m_hose_a, itm_m_greaves_a, itm_m_brigandine_a, itm_m_gauntlets_b, itm_longsword, itm_steel_shield, itm_m_sallet_black_a, itm_jarid, itm_heavy_lance], knight_attrib_5,wp(250),knight_skills_5, 0x0000000e4408239436db6db6db6dddad00000000001db6fb0000000000000000, rhodok_face_older_2],
  ["knight_7_2", "Duke Roland Stormcrest", "Roland", tf_hero, 0, reserved, fac_kingdom_7, [itm_mt_horse_b3, itm_tabard, itm_m_hose_a, itm_m_greaves_a, itm_m_brigandine_a, itm_m_gauntlets_b, itm_longsword, itm_steel_shield, itm_m_sallet_black_a, itm_jarid, itm_heavy_lance], knight_attrib_5,wp(250),knight_skills_5, 0x0000000c4408335336db6db6db6dddad00000000001db6f80000000000000000, rhodok_face_older_2],
  ["knight_7_3", "Duke Hugo Stonehelm", "Hugo", tf_hero, 0, reserved, fac_kingdom_7, [itm_mt_horse_b3, itm_tabard, itm_m_hose_a, itm_m_greaves_a, itm_m_brigandine_a, itm_m_gauntlets_b, itm_longsword, itm_steel_shield, itm_m_sallet_black_a, itm_jarid, itm_heavy_lance], knight_attrib_5,wp(250),knight_skills_5, 0x0000000fc408431137db6db6db0dfdb600000000001db6f80000000000000000, rhodok_face_older_2],
  ["knight_7_4", "Duke Cedric Ironwood", "Cedric", tf_hero, 0, reserved, fac_kingdom_7, [itm_mt_horse_b3, itm_tabard, itm_m_hose_a, itm_m_greaves_a, itm_m_brigandine_a, itm_m_gauntlets_b, itm_longsword, itm_steel_shield, itm_m_sallet_black_a, itm_jarid, itm_heavy_lance], knight_attrib_5,wp(250),knight_skills_5, 0x00000003840802cf06db6db6db6ddffe00000000001db6f80000000000000000, rhodok_face_older_2],
  ["knight_7_5", "Duke Aldric Blackwater", "Aldric", tf_hero, 0, reserved, fac_kingdom_7, [itm_mt_horse_b3, itm_tabard, itm_m_hose_b, itm_m_greaves_a, itm_m_brigandine_b, itm_m_gauntlets_a, itm_military_cleaver_c, itm_steel_shield, itm_m_sallet_black_a, itm_throwing_knives, itm_lance], knight_attrib_5,wp(250),knight_skills_5, 0x000000038408129106db6db6db6ddffe00000000001db6f80000000000000000, rhodok_face_older_2],
  ["knight_7_6", "Duke Thaddeus Ravenshore", "Thaddeus", tf_hero, 0, reserved, fac_kingdom_7, [itm_mt_horse_b3, itm_tabard, itm_m_hose_b, itm_m_greaves_b, itm_m_brigandine_b, itm_m_gauntlets_a, itm_grosse_messer_b, itm_steel_shield, itm_m_sallet_black_a, itm_throwing_knives, itm_lance], knight_attrib_5,wp(250),knight_skills_5, 0x00000003800822c904db6db6db6ddffe00000000001fb6f80000000000000000, rhodok_face_older_2],
  ["knight_7_7", "Duke Leopold Goldenfield", "Leopold", tf_hero, 0, reserved, fac_kingdom_7, [itm_mt_horse_b3, itm_tabard, itm_m_hose_b, itm_m_greaves_b, itm_m_brigandine_b, itm_m_gauntlets_a, itm_military_cleaver_b, itm_steel_shield, itm_m_sallet_black_a, itm_throwing_knives, itm_lance], knight_attrib_5,wp(250),knight_skills_5, 0x0000000bbf08248536db6db6db6debad00000000001db6db0000000000000000, rhodok_face_older_2],
  ["knight_7_8", "Duke Magnus Stormpeak", "Magnus", tf_hero, 0, reserved, fac_kingdom_7, [itm_mt_horse_b3, itm_tabard, itm_m_hose_b, itm_m_greaves_b, itm_m_brigandine_b, itm_m_gauntlets_a, itm_grosse_messer_b, itm_tab_shield_pavise_d, itm_m_sallet_black_a, itm_throwing_knives, itm_lance], knight_attrib_5,wp(250),knight_skills_5, 0x0000000e8008344f36db6db6db6debad00000000001db6fb0000000000000000, rhodok_face_older_2],

  # younger knights  
  ["knight_7_9", "Duke Ashton", "Ashton", tf_hero, 0, reserved,  fac_kingdom_7, [itm_mt_horse_b3, itm_tabard, itm_m_hose_b, itm_m_greaves_a, itm_m_brigandine_a, itm_m_gauntlets_a, itm_longsword, itm_shield_heater_d, itm_m_chapel_heavy_c, itm_throwing_knives, itm_lance],    knight_attrib_3,wp(160),knight_skills_3, 0x0000000ac400314520db6db6db6dfcff00000000001db6f80000000000000000, swadian_face_old_2],
  ["knight_7_10", "Duke Zelenn", "Zelenn", tf_hero, 0, reserved,  fac_kingdom_7, [itm_mt_horse_b3, itm_tabard, itm_m_hose_b, itm_m_greaves_a, itm_m_brigandine_b, itm_m_gauntlets_a, itm_longsword, itm_shield_heater_d, itm_m_sallet_black_a, itm_lance],   knight_attrib_3,wp(190),knight_skills_3, 0x0000000ac400418620db6db6db6dfcff00000000001db6f80000000000000000, swadian_face_older_2],
  ["knight_7_11", "Duke Cangann", "Cangann", tf_hero, 0, reserved,  fac_kingdom_7, [itm_mt_horse_b3, itm_tabard, itm_m_hose_b, itm_m_greaves_b, itm_m_brigandine_c, itm_m_gauntlets_a, itm_longsword, itm_tab_shield_pavise_d, itm_m_chapel_heavy_a, itm_lance],       knight_attrib_3,wp(220),knight_skills_3, 0x0000000ac00071c620db6db6db6dfcff00000000001db6f80000000000000000, swadian_face_older_2],
  ["knight_7_12", "Duke Yrosh", "Yrosh", tf_hero, 0, reserved,  fac_kingdom_7, [itm_mt_horse_b3, itm_tabard, itm_m_hose_b, itm_m_greaves_b, itm_m_brigandine_b, itm_m_gauntlets_a, itm_longsword, itm_tab_shield_pavise_d, itm_m_chapel_heavy_b, itm_lance],    knight_attrib_3,wp(130),knight_skills_3, 0x0000000ac00020c520db6db6db6dfcff00000000001db6f80000000000000000, swadian_face_older_2],
  ["knight_7_13", "Duke Liber", "Liber", tf_hero, 0, reserved,  fac_kingdom_7, [itm_mt_horse_b3, itm_tabard, itm_m_hose_b, itm_m_greaves_b, itm_m_brigandine_c, itm_m_gauntlets_a, itm_grosse_messer_b, itm_tab_shield_pavise_d, itm_m_chapel_heavy_a, itm_war_darts, itm_lance],   knight_attrib_2,wp(160),knight_skills_2, 0x0000000afd00314420db6db6db6dfcff00000000001db6f80000000000000000, swadian_face_older_2],
  ["knight_7_14", "Duke George", "George", tf_hero, 0, reserved,  fac_kingdom_7, [itm_mt_horse_b3, itm_tabard, itm_m_hose_b, itm_m_greaves_b, itm_m_hauberk_c, itm_m_gauntlets_a, itm_side_sword, itm_steel_shield, itm_m_chapel_heavy_c, itm_war_darts, itm_lance],    knight_attrib_2,wp(190),knight_skills_3|knows_trainer_6, 0x0000000ac000028420db6db6db6dfcff00000000001db6f80000000000000000, swadian_face_older_2],
  ["knight_7_15", "Duke Jay", "Jay", tf_hero, 0, reserved,  fac_kingdom_7, [itm_mt_horse_b3, itm_tabard, itm_m_hose_b, itm_m_leather_boots_a, itm_m_hauberk_c, itm_m_gauntlets_a, itm_side_sword, itm_shield_heater_d, itm_m_kattle_a, itm_war_darts, itm_lance],      knight_attrib_4,wp(140),knight_skills_2, 0x0000000afd00629420db6db6db6dfcff00000000001db6f80000000000000000, swadian_face_young_2],
  ["knight_7_16", "Duke Itreth", "Itreth", tf_hero, 0, reserved,  fac_kingdom_7, [itm_mt_horse_b3, itm_tabard, itm_m_hose_b, itm_m_leather_boots_a, itm_m_brigandine_d, itm_m_gauntlets_a, itm_side_sword, itm_shield_heater_d, itm_m_chapel_light_a, itm_darts, itm_lance],   knight_attrib_1,wp(130),knight_skills_2, 0x0000000afd00520020db6db6db6dfcff00000000001db6f80000000000000000, swadian_face_young_2],
  ["knight_7_17", "Duke Zac", "Zac", tf_hero, 0, reserved,  fac_kingdom_7, [itm_mt_horse_b3, itm_tabard, itm_m_hose_b, itm_m_leather_boots_a, itm_m_brigandine_e, itm_m_gloves_a, itm_grosse_messer_b, itm_shield_heater_d, itm_m_chapel_light_b, itm_darts, itm_lance],    knight_attrib_2,wp(190),knight_skills_1|knows_trainer_4, 0x0000000ac40021c620db6db6db6dfcff00000000001db6f80000000000000000, swadian_face_young_2],
  ["knight_7_18", "Duke Hudson", "Hudson", tf_hero, 0, reserved,  fac_kingdom_7, [itm_mt_horse_b3, itm_tabard, itm_m_hose_b, itm_m_leather_boots_a, itm_m_hauberk_a, itm_m_gloves_a, itm_crusader_sword, itm_steel_shield, itm_m_kattle_a, itm_lance],   knight_attrib_3,wp(210),knight_skills_1, 0x0000000ac400320a20db6db6db6dfcff00000000001db6f80000000000000000, swadian_face_young_2],
  ["knight_7_19", "Duke Lommas", "Lommas", tf_hero, 0, reserved,  fac_kingdom_7, [itm_mt_horse_b3, itm_tabard, itm_m_hose_b, itm_m_leather_boots_a, itm_m_hauberk_b, itm_m_gloves_a, itm_crusader_sword, itm_steel_shield, itm_m_chapel_light_b, itm_lance],    knight_attrib_1,wp(120),knight_skills_1, 0x0000000ac400424720db6db6db6dfcff00000000001db6f80000000000000000, swadian_face_young_2],
  ["knight_7_20", "Duke Jazo", "Jazo", tf_hero, 0, reserved,  fac_kingdom_7, [itm_mt_horse_b3, itm_tabard, itm_m_hose_b, itm_m_leather_boots_a, itm_m_hauberk_c, itm_m_gauntlets_b, itm_crusader_sword, itm_steel_shield, itm_m_chapel_light_c, itm_lance],   knight_attrib_2,wp(150),knight_skills_1, 0x0000000ac400528820db6db6db6dfcff00000000001db6f80000000000000000, swadian_face_young_2],

  ["knight_8_1", "Chieftain Kael Bloodclaw", "Kael", tf_hero, 0, reserved, fac_kingdom_8, [itm_mh_horse_a, itm_tabard, itm_khergit_leather_boots, itm_mt_scale_gloves_a, itm_mh_armor_heavy_a, itm_mh_helmet_heavy_a, itm_javelin, itm_mh_spear_a, itm_plate_covered_round_shield, itm_mh_sword_a], knight_attrib_5,wp(250),knight_skills_5, 0x0000000e8008344f36db6db6db6debad00000000001db6fb0000000000000000, rhodok_face_older_2],
  ["knight_8_2", "Chieftain Tatsuya Flameheart", "Tatsuya", tf_hero, 0, reserved, fac_kingdom_8, [itm_mh_horse_b, itm_tabard, itm_khergit_leather_boots, itm_mt_scale_gloves_b, itm_mh_armor_heavy_a, itm_mh_helmet_medium_b, itm_throwing_spears, itm_mh_pike_a, itm_plate_covered_round_shield, itm_mh_sword_a], knight_attrib_5,wp(250),knight_skills_5, 0x0000000e400401c636db6db6db6db6db00000000001db6db0000000000000000, rhodok_face_older_2],
  ["knight_8_3", "Chieftain Akira Stormcaller", "Akira", tf_hero, 0, reserved, fac_kingdom_8, [itm_mh_horse_c, itm_tabard, itm_m_leather_boots_a, itm_mt_scale_gloves_a, itm_mh_armor_heavy_a, itm_mh_helmet_medium_a, itm_javelin, itm_mh_pike_b, itm_plate_covered_round_shield, itm_mh_sword_a], knight_attrib_5,wp(250),knight_skills_5, 0x0000000e7f041386061e69d89b6dbef700000000001dc6f80000000000000000, rhodok_face_older_2],
  ["knight_8_4", "Chieftain Haru Ironhoof", "Haru", tf_hero, 0, reserved, fac_kingdom_8, [itm_mh_horse_d, itm_tabard, itm_khergit_leather_boots, itm_mt_scale_gloves_a, itm_mh_armor_heavy_a, itm_mh_helmet_heavy_a, itm_javelin, itm_mh_spear_a, itm_plate_covered_round_shield, itm_mh_sword_a], knight_attrib_5,wp(250),knight_skills_5, 0x0000000e7f042345061e69d89b6dbef700000000001dc6f80000000000000000, rhodok_face_older_2],
  ["knight_8_5", "Chieftain Takeshi Silentclaw", "Takeshi", tf_hero, 0, reserved, fac_kingdom_8, [itm_mh_horse_e, itm_tabard, itm_m_leather_boots_a, itm_mt_scale_gloves_a, itm_mh_armor_heavy_a, itm_mh_helmet_heavy_a, itm_javelin, itm_mh_pike_a, itm_plate_covered_round_shield, itm_mh_sword_a], knight_attrib_5,wp(250),knight_skills_5, 0x0000000e7f0411ca061e69d89b6dbef700000000001dc6f80000000000000000, rhodok_face_older_2],
  ["knight_8_6", "Chieftain Hiro Wildheart", "Hiro", tf_hero, 0, reserved, fac_kingdom_8, [itm_mh_horse_b, itm_tabard, itm_m_leather_boots_a, itm_mt_scale_gloves_a, itm_mh_armor_heavy_a, itm_mh_helmet_medium_a, itm_javelin, itm_mh_spear_a, itm_plate_covered_round_shield, itm_mh_sword_a], knight_attrib_5,wp(250),knight_skills_5, 0x0000000e7f0421c9061e69d89b6dbef700000000001dc6f80000000000000000, rhodok_face_older_2],
  ["knight_8_7", "Chieftain Yukio Frostblade", "Yukio", tf_hero, 0, reserved, fac_kingdom_8, [itm_mh_horse_a, itm_tabard, itm_m_leather_boots_a, itm_mt_scale_gloves_a, itm_mh_armor_heavy_a, itm_mh_helmet_medium_b, itm_throwing_spears, itm_mh_pike_b, itm_plate_covered_round_shield, itm_mh_sword_a], knight_attrib_5,wp(250),knight_skills_5, 0x0000000e7f042188061e69d89b6dbef700000000001dc6f80000000000000000, rhodok_face_older_2],
  ["knight_8_8", "Chieftain Kenta Stormfury", "Kenta", tf_hero, 0, reserved, fac_kingdom_8, [itm_mh_horse_c, itm_tabard, itm_m_leather_boots_a, itm_m_gloves_a, itm_mh_armor_heavy_a, itm_mh_helmet_heavy_a, itm_throwing_spears, itm_mh_spear_a, itm_plate_covered_round_shield, itm_mh_sword_a], knight_attrib_5,wp(250),knight_skills_5, 0x0000000e7f0405c6061e69d89b6dbef700000000001dc6f80000000000000000, rhodok_face_older_2],

  # younger knights
  ["knight_8_9", "Chieftain Ninezzuu", "Ninezzuu", tf_hero, 0, reserved, fac_kingdom_8, [itm_mh_horse_b, itm_tabard, itm_khergit_leather_boots, itm_m_gloves_a, itm_mh_armor_lamellar_a, itm_mh_helmet_medium_a, itm_javelin, itm_plate_covered_round_shield, itm_mh_sword_a],    knight_attrib_3,wp(160),knight_skills_3, 0x0000000e7f046554061e69d89b6dbef700000000001dc6f80000000000000000, swadian_face_old_2],
  ["knight_8_10", "Chieftain Ningusu", "Ningusu", tf_hero, 0, reserved, fac_kingdom_8, [itm_mh_horse_c, itm_tabard, itm_khergit_leather_boots, itm_m_gloves_a, itm_mh_armor_mail_a, itm_mh_helmet_medium_a, itm_javelin, itm_plate_covered_round_shield, itm_mh_sword_a],   knight_attrib_3,wp(190),knight_skills_3, 0x0000000e7f045450061e69d89b6dbef700000000001dc6f80000000000000000, swadian_face_older_2],
  ["knight_8_11", "Chieftain Nabu", "Nabu", tf_hero, 0, reserved, fac_kingdom_8, [itm_mh_horse_e, itm_tabard, itm_m_leather_boots_a, itm_m_gloves_a, itm_mh_armor_mail_a, itm_mh_helmet_medium_a, itm_javelin, itm_plate_covered_round_shield, itm_mh_sword_a],       knight_attrib_3,wp(220),knight_skills_3, 0x0000000e7f044448061e69d89b6dbef700000000001dc6f80000000000000000, swadian_face_older_2],
  ["knight_8_12", "Chieftain Ammardum", "Ammardum", tf_hero, 0, reserved, fac_kingdom_8, [itm_mh_horse_d, itm_tabard, itm_m_leather_boots_a, itm_mt_scale_gloves_a, itm_mh_armor_mail_b, itm_mh_helmet_medium_a, itm_javelin, itm_plate_covered_round_shield, itm_mh_sword_a],    knight_attrib_3,wp(130),knight_skills_3, 0x0000000e7f0443c6061e69d89b6dbef700000000001dc6f80000000000000000, swadian_face_older_2],
  ["knight_8_13", "Chieftain Nina", "Nina", tf_hero, 0, reserved, fac_kingdom_8, [itm_mh_horse_a, itm_tabard, itm_m_leather_boots_a, itm_mt_scale_gloves_a, itm_mh_armor_mail_a, itm_mh_helmet_medium_b, itm_javelin, itm_plate_covered_round_shield, itm_mh_sword_a],   knight_attrib_2,wp(160),knight_skills_2, 0x0000000e7f043383061e69d89b6dbef700000000001dc6f80000000000000000, swadian_face_older_2],
  ["knight_8_14", "Chieftain Adarar", "Adarar", tf_hero, 0, reserved, fac_kingdom_8, [itm_mh_horse_b, itm_tabard, itm_m_leather_boots_a, itm_mt_scale_gloves_a, itm_mh_armor_lamellar_c, itm_mh_helmet_medium_b, itm_javelin, itm_plate_covered_round_shield, itm_mh_sword_a],    knight_attrib_2,wp(190),knight_skills_3|knows_trainer_6, 0x0000000e7f042342061e69d89b6dbef700000000001dc6f80000000000000000, swadian_face_older_2],
  ["knight_8_15", "Chieftain Adus", "Adus", tf_hero, 0, reserved, fac_kingdom_8, [itm_mh_horse_e, itm_tabard, itm_m_leather_boots_a, itm_mt_scale_gloves_a, itm_mh_armor_mail_a, itm_mh_helmet_medium_b, itm_javelin, itm_plate_covered_round_shield, itm_mh_sword_a],      knight_attrib_4,wp(140),knight_skills_2, 0x0000000e7f041300061e69d89b6dbef700000000001dc6f80000000000000000, swadian_face_young_2],
  ["knight_8_16", "Chieftain Nezzu", "Nezzu", tf_hero, 0, reserved, fac_kingdom_8, [itm_mh_horse_b, itm_tabard, itm_khergit_leather_boots, itm_mt_scale_gloves_a, itm_mh_armor_mail_b, itm_mh_helmet_medium_b, itm_javelin, itm_plate_covered_round_shield, itm_mh_sword_a],   knight_attrib_1,wp(130),knight_skills_2, 0x0000000e630402d4061e69d89b6dbef700000000001dc6f80000000000000000, swadian_face_young_2],
  ["knight_8_17", "Chieftain Nebilu", "Nebilu", tf_hero, 0, reserved, fac_kingdom_8, [itm_mh_horse_e, itm_tabard, itm_khergit_leather_boots, itm_mt_scale_gloves_b, itm_mh_armor_mail_c, itm_mh_helmet_medium_b, itm_javelin, itm_mh_spear_a, itm_plate_covered_round_shield, itm_mh_sword_a],    knight_attrib_2,wp(190),knight_skills_1|knows_trainer_4, 0x0000000e63046294061e69d89b6dbef700000000001dc6f80000000000000000, swadian_face_young_2],
  ["knight_8_18", "Chieftain Maamuzi", "Maamuzi", tf_hero, 0, reserved, fac_kingdom_8, [itm_mh_horse_c, itm_tabard, itm_m_leather_boots_a, itm_mt_scale_gloves_b, itm_mh_armor_mail_a, itm_mh_helmet_medium_a, itm_mh_spear_a, itm_plate_covered_round_shield, itm_mh_sword_a],   knight_attrib_3,wp(210),knight_skills_1, 0x0000000e63044251061e69d89b6dbef700000000001dc6f80000000000000000, swadian_face_young_2],
  ["knight_8_19", "Chieftain Annikan", "Annikan", tf_hero, 0, reserved, fac_kingdom_8, [itm_mh_horse_c, itm_tabard, itm_khergit_leather_boots, itm_mt_scale_gloves_b, itm_mh_armor_mail_b, itm_mh_helmet_medium_a, itm_mh_spear_a, itm_plate_covered_round_shield, itm_mh_sword_a],    knight_attrib_1,wp(120),knight_skills_1, 0x0000000e630431cb061e69d89b6dbef700000000001dc6f80000000000000000, swadian_face_young_2],
  ["knight_8_20", "Chieftain Milkadea", "Milkadea", tf_hero, 0, reserved, fac_kingdom_8, [itm_mh_horse_e, itm_tabard, itm_m_leather_boots_a, itm_mt_scale_gloves_a, itm_mh_armor_mail_c, itm_mh_helmet_medium_a, itm_mh_spear_a, itm_plate_covered_round_shield, itm_mh_sword_a],   knight_attrib_2,wp(150),knight_skills_1, 0x0000000e7f04228b061e69d89b6dbef700000000001dc6f80000000000000000, swadian_face_young_2],

  ["knight_9_1", "Knight Jamond", "Jamond", tf_hero, 0, reserved, fac_kingdom_9,[itm_m_hose_b, itm_rich_outfit, itm_mt_greaves_a, itm_mt_heavy_plate_a, itm_mt_gauntlets_a, itm_mt_knight_helm_a, itm_mt_horse_b, itm_great_lance, itm_shield_heater_d, itm_crusader_sword],knight_attrib_5,wp(350),knight_skills_5|knows_trainer_5|knows_ironflesh_10|knows_riding_10, 0x000000018004054626db6db6db6dbeff00000000001db6eb0000000000000000,swadian_face_older_2],
  ["knight_9_2", "Knight Wearda", "Wearda", tf_hero, 0, reserved, fac_kingdom_9,[itm_m_hose_b, itm_rich_outfit, itm_mt_greaves_a, itm_mt_heavy_plate_a2, itm_mt_gauntlets_a, itm_mt_knight_helm_b, itm_mt_horse_b, itm_great_lance, itm_shield_heater_d, itm_crusader_sword],knight_attrib_5,wp(350),knight_skills_5|knows_trainer_5|knows_ironflesh_10|knows_riding_10, 0x000000018004150526db6db6db6dbeff00000000001db6e30000000000000000,swadian_face_older_2],
  ["knight_9_3", "Knight Wealdther", "Wealdther", tf_hero, 0, reserved, fac_kingdom_9,[itm_m_hose_b, itm_rich_outfit, itm_mt_greaves_a, itm_mt_heavy_plate_a, itm_mt_gauntlets_a2, itm_mt_knight_helm_c, itm_mt_horse_b2, itm_great_lance, itm_shield_heater_d, itm_crusader_sword],knight_attrib_5,wp(350),knight_skills_5|knows_trainer_5|knows_ironflesh_10|knows_riding_10, 0x000000018004058426db6db6db6dbeff00000000001db6e30000000000000000,swadian_face_older_2],
  ["knight_9_4", "Knight Eallan", "Eallan", tf_hero, 0, reserved, fac_kingdom_9,[itm_m_hose_b, itm_rich_outfit, itm_mt_greaves_a, itm_mt_heavy_plate_a2, itm_mt_gauntlets_a, itm_mt_knight_helm_a, itm_mt_horse_b2, itm_great_lance, itm_shield_heater_d, itm_morningstar],knight_attrib_5,wp(350),knight_skills_5|knows_trainer_5|knows_ironflesh_10|knows_riding_10, 0x000000018004249426db6db6db6dbeff00000000001db6e30000000000000000,swadian_face_older_2],
  ["knight_9_5", "Knight Ichohn", "Ichohn", tf_hero, 0, reserved, fac_kingdom_9,[itm_m_hose_b, itm_rich_outfit, itm_mt_greaves_g, itm_mt_heavy_plate_a2, itm_mt_gauntlets_a, itm_mt_knight_helm_b, itm_mt_horse_b2, itm_great_lance, itm_shield_heater_d, itm_crusader_sword],knight_attrib_5,wp(350),knight_skills_5|knows_trainer_5|knows_ironflesh_10|knows_riding_10, 0x000000018004245226db6db6db6dbeff00000000001db6e30000000000000000,swadian_face_older_2],
  ["knight_9_6", "Knight Hony Pycey", "Hony Pycey", tf_hero, 0, reserved, fac_kingdom_9,[itm_m_hose_b, itm_rich_outfit, itm_mt_greaves_g, itm_mt_heavy_plate_a2, itm_mt_gauntlets_b, itm_mt_knight_helm_b, itm_mt_horse_b, itm_great_lance, itm_shield_heater_d, itm_crusader_sword],knight_attrib_5,wp(350),knight_skills_5|knows_trainer_5|knows_ironflesh_10|knows_riding_10, 0x000000018004041026db6db6db6dbeff00000000001db6e30000000000000000,swadian_face_older_2],
  ["knight_9_7", "Knight Behrtio", "Behrtio", tf_hero, 0, reserved, fac_kingdom_9,[itm_m_hose_b, itm_rich_outfit, itm_mt_greaves_g, itm_mt_heavy_plate_a, itm_mt_gauntlets_a, itm_mt_knight_helm_a, itm_mt_horse_b, itm_great_lance, itm_shield_heater_d, itm_crusader_sword],knight_attrib_5,wp(350),knight_skills_5|knows_trainer_5|knows_ironflesh_10|knows_riding_10, 0x00000001800405c526db6db6db6dbeff00000000001db6e30000000000000000,swadian_face_older_2],
  ["knight_9_8", "Knight Ulfrith", "Ulfrith", tf_hero, 0, reserved, fac_kingdom_9,[itm_m_hose_b, itm_rich_outfit, itm_mt_greaves_a, itm_mt_heavy_plate_a, itm_mt_gauntlets_b, itm_mt_knight_helm_c, itm_mt_horse_b, itm_great_lance, itm_shield_heater_d, itm_crusader_sword],knight_attrib_5,wp(350),knight_skills_5|knows_trainer_5|knows_ironflesh_10|knows_riding_10, 0x000000018004114426db6db6db6dbeff00000000001db6e30000000000000000,swadian_face_older_2],

  # younger knights
  ["knight_9_9", "Knight Debeorht", "Debeorht", tf_hero, 0, reserved, fac_kingdom_9, [itm_m_hose_b, itm_rich_outfit, itm_mt_greaves_g, itm_mt_heavy_plate_c, itm_mt_gauntlets_a, itm_mt_full_helm_c, itm_mt_horse_b, itm_guisarme, itm_practice_board_shield, itm_military_pick],    knight_attrib_3,wp(160),knight_skills_3, 0x000000018004218526db6db6db6dbeff00000000001db6e30000000000000000, swadian_face_old_2],
  ["knight_9_10", "Knight Eorcald", "Eorcald", tf_hero, 0, reserved, fac_kingdom_9, [itm_m_hose_b, itm_rich_outfit, itm_mt_greaves_a, itm_mt_heavy_plate_c, itm_mt_gauntlets_a2, itm_mt_sallet_a2, itm_mt_horse_b, itm_great_lance, itm_shield_heater_d, itm_crusader_sword],   knight_attrib_3,wp(190),knight_skills_3, 0x000000018004128526db6db6db6dbeff00000000001db6e30000000000000000, swadian_face_older_2],
  ["knight_9_11", "Knight Robern Quinte", "Robern Quinte", tf_hero, 0, reserved, fac_kingdom_9, [itm_m_hose_b, itm_rich_outfit, itm_mt_greaves_a, itm_mt_heavy_plate_c, itm_mt_gauntlets_a2, itm_mt_bascinet_b, itm_mt_horse_b, itm_great_lance, itm_shield_heater_d, itm_military_pick],       knight_attrib_3,wp(220),knight_skills_3, 0x00000001800402d426db6db6db6dbeff00000000001db6e30000000000000000, swadian_face_older_2],
  ["knight_9_12", "Knight Jamart", "Jamart", tf_hero, 0, reserved, fac_kingdom_9, [itm_m_hose_b, itm_rich_outfit, itm_mt_greaves_c, itm_mt_heavy_plate_a2, itm_mt_gauntlets_b, itm_mt_sallet_a, itm_mt_horse_b, itm_great_lance, itm_shield_heater_d, itm_military_pick],       knight_attrib_3,wp(220),knight_skills_3, 0x000000018004014826db6db6db6dbeff00000000001db6e30000000000000000, swadian_face_older_2],
  ["knight_9_13", "Knight Chury", "Chury", tf_hero, 0, reserved, fac_kingdom_9, [itm_m_hose_b, itm_rich_outfit, itm_mt_greaves_c, itm_mt_heavy_plate_c, itm_mt_gauntlets_b, itm_mt_bascinet_b, itm_mt_horse_b, itm_great_lance, itm_shield_heater_d, itm_military_pick],       knight_attrib_3,wp(220),knight_skills_3, 0x000000018004210526db6db6db6dbeff00000000001db6e30000000000000000, swadian_face_older_2],
  ["knight_9_14", "Knight Aered", "Aered", tf_hero, 0, reserved, fac_kingdom_9, [itm_m_hose_b, itm_rich_outfit, itm_mt_greaves_c, itm_mt_heavy_plate_c, itm_mt_gauntlets_b, itm_mt_bascinet_b, itm_mt_horse_b, itm_great_lance, itm_shield_heater_d, itm_military_pick],       knight_attrib_3,wp(220),knight_skills_3, 0x00000001800410c426db6db6db6dbeff00000000001db6e30000000000000000, swadian_face_older_2],
  ["knight_9_15", "Knight Wige", "Wige", tf_hero, 0, reserved, fac_kingdom_9, [itm_m_hose_b, itm_rich_outfit, itm_mt_greaves_a, itm_mt_heavy_plate_a2, itm_mt_gauntlets_b, itm_mt_bascinet_b2, itm_mt_horse_b, itm_great_lance, itm_shield_heater_d, itm_crusader_sword],       knight_attrib_3,wp(220),knight_skills_3, 0x000000018004009426db6db6db6dbeff00000000001db6e30000000000000000, swadian_face_older_2],
  ["knight_9_16", "Knight Wine", "Wine", tf_hero, 0, reserved, fac_kingdom_9, [itm_m_hose_b, itm_rich_outfit, itm_mt_greaves_g, itm_mt_heavy_plate_a, itm_mt_gauntlets_a2, itm_mt_bascinet_b, itm_mt_horse_b, itm_great_lance, itm_shield_heater_d, itm_crusader_sword],       knight_attrib_3,wp(220),knight_skills_3, 0x000000018004205426db6db6db6dbeff00000000001db6e30000000000000000, swadian_face_older_2],
  ["knight_9_17", "Knight Freward", "Freward", tf_hero, 0, reserved, fac_kingdom_9, [itm_m_hose_b, itm_rich_outfit, itm_mt_greaves_g, itm_mt_heavy_plate_a2, itm_mt_gauntlets_b, itm_mt_bascinet_d, itm_mt_horse_b, itm_great_lance, itm_shield_heater_d, itm_crusader_sword],       knight_attrib_3,wp(220),knight_skills_3, 0x000000018004000626db6db6db6dbeff00000000001db6e30000000000000000, swadian_face_older_2],
  ["knight_9_18", "Knight Ceolfre", "Ceolfre", tf_hero, 0, reserved, fac_kingdom_9, [itm_m_hose_b, itm_rich_outfit, itm_mt_greaves_g, itm_mt_heavy_plate_a, itm_mt_gauntlets_b, itm_mt_bascinet_d, itm_mt_horse_b, itm_great_lance, itm_shield_heater_d, itm_crusader_sword],       knight_attrib_3,wp(220),knight_skills_3, 0x000000018004100526db6db6db6dbeff00000000001db6e30000000000000000, swadian_face_older_2],
  ["knight_9_19", "Knight Afod", "Afod", tf_hero, 0, reserved, fac_kingdom_9, [itm_m_hose_b, itm_rich_outfit, itm_mt_greaves_a, itm_mt_heavy_plate_a2, itm_mt_gauntlets_b, itm_mt_bascinet_d, itm_mt_horse_b, itm_great_lance, itm_shield_heater_d, itm_crusader_sword],       knight_attrib_3,wp(220),knight_skills_3, 0x00000001800425c526db6db6db6dbeff00000000001db6e30000000000000000, swadian_face_older_2],
  ["knight_9_20", "Knight Aethelm", "Aethelm", tf_hero, 0, reserved, fac_kingdom_9, [itm_m_hose_b, itm_rich_outfit, itm_mt_greaves_a, itm_mt_heavy_plate_a, itm_mt_gauntlets_b, itm_mt_bascinet_b, itm_mt_horse_b, itm_great_lance, itm_shield_heater_d, itm_crusader_sword],       knight_attrib_3,wp(220),knight_skills_3, 0x00000001800404c626db6db6db6dbeff00000000001db6e30000000000000000, swadian_face_older_2],

  ["knight_10_1", "Noble Egnor", "Egnor", tf_hero, 0, reserved, fac_kingdom_10,[itm_m_hose_b, itm_mt_coat_a, itm_mt_greaves_a, itm_mt_special_c, itm_m_gauntlets_b, itm_mt_armet_a2, itm_mt_horse_a, itm_ms_metal_shield_a, itm_side_sword, itm_danish_greatsword],knight_attrib_5,wp(350),knight_skills_5|knows_trainer_5|knows_ironflesh_10|knows_riding_10, 0x00000001aa10420721036db6d36e5efe00000000001db6f80000000000000000,swadian_face_older_2],
  ["knight_10_2", "Noble Golure", "Golure", tf_hero, 0, reserved, fac_kingdom_10,[itm_m_hose_b, itm_mt_coat_a, itm_mt_greaves_a, itm_mt_special_c, itm_m_gauntlets_b, itm_mt_armet_a2, itm_mt_horse_a, itm_tab_shield_kite_d, itm_side_sword, itm_danish_greatsword],knight_attrib_5,wp(350),knight_skills_5|knows_trainer_5|knows_ironflesh_10|knows_riding_10, 0x00000001aa10624821036db6d36e5efe00000000001db6f80000000000000000,swadian_face_older_2],
  ["knight_10_3", "Noble Finasaer", "Finasaer", tf_hero, 0, reserved, fac_kingdom_10,[itm_m_hose_b, itm_mt_coat_a, itm_mt_greaves_b, itm_mt_special_c, itm_m_gauntlets_b, itm_mt_armet_a, itm_mt_horse_a2, itm_tab_shield_kite_d, itm_milanese_sword, itm_glaive_a],knight_attrib_5,wp(350),knight_skills_5|knows_trainer_5|knows_ironflesh_10|knows_riding_10, 0x00000001bf10128821036db6d36e5efe00000000001db6f80000000000000000,swadian_face_older_2],
  ["knight_10_4", "Noble Mahtata", "Mahtata", tf_hero, 0, reserved, fac_kingdom_10,[itm_m_hose_b, itm_mt_coat_a, itm_mt_greaves_b, itm_mt_special_c, itm_m_gauntlets_b, itm_mt_armet_a, itm_mt_horse_a, itm_ms_metal_shield_a2, itm_side_sword, itm_danish_greatsword],knight_attrib_5,wp(350),knight_skills_5|knows_trainer_5|knows_ironflesh_10|knows_riding_10, 0x00000001bf1022c921036db6d36e5efe00000000001db6f80000000000000000,swadian_face_older_2],
  ["knight_10_5", "Noble Alatad", "Alatad", tf_hero, 0, reserved, fac_kingdom_10,[itm_m_hose_b, itm_mt_coat_a, itm_mt_greaves_b, itm_mt_special_c, itm_m_gauntlets_b, itm_mt_armet_a2, itm_mt_horse_a2, itm_tab_shield_kite_d, itm_side_sword, itm_danish_greatsword],knight_attrib_5,wp(350),knight_skills_5|knows_trainer_5|knows_ironflesh_10|knows_riding_10, 0x00000001bf10334a21036db6d36e5efe00000000001db6f80000000000000000,swadian_face_older_2],
  ["knight_10_6", "Noble Galinor", "Galinor", tf_hero, 0, reserved, fac_kingdom_10,[itm_m_hose_b, itm_mt_coat_a, itm_mt_greaves_b, itm_mt_special_c, itm_m_gauntlets_b, itm_mt_armet_a, itm_mt_horse_a2, itm_ms_metal_shield_a, itm_italian_falchion, itm_glaive_a],knight_attrib_5,wp(350),knight_skills_5|knows_trainer_5|knows_ironflesh_10|knows_riding_10, 0x00000001bf10419121036db6d36e5efe00000000001db6f80000000000000000,swadian_face_older_2],
  ["knight_10_7", "Noble Elelroth", "Elelroth", tf_hero, 0, reserved, fac_kingdom_10,[itm_m_hose_b, itm_mt_coat_a, itm_mt_greaves_a, itm_mt_special_c, itm_m_gauntlets_b, itm_mt_armet_a, itm_mt_horse_a2, itm_ms_metal_shield_a2, itm_italian_falchion, itm_glaive_a],knight_attrib_5,wp(350),knight_skills_5|knows_trainer_5|knows_ironflesh_10|knows_riding_10, 0x00000001bf1061d421036db6d36e5efe00000000001db6f80000000000000000,swadian_face_older_2],
  ["knight_10_8", "Noble Eliolad", "Eliolad", tf_hero, 0, reserved, fac_kingdom_10,[itm_m_hose_b, itm_mt_coat_a, itm_mt_greaves_a, itm_mt_special_b, itm_m_gauntlets_b, itm_mt_armet_a, itm_mt_horse_a, itm_ms_metal_shield_a3, itm_italian_falchion, itm_glaive_a],knight_attrib_5,wp(350),knight_skills_5|knows_trainer_5|knows_ironflesh_10|knows_riding_10, 0x00000001bf10121421036db6d36e5efe00000000001db6f80000000000000000,swadian_face_older_2],

  # younger knights
  ["knight_10_9", "Noble Olar", "Olar", tf_hero, 0, reserved, fac_kingdom_10, [itm_m_hose_b, itm_mt_coat_a, itm_mt_greaves_a, itm_mt_special_b, itm_m_gauntlets_b, itm_mt_armet_a2, itm_ms_metal_shield_a5, itm_side_sword, itm_danish_greatsword],    knight_attrib_3,wp(160),knight_skills_3, 0x00000001bf10228121036db6d36e5efe00000000001db6f80000000000000000, swadian_face_old_2],
  ["knight_10_10", "Noble Elelrol", "Elelrol", tf_hero, 0, reserved, fac_kingdom_10, [itm_m_hose_b, itm_mt_coat_a, itm_mt_greaves_a, itm_mt_special_b, itm_m_gauntlets_b, itm_mt_armet_a2, itm_tab_shield_kite_d, itm_longbowman_sword, itm_glaive_b],   knight_attrib_3,wp(190),knight_skills_3, 0x00000001bf10331421036db6d36e5efe00000000001db6f80000000000000000, swadian_face_older_2],
  ["knight_10_11", "Noble Legali", "Legali", tf_hero, 0, reserved, fac_kingdom_10, [itm_m_hose_b, itm_mt_coat_a, itm_mt_greaves_a, itm_mt_special_b, itm_m_gauntlets_b, itm_mt_armet_a2, itm_mt_horse_a, itm_tab_shield_kite_d, itm_longbowman_sword, itm_glaive_b],       knight_attrib_3,wp(220),knight_skills_3, 0x00000001801065c421036db6d36e5efe00000000001db6f80000000000000000, swadian_face_older_2],
  ["knight_10_12", "Noble Finrethel", "Finrethel", tf_hero, 0, reserved, fac_kingdom_10, [itm_m_hose_b, itm_mt_coat_a, itm_mt_greaves_a, itm_mt_special_b, itm_m_gauntlets_b, itm_mt_armet_a2, itm_mt_horse_a, itm_ms_metal_shield_a5, itm_longbowman_sword, itm_glaive_b],       knight_attrib_3,wp(220),knight_skills_3, 0x000000018010010621036db6d36e5efe00000000001db6f80000000000000000, swadian_face_older_2],
  ["knight_10_13", "Noble Eros", "Eros", tf_hero, 0, reserved, fac_kingdom_10, [itm_m_hose_b, itm_mt_coat_a, itm_mt_greaves_a, itm_mt_special_a, itm_m_gauntlets_b, itm_mt_armet_a2, itm_mt_horse_a, itm_ms_metal_shield_a, itm_longbowman_sword, itm_glaive_b],       knight_attrib_3,wp(220),knight_skills_3, 0x00000001801001c721036db6d36e5efe00000000001db6f80000000000000000, swadian_face_older_2],
  ["knight_10_14", "Noble Lathonel", "Lathonel", tf_hero, 0, reserved, fac_kingdom_10, [itm_m_hose_b, itm_mt_coat_a, itm_mt_greaves_a, itm_mt_special_a, itm_m_gauntlets_b, itm_mt_hood_a4, itm_tab_shield_kite_d, itm_side_sword, itm_glaive_b],       knight_attrib_3,wp(220),knight_skills_3, 0x000000018010228721036db6d36e5efe00000000001db6f80000000000000000, swadian_face_older_2],
  ["knight_10_15", "Noble Elror", "Elror", tf_hero, 0, reserved, fac_kingdom_10, [itm_m_hose_b, itm_mt_coat_a, itm_mt_greaves_a, itm_mt_special_a, itm_m_gauntlets_b, itm_mt_hood_a3, itm_tab_shield_kite_d, itm_side_sword, itm_danish_greatsword],       knight_attrib_3,wp(220),knight_skills_3, 0x000000018010128821036db6d36e5efe00000000001db6f80000000000000000, swadian_face_older_2],
  ["knight_10_16", "Noble Elethol", "Elethol", tf_hero, 0, reserved, fac_kingdom_10, [itm_m_hose_b, itm_mt_coat_a, itm_mt_greaves_a, itm_mt_special_a, itm_m_gauntlets_b, itm_mt_hood_a2, itm_ms_metal_shield_a, itm_side_sword, itm_danish_greatsword],       knight_attrib_3,wp(220),knight_skills_3, 0x000000018010724921036db6d36e5efe00000000001db6f80000000000000000, swadian_face_older_2],
  ["knight_10_17", "Noble Galebre", "Galebre", tf_hero, 0, reserved, fac_kingdom_10, [itm_m_hose_b, itm_mt_coat_a, itm_mt_greaves_a, itm_mt_special_a, itm_m_gauntlets_b, itm_mt_armet_a2, itm_mt_horse_a, itm_ms_metal_shield_a5, itm_side_sword, itm_danish_greatsword],       knight_attrib_3,wp(220),knight_skills_3, 0x0000000b8010414521036db6d36e5efe00000000001cd6f80000000000000000, swadian_face_older_2],
  ["knight_10_18", "Noble Goneli", "Goneli", tf_hero, 0, reserved, fac_kingdom_10, [itm_m_hose_b, itm_mt_coat_a, itm_m_leather_boots_a, itm_mt_leather_armor_c3, itm_m_gloves_a, itm_mt_hood_a, itm_ms_metal_shield_a2, itm_side_sword, itm_war_bow, itm_barbed_arrows],       knight_attrib_3,wp(220),knight_skills_3|knows_power_draw_8|knows_athletics_10, 0x00000001801031c521036db6d36e5efe00000000001db6f80000000000000000, swadian_face_older_2],
  ["knight_10_19", "Noble Alanwel", "Alanwel", tf_hero, 0, reserved, fac_kingdom_10, [itm_m_hose_b, itm_mt_coat_a, itm_m_leather_boots_a, itm_mt_leather_armor_c2, itm_m_gloves_a, itm_mt_hood_a2, itm_ms_metal_shield_a3, itm_side_sword, itm_war_bow, itm_bodkin_arrows],       knight_attrib_3,wp(220),knight_skills_3|knows_power_draw_8|knows_athletics_10, 0x0000000b8010318421036db6d36e5efe00000000001db6f80000000000000000, swadian_face_older_2],
  ["knight_10_20", "Noble Diredior", "Diredior", tf_hero, 0, reserved, fac_kingdom_10, [itm_m_hose_b, itm_mt_coat_a, itm_m_leather_boots_a, itm_mt_leather_armor_c3, itm_m_gloves_a, itm_mt_hood_a, itm_ms_metal_shield_a, itm_side_sword, itm_war_bow, itm_arrows],       knight_attrib_3,wp(220),knight_skills_3|knows_power_draw_8|knows_athletics_10, 0x000000018010720621036db6d36e5efe00000000001db6f80000000000000000, swadian_face_older_2],

  # Adid knights
  # knight_11_1 - Vizier Malik ibn Rahim
  # knight_11_2 - Vizier Khalid al-Qadir
  # knight_11_3 - Vizier Tariq ibn Ziyad
  # knight_11_4 - Vizier Zahir ibn al-Hakam
  # knight_11_5 - Vizier Faris al-Jabbar
  ["knight_11_1", "Vizier Malik ibn Rahim", "Malik", tf_hero, 0, reserved, fac_kingdom_11, [itm_ankle_boots, itm_shirt, itm_maa_camel_war_a, itm_maa_scale_b, itm_m_leather_boots_a, itm_mt_scale_gloves_a, itm_maa_mail_coif_b, itm_ms_hook_sword, itm_maa_camel_rider_shield_a], knight_attrib_5,wp(250),knight_skills_5, 0x0000000e8004615436db6dd79f6df92f00000000001db6eb0000000000000000, rhodok_face_older_2],
  ["knight_11_2", "Vizier Khalid al-Qadir", "Khalid", tf_hero, 0, reserved, fac_kingdom_11, [itm_ankle_boots, itm_shirt, itm_warhorse_sarranid, itm_maa_scale_a, itm_m_leather_boots_a, itm_mt_scale_gloves_a, itm_maa_mail_coif_a, itm_scimitar_b, itm_maa_camel_rider_shield_b], knight_attrib_5,wp(250),knight_skills_5, 0x0000000dff0471d314db6dd79f6df92f00000000001db6f80000000000000000, rhodok_face_older_2],
  ["knight_11_3", "Vizier Tariq ibn Ziyad", "Tariq", tf_hero, 0, reserved, fac_kingdom_11, [itm_ankle_boots, itm_shirt, itm_maa_camel_war_b, itm_maa_scale_a2, itm_m_leather_boots_a, itm_mt_scale_gloves_b, itm_maa_mail_coif_b, itm_scimitar_b, itm_maa_camel_rider_shield_b, itm_strong_bow, itm_barbed_arrows], knight_attrib_5,wp(250),knight_skills_5, 0x0000000da104728d34dba1d79f7dffff00000000001db73c0000000000000000, rhodok_face_older_2],
  ["knight_11_4", "Vizier Zahir ibn al-Hakam", "Zahir", tf_hero, 0, reserved, fac_kingdom_11, [itm_ankle_boots, itm_shirt, itm_warhorse_sarranid, itm_maa_heavy_scale_a, itm_m_leather_boots_a, itm_mt_scale_gloves_a, itm_maa_cavalry_a, itm_lance, itm_maa_round_shield_a, itm_scimitar_b], knight_attrib_5,wp(250),knight_skills_5, 0x0000000d8004634534db6daf9f6dfdb600000000001e493c0000000000000000, rhodok_face_older_2],
  ["knight_11_5", "Vizier Faris al-Jabbar", "Faris", tf_hero, 0, reserved, fac_kingdom_11, [itm_ankle_boots, itm_shirt, itm_maa_camel_war_c, itm_maa_scale_b, itm_m_leather_boots_a, itm_mt_scale_gloves_a, itm_maa_mail_coif_b, itm_sarranid_mace_1, itm_maa_camel_rider_shield_c, itm_hunting_crossbow, itm_steel_bolts], knight_attrib_5,wp(250),knight_skills_5, 0x0000000dff04644934db6dab176dff7f00000000001e4b3c0000000000000000, rhodok_face_older_2],
  ["knight_11_6", "Vizier Ud'in ibn Laa'ni al-Mee", "Ud'in", tf_hero, 0, reserved, fac_kingdom_11, [itm_ankle_boots, itm_shirt, itm_maa_camel_war_c, itm_maa_scale_b, itm_m_leather_boots_a, itm_mt_scale_gloves_a, itm_maa_mail_coif_b, itm_sarranid_mace_1, itm_maa_camel_rider_shield_c, itm_hunting_crossbow, itm_steel_bolts], knight_attrib_5,wp(250),knight_skills_5, 0x0000000f4700229336db6db6db6dfcf700000000001db6fb0000000000000000, rhodok_face_older_2],
  ["knight_11_7", "Vizier Ullah al-Ad", "Ullah", tf_hero, 0, reserved, fac_kingdom_11, [itm_ankle_boots, itm_shirt, itm_maa_camel_war_c, itm_maa_scale_a2, itm_m_leather_boots_a, itm_mt_scale_gloves_a, itm_maa_mail_coif_b, itm_sarranid_mace_1, itm_maa_camel_rider_shield_c, itm_hunting_crossbow, itm_steel_bolts], knight_attrib_5,wp(250),knight_skills_5, 0x000000003f00228936db6db6db6dfcf700000000001db6fb0000000000000000, rhodok_face_older_2],
  ["knight_11_8", "Vizier Zuha ibn Feeqah al-Matrai", "Zuha", tf_hero, 0, reserved, fac_kingdom_11, [itm_ankle_boots, itm_shirt, itm_maa_camel_war_c, itm_maa_scale_a2, itm_m_leather_boots_a, itm_mt_scale_gloves_a, itm_maa_mail_coif_b, itm_sarranid_mace_1, itm_maa_camel_rider_shield_c, itm_hunting_crossbow, itm_steel_bolts], knight_attrib_5,wp(250),knight_skills_5, 0x000000003f0072c736db6db6db6dfcf700000000001db6fb0000000000000000, rhodok_face_older_2],

  ["knight_11_9", "Vizier Baha ibn Samee al-Fi", "Baha", tf_hero, 0, reserved, fac_kingdom_11, [itm_ankle_boots, itm_shirt, itm_maa_camel_war_c, itm_maa_scale_a2, itm_m_leather_boots_a, itm_mt_scale_gloves_a, itm_maa_mail_coif_b, itm_sarranid_mace_1, itm_maa_camel_rider_shield_c, itm_hunting_crossbow, itm_steel_bolts], knight_attrib_5,wp(250),knight_skills_5, 0x000000003f00735436db6db6db6dfcf700000000001db6fb0000000000000000, rhodok_face_older_2],
  ["knight_11_10", "Vizier Awad al-Habaii", "Awad", tf_hero, 0, reserved, fac_kingdom_11, [itm_ankle_boots, itm_shirt, itm_maa_camel_war_c, itm_maa_scale_b, itm_m_leather_boots_a, itm_mt_scale_gloves_a, itm_maa_mail_coif_b, itm_sarranid_mace_1, itm_maa_camel_rider_shield_c, itm_hunting_crossbow, itm_steel_bolts], knight_attrib_5,wp(250),knight_skills_5, 0x000000003f00628836db6db6db6dfcf700000000001db6fb0000000000000000, rhodok_face_older_2],
  ["knight_11_11", "Vizier Abu Samee Waha al-Ha", "Abu", tf_hero, 0, reserved, fac_kingdom_11, [itm_ankle_boots, itm_shirt, itm_maa_camel_war_c, itm_maa_scale_a, itm_m_leather_boots_a, itm_mt_scale_gloves_a, itm_maa_mail_coif_b, itm_sarranid_mace_1, itm_maa_camel_rider_shield_c, itm_hunting_crossbow, itm_steel_bolts], knight_attrib_5,wp(250),knight_skills_5, 0x000000003f00728636db6db6db6dfcf700000000001db6fb0000000000000000, rhodok_face_older_2],
  ["knight_11_12", "Vizier Sa'khiy ibn Waha al-Sirai", "Sa'khiy", tf_hero, 0, reserved, fac_kingdom_11, [itm_ankle_boots, itm_shirt, itm_maa_camel_war_c, itm_maa_scale_a, itm_m_leather_boots_a, itm_mt_scale_gloves_a, itm_maa_mail_coif_b, itm_sarranid_mace_1, itm_maa_camel_rider_shield_a, itm_hunting_crossbow, itm_steel_bolts], knight_attrib_5,wp(250),knight_skills_5, 0x000000003f00730336db6db6db6dfcf700000000001db6fb0000000000000000, rhodok_face_older_2],
  ["knight_11_13", "Vizier Abu Sa'qud Ma'ul al-Sa", "Abu Sa'qud", tf_hero, 0, reserved, fac_kingdom_11, [itm_ankle_boots, itm_shirt, itm_maa_camel_war_c, itm_maa_scale_a, itm_m_leather_boots_a, itm_mt_scale_gloves_a, itm_maa_mail_coif_b, itm_sarranid_mace_1, itm_maa_camel_rider_shield_b, itm_hunting_crossbow, itm_steel_bolts], knight_attrib_5,wp(250),knight_skills_5, 0x000000003f00428020db6db6db6dfcf700000000001ed4b80000000000000000, rhodok_face_older_2],
  ["knight_11_14", "Vizier Zaafi ibn Dee'sa al-Taa", "Zaafi", tf_hero, 0, reserved, fac_kingdom_11, [itm_ankle_boots, itm_shirt, itm_maa_camel_war_c, itm_maa_scale_a, itm_m_leather_boots_a, itm_mt_scale_gloves_a, itm_maa_mail_coif_b, itm_sarranid_axe_a, itm_maa_camel_rider_shield_c, itm_hunting_crossbow, itm_steel_bolts], knight_attrib_5,wp(250),knight_skills_5, 0x000000003f00314f21c0edb6dbfdffff00000000001ff1380000000000000000, rhodok_face_older_2],
  ["knight_11_15", "Vizier Idreed ibn Ni'taa al-Sa", "Idreed", tf_hero, 0, reserved, fac_kingdom_11, [itm_ankle_boots, itm_shirt, itm_maa_camel_war_c, itm_maa_scale_b, itm_m_leather_boots_a, itm_mt_scale_gloves_a, itm_maa_mail_coif_b, itm_sarranid_axe_a, itm_maa_camel_rider_shield_b, itm_hunting_crossbow, itm_steel_bolts], knight_attrib_5,wp(250),knight_skills_5, 0x000000003f00619436db6db6db6dfcf700000000001db6fb0000000000000000, rhodok_face_older_2],
  ["knight_11_16", "Vizier Muni ibn Jaaha al-Majmii", "Muni", tf_hero, 0, reserved, fac_kingdom_11, [itm_ankle_boots, itm_shirt, itm_maa_camel_war_c, itm_maa_scale_b, itm_m_leather_boots_a, itm_mt_scale_gloves_a, itm_maa_mail_coif_b, itm_sarranid_axe_a, itm_maa_camel_rider_shield_b, itm_hunting_crossbow, itm_steel_bolts], knight_attrib_5,wp(250),knight_skills_5, 0x000000003f00324020db6db6db6dfcf700000000001ed4b80000000000000000, rhodok_face_older_2],
  ["knight_11_17", "Vizier Wiya'ni ibn Ullan al-Ni", "Wiya'ni", tf_hero, 0, reserved, fac_kingdom_11, [itm_ankle_boots, itm_shirt, itm_maa_camel_war_c, itm_maa_scale_b, itm_m_leather_boots_a, itm_mt_scale_gloves_a, itm_maa_mail_coif_b, itm_sarranid_mace_1, itm_maa_camel_rider_shield_b, itm_hunting_crossbow, itm_steel_bolts], knight_attrib_5,wp(250),knight_skills_5, 0x000000003f0071cb20db6db6db6dfcf700000000001ed4b80000000000000000, rhodok_face_older_2],
  ["knight_11_18", "Vizier Sa'qib ibn Sa'on al-Jubii", "Sa'qib", tf_hero, 0, reserved, fac_kingdom_11, [itm_ankle_boots, itm_shirt, itm_maa_camel_war_c, itm_maa_scale_b, itm_m_leather_boots_a, itm_mt_scale_gloves_a, itm_maa_mail_coif_b, itm_sarranid_mace_1, itm_maa_camel_rider_shield_c, itm_hunting_crossbow, itm_steel_bolts], knight_attrib_5,wp(250),knight_skills_5, 0x000000003f00628936db6db6db6dfcf700000000001db6fb0000000000000000, rhodok_face_older_2],
  ["knight_11_19", "Vizier Faary ibn Mee'id al-Sa", "Faary", tf_hero, 0, reserved, fac_kingdom_11, [itm_ankle_boots, itm_shirt, itm_maa_camel_war_c, itm_maa_scale_b, itm_m_leather_boots_a, itm_mt_scale_gloves_a, itm_maa_mail_coif_b, itm_sarranid_axe_b, itm_maa_camel_rider_shield_c, itm_hunting_crossbow, itm_steel_bolts], knight_attrib_5,wp(250),knight_skills_5, 0x000000003f00718a36db6db6db6dfcf700000000001db6fb0000000000000000, rhodok_face_older_2],
  ["knight_11_20", "Vizier Ry'sa al-Anuti", "Ry'sa", tf_hero, 0, reserved, fac_kingdom_11, [itm_ankle_boots, itm_shirt, itm_maa_camel_war_c, itm_maa_scale_b, itm_m_leather_boots_a, itm_mt_scale_gloves_a, itm_maa_mail_coif_b, itm_sarranid_axe_b, itm_maa_camel_rider_shield_c, itm_hunting_crossbow, itm_steel_bolts], knight_attrib_5,wp(250),knight_skills_5, 0x000000003f0061c736db6db6db6dfcf700000000001db6fb0000000000000000, rhodok_face_older_2],

  # Stormguard Knights
  ["knight_12_1", "Lord Alistair Stormrider", "Alistair", tf_hero, 0, reserved, fac_kingdom_12, [itm_hunter, itm_nobleman_outfit, itm_leather_boots, itm_mt_greaves_g, itm_ms_coat_of_plates_a, itm_ms_bear_gauntlets, itm_ms_flamberg_great, itm_tab_shield_small_round_c, itm_grosse_messer_b, itm_ms_helmet_wolf_a], knight_attrib_5,wp(250),knight_skills_5, 0x0000000dbf04500636db6db71b4dff3f00000000001db6f30000000000000000, rhodok_face_older_2],
  ["knight_12_2", "Lady Seraphina Windwhisper", "Seraphina", tf_hero|tf_female, 0, reserved, fac_kingdom_12, [itm_hunter, itm_nobleman_outfit, itm_leather_boots, itm_m_leather_boots_a, itm_ms_stormbringer_hauberk_c, itm_m_gloves_a, itm_light_lance, itm_tab_shield_small_round_c, itm_german_bastard_sword, itm_ms_helmet_e, itm_throwing_daggers], knight_attrib_5,wp(250),knight_skills_5, 0x0000000ec004000736db6db6db6db6db00000000001db6db0000000000000000, rhodok_face_older_2],
  ["knight_12_3", "Lord Cedric Stoneheart", "Cedric", tf_hero, 0, reserved, fac_kingdom_12, [itm_hunter, itm_nobleman_outfit, itm_leather_boots, itm_mt_greaves_g, itm_ms_coat_of_plates_b, itm_mt_scale_gloves_b, itm_ms_great_axe_b, itm_ms_helmet_dark_b], knight_attrib_5,wp(250),knight_skills_5|knows_ironflesh_10|knows_power_strike_10, 0x0000000fff04228920c67127686fff3f00000000001dc9380000000000000000, rhodok_face_older_2],
  ["knight_12_2", "Lady Elara Stormsong", "Elara", tf_hero|tf_female, 0, reserved, fac_kingdom_12, [itm_hunter, itm_nobleman_outfit, itm_leather_boots, itm_m_leather_boots_a, itm_ms_armor_plate_c, itm_m_gloves_a, itm_double_sided_lance, itm_ms_facemask_a, itm_throwing_daggers], knight_attrib_5,wp(250),knight_skills_5, 0x0000000ec004000736db6db6db6db6db00000000001db6db0000000000000000, rhodok_face_older_2],
  ["knight_12_5", "Lord Gareth Ironhand", "Gareth", tf_hero, 0, reserved, fac_kingdom_12, [itm_warhorse, itm_nobleman_outfit, itm_leather_boots, itm_m_leather_boots_a, itm_ms_coat_of_plates_a, itm_m_gloves_a, itm_ms_flamberg_great, itm_tab_shield_small_round_c, itm_light_lance, itm_ms_facemask_a], knight_attrib_5,wp(250),knight_skills_5, 0x0000000aff0844c630db6db6db0dcfff00000000001db6fb0000000000000000, rhodok_face_older_2],
  ["knight_12_6", "Lord Tasco", "Tasco", tf_hero, 0, reserved, fac_kingdom_12, [itm_warhorse, itm_nobleman_outfit, itm_leather_boots, itm_m_leather_boots_a, itm_ms_coat_of_plates_a, itm_m_gloves_a, itm_ms_flamberg_great, itm_tab_shield_small_round_c, itm_light_lance, itm_ms_facemask_a], knight_attrib_5,wp(250),knight_skills_5, 0x00000000350801c13a9292b75aaeff3f00000000001e46f60000000000000000, rhodok_face_older_2],
  ["knight_12_7", "Lord Muirue", "Muirue", tf_hero, 0, reserved, fac_kingdom_12, [itm_warhorse, itm_nobleman_outfit, itm_leather_boots, itm_m_leather_boots_a, itm_ms_coat_of_plates_a, itm_m_gloves_a, itm_ms_flamberg_great, itm_tab_shield_small_round_c, itm_light_lance, itm_ms_facemask_a], knight_attrib_5,wp(250),knight_skills_5, 0x000000002700200618848998a361febf00000000001e3ef90000000000000000, rhodok_face_older_2],
  ["knight_12_8", "Lord Aniod", "Aniod", tf_hero, 0, reserved, fac_kingdom_12, [itm_warhorse, itm_nobleman_outfit, itm_leather_boots, itm_m_leather_boots_a, itm_ms_coat_of_plates_a, itm_m_gloves_a, itm_ms_flamberg_great, itm_tab_shield_small_round_c, itm_light_lance, itm_ms_facemask_a], knight_attrib_5,wp(250),knight_skills_5, 0x00000000331002d1613cb2965b2d7f3f00000000001da77c0000000000000000, rhodok_face_older_2],

  ["knight_12_9", "Lord Vorti", "Vorti", tf_hero, 0, reserved, fac_kingdom_12, [itm_warhorse, itm_nobleman_outfit, itm_leather_boots, itm_m_leather_boots_a, itm_ms_coat_of_plates_a, itm_m_gloves_a, itm_ms_flamberg_great, itm_tab_shield_small_round_c, itm_light_lance, itm_ms_facemask_a], knight_attrib_5,wp(250),knight_skills_5, 0x000000000d002287566491341b2afebe00000000001f693b0000000000000000, rhodok_face_older_2],
  ["knight_12_10", "Lord Vati", "Vati", tf_hero, 0, reserved, fac_kingdom_12, [itm_warhorse, itm_nobleman_outfit, itm_leather_boots, itm_m_leather_boots_a, itm_ms_coat_of_plates_a, itm_m_gloves_a, itm_ms_flamberg_great, itm_tab_shield_small_round_c, itm_light_lance, itm_ms_facemask_a], knight_attrib_5,wp(250),knight_skills_5, 0x00000000060852142353723ceed17eff00000000001cd33c0000000000000000, rhodok_face_older_2],
  ["knight_12_11", "Lord Epon", "Epon", tf_hero, 0, reserved, fac_kingdom_12, [itm_warhorse, itm_nobleman_outfit, itm_leather_boots, itm_m_leather_boots_a, itm_ms_coat_of_plates_a, itm_m_gloves_a, itm_ms_flamberg_great, itm_tab_shield_small_round_c, itm_light_lance, itm_ms_facemask_a], knight_attrib_5,wp(250),knight_skills_5, 0x00000000220814c755136c9ba6c97eff00000000001ca9bd0000000000000000, rhodok_face_older_2],
  ["knight_12_12", "Lord Comgi", "Comgi", tf_hero, 0, reserved, fac_kingdom_12, [itm_warhorse, itm_nobleman_outfit, itm_leather_boots, itm_m_leather_boots_a, itm_ms_coat_of_plates_a, itm_m_gloves_a, itm_ms_flamberg_great, itm_tab_shield_small_round_c, itm_light_lance, itm_ms_facemask_a], knight_attrib_5,wp(250),knight_skills_5, 0x00000000000850c32b1949b46b99ffbf00000000001e36fd0000000000000000, rhodok_face_older_2],
  ["knight_12_13", "Lord Algoil", "Algoil", tf_hero, 0, reserved, fac_kingdom_12, [itm_warhorse, itm_nobleman_outfit, itm_leather_boots, itm_m_leather_boots_a, itm_ms_coat_of_plates_a, itm_m_gloves_a, itm_ms_flamberg_great, itm_tab_shield_small_round_c, itm_light_lance, itm_ms_facemask_a], knight_attrib_5,wp(250),knight_skills_5, 0x00000000090c10c537232d3b5bc57f3f00000000001e41790000000000000000, rhodok_face_older_2],
  ["knight_12_14", "Lord Slorue", "Slorue", tf_hero, 0, reserved, fac_kingdom_12, [itm_warhorse, itm_nobleman_outfit, itm_leather_boots, itm_m_leather_boots_a, itm_ms_coat_of_plates_a, itm_m_gloves_a, itm_ms_flamberg_great, itm_tab_shield_small_round_c, itm_light_lance, itm_ms_facemask_a], knight_attrib_5,wp(250),knight_skills_5, 0x000000000e1000d1331b91c6cc54ffbf00000000001e353b0000000000000000, rhodok_face_older_2],
  ["knight_12_15", "Lord Corca", "Corca", tf_hero, 0, reserved, fac_kingdom_12, [itm_warhorse, itm_nobleman_outfit, itm_leather_boots, itm_m_leather_boots_a, itm_ms_stormbringer_hauberk_a, itm_m_gloves_a, itm_ms_flamberg_great, itm_tab_shield_small_round_c, itm_light_lance, itm_ms_facemask_a], knight_attrib_5,wp(250),knight_skills_5, 0x000000000a04504914cc4d199aaa7e7f00000000001d43b80000000000000000, rhodok_face_older_2],
  ["knight_12_16", "Lord Sesne", "Sesne", tf_hero, 0, reserved, fac_kingdom_12, [itm_warhorse, itm_nobleman_outfit, itm_leather_boots, itm_m_leather_boots_a, itm_ms_coat_of_plates_a, itm_m_gloves_a, itm_ms_flamberg_great, itm_tab_shield_small_round_c, itm_light_lance, itm_ms_facemask_a], knight_attrib_5,wp(250),knight_skills_5, 0x000000000d0c0589449569b71c75ff7f00000000001e387e0000000000000000, rhodok_face_older_2],
  ["knight_12_17", "Lord Cormi", "Cormi", tf_hero, 0, reserved, fac_kingdom_12, [itm_warhorse, itm_nobleman_outfit, itm_leather_boots, itm_m_leather_boots_a, itm_ms_coat_of_plates_a, itm_m_gloves_a, itm_ms_flamberg_great, itm_tab_shield_small_round_c, itm_light_lance, itm_ms_facemask_a], knight_attrib_5,wp(250),knight_skills_5, 0x000000000b0021c546db6e242b517f3f00000000001e19bc0000000000000000, rhodok_face_older_2],
  ["knight_12_18", "Lord Arix", "Arix", tf_hero, 0, reserved, fac_kingdom_12, [itm_warhorse, itm_nobleman_outfit, itm_leather_boots, itm_m_leather_boots_a, itm_ms_coat_of_plates_a, itm_m_gloves_a, itm_ms_flamberg_great, itm_tab_shield_small_round_c, itm_light_lance, itm_ms_facemask_a], knight_attrib_5,wp(250),knight_skills_5, 0x000000001604628f429b763cec8d7f7f00000000001d49630000000000000000, rhodok_face_older_2],
  ["knight_12_19", "Lord Goloy", "Goloy", tf_hero, 0, reserved, fac_kingdom_12, [itm_warhorse, itm_nobleman_outfit, itm_leather_boots, itm_m_leather_boots_a, itm_ms_stormbringer_hauberk_a, itm_m_gloves_a, itm_ms_flamberg_great, itm_tab_shield_small_round_c, itm_light_lance, itm_ms_facemask_a], knight_attrib_5,wp(250),knight_skills_5, 0x000000003e08130416cbacb4e451feff00000000001e5afb0000000000000000, rhodok_face_older_2],
  ["knight_12_20", "Lord Drigo", "Drigo", tf_hero, 0, reserved, fac_kingdom_12, [itm_warhorse, itm_nobleman_outfit, itm_leather_boots, itm_m_leather_boots_a, itm_ms_stormbringer_hauberk_c, itm_m_gloves_a, itm_war_axe, itm_tab_shield_small_round_c, itm_light_lance, itm_ms_helmet_a], knight_attrib_5,wp(250),knight_skills_5, 0x000000000000258116b3d5d5124cffff00000000001ee0fb0000000000000000, rhodok_face_older_2],
  
  ["kingdom_1_pretender",  "Lady Isolla of Suno",       "Isolla",  tf_hero|tf_female|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_1,[itm_charger,   itm_rich_outfit,  itm_blue_hose,      itm_iron_greaves,         itm_mail_shirt,      itm_sword_medieval_c_small,      itm_tab_shield_small_round_c,       itm_bascinet],          lord_attrib,wp(220),knight_skills_5, 0x00000000ef00000237dc71b90c31631200000000001e371b0000000000000000],
#claims pre-salic descent

  ["kingdom_2_pretender",  "Prince Valdym the Bastard", "Valdym",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_2,[itm_hunter,    itm_courtly_outfit,      itm_leather_boots,              itm_mail_chausses,              itm_lamellar_armor,       itm_military_pick,      itm_tab_shield_heater_b,      itm_flat_topped_helmet],    lord_attrib,wp(220),knight_skills_5, 0x00000000200412142452ed631b30365c00000000001c94e80000000000000000, vaegir_face_middle_2],
#had his patrimony falsified

  ["kingdom_3_pretender",  "Dustum Khan",               "Dustum",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_3,[itm_courser,   itm_nomad_robe,             itm_leather_boots,              itm_splinted_greaves,           itm_khergit_guard_armor,         itm_sword_khergit_2,              itm_tab_shield_small_round_c,       itm_segmented_helmet],      lord_attrib,wp(220),knight_skills_5, 0x000000065504310b30d556b51238f66100000000001c256d0000000000000000, khergit_face_middle_2],
#of the family

  ["kingdom_4_pretender",  "Lethwin Far-Seeker",   "Lethwin",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_4,[itm_hunter,    itm_tabard,    itm_leather_boots,              itm_mail_boots,                 itm_brigandine_red,           itm_sword_medieval_c,           itm_tab_shield_heater_cav_a,    itm_kettle_hat],            lord_attrib,wp(220),knight_skills_5, 0x00000004340c01841d89949529a6776a00000000001c910a0000000000000000, nord_face_young_2],
#dispossessed and wronged

  ["kingdom_5_pretender",  "Lord Kastor of Veluca",  "Kastor",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_5,[itm_warhorse,  itm_nobleman_outfit,             itm_leather_boots,              itm_splinted_leather_greaves,   itm_mail_hauberk,           itm_sword_medieval_c,         itm_tab_shield_heater_d,        itm_spiked_helmet],         lord_attrib,wp(220),knight_skills_5, 0x0000000bed1031051da9abc49ecce25e00000000001e98680000000000000000, rhodok_face_old_2],
#republican

  ["kingdom_6_pretender",  "Arwa the Pearled One",       "Arwa",  tf_hero|tf_female|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_6,[itm_arabian_horse_b, itm_sarranid_mail_shirt, itm_sarranid_boots_c, itm_sarranid_cavalry_sword,      itm_tab_shield_small_round_c],          lord_attrib,wp(220),knight_skills_5, 0x000000050b003004072d51c293a9a70b00000000001dd6a90000000000000000],

##  ["kingdom_1_lord_a", "Kingdom 1 Lord A", "Kingdom 1 Lord A", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_b", "Kingdom 1 Lord B", "Kingdom 1 Lord B", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_c", "Kingdom 1 Lord C", "Kingdom 1 Lord C", tf_hero, 0,reserved,  fac_kingdom_3,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_d", "Kingdom 1 Lord D", "Kingdom 1 Lord D", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_e", "Kingdom 1 Lord E", "Kingdom 1 Lord E", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_f", "Kingdom 1 Lord F", "Kingdom 1 Lord F", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_g", "Kingdom 1 Lord G", "Kingdom 1 Lord G", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_h", "Kingdom 1 Lord H", "Kingdom 1 Lord H", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_i", "Kingdom 1 Lord I", "Kingdom 1 Lord I", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_j", "Kingdom 1 Lord J", "Kingdom 1 Lord J", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_k", "Kingdom 1 Lord K", "Kingdom 1 Lord K", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_l", "Kingdom 1 Lord L", "Kingdom 1 Lord L", tf_hero, 0,reserved,  fac_kingdom_3,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_m", "Kingdom 1 Lord M", "Kingdom 1 Lord M", tf_hero, 0,reserved,  fac_kingdom_3,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_n", "Kingdom 1 Lord N", "Kingdom 1 Lord N", tf_hero, 0,reserved,  fac_kingdom_3,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],



#  ["town_1_ruler_a", "King Harlaus",  "King Harlaus",  tf_hero, scn_town_1_castle|entry(9),reserved,  fac_swadians,[itm_saddle_horse,itm_courtly_outfit,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000010908101e36db44b75b6dd],
#  ["town_2_ruler_a", "Duke Taugard",  "Duke Taugard",  tf_hero, scn_town_2_castle|entry(9),reserved,  fac_swadians,[itm_saddle_horse,itm_courtly_outfit,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000000310401e06db86375f6da],
#  ["town_3_ruler_a", "Count Grimar",  "Count Grimar",  tf_hero, scn_town_3_castle|entry(9),reserved, fac_swadians,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000004430301e46136eb75bc0a],
#  ["town_4_ruler_a", "Count Haxalye", "Count Haxalye", tf_hero, scn_town_4_castle|entry(9),reserved,  fac_swadians,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000010918701e77136e905bc0e
#  ["town_5_ruler_a", "Count Belicha", "Count Belicha", tf_hero, scn_town_5_castle|entry(9),reserved, fac_swadians,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x00000000000421c801e7713729c5b8ce],
#  ["town_6_ruler_a", "Count Nourbis", "Count Nourbis", tf_hero, scn_town_6_castle|entry(9),reserved,  fac_swadians,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x00000000000c640501e371b72bcdb724],
#  ["town_7_ruler_a", "Count Rhudolg", "Count Rhudolg", tf_hero, scn_town_7_castle|entry(9),reserved,  fac_swadians,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x00000000000c710201fa51b7286db721],
 
#  ["town_8_ruler_b", "King Yaroglek", "King_yaroglek", tf_hero, scn_town_8_castle|entry(9),reserved,  fac_vaegirs,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000000128801f294ca6d66d555],
#  ["town_9_ruler_b", "Count Aolbrug", "Count_Aolbrug", tf_hero, scn_town_9_castle|entry(9),reserved,  fac_vaegirs,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000004234401f26a271c8d38ea],
#  ["town_10_ruler_b","Count Rasevas", "Count_Rasevas", tf_hero, scn_town_10_castle|entry(9),reserved, fac_vaegirs,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x00000000001032c201f38e269372471c],
#  ["town_11_ruler_b","Count Leomir",  "Count_Leomir",  tf_hero, scn_town_11_castle|entry(9),reserved,  fac_vaegirs,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x00000000000c538001f55148936d3895],
#  ["town_12_ruler_b","Count Haelbrad","Count_Haelbrad",tf_hero, scn_town_12_castle|entry(9),reserved,  fac_vaegirs,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x00000000000410c701f38598ac8aaaab],
#  ["town_13_ruler_b","Count Mira",    "Count_Mira",    tf_hero, scn_town_13_castle|entry(9),reserved, fac_vaegirs,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000004204401f390c515555594],
#  ["town_14_ruler_b","Count Camechaw","Count_Camechaw",tf_hero, scn_town_14_castle|entry(9),reserved,  fac_vaegirs,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000008318101f390c515555594],

##  ["kingdom_2_lord_a", "Kingdom 2 Lord A", "Kingdom 2 Lord A", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_b", "Kingdom 2 Lord B", "Kingdom 2 Lord B", tf_hero, 0,reserved,  fac_kingdom_11,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_c", "Kingdom 2 Lord C", "Kingdom 2 Lord C", tf_hero, 0,reserved,  fac_kingdom_12,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_d", "Kingdom 2 Lord D", "Kingdom 2 Lord D", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_e", "Kingdom 2 Lord E", "Kingdom 2 Lord E", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_f", "Kingdom 2 Lord F", "Kingdom 2 Lord F", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_g", "Kingdom 2 Lord G", "Kingdom 2 Lord G", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_h", "Kingdom 2 Lord H", "Kingdom 2 Lord H", tf_hero, 0,reserved,  fac_kingdom_11,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_i", "Kingdom 2 Lord I", "Kingdom 2 Lord I", tf_hero, 0,reserved,  fac_kingdom_11,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_j", "Kingdom 2 Lord J", "Kingdom 2 Lord J", tf_hero, 0,reserved,  fac_kingdom_11,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_k", "Kingdom 2 Lord K", "Kingdom 2 Lord K", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_l", "Kingdom 2 Lord L", "Kingdom 2 Lord L", tf_hero, 0,reserved,  fac_kingdom_12,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_m", "Kingdom 2 Lord M", "Kingdom 2 Lord M", tf_hero, 0,reserved,  fac_kingdom_12,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_n", "Kingdom 2 Lord N", "Kingdom 2 Lord N", tf_hero, 0,reserved,  fac_kingdom_12,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],



#Royal family members

  ["knight_1_1_wife","Error - knight_1_1_wife should not appear in game","knight_1_1_wife",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_commoners, [itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],

  #Swadian ladies - eight mothers, eight daughters, four sisters
  ["kingdom_1_lady_1","Lady Anna","Anna",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [          itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
  ["kingdom_1_lady_2","Lady Nelda","Nelda",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
  ["knight_1_lady_3","Lady Bela","Bela",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,  [       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
  ["knight_1_lady_4","Lady Elina","Elina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,  [       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000],
  ["kingdom_l_lady_5","Lady Constanis","Constanis",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_6","Lady Vera","Vera",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],
  ["kingdom_1_lady_7","Lady Auberina","Auberina",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_8","Lady Tibal","Tibal",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000],
  ["kingdom_1_lady_9","Lady Magar","Magar",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_10","Lady Thedosa","Thedosa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000],
  ["kingdom_1_lady_11","Lady Melisar","Melisar",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_12","Lady Irena","Irena",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,  0x000000003f04100148d245d6526d456b00000000001e3b350000000000000000],
  ["kingdom_l_lady_13","Lady Philenna","Philenna",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_14","Lady Sonadel","Sonadel",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000],
  ["kingdom_1_lady_15","Lady Boadila","Boadila",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_16","Lady Elys","Elys",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003b080003531e8932e432bb5a000000000008db6a0000000000000000],
  ["kingdom_1_lady_17","Lady Johana","Johana",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000446e4b4c2cc5234d200000000001ea3120000000000000000],
  ["kingdom_1_lady_18","Lady Bernatys","Bernatys",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000000083006465800000901161200000000001e38cc0000000000000000],
  ["kingdom_1_lady_19","Lady Enricata","Enricata",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
  ["kingdom_1_lady_20","Lady Gaeta","Gaeta",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_2],
  
  #Vaegir ladies
  ["kingdom_2_lady_1","Lady Junitha","Junitha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_2","Lady Katia","Katia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_3","Lady Seomis","Seomis",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [   itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_4","Lady Drina","Drina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_2_lady_5","Lady Nesha","Nesha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_6","Lady Tabath","Tabath",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_7","Lady Pelaeka","Pelaeka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_8","Lady Haris","Haris",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_2_lady_9","Lady Vayen","Vayen",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_10","Lady Joaka","Joaka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_11","Lady Tejina","Tejina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_12","Lady Olekseia","Olekseia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [      itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_2_lady_13","Lady Myntha","Myntha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_14","Lady Akilina","Akilina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_15","Lady Sepana","Sepana",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_16","Lady Iarina","Iarina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_2_lady_17","Lady Sihavan","Sihavan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_18","Lady Erenchina","Erenchina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [  itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_19","Lady Tamar","Tamar",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_20","Lady Valka","Valka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [itm_green_dress,   itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],


  ["kingdom_3_lady_1","Lady Borge","Borge",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_1],
  ["kingdom_3_lady_2","Lady Tuan","Tuan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_green_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
  ["kingdom_3_lady_3","Lady Mahraz","Mahraz",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [itm_red_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_2],
  ["kingdom_3_lady_4","Lady Ayasu","Ayasu",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_red_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],
  ["kingdom_3_lady_5","Lady Ravin","Ravin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_green_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
  ["kingdom_3_lady_6","Lady Ruha","Ruha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_green_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
  ["kingdom_3_lady_7","Lady Chedina","Chedina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
  ["kingdom_3_lady_8","Lady Kefra","Kefra",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
  ["kingdom_3_lady_9","Lady Nirvaz","Nirvaz",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001940c3006019c925165d1129b00000000001d13240000000000000000],
  ["kingdom_3_lady_10","Lady Dulua","Dulua",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
  ["kingdom_3_lady_11","Lady Selik","Selik",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000019b083005389591941379b8d100000000001e63150000000000000000],
  ["kingdom_3_lady_12","Lady Thalatha","Thalatha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],
  ["kingdom_3_lady_13","Lady Yasreen","Yasreen",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
  ["kingdom_3_lady_14","Lady Nadha","Nadha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_1],
  ["kingdom_3_lady_15","Lady Zenur","Zenur",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_2],
  ["kingdom_3_lady_16","Lady Arjis","Zenur",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001ad003001628c54b05d2e48b200000000001d56e60000000000000000],
  ["kingdom_3_lady_17","Lady Atjahan", "Atjahan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001a700300265cb6db15d6db6da00000000001f82180000000000000000],
  ["kingdom_3_lady_18","Lady Qutala","Qutala",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
  ["kingdom_3_lady_19","Lady Hindal","Hindal",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
  ["kingdom_3_lady_20","Lady Mechet","Mechet",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],
  
  
  
  ["kingdom_4_lady_1","Lady Jadeth","Jadeth",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_4_lady_2","Lady Miar","Miar",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_4_lady_3","Lady Dria","Dria",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress, itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["kingdom_4_lady_4","Lady Glunde","Glunde",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["kingdom_4_lady_5","Lady Loeka","Loeka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_4_lady_6","Lady Bryn","Bryn",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_4_lady_7","Lady Eir","Eir",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["knight_4_2b_daughter_1","Lady Thera","Thera",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["kingdom_4_lady_9","Lady Hild","Hild",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,  itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["knight_4_2c_wife_1","Lady Endegrid","Endegrid",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_4_lady_11","Lady Herjasa","Herjasa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["knight_4_2c_daughter","Lady Svipul","Svipul",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["knight_4_1b_wife","Lady Ingunn","Ingunn",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_4_lady_14","Lady Kaeteli","Kaeteli",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["knight_4_1b_daughter","Lady Eilif","Eilif",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["knight_4_2b_daughter_2","Lady Gudrun","Gudrun",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["kingdom_4_lady_17","Lady Bergit","Bergit",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["knight_4_2c_wife_2","Lady Aesa","Aesa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["knight_4_1c_daughter","Lady Alfrun","Alfrun",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["kingdom_4_lady_20","Lady Afrid","Afrid",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],


  ["kingdom_5_lady_1","Lady Brina","Brina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
  ["kingdom_5_lady_2","Lady Aliena","Aliena",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
  ["kingdom_5_lady_3","Lady Aneth","Aneth",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_lady_4","Lady Reada","Reada",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  ["kingdom_5_5_wife","Lady Saraten","Saraten",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
  ["kingdom_5_2b_wife_1","Lady Baotheia","Baotheia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [itm_lady_dress_green,     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000bf0400035913aa236b4d975a00000000001eb69c0000000000000000],
  ["kingdom_5_1c_daughter_1","Lady Eleandra","Eleandra",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_2c_daughter_1","Lady Meraced","Meraced",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  ["kingdom_5_1c_wife_1","Lady Adelisa","Adelisa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
  ["kingdom_5_2c_wife_1","Lady Calantina","Calantina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
  ["kingdom_5_1c_daughter_2","Lady Forbesa","Forbesa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_2c_daughter_2","Lady Claudora","Claudora",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  ["kingdom_5_1b_wife","Lady Anais","Anais",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
  ["kingdom_5_2b_wife_2","Lady Miraeia","Miraeia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
  ["kingdom_5_1c_daughter_3","Lady Agasia","Agasia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_lady_16","Lady Geneiava","Geneiava",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  ["kingdom_5_1c_wife_2","Lady Gwenael","Gwenael",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
  ["kingdom_5_2c_wife_2","Lady Ysueth","Ysueth",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
  ["kingdom_5_1c_daughter_4","Lady Ellian","Ellian",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_lady_20","Lady Timethi","Timethi",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  
#Sarranid ladies
  ["kingdom_6_lady_1","Lady Rayma","Rayma",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,  itm_sarranid_head_cloth,        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
  ["kingdom_6_lady_2","Lady Thanaikha","Thanaikha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
  ["kingdom_6_lady_3","Lady Sulaha","Sulaha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,  [itm_sarranid_lady_dress,       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
  ["kingdom_6_lady_4","Lady Shatha","Shatha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,  [itm_sarranid_lady_dress,       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000],
  ["kingdom_6_lady_5","Lady Bawthan","Bawthan",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_6_lady_6","Lady Mahayl","Mahayl",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],
  ["kingdom_6_lady_7","Lady Isna","Isna",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_6_lady_8","Lady Siyafan","Siyafan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000],
  ["kingdom_6_lady_9","Lady Ifar","Ifar",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_6_lady_10","Lady Yasmin","Yasmin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000],
  ["kingdom_6_lady_11","Lady Dula","Dula",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_6_lady_12","Lady Ruwa","Ruwa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,  0x000000003f04100148d245d6526d456b00000000001e3b350000000000000000],
  ["kingdom_6_lady_13","Lady Luqa","Luqa",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_6_lady_14","Lady Zandina","Zandina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000],
  ["kingdom_6_lady_15","Lady Lulya","Lulya",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_6_lady_16","Lady Zahara","Zahara",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003b080003531e8932e432bb5a000000000008db6a0000000000000000],
  ["kingdom_6_lady_17","Lady Safiya","Safiya",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000446e4b4c2cc5234d200000000001ea3120000000000000000],
  ["kingdom_6_lady_18","Lady Khalisa","Khalisa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000000083006465800000901161200000000001e38cc0000000000000000],
  ["kingdom_6_lady_19","Lady Janab","Janab",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
  ["kingdom_6_lady_20","Lady Sur","Sur",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_2],

  ["kingdom_7_lady_1","Lady Erin Reeve","Erin Reeve",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_lady_dress_blue,  itm_sarranid_head_cloth,        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
  ["kingdom_7_lady_2","Lady Ealurg","Ealurg",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
  ["kingdom_7_lady_3","Lady Wifru","Wifru",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7,  [itm_lady_dress_blue,       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
  ["kingdom_7_lady_4","Lady Jane","Jane",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7,  [itm_lady_dress_blue,       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000],
  ["kingdom_7_lady_5","Lady Hilda","Hilda",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_lady_dress_blue,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_7_lady_6","Lady Maly","Maly",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],
  ["kingdom_7_lady_7","Lady Arran","Arran",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_lady_dress_blue,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_7_lady_8","Lady Egild","Egild",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_lady_dress_green,        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000],
  ["kingdom_7_lady_9","Lady Heva","Heva",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_7_lady_10","Lady Burghwe","Burghwe",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_lady_dress_blue,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000],
  ["kingdom_7_lady_11","Lady Hilia","Hilia",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_lady_dress_blue,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_7_lady_12","Lady Jane","Jane",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_lady_dress_green,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,  0x000000003f04100148d245d6526d456b00000000001e3b350000000000000000],
  ["kingdom_7_lady_13","Lady Atel","Atel",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_lady_dress_green,     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_7_lady_14","Lady Alhhild","Alhhild",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_lady_dress_blue,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000],
  ["kingdom_7_lady_15","Lady Joane","Joane",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_lady_dress_green,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_7_lady_16","Lady Beatra","Beatra",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_lady_dress_blue,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003b080003531e8932e432bb5a000000000008db6a0000000000000000],
  ["kingdom_7_lady_17","Lady Sabeth Hawte","Sabeth Hawte",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000446e4b4c2cc5234d200000000001ea3120000000000000000],
  ["kingdom_7_lady_18","Lady Cece","Cece",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_lady_dress_blue,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000000083006465800000901161200000000001e38cc0000000000000000],
  ["kingdom_7_lady_19","Lady Adburh","Adburh",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
  ["kingdom_7_lady_20","Lady Cyna","Cyna",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_lady_dress_blue,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_2],

  ["kingdom_8_lady_1","Lady Sila","Sila",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_lady_dress_blue,  itm_sarranid_head_cloth,        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
  ["kingdom_8_lady_2","Lady Ninla","Ninla",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
  ["kingdom_8_lady_3","Lady Abag","Abag",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8,  [itm_lady_dress_blue,       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
  ["kingdom_8_lady_4","Lady Saga","Saga",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8,  [itm_lady_dress_blue,       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000],
  ["kingdom_8_lady_5","Lady Inlit","Inlit",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_lady_dress_blue,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_8_lady_6","Lady Suna","Suna",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],
  ["kingdom_8_lady_7","Lady Ninhub","Ninhub",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_lady_dress_blue,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_8_lady_8","Lady Ninki","Ninki",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_lady_dress_green,        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000],
  ["kingdom_8_lady_9","Lady Ilil","Ilil",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_8_lady_10","Lady Nindur","Nindur",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_lady_dress_blue,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000],
  ["kingdom_8_lady_11","Lady Ninduk","Ninduk",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_lady_dress_blue,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_8_lady_12","Lady Saga","Saga",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_lady_dress_green,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,  0x000000003f04100148d245d6526d456b00000000001e3b350000000000000000],
  ["kingdom_8_lady_13","Lady Sidur","Sidur",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_lady_dress_green,     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_8_lady_14","Lady Ninga","Ninga",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_lady_dress_blue,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000],
  ["kingdom_8_lady_15","Lady Ayammeshki","Ayammeshki",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_lady_dress_green,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_8_lady_16","Lady Nanna","Nanna",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_lady_dress_blue,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003b080003531e8932e432bb5a000000000008db6a0000000000000000],
  ["kingdom_8_lady_17","Lady Ingag","Ingag",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000446e4b4c2cc5234d200000000001ea3120000000000000000],
  ["kingdom_8_lady_18","Lady Ayarum","Ayarum",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_lady_dress_blue,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000000083006465800000901161200000000001e38cc0000000000000000],
  ["kingdom_8_lady_19","Lady Ayabit","Ayabit",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
  ["kingdom_8_lady_20","Lady Shuba","Shuba",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_lady_dress_blue,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_2],

  ["kingdom_9_lady_1","Lady Elyn","Elyn",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_lady_dress_blue,  itm_sarranid_head_cloth,        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
  ["kingdom_9_lady_2","Lady Bride","Bride",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
  ["kingdom_9_lady_3","Lady Cece","Cece",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9,  [itm_lady_dress_ruby,       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
  ["kingdom_9_lady_4","Lady Elyn Teray","Elyn Teray",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9,  [itm_lady_dress_ruby,       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000],
  ["kingdom_9_lady_5","Lady Bily","Bily",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_lady_dress_ruby,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_9_lady_6","Lady Abet","Abet",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],
  ["kingdom_9_lady_7","Lady Mera","Mera",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_lady_dress_ruby,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_9_lady_8","Lady Lucie Gare","Lucie Gare",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_lady_dress_green,        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000],
  ["kingdom_9_lady_9","Lady Sabeatr","Sabeatr",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_9_lady_10","Lady Cily","Cily",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_lady_dress_ruby,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000],
  ["kingdom_9_lady_11","Lady Anel","Anel",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_lady_dress_ruby,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_9_lady_12","Lady Efril","Efril",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_lady_dress_green,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,  0x000000003f04100148d245d6526d456b00000000001e3b350000000000000000],
  ["kingdom_9_lady_13","Lady Marget","Marget",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_lady_dress_green,     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_9_lady_14","Lady Atet Payne","Atet Payne",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_lady_dress_ruby,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000],
  ["kingdom_9_lady_15","Lady Marget Vaughey","Marget Vaughey",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_lady_dress_green,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_9_lady_16","Lady Ellyn","Ellyn",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_lady_dress_ruby,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003b080003531e8932e432bb5a000000000008db6a0000000000000000],
  ["kingdom_9_lady_17","Lady Argell Righte","Argell Righte",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000446e4b4c2cc5234d200000000001ea3120000000000000000],
  ["kingdom_9_lady_18","Lady Jane","Jane",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_lady_dress_ruby,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000000083006465800000901161200000000001e38cc0000000000000000],
  ["kingdom_9_lady_19","Lady Enet","Enet",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
  ["kingdom_9_lady_20","Lady Beatra","Beatra",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_lady_dress_ruby,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_2],
  
  ["kingdom_10_lady_1","Lady Elys","Elys",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10, [itm_lady_dress_ruby,  itm_sarranid_head_cloth,        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
  ["kingdom_10_lady_2","Lady Lyse Vere","Lyse Vere",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10, [itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
  ["kingdom_10_lady_3","Lady Eryen","Eryen",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10,  [itm_lady_dress_ruby,       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
  ["kingdom_10_lady_4","Lady Eryn Finchey","Eryn Finchey",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10,  [itm_lady_dress_ruby,       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000],
  ["kingdom_10_lady_5","Lady Sarrey Gysby","Sarrey Gysby",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10, [itm_lady_dress_ruby,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_10_lady_6","Lady Hone Dreyne","Hone Dreyne",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10, [itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],
  ["kingdom_10_lady_7","Lady Benne","Benne",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10, [itm_lady_dress_ruby,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_10_lady_8","Lady Abell Finchey","Abell Finchey",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10, [itm_lady_dress_green,        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000],
  ["kingdom_10_lady_9","Lady Sarra","Sarra",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10, [itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_10_lady_10","Lady Auciel","Auciel",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10, [itm_lady_dress_ruby,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000],
  ["kingdom_10_lady_11","Lady Jane","Jane",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10, [itm_lady_dress_ruby,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_10_lady_12","Lady Mery","Mery",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10, [itm_lady_dress_green,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,  0x000000003f04100148d245d6526d456b00000000001e3b350000000000000000],
  ["kingdom_10_lady_13","Lady Brose Aver","Brose Aver",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10, [itm_lady_dress_green,     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_10_lady_14","Lady Suse","Suse",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10, [itm_lady_dress_ruby,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000],
  ["kingdom_10_lady_15","Lady Mery Rowe","Mery Rowe",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10, [itm_lady_dress_green,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_10_lady_16","Lady Joane Tere","Joane Tere",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10, [itm_lady_dress_ruby,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003b080003531e8932e432bb5a000000000008db6a0000000000000000],
  ["kingdom_10_lady_17","Lady Malia","Malia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10, [itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000446e4b4c2cc5234d200000000001ea3120000000000000000],
  ["kingdom_10_lady_18","Lady Elin","Elin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10, [itm_lady_dress_ruby,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000000083006465800000901161200000000001e38cc0000000000000000],
  ["kingdom_10_lady_19","Lady Joane","Joane",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10, [itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
  ["kingdom_10_lady_20","Lady Joane Flerke","Joane Flerke",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10, [itm_lady_dress_ruby,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_2],

  ["kingdom_11_lady_1","Lady Yaelah Weidi","Yaelah Weidi",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [itm_lady_dress_green,  itm_sarranid_head_cloth,        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
  ["kingdom_11_lady_2","Lady Jethra Rosenb","Jethra Rosenb",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [itm_lady_dress_ruby,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
  ["kingdom_11_lady_3","Lady Ariel Jero","Ariel Jero",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11,  [itm_lady_dress_green,       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
  ["kingdom_11_lady_4","Lady Sheba Mani","Sheba Mani",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11,  [itm_lady_dress_green,       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000],
  ["kingdom_11_lady_5","Lady Anar Goni","Anar Goni",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_11_lady_6","Lady Amith Goloh","Amith Goloh",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [itm_lady_dress_ruby,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],
  ["kingdom_11_lady_7","Lady Bara Mani","Bara Mani",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_11_lady_8","Lady Adah Denhel","Adah Denhel",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [itm_lady_dress_ruby,        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000],
  ["kingdom_11_lady_9","Lady Mera Rossman","Mera Rossman",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [itm_lady_dress_ruby,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_11_lady_10","Lady Elav Gottor","Elav Gottor",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [itm_lady_dress_green,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000],
  ["kingdom_11_lady_11","Lady Avit Rayeshav","Avit Rayeshav",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_11_lady_12","Lady Arar Inskir","Arar Inskir",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [itm_lady_dress_ruby,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,  0x000000003f04100148d245d6526d456b00000000001e3b350000000000000000],
  ["kingdom_11_lady_13","Lady Yaelil Golomst","Yaelil Golomst",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [itm_lady_dress_ruby,     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_11_lady_14","Lady Elah Pinsky","Elah Pinsky",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000],
  ["kingdom_11_lady_15","Lady Shana Dermoh","Shana Dermoh",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [itm_lady_dress_ruby,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_11_lady_16","Lady Agag Daro","Agag Daro",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003b080003531e8932e432bb5a000000000008db6a0000000000000000],
  ["kingdom_11_lady_17","Lady Maela Bermach","Maela Bermach",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [itm_lady_dress_ruby,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000446e4b4c2cc5234d200000000001ea3120000000000000000],
  ["kingdom_11_lady_18","Lady Orpah Nero","Orpah Nero",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000000083006465800000901161200000000001e38cc0000000000000000],
  ["kingdom_11_lady_19","Lady Tala Zahad","Tala Zahad",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [itm_lady_dress_ruby,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
  ["kingdom_11_lady_20","Lady Anar Pazy","Anar Pazy",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_2],

  ["kingdom_12_lady_1","Lady Garda","Garda",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12, [itm_lady_dress_blue,  itm_sarranid_head_cloth,        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
  ["kingdom_12_lady_2","Lady Cina","Cina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12, [itm_lady_dress_ruby,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
  ["kingdom_12_lady_3","Lady Disebe","Disebe",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12,  [itm_lady_dress_blue,       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
  ["kingdom_12_lady_4","Lady Aradard","Aradard",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12,  [itm_lady_dress_blue,       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000],
  ["kingdom_12_lady_5","Lady Ardalad","Ardalad",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12, [itm_lady_dress_blue,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_12_lady_6","Lady Adadel","Adadel",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12, [itm_lady_dress_ruby,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],
  ["kingdom_12_lady_7","Lady Radborga","Radborga",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12, [itm_lady_dress_blue,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_12_lady_8","Lady Eresuuis","Eresuuis",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12, [itm_lady_dress_ruby,        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000],
  ["kingdom_12_lady_9","Lady Indanard","Indanard",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12, [itm_lady_dress_ruby,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_12_lady_10","Lady Hildisa","Hildisa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12, [itm_lady_dress_blue,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000],
  ["kingdom_12_lady_11","Lady Creda","Creda",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12, [itm_lady_dress_blue,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_12_lady_12","Lady Thinilda","Thinilda",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12, [itm_lady_dress_ruby,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,  0x000000003f04100148d245d6526d456b00000000001e3b350000000000000000],
  ["kingdom_12_lady_13","Lady Indis","Indis",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12, [itm_lady_dress_ruby,     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_12_lady_14","Lady Rude","Rude",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12, [itm_lady_dress_blue,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000],
  ["kingdom_12_lady_15","Lady Thieta","Thieta",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12, [itm_lady_dress_ruby,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_12_lady_16","Lady Egekis","Egekis",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12, [itm_lady_dress_blue,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003b080003531e8932e432bb5a000000000008db6a0000000000000000],
  ["kingdom_12_lady_17","Lady Hilda","Hilda",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12, [itm_lady_dress_ruby,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000446e4b4c2cc5234d200000000001ea3120000000000000000],
  ["kingdom_12_lady_18","Lady Windise","Windise",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12, [itm_lady_dress_blue,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000000083006465800000901161200000000001e38cc0000000000000000],
  ["kingdom_12_lady_19","Lady Thilda","Thilda",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12, [itm_lady_dress_blue,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
  ["kingdom_12_lady_20","Lady Bergunda","Bergunda",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12, [itm_lady_dress_blue,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_2],

#  ["kingdom_11_lord_daughter","kingdom_11_lord_daughter","kingdom_11_lord_daughter",tf_hero|tf_female,0,reserved,fac_kingdom_10,  [ itm_lady_dress_blue ,   itm_turret_hat_blue,    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008300701c08d34a450ce43],
#  ["kingdom_13_lord_daughter","kingdom_13_lord_daughter","kingdom_13_lord_daughter",tf_hero|tf_female,0,reserved,fac_kingdom_10,  [ itm_lady_dress_green,   itm_turret_hat_green,   itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008000401db10a45b41d6d8],
##  ["kingdom_1_lady_a","kingdom_1_lady_a","kingdom_1_lady_a",tf_hero|tf_female,0,reserved,fac_kingdom_1, [   itm_lady_dress_blue ,   itm_turret_hat_blue,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008500201d8ad93708e4694],
##  ["kingdom_1_lady_b","kingdom_1_lady_b","kingdom_1_lady_b",tf_hero|tf_female,0,reserved,fac_kingdom_1, [   itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000004000101c3ae68e0e944ac],
##  ["kingdom_2_lady_a","Kingdom 2 Lady a","Kingdom 2 Lady a",tf_hero|tf_female,0,reserved,fac_kingdom_2, [               itm_lady_dress_green,   itm_turret_hat_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008100501d8ad93708e4694],
##  ["kingdom_2_lady_b","Kingdom 2 Lady b","Kingdom 2 Lady b",tf_hero|tf_female,0,reserved,fac_kingdom_2, [               itm_lady_dress_blue ,   itm_turret_hat_blue,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000004000401d8ad93708e4694],
##  ["kingdom_3_lady_a","Kingdom 3 Lady a","Kingdom 3 Lady a",tf_hero|tf_female,0,reserved,fac_kingdom_3, [               itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000010500301d8ad93708e4694],
##
##  ["kingdom_3_lady_b","Kingdom 3 Lady b","Kingdom 3 Lady b",tf_hero|tf_female,0,reserved,fac_kingdom_3,  [                         itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000000100601d8b08d76d14a24],
##  ["kingdom_4_lady_a","Kingdom 4 Lady a","Kingdom 4 Lady a",tf_hero|tf_female,0,reserved,fac_kingdom_4,  [                         itm_lady_dress_green,   itm_turret_hat_green,   itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000010500601d8ad93708e4694],
##  ["kingdom_4_lady_b","Kingdom 4 Lady b","Kingdom 4 Lady b",tf_hero|tf_female,0,reserved,fac_kingdom_4,  [                         itm_lady_dress_blue ,   itm_turret_hat_blue,    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008500201d8ad93708e4694],

  ["heroes_end", "{!}heroes end", "{!}heroes end", tf_hero, 0,reserved,  fac_neutral,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000008318101f390c515555594],
#Merchants                                                                              AT                      SILAH                   ZIRH                        BOT                         Head_wear
##  ["merchant_1", "merchant_1_F", "merchant_1_F",tf_hero|tf_female,  0,0, fac_kingdom_1,[itm_courser,            itm_fighting_axe,       itm_leather_jerkin,         itm_leather_boots,          itm_straw_hat],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008200201e54c137a940c91],
##  ["merchant_2", "merchant_2", "merchant_2", tf_hero,               0,0, fac_kingdom_2,[itm_saddle_horse,       itm_arming_sword,       itm_light_leather,          itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000000000601db6db6db6db6db],
##  ["merchant_3", "merchant_3", "merchant_3", tf_hero,               0,0, fac_kingdom_3,[itm_courser,            itm_nordic_sword,       itm_leather_jerkin,         itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008100701db6db6db6db6db],
##  ["merchant_4", "merchant_4_F", "merchant_4_F",tf_hero|tf_female,  0,0, fac_kingdom_4,[itm_saddle_horse,       itm_falchion,           itm_light_leather,          itm_blue_hose,                              ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000010500401e54c137a945c91],
##  ["merchant_5", "merchant_5", "merchant_5", tf_hero,               0,0, fac_kingdom_5,[itm_saddle_horse,       itm_sword,              itm_ragged_outfit,          itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008038001e54c135a945c91],
##  ["merchant_6", "merchant_6", "merchant_6", tf_hero,               0,0, fac_kingdom_1,[itm_saddle_horse,      itm_scimitar,           itm_leather_jerkin,         itm_leather_boots,                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000000248e01e54c1b5a945c91],
##  ["merchant_7", "merchant_7_F", "merchant_7_F",tf_hero|tf_female,  0,0, fac_kingdom_2,[itm_hunter,            itm_arming_sword,       itm_padded_leather,         itm_blue_hose,                              ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000004200601c98ad39c97557a],
##  ["merchant_8", "merchant_8", "merchant_8", tf_hero,               0,0, fac_kingdom_3,[itm_saddle_horse,      itm_nordic_sword,       itm_light_leather,          itm_leather_boots,          itm_woolen_hood],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000001095ce01d6aad3a497557a],
##  ["merchant_9", "merchant_9", "merchant_9", tf_hero,               0,0, fac_kingdom_4,[itm_saddle_horse,      itm_sword,              itm_padded_leather,         itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000010519601ec26ae99898697],
##  ["merchant_10","merchant_10","merchant_10",tf_hero,               0,0, fac_merchants,[itm_hunter,             itm_bastard_sword,      itm_light_leather,          itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000884c401f6837d3294e28a],
##  ["merchant_11","merchant_11","merchant_11",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_sword,              itm_leather_jacket,         itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000c450501e289dd2c692694],
##  ["merchant_12","merchant_12","merchant_12",tf_hero,               0,0, fac_merchants,[itm_hunter,             itm_falchion,           itm_leather_jerkin,         itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000c660a01e5af3cb2763401],
##  ["merchant_13","merchant_13","merchant_13",tf_hero,               0,0, fac_merchants,[itm_sumpter_horse,      itm_nordic_sword,       itm_padded_leather,         itm_leather_boots,                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000001001d601ec912a89e4d534],
##  ["merchant_14","merchant_14","merchant_14",tf_hero,               0,0, fac_merchants,[itm_courser,            itm_bastard_sword,      itm_light_leather,          itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000004335601ea2c04a8b6a394],
##  ["merchant_15","merchant_15","merchant_15",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_sword,              itm_padded_leather,         itm_woolen_hose,            itm_fur_hat],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008358e01dbf27b6436089d],
##  ["merchant_16","merchant_16_F","merchant_16_F",tf_hero|tf_female, 0,0, fac_merchants,[itm_hunter,             itm_bastard_sword,      itm_light_leather,          itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000c300101db0b9921494add],
##  ["merchant_17","merchant_17","merchant_17",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_sword,              itm_leather_jacket,         itm_blue_hose,                              ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008740f01e945c360976a0a],
##  ["merchant_18","merchant_18","merchant_18",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_nordic_sword,       itm_padded_leather,         itm_leather_boots,                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008020c01fc2db3b4c97685],
##  ["merchant_19","merchant_19","merchant_19",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_falchion,           itm_leather_jerkin,         itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008118301f02af91892725b],
##  ["merchant_20","merchant_20_F","merchant_20_F",tf_hero|tf_female, 0,0, fac_merchants,[itm_courser,            itm_arming_sword,       itm_padded_leather,         itm_leather_boots,                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000010500401f6837d27688212],

  
#Seneschals
  ["town_1_seneschal", "{!}Town 1 Seneschal", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["town_2_seneschal", "{!}Town 2 Seneschal", "{!}Town 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_padded_leather,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["town_3_seneschal", "{!}Town 3 Seneschal", "{!}Town 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["town_4_seneschal", "{!}Town 4 Seneschal", "{!}Town 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["town_5_seneschal", "{!}Town 5 Seneschal", "{!}Town 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000000249101e7898999ac54c6],
  ["town_6_seneschal", "{!}Town 6 Seneschal", "{!}Town 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_red_gambeson,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000000010360b01cef8b57553d34e],
  ["town_7_seneschal", "{!}Town 7 Seneschal", "{!}Town7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000000018101f9487aa831dce4],
  ["town_8_seneschal", "{!}Town 8 Seneschal", "{!}Town 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_red_gambeson,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["town_9_seneschal", "{!}Town 9 Seneschal", "{!}Town 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["town_10_seneschal", "{!}Town 10 Seneschal", "{!}Town 10 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000010230c01ef41badb50465e],
  ["town_11_seneschal", "{!}Town 11 Seneschal", "{!}Town 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jacket,     itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["town_12_seneschal", "{!}Town 12 Seneschal", "{!}Town 12 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["town_13_seneschal", "{!}Town 13 Seneschal", "{!}Town 13 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["town_14_seneschal", "{!}Town 14 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_15_seneschal", "{!}Town 15 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_16_seneschal", "{!}Town 16 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_17_seneschal", "{!}Town17 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_18_seneschal", "{!}Town 18 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_19_seneschal", "{!}Town 19 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_20_seneschal", "{!}Town 20 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_21_seneschal", "{!}Town 21 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_22_seneschal", "{!}Town 22 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],

  ["castle_1_seneschal", "{!}Castle 1 Seneschal", "{!}Castle 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x000000000010360b01cef8b57553d34e],
  ["castle_2_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_nomad_armor,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_3_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_4_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_5_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_6_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_7_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_blue_gambeson,         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_8_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_9_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_10_seneschal", "{!}Castle 10 Seneschal", "{!}Castle 10 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_11_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_12_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_nomad_armor,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_13_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_14_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_15_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_16_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_17_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_blue_gambeson,         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_18_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_19_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_20_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_21_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_22_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_nomad_armor,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_23_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_24_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_25_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_26_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_27_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_blue_gambeson,         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_28_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_29_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_30_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_31_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_32_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_nomad_armor,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_33_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_34_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_35_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_36_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_37_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_blue_gambeson,         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_38_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_39_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_40_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_41_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_42_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_43_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_44_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_45_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_46_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_47_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_48_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_49_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],

#Arena Masters
  ["town_1_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_1_arena|entry(52),reserved,   fac_commoners,[itm_coarse_tunic,      itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_2_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_2_arena|entry(52),reserved,   fac_commoners,[itm_linen_tunic,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_3_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_3_arena|entry(52),reserved,   fac_commoners,[itm_nomad_armor,       itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_4_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_4_arena|entry(52),reserved,   fac_commoners,[itm_coarse_tunic,      itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_5_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_5_arena|entry(52),reserved,   fac_commoners,[itm_linen_tunic,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_6_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_6_arena|entry(52),reserved,   fac_commoners,[itm_leather_jerkin,    itm_leather_boots], def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_7_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_7_arena|entry(52),reserved,   fac_commoners,[itm_padded_leather,    itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_8_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_8_arena|entry(52),reserved,   fac_commoners,[itm_linen_tunic,       itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_9_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_9_arena|entry(52),reserved,   fac_commoners,[itm_padded_leather,    itm_leather_boots], def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_10_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_10_arena|entry(52),reserved,  fac_commoners,[itm_nomad_armor,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_11_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_11_arena|entry(52),reserved,  fac_commoners,[itm_coarse_tunic,      itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_12_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_12_arena|entry(52),reserved,  fac_commoners,[itm_leather_jerkin,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_13_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_13_arena|entry(52),reserved,  fac_commoners,[itm_coarse_tunic,      itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_14_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_14_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_15_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_15_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_16_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_16_arena|entry(52),reserved,  fac_commoners,[itm_fur_coat,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_17_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_17_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_18_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_18_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_19_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_19_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_20_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_20_arena|entry(52),reserved,  fac_commoners,[itm_fur_coat,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_21_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_21_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_22_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_22_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],



# Underground 

##  ["town_1_crook","Town 1 Crook","Town 1 Crook",tf_hero,                0,0, fac_neutral,[itm_linen_tunic,        itm_leather_boots       ],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x000000000004428401f46e44a27144e3],
##  ["town_2_crook","Town 2 Crook","Town 2 Crook",tf_hero|tf_female,      0,0, fac_neutral,[itm_lady_dress_ruby,    itm_turret_hat_ruby     ],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x000000000004300101c36db6db6db6db],
##  ["town_3_crook","Town 3 Crook","Town 3 Crook",tf_hero,                0,0, fac_neutral,[itm_leather_apron,      itm_hide_boots          ],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x00000000000c530701f17944a25164e1],
##  ["town_4_crook","Town 4 Crook","Town 4 Crook",tf_hero,                0,0, fac_neutral,[itm_coarse_tunic,       itm_hide_boots          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c840501f36db6db7134db],
##  ["town_5_crook","Town 5 Crook","Town 5 Crook",tf_hero,                0,0, fac_neutral,[itm_red_gambeson,       itm_blue_hose           ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c000601f36db6db7134db],
##  ["town_6_crook","Town 6 Crook","Town 6 Crook",tf_hero,                0,0, fac_neutral,[itm_coarse_tunic,       itm_hide_boots          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c10c801db6db6dd7598aa],
##  ["town_7_crook","Town 7 Crook","Town 7 Crook",tf_hero|tf_female,      0,0, fac_neutral,[itm_woolen_dress,       itm_woolen_hood         ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000010214101de2f64db6db58d],
##  
##  ["town_8_crook","Town 8 Crook","Town 8 Crook",tf_hero,                0,0, fac_neutral,[itm_leather_jacket,     itm_leather_boots       ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000010318401c96db4db6db58d],
##  ["town_9_crook","Town 9 Crook","Town 9 Crook",tf_hero,                0,0, fac_neutral,[itm_linen_tunic,        itm_hide_boots          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000008520501f16db4db6db58d],
##  ["town_10_crook","Town 10 Crook","Town 10 Crook",tf_hero,             0,0, fac_neutral,[itm_coarse_tunic,      itm_nomad_boots         ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000008600701f35144db6db8a2],
##  ["town_11_crook","Town 11 Crook","Town 11 Crook",tf_hero|tf_female,   0,0, fac_neutral,[itm_blue_dress,        itm_wimple_with_veil    ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000008408101f386c4db4dd514],
##  ["town_12_crook","Town 12 Crook","Town 12 Crook",tf_hero,             0,0, fac_neutral,[itm_coarse_tunic,      itm_hide_boots          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000870c501f386c4f34dbaa1],
##  ["town_13_crook","Town 13 Crook","Town 13 Crook",tf_hero,             0,0, fac_neutral,[itm_blue_gambeson,     itm_nomad_boots         ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c114901f245caf34dbaa1],
##  ["town_14_crook","Town 14 Crook","Town 14 Crook",tf_hero|tf_female,   0,0, fac_neutral,[itm_woolen_dress,      itm_turret_hat_ruby     ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000001021c001f545a49b6eb2bc],

# Armor Merchants
  #arena_masters_end = zendar_armorer

  ["town_1_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,           itm_leather_boots   ],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_2_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_woolen_dress,          itm_straw_hat       ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_3_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_red,        itm_hide_boots      ],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_4_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_red_gambeson,         itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_5_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,          itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_6_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,       itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_7_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,       itm_blue_hose       ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_8_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_leather,       itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_9_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_blue_gambeson,        itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_10_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,       itm_hide_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_11_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,        itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_12_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_red_gambeson,         itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_13_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jacket,       itm_hide_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_14_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_woolen_dress,         itm_headcloth       ],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_15_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_blue_gambeson,        itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_16_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,         itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_17_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,       itm_hide_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_18_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_woolen_dress,         itm_headcloth       ],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_19_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_blue_gambeson,        itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_20_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,         itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_21_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,       itm_hide_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_22_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_sarranid_common_dress,         itm_sarranid_head_cloth       ],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],

# Weapon merchants

  ["town_1_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,      itm_hide_boots,itm_straw_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_2_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,     itm_nomad_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_3_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,   itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_4_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,            itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_5_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,   itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_6_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,      itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_7_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,            itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_8_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_woolen_dress,     itm_wrapping_boots,itm_straw_hat],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_9_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,   itm_leather_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_10_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,     itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_11_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jacket,  itm_woolen_hose],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_12_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,           itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_13_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_red,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_14_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_blue,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_15_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jacket,  itm_woolen_hose],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_16_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,           itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_17_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_green,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_18_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_19_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jacket,  itm_sarranid_boots_a],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_20_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,           itm_sarranid_boots_a],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_21_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_green,     itm_sarranid_boots_a],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_22_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,     itm_sarranid_boots_a],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],

#Tavern keepers

  ["town_1_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_1_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_wrapping_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_2_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_2_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_3_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_3_tavern|entry(9),0,   fac_commoners,[itm_woolen_dress,        itm_hide_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_4_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_4_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_5_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_5_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_hide_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_6_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_6_tavern|entry(9),0,   fac_commoners,[itm_woolen_dress,        itm_hide_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_7_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_7_tavern|entry(9),0,   fac_commoners,[itm_woolen_dress,        itm_leather_boots,      itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_8_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_8_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,      itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_9_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_9_tavern|entry(9),0,   fac_commoners,[itm_woolen_dress,        itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_10_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_10_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_hide_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_11_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_11_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_12_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_12_tavern|entry(9),0,  fac_commoners,[itm_leather_apron,       itm_hide_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_13_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_13_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_hide_boots,     itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_14_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_14_tavern|entry(9),0,  fac_commoners,[itm_shirt,               itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_15_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_15_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_16_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_16_tavern|entry(9),0,  fac_commoners,[itm_leather_apron,       itm_hide_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_17_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_17_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_hide_boots,     itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_18_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_18_tavern|entry(9),0,  fac_commoners,[itm_shirt,               itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_19_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_19_tavern|entry(9),0,  fac_commoners,[itm_sarranid_dress_a,        itm_sarranid_boots_a],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_20_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_20_tavern|entry(9),0,  fac_commoners,[itm_sarranid_cloth_robe,       itm_sarranid_boots_a],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_21_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_21_tavern|entry(9),0,  fac_commoners,[itm_sarranid_common_dress,        itm_sarranid_boots_a,     itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_22_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_22_tavern|entry(9),0,  fac_commoners,[itm_sarranid_cloth_robe_b,               itm_sarranid_boots_a],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],

#Goods Merchants

  ["town_1_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_1_store|entry(9),0, fac_commoners,     [itm_coarse_tunic,  itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_2_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_2_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_3_merchant", "Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_3_store|entry(9),0, fac_commoners,     [itm_dress,         itm_leather_boots,  itm_straw_hat   ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_4_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_4_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_5_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_5_store|entry(9),0, fac_commoners,     [itm_nomad_armor,   itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_6_merchant", "Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_6_store|entry(9),0, fac_commoners,     [itm_woolen_dress,  itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_7_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_7_store|entry(9),0, fac_commoners,     [itm_leather_jerkin,itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_8_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_8_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_9_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_9_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_10_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_10_store|entry(9),0, fac_commoners,    [itm_leather_jerkin,itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_11_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_11_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_12_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_12_store|entry(9),0, fac_commoners,    [itm_woolen_dress,  itm_leather_boots,  itm_female_hood ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_13_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_13_store|entry(9),0, fac_commoners,    [itm_dress,         itm_leather_boots,  itm_straw_hat   ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_14_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_14_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_15_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_15_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_16_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_16_store|entry(9),0, fac_commoners,    [itm_woolen_dress,  itm_leather_boots,  itm_female_hood ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_17_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_17_store|entry(9),0, fac_commoners,    [itm_dress,         itm_leather_boots,  itm_straw_hat   ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_18_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_18_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_19_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_19_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_20_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_20_store|entry(9),0, fac_commoners,    [itm_sarranid_common_dress_b,  itm_sarranid_boots_a, itm_sarranid_felt_head_cloth_b  ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_21_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_21_store|entry(9),0, fac_commoners,    [itm_sarranid_dress_a,         itm_sarranid_boots_a,  itm_sarranid_felt_head_cloth  ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_22_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_22_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],

  ["salt_mine_merchant","Barezan","Barezan",                tf_hero|tf_is_merchant, scn_salt_mine|entry(1),0, fac_commoners,        [itm_leather_apron, itm_leather_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x00000000000c528601ea69b6e46dbdb6],

# Horse Merchants

  ["town_1_horse_merchant","Horse Merchant","{!}Town 1 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_blue_dress,           itm_blue_hose,      itm_female_hood],   def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_2_horse_merchant","Horse Merchant","{!}Town 2 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_linen_tunic,          itm_nomad_boots,],                      def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_3_horse_merchant","Horse Merchant","{!}Town 3 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_nomad_armor,          itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_4_horse_merchant","Horse Merchant","{!}Town 4 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_leather_jerkin,       itm_nomad_boots],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_5_horse_merchant","Horse Merchant","{!}Town 5 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_dress,                itm_woolen_hose,    itm_woolen_hood],   def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_6_horse_merchant","Horse Merchant","{!}Town 6 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,         itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_7_horse_merchant","Horse Merchant","{!}Town 7 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,         itm_leather_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_8_horse_merchant","Horse Merchant","{!}Town 8 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,         itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_9_horse_merchant","Horse Merchant","{!}Town 9 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_leather_jerkin,       itm_woolen_hose],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_10_horse_merchant","Horse Merchant","{!}Town 10 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_blue_dress,          itm_blue_hose,      itm_straw_hat],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_11_horse_merchant","Horse Merchant","{!}Town 11 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_nomad_armor,         itm_leather_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_12_horse_merchant","Horse Merchant","{!}Town 12 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_leather_jacket,      itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_13_horse_merchant","Horse Merchant","{!}Town 13 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_coarse_tunic,        itm_nomad_boots],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_14_horse_merchant","Horse Merchant","{!}Town 14 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_peasant_dress,       itm_blue_hose,      itm_headcloth],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_15_horse_merchant","Horse Merchant","{!}Town 15 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_nomad_armor,         itm_leather_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_16_horse_merchant","Horse Merchant","{!}Town 16 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_leather_jacket,      itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_17_horse_merchant","Horse Merchant","{!}Town 17 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_coarse_tunic,        itm_nomad_boots],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_18_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_peasant_dress,       itm_blue_hose,      itm_headcloth],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_19_horse_merchant","Horse Merchant","{!}Town 15 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_nomad_armor,         itm_sarranid_boots_a],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_20_horse_merchant","Horse Merchant","{!}Town 16 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_sarranid_cloth_robe,      itm_sarranid_boots_a],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_21_horse_merchant","Horse Merchant","{!}Town 17 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_sarranid_cloth_robe_b,        itm_sarranid_boots_a],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_22_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_sarranid_common_dress_b,       itm_blue_hose,      itm_sarranid_felt_head_cloth_b],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],


#Town Mayors    #itm_courtly_outfit itm_gambeson itm_blue_gambeson itm_red_gambeson itm_nobleman_outfit itm_rich_outfit
  ["town_1_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_courtly_outfit, itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["town_2_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_gambeson,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_3_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_blue_gambeson,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_4_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_fur_coat,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_5_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_nobleman_outfit,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_6_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_red_gambeson,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_7_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_rich_outfit,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_8_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_red_gambeson,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_9_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_courtly_outfit,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_10_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_11_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_leather_jacket,     itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_12_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_red_gambeson,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_13_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_nobleman_outfit,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_14_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_15_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_leather_jacket,     itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_16_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_fur_coat,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_17_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_nobleman_outfit,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_18_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_19_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,     itm_sarranid_boots_a],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_20_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,       itm_sarranid_boots_a], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_21_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,    itm_sarranid_boots_a],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_22_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,      itm_sarranid_boots_a],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],


#Village stores
  ["village_1_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_2_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_3_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_4_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_5_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                      man_face_old_1, man_face_older_2],
  ["village_6_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_7_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_8_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_9_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,         man_face_old_1, man_face_older_2],
  ["village_10_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_11_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_12_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_13_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_14_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_15_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_16_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_17_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_18_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_19_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots, itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_20_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_21_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_22_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_23_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_24_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_25_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                      man_face_old_1, man_face_older_2],
  ["village_26_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_27_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_28_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_29_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_30_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_31_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_32_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_33_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_34_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_35_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_36_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_37_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_38_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_39_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_40_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_41_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_42_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_43_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_44_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_45_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_46_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_47_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_48_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_49_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_50_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_51_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_52_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_53_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_54_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_55_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_56_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_57_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_58_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_59_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_60_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_61_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_62_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_63_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_64_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_65_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_66_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_67_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_68_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_69_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_70_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_71_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_72_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_73_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_74_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_75_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_76_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_77_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_78_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_79_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_80_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_81_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_82_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_83_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_84_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_85_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_86_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_87_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_88_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_89_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_90_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_91_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_92_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_93_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_94_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_95_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_96_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_97_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_98_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_99_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_100_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_101_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_102_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_103_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_104_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_105_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_106_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_107_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_108_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_109_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_110_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
# Place extra merchants before this point
  ["merchants_end","merchants_end","merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],

  #Used for player enterprises
  ["town_1_master_craftsman", "{!}Town 1 Craftsman", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_2_master_craftsman", "{!}Town 2 Craftsman", "{!}Town 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_padded_leather,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x0000000f010811c92d3295e46a96c72300000000001f5a980000000000000000],
  ["town_3_master_craftsman", "{!}Town 3 Craftsman", "{!}Town 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000001b083203151d2ad5648e52b400000000001b172e0000000000000000],
  ["town_4_master_craftsman", "{!}Town 4 Craftsman", "{!}Town 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000001a10114f091b2c259cd4c92300000000000228dd0000000000000000],
  ["town_5_master_craftsman", "{!}Town 5 Craftsman", "{!}Town 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000d1044c578598cd92b5256db00000000001f23340000000000000000],
  ["town_6_master_craftsman", "{!}Town 6 Craftsman", "{!}Town 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000001f046285493eaf1b048abcdb00000000001a8aad0000000000000000],
  ["town_7_master_craftsman", "{!}Town 7 Craftsman", "{!}Town 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000002b0052c34c549225619356d400000000001cc6e60000000000000000],
  ["town_8_master_craftsman", "{!}Town 8 Craftsman", "{!}Town 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x0000000fdb0c20465b6e51e8a12c82d400000000001e148c0000000000000000],
  ["town_9_master_craftsman", "{!}Town 9 Craftsman", "{!}Town 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000009f7005246071db236e296a45300000000001a8b0a0000000000000000],
  ["town_10_master_craftsman", "{!}Town 10 Craftsman", "{!}Town 10 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000009f71012c2456a921aa379321a000000000012c6d90000000000000000],
  ["town_11_master_craftsman", "{!}Town 11 Craftsman", "{!}Town 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,     itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x00000009f308514428db71b9ad70b72400000000001dc9140000000000000000],
  ["town_12_master_craftsman", "{!}Town 12 Seneschal", "{!}Town 12 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000009e90825863853a5b91cd71a5b00000000000598db0000000000000000],
  ["town_13_master_craftsman", "{!}Town 13 Seneschal", "{!}Town 13 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000009fa0c708f274c8eb4c64e271300000000001eb69a0000000000000000],
  ["town_14_master_craftsman", "{!}Town 14 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000007590c3206155c8b475a4e439a00000000001f489a0000000000000000],
  ["town_15_master_craftsman", "{!}Town 15 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000007440022d04b2c6cb7d3723d5a00000000001dc90a0000000000000000],
  ["town_16_master_craftsman", "{!}Town 16 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000007680c3586054b8e372e4db65c00000000001db7230000000000000000],
  ["town_17_master_craftsman", "{!}Town 17 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x0000000766046186591b564cec85d2e200000000001e4cea0000000000000000],
  ["town_18_master_craftsman", "{!}Town 18 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x0000000e7e0075523a6aa9b6da61e8dd00000000001d96d30000000000000000],
  ["town_19_master_craftsman", "{!}Town 19 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000002408314852a432e88aaa42e100000000001e284e0000000000000000],
  ["town_20_master_craftsman", "{!}Town 20 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe_b,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000001104449136e44cbd1c9352bc000000000005e8d10000000000000000],
  ["town_21_master_craftsman", "{!}Town 21 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000000131032d3351c6e43226ec96c000000000005b5240000000000000000],
  ["town_22_master_craftsman", "{!}Town 22 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe_b,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000000200c658a5723b1a3148dc455000000000015ab920000000000000000],
  
  
  
# Chests
  ["zendar_chest","{!}Zendar Chest","{!}Zendar Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,
   [],def_attrib|level(18),wp(60),knows_common, 0],
  ["tutorial_chest_1","{!}Melee Weapons Chest","{!}Melee Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_tutorial_sword, itm_tutorial_axe, itm_tutorial_spear, itm_tutorial_club, itm_tutorial_battle_axe],def_attrib|level(18),wp(60),knows_common, 0],
  ["tutorial_chest_2","{!}Ranged Weapons Chest","{!}Ranged Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_tutorial_short_bow, itm_tutorial_arrows, itm_tutorial_crossbow, itm_tutorial_bolts, itm_tutorial_throwing_daggers],def_attrib|level(18),wp(60),knows_common, 0],
  ["bonus_chest_1","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_strange_armor,itm_strange_short_sword],def_attrib|level(18),wp(60),knows_common, 0],
  ["bonus_chest_2","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_strange_boots,itm_strange_sword],def_attrib|level(18),wp(60),knows_common, 0],
  ["bonus_chest_3","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_strange_helmet,itm_strange_great_sword],def_attrib|level(18),wp(60),knows_common, 0],

  ["household_possessions","{!}household_possessions","{!}household_possessions",tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],  
  
# These are used as arrays in the scripts.
  ["temp_array_a","{!}temp_array_a","{!}temp_array_a",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
  ["temp_array_b","{!}temp_array_b","{!}temp_array_b",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
  ["temp_array_c","{!}temp_array_c","{!}temp_array_c",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],

  ["stack_selection_amounts","{!}stack_selection_amounts","{!}stack_selection_amounts",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
  ["stack_selection_ids","{!}stack_selection_ids","{!}stack_selection_ids",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

  ["notification_menu_types","{!}notification_menu_types","{!}notification_menu_types",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
  ["notification_menu_var1","{!}notification_menu_var1","{!}notification_menu_var1",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
  ["notification_menu_var2","{!}notification_menu_var2","{!}notification_menu_var2",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

  ["banner_background_color_array","{!}banner_background_color_array","{!}banner_background_color_array",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

  ["multiplayer_data","{!}multiplayer_data","{!}multiplayer_data",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

##  ["black_khergit_guard","Black Khergit Guard","Black Khergit Guard",tf_mounted|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_black_khergits,
##   [itm_arrows,itm_nomad_sabre,itm_scimitar,itm_winged_mace,itm_lance,itm_khergit_bow,itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_khergit_guard_boots,itm_khergit_guard_armor,itm_nomad_shield,itm_steppe_horse,itm_warhorse],
##   def_attrib|level(28),wp(140),knows_riding_6|knows_ironflesh_4|knows_horse_archery_6|knows_power_draw_6,khergit_face1, khergit_face2],


# Add Extra Quest NPCs below this point  

  ["local_merchant","Local Merchant","Local Merchants",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["tax_rebel","Peasant Rebel","Peasant Rebels",tf_guarantee_armor,0,reserved,fac_commoners,
   [itm_cleaver,itm_knife,itm_pitch_fork,itm_sickle,itm_club,itm_stones,itm_leather_cap,itm_felt_hat,itm_felt_hat,itm_linen_tunic,itm_coarse_tunic,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,vaegir_face1, vaegir_face2],
  ["trainee_peasant","Peasant","Peasants",tf_guarantee_armor,0,reserved,fac_commoners,
   [itm_cleaver,itm_knife,itm_pitch_fork,itm_sickle,itm_club,itm_stones,itm_leather_cap,itm_felt_hat,itm_felt_hat,itm_linen_tunic,itm_coarse_tunic,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,vaegir_face1, vaegir_face2],
  ["fugitive","Nervous Man","Nervous Men",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_short_tunic,itm_linen_tunic,itm_coarse_tunic, itm_tabard, itm_leather_vest, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_wrapping_boots, itm_fur_hat, itm_leather_cap, itm_sword_medieval_b, itm_throwing_daggers],
   def_attrib|str_24|agi_25|level(26),wp(180),knows_common|knows_power_throw_6|knows_power_strike_6|knows_ironflesh_9,man_face_middle_1, man_face_old_2],
   
  ["belligerent_drunk","Belligerent Drunk","Belligerent Drunks",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_short_tunic,itm_linen_tunic,itm_coarse_tunic, itm_tabard, itm_leather_vest, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_wrapping_boots, itm_fur_hat, itm_leather_cap, itm_sword_viking_1],
   def_attrib|str_20|agi_8|level(15),wp(120),knows_common|knows_power_strike_2|knows_ironflesh_9,    bandit_face1, bandit_face2],

  ["hired_assassin","Hired Assassin","Hired Assassin",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners, #they look like belligerent drunks
   [itm_short_tunic,itm_linen_tunic,itm_coarse_tunic, itm_tabard, itm_leather_vest, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_wrapping_boots, itm_fur_hat, itm_leather_cap, itm_sword_viking_1],
   def_attrib|str_20|agi_16|level(20),wp(180),knows_common|knows_power_strike_5|knows_ironflesh_3,    bandit_face1, bandit_face2],

  ["fight_promoter","Rough-Looking Character","Rough-Looking Character",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_short_tunic,itm_linen_tunic,itm_coarse_tunic, itm_tabard, itm_leather_vest, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_wrapping_boots, itm_fur_hat, itm_leather_cap, itm_sword_viking_1],
   def_attrib|str_20|agi_16|level(20),wp(180),knows_common|knows_power_strike_5|knows_ironflesh_3,    bandit_face1, bandit_face2],

   
   
  ["spy","Ordinary Townsman","Ordinary Townsmen", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
   [itm_sword_viking_1,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves],
   def_attrib|agi_11|level(20),wp(130),knows_common,man_face_middle_1, man_face_older_2],
   
  ["spy_partner","Unremarkable Townsman","Unremarkable Townsmen", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
   [itm_sword_medieval_b,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves],
   def_attrib|agi_11|level(10),wp(130),knows_common,vaegir_face1, vaegir_face2],

   ["nurse_for_lady","Nurse","Nurse",tf_female|tf_guarantee_armor,0,reserved,fac_commoners,
   [itm_robe, itm_black_hood, itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,woman_face_1, woman_face_2],   
   ["temporary_minister","Minister","Minister",tf_guarantee_armor|tf_guarantee_boots,0,reserved,fac_commoners,
   [itm_rich_outfit, itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_older_2],   
   
   
##  ["conspirator","Conspirator","Conspirators", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
##   [itm_sword,itm_leather_jerkin,itm_leather_boots,itm_hunter,itm_leather_gloves],
##   def_attrib|agi_11|level(10),wp(130),knows_common,vaegir_face1, vaegir_face2],
##  ["conspirator_leader","Conspirator","Conspirators", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
##   [itm_sword,itm_leather_jerkin,itm_leather_boots,itm_hunter,itm_leather_gloves],
##   def_attrib|agi_11|level(10),wp(130),knows_common,vaegir_face1, vaegir_face2],
##  ["peasant_rebel","Peasant Rebel","Peasant Rebels",tf_guarantee_armor,0,reserved,fac_peasant_rebels,
##   [itm_cleaver,itm_knife,itm_pitch_fork,itm_sickle,itm_club,itm_stones,itm_leather_cap,itm_felt_hat,itm_felt_hat,itm_linen_tunic,itm_coarse_tunic,itm_nomad_boots,itm_wrapping_boots],
##   def_attrib|level(4),wp(60),knows_common,vaegir_face1, vaegir_face2],
##  ["noble_refugee","Noble Refugee","Noble Refugees",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_noble_refugees,
##   [itm_sword,itm_leather_jacket,itm_hide_boots, itm_saddle_horse, itm_leather_jacket, itm_leather_cap],
##   def_attrib|level(9),wp(100),knows_common,swadian_face1, swadian_face2],
##  ["noble_refugee_woman","Noble Refugee Woman","Noble Refugee Women",tf_female|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_noble_refugees,
##   [itm_knife,itm_dagger,itm_hunting_crossbow,itm_dress,itm_robe,itm_woolen_dress, itm_headcloth, itm_woolen_hood, itm_wrapping_boots],
##   def_attrib|level(3),wp(45),knows_common,refugee_face1,refugee_face2],


  ["quick_battle_6_player", "{!}quick_battle_6_player", "{!}quick_battle_6_player", tf_hero, 0, reserved,  fac_player_faction, [itm_padded_cloth,itm_nomad_boots, itm_splinted_leather_greaves, itm_skullcap, itm_sword_medieval_b,  itm_crossbow, itm_bolts, itm_plate_covered_round_shield],    knight_attrib_1,wp(130),knight_skills_1, 0x000000000008010b01f041a9249f65fd],

#Multiplayer ai troops
  ["silver_rose_trained_crossbowman_multiplayer_ai","Swadian Crossbowman","Swadian Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_bolts,itm_crossbow,itm_sword_medieval_a,itm_tab_shield_heater_b,
    itm_leather_jerkin,itm_leather_armor,itm_ankle_boots,itm_footman_helmet],
   def_attrib|level(19),wp_melee(90)|wp_crossbow(100),knows_common|knows_ironflesh_4|knows_athletics_6|knows_shield_5|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
  ["silver_rose_infantry_multiplayer_ai","Swadian Infantry","Swadian Infantry",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_1,
   [itm_pike,itm_bastard_sword_a,itm_tab_shield_heater_c,
    itm_studded_leather_coat,itm_ankle_boots,itm_flat_topped_helmet],
   def_attrib|level(19),wp_melee(105),knows_common|knows_ironflesh_5|knows_shield_4|knows_power_strike_5|knows_athletics_4,swadian_face_middle_1, swadian_face_old_2],
  ["silver_rose_man_at_arms_multiplayer_ai","Swadian Man at Arms","Swadian Men at Arms",tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac_kingdom_1,
   [itm_lance,itm_bastard_sword_a,itm_tab_shield_heater_cav_a,
    itm_mail_with_surcoat,itm_hide_boots,itm_norman_helmet,itm_hunter],
   def_attrib|level(19),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_4|knows_shield_4|knows_power_strike_4|knows_athletics_1,swadian_face_young_1, swadian_face_old_2],
  ["vaegir_archer_multiplayer_ai","Vaegir Archer","Vaegir Archers",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_arrows,itm_scimitar,itm_nomad_bow,
    itm_leather_vest,itm_nomad_boots,itm_spiked_helmet,itm_nomad_cap],
   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_4|knows_power_draw_5|knows_athletics_6|knows_shield_2,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_spearman_multiplayer_ai","Vaegir Spearman","Vaegir Spearmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_2,
   [itm_padded_leather,itm_nomad_boots,itm_spiked_helmet,itm_nomad_cap, itm_spear, itm_tab_shield_kite_b, itm_mace_1, itm_javelin],
   def_attrib|str_12|level(19),wp_melee(90),knows_ironflesh_4|knows_athletics_6|knows_power_throw_3|knows_power_strike_3|knows_shield_2,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_horseman_multiplayer_ai","Vaegir Horseman","Vaegir Horsemen",tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac_kingdom_2,
   [itm_battle_axe,itm_scimitar,itm_lance,itm_tab_shield_kite_cav_a,
     itm_studded_leather_coat,itm_lamellar_vest,itm_nomad_boots,itm_spiked_helmet,itm_saddle_horse],
   def_attrib|level(19),wp(100),knows_riding_4|knows_ironflesh_4|knows_power_strike_4|knows_shield_3,vaegir_face_young_1, vaegir_face_older_2],
  ["khergit_dismounted_lancer_multiplayer_ai","Khergit Dismounted Lancer","Khergit Dismounted Lancer",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_3,
   [itm_sword_khergit_4,itm_spiked_mace,itm_one_handed_war_axe_b,itm_one_handed_war_axe_a,itm_hafted_blade_a,itm_hafted_blade_b,itm_heavy_lance,itm_lance,
    itm_khergit_cavalry_helmet,itm_khergit_war_helmet,itm_lamellar_vest_khergit,itm_tribal_warrior_outfit,itm_khergit_leather_boots,itm_splinted_leather_greaves,itm_leather_gloves,itm_mail_mittens,itm_tab_shield_small_round_b,itm_tab_shield_small_round_c],
   def_attrib|level(19),wp(100),knows_riding_4|knows_power_strike_1|knows_power_draw_4|knows_power_throw_2|knows_ironflesh_1|knows_horse_archery_1,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_veteran_horse_archer_multiplayer_ai","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_khergit_3,itm_khergit_bow,itm_khergit_arrows,itm_tab_shield_small_round_b,
    itm_khergit_cavalry_helmet,itm_tribal_warrior_outfit,itm_khergit_leather_boots,itm_steppe_horse],
   def_attrib|level(19),wp(90)|wp_archery(100),knows_riding_6|knows_power_draw_5|knows_shield_2|knows_horse_archery_5,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_lancer_multiplayer_ai","Khergit Lancer","Khergit Lancers",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_3,
   [itm_sword_khergit_4,itm_spiked_mace,itm_one_handed_war_axe_b,itm_one_handed_war_axe_a,itm_hafted_blade_a,itm_hafted_blade_b,itm_heavy_lance,itm_lance,
    itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_khergit_war_helmet,itm_lamellar_vest_khergit,itm_lamellar_armor,itm_khergit_leather_boots,itm_splinted_leather_greaves,itm_leather_gloves,itm_mail_mittens,itm_scale_gauntlets,itm_tab_shield_small_round_b,itm_tab_shield_small_round_c,itm_courser],
   def_attrib|level(19),wp(100),knows_riding_7|knows_power_strike_2|knows_power_draw_4|knows_power_throw_2|knows_ironflesh_1|knows_horse_archery_1,khergit_face_middle_1, khergit_face_older_2],
  ["nord_veteran_multiplayer_ai","Nord Footman","Nord Footmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_4,
   [itm_sword_viking_2,itm_one_handed_battle_axe_b,itm_two_handed_axe,itm_tab_shield_round_d,itm_throwing_axes,
    itm_nordic_helmet,itm_nordic_fighter_helmet,itm_mail_hauberk,itm_splinted_leather_greaves,itm_leather_boots,itm_leather_gloves],
   def_attrib|level(19),wp(130),knows_ironflesh_3|knows_power_strike_5|knows_power_throw_3|knows_athletics_5|knows_shield_3,nord_face_young_1, nord_face_older_2],
  ["nord_scout_multiplayer_ai","Nord Scout","Nord Scouts",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_javelin,itm_sword_viking_1,itm_two_handed_axe,itm_spear,itm_tab_shield_round_a,
    itm_skullcap,itm_nordic_archer_helmet,itm_leather_jerkin,itm_leather_boots,itm_saddle_horse],
   def_attrib|level(19),wp(100),knows_riding_5|knows_ironflesh_2|knows_power_strike_2|knows_shield_1|knows_horse_archery_2|knows_power_throw_3,nord_face_young_1, nord_face_older_2],
  ["nord_archer_multiplayer_ai","Nord Archer","Nord Archers",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_arrows,itm_two_handed_axe,itm_sword_viking_2,itm_short_bow,
    itm_leather_jerkin,itm_blue_tunic,itm_leather_boots,itm_nasal_helmet,itm_leather_cap],
   def_attrib|str_11|level(19),wp_melee(80)|wp_archery(110),knows_ironflesh_4|knows_power_strike_2|knows_shield_1|knows_power_draw_5|knows_athletics_6,nord_face_young_1, nord_face_old_2],
  ["rhodok_veteran_crossbowman_multiplayer_ai","Rhodok Crossbowman","Rhodok Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_fighting_pick,itm_club_with_spike_head,itm_maul,itm_tab_shield_pavise_c,itm_heavy_crossbow,itm_bolts,
    itm_leather_cap,itm_padded_leather,itm_nomad_boots],
   def_attrib|level(19),wp_melee(100)|wp_crossbow(120),knows_common|knows_ironflesh_4|knows_shield_5|knows_power_strike_3|knows_athletics_6,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_veteran_spearman_multiplayer_ai","Rhodok Spearman","Rhodok Spearmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_5,
   [itm_ashwood_pike,itm_war_spear,itm_pike,itm_club_with_spike_head,itm_sledgehammer,itm_tab_shield_pavise_c,itm_sword_medieval_a,
    itm_leather_cap,itm_byrnie,itm_ragged_outfit,itm_nomad_boots],
   def_attrib|level(19),wp(115),knows_common|knows_ironflesh_5|knows_shield_3|knows_power_strike_4|knows_athletics_3,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_scout_multiplayer_ai","Rhodok Scout","Rhodok Scouts",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_5,
   #TODO: Change weapons, copied from Nord Scout
   [itm_sword_medieval_a,itm_tab_shield_heater_cav_a,itm_light_lance,itm_skullcap,itm_aketon_green,
    itm_ragged_outfit,itm_nomad_boots,itm_ankle_boots,itm_saddle_horse],
   def_attrib|level(19),wp(100),knows_riding_5|knows_ironflesh_2|knows_power_strike_2|knows_shield_1|knows_horse_archery_2|knows_power_throw_3,rhodok_face_young_1, rhodok_face_older_2],
  ["sarranid_infantry_multiplayer_ai","Sarranid Infantry","Sarranid Infantries",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_6,
   [itm_sarranid_mail_shirt,itm_sarranid_horseman_helmet,itm_sarranid_boots_b,itm_sarranid_boots_c,itm_splinted_leather_greaves,itm_arabian_sword_b,itm_mace_3,itm_spear,itm_tab_shield_kite_c],
   def_attrib|level(20),wp_melee(105),knows_common|knows_riding_3|knows_ironflesh_2|knows_shield_3,swadian_face_middle_1, swadian_face_old_2],
  ["sarranid_archer_multiplayer_ai","Sarranid Archer","Sarranid Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [itm_arrows,itm_nomad_bow,itm_arabian_sword_a,itm_archers_vest,itm_sarranid_boots_b,itm_sarranid_helmet1,itm_turban,itm_desert_turban],
   def_attrib|level(19),wp_melee(90)|wp_archery(100),knows_common|knows_riding_2|knows_ironflesh_1,swadian_face_young_1, swadian_face_old_2],
  ["sarranid_horseman_multiplayer_ai","Sarranid Horseman","Sarranid Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_6,
   [itm_lance,itm_arabian_sword_b,itm_scimitar_b,itm_mace_4,itm_tab_shield_small_round_b,
    itm_sarranid_mail_shirt,itm_sarranid_boots_b,itm_sarranid_boots_c,itm_sarranid_horseman_helmet,itm_courser,itm_hunter],
   def_attrib|level(20),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],

   
   
#Multiplayer troops (they must have the base items only, nothing else)
  ["silver_rose_trained_crossbowman_multiplayer","Swadian Crossbowman","Swadian Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_bolts,itm_crossbow,itm_sword_medieval_b_small,itm_tab_shield_heater_a,itm_red_shirt,itm_ankle_boots],
   str_14 | agi_15 |def_attrib_multiplayer|level(19),wpe(90,60,180,90),knows_common_multiplayer|knows_ironflesh_2|knows_athletics_4|knows_shield_5|knows_power_strike_2|knows_riding_1,swadian_face_young_1, swadian_face_old_2],
  ["silver_rose_infantry_multiplayer","Swadian Infantry","Swadian Infantry",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_sword_medieval_a,itm_tab_shield_heater_a,itm_red_tunic,itm_ankle_boots],
   str_15 | agi_15 |def_attrib_multiplayer|level(20),wpex(105,130,110,40,60,110),knows_common_multiplayer|knows_ironflesh_5|knows_shield_4|knows_power_strike_4|knows_power_throw_2|knows_athletics_6|knows_riding_1,swadian_face_middle_1, swadian_face_old_2],
  ["silver_rose_man_at_arms_multiplayer","Swadian Man at Arms","Swadian Men at Arms",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_lance,itm_sword_medieval_a,itm_tab_shield_heater_a,
    itm_red_tunic,itm_ankle_boots,itm_saddle_horse],
   str_14 | agi_16 |def_attrib_multiplayer|level(20),wp_melee(110),knows_common_multiplayer|knows_riding_5|knows_ironflesh_3|knows_shield_2|knows_power_throw_2|knows_power_strike_3|knows_athletics_3,swadian_face_young_1, swadian_face_old_2],
#  ["swadian_mounted_crossbowman_multiplayer","Swadian Mounted Crossbowman","Swadian Mounted Crossbowmen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_1,
#   [itm_bolts,itm_light_crossbow,itm_tab_shield_heater_cav_a,itm_bastard_sword_a,
#    itm_red_shirt,itm_hide_boots,itm_saddle_horse],
#   def_attrib_multiplayer|level(20),wp_melee(100)|wp_crossbow(120),knows_common_multiplayer|knows_riding_4|knows_shield_3|knows_ironflesh_3|knows_horse_archery_2|knows_power_strike_3|knows_athletics_2|knows_shield_2,swadian_face_young_1, swadian_face_old_2],
  ["vaegir_archer_multiplayer","Vaegir Archer","Vaegir Archers",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_arrows,itm_mace_1,itm_nomad_bow,
    itm_linen_tunic,itm_hide_boots],
   str_14 | agi_14 |def_attrib_multiplayer|str_12|level(19),wpe(80,150,60,80),knows_common_multiplayer|knows_ironflesh_2|knows_power_draw_7|knows_athletics_3|knows_shield_2|knows_riding_1,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_spearman_multiplayer","Vaegir Spearman","Vaegir spearman",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_spear, itm_tab_shield_kite_a, itm_mace_1,
    itm_linen_tunic,itm_hide_boots],
   str_15 | agi_15 |def_attrib_multiplayer|str_12|level(19),wpex(110,100,130,30,50,120),knows_common_multiplayer|knows_ironflesh_4|knows_shield_2|knows_power_throw_3|knows_power_strike_4|knows_athletics_6|knows_riding_1,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_horseman_multiplayer","Vaegir Horseman","Vaegir Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_scimitar,itm_lance,itm_tab_shield_kite_cav_a,
    itm_linen_tunic,itm_hide_boots,itm_saddle_horse],
   str_16 | agi_15 |def_attrib_multiplayer|level(19),wpe(110,90,60,110),knows_common_multiplayer|knows_riding_5|knows_ironflesh_4|knows_power_strike_3|knows_shield_3|knows_power_throw_4|knows_horse_archery_1,vaegir_face_young_1, vaegir_face_older_2],
  ["khergit_veteran_horse_archer_multiplayer","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_khergit_1,itm_nomad_bow,itm_arrows,
    itm_khergit_armor,itm_leather_steppe_cap_a,itm_hide_boots,itm_steppe_horse],
   str_15 | agi_18 |def_attrib_multiplayer|level(21),wpe(70,142,60,100),knows_common_multiplayer|knows_riding_2|knows_power_draw_5|knows_horse_archery_3|knows_athletics_3|knows_shield_1,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_infantry_multiplayer","Khergit Infantry","Khergit Infantries",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_khergit_1,itm_spear,itm_tab_shield_small_round_a,
    itm_steppe_armor,itm_hide_boots,itm_leather_gloves],
   str_14 | agi_15 |def_attrib_multiplayer|level(19),wp(110),knows_common_multiplayer|knows_ironflesh_3|knows_power_throw_3|knows_shield_4|knows_power_strike_3|knows_athletics_6|knows_riding_1,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_lancer_multiplayer","Khergit Lancer","Khergit Lancers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_khergit_1,itm_lance,itm_tab_shield_small_round_a,
    itm_khergit_armor,itm_leather_steppe_cap_a,itm_hide_boots,itm_steppe_horse],
   str_15 | agi_14 |def_attrib_multiplayer|level(21),wp(115),knows_common_multiplayer|knows_riding_6|knows_ironflesh_3|knows_power_throw_3|knows_shield_4|knows_power_strike_3|knows_athletics_4,khergit_face_middle_1, khergit_face_older_2],
  ["nord_archer_multiplayer","Nord Archer","Nord Archers",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_arrows,itm_sword_viking_2_small,itm_short_bow,
    itm_blue_tunic,itm_leather_boots],
   str_15 | agi_14 |def_attrib_multiplayer|str_11|level(15),wpe(90,150,60,80),knows_common_multiplayer|knows_ironflesh_2|knows_power_strike_2|knows_shield_3|knows_power_draw_5|knows_athletics_3|knows_riding_1,nord_face_young_1, nord_face_old_2],
  ["nord_veteran_multiplayer","Nord Huscarl","Nord Huscarls",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_sword_viking_1,itm_one_handed_war_axe_a,itm_tab_shield_round_a,
    itm_blue_tunic,itm_leather_boots],
   str_17 | agi_15 |def_attrib_multiplayer|level(24),wpex(110,135,100,40,60,140),knows_common_multiplayer|knows_ironflesh_4|knows_power_strike_5|knows_power_throw_4|knows_athletics_6|knows_shield_3|knows_riding_1,nord_face_young_1, nord_face_older_2],
  ["nord_scout_multiplayer","Nord Scout","Nord Scouts",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_javelin,itm_sword_viking_1,itm_spear,itm_tab_shield_small_round_a,
    itm_blue_tunic,itm_leather_boots,itm_saddle_horse],
   str_16 | agi_15 |def_attrib_multiplayer|level(19),wp(105),knows_common_multiplayer|knows_riding_6|knows_ironflesh_2|knows_power_strike_2|knows_shield_1|knows_horse_archery_3|knows_power_throw_3|knows_athletics_3,vaegir_face_young_1, vaegir_face_older_2],
  ["rhodok_veteran_crossbowman_multiplayer","Rhodok Crossbowman","Rhodok Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_crossbow,itm_bolts,itm_fighting_pick,itm_tab_shield_pavise_a,
    itm_tunic_with_green_cape,itm_ankle_boots],
   str_16 | agi_15 |def_attrib_multiplayer|level(20),wpe(100,60,180,90),knows_common_multiplayer|knows_ironflesh_2|knows_shield_2|knows_power_strike_2|knows_athletics_4|knows_riding_1,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_sergeant_multiplayer","Rhodok Sergeant","Rhodok Sergeants",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_fighting_pick,itm_tab_shield_pavise_a,itm_spear,
    itm_green_tunic,itm_ankle_boots],
   str_16 | agi_14 |def_attrib_multiplayer|level(20),wpex(110,100,140,30,50,110),knows_common_multiplayer|knows_ironflesh_4|knows_shield_5|knows_power_strike_4|knows_power_throw_1|knows_athletics_6|knows_riding_1,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_horseman_multiplayer","Rhodok Horseman","Rhodok Horsemen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_sword_medieval_a,itm_tab_shield_heater_cav_a, itm_light_lance, 
    itm_green_tunic,itm_ankle_boots,itm_saddle_horse],
   str_15 | agi_15 |def_attrib_multiplayer|level(20),wp(100),knows_common_multiplayer|knows_riding_4|knows_ironflesh_3|knows_shield_3|knows_power_strike_3|knows_power_throw_1|knows_athletics_3,rhodok_face_middle_1, rhodok_face_older_2],
  ["sarranid_archer_multiplayer","Sarranid Archer","Sarranid Archers",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_arrows,itm_arabian_sword_a,itm_nomad_bow,
    itm_sarranid_cloth_robe, itm_sarranid_boots_b],
   str_15 | agi_16 |def_attrib_multiplayer|str_12|level(19),wpe(80,150,60,80),knows_common_multiplayer|knows_ironflesh_4|knows_power_draw_5|knows_athletics_3|knows_shield_2|knows_riding_1|knows_weapon_master_1,vaegir_face_young_1, vaegir_face_older_2],
  ["sarranid_footman_multiplayer","Sarranid Footman","Sarranid footman",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_bamboo_spear, itm_tab_shield_kite_a, itm_arabian_sword_a,
    itm_sarranid_cloth_robe, itm_sarranid_boots_b],
   str_14 | agi_15 |def_attrib_multiplayer|str_12|level(19),wpex(110,100,130,30,50,120),knows_common_multiplayer|knows_ironflesh_4|knows_shield_2|knows_power_throw_3|knows_power_strike_4|knows_athletics_6|knows_riding_1,vaegir_face_young_1, vaegir_face_older_2],
  ["sarranid_mamluke_multiplayer","Sarranid Mamluke","Sarranid Mamluke",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_arabian_sword_a,itm_lance,itm_tab_shield_small_round_a,
    itm_sarranid_cloth_robe, itm_sarranid_boots_b,itm_saddle_horse],
   str_15 | agi_14 |def_attrib_multiplayer|level(19),wpe(110,90,60,110),knows_common_multiplayer|knows_riding_5|knows_ironflesh_3|knows_power_strike_2|knows_shield_3|knows_power_throw_2|knows_weapon_master_1,vaegir_face_young_1, vaegir_face_older_2],


   ["multiplayer_end","{!}multiplayer_end","{!}multiplayer_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],
   
   #Player history array
  ["log_array_entry_type",            "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_entry_time",            "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_actor",                 "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_center_object",         "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_center_object_lord",    "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_center_object_faction", "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_troop_object",          "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_troop_object_faction",  "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_faction_object",        "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],

  ["quick_battle_troop_1","Sir Artorio of Nerpa","Sir Artorio of Nerpa", tf_hero,0,0,fac_kingdom_1, [itm_m_sallet_black_a, itm_m_brigandine_a, itm_m_gauntlets_b, itm_m_greaves_a, itm_tab_shield_pavise_d, itm_throwing_spears, itm_german_poleaxe],str_30|agi_30|int_12|cha_12|level(55),wpex(400,300,500,200,200,350),knows_athletics_10|knows_shield_7|knows_weapon_master_7|knows_power_throw_8|knows_power_strike_9|knows_ironflesh_10,0x0000000e7f10400836db6db6db6ddbb600000000001db6db0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_2","Borato","Borato", tf_hero,0,0,fac_kingdom_1,[itm_m_kattle_a, itm_m_brigandine_b, itm_m_gloves_a, itm_m_greaves_b, itm_tab_shield_heater_d, itm_italian_falchion, itm_sniper_crossbow, itm_steel_bolts], str_30|agi_30|int_11|cha_18|level(54),wpex(400,100,200,450,100,100),knows_athletics_10|knows_shield_10|knows_weapon_master_10|knows_power_strike_8|knows_ironflesh_8,0x000000097f1065c636db6db6db6ddbb600000000001db6db0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_3","Francisco","Francisco", tf_hero,0,0,fac_kingdom_1, [itm_mt_full_helm_a, itm_mt_mail_tunic_a, itm_m_gauntlets_b, itm_mt_greaves_a, itm_tab_shield_heater_cav_b, itm_crusader_sword, itm_danish_greatsword, itm_heavy_lance, itm_mt_horse_c2], str_30|agi_30|int_11|cha_18|level(54),wpex(400,400,400,100,100,100),knows_athletics_10|knows_shield_10|knows_riding_10|knows_weapon_master_10|knows_power_strike_8|knows_ironflesh_8,0x000000000010014536db6db6db6ddbb600000000001db6db0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_4","Elindero the Tower","Elindero the Tower", tf_hero,0,0,fac_kingdom_1, [itm_mt_armet_b, itm_mt_heavy_plate_b, itm_m_gauntlets_b, itm_mt_greaves_a, itm_steel_shield, itm_side_sword, itm_english_bill, itm_mt_horse_c2], str_30|agi_30|int_11|cha_18|level(54),wpex(400,200,450,100,100,100),knows_athletics_10|knows_shield_10|knows_weapon_master_10|knows_power_strike_8|knows_ironflesh_8,0x0000000f3f10219436db6db6db6ddbb600000000001db6db0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_5","Sir Skolle","Sir Skolle", tf_hero,0,0,fac_kingdom_1, [itm_mt_armet_a2, itm_mt_hearldic_d2, itm_m_gauntlets_a, itm_mt_greaves_a, itm_plate_covered_round_shield, itm_longsword], str_30|agi_30|int_11|cha_18|level(54),wpex(600,200,200,100,100,100),knows_athletics_10|knows_shield_10|knows_weapon_master_10|knows_power_strike_8|knows_ironflesh_8,0x0000000fff10321336db6db6db6ddbb600000000001db6db0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_6","Xan","Xan", tf_hero,0,0,fac_kingdom_1, [itm_mh_horse_a, itm_mt_scale_gloves_b, itm_khergit_leather_boots, itm_mh_helmet_heavy_a, itm_mh_armor_heavy_a, itm_ms_hook_sword, itm_mh_bow_a, itm_barbed_arrows, itm_plate_covered_round_shield], str_30|agi_30|int_11|cha_18|level(54),wpex(450,200,200,450,100,100),knows_athletics_6|knows_shield_10|knows_weapon_master_10|knows_power_strike_8|knows_ironflesh_8|knows_riding_10,0x0000000fff08338536db6db6db6ddb6d00000000001db6db0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_7","Gylas","Gylas", tf_hero,0,0,fac_kingdom_1, [itm_m_gloves_a, itm_m_leather_boots_a, itm_m_coif_a, itm_war_bow, itm_bodkin_arrows, itm_bodkin_arrows, itm_espada_eslavona_b, itm_m_brigandine_c], str_30|agi_30|int_11|cha_18|level(54),wpex(240,200,200,500,100,100),knows_athletics_6|knows_shield_5|knows_weapon_master_10|knows_power_strike_8|knows_ironflesh_8|knows_power_draw_10,0x0000000fff08338536db6db6db6ddb6d00000000001db6db0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_8","Hamart Boley","Hamart Boley", tf_hero,0,0,fac_kingdom_1, [itm_m_gloves_a, itm_m_leather_boots_a, itm_war_bow, itm_barbed_arrows, itm_side_sword, itm_mt_special_c, itm_mt_hood_a3, itm_ms_metal_shield_a3], str_30|agi_30|int_11|cha_18|level(54),wpex(240,200,200,500,100,100),knows_athletics_10|knows_shield_5|knows_weapon_master_10|knows_power_strike_8|knows_ironflesh_8|knows_power_draw_10,0x00000006ff00219436db6db6db6dff6500000000001db6db0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_9","Eward","Eward", tf_hero,0,0,fac_kingdom_1, [itm_ms_bear_gauntlets, itm_m_leather_boots_a, itm_ms_helmet_wolf_a3, itm_ms_armor_bear, itm_ms_two_h_sword_c, itm_heavy_throwing_axes, itm_tab_shield_round_e], str_30|agi_30|int_11|cha_18|level(56),wpex(240,500,100,100,100,400),knows_athletics_10|knows_shield_5|knows_weapon_master_10|knows_power_strike_10|knows_ironflesh_10,0x0000000ff108330906db6db6db6ddb6c00000000001db6f80000000000000000, swadian_face_old_2],
  ["quick_battle_troop_10","Axlerd Githal","Axlerd Githal", tf_hero,0,0,fac_kingdom_1, [itm_ms_armor_dark_a, itm_ms_dark_boots_a, itm_ms_dark_gauntlets_a, itm_ms_strange_sword, itm_ms_doom], str_30|agi_30|int_11|cha_18|level(56),wpex(500,500,100,100,100,100),knows_athletics_10|knows_shield_5|knows_weapon_master_10|knows_power_strike_10|knows_ironflesh_10,0x0000000fff08434906076c3a1b1dffff00000000001db6380000000000000000, swadian_face_old_2],
  ["quick_battle_troop_11","Ezzenmer","Ezzenmer", tf_hero,0,0,fac_kingdom_1, [itm_ms_flamberg_great, itm_ms_helmet_heretic, itm_ms_armor_heretic, itm_ms_demonic_boots_a, itm_ms_demonic_gauntlets_a], str_30|agi_30|int_11|cha_18|level(69),wpex(0,900,0,0,0,0),knows_athletics_10|knows_weapon_master_10|knows_power_strike_10|knows_ironflesh_10,0x0000000fff08738006056c3a1b1dffff00000000001db6380000000000000000, swadian_face_old_2],
  ["quick_battle_troop_12","Bronze Ganaka","Bronze Ganaka", tf_hero,0,0,fac_kingdom_1, [itm_battle_fork, itm_m_leather_boots_a, itm_m_gloves_a, itm_ms_armor_plate_b, itm_ms_helmet_golem], str_30|agi_30|int_11|cha_18|level(54),wpex(0,0,900,0,0,0),knows_athletics_10|knows_weapon_master_10|knows_power_strike_10|knows_ironflesh_10,0x0000000e7f08244036db6db6db6edd6d00000000001db6f30000000000000000, swadian_face_old_2],

  ["quick_battle_troops_end","{!}quick_battle_troops_end","{!}quick_battle_troops_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],

  ["tutorial_fighter_1","Novice Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_linen_tunic,itm_nomad_boots],
   def_attrib|level(1),wp_melee(10),knows_athletics_1|knows_ironflesh_2|knows_shield_2,0x000000088c1073144252b1929a85569300000000000496a50000000000000000, vaegir_face_older_2],
  ["tutorial_fighter_2","Novice Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_green_tunic,itm_nomad_boots],
   def_attrib|level(1),wp_melee(10),knows_athletics_1|knows_ironflesh_2|knows_shield_2,0x000000088b08049056ab56566135c46500000000001dda1b0000000000000000, vaegir_face_older_2],
  ["tutorial_fighter_3","Regular Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_green_tunic,itm_nomad_boots],
   def_attrib|level(9),wp_melee(50),knows_athletics_1|knows_ironflesh_2|knows_shield_2,0x00000008bc00400654914a3b0d0de74d00000000001d584e0000000000000000, vaegir_face_older_2],
  ["tutorial_fighter_4","Veteran Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_linen_tunic,itm_nomad_boots],
   def_attrib|level(16),wp_melee(110),knows_athletics_1|knows_ironflesh_3|knows_power_strike_2|knows_shield_2,0x000000089910324a495175324949671800000000001cd8ab0000000000000000, vaegir_face_older_2],
  ["tutorial_archer_1","Archer","Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_2,
   [itm_leather_jerkin,itm_leather_vest,itm_nomad_boots,itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet,itm_vaegir_fur_cap,itm_nomad_cap],
   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_athletics_2|knows_power_throw_1,vaegir_face_young_1, vaegir_face_older_2],
  ["tutorial_master_archer","Archery Trainer","Archery Trainer",tf_hero,0,0,fac_kingdom_2,
   [itm_linen_tunic,itm_nomad_boots],
   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_athletics_2|knows_power_throw_1,0x0000000ea508540642f34d461d2d54a300000000001d5d9a0000000000000000, vaegir_face_older_2],
  ["tutorial_rider_1","Rider","{!}Vaegir Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_green_tunic,itm_hunter, itm_saddle_horse,itm_leather_gloves],
   def_attrib|level(24),wp(130),knows_riding_4|knows_shield_2|knows_ironflesh_3|knows_power_strike_2,vaegir_face_middle_1, vaegir_face_older_2],
  ["tutorial_rider_2","Horse archer","{!}Khergit Horse Archers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac_kingdom_3,
   [itm_tribal_warrior_outfit,itm_nomad_robe,itm_hide_boots,itm_tab_shield_small_round_a,itm_steppe_horse],
   def_attrib|level(14),wp(80)|wp_archery(110),knows_riding_5|knows_power_draw_3|knows_ironflesh_1|knows_horse_archery_4|knows_power_throw_1,khergit_face_young_1, khergit_face_older_2],
  ["tutorial_master_horseman","Riding Trainer","Riding Trainer",tf_hero,0,0,fac_kingdom_2,
   [itm_leather_vest,itm_nomad_boots],
   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_athletics_2|knows_power_throw_1,0x0000000ea0084140478a692894ba185500000000001d4af30000000000000000, vaegir_face_older_2],
   
  ["swadian_merchant", "Merchant of Praven", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_4, [itm_sword_two_handed_a, itm_courtly_outfit, itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["vaegir_merchant", "Merchant of Reyvadin", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_5, [itm_sword_two_handed_a, itm_nobleman_outfit, itm_woolen_hose], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["khergit_merchant", "Merchant of Tulga", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_1, [itm_sword_two_handed_a, itm_red_gambeson, itm_nomad_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["nord_merchant", "Merchant of Sargoth", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_2, [itm_sword_two_handed_a, itm_red_gambeson, itm_nomad_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["rhodok_merchant", "Merchant of Jelkala", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_3, [itm_sword_two_handed_a, itm_leather_jerkin, itm_blue_hose], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["sarranid_merchant", "Merchant of Shariz", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_6, [itm_sword_two_handed_a, itm_sarranid_cloth_robe, itm_sarranid_boots_a], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],       
  ["startup_merchants_end","startup_merchants_end","startup_merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],
 
  ["sea_raider_leader","Sea Raider Captain","Sea Raider Captains",tf_hero|tf_guarantee_all_wo_ranged,0,0,fac_outlaws,
   [itm_arrows,itm_sword_viking_1,itm_sword_viking_2,itm_fighting_axe,itm_battle_axe,itm_spear,itm_nordic_shield,itm_nordic_shield,itm_nordic_shield,itm_wooden_shield,itm_long_bow,itm_javelin,itm_throwing_axes,
    itm_nordic_helmet,itm_nordic_helmet,itm_nasal_helmet,itm_mail_shirt,itm_byrnie,itm_mail_hauberk,itm_leather_boots, itm_nomad_boots],
   def_attrib|level(24),wp(110),knows_ironflesh_2|knows_power_strike_2|knows_power_draw_3|knows_power_throw_2|knows_riding_1|knows_athletics_2,nord_face_young_1, nord_face_old_2],

  ["looter_leader","Robber","Looters",tf_hero,0,0,fac_outlaws,
   [itm_hatchet,itm_club,itm_butchering_knife,itm_falchion,itm_rawhide_coat,itm_stones,itm_nomad_armor,itm_nomad_armor,itm_woolen_cap,itm_woolen_cap,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(4),wp(20),knows_common,0x00000001b80032473ac49738206626b200000000001da7660000000000000000, bandit_face2],
   
  ["bandit_leaders_end","bandit_leaders_end","bandit_leaders_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],   
  
  ["relative_of_merchant", "Merchant's Brother", "{!}Prominent",tf_hero,0,0,fac_kingdom_2,
   [itm_linen_tunic,itm_nomad_boots],
   def_attrib|level(1),wp_melee(10),knows_athletics_1|knows_ironflesh_2|knows_shield_2, 0x00000000320410022d2595495491afa400000000001d9ae30000000000000000, mercenary_face_2],   
   
  ["relative_of_merchants_end","relative_of_merchants_end","relative_of_merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],     

  ["silver_rose_trained_crossbowman_multiplayer_coop_tier_1","Swadian Crossbowman","Swadian Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_hunting_crossbow,itm_bolts,itm_fighting_pick,itm_tab_shield_heater_a,itm_arming_cap,itm_padded_cloth,itm_ankle_boots],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["silver_rose_infantry_multiplayer_coop_tier_1","Swadian Infantry","Swadian Infantry",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_spiked_club,itm_tab_shield_heater_b,itm_felt_hat,itm_leather_apron,itm_wrapping_boots],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["silver_rose_man_at_arms_multiplayer_coop_tier_1","Swadian Man at Arms","Swadian Men at Arms",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_light_lance,itm_sword_medieval_b_small,itm_tab_shield_heater_a,itm_leather_cap,itm_leather_gloves,itm_padded_cloth,itm_wrapping_boots,itm_warhorse],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["vaegir_archer_multiplayer_coop_tier_1","Vaegir Archer","Vaegir Archers",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_arrows,itm_axe,itm_hunting_bow,itm_linen_tunic,itm_nomad_boots],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["vaegir_spearman_multiplayer_coop_tier_1","Vaegir Spearman","Vaegir spearman",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_tab_shield_kite_a, itm_axe,itm_rawhide_coat,itm_hide_boots],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["vaegir_horseman_multiplayer_coop_tier_1","Vaegir Horseman","Vaegir Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_spear,itm_tab_shield_kite_cav_a,itm_linen_tunic,itm_hide_boots,itm_hunter],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["khergit_veteran_horse_archer_multiplayer_coop_tier_1","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_khergit_1,itm_nomad_bow,itm_arrows,itm_steppe_armor,itm_hide_boots,itm_steppe_horse],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["khergit_infantry_multiplayer_coop_tier_1","Khergit Infantry","Khergit Infantries",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_khergit_1,itm_tab_shield_small_round_a,itm_steppe_armor,itm_hide_boots,itm_leather_gloves],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["khergit_lancer_multiplayer_coop_tier_1","Khergit Lancer","Khergit Lancers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_spear,itm_tab_shield_small_round_a,itm_steppe_armor,itm_steppe_cap,itm_hide_boots,itm_leather_gloves,itm_courser],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["nord_archer_multiplayer_coop_tier_1","Nord Archer","Nord Archers",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_arrows,itm_sword_viking_2_small,itm_short_bow,itm_blue_tunic,itm_leather_boots],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["nord_veteran_multiplayer_coop_tier_1","Nord Huscarl","Nord Huscarls",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_sword_viking_1,itm_one_handed_war_axe_a,itm_tab_shield_round_a,itm_blue_tunic,itm_leather_boots],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["nord_scout_multiplayer_coop_tier_1","Nord Scout","Nord Scouts",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_javelin,itm_war_spear,itm_tab_shield_small_round_a,itm_blue_tunic,itm_leather_boots,itm_saddle_horse],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["rhodok_veteran_crossbowman_multiplayer_coop_tier_1","Rhodok Crossbowman","Rhodok Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_crossbow,itm_bolts,itm_fighting_pick,itm_tab_shield_pavise_a,itm_tunic_with_green_cape,itm_ankle_boots],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["rhodok_sergeant_multiplayer_coop_tier_1","Rhodok Sergeant","Rhodok Sergeants",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_military_cleaver_b,itm_tab_shield_pavise_a,itm_darts,itm_green_tunic,itm_ankle_boots,itm_leather_cap],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["rhodok_horseman_multiplayer_coop_tier_1","Rhodok Horseman","Rhodok Horsemen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_tab_shield_heater_cav_a, itm_light_lance, itm_green_tunic,itm_ankle_boots,itm_padded_coif,itm_saddle_horse],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["sarranid_archer_multiplayer_coop_tier_1","Sarranid Archer","Sarranid Archers",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_arrows,itm_sarranid_mace_1,itm_short_bow,itm_sarranid_cloth_robe, itm_sarranid_boots_b],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["sarranid_footman_multiplayer_coop_tier_1","Sarranid Footman","Sarranid footman",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_tab_shield_kite_a, itm_sarranid_axe_a,itm_sarranid_cloth_robe, itm_sarranid_boots_b],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["sarranid_mamluke_multiplayer_coop_tier_1","Sarranid Mamluke","Sarranid Mamluke",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_lance,itm_tab_shield_small_round_a,itm_sarranid_cloth_robe, itm_sarranid_boots_b,itm_arabian_horse_a],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],

  ["silver_rose_trained_crossbowman_multiplayer_coop_tier_2","Swadian Crossbowman","Swadian Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_spiked_club,itm_crossbow,itm_bolts,itm_tab_shield_heater_b,itm_arming_cap,itm_red_gambeson,itm_ankle_boots],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["silver_rose_infantry_multiplayer_coop_tier_2","Swadian Infantry","Swadian Infantry",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_sword_medieval_b,itm_tab_shield_heater_c,itm_spear,itm_mail_coif,itm_leather_gloves,itm_mail_with_tunic_red,itm_ankle_boots],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["silver_rose_man_at_arms_multiplayer_coop_tier_2","Swadian Man at Arms","Swadian Men at Arms",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_lance,itm_sword_medieval_a,itm_tab_shield_heater_b,itm_helmet_with_neckguard,itm_leather_gloves,itm_haubergeon,itm_leather_boots,itm_warhorse],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["vaegir_archer_multiplayer_coop_tier_2","Vaegir Archer","Vaegir Archers",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_barbed_arrows,itm_axe,itm_nomad_bow,itm_leather_vest,itm_nomad_boots,itm_vaegir_fur_helmet],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["vaegir_spearman_multiplayer_coop_tier_2","Vaegir Spearman","Vaegir spearman",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_javelin,itm_scimitar,itm_tab_shield_kite_b,itm_leather_jerkin,itm_nomad_boots,itm_vaegir_lamellar_helmet,itm_leather_gloves],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["vaegir_horseman_multiplayer_coop_tier_2","Vaegir Horseman","Vaegir Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_war_spear,itm_tab_shield_kite_cav_b,itm_javelin,itm_studded_leather_coat,itm_leather_gloves,itm_nomad_boots,itm_vaegir_lamellar_helmet,itm_hunter],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["khergit_veteran_horse_archer_multiplayer_coop_tier_2","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_khergit_2,itm_khergit_bow,itm_barbed_arrows,itm_steppe_armor,itm_leather_steppe_cap_a,itm_nomad_boots,itm_steppe_horse],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["khergit_infantry_multiplayer_coop_tier_2","Khergit Infantry","Khergit Infantries",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_khergit_2,itm_tab_shield_small_round_b,itm_javelin,itm_tribal_warrior_outfit,itm_nomad_boots,itm_leather_gloves],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["khergit_lancer_multiplayer_coop_tier_2","Khergit Lancer","Khergit Lancers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_war_spear,itm_tab_shield_small_round_b,itm_javelin,itm_tribal_warrior_outfit,itm_leather_steppe_cap_b,itm_nomad_boots,itm_courser],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["nord_archer_multiplayer_coop_tier_2","Nord Archer","Nord Archers",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_arrows,itm_sword_viking_2,itm_long_bow,itm_leather_jerkin,itm_leather_boots,itm_nordic_archer_helmet],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["nord_veteran_multiplayer_coop_tier_2","Nord Huscarl","Nord Huscarls",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_one_handed_war_axe_a,itm_tab_shield_round_b,itm_throwing_axes,itm_leather_jerkin,itm_leather_boots,itm_nordic_footman_helmet,itm_leather_gloves],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["nord_scout_multiplayer_coop_tier_2","Nord Scout","Nord Scouts",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_javelin,itm_lance,itm_tab_shield_small_round_a,itm_leather_jerkin,itm_leather_boots,itm_leather_gloves,itm_nordic_footman_helmet,itm_saddle_horse],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["rhodok_veteran_crossbowman_multiplayer_coop_tier_2","Rhodok Crossbowman","Rhodok Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_heavy_crossbow,itm_bolts,itm_club_with_spike_head,itm_tab_shield_pavise_b,itm_leather_armor,itm_leather_boots,itm_leather_gloves,itm_leather_cap],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["rhodok_sergeant_multiplayer_coop_tier_2","Rhodok Sergeant","Rhodok Sergeants",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_military_cleaver_b,itm_tab_shield_pavise_b,itm_war_darts,itm_padded_cloth,itm_leather_boots,itm_leather_gloves,itm_footman_helmet],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["rhodok_horseman_multiplayer_coop_tier_2","Rhodok Horseman","Rhodok Horsemen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_tab_shield_heater_cav_b, itm_heavy_lance,itm_javelin,itm_padded_cloth,itm_leather_boots,itm_leather_gloves,itm_footman_helmet,itm_saddle_horse],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["sarranid_archer_multiplayer_coop_tier_2","Sarranid Archer","Sarranid Archers",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_barbed_arrows,itm_sarranid_mace_1,itm_nomad_bow,itm_archers_vest,itm_desert_turban,itm_leather_gloves,itm_sarranid_boots_b],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["sarranid_footman_multiplayer_coop_tier_2","Sarranid Footman","Sarranid footman",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_tab_shield_kite_b, itm_sarranid_axe_b,itm_javelin,itm_archers_vest,itm_sarranid_warrior_cap,itm_leather_gloves,itm_sarranid_boots_b],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["sarranid_mamluke_multiplayer_coop_tier_2","Sarranid Mamluke","Sarranid Mamluke",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_heavy_lance,itm_tab_shield_small_round_b,itm_javelin,itm_archers_vest, itm_sarranid_warrior_cap,itm_leather_gloves,itm_sarranid_boots_b,itm_arabian_horse_a],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],

  ["silver_rose_trained_crossbowman_multiplayer_coop_tier_3","Swadian Crossbowman","Swadian Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_sword_medieval_b,itm_heavy_crossbow,itm_steel_bolts,itm_tab_shield_heater_c,itm_segmented_helmet,itm_leather_jerkin,itm_leather_boots],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["silver_rose_infantry_multiplayer_coop_tier_3","Swadian Infantry","Swadian Infantry",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_bastard_sword_a,itm_awlpike,itm_tab_shield_heater_c,itm_bascinet,itm_mail_mittens,itm_mail_with_surcoat,itm_mail_chausses],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["silver_rose_man_at_arms_multiplayer_coop_tier_3","Swadian Man at Arms","Swadian Men at Arms",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_heavy_lance,itm_bastard_sword_b,itm_tab_shield_heater_cav_a,itm_flat_topped_helmet,itm_mail_mittens,itm_mail_with_surcoat,itm_mail_chausses,itm_warhorse],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["vaegir_archer_multiplayer_coop_tier_3","Vaegir Archer","Vaegir Archers",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_barbed_arrows,itm_scimitar_b,itm_strong_bow,itm_leather_jerkin,itm_splinted_leather_greaves,itm_vaegir_spiked_helmet,itm_leather_gloves],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["vaegir_spearman_multiplayer_coop_tier_3","Vaegir Spearman","Vaegir spearman",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_scimitar_b, itm_tab_shield_kite_b,itm_javelin,itm_lamellar_armor,itm_splinted_leather_greaves,itm_vaegir_lamellar_helmet,itm_leather_gloves],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["vaegir_horseman_multiplayer_coop_tier_3","Vaegir Horseman","Vaegir Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_heavy_lance,itm_tab_shield_kite_cav_b, itm_javelin,itm_lamellar_armor,itm_splinted_leather_greaves,itm_vaegir_lamellar_helmet,itm_hunter,itm_mail_mittens],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["khergit_veteran_horse_archer_multiplayer_coop_tier_3","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_khergit_3,itm_strong_bow,itm_khergit_arrows,itm_tribal_warrior_outfit,itm_leather_steppe_cap_c,itm_khergit_leather_boots,itm_steppe_horse],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["khergit_infantry_multiplayer_coop_tier_3","Khergit Infantry","Khergit Infantries",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_hafted_blade_a,itm_javelin,itm_leather_steppe_cap_c,itm_lamellar_armor,itm_splinted_leather_greaves,itm_mail_mittens],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["khergit_lancer_multiplayer_coop_tier_3","Khergit Lancer","Khergit Lancers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_heavy_lance,itm_tab_shield_small_round_a,itm_lamellar_armor,itm_leather_steppe_cap_c,itm_splinted_leather_greaves,itm_courser],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["nord_archer_multiplayer_coop_tier_3","Nord Archer","Nord Archers",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_barbed_arrows,itm_sword_viking_3,itm_long_bow,itm_leather_jerkin,itm_leather_boots,itm_nordic_veteran_archer_helmet,itm_leather_gloves],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["nord_veteran_multiplayer_coop_tier_3","Nord Huscarl","Nord Huscarls",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_one_handed_war_axe_b,itm_tab_shield_round_d,itm_heavy_throwing_axes,itm_mail_shirt,itm_splinted_leather_greaves,itm_nordic_huscarl_helmet],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["nord_scout_multiplayer_coop_tier_3","Nord Scout","Nord Scouts",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_throwing_spears,itm_heavy_lance,itm_tab_shield_small_round_b,itm_mail_shirt,itm_splinted_leather_greaves,itm_nordic_fighter_helmet,itm_saddle_horse],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["rhodok_veteran_crossbowman_multiplayer_coop_tier_3","Rhodok Crossbowman","Rhodok Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_sniper_crossbow,itm_steel_bolts,itm_military_cleaver_c,itm_tab_shield_pavise_c,itm_padded_cloth,itm_leather_boots,itm_footman_helmet,itm_leather_gloves],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["rhodok_sergeant_multiplayer_coop_tier_3","Rhodok Sergeant","Rhodok Sergeants",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_tab_shield_pavise_c,itm_military_cleaver_c,itm_javelin,itm_ragged_outfit,itm_splinted_greaves,itm_kettle_hat,itm_mail_mittens],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["rhodok_horseman_multiplayer_coop_tier_3","Rhodok Horseman","Rhodok Horsemen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_javelin,itm_tab_shield_heater_cav_b, itm_heavy_lance, itm_ragged_outfit,itm_splinted_greaves,itm_bascinet_2,itm_mail_mittens,itm_saddle_horse],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["sarranid_archer_multiplayer_coop_tier_3","Sarranid Archer","Sarranid Archers",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_khergit_arrows,itm_sarranid_mace_1,itm_nomad_bow,itm_archers_vest,itm_sarranid_mail_coif,itm_leather_gloves,itm_sarranid_boots_c],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["sarranid_footman_multiplayer_coop_tier_3","Sarranid Footman","Sarranid footman",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_jarid, itm_tab_shield_kite_c, itm_sarranid_axe_b,itm_sarranid_mail_shirt,itm_sarranid_mail_coif,itm_mail_mittens,itm_sarranid_boots_c],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["sarranid_mamluke_multiplayer_coop_tier_3","Sarranid Mamluke","Sarranid Mamluke",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_heavy_lance,itm_tab_shield_small_round_b,itm_jarid,itm_sarranid_cavalry_robe,itm_sarranid_horseman_helmet,itm_mail_mittens,itm_sarranid_boots_c,itm_arabian_horse_a],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],

  ["silver_rose_trained_crossbowman_multiplayer_coop_tier_4","Swadian Crossbowman","Swadian Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_sword_medieval_b,itm_sniper_crossbow,itm_steel_bolts,itm_tab_shield_heater_c,itm_helmet_with_neckguard,itm_leather_gloves,itm_haubergeon,itm_mail_chausses],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["silver_rose_infantry_multiplayer_coop_tier_4","Swadian Infantry","Swadian Infantry",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_bastard_sword_b,itm_awlpike_long,itm_tab_shield_heater_d,itm_guard_helmet,itm_gauntlets,itm_coat_of_plates,itm_iron_greaves],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["silver_rose_man_at_arms_multiplayer_coop_tier_4","Swadian Man at Arms","Swadian Men at Arms",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_great_lance,itm_morningstar,itm_tab_shield_heater_cav_b,itm_great_helmet,itm_gauntlets,itm_coat_of_plates_red,itm_plate_boots,itm_warhorse],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["vaegir_archer_multiplayer_coop_tier_4","Vaegir Archer","Vaegir Archers",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_barbed_arrows,itm_bardiche,itm_war_bow,itm_lamellar_vest,itm_splinted_leather_greaves,itm_vaegir_lamellar_helmet,itm_leather_gloves],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["vaegir_spearman_multiplayer_coop_tier_4","Vaegir Spearman","Vaegir spearman",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_bardiche,itm_javelin,itm_vaegir_elite_armor,itm_splinted_greaves,itm_vaegir_war_helmet,itm_mail_mittens],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["vaegir_horseman_multiplayer_coop_tier_4","Vaegir Horseman","Vaegir Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_heavy_lance,itm_tab_shield_kite_cav_b,itm_javelin,itm_vaegir_elite_armor,itm_splinted_greaves,itm_hunter,itm_vaegir_war_helmet,itm_scale_gauntlets],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["khergit_veteran_horse_archer_multiplayer_coop_tier_4","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_hafted_blade_b,itm_strong_bow,itm_khergit_arrows,itm_lamellar_vest_khergit,itm_khergit_guard_helmet,itm_splinted_leather_greaves,itm_steppe_horse],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["khergit_infantry_multiplayer_coop_tier_4","Khergit Infantry","Khergit Infantries",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_hafted_blade_b,itm_tab_shield_small_round_a,itm_jarid,itm_khergit_elite_armor,itm_khergit_guard_boots,itm_khergit_war_helmet,itm_lamellar_gauntlets],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["khergit_lancer_multiplayer_coop_tier_4","Khergit Lancer","Khergit Lancers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_great_lance,itm_tab_shield_small_round_c,itm_khergit_elite_armor,itm_khergit_war_helmet,itm_khergit_guard_boots,itm_lamellar_gauntlets,itm_courser],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["nord_archer_multiplayer_coop_tier_4","Nord Archer","Nord Archers",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_khergit_arrows,itm_sword_viking_3,itm_long_bow,itm_byrnie,itm_splinted_leather_greaves,itm_nordic_footman_helmet,itm_leather_gloves],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["nord_veteran_multiplayer_coop_tier_4","Nord Huscarl","Nord Huscarls",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_great_axe,itm_tab_shield_round_e,itm_heavy_throwing_axes,itm_banded_armor,itm_mail_boots,itm_nordic_warlord_helmet],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["nord_scout_multiplayer_coop_tier_4","Nord Scout","Nord Scouts",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_throwing_spears,itm_great_lance,itm_tab_shield_small_round_c,itm_mail_hauberk,itm_splinted_leather_greaves,itm_nordic_huscarl_helmet,itm_saddle_horse],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["rhodok_veteran_crossbowman_multiplayer_coop_tier_4","Rhodok Crossbowman","Rhodok Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_sniper_crossbow,itm_steel_bolts,itm_sledgehammer,itm_tab_shield_pavise_d,itm_mail_with_tunic_green,itm_kettle_hat,itm_splinted_greaves,itm_leather_gloves],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["rhodok_sergeant_multiplayer_coop_tier_4","Rhodok Sergeant","Rhodok Sergeants",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_two_handed_cleaver,itm_tab_shield_pavise_d,itm_javelin,itm_surcoat_over_mail,itm_iron_greaves,itm_gauntlets,itm_full_helm,],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["rhodok_horseman_multiplayer_coop_tier_4","Rhodok Horseman","Rhodok Horsemen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_javelin,itm_tab_shield_heater_cav_b, itm_great_lance, itm_surcoat_over_mail,itm_iron_greaves,itm_gauntlets,itm_full_helm,itm_saddle_horse],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["sarranid_archer_multiplayer_coop_tier_4","Sarranid Archer","Sarranid Archers",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_khergit_arrows,itm_sarranid_two_handed_mace_1,itm_strong_bow,itm_sarranid_mail_shirt,itm_sarranid_mail_coif,itm_leather_gloves,itm_sarranid_boots_d],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["sarranid_footman_multiplayer_coop_tier_4","Sarranid Footman","Sarranid footman",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_bamboo_spear, itm_tab_shield_kite_c, itm_arabian_sword_a,itm_sarranid_elite_armor,itm_sarranid_veiled_helmet,itm_scale_gauntlets, itm_sarranid_boots_d],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["sarranid_mamluke_multiplayer_coop_tier_4","Sarranid Mamluke","Sarranid Mamluke",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_arabian_sword_a,itm_lance,itm_tab_shield_small_round_c,itm_mamluke_mail,itm_sarranid_veiled_helmet,itm_scale_gauntlets, itm_sarranid_boots_d,itm_arabian_horse_a],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],

   ["coop_faction_troop_templates_end","{!}multiplayer_end","{!}multiplayer_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],
   #tier 1
  ["npc1_1","Borcha","Borcha",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_khergit_armor,itm_nomad_boots,itm_knife, itm_courser],
   str_16|agi_17|int_6|cha_30|level(25),wpex(250,80,140,160,90,250),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_ironflesh_1|knows_power_strike_7|knows_pathfinding_3|knows_athletics_5|knows_tracking_1|knows_riding_6|knows_power_throw_7|knows_power_draw_5, #skills 2/3 player at that level
   0x00000004bf086143259d061a9046e23500000000001db52c0000000000000000],
  ["npc2_1","Marnid","Marnid", tf_hero|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,[itm_linen_tunic,itm_hide_boots,itm_club, itm_saddle_horse],
   str_14|agi_17|int_6|cha_30|level(25),wpex(240,130,170,150,170,90),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_trade_2|knows_weapon_master_1|knows_ironflesh_1|knows_wound_treatment_1|knows_athletics_5|knows_first_aid_1|knows_leadership_1|knows_riding_4|knows_power_strike_7|knows_power_draw_3|knows_power_throw_3,
   0x000000019d004001570b893712c8d28d00000000001dc8990000000000000000],
  ["npc3_1","Ymira","Ymira",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_dress,itm_woolen_hose,itm_knife, itm_hunter],
   str_24|agi_13|int_6|cha_30|level(25),wpex(190,80,240,180,180,80),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_wound_treatment_1|knows_trade_1|knows_first_aid_3|knows_surgery_1|knows_athletics_6|knows_riding_8|knows_power_strike_5|knows_power_draw_3|knows_power_throw_3,
   0x0000000083040001583b6db8dec5925b00000000001d80980000000000000000],
  ["npc4_1","Rolf","Rolf",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_leather_jerkin,itm_nomad_boots, itm_sword_medieval_a, itm_hunter],
   str_20|agi_13|int_6|cha_30|level(25),wpex(210,230,200,90,100,95),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_weapon_master_2|knows_power_strike_9|knows_riding_8|knows_athletics_7|knows_power_throw_3|knows_first_aid_1|knows_surgery_1|knows_tactics_2|knows_leadership_2|knows_power_draw_2,
   0x000000057f1074002c75c6a8a58ad72e00000000001e1a890000000000000000],
  ["npc5_1","Baheshtur","Baheshtur",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_nomad_vest,itm_nomad_boots, itm_sword_khergit_1, itm_steppe_horse],
   str_18|agi_13|int_6|cha_30|level(25),wpex(160,80,130,250,50,230),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_riding_7|knows_horse_archery_9|knows_power_draw_8|knows_leadership_2|knows_weapon_master_1|knows_power_strike_5|knows_power_throw_8|knows_athletics_5,
   0x000000088910318b5c6f972328324a6200000000001cd3310000000000000000],
  ["npc6_1","Firentis","Firentis",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_tabard,itm_nomad_boots, itm_sword_medieval_a, itm_sumpter_horse],
   str_20|agi_19|int_6|cha_30|level(25),wpex(240,210,180,90,100,80),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_riding_7|knows_weapon_master_2|knows_athletics_8|knows_trainer_1|knows_leadership_1|knows_power_strike_7|knows_power_draw_2|knows_power_throw_3,
  0x00000002050052036a1895d0748f3ca30000000000000f0b0000000000000000],
  ["npc7_1","Deshavi","Deshavi",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_ragged_outfit,itm_wrapping_boots, itm_hunting_bow, itm_arrows, itm_quarter_staff, itm_arabian_horse_b],
   str_16|agi_13|int_6|cha_30|level(25),wpex(90,80,230,280,110,130),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_tracking_2|knows_athletics_8|knows_spotting_1|knows_pathfinding_1|knows_power_draw_10|knows_riding_4|knows_power_strike_6|knows_power_throw_5,
   0x00000001fc08400533a15297634d44f400000000001e02db0000000000000000],
  ["npc8_1","Matheld","Matheld",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_tribal_warrior_outfit,itm_nomad_boots, itm_sword_viking_1, itm_courser],
   str_18|agi_15|int_6|cha_30|level(25),wpex(190,250,80,120,80,250),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_weapon_master_3|knows_athletics_10|knows_leadership_3|knows_tactics_1|knows_riding_4|knows_power_strike_10|knows_power_draw_2|knows_power_throw_8,
   0x00000005800c000637db8314e331e76e00000000001c46db0000000000000000],
  ["npc9_1","Alayen","Alayen",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_tabard,itm_nomad_boots, itm_sword_medieval_b_small, itm_courser],
   str_22|agi_19|int_6|cha_30|level(25),wpex(80,230,130,220,70,160),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_weapon_master_1|knows_riding_4|knows_athletics_6|knows_leadership_1|knows_tactics_1|knows_power_strike_4|knows_power_draw_7|knows_power_throw_5,
   0x000000030100300f499d5b391b6db8d300000000001dc2e10000000000000000],
  ["npc10_1","Bunduk","Bunduk",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_padded_leather,itm_nomad_boots, itm_crossbow, itm_bolts, itm_pickaxe, itm_saddle_horse],
   str_24|agi_19|int_6|cha_30|level(25),wpex(170,80,80,160,290,150),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_weapon_master_3|knows_tactics_1|knows_leadership_1|knows_ironflesh_3|knows_trainer_2|knows_first_aid_2|knows_riding_4|knows_power_strike_5|knows_power_draw_5|knows_power_throw_5|knows_athletics_7,
   0x0000000a3f081006572c91c71c8d46cb00000000001e468a0000000000000000],
  ["npc11_1","Katrin","Katrin",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_leather_apron, itm_falchion, itm_wrapping_boots, itm_sumpter_horse],
   str_16|agi_17|int_6|cha_30|level(25),wpex(140,230,130,80,210,170),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_weapon_master_1|knows_first_aid_1|knows_wound_treatment_2|knows_ironflesh_3|knows_inventory_management_5|knows_riding_4|knows_power_strike_5|knows_power_draw_2|knows_power_throw_7|knows_athletics_5,
   0x0000000d7f0400035915aa226b4d975200000000001ea49e0000000000000000],
  ["npc12_1","Jeremus","Jeremus",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_pilgrim_disguise,itm_nomad_boots, itm_staff, itm_sumpter_horse],
   str_16|agi_17|int_6|cha_30|level(25),wpex(120,110,290,80,110,120),   knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_ironflesh_1|knows_power_strike_7|knows_surgery_4|knows_wound_treatment_3|knows_first_aid_3|knows_riding_4|knows_power_draw_2|knows_power_throw_3|knows_athletics_7,
   0x000000078000500e4f8ba62a9cd5d36d00000000001e36250000000000000000],
  ["npc13_1","Nizar","Nizar",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_nomad_robe,itm_nomad_boots, itm_scimitar, itm_courser],
   str_14|agi_17|int_6|cha_30|level(25),wpex(250,80,140,210,110,140),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_riding_9|knows_leadership_2|knows_athletics_5|knows_ironflesh_2|knows_power_strike_6|knows_weapon_master_1|knows_power_draw_7|knows_power_throw_4,
   0x00000004bf0475c85f4e9592de4e574c00000000001e369c0000000000000000],
  ["npc14_1","Lezalit","Lezalit",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_nobleman_outfit,itm_nomad_boots, itm_sword_medieval_b_small, itm_courser],
   str_18|agi_19|int_6|cha_30|level(25),wpex(280,170,170,170,170,180),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_trainer_4|knows_weapon_master_3|knows_leadership_2|knows_power_strike_1|knows_riding_7|knows_power_strike_7|knows_power_draw_6|knows_power_throw_6|knows_athletics_8,
   0x00000001a410259144d5d1d6eb55e96a00000000001db0db0000000000000000],
  ["npc15_1","Artimenner","Artimenner",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_rich_outfit,itm_nomad_boots, itm_sword_medieval_b_small, itm_hunter],
   str_18|agi_13|int_6|cha_30|level(25),wpex(190,290,130,210,90,90),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_tactics_2|knows_engineer_4|knows_trade_3|knows_tracking_1|knows_spotting_1|knows_riding_6|knows_power_strike_7|knows_power_draw_7|knows_power_throw_3|knows_athletics_5,
   0x0000000f2e1021862b4b9123594eab5300000000001d55360000000000000000],
  ["npc16_1","Klethi","Klethi",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_peasant_dress,itm_nomad_boots, itm_dagger, itm_throwing_knives, itm_saddle_horse],
   str_14|agi_17|int_6|cha_30|level(25),wpex(260,10,100,160,30,300),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_power_throw_10|knows_athletics_10|knows_power_strike_8|knows_riding_4|knows_power_draw_5,
   0x00000000000c100739ce9c805d2f381300000000001cc7ad0000000000000000],
   
    #tier 2
  ["npc1_2","Borcha","Borcha",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_leather_steppe_cap_c,itm_leather_gloves,itm_nomad_robe,itm_hide_boots,itm_sword_medieval_b_small, itm_courser],
   str_16|agi_17|int_12|cha_7|level(14),wp(60),knows_tracker_npc|
   knows_ironflesh_1|knows_power_strike_1|knows_pathfinding_3|knows_athletics_2|knows_tracking_1|knows_riding_2, #skills 2/3 player at that level
   0x00000004bf086143259d061a9046e23500000000001db52c0000000000000000],
  ["npc2_2","Marnid","Marnid", tf_hero|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,[itm_nasal_helmet,itm_padded_leather,itm_leather_boots,itm_mace_2,itm_tab_shield_small_round_a, itm_saddle_horse],
   str_14|agi_17|int_11|cha_6|level(14),wp(40),knows_merchant_npc|
   knows_trade_2|knows_weapon_master_1|knows_ironflesh_1|knows_wound_treatment_1|knows_athletics_2|knows_first_aid_1|knows_leadership_1,
   0x000000019d004001570b893712c8d28d00000000001dc8990000000000000000],
  ["npc3_2","Ymira","Ymira",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_head_wrappings,itm_leather_jerkin,itm_wrapping_boots,itm_sword_medieval_b_small, itm_hunter],
   str_24|agi_13|int_11|cha_6|level(14),wp(20),knows_merchant_npc|
   knows_wound_treatment_1|knows_trade_1|knows_first_aid_3|knows_surgery_1|knows_athletics_1|knows_riding_1,
   0x0000000083040001583b6db8dec5925b00000000001d80980000000000000000],
  ["npc4_2","Rolf","Rolf",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_kettle_hat,itm_leather_gloves,itm_studded_leather_coat,itm_leather_boots,itm_sword_medieval_c,itm_tab_shield_heater_c, itm_hunter],
   str_20|agi_13|int_13|cha_10|level(27),wp(110),knows_warrior_npc|
   knows_weapon_master_2|knows_power_strike_2|knows_riding_2|knows_athletics_2|knows_power_throw_2|knows_first_aid_1|knows_surgery_1|knows_tactics_2|knows_leadership_2,
   0x000000057f1074002c75c6a8a58ad72e00000000001e1a890000000000000000],
  ["npc5_2","Baheshtur","Baheshtur",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sword_khergit_2, itm_tab_shield_small_round_b, itm_leather_steppe_cap_b, itm_tribal_warrior_outfit, itm_khergit_leather_boots, itm_steppe_horse],
   str_18|agi_13|int_12|cha_7|level(23),wp(90),knows_warrior_npc|
   knows_riding_2|knows_horse_archery_3|knows_power_draw_3|knows_leadership_2|knows_weapon_master_1,
   0x000000088910318b5c6f972328324a6200000000001cd3310000000000000000],
  ["npc6_2","Firentis","Firentis",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_bastard_sword_a, itm_mail_coif, itm_mail_with_tunic_red, itm_ankle_boots, itm_sumpter_horse],
   str_20|agi_19|int_10|cha_5|level(25),wp(105),knows_warrior_npc|
   knows_riding_2|knows_weapon_master_2|knows_power_strike_2|knows_athletics_3|knows_trainer_1|knows_leadership_1,
  0x00000002050052036a1895d0748f3ca30000000000000f0b0000000000000000],
  ["npc7_2","Deshavi","Deshavi",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_voulge, itm_short_bow, itm_barbed_arrows, itm_nordic_fighter_helmet, itm_leather_gloves, itm_studded_leather_coat, itm_leather_boots, itm_arabian_horse_b],
   str_16|agi_13|int_10|cha_6|level(17),wp(80),knows_tracker_npc|
   knows_tracking_2|knows_athletics_2|knows_spotting_1|knows_pathfinding_1|knows_power_draw_2,
   0x00000001fc08400533a15297634d44f400000000001e02db0000000000000000],
  ["npc8_2","Matheld","Matheld",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sword_viking_2, itm_nordic_helmet, itm_byrnie, itm_leather_boots, itm_courser],
   str_18|agi_15|int_9|cha_10|level(26),wp(90),knows_warrior_npc|
   knows_weapon_master_3|knows_power_strike_2|knows_athletics_2|knows_leadership_3|knows_tactics_1,
   0x00000005800c000637db8314e331e76e00000000001c46db0000000000000000],
  ["npc9_2","Alayen","Alayen",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sword_medieval_c, itm_vaegir_fur_cap, itm_leather_vest, itm_nomad_boots, itm_courser],
   str_22|agi_19|int_7|cha_8|level(17),wp(100),knows_warrior_npc|
   knows_weapon_master_1|knows_riding_1|knows_athletics_1|knows_leadership_1|knows_tactics_1|knows_power_strike_1,
   0x000000030100300f499d5b391b6db8d300000000001dc2e10000000000000000],
  ["npc10_2","Bunduk","Bunduk",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_military_sickle_a, itm_heavy_crossbow, itm_bolts, itm_mail_coif, itm_leather_gloves, itm_aketon_green, itm_leather_boots, itm_saddle_horse],
   str_24|agi_19|int_9|cha_11|level(27),wp(105),knows_warrior_npc|
   knows_weapon_master_3|knows_tactics_1|knows_leadership_1|knows_ironflesh_3|knows_trainer_2|knows_first_aid_2,
   0x0000000a3f081006572c91c71c8d46cb00000000001e468a0000000000000000],
  ["npc11_2","Katrin","Katrin",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sarranid_axe_a, itm_arming_cap, itm_leather_gloves, itm_padded_cloth, itm_ankle_boots, itm_sumpter_horse],
   str_16|agi_17|int_10|cha_10|level(26),wp(70),knows_merchant_npc|
   knows_weapon_master_1|knows_first_aid_1|knows_wound_treatment_2|knows_ironflesh_3|knows_inventory_management_5,
   0x0000000d7f0400035915aa226b4d975200000000001ea49e0000000000000000],
  ["npc12_2","Jeremus","Jeremus",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_iron_staff, itm_padded_coif, itm_leather_gloves, itm_pilgrim_disguise, itm_leather_boots, itm_sumpter_horse],
   str_16|agi_17|int_13|cha_7|level(20),wp(30),   knows_merchant_npc|
   knows_ironflesh_1|knows_power_strike_1|knows_surgery_4|knows_wound_treatment_3|knows_first_aid_3,
   0x000000078000500e4f8ba62a9cd5d36d00000000001e36250000000000000000],
  ["npc13_2","Nizar","Nizar",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_scimitar, itm_tab_shield_small_round_b, itm_sarranid_warrior_cap, itm_sarranid_leather_armor, itm_sarranid_boots_b, itm_courser],
   str_14|agi_17|int_12|cha_8|level(19),wp(80),knows_warrior_npc|
   knows_riding_2|knows_leadership_2|knows_athletics_2|knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_1,
   0x00000004bf0475c85f4e9592de4e574c00000000001e369c0000000000000000],
  ["npc14_2","Lezalit","Lezalit",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sword_medieval_b, itm_tab_shield_heater_c, itm_mail_coif, itm_studded_leather_coat, itm_leather_boots, itm_courser],
   str_18|agi_19|int_11|cha_8|level(23),wp(100),knows_warrior_npc|
   knows_trainer_4|knows_weapon_master_3|knows_leadership_2|knows_power_strike_1,
   0x00000001a410259144d5d1d6eb55e96a00000000001db0db0000000000000000],
  ["npc15_2","Artimenner","Artimenner",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_long_axe, itm_helmet_with_neckguard, itm_leather_gloves, itm_red_gambeson, itm_leather_boots, itm_hunter],
   str_18|agi_13|int_12|cha_8|level(25),wp(80),knows_warrior_npc|
   knows_tactics_2|knows_engineer_4|knows_trade_3|knows_tracking_1|knows_spotting_1,
   0x0000000f2e1021862b4b9123594eab5300000000001d55360000000000000000],
  ["npc16_2","Klethi","Klethi",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sword_viking_2_small, itm_light_throwing_axes, itm_helmet_with_neckguard, itm_leather_gloves, itm_leather_jerkin, itm_ankle_boots, itm_saddle_horse],
   str_14|agi_17|int_8|cha_7|level(17),wp(80),knows_tracker_npc|
   knows_power_throw_3|knows_athletics_2|knows_power_strike_1,
   0x00000000000c100739ce9c805d2f381300000000001cc7ad0000000000000000],

  #tier 3
  ["npc1_3","Borcha","Borcha",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_khergit_war_helmet,itm_lamellar_gauntlets,itm_lamellar_vest_khergit,itm_khergit_leather_boots,itm_sword_medieval_c_small, itm_courser],
   str_16|agi_17|int_12|cha_7|level(14),wp(60),knows_tracker_npc|
   knows_ironflesh_1|knows_power_strike_1|knows_pathfinding_3|knows_athletics_2|knows_tracking_1|knows_riding_2, #skills 2/3 player at that level
   0x00000004bf086143259d061a9046e23500000000001db52c0000000000000000],
  ["npc2_3","Marnid","Marnid", tf_hero|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,[itm_nordic_veteran_archer_helmet,itm_leather_gloves,itm_byrnie,itm_leather_boots,itm_mace_3,itm_tab_shield_small_round_b, itm_saddle_horse],
   str_14|agi_17|int_11|cha_6|level(14),wp(40),knows_merchant_npc|
   knows_trade_2|knows_weapon_master_1|knows_ironflesh_1|knows_wound_treatment_1|knows_athletics_2|knows_first_aid_1|knows_leadership_1,
   0x000000019d004001570b893712c8d28d00000000001dc8990000000000000000],
  ["npc3_3","Ymira","Ymira",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_skullcap,itm_leather_gloves,itm_mail_shirt,itm_wrapping_boots,itm_sword_medieval_c_small, itm_hunter],
   str_24|agi_13|int_11|cha_6|level(14),wp(20),knows_merchant_npc|
   knows_wound_treatment_1|knows_trade_1|knows_first_aid_3|knows_surgery_1|knows_athletics_1|knows_riding_1,
   0x0000000083040001583b6db8dec5925b00000000001d80980000000000000000],
  ["npc4_3","Rolf","Rolf",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_bascinet_2,itm_leather_gloves,itm_surcoat_over_mail,itm_mail_chausses,itm_sword_medieval_c_long,itm_tab_shield_heater_c, itm_hunter],
   str_20|agi_13|int_13|cha_10|level(27),wp(110),knows_warrior_npc|
   knows_weapon_master_2|knows_power_strike_2|knows_riding_2|knows_athletics_2|knows_power_throw_2|knows_first_aid_1|knows_surgery_1|knows_tactics_2|knows_leadership_2,
   0x000000057f1074002c75c6a8a58ad72e00000000001e1a890000000000000000],
  ["npc5_3","Baheshtur","Baheshtur",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_scimitar, itm_tab_shield_small_round_c, itm_khergit_cavalry_helmet, itm_leather_gloves, itm_lamellar_vest, itm_khergit_leather_boots, itm_steppe_horse],
   str_18|agi_13|int_12|cha_7|level(23),wp(90),knows_warrior_npc|
   knows_riding_2|knows_horse_archery_3|knows_power_draw_3|knows_leadership_2|knows_weapon_master_1,
   0x000000088910318b5c6f972328324a6200000000001cd3310000000000000000],
  ["npc6_3","Firentis","Firentis",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_bastard_sword_b, itm_flat_topped_helmet, itm_mail_mittens, itm_haubergeon, itm_mail_chausses, itm_sumpter_horse],
   str_20|agi_19|int_10|cha_5|level(25),wp(105),knows_warrior_npc|
   knows_riding_2|knows_weapon_master_2|knows_power_strike_2|knows_athletics_3|knows_trainer_1|knows_leadership_1,
  0x00000002050052036a1895d0748f3ca30000000000000f0b0000000000000000],
  ["npc7_3","Deshavi","Deshavi",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_long_bardiche, itm_strong_bow, itm_barbed_arrows, itm_nordic_helmet, itm_leather_gloves, itm_mail_hauberk, itm_splinted_leather_greaves, itm_arabian_horse_b],
   str_16|agi_13|int_10|cha_6|level(17),wp(80),knows_tracker_npc|
   knows_tracking_2|knows_athletics_2|knows_spotting_1|knows_pathfinding_1|knows_power_draw_2,
   0x00000001fc08400533a15297634d44f400000000001e02db0000000000000000],
  ["npc8_3","Matheld","Matheld",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_battle_axe, itm_nordic_huscarl_helmet, itm_leather_gloves, itm_mail_hauberk, itm_mail_chausses, itm_courser],
   str_18|agi_15|int_9|cha_10|level(26),wp(90),knows_warrior_npc|
   knows_weapon_master_3|knows_power_strike_2|knows_athletics_2|knows_leadership_3|knows_tactics_1,
   0x00000005800c000637db8314e331e76e00000000001c46db0000000000000000],
  ["npc9_3","Alayen","Alayen",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sword_medieval_c_long, itm_vaegir_lamellar_helmet, itm_leather_gloves, itm_lamellar_vest, itm_leather_boots, itm_courser],
   str_22|agi_19|int_7|cha_8|level(17),wp(100),knows_warrior_npc|
   knows_weapon_master_1|knows_riding_1|knows_athletics_1|knows_leadership_1|knows_tactics_1|knows_power_strike_1,
   0x000000030100300f499d5b391b6db8d300000000001dc2e10000000000000000],
  ["npc10_3","Bunduk","Bunduk",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_military_pick, itm_heavy_crossbow, itm_steel_bolts, itm_kettle_hat, itm_leather_gloves, itm_mail_with_tunic_green, itm_leather_boots, itm_saddle_horse],
   str_24|agi_19|int_9|cha_11|level(27),wp(105),knows_warrior_npc|
   knows_weapon_master_3|knows_tactics_1|knows_leadership_1|knows_ironflesh_3|knows_trainer_2|knows_first_aid_2,
   0x0000000a3f081006572c91c71c8d46cb00000000001e468a0000000000000000],
  ["npc11_3","Katrin","Katrin",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sarranid_axe_b, itm_arming_cap, itm_leather_gloves, itm_mail_with_surcoat, itm_mail_chausses, itm_sumpter_horse],
   str_16|agi_17|int_10|cha_10|level(26),wp(70),knows_merchant_npc|
   knows_weapon_master_1|knows_first_aid_1|knows_wound_treatment_2|knows_ironflesh_3|knows_inventory_management_5,
   0x0000000d7f0400035915aa226b4d975200000000001ea49e0000000000000000],
  ["npc12_3","Jeremus","Jeremus",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_iron_staff, itm_mail_coif, itm_mail_mittens, itm_pilgrim_disguise, itm_mail_chausses, itm_sumpter_horse],
   str_16|agi_17|int_13|cha_7|level(20),wp(30),   knows_merchant_npc|
   knows_ironflesh_1|knows_power_strike_1|knows_surgery_4|knows_wound_treatment_3|knows_first_aid_3,
   0x000000078000500e4f8ba62a9cd5d36d00000000001e36250000000000000000],
  ["npc13_3","Nizar","Nizar",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_scimitar, itm_tab_shield_small_round_c, itm_sarranid_mail_coif, itm_arabian_armor_b, itm_sarranid_boots_c, itm_courser],
   str_14|agi_17|int_12|cha_8|level(19),wp(80),knows_warrior_npc|
   knows_riding_2|knows_leadership_2|knows_athletics_2|knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_1,
   0x00000004bf0475c85f4e9592de4e574c00000000001e369c0000000000000000],
  ["npc14_3","Lezalit","Lezalit",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sword_medieval_c, itm_tab_shield_heater_c, itm_bascinet_2, itm_leather_gloves, itm_surcoat_over_mail, itm_mail_chausses, itm_courser],
   str_18|agi_19|int_11|cha_8|level(23),wp(100),knows_warrior_npc|
   knows_trainer_4|knows_weapon_master_3|knows_leadership_2|knows_power_strike_1,
   0x00000001a410259144d5d1d6eb55e96a00000000001db0db0000000000000000],
  ["npc15_3","Artimenner","Artimenner",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_long_axe_b, itm_guard_helmet, itm_mail_mittens, itm_haubergeon, itm_mail_chausses, itm_hunter],
   str_18|agi_13|int_12|cha_8|level(25),wp(80),knows_warrior_npc|
   knows_tactics_2|knows_engineer_4|knows_trade_3|knows_tracking_1|knows_spotting_1,
   0x0000000f2e1021862b4b9123594eab5300000000001d55360000000000000000],
  ["npc16_3","Klethi","Klethi",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sword_viking_2_small, itm_throwing_axes, itm_vaegir_fur_helmet, itm_leather_gloves, itm_lamellar_vest, itm_leather_boots, itm_saddle_horse],
   str_14|agi_17|int_8|cha_7|level(17),wp(80),knows_tracker_npc|
   knows_power_throw_3|knows_athletics_2|knows_power_strike_1,
   0x00000000000c100739ce9c805d2f381300000000001cc7ad0000000000000000],

   #tier 4
  ["npc1_4","Borcha","Borcha",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_khergit_guard_helmet,itm_lamellar_gauntlets,itm_khergit_guard_armor,itm_khergit_guard_boots,itm_sword_viking_3_small, itm_courser],
   str_16|agi_17|int_12|cha_7|level(14),wp(60),knows_tracker_npc|
   knows_ironflesh_1|knows_power_strike_1|knows_pathfinding_3|knows_athletics_2|knows_tracking_1|knows_riding_2, #skills 2/3 player at that level
   0x00000004bf086143259d061a9046e23500000000001db52c0000000000000000],
  ["npc2_4","Marnid","Marnid", tf_hero|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,[itm_nordic_helmet,itm_mail_mittens,itm_mail_hauberk,itm_mail_chausses,itm_mace_4,itm_tab_shield_small_round_c, itm_saddle_horse],
   str_14|agi_17|int_11|cha_6|level(14),wp(40),knows_merchant_npc|
   knows_trade_2|knows_weapon_master_1|knows_ironflesh_1|knows_wound_treatment_1|knows_athletics_2|knows_first_aid_1|knows_leadership_1,
   0x000000019d004001570b893712c8d28d00000000001dc8990000000000000000],
  ["npc3_4","Ymira","Ymira",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_guard_helmet,itm_gauntlets,itm_plate_armor,itm_plate_boots,itm_sword_viking_3_small, itm_hunter],
   str_24|agi_13|int_11|cha_6|level(14),wp(20),knows_merchant_npc|
   knows_wound_treatment_1|knows_trade_1|knows_first_aid_3|knows_surgery_1|knows_athletics_1|knows_riding_1,
   0x0000000083040001583b6db8dec5925b00000000001d80980000000000000000],
  ["npc4_4","Rolf","Rolf",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_full_helm,itm_scale_gauntlets,itm_heraldic_mail_with_tabard,itm_iron_greaves,itm_sword_medieval_d_long,itm_tab_shield_heater_d, itm_hunter],
   str_20|agi_13|int_13|cha_10|level(27),wp(110),knows_warrior_npc|
   knows_weapon_master_2|knows_power_strike_2|knows_riding_2|knows_athletics_2|knows_power_throw_2|knows_first_aid_1|knows_surgery_1|knows_tactics_2|knows_leadership_2,
   0x000000057f1074002c75c6a8a58ad72e00000000001e1a890000000000000000],
  ["npc5_4","Baheshtur","Baheshtur",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_scimitar_b, itm_tab_shield_small_round_c, itm_khergit_guard_helmet, itm_scale_gauntlets, itm_lamellar_armor, itm_iron_greaves, itm_steppe_horse],
   str_18|agi_13|int_12|cha_7|level(23),wp(90),knows_warrior_npc|
   knows_riding_2|knows_horse_archery_3|knows_power_draw_3|knows_leadership_2|knows_weapon_master_1,
   0x000000088910318b5c6f972328324a6200000000001cd3310000000000000000],
  ["npc6_4","Firentis","Firentis",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sword_two_handed_b, itm_bascinet, itm_gauntlets, itm_cuir_bouilli, itm_plate_boots, itm_sumpter_horse],
   str_20|agi_19|int_10|cha_5|level(25),wp(105),knows_warrior_npc|
   knows_riding_2|knows_weapon_master_2|knows_power_strike_2|knows_athletics_3|knows_trainer_1|knows_leadership_1,
  0x00000002050052036a1895d0748f3ca30000000000000f0b0000000000000000],
  ["npc7_4","Deshavi","Deshavi",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_great_long_bardiche, itm_war_bow, itm_khergit_arrows, itm_nordic_huscarl_helmet, itm_scale_gauntlets, itm_heraldic_mail_with_tabard, itm_iron_greaves, itm_arabian_horse_b],
   str_16|agi_13|int_10|cha_6|level(17),wp(80),knows_tracker_npc|
   knows_tracking_2|knows_athletics_2|knows_spotting_1|knows_pathfinding_1|knows_power_draw_2,
   0x00000001fc08400533a15297634d44f400000000001e02db0000000000000000],
  ["npc8_4","Matheld","Matheld",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_great_axe, itm_nordic_warlord_helmet, itm_mail_mittens, itm_banded_armor, itm_mail_chausses, itm_courser],
   str_18|agi_15|int_9|cha_10|level(26),wp(90),knows_warrior_npc|
   knows_weapon_master_3|knows_power_strike_2|knows_athletics_2|knows_leadership_3|knows_tactics_1,
   0x00000005800c000637db8314e331e76e00000000001c46db0000000000000000],
  ["npc9_4","Alayen","Alayen",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_bastard_sword_b, itm_vaegir_war_helmet, itm_lamellar_gauntlets, itm_banded_armor, itm_iron_greaves, itm_courser],
   str_22|agi_19|int_7|cha_8|level(17),wp(100),knows_warrior_npc|
   knows_weapon_master_1|knows_riding_1|knows_athletics_1|knows_leadership_1|knows_tactics_1|knows_power_strike_1,
   0x000000030100300f499d5b391b6db8d300000000001dc2e10000000000000000],
  ["npc10_4","Bunduk","Bunduk",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_military_pick, itm_sniper_crossbow, itm_steel_bolts, itm_full_helm, itm_mail_mittens, itm_surcoat_over_mail, itm_splinted_leather_greaves, itm_saddle_horse],
   str_24|agi_19|int_9|cha_11|level(27),wp(105),knows_warrior_npc|
   knows_weapon_master_3|knows_tactics_1|knows_leadership_1|knows_ironflesh_3|knows_trainer_2|knows_first_aid_2,
   0x0000000a3f081006572c91c71c8d46cb00000000001e468a0000000000000000],
  ["npc11_4","Katrin","Katrin",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sarranid_two_handed_axe_a, itm_great_helmet, itm_gauntlets, itm_brigandine_red, itm_plate_boots, itm_sumpter_horse],
   str_16|agi_17|int_10|cha_10|level(26),wp(70),knows_merchant_npc|
   knows_weapon_master_1|knows_first_aid_1|knows_wound_treatment_2|knows_ironflesh_3|knows_inventory_management_5,
   0x0000000d7f0400035915aa226b4d975200000000001ea49e0000000000000000],
  ["npc12_4","Jeremus","Jeremus",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_iron_staff, itm_kettle_hat, itm_gauntlets, itm_surcoat_over_mail, itm_plate_boots, itm_sumpter_horse],
   str_16|agi_17|int_13|cha_7|level(20),wp(30),   knows_merchant_npc|
   knows_ironflesh_1|knows_power_strike_1|knows_surgery_4|knows_wound_treatment_3|knows_first_aid_3,
   0x000000078000500e4f8ba62a9cd5d36d00000000001e36250000000000000000],
  ["npc13_4","Nizar","Nizar",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_scimitar_b, itm_tab_shield_small_round_c, itm_sarranid_veiled_helmet, itm_scale_gauntlets, itm_mamluke_mail, itm_sarranid_boots_d, itm_courser],
   str_14|agi_17|int_12|cha_8|level(19),wp(80),knows_warrior_npc|
   knows_riding_2|knows_leadership_2|knows_athletics_2|knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_1,
   0x00000004bf0475c85f4e9592de4e574c00000000001e369c0000000000000000],
  ["npc14_4","Lezalit","Lezalit",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sword_medieval_d_long, itm_tab_shield_heater_d, itm_great_helmet, itm_gauntlets, itm_heraldic_mail_with_surcoat, itm_plate_boots, itm_courser],
   str_18|agi_19|int_11|cha_8|level(23),wp(100),knows_warrior_npc|
   knows_trainer_4|knows_weapon_master_3|knows_leadership_2|knows_power_strike_1,
   0x00000001a410259144d5d1d6eb55e96a00000000001db0db0000000000000000],
  ["npc15_4","Artimenner","Artimenner",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_long_axe_c, itm_full_helm, itm_scale_gauntlets, itm_heraldic_mail_with_surcoat, itm_iron_greaves, itm_hunter],
   str_18|agi_13|int_12|cha_8|level(25),wp(80),knows_warrior_npc|
   knows_tactics_2|knows_engineer_4|knows_trade_3|knows_tracking_1|knows_spotting_1,
   0x0000000f2e1021862b4b9123594eab5300000000001d55360000000000000000],
  ["npc16_4","Klethi","Klethi",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sword_viking_3_small, itm_heavy_throwing_axes, itm_vaegir_lamellar_helmet, itm_lamellar_gauntlets, itm_lamellar_armor, itm_khergit_guard_boots, itm_saddle_horse],
   str_14|agi_17|int_8|cha_7|level(17),wp(80),knows_tracker_npc|
   knows_power_throw_3|knows_athletics_2|knows_power_strike_1,
   0x00000000000c100739ce9c805d2f381300000000001cc7ad0000000000000000],

   ["coop_companion_equipment_ui_0","{!}multiplayer_end","{!}multiplayer_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],
   ["coop_companion_equipment_ui_0_f","{!}multiplayer_end","{!}multiplayer_end", tf_female, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],
   ["coop_companion_equipment_ui_1","{!}multiplayer_end","{!}multiplayer_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],
   ["coop_companion_equipment_ui_1_f","{!}multiplayer_end","{!}multiplayer_end", tf_female, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],
   ["coop_companion_equipment_sets_end","{!}multiplayer_end","{!}multiplayer_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],

  ##diplomacy begin
  #SB : fixed plural name (hero name), TODO actually use name/gender in hiring dialogues
  ["dplmc_chamberlain","Chamberlain Aubrey de Vere", "Aubrey de Vere",tf_hero|tf_male,0,0,fac_commoners,[itm_tabard, itm_leather_boots], def_attrib|level(10), wp(40),knows_inventory_management_10,0x0000000dfc0c238838e571c8d469c91b00000000001e39230000000000000000],

  ["dplmc_constable","Constable Miles de Gloucester","Miles de Gloucester",tf_hero|tf_male,0,0,fac_commoners,[itm_dplmc_coat_of_plates_red_constable, itm_leather_boots],
   knight_attrib_4,wp_melee(200),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_4|knows_athletics_4,0x0000000b4b1015054b1b4d591cba28d300000000001e472b0000000000000000],

  ["dplmc_chancellor","Chancellor Herfast","Herfast",tf_hero|tf_male,0,0,fac_commoners,[itm_nobleman_outfit, itm_leather_boots],def_attrib|level(10), wp(40),knows_inventory_management_10, 0x00000009a20c21cf491bad28a28628d400000000001e371a0000000000000000],

  ["dplmc_messenger","Messenger","Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_neutral,
   [itm_sword_medieval_a,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_light_crossbow,itm_bolts],
   def_attrib|agi_21|int_30|cha_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_leadership_7,man_face_young_1,man_face_old_2],
  ["dplmc_scout","Scout","Scouts",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_neutral,
   [itm_sword_medieval_a,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_light_crossbow,itm_bolts],
   def_attrib|agi_21|int_30|cha_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_leadership_7,man_face_young_1,man_face_old_2],
# recruiter kit begin
  ["dplmc_recruiter","Recruiter","Recruiter",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_neutral,
   [itm_sword_medieval_a,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_light_crossbow,itm_bolts],
   def_attrib|agi_21|int_30|cha_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_leadership_7,swadian_face_young_1, swadian_face_old_2],
# recruiter kit end
  ##diplomacy end
]


#Troop upgrade declarations

upgrade(troops,"farmer", "watchman")
upgrade(troops,"townsman","watchman")
upgrade2(troops,"watchman","caravan_guard","mercenary_crossbowman")
upgrade2(troops,"caravan_guard","mercenary_swordsman","mercenary_horseman")
upgrade(troops,"mercenary_swordsman","hired_blade")
upgrade(troops,"mercenary_horseman","mercenary_cavalry")

upgrade(troops,"delgay_mercenary","delgay_mercenary_assasin")
upgrade(troops,"delgay_mercenary_assasin","delgay_mercenary_rajas_killer")

#  nerpa troop tree
upgrade(troops,"nerpa_recruit","nerpa_footman")
upgrade2(troops,"nerpa_footman","nerpa_soldier", "nerpa_yeoman")
upgrade(troops,"nerpa_yeoman","nerpa_trickshot")

upgrade2(troops,"nerpa_soldier","nerpa_ranger","nerpa_captain")

upgrade(troops,"nerpa_ranger","nerpa_master_ranger")

upgrade(troops,"nerpa_captain","nerpa_army_veteran")
upgrade(troops,"nerpa_army_veteran","nerpa_mounted_veteran")
upgrade2(troops,"nerpa_mounted_veteran","nerpa_commader","nerpa_black_head")

# hairako troop tree
upgrade2(troops,"hairako_nomad","hairako_footman","hairako_archer")
upgrade2(troops,"hairako_footman","hairako_infantry","hairako_rider")

upgrade(troops,"hairako_infantry","hairako_infantry_veteran")
upgrade(troops,"hairako_infantry_veteran","hairako_shaitan")

upgrade(troops,"hairako_rider","hairako_experienced_rider")
upgrade(troops,"hairako_experienced_rider","hairako_mounted_shaitan")

upgrade(troops,"hairako_archer","hairako_sniper")
upgrade(troops,"hairako_sniper","hairako_sniper_elite")

# tauria
upgrade(troops,"tauria_recruit","tauria_trooper")
upgrade2(troops,"tauria_trooper","tauria_soldier","tauria_crossbowman")
upgrade2(troops,"tauria_soldier","tauria_foot_knight","tauria_horseman")

upgrade(troops,"tauria_foot_knight","tauria_sword_master")
upgrade(troops,"tauria_sword_master","tauria_man_at_arms")

upgrade(troops,"tauria_horseman","tauria_knight")
upgrade(troops,"tauria_knight","tauria_noble_knight")

upgrade(troops,"tauria_crossbowman","tauria_siege_crossbowman")

# elen
upgrade(troops,"elen_forester","elen_footman")
upgrade2(troops,"elen_footman","elen_fighter","elen_archer")

upgrade(troops,"elen_fighter","elen_light_infantry")
upgrade(troops,"elen_light_infantry","elen_heavy_infantry")
upgrade(troops,"elen_heavy_infantry", "elen_cheif")

upgrade(troops,"elen_archer","elen_experienced_archer")
upgrade(troops,"elen_experienced_archer","elen_sniper")
upgrade(troops,"elen_sniper","elen_white_hood")

# adid
upgrade(troops,"adid_nomad_scout","adid_desert_vanguard")
upgrade(troops,"adid_desert_vanguard","adid_sultanate_vanguard")

upgrade2(troops,"adid_sultanate_vanguard","adid_camel_rider","adid_serpent_guard")
upgrade(troops,"adid_camel_rider","adid_sandstalker")
upgrade(troops,"adid_serpent_guard","adid_oasis_acolyte")

upgrade2(troops,"adid_oasis_acolyte","adid_oasis_priest","adid_royal_lancer")
upgrade(troops,"adid_oasis_priest","adid_oasis_high_priest")
upgrade(troops,"adid_royal_lancer","adid_golden_falcon")

# stormguard
upgrade(troops,"stormguard_mountaineer","stormguard_thunderguard")
upgrade(troops,"stormguard_thunderguard","stormguard_stormbringer")
upgrade(troops,"stormguard_stormbringer","stormguard_avalanche_warrior")

upgrade2(troops,"stormguard_avalanche_warrior","stormguard_lightning_rider","stormguard_tempest_sentinel")
upgrade(troops,"stormguard_tempest_sentinel","stormguard_elite_stormguard")

# new troop trees for native factions
upgrade(troops,"silver_rose_novice","silver_rose_levy")

upgrade(troops,"swadian_young_lion","swadian_guild_initiate")
upgrade(troops,"swadian_guild_initiate","swadian_guild_knight")
upgrade(troops,"swadian_guild_knight","swadian_lionheart")

# native
upgrade2(troops,"silver_rose_levy","silver_rose_milita","silver_rose_scout")

upgrade2(troops,"silver_rose_milita","silver_rose_footman","silver_rose_crossbowman")
upgrade2(troops,"silver_rose_footman","silver_rose_hacker","silver_rose_infantry")
upgrade2(troops,"silver_rose_infantry","silver_rose_sergeant","silver_rose_horseman")
upgrade(troops,"silver_rose_crossbowman","silver_rose_trained_crossbowman")

upgrade(troops,"silver_rose_trained_crossbowman","silver_rose_sharpshooter")

upgrade(troops,"silver_rose_horseman","silver_rose_man_at_arms")
upgrade(troops,"silver_rose_man_at_arms","silver_rose_knight")

upgrade(troops,"vaegir_watchman","vaegir_night_watch")
upgrade(troops,"vaegir_night_watch","vaegir_watch_cheif")
upgrade(troops,"vaegir_watch_cheif","vaegir_recruit")

upgrade(troops,"vaegir_recruit","vaegir_footman")
upgrade(troops,"vaegir_footman","vaegir_veteran")

upgrade(troops,"vaegir_skirmisher","vaegir_archer")
upgrade(troops,"vaegir_archer","vaegir_marksman")

upgrade2(troops,"vaegir_veteran","vaegir_infantry", "vaegir_spearman")
upgrade(troops,"vaegir_spearman","vaegir_bardiche_bearer")
upgrade(troops,"vaegir_infantry","vaegir_guard")

upgrade(troops,"vaegir_horseman","vaegir_knight")
upgrade(troops,"vaegir_gryden","vaegir_boyar")
upgrade2(troops,"vaegir_boyar","vaegir_zemskyi_boyar","vaegir_knyazhiy_boyar")

upgrade(troops,"khergit_slave","khergit_frontliner")
upgrade(troops,"khergit_frontliner","khergit_suicidal")
upgrade(troops,"khergit_suicidal","khergit_tribesman")

upgrade(troops,"khergit_tribesman","khergit_warrior")

upgrade(troops,"khergit_warrior","khergit_swordsman")
upgrade(troops,"khergit_swordsman","khergit_veteran")
upgrade(troops,"khergit_veteran","khergit_champion")

upgrade(troops,"khergit_skirmisher","khergit_horseman")
upgrade2(troops,"khergit_horseman","khergit_lancer","khergit_horse_archer")
upgrade(troops,"khergit_horse_archer","khergit_veteran_horse_archer")

upgrade(troops,"khergit_khevtuul","khergit_kheshig")

upgrade2(troops,"nord_recruit","nord_footman","nord_huntsman")
upgrade(troops,"nord_footman","nord_trained_footman")
upgrade(troops,"nord_trained_footman","nord_warrior")
upgrade2(troops,"nord_warrior","nord_veteran", "nord_guard")
upgrade(troops,"nord_veteran","nord_champion")

upgrade(troops,"nord_huntsman","nord_archer")
upgrade2(troops,"nord_archer","nord_veteran_archer", "nord_tracer")

upgrade2(troops,"rhodok_peasant","rhodok_milita","rhodok_hunter")
upgrade(troops,"rhodok_hunter","rhodok_bear_hunter")
upgrade(troops,"rhodok_milita","rhodok_tribesman")
upgrade(troops,"rhodok_bear_hunter","rhodok_crossbowman")

upgrade2(troops,"rhodok_tribesman","rhodok_levy","rhodok_foot_knight")
upgrade(troops,"rhodok_foot_knight","rhodok_swordmaster")
upgrade(troops,"rhodok_swordmaster","rhodok_brother_of_sword")

upgrade2(troops,"rhodok_levy","rhodok_spearman","rhodok_crossbowman")
upgrade2(troops,"rhodok_spearman","rhodok_trained_spearman", "rhodok_executioner")
upgrade(troops,"rhodok_executioner","rhodok_law_itself")
upgrade(troops,"rhodok_trained_spearman","rhodok_veteran_spearman")
upgrade(troops,"rhodok_veteran_spearman","rhodok_sergeant")

upgrade(troops,"rhodok_crossbowman","rhodok_trained_crossbowman")
upgrade(troops,"rhodok_trained_crossbowman","rhodok_veteran_crossbowman") #new 1.126
upgrade(troops,"rhodok_veteran_crossbowman","rhodok_sharpshooter")


upgrade(troops,"sarranid_recruit","sarranid_footman")

upgrade2(troops,"sarranid_footman","sarranid_veteran_footman","sarranid_skirmisher")
upgrade2(troops,"sarranid_veteran_footman","sarranid_horseman","sarranid_infantry")
upgrade(troops,"sarranid_infantry","sarranid_guard")
upgrade(troops,"sarranid_skirmisher","sarranid_archer")

upgrade(troops,"sarranid_archer","sarranid_master_archer")

upgrade(troops,"sarranid_horseman","sarranid_mamluke")


#        Looter
#        /        \
#      Bandit   Outlaw
#      /      \         /    
# Pillager   Marauder  Highwayman
#                     |
#               Bandit Lord
upgrade2(troops,"looter","bandit","outlaw")
upgrade2(troops,"bandit","pillager","marauder")

upgrade(troops,"outlaw","highwayman")
upgrade(troops,"highwayman","bandit_lord")

# Cultists
upgrade(troops,"cultist_acolyte","dark_cultist")

#new tree connections
upgrade(troops,"mountain_bandit","rhodok_tribesman")
upgrade(troops,"forest_bandit","silver_rose_levy")
upgrade(troops,"steppe_bandit","khergit_tribesman")
upgrade(troops,"taiga_bandit","vaegir_recruit")
upgrade(troops,"sea_raider","nord_recruit")
upgrade(troops,"desert_bandit","sarranid_recruit")
#new tree connections ended

upgrade2(troops,"bandit","brigand","mercenary_swordsman")
upgrade(troops,"manhunter","slave_driver")

#upgrade(troops,"forest_bandit","mercenary_crossbowman")

upgrade(troops,"slave_driver","slave_hunter")
upgrade(troops,"slave_hunter","slave_crusher")
upgrade(troops,"slave_crusher","slaver_chief")

upgrade(troops,"follower_woman","hunter_woman")
upgrade(troops,"hunter_woman","fighter_woman")

upgrade(troops,"fighter_woman","sword_sister")
upgrade(troops,"refugee","follower_woman")
upgrade(troops,"peasant_woman","follower_woman")
# modmerger_start version=201 type=2
try:
    component_name = "troops"
    var_set = { "troops" : troops }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end
