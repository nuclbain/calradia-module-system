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
  [
    "player",
    "Player",
    "Player",
    tf_hero|tf_unmoveable_in_party_window,
    no_scene,
    reserved,
    fac_player_faction,
    [],
    str_4|agi_4|int_4|cha_4,
    wp(15),
    0,
    0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000
  ],

  [
    "multiplayer_profile_troop_male",
    "multiplayer_profile_troop_male",
    "multiplayer_profile_troop_male",
    tf_hero|tf_guarantee_all,
    0,
    0,
    fac_commoners,
    [
      itm_shirt,
      itm_leather_shoes_a
    ],
    0,
    0,
    0,
    0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000
  ],

  [
    "multiplayer_profile_troop_female",
    "multiplayer_profile_troop_female",
    "multiplayer_profile_troop_female",
    tf_hero|tf_female|tf_guarantee_all,
    0,
    0,
    fac_commoners,
    [
      itm_shirt,
      itm_leather_shoes_a
    ],
    0,
    0,
    0,
    0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000
  ],

  [
    "temp_troop",
    "Temp Troop",
    "Temp Troop",
    tf_hero,
    no_scene,
    reserved,
    fac_commoners,
    [],
    def_attrib,
    0,
    knows_common|knows_inventory_management_10,
    0
  ],

  ####################################################################################################################
  # Troops before this point are hardwired into the game and their order should not be changed!
  ####################################################################################################################
  [
    "find_item_cheat",
    "find_item_cheat",
    "find_item_cheat",
    tf_hero|tf_is_merchant,
    no_scene,
    reserved,
    fac_commoners,
    [],
    def_attrib,
    0,
    knows_common|knows_inventory_management_10,
    0
  ],

  [
    "random_town_sequence",
    "Random Town Sequence",
    "Random Town Sequence",
    tf_hero,
    no_scene,
    reserved,
    fac_commoners,
    [],
    def_attrib,
    0,
    knows_common|knows_inventory_management_10,
    0
  ],

  [
    "tournament_participants",
    "Tournament Participants",
    "Tournament Participants",
    tf_hero,
    no_scene,
    reserved,
    fac_commoners,
    [],
    def_attrib,
    0,
    knows_common|knows_inventory_management_10,
    0
  ],

  [
    "tutorial_maceman",
    "Maceman",
    "Maceman",
    tf_guarantee_boots|tf_guarantee_armor,
    no_scene,
    reserved,
    fac_commoners,
    [
      itm_tutorial_club,
      itm_shirt,
      itm_leather_shoes_a
    ],

   str_6|agi_6|level(1),
   wp(50),
   knows_common,
   mercenary_face_1,
   mercenary_face_2],

  [
    "tutorial_archer",
    "Archer",
    "Archer",
    tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,
    no_scene,
    reserved,
    fac_commoners,
    [
      itm_tutorial_short_bow,
      itm_tutorial_arrows,
      itm_shirt,
      itm_leather_shoes_a
    ],
    str_6|agi_6|level(5),
    wp(100),
    knows_common|knows_power_draw_4,
    mercenary_face_1,
    mercenary_face_2
  ],

  [
    "tutorial_swordsman",
    "Swordsman",
    "Swordsman",
    tf_guarantee_boots|tf_guarantee_armor,
    no_scene,
    reserved,
    fac_commoners,
    [
      itm_tutorial_sword,
      itm_shirt,
      itm_leather_shoes_a
    ],
    str_6|agi_6|level(5),
    wp(80),
    knows_common,
    mercenary_face_1,
    mercenary_face_2
  ],

  # ========================================================================================================
  # Training partners
  # ========================================================================================================
  [
    "novice_fighter",
    "Novice Fighter",
    "Novice Fighters",
    tf_guarantee_boots|tf_guarantee_armor,
    no_scene,
    reserved,
    fac_commoners,
    [
      itm_short_tunic,
      itm_poulaines_b
    ],
    str_6|agi_6|level(5),
    wp(60),
    knows_common,
    mercenary_face_1,
    mercenary_face_2
  ],
   
  [
    "regular_fighter",
    "Regular Fighter",
    "Regular Fighters",
    tf_guarantee_boots|tf_guarantee_armor,
    no_scene,
    reserved,
    fac_commoners,
    [
      itm_short_tunic,
      itm_poulaines_b
    ],
    str_8|agi_8|level(11),
    wp(90),
    knows_common|knows_ironflesh_1|knows_power_strike_1|knows_athletics_1|knows_riding_1|knows_shield_2,
    mercenary_face_1,
    mercenary_face_2
  ],
   
  [
    "veteran_fighter",
    "Veteran Fighter",
    "Veteran Fighters",
    tf_guarantee_boots|tf_guarantee_armor,
    no_scene,
    0,
    fac_commoners,
    [
      itm_short_tunic,
      itm_poulaines_b
    ],
    str_10|agi_10|level(17),
    wp(110),
    knows_common|knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2|knows_shield_3,
    mercenary_face_1,
    mercenary_face_2
  ],
 
  [
    "champion_fighter",
    "Champion Fighter",
    "Champion Fighters",
    tf_guarantee_boots|tf_guarantee_armor,
    no_scene,
    reserved,
    fac_commoners,
    [
      itm_short_tunic,
      itm_poulaines_b
    ],
    str_12|agi_11|level(22),
    wp(140),
    knows_common|knows_ironflesh_4|knows_power_strike_3|knows_athletics_3|knows_riding_3|knows_shield_4,
    mercenary_face_1,
    mercenary_face_2
  ], 

  [
    "arena_training_fighter_1",
    "Novice Fighter",
    "Novice Fighters",
    tf_guarantee_boots|tf_guarantee_armor,
    no_scene,
    reserved,
    fac_commoners,
    [
      itm_short_tunic,
      itm_poulaines_b
    ],
    str_6|agi_6|level(5),
    wp(60),
    knows_common,
    mercenary_face_1,
    mercenary_face_2
  ],
 
  [
    "arena_training_fighter_2",
    "Novice Fighter",
    "Novice Fighters",
    tf_guarantee_boots|tf_guarantee_armor,
    no_scene,
    reserved,
    fac_commoners,
    [
      itm_short_tunic,
      itm_poulaines_b
    ],
    str_7|agi_6|level(7),
    wp(70),
    knows_common,
    mercenary_face_1,
    mercenary_face_2
  ],
 
  [
    "arena_training_fighter_3",
    "Regular Fighter",
    "Regular Fighters",
    tf_guarantee_boots|tf_guarantee_armor,
    no_scene,
    reserved,
    fac_commoners,
    [
      itm_short_tunic,
      itm_poulaines_b
    ],
    str_8|agi_7|level(9),
    wp(80),
    knows_common,
    mercenary_face_1,
    mercenary_face_2
  ],
 
  [
    "arena_training_fighter_4",
    "Regular Fighter",
    "Regular Fighters",
    tf_guarantee_boots|tf_guarantee_armor,
    no_scene,
    reserved,
    fac_commoners,
    [
      itm_short_tunic,
      itm_poulaines_b
    ],
    str_8|agi_8|level(11),
    wp(90),
    knows_common,
    mercenary_face_1,
    mercenary_face_2
  ],
 
  [
    "arena_training_fighter_5",
    "Regular Fighter",
    "Regular Fighters",
    tf_guarantee_boots|tf_guarantee_armor,
    no_scene,
    reserved,
    fac_commoners,
    [
      itm_short_tunic,
      itm_poulaines_b
    ],
    str_9|agi_8|level(13),
    wp(100),
    knows_common,
    mercenary_face_1,
    mercenary_face_2
  ],
 
  [
    "arena_training_fighter_6",
    "Veteran Fighter",
    "Veteran Fighters",
    tf_guarantee_boots|tf_guarantee_armor,
    no_scene,
    reserved,
    fac_commoners,
    [
      itm_short_tunic,
      itm_poulaines_b
    ],
    str_10|agi_9|level(15),
    wp(110),
    knows_common,
    mercenary_face_1,
    mercenary_face_2
  ],
 
  [
    "arena_training_fighter_7",
    "Veteran Fighter",
    "Veteran Fighters",
    tf_guarantee_boots|tf_guarantee_armor,
    no_scene,
    reserved,
    fac_commoners,
    [
      itm_short_tunic,
      itm_poulaines_b
    ],
    str_10|agi_10|level(17),
    wp(120),
    knows_common,
    mercenary_face_1,
    mercenary_face_2
  ],
 
  [
    "arena_training_fighter_8",
    "Veteran Fighter",
    "Veteran Fighters",
    tf_guarantee_boots|tf_guarantee_armor,
    no_scene,
    reserved,
    fac_commoners,
    [
      itm_short_tunic,
      itm_poulaines_b
    ],
    str_11|agi_10|level(19),
    wp(130),
    knows_common,
    mercenary_face_1,
    mercenary_face_2
  ],
 
  [
    "arena_training_fighter_9",
    "Champion Fighter",
    "Champion Fighters",
    tf_guarantee_boots|tf_guarantee_armor,
    no_scene,
    reserved,
    fac_commoners,
    [
      itm_short_tunic,
      itm_poulaines_b
    ],
    str_12|agi_11|level(21),
    wp(140),
    knows_common,
    mercenary_face_1,
    mercenary_face_2
  ],
 
  [
    "arena_training_fighter_10",
    "Champion Fighter",
    "Champion Fighters",
    tf_guarantee_boots|tf_guarantee_armor,
    no_scene,
    reserved,
    fac_commoners,
    [
      itm_short_tunic,
      itm_poulaines_b
    ],
    str_12|agi_12|level(23),
    wp(150),
    knows_common,
    mercenary_face_1,
    mercenary_face_2
  ], 

  # ========================================================================================================
  # Cattle
  # ========================================================================================================
  [
    "cattle",
    "Cattle",
    "Cattle",
    0,
    no_scene,
    reserved,
    fac_neutral,
    [],
    def_attrib|level(1),
    wp(60),
    0,
    mercenary_face_1,
    mercenary_face_2
  ],

  # ========================================================================================================
  # Generic troops that dont really belong to any faction and mercenaries
  # ========================================================================================================
  # This troop is the troop marked as soldiers_begin
  [
    "farmer",
    "Farmer",
    "Farmers",
    tf_guarantee_armor,
    no_scene,
    reserved,
    fac_commoners,
    [
      itm_cleaver,
      itm_knife,
      itm_pitch_fork,
      itm_sickle,
      itm_club,
      itm_stones,
      itm_leather_cap,
      itm_felt_hat,
      itm_felt_hat,
      itm_shirt,
      itm_linen_tunic,
      itm_short_tunic,
      itm_poulaines_b,
      itm_poulaines_d
    ],
    def_attrib|level(4),
    wp(60),
    knows_common,
    man_face_middle_1,
    man_face_old_2
  ],

  [
    "townsman",
    "Townsman",
    "Townsmen",
    tf_guarantee_boots|tf_guarantee_armor,
    no_scene,
    reserved,
    fac_commoners,
    [
      itm_cleaver,
      itm_knife,
      itm_club,
      itm_quarter_staff,
      itm_dagger,
      itm_stones,
      itm_leather_cap,
      itm_linen_tunic,
      itm_short_tunic,
      itm_tunic_with_green_cape,
      itm_poulaines_b,
      itm_poulaines_d
    ],
    def_attrib|level(4),
    wp(60),
    knows_common,
    mercenary_face_1,
    mercenary_face_2
  ],

  [
    "watchman",
    "Watchman",
    "Watchmen",
    tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,
    no_scene,
    reserved,
    fac_commoners,
    [
      itm_bolts,
      itm_mace_3,
      itm_mace_3,
      itm_fighting_pick,
      itm_sword_medieval_a,
      itm_spear,
      itm_hunting_crossbow,
      itm_light_crossbow,
      itm_shield_kite_k,
      itm_short_tunic,
      itm_cheap_padding_a,
      itm_cheap_padding_b,
      itm_neutral_sallet_a,
      itm_neutral_sallet_b,
      itm_leather_gloves,
      itm_old_leather_gloves,
      itm_poulaines_b,
      itm_hose_b
    ],
    def_attrib|level(9),
    wp(75),
    knows_common|knows_shield_1,
    mercenary_face_1,
    mercenary_face_2
  ],

  [
    "caravan_guard",
    "Caravan Guard",
    "Caravan Guards",
    tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield,
    no_scene,
    0,
    fac_commoners,
    [
      itm_fighting_pick,
      itm_sword_medieval_a,
      itm_sword_medieval_b,
      itm_sword_medieval_c_long,
      itm_sword_medieval_d_long,
      itm_spear,
      itm_shield_kite_k,
      itm_cheap_mail_a,
      itm_cheap_mail_b,
      itm_neutral_sallet_a,
      itm_neutral_sallet_b,
      itm_neutral_chapel_a,
      itm_neutral_kettlehat_a,
      itm_m_gloves_a,
      itm_poulaines_b,
      itm_hose_b,
      itm_saddle_horse
    ],
    def_attrib|level(14),
    wp(85),
    knows_common|knows_riding_2|knows_ironflesh_1|knows_shield_3,
    mercenary_face_1,
    mercenary_face_2
  ],

  [
    "mercenary_swordsman",
    "Mercenary Swordsman",
    "Mercenary Swordsmen",
    tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
    no_scene,
    reserved,
    fac_commoners,
    [
      itm_scottish_sword,
      itm_grosse_messer_b,
      itm_crusader_sword,
      itm_longsword,
      itm_english_longsword,
      itm_german_bastard_sword,
      itm_shield_kite_k,
      itm_shield_heater_d,
      itm_neutral_aketon_a,
      itm_neutral_aketon_a_v1,
      itm_neutral_aketon_b,
      itm_neutral_aketon_c,
      itm_neutral_aketon_c_v1,
      itm_neutral_sallet_a,
      itm_neutral_sallet_b,
      itm_neutral_chapel_a,
      itm_neutral_kettlehat_a,
      itm_leather_gloves,
      itm_m_gloves_a,
      itm_poulaines_b,
      itm_hose_b,
      itm_leather_boots_a
    ],
    def_attrib|level(20),
    wp(100),
    knows_common|knows_riding_3|knows_ironflesh_3|knows_shield_3|knows_power_strike_3,
    mercenary_face_1,
    mercenary_face_2
  ],

  [
    "hired_blade",
    "Hired Blade",
    "Hired Blades",
    tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,
    no_scene,
    reserved,
    fac_commoners,
    [
      itm_scottish_sword,
      itm_grosse_messer_b,
      itm_crusader_sword,
      itm_longsword,
      itm_english_longsword,
      itm_german_bastard_sword,
      itm_shield_kite_k,
      itm_shield_heater_d,
      itm_hauberk_neutral_a,
      itm_hauberk_neutral_a_v1,
      itm_neutral_sallet_a,
      itm_neutral_sallet_b,
      itm_neutral_chapel_a,
      itm_neutral_kettlehat_a,
      itm_m_gloves_a,
      itm_mail_mittens,
      itm_old_mail_gloves,
      itm_mail_boots_a,
      itm_mail_boots_b,
      itm_mail_boots_c
    ],
    def_attrib|level(25),
    wp(130),
    knows_common|knows_riding_3|knows_athletics_5|knows_shield_5|knows_power_strike_5|knows_ironflesh_5,
    mercenary_face_1,
    mercenary_face_2
  ],

  [
    "mercenary_crossbowman",
    "Mercenary Crossbowman",
    "Mercenary Crossbowmen",
    tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,
    no_scene,
    reserved,
    fac_commoners,
    [
      itm_bolts,
      itm_mace_3,
      itm_mace_3,
      itm_fighting_pick,
      itm_side_sword,
      itm_longbowman_sword,
      itm_hunting_crossbow,
      itm_light_crossbow,
      itm_shield_kite_k,
      itm_neutral_aketon_a,
      itm_neutral_aketon_a_v1,
      itm_neutral_aketon_b,
      itm_neutral_aketon_c,
      itm_neutral_aketon_c_v1,
      itm_neutral_sallet_a,
      itm_neutral_sallet_b,
      itm_neutral_chapel_a,
      itm_neutral_kettlehat_a,
      itm_leather_gloves,
      itm_m_gloves_a,
      itm_poulaines_b,
      itm_hose_b
    ],
    def_attrib|level(19),
    wp_one_handed (90) | wp_two_handed (90) | wp_polearm (90) | wp_archery (90) | wp_crossbow (130) | wp_throwing (90),
    knows_common|knows_athletics_5|knows_shield_1,
    mercenary_face_1,
    mercenary_face_2
  ],

  [
    "mercenary_horseman",
    "Mercenary Horseman",
    "Mercenary Horsemen",
    tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,
    no_scene,
    reserved,
    fac_commoners,
    [
      itm_espada_eslavona_b,
      itm_espada_eslavona_a,
      itm_lance,
      itm_shield_heater_d,
      itm_hauberk_neutral_a,
      itm_hauberk_neutral_a_v1,
      itm_brigandine_neutral_a,
      itm_brigandine_neutral_a_v1,
      itm_brigandine_neutral_b,
      itm_brigandine_neutral_b_v1,
      itm_neutral_sallet_a,
      itm_neutral_sallet_b,
      itm_neutral_chapel_a,
      itm_neutral_kettlehat_a,
      itm_leather_gloves,
      itm_m_gloves_a,
      itm_leather_boots_a,
      itm_hunter
    ],
    def_attrib|level(20),
    wp(100),
    knows_common|knows_riding_4|knows_ironflesh_3|knows_shield_2|knows_power_strike_3,
    mercenary_face_1,
    mercenary_face_2
  ],

  [
    "mercenary_cavalry",
    "Mercenary Cavalry",
    "Mercenary Cavalry",
    tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,
    no_scene,
    reserved,
    fac_commoners,
    [
      itm_crusader_sword,
      itm_longsword,
      itm_english_longsword,
      itm_german_bastard_sword,
      itm_lance,
      itm_shield_heater_d,
      itm_brigandine_neutral_heavy_a,
      itm_brigandine_neutral_heavy_a_v1,
      itm_brigandine_neutral_heavy_b,
      itm_brigandine_neutral_heavy_b_v1,
      itm_neutral_sallet_a,
      itm_neutral_sallet_b,
      itm_neutral_chapel_a,
      itm_neutral_kettlehat_a,
      itm_m_gloves_a,
      itm_mail_mittens,
      itm_old_mail_gloves,
      itm_mail_boots_a,
      itm_mail_boots_b,
      itm_mail_boots_c,
      itm_warhorse
    ],
    def_attrib|level(25),
    wp(130),
    knows_common|knows_riding_5|knows_ironflesh_4|knows_shield_5|knows_power_strike_4,
    mercenary_face_1,
    mercenary_face_2
  ],

  [
    "delgay_mercenary",
    "Delgay Mercenary",
    "Delgay Mercenaries",
    tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield,
    no_scene,
    0,
    fac_commoners,
    [
      itm_solarian_turban_a,
      itm_solarian_turban_b,
      itm_solarian_turban_c,
      itm_solarian_mail_vest_f,
      itm_solarian_mail_vest_e,
      itm_eastern_scale_gloves_a,
      itm_eastern_scale_gloves_b,
      itm_desert_rich_boots_a,
      itm_desert_rich_boots_b,
      itm_maa_camel_rider_shield_a,
      itm_maa_camel_rider_shield_b,
      itm_maa_camel_rider_shield_c,
      itm_maa_camel_rider_shield_d,
      itm_maa_camel_rider_shield_e,
      itm_maa_camel_rider_shield_f,
      itm_sarranid_mace_1,
      itm_sarranid_axe_a,
      itm_sarranid_axe_b,
      itm_falshion_2,
      itm_falshion_1
    ],
    def_attrib|level(14),
    wp(85),
    knows_common|knows_riding_2|knows_ironflesh_1|knows_shield_3,
    mercenary_face_1,
    mercenary_face_2
  ],

  [
    "delgay_mercenary_assasin",
    "Delgay Mercenary Assasin",
    "Delgay Mercenaries Assasin",
    tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield,
    no_scene,
    0,
    fac_commoners,
    [
      itm_solarian_turban_c,
      itm_solarian_armor_scale_c,
      itm_solarian_armor_scale_a,
      itm_eastern_scale_gloves_a,
      itm_eastern_scale_gloves_b,
      itm_desert_rich_boots_a,
      itm_desert_rich_boots_b,
      itm_maa_camel_rider_shield_a,
      itm_maa_camel_rider_shield_b,
      itm_maa_camel_rider_shield_c,
      itm_maa_camel_rider_shield_d,
      itm_maa_camel_rider_shield_e,
      itm_maa_camel_rider_shield_f,
      itm_falshion_2,
      itm_falshion_1,
      itm_throwing_daggers,
      itm_throwing_daggers
    ],
    def_attrib|agi_25|level(24),
    wp(150)|wp_throwing(220),
    knows_common|knows_riding_2|knows_ironflesh_9|knows_power_strike_4|knows_power_throw_10|knows_athletics_10|knows_shield_3,
    mercenary_face_1,
    mercenary_face_2
  ],

  [
    "delgay_mercenary_rajas_killer",
    "Delgay Mercenary Rajas Killer",
    "Delgay Mercenaries Rajas Killers",
    tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield,
    no_scene,
    0,
    fac_commoners,
    [
      itm_solarian_turban_c,
      itm_mkk_black_scale_a,
      itm_mkk_black_scale_b,
      itm_mkk_black_scale_c,
      itm_eastern_scale_gloves_a,
      itm_eastern_scale_gloves_b,
      itm_desert_rich_boots_a,
      itm_desert_rich_boots_b,
      itm_maa_camel_rider_shield_a,
      itm_maa_camel_rider_shield_b,
      itm_maa_camel_rider_shield_c,
      itm_maa_camel_rider_shield_d,
      itm_maa_camel_rider_shield_e,
      itm_maa_camel_rider_shield_f,
      itm_falshion_2,
      itm_falshion_1,
      itm_throwing_daggers,
      itm_throwing_daggers
    ],
    def_attrib|agi_30|str_30|level(34),
    wp(250)|wp_throwing(420),
    knows_common|knows_riding_2|knows_ironflesh_10|knows_power_strike_8|knows_power_throw_10|knows_athletics_10|knows_shield_3,
    mercenary_face_1,
    mercenary_face_2
  ],

  [
    "menegras_halberdier",
    "Menegras Halberdier",
    "Menegras Halberdiers",
    tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,
    no_scene,
    reserved,
    fac_commoners,
    [
      itm_player_skull_helmet_a,
      itm_player_skull_helmet_b,
      itm_m_aketon_a,
      itm_m_aketon_b,
      itm_leather_gloves,
      itm_old_leather_gloves,
      itm_m_gloves_a,
      itm_poulaines_b,
      itm_poulaines_d,
      itm_guisarme,
      itm_swiss_halberd,
      itm_english_bill
    ],
    def_attrib|level(14),
    wp(135),
    knows_common|knows_power_strike_2|knows_ironflesh_2|knows_athletics_2,
    mercenary_face_1,
    mercenary_face_2
  ],

  [
    "experienced_menegras_halberdier",
    "Experienced Menegras Halberdier",
    "Experienced Menegras Halberdiers",
    tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,
    no_scene,
    reserved,
    fac_commoners,
    [
      itm_player_skull_helmet_c,
      itm_player_skull_helmet_d,
      itm_m_hauberk_b,
      itm_m_hauberk_c,
      itm_mail_mittens,
      itm_old_mail_gloves,
      itm_m_gloves_a,
      itm_mail_boots_a,
      itm_mail_boots_b,
      itm_mail_boots_c,
      itm_guisarme,
      itm_swiss_halberd,
      itm_english_bill
    ],
    def_attrib|level(20),
    wp(175),
    knows_common|knows_power_strike_3|knows_ironflesh_3|knows_athletics_3,
    mercenary_face_1,
    mercenary_face_2
  ],

  [
    "menegras_halberdier_veteran",
    "Menegras Halberdier Veteran",
    "Menegras Halberdiers Veterans",
    tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,
    no_scene,
    reserved,
    fac_commoners,
    [
      itm_player_skull_helmet_c,
      itm_player_skull_helmet_d,
      itm_m_brigandine_f,
      itm_m_brigandine_g,
      itm_mail_mittens,
      itm_m_gauntlets_a,
      itm_m_gauntlets_b,
      itm_plate_boots_a,
      itm_plate_boots_b,
      itm_guisarme,
      itm_swiss_halberd,
      itm_english_bill
    ],
    def_attrib|level(26),
    wp(215),
    knows_common|knows_power_strike_4|knows_ironflesh_4|knows_athletics_4,
    mercenary_face_1,
    mercenary_face_2
  ],

  [
    "mercenaries_end",
    "mercenaries_end",
    "mercenaries_end",
    0,
    no_scene,
    reserved,
    fac_commoners,
    [],
    def_attrib|level(4),
    wp(60),
    knows_common,
    mercenary_face_1,
    mercenary_face_2
  ],

  # Nerpa troops
  [
    "nerpa_recruit",
    "Nerpa Recruit",
    "Nerpa Recruits",
    tf_guarantee_armor|tf_guarantee_boots,
    0,
    0,
    fac_kingdom_7,
    [
      itm_nerpa_shirt_a,
      itm_nerpa_shirt_a_v1,
      itm_arming_cap,
      itm_sword_medieval_c_small,
      itm_mace_2,
      itm_mace_4,
      itm_poulaines_b,
      itm_hose_b,
      itm_tab_shield_pavise_a
    ],
    def_attrib|level(5),
    wp(60),
    knows_common,
    swadian_face_younger_1,
    swadian_face_middle_2
  ],

  [
    "nerpa_footman",
    "Nerpa Footman",
    "Nerpa Footmen",
    tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet,
    0,
    0,
    fac_kingdom_7,
    [
      itm_m_nerpa_aketon_a,
      itm_m_nerpa_aketon_b,
      itm_nerpa_barbuta_open_cloth_a,
      itm_nerpa_barbuta_open_cloth_b,
      itm_nerpa_barbuta_open_a,
      itm_nerpa_barbuta_open_b,
      itm_sword_medieval_c_small,
      itm_mace_2,
      itm_mace_4,
      itm_tab_shield_pavise_a,
      itm_poulaines_b,
      itm_hose_b
    ],
    def_attrib|level(10),
    wp(90),
    knows_common,
    swadian_face_younger_1,
    swadian_face_middle_2
  ],

  [
    "nerpa_yeoman",
    "Nerpa Yeoman",
    "Nerpa Yeomen",
    tf_guarantee_all,
    0,
    0,
    fac_kingdom_7,
    [
      itm_m_nerpa_aketon_a,
      itm_m_nerpa_aketon_b,
      itm_nerpa_barbuta_open_a,
      itm_nerpa_barbuta_open_b,
      itm_sword_medieval_c_small,
      itm_mace_2,
      itm_mace_4,
      itm_long_bow,
      itm_arrows,
      itm_poulaines_b,
      itm_hose_b
    ],
    def_attrib|level(15),
    wp(100)|wp_archery(50),
    knows_common|knows_power_draw_3,
    swadian_face_younger_1,
    swadian_face_middle_2
  ],

  [
    "nerpa_trickshot",
    "Nerpa Trickshot",
    "Nerpa Trickshots",
    tf_guarantee_all,
    0,
    0,
    fac_kingdom_7,
    [
      itm_m_nerpa_coat_of_plates_light_a,
      itm_m_nerpa_coat_of_plates_light_a_v1,
      itm_m_nerpa_coat_of_plates_light_b,
      itm_m_nerpa_coat_of_plates_light_b_v1,
      itm_nerpa_barbuta_open_nasal,
      itm_sword_medieval_c_small,
      itm_mace_2,
      itm_mace_4,
      itm_long_bow,
      itm_arrows,
      itm_leather_boots_a
    ],
    def_attrib|level(20),
    wp(130)|wp_archery(50),
    knows_common|knows_power_draw_6,
    swadian_face_younger_1,
    swadian_face_middle_2
  ],

  [
    "nerpa_soldier",
    "Nerpa Soldier",
    "Nerpa Soldiers",
    tf_guarantee_all,
    0,
    0,
    fac_kingdom_7,
    [
      itm_m_nerpa_coat_of_plates_light_a,
      itm_m_nerpa_coat_of_plates_light_a_v1,
      itm_m_nerpa_coat_of_plates_light_b,
      itm_m_nerpa_coat_of_plates_light_b_v1,
      itm_nerpa_barbuta_open_cloth_a,
      itm_nerpa_barbuta_open_cloth_b,
      itm_nerpa_barbuta_open_padded_a,
      itm_nerpa_barbuta_open_padded_b,
      itm_sword_medieval_c_small,
      itm_mace_2,
      itm_mace_4,
      itm_tab_shield_pavise_c,
      itm_leather_boots_a
    ],
    def_attrib|level(15),
    wp(120),
    knows_common,
    swadian_face_younger_1,
    swadian_face_middle_2
  ],

  [
    "nerpa_captain",
    "Nerpa Captain",
    "Nerpa Captains",
    tf_guarantee_all,
    0,
    0,
    fac_kingdom_7,
    [
      itm_m_nerpa_coat_of_plates_medium_a,
      itm_m_nerpa_coat_of_plates_medium_b,
      itm_nerpa_barbuta_open_padded_a,
      itm_nerpa_barbuta_open_padded_b,
      itm_sword_medieval_c_small,
      itm_mace_2,
      itm_mace_4,
      itm_tab_shield_pavise_c,
      itm_leather_gloves,
      itm_mail_boots_a
    ],
    def_attrib|level(20),
    wp(150),
    knows_common|knows_ironflesh_2|knows_power_strike_2|knows_athletics_3,
    swadian_face_younger_1,
    swadian_face_middle_2
  ],

  [
    "nerpa_army_veteran",
    "Nerpa Army Veteran",
    "Nerpa Army Veterans",
    tf_guarantee_all,
    0,
    0,
    fac_kingdom_7,
    [
      itm_m_nerpa_coat_of_plates_heavy_a,
      itm_m_nerpa_coat_of_plates_heavy_b,
      itm_nerpa_barbuta_open_padded_a,
      itm_nerpa_barbuta_open_padded_b,
      itm_sword_medieval_c_small,
      itm_awlpike,
      itm_awlpike_long,
      itm_tab_shield_pavise_c,
      itm_m_gloves_a,
      itm_mail_boots_a
    ],
    def_attrib|level(25),
    wp(180)|wp_polearm(50),
    knows_common|knows_ironflesh_5|knows_power_strike_5|knows_athletics_3,
    swadian_face_old_1,
    swadian_face_old_2
  ],

  [
    "nerpa_mounted_veteran",
    "Nerpa Mounted Veteran",
    "Nerpa Mounted Veterans",
    tf_guarantee_all,
    0,
    0,
    fac_kingdom_7,
    [
      itm_m_nerpa_coat_of_plates_medium_a,
      itm_m_nerpa_coat_of_plates_medium_b,
      itm_nerpa_barbuta_a,
      itm_nerpa_barbuta_b,
      itm_nerpa_barbuta_c,
      itm_sword_medieval_c_small,
      itm_awlpike,
      itm_awlpike_long,
      itm_steel_shield,
      itm_m_gloves_a,
      itm_mail_boots_a,
      itm_leather_boots_a,
      itm_hunter
    ],
    def_attrib|level(30),
    wp(210)|wp_polearm(50),
    knows_common|knows_ironflesh_5|knows_power_strike_5|knows_athletics_3|knows_riding_5,
    swadian_face_old_1,
    swadian_face_old_2
  ],

  [
    "nerpa_commader",
    "Nerpa Commander",
    "Nerpa Commanders",
    tf_guarantee_all,
    0,
    0,
    fac_kingdom_7,
    [
      itm_m_nerpa_coat_of_plates_heavy_a,
      itm_m_nerpa_coat_of_plates_heavy_b,
      itm_nerpa_barbuta_a,
      itm_nerpa_barbuta_b,
      itm_nerpa_barbuta_c,
      itm_sword_medieval_c_small,
      itm_awlpike,
      itm_awlpike_long,
      itm_steel_shield,
      itm_m_gloves_a,
      itm_m_gauntlets_a,
      itm_mail_boots_a,
      itm_warhorse
    ],
    def_attrib|level(35),
    wp(240)|wp_polearm(50),
    knows_common|knows_ironflesh_6|knows_power_strike_6|knows_athletics_3|knows_riding_8,
    swadian_face_old_1,
    swadian_face_old_2
  ],

  [
    "nerpa_black_head",
    "Nerpa Black Head",
    "Nerpa Black Heads",
    tf_guarantee_all,
    0,
    0,
    fac_kingdom_7,
    [
      itm_m_nerpa_coat_of_plates_heavy_a,
      itm_m_nerpa_coat_of_plates_heavy_b,
      itm_m_nerpa_coat_of_plates_heavy_b_v1,
      itm_m_nerpa_coat_of_plates_heavy_b_v2,
      itm_nerpa_barbuta_mail_a,
      itm_nerpa_barbuta_mail_b,
      itm_military_cleaver_c,
      itm_tab_shield_pavise_d,
      itm_m_gloves_a,
      itm_m_gauntlets_b,
      itm_m_gauntlets_a,
      itm_mail_boots_a
    ],
    def_attrib|level(35),
    wp(240)|wp_one_handed(50),
    knows_common|knows_ironflesh_10|knows_power_strike_10|knows_athletics_8,
    swadian_face_old_1,
    swadian_face_old_2
  ],

  [
    "nerpa_ranger",
    "Nerpa Ranger",
    "Nerpa Rangers",
    tf_guarantee_all,
    0,
    0,
    fac_kingdom_7,
    [
      itm_m_nerpa_coat_of_plates_medium_a,
      itm_m_nerpa_coat_of_plates_medium_b,
      itm_nerpa_barbuta_open_padded_a,
      itm_nerpa_barbuta_open_padded_b,
      itm_sword_medieval_c_small,
      itm_war_darts,
      itm_tab_shield_pavise_c,
      itm_m_gloves_a,
      itm_leather_boots_a
    ],
    def_attrib|level(20),
    wp(120)|wp_throwing(50),
    knows_common|knows_ironflesh_3|knows_power_throw_4|knows_athletics_2,
    swadian_face_younger_1,
    swadian_face_middle_2
  ],

  [
    "nerpa_master_ranger",
    "Nerpa Master Ranger",
    "Nerpa Master Rangers",
    tf_guarantee_all,
    0,
    0,
    fac_kingdom_7,
    [
      itm_m_nerpa_coat_of_plates_heavy_a,
      itm_m_nerpa_coat_of_plates_heavy_b,
      itm_nerpa_barbuta_mail_a,
      itm_nerpa_barbuta_mail_b,
      itm_sword_medieval_c_small,
      itm_throwing_spears,
      itm_tab_shield_pavise_c,
      itm_m_gloves_a,
      itm_mail_boots_a
    ],
    def_attrib|level(25),
    wp(150)|wp_throwing(50),
    knows_common|knows_ironflesh_5|knows_power_throw_7|knows_athletics_4,
    swadian_face_old_1,
    swadian_face_old_2
  ],

  # hairako
  [
    "hairako_nomad",
    "Hairako Nomad",
    "Hairako Nomads",
    tf_guarantee_armor|tf_guarantee_boots,
    0,
    0,
    fac_kingdom_8,
    [
      itm_hairako_long_coat_a,
      itm_hairako_long_coat_b,
      itm_leather_covered_round_shield,
      itm_m_plain_round_shield_a,
      itm_tab_shield_round_a,
      itm_scimitar,
      itm_scimitar_b,
      itm_straight_falchion,
      itm_mace_1,
      itm_hose_d,
      itm_poulaines_d
    ],
    def_attrib|level(5),
    wp(60),
    knows_common,
    khergit_face_young_1,
    khergit_face_young_2
  ],

  [
    "hairako_footman",
    "Hairako Footman",
    "Hairako Footmans",
    tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_shield,
    0,
    0,
    fac_kingdom_8,
    [
      itm_hairako_fur_hat_a,
      itm_hairako_fur_hat_b,
      itm_hairako_helmet_a,
      itm_hairako_helmet_b,
      itm_hairako_helmet_c,
      itm_hairako_long_coat_c,
      itm_hairako_long_coat_d,
      itm_hairako_long_coat_a,
      itm_hairako_long_coat_b,
      itm_leather_gloves,
      itm_old_leather_gloves,
      itm_tab_shield_tauria_a,
      itm_arabian_sword_a,
      itm_arabian_sword_b,
      itm_war_spear,
      itm_straight_falchion,
      itm_mace_2,
      itm_mace_3,
      itm_hose_d,
      itm_poulaines_d
    ],
    def_attrib|level(10),
    wp(90),
    knows_common,
    khergit_face_young_1,
    khergit_face_young_2
  ],

  [
    "hairako_infantry",
    "Hairako Infantry",
    "Hairako Infantries",
    tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_shield,
    0,
    0,
    fac_kingdom_8,
    [
      itm_hairako_fur_hat_a,
      itm_hairako_fur_hat_b,
      itm_hairako_helmet_a,
      itm_hairako_helmet_b,
      itm_hairako_helmet_c,
      itm_hairako_nasal_helmet_a,
      itm_hairako_nasal_helmet_b,
      itm_hairako_infantry_vest_a,
      itm_hairako_infantry_vest_b,
      itm_hairako_infantry_vest_c,
      itm_leather_gloves,
      itm_old_leather_gloves,
      itm_decorated_leather_gloves_a,
      itm_old_mail_gloves,
      itm_tab_shield_tauria_a,
      itm_sarranid_cavalry_sword,
      itm_arabian_sword_b,
      itm_war_spear,
      itm_mace_4,
      itm_mace_3,
      itm_desert_leather_boots_a
    ],
    def_attrib|level(15),
    wp(120),
    knows_common,
    khergit_face_young_1,
    khergit_face_young_2
  ],

  [
    "hairako_infantry_veteran",
    "Hairako Infantry Veteran",
    "Hairako Infantry Veterans",
    tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,
    0,
    0,
    fac_kingdom_8,
    [
      itm_hairako_nasal_helmet_a,
      itm_hairako_nasal_helmet_b,
      itm_hairako_nasal_helmet_c,
      itm_hairako_nasal_helmet_d,
      itm_hairako_nasal_helmet_e,
      itm_hairako_infantry_vest_d,
      itm_hairako_infantry_vest_c,
      itm_hairako_long_coat_mail_a,
      itm_hairako_long_coat_mail_b,
      itm_m_gloves_a,
      itm_mail_mittens,
      itm_decorated_leather_gloves_a,
      itm_old_mail_gloves,
      itm_tab_shield_tauria_a,
      itm_sarranid_cavalry_sword,
      itm_arabian_sword_d,
      itm_battle_trident,
      itm_ranseur,
      itm_mace_4,
      itm_mace_3,
      itm_desert_leather_boots_a,
      itm_desert_leather_boots_b
    ],
    def_attrib|level(20),
    wp(150),
    knows_common|knows_athletics_5|knows_power_strike_4,
    khergit_face_middle_1,
    khergit_face_old_2
  ],

  [
    "hairako_shaitan",
    "Hairako Shaitan",
    "Hairako Shaitans",
    tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,
    0,
    0,
    fac_kingdom_8,
    [
      itm_hairako_helmet_b,
      itm_hairako_mail_helmet_a,
      itm_hairako_mail_helmet_b,
      itm_hairako_nasal_helmet_d,
      itm_hairako_nasal_helmet_e,
      itm_hairako_full_helmet_a,
      itm_hairako_full_helmet_b,
      itm_hairako_full_helmet_c,
      itm_hairako_full_mail_a,
      itm_hairako_full_mail_b,
      itm_m_gloves_a,
      itm_mail_mittens,
      itm_eastern_scale_gloves_b,
      itm_eastern_scale_gloves_a,
      itm_tab_shield_tauria_b,
      itm_sarranid_cavalry_sword,
      itm_arabian_sword_d,
      itm_arabian_sword_c,
      itm_battle_trident,
      itm_ranseur,
      itm_desert_heavy_boots_a,
      itm_desert_heavy_boots_b
    ],
    def_attrib|level(25),
    wp(180),
    knows_common|knows_athletics_10|knows_power_strike_9|knows_ironflesh_10,
    khergit_face_middle_1,
    khergit_face_old_2
  ],

  [
    "hairako_rider",
    "Hairako Rider",
    "Hairako Riders",
    tf_mounted|tf_guarantee_horse|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_gloves,
    0,
    0,
    fac_kingdom_8,
    [
      itm_hairako_fur_hat_a,
      itm_hairako_fur_hat_b,
      itm_hairako_helmet_a,
      itm_hairako_helmet_b,
      itm_hairako_helmet_c,
      itm_hairako_long_coat_mail_a,
      itm_hairako_long_coat_mail_b,
      itm_leather_gloves,
      itm_old_leather_gloves,
      itm_decorated_leather_gloves_a,
      itm_old_mail_gloves,
      itm_tab_shield_tauria_a,
      itm_sarranid_cavalry_sword,
      itm_arabian_sword_b,
      itm_solarian_lance_a,
      itm_solarian_lance_b,
      itm_solarian_lance_c,
      itm_solarian_lance_d,
      itm_steppe_horse,
      itm_desert_leather_boots_a,
      itm_desert_leather_boots_b
    ],
    def_attrib|level(15),
    wp(120),
    knows_common|knows_riding_4,
    khergit_face_young_1,
    khergit_face_young_2
  ],

  [
    "hairako_experienced_rider",
    "Hairako Experienced Rider",
    "Hairako Experienced Riders",
    tf_mounted|tf_guarantee_horse|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_gloves,
    0,
    0,
    fac_kingdom_8,
    [
      itm_hairako_nasal_helmet_a,
      itm_hairako_nasal_helmet_b,
      itm_hairako_nasal_helmet_c,
      itm_hairako_long_coat_scale_a,
      itm_hairako_long_coat_scale_b,
      itm_mail_mittens,
      itm_old_mail_gloves,
      itm_decorated_leather_gloves_a,
      itm_tab_shield_tauria_a,
      itm_sarranid_cavalry_sword,
      itm_arabian_sword_b,
      itm_solarian_lance_a,
      itm_solarian_lance_b,
      itm_solarian_lance_c,
      itm_solarian_lance_d,
      itm_steppe_horse,
      itm_steppe_horse_b,
      itm_desert_leather_boots_a,
      itm_desert_leather_boots_b
    ],
    def_attrib|level(20),
    wp(150),
    knows_common|knows_riding_5|knows_ironflesh_4,
    khergit_face_old_1,
    khergit_face_old_2
  ],

  [
    "hairako_mounted_shaitan",
    "Hairako Mounted Shaitan",
    "Hairako Mounted Shaitans",
    tf_mounted|tf_guarantee_horse|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_gloves,
    0,
    0,
    fac_kingdom_8,
    [
      itm_hairako_mail_helmet_a,
      itm_hairako_mail_helmet_b,
      itm_hairako_mail_helmet_c,
      itm_hairako_mail_helmet_d,
      itm_hairako_long_coat_scale_c,
      itm_hairako_long_coat_scale_d,
      itm_hairako_full_mail_a,
      itm_hairako_full_mail_b,
      itm_mail_mittens,
      itm_old_mail_gloves,
      itm_eastern_scale_gloves_a,
      itm_eastern_scale_gloves_b,
      itm_tab_shield_tauria_b,
      itm_sarranid_cavalry_sword,
      itm_arabian_sword_b,
      itm_arabian_sword_c,
      itm_solarian_lance_a,
      itm_solarian_lance_b,
      itm_solarian_lance_c,
      itm_solarian_lance_d,
      itm_horseman_poleaxe_a,
      itm_horseman_poleaxe_b,
      itm_steppe_horse_b,
      itm_steppe_horse_c,
      itm_steppe_horse_d,
      itm_desert_heavy_boots_a,
      itm_desert_heavy_boots_b
    ],
    def_attrib|level(25),
    wp(180),
    knows_common|knows_riding_8|knows_ironflesh_10|knows_power_strike_7,
    khergit_face_old_1,
    khergit_face_old_2
  ],

  [
    "hairako_archer",
    "Hairako Archer",
    "Hairako Archers",
    tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,
    0,
    0,
    fac_kingdom_8,
    [
      itm_hairako_fur_hat_a,
      itm_hairako_fur_hat_b,
      itm_hairako_helmet_b,
      itm_hairako_helmet_a,
      itm_hairako_helmet_c,
      itm_hairako_long_coat_a,
      itm_hairako_long_coat_b,
      itm_tab_shield_tauria_a,
      itm_scimitar,
      itm_scimitar_b,
      itm_straight_falchion,
      itm_mace_1,
      itm_sword_khergit_1,
      itm_strong_bow,
      itm_arrows,
      itm_desert_leather_boots_a,
      itm_desert_leather_boots_b
    ],
    def_attrib|level(10),
    wp(90)|wp_archery(50),
    knows_common|knows_power_draw_4,
    khergit_face_young_1,
    khergit_face_young_2
  ],

  [
    "hairako_sniper",
    "Hairako Sniper",
    "Hairako Snipers",
    tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,
    0,
    0,
    fac_kingdom_8,
    [
      itm_hairako_fur_hat_a,
      itm_hairako_fur_hat_b,
      itm_hairako_helmet_b,
      itm_hairako_nasal_helmet_e,
      itm_hairako_infantry_vest_a,
      itm_hairako_infantry_vest_b,
      itm_tab_shield_tauria_a,
      itm_arabian_sword_a,
      itm_arabian_sword_b,
      itm_mace_2,
      itm_ranseur,
      itm_strong_bow,
      itm_arrows,
      itm_desert_leather_boots_a,
      itm_desert_leather_boots_b
    ],
    def_attrib|level(15),
    wp(120)|wp_archery(50),
    knows_common|knows_power_draw_6,
    khergit_face_young_1,
    khergit_face_young_2
  ],

  [
    "hairako_sniper_elite",
    "Hairako Sniper Elite",
    "Hairako Sniper Elites",
    tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,
    0,
    0,
    fac_kingdom_8,
    [
      itm_hairako_nasal_helmet_e,
      itm_hairako_mail_helmet_a,
      itm_hairako_mail_helmet_d,
      itm_hairako_infantry_vest_d,
      itm_tab_shield_tauria_a,
      itm_tab_shield_tauria_b,
      itm_arabian_sword_d,
      itm_arabian_sword_c,
      itm_ranseur,
      itm_battle_trident,
      itm_strong_bow,
      itm_arrows,
      itm_barbed_arrows,
      itm_desert_heavy_boots_a,
      itm_desert_heavy_boots_b
    ],
    def_attrib|level(20),
    wp(180)|wp_archery(50),
    knows_common|knows_power_draw_9|knows_athletics_5|knows_ironflesh_4,
    khergit_face_old_1,
    khergit_face_old_2
  ],

  # tauria
  # TODO: battle priest and spearman/helbardier
  [
    "tauria_recruit",
    "Tauria Recruit",
    "Tauria Recruits",
    tf_guarantee_armor|tf_guarantee_boots,
    0,
    0,
    fac_kingdom_9,
    [
      itm_m_tauria_vest_a,
      itm_m_tauria_vest_b,
      itm_m_coif_cloth_a,
      itm_m_coif_cloth_b,
      itm_tab_shield_tauria_a,
      itm_falchion,
      itm_hatchet,
      itm_boar_spear,
      itm_scythe,
      itm_mace_1,
      itm_poulaines_d,
      itm_hose_d
    ],
    def_attrib|level(5),
    wp(60),
    knows_common,
    swadian_face_young_1,
    swadian_face_young_2
  ],

  [
    "tauria_trooper",
    "Tauria Trooper",
    "Tauria Troopers",
    tf_guarantee_armor|tf_guarantee_boots,
    0,
    0,
    fac_kingdom_9,
    [
      itm_m_tauria_vest_a,
      itm_m_tauria_vest_b,
      itm_m_tauria_vest_medium_a,
      itm_m_tauria_plate_a,
      itm_m_tauria_plate_a_v1,
      itm_leather_gloves,
      itm_m_coif_cloth_a,
      itm_m_coif_cloth_b,
      itm_mail_coif ,
      itm_tab_shield_tauria_a,
      itm_boar_spear,
      itm_falchion,
      itm_voulge,
      itm_crusader_sword_a,
      itm_crusader_sword_b,
      itm_poulaines_d,
      itm_hose_d,
      itm_leather_shoes_a,
      itm_leather_shoes_b
    ],
    def_attrib|level(10),
    wp(90),
    knows_common,
    swadian_face_young_1,
    swadian_face_young_2
  ],

  [
    "tauria_soldier",
    "Tauria Soldier",
    "Tauria Soldiers",
    tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,
    0,
    0,
    fac_kingdom_9,
    [
      itm_m_tauria_plate_b,
      itm_m_tauria_plate_a,
      itm_m_tauria_vest_medium_a,
      itm_leather_gloves,
      itm_old_mail_gloves,
      itm_m_gloves_a,
      itm_mail_coif,
      itm_m_flat_top_a,
      itm_tab_shield_tauria_a,
      itm_crusader_spear_a,
      itm_axe_crusader_a,
      itm_crusader_sword_a,
      itm_crusader_sword_b,
      itm_winged_mace,
      itm_leather_boots_a
    ],
    def_attrib|level(15),
    wp(120),
    knows_common,
    swadian_face_young_1,
    swadian_face_young_2
  ],

  [
    "tauria_foot_knight",
    "Tauria Foot Knight",
    "Tauria Foot Knights",
    tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,
    0,
    0,
    fac_kingdom_9,
    [
      itm_m_tauria_plate_mail_a,
      itm_m_tauria_plate_mail_a_v1,
      itm_m_tauria_plate_c,
      itm_m_tauria_vest_heavy_a,
      itm_leather_gloves,
      itm_old_mail_gloves,
      itm_m_gloves_a,
      itm_m_pepperpot_b,
      itm_m_pepperpot_c,
      itm_tab_shield_tauria_a,
      itm_tab_shield_tauria_b,
      itm_crusader_spear_a,
      itm_crusader_spear_b,
      itm_axe_crusader_a,
      itm_axe_crusader_b,
      itm_crusader_sword_a,
      itm_crusader_long_sword_b,
      itm_winged_mace,
      itm_flanged_mace,
      itm_leather_boots_a,
      itm_mail_boots_a
    ],
    def_attrib|level(20),
    wp(150),
    knows_common,
    swadian_face_young_1,
    swadian_face_young_2
  ],

  [
    "tauria_sword_master",
    "Tauria Sword Master",
    "Tauria Sword Masters",
    tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,
    0,
    0,
    fac_kingdom_9,
    [
      itm_m_tauria_plate_c,
      itm_m_tauria_plate_mail_a,
      itm_m_tauria_vest_heavy_a,
      itm_m_tauria_vest_heavy_b,
      itm_old_mail_gloves,
      itm_m_gloves_a,
      itm_m_pepperpot_a,
      itm_m_pepperpot_d,
      itm_m_munitions_helm_b,
      itm_tab_shield_tauria_a,
      itm_tab_shield_tauria_b,
      itm_crusader_spear_a,
      itm_crusader_spear_b,
      itm_axe_crusader_1,
      itm_axe_crusader_b,
      itm_crusader_long_sword_b,
      itm_winged_mace,
      itm_flanged_mace,
      itm_m_war_hammer_a,
      itm_guisarme,
      itm_leather_boots_a,
      itm_mail_boots_a,
      itm_mail_boots_b      
    ],
    def_attrib|level(25),
    wp(180),
    knows_common,
    swadian_face_young_1,
    swadian_face_young_2
  ],

  [
    "tauria_man_at_arms",
    "Tauria Man-at-Arms",
    "Tauria Men-at-Arms",
    tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,
    0,
    0,
    fac_kingdom_9,
    [
      itm_m_tauria_plate_c,
      itm_m_tauria_plate_mail_b,
      itm_m_tauria_brigandine_a,
      itm_m_tauria_vest_heavy_b,
      itm_old_mail_gloves,
      itm_m_gloves_a,
      itm_m_gauntlets_b,
      itm_m_munitions_helm_a,
      itm_m_pepperpot_d,
      itm_tab_shield_tauria_c,
      itm_tab_shield_tauria_b,
      itm_crusader_spear_b,
      itm_crusader_spear_c,
      itm_axe_crusader_1,
      itm_axe_crusader_c,
      itm_crusader_long_sword_c,
      itm_k_long_sword_a,
      itm_m_pole_hammer_b,
      itm_flanged_mace,
      itm_m_war_hammer_a,
      itm_guisarme,
      itm_english_bill,
      itm_mail_boots_a,
      itm_mail_boots_b,
      itm_plate_boots_b
    ],
    def_attrib|level(30),
    wp(210),
    knows_common|knows_ironflesh_7|knows_power_strike_7,
    swadian_face_old_1,
    swadian_face_old_2
  ],

  [
    "tauria_horseman",
    "Tauria Horseman",
    "Tauria Horsemans",
    tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_shield|tf_mounted|tf_guarantee_horse,
    0,
    0,
    fac_kingdom_9,
    [
      itm_m_tauria_plate_b,
      itm_m_tauria_plate_a,
      itm_m_tauria_plate_a_v1,
      itm_m_tauria_vest_medium_a,
      itm_leather_gloves,
      itm_old_mail_gloves,
      itm_m_gloves_a,
      itm_mail_coif,
      itm_tab_shield_tauria_a,
      itm_lance,
      itm_axe_crusader_a,
      itm_crusader_sword_a,
      itm_crusader_sword_b,
      itm_winged_mace,
      itm_hunter,
      itm_leather_boots_a,
      itm_mail_boots_a,
      itm_mail_boots_b
    ],
    def_attrib|level(20),
    wp(150),
    knows_common|knows_riding_3,
    swadian_face_young_1,
    swadian_face_young_2
  ],

  [
    "tauria_knight",
    "Tauria Knight",
    "Tauria Knights",
    tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_shield|tf_mounted|tf_guarantee_horse|tf_guarantee_gloves,
    0,
    0,
    fac_kingdom_9,
    [
      itm_m_tauria_plate_c,
      itm_m_tauria_plate_mail_a,
      itm_m_tauria_plate_mail_a_v1,
      itm_m_tauria_vest_heavy_a,
      itm_m_tauria_vest_heavy_b,
      itm_old_mail_gloves,
      itm_m_gloves_a,
      itm_m_pepperpot_a,
      itm_m_pepperpot_d,
      itm_m_munitions_helm_b,
      itm_tab_shield_tauria_a,
      itm_tab_shield_tauria_b,
      itm_axe_crusader_1,
      itm_axe_crusader_b,
      itm_crusader_long_sword_b,
      itm_winged_mace,
      itm_flanged_mace,
      itm_lance,
      itm_mt_horse_c6,
      itm_mt_horse_c7,
      itm_mt_horse_c8,
      itm_mt_horse_c9,
      itm_mt_horse_c10,
      itm_mail_boots_a,
      itm_mail_boots_b,
      itm_mail_boots_c
    ],
    def_attrib|level(25),
    wp(180),
    knows_common|knows_riding_5|knows_ironflesh_4,
    swadian_face_young_1,
    swadian_face_young_2
  ],

  [
    "tauria_noble_knight",
    "Tauria Noble Knight",
    "Tauria Noble Knights",
    tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_shield|tf_mounted|tf_guarantee_horse|tf_guarantee_gloves,
    0,
    0,
    fac_kingdom_9,
    [
      itm_m_tauria_plate_mail_a,
      itm_m_tauria_plate_mail_a_v1,
      itm_m_tauria_plate_mail_b,
      itm_old_mail_gloves,
      itm_m_gloves_a,
      itm_m_pepperpot_a,
      itm_m_pepperpot_d,
      itm_m_munitions_helm_b,
      itm_tab_shield_tauria_a,
      itm_tab_shield_tauria_b,
      itm_axe_crusader_1,
      itm_crusader_long_sword_a,
      itm_crusader_long_sword_b,
      itm_winged_mace,
      itm_flanged_mace,
      itm_lance,
      itm_mt_horse_c11,
      itm_plate_boots_b,
      itm_plate_boots_a
    ],
    def_attrib|level(30),
    wp(210)|wp_melee(50),
    knows_common|knows_riding_8|knows_ironflesh_10|knows_power_strike_10,
    swadian_face_old_1,
    swadian_face_old_2
  ],

  [
    "tauria_crossbowman",
    "Tauria Crossbowman",
    "Tauria Crossbowmans",
    tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,
    0,
    0,
    fac_kingdom_9,
    [
      itm_m_tauria_vest_a,
      itm_m_tauria_vest_b,
      itm_m_coif_cloth_a,
      itm_m_coif_cloth_b,
      itm_tab_shield_tauria_a,
      itm_winged_mace,
      itm_flanged_mace,
      itm_axe_crusader_b,
      itm_heavy_crossbow,
      itm_bolts,
      itm_poulaines_d,
      itm_hose_d
    ],
    def_attrib|level(15),
    wp(120)|wp_crossbow(50),
    knows_common,
    swadian_face_young_1,
    swadian_face_young_2
  ],

  [
    "tauria_siege_crossbowman",
    "Tauria Siege Crossbowman",
    "Tauria Siege Crossbowmans",
    tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,
    0,
    0,
    fac_kingdom_9,
    [
      itm_m_tauria_vest_a,
      itm_m_tauria_vest_b,
      itm_mail_coif,
      itm_m_coif_cloth_a,
      itm_m_coif_cloth_b,
      itm_tab_shield_tauria_a,
      itm_tab_shield_tauria_b,
      itm_winged_mace,
      itm_flanged_mace,
      itm_axe_crusader_b,
      itm_falshion_1,
      itm_axe_crusader_c,
      itm_heavy_crossbow,
      itm_sniper_crossbow,
      itm_bolts,
      itm_leather_boots_a,
    ],
    def_attrib|level(20),
    wp(150)|wp_crossbow(50),
    knows_common,
    swadian_face_middle_1,
    swadian_face_old_2
  ],

  # elen
  [
    "elen_novice",
    "Elen Novice",
    "Elen Novices",
    tf_guarantee_armor|tf_guarantee_boots,
    0,
    0,
    fac_kingdom_10,
    [
      itm_m_elen_leather_vest_a,
      itm_m_elen_leather_vest_b,
      itm_arming_cap,
      itm_elen_nasal_a,
      itm_leather_gloves,
      itm_mace_1,
      itm_hand_axe,
      itm_spear,
      itm_tab_shield_tauria_a,
      itm_hose_b,
      itm_poulaines_b
    ],
    def_attrib|level(5),
    wp(60),
    knows_common|swadian_face_young_1,
    swadian_face_young_2
  ],

  [
    "elen_footman",
    "Elen Footman",
    "Elen Footmen",
    tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet,
    0,
    0,
    fac_kingdom_10,
    [
      itm_m_elen_leather_vest_a,
      itm_m_elen_leather_vest_b,
      itm_m_elen_vest_a,
      itm_elen_nasal_a,
      itm_elen_nasal_b,
      itm_leather_gloves,
      itm_falchion,
      itm_flanged_mace,
      itm_military_scythe,
      itm_fighting_axe,
      itm_tab_shield_tauria_a,
      itm_hose_b,
      itm_poulaines_b
    ],
    def_attrib|level(10),
    wp(90),
    knows_common|swadian_face_young_1,
    swadian_face_young_2
  ],

  [
    "elen_fighter",
    "Elen Fighter",
    "Elen Fighters",
    tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_shield,
    0,
    0,
    fac_kingdom_10,
    [
      itm_m_elen_vest_a,
      itm_m_elen_vest_b,
      itm_elen_nasal_a,
      itm_elen_nasal_b,
      itm_elen_nasal_padded_a,
      itm_leather_gloves,
      itm_m_gloves_a,
      itm_crusader_sword_a,
      itm_crusader_sword_b,
      itm_glaive_a,
      itm_glaive_b,
      itm_partisan,
      itm_tab_shield_tauria_a,
      itm_hose_b,
      itm_poulaines_b,
      itm_leather_boots_a
    ],
    def_attrib|level(15),
    wp(120),
    knows_common|knows_ironflesh_2,
    swadian_face_young_1,
    swadian_face_young_2
  ],

  [
    "elen_light_infantry",
    "Elen Light Infantry",
    "Elen Light Infantries",
    tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,
    0,
    0,
    fac_kingdom_10,
    [
      itm_m_elen_leather_vest_a,
      itm_m_elen_leather_vest_b,
      itm_m_elen_vest_c,
      itm_m_elen_vest_d,
      itm_m_elen_vest_e,
      itm_elen_nasal_padded_a,
      itm_elen_nasal_padded_b,
      itm_m_gloves_a,
      itm_old_mail_gloves,
      itm_mail_mittens,
      itm_crusader_sword_b,
      itm_flanged_mace,
      itm_winged_mace,
      itm_m_glaive_b,
      itm_military_scythe,
      itm_crusader_spear_inf_a,
      itm_tab_shield_tauria_a,
      itm_leather_boots_a,
      itm_leather_boots_b,
      itm_mail_boots_a
    ],
    def_attrib|level(20),
    wp(150),
    knows_common|knows_ironflesh_3,
    swadian_face_young_1,
    swadian_face_young_2
  ],

  [
    "elen_heavy_infantry",
    "Elen Heavy Infantry",
    "Elen Heavy Infantries",
    tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,
    0,
    0,
    fac_kingdom_10,
    [
      itm_m_elen_lamellar_a,
      itm_m_elen_lamellar_b,
      itm_m_elen_lamellar_c,
      itm_m_elen_lamellar_d,
      itm_elen_plated_lamellar_a,
      itm_elen_plated_lamellar_b,
      itm_elen_plated_lamellar_c,
      itm_elen_full_lamellar_a,
      itm_elen_full_lamellar_b,
      itm_elen_nasal_mail_a,
      itm_elen_nasal_mail_b,
      itm_elen_nasal_mail_c,
      itm_elen_masked_helmet_a,
      itm_elen_masked_helmet_b,
      itm_m_gloves_a,
      itm_old_mail_gloves,
      itm_mail_mittens,
      itm_m_gauntlets_b,
      itm_crusader_long_sword_a,
      itm_m_one_handed_knight_axe_a,
      itm_heavy_infantry_axe,
      itm_m_one_handed_knight_axe_b,
      itm_strange_winged_mace,
      itm_winged_mace,
      itm_m_glaive_b,
      itm_m_glaive_a,
      itm_crusader_spear_inf_b,
      itm_tab_shield_tauria_a,
      itm_mail_boots_a,
      itm_mail_boots_b,
      itm_plate_boots_a,
      itm_plate_boots_b
    ],
    def_attrib|level(25),
    wp(180),
    knows_common|knows_ironflesh_5|knows_power_strike_5,
    swadian_face_young_1,
    swadian_face_young_2
  ],

  [
    "elen_cheif",
    "Elen Cheif",
    "Elen Cheifs",
    tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_horse,
    0,
    0,
    fac_kingdom_10,
    [
      itm_m_elen_plated_leather_a,
      itm_m_elen_plated_leather_b,
      itm_m_elen_plated_leather_b,
      itm_elen_great_helm_a,
      itm_elen_great_helm_b,
      itm_elen_great_helm_c,
      itm_mt_gauntlets_a,
      itm_mt_gauntlets_b,
      itm_old_mail_gloves,
      itm_mail_mittens,
      itm_crusader_long_sword_a,
      itm_crusader_long_sword_b,
      itm_m_one_handed_knight_axe_a,
      itm_m_two_handed_knight_axe_b,
      itm_crusader_knight_spear_a,
      itm_crusader_knight_spear_b,
      itm_tab_shield_tauria_a,
      itm_elen_warhorse_a,
      itm_elen_warhorse_b,
      itm_mail_boots_a,
      itm_mail_boots_b,
      itm_plate_boots_a,
      itm_plate_boots_b
    ],
    tier_two_attrib|level(30),
    wp(210),
    knows_common|knows_ironflesh_9|knows_power_strike_9|knows_riding_8,
    swadian_face_young_1,
    swadian_face_young_2
  ],

  [
    "elen_archer",
    "Elen Archer",
    "Elen Archers",
    tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_ranged,
    0,
    0,
    fac_kingdom_10,
    [
      itm_m_elen_leather_vest_a,
      itm_m_elen_leather_vest_b,
      itm_elen_nasal_a,
      itm_elen_nasal_b,
      itm_leather_gloves,
      itm_mace_1,
      itm_hand_axe,
      itm_arrows,
      itm_hunting_bow,
      itm_leather_boots_a,
      itm_leather_boots_b,
      itm_hose_b,
      itm_poulaines_b
    ],
    def_attrib|level(15),
    wp(120)|wp_archery(50),
    knows_common|knows_ironflesh_2|knows_power_draw_3,
    swadian_face_young_1,
    swadian_face_young_2
  ],

  [
    "elen_experienced_archer",
    "Elen Experienced Archer",
    "Elen Experienced Archers",
    tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_ranged,
    0,
    0,
    fac_kingdom_10,
    [
      itm_m_elen_vest_a,
      itm_elen_leather_armor_a,
      itm_elen_leather_armor_b,
      itm_elen_nasal_a,
      itm_elen_nasal_b,
      itm_leather_gloves,
      itm_falchion,
      itm_flanged_mace,
      itm_fighting_axe,
      itm_arrows,
      itm_long_bow,
      itm_leather_boots_a,
      itm_leather_boots_b,
      itm_hose_b,
      itm_poulaines_b
    ],
    def_attrib|level(20),
    wp(150)|wp_archery(50),
    knows_common|knows_ironflesh_2|knows_power_draw_4,
    swadian_face_young_1,
    swadian_face_young_2
  ],

  [
    "elen_sniper",
    "Elen Sniper",
    "Elen Snipers",
    tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_ranged,
    0,
    0,
    fac_kingdom_10,
    [
      itm_m_elen_vest_a,
      itm_elen_leather_armor_a,
      itm_elen_leather_armor_b,
      itm_elen_nasal_padded_a,
      itm_elen_nasal_padded_b,
      itm_leather_gloves,
      itm_falchion,
      itm_flanged_mace,
      itm_crusader_sword_b,
      itm_crusader_sword_a,
      itm_tab_shield_pavise_b,
      itm_tab_shield_pavise_c,
      itm_crossbow,
      itm_bolts,
      itm_leather_boots_a,
      itm_leather_boots_b,
      itm_mail_boots_a,
      itm_mail_boots_b
    ],
    def_attrib|level(20),
    wp(150)|wp_crossbow(70),
    knows_common|knows_ironflesh_2|knows_power_strike_2,
    swadian_face_young_1,
    swadian_face_young_2
  ],

  # Adid units
  # Nomad Scout - Desert Vanguard - Sultanate Vanguard
  [
    "adid_nomad_scout",
    "Adid Nomad Scout",
    "Adid Nomad Scouts",
    tf_guarantee_boots|tf_guarantee_armor,
    0,
    0,
    fac_kingdom_11,
    [
      itm_solarian_turban_c,
      itm_m_bandit_turban_a,
      itm_m_bandit_turban_b,
      itm_m_desert_bandit_a,
      itm_old_leather_gloves,
      itm_spiked_club,
      itm_falshion_1,
      itm_falshion_2,
      itm_long_spiked_club,
      itm_tab_shield_tauria_a,
      itm_leather_shoes_a,
      itm_leather_shoes_b,
      itm_leather_shoes_c
    ],
    def_attrib|level(5),
    wp(60),
    knows_common,
    swadian_face_younger_1,
    swadian_face_middle_2
  ],

  [
    "adid_desert_vanguard",
    "Adid Desert Vanguard",
    "Adid Desert Vanguards",
    tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
    0,
    0,
    fac_kingdom_11,
    [
      itm_m_bandit_turban_c,
      itm_m_bandit_turban_d,
      itm_solarian_turban_c,
      itm_m_desert_bandit_d,
      itm_m_desert_bandit_c,
      itm_old_leather_gloves,
      itm_leather_gloves,
      itm_scimitar,
      itm_falshion_1,
      itm_falshion_2,
      itm_eastern_falchion,
      itm_voulge_short,
      itm_spear,
      itm_tab_shield_tauria_a,
      itm_leather_shoes_a,
      itm_leather_shoes_b,
      itm_leather_shoes_c
    ],
    def_attrib|level(10),
    wp(90),
    knows_common,
    swadian_face_young_1,
    swadian_face_middle_2
  ],

  [
    "adid_sultanate_vanguard",
    "Adid Sultanate Vanguard",
    "Adid Sultanate Vanguards",
    tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,
    0,
    0,
    fac_kingdom_11,
    [
      itm_adid_helmet_a,
      itm_adid_helmet_b,
      itm_adid_helmet_c,
      itm_m_desert_bandit_b,
      itm_m_desert_bandit_c,
      itm_decorated_leather_gloves_a,
      itm_leather_gloves,
      itm_m_gloves_a,
      itm_m_scimitar_a,
      itm_falshion_1,
      itm_falshion_2,
      itm_eastern_falchion,
      itm_hafted_blade_a,
      itm_hafted_blade_b,
      itm_hafted_blade_c,
      itm_hafted_blade_d,
      itm_hafted_blade_e,
      itm_hafted_blade_f,
      itm_tab_shield_tauria_a,
      itm_leather_shoes_a,
      itm_leather_shoes_b,
      itm_leather_shoes_c
    ],
    def_attrib|level(15),
    wp(120),
    knows_common,
    swadian_face_young_1,
    swadian_face_middle_2
  ],

  # Sultanate Vanguard - Camel Rider - Sandstalker
  [
    "adid_camel_rider",
    "Adid Camel Rider",
    "Adid Camel Riders",
    tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves|tf_mounted|tf_guarantee_horse|tf_guarantee_ranged,
    0,
    0,
    fac_kingdom_11,
    [
      itm_m_bandit_turban_a,
      itm_m_bandit_turban_b,
      itm_m_desert_bandit_a,
      itm_old_leather_gloves,
      itm_falshion_1,
      itm_falshion_2,
      itm_nomad_bow,
      itm_arrows,
      itm_maa_camel_light_c,
      itm_maa_camel_light_d,
      itm_tab_shield_tauria_a,
      itm_leather_shoes_a,
      itm_leather_shoes_b,
      itm_leather_shoes_c
    ],
    def_attrib|level(20),
    wp(150)|wp_archery(50),
    knows_common|knows_riding_5|knows_horse_archery_5,
    swadian_face_young_1,
    swadian_face_middle_2
  ],

  [
    "adid_sandstalker",
    "Adid Sandstalker",
    "Adid Sandstalkers",
    tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves|tf_mounted|tf_guarantee_horse|tf_guarantee_ranged,
    0,
    0,
    fac_kingdom_11,
    [
      itm_m_bandit_turban_a,
      itm_m_bandit_turban_b,
      itm_m_desert_bandit_a,
      itm_old_leather_gloves,
      itm_decorated_leather_gloves_a,
      itm_leather_gloves,
      itm_hafted_blade_a,
      itm_hafted_blade_b,
      itm_hafted_blade_c,
      itm_hafted_blade_d,
      itm_hafted_blade_e,
      itm_hafted_blade_f,
      itm_strong_bow,
      itm_barbed_arrows,
      itm_maa_camel_war_a,
      itm_maa_camel_war_b,
      itm_maa_camel_war_c,
      itm_maa_camel_war_d,
      itm_tab_shield_tauria_a,
      itm_light_leather_boots_a,
      itm_light_leather_boots_b,
      itm_light_leather_boots_c
    ],
    def_attrib|level(25),
    wp(180)|wp_archery(50),
    knows_common|knows_riding_5|knows_horse_archery_8,
    swadian_face_young_1,
    swadian_face_middle_2
  ],

  # Sultanate Vanguard - Serpent Guard - Oasis Acolyte
  [
    "adid_serpent_guard",
    "Adid Serpent Guard",
    "Adid Serpent Guards",
    tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,
    0,
    0,
    fac_kingdom_11,
    [
      itm_adid_helmet_a,
      itm_adid_helmet_b,
      itm_adid_helmet_c,
      itm_m_desert_bandit_b,
      itm_m_desert_bandit_c,
      itm_mail_mittens,
      itm_old_mail_gloves,
      itm_m_gloves_a,
      itm_m_scimitar_a,
      itm_strange_winged_mace,
      itm_strange_winged_mace_decorated,
      itm_falshion_2,
      itm_eastern_falchion,
      itm_hafted_blade_a,
      itm_hafted_blade_b,
      itm_hafted_blade_c,
      itm_hafted_blade_d,
      itm_hafted_blade_e,
      itm_hafted_blade_f,
      itm_tab_shield_tauria_a,
      itm_light_leather_boots_a,
      itm_light_leather_boots_b,
      itm_light_leather_boots_c
    ],
    def_attrib|level(20),
    wp(150)|wp_polearm(50),
    knows_common,
    swadian_face_young_1,
    swadian_face_middle_2
  ],

  [
    "adid_oasis_acolyte",
    "Adid Oasis Acolyte",
    "Adid Oasis Acolytes",
    tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,
    0,
    0,
    fac_kingdom_11,
    [
      itm_adid_helmet_a,
      itm_adid_helmet_b,
      itm_adid_helmet_c,
      itm_mkk_black_scale_a,
      itm_mkk_black_scale_b,
      itm_mkk_black_scale_c,
      itm_mail_mittens,
      itm_old_mail_gloves,
      itm_m_two_handed_ball_mace,
      itm_m_two_handed_flanged_mace,
      itm_falshion_2,
      itm_eastern_falchion,
      itm_hafted_blade_a,
      itm_hafted_blade_b,
      itm_hafted_blade_c,
      itm_hafted_blade_d,
      itm_hafted_blade_e,
      itm_hafted_blade_f,
      itm_battle_trident,
      itm_tab_shield_tauria_a,
      itm_light_leather_boots_a,
      itm_light_leather_boots_b,
      itm_light_leather_boots_c
    ],
    def_attrib|level(25),
    wp(180)|wp_polearm(50),
    knows_common|knows_ironflesh_4|knows_power_throw_4,
    swadian_face_young_1,
    swadian_face_middle_2
  ],

  # Oasis Acolyte - Oasis Priest - Oasis High Priest
  [
    "adid_oasis_priest",
    "Adid Oasis Priest",
    "Adid Oasis Priests",
    tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,
    0,
    0,
    fac_kingdom_11,
    [
      itm_adid_helmet_a,
      itm_adid_helmet_b,
      itm_adid_helmet_c,
      itm_mkk_black_scale_a,
      itm_mkk_black_scale_b,
      itm_mkk_black_scale_c,
      itm_mail_mittens,
      itm_old_mail_gloves,
      itm_eastern_scale_gloves_a,
      itm_eastern_scale_gloves_b,
      itm_falshion_2,
      itm_hafted_blade_a,
      itm_hafted_blade_b,
      itm_hafted_blade_c,
      itm_hafted_blade_d,
      itm_hafted_blade_e,
      itm_hafted_blade_f,
      itm_battle_trident,
      itm_eastern_round_shield_a,
      itm_eastern_round_shield_b,
      itm_eastern_round_shield_c,
      itm_throwing_spears,
      itm_light_leather_boots_a,
      itm_light_leather_boots_b,
      itm_light_leather_boots_c
    ],
    def_attrib|level(30),
    wp(210)|wp_polearm(50),
    knows_common|knows_ironflesh_9|knows_power_strike_5|knows_athletics_6|knows_power_throw_5,
    swadian_face_young_1,
    swadian_face_middle_2
  ],

  [
    "adid_oasis_high_priest",
    "Adid Oasis High Priest",
    "Adid Oasis High Priests",
    tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,
    0,
    0,
    fac_kingdom_11,
    [
      itm_adid_elite_helmet_a,
      itm_mkk_mamluke_a,
      itm_mkk_mamluke_b,
      itm_mkk_mamluke_c,
      itm_eastern_scale_gloves_a,
      itm_eastern_scale_gloves_b,
      itm_falshion_2,
      itm_arabian_sword_a,
      itm_arabian_sword_b,
      itm_hafted_blade_a,
      itm_hafted_blade_b,
      itm_hafted_blade_c,
      itm_hafted_blade_d,
      itm_hafted_blade_e,
      itm_hafted_blade_f,
      itm_battle_trident,
      itm_eastern_round_shield_a,
      itm_eastern_round_shield_b,
      itm_eastern_round_shield_c,
      itm_throwing_spears,
      itm_mail_boots_a,
      itm_mail_boots_b,
      itm_mail_boots_c
    ],
    def_attrib|level(35),
    wp(240)|wp_polearm(50),
    knows_common|knows_ironflesh_10|knows_power_strike_10|knows_athletics_6|knows_power_throw_7,
    swadian_face_young_1,
    swadian_face_middle_2
  ],

  # Oasis Acolyte - Royal Lancer - Golden Falcon
  [
    "adid_royal_lancer",
    "Adid Royal Lancer",
    "Adid Royal Lancers",
    tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves|tf_mounted|tf_guarantee_horse,
    0,
    0,
    fac_kingdom_11,
    [
      itm_adid_cavalry_helmet_a,
      itm_mkk_black_scale_a,
      itm_mkk_black_scale_b,
      itm_mkk_black_scale_c,
      itm_mail_mittens,
      itm_old_mail_gloves,
      itm_eastern_scale_gloves_a,
      itm_eastern_scale_gloves_b,
      itm_sarranid_cavalry_sword,
      itm_eastern_round_shield_a,
      itm_eastern_round_shield_b,
      itm_eastern_round_shield_c,
      itm_lance,
      itm_hafted_blade_a,
      itm_hafted_blade_b,
      itm_hafted_blade_c,
      itm_hafted_blade_d,
      itm_hafted_blade_e,
      itm_hafted_blade_f,
      itm_arabian_horse_a,
      itm_arabian_horse_b,
      itm_mail_boots_a,
      itm_mail_boots_b,
      itm_mail_boots_c
    ],
    def_attrib|level(30),
    wp(210),
    knows_common|knows_ironflesh_9|knows_power_strike_5|knows_riding_6,
    swadian_face_young_1,
    swadian_face_middle_2
  ],

  [
    "adid_golden_falcon",
    "Adid Golden Falcon",
    "Adid Golden Falcons",
    tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves|tf_mounted|tf_guarantee_horse,
    0,
    0,
    fac_kingdom_11,
    [
      itm_adid_cavalry_helmet_a,
      itm_mkk_mamluke_a,
      itm_mkk_mamluke_b,
      itm_mkk_mamluke_c,
      itm_mail_mittens,
      itm_old_mail_gloves,
      itm_eastern_scale_gloves_a,
      itm_eastern_scale_gloves_b,
      itm_sarranid_cavalry_sword,
      itm_sarranid_two_handed_axe_a,
      itm_sarranid_two_handed_axe_b,
      itm_eastern_round_shield_a,
      itm_eastern_round_shield_b,
      itm_eastern_round_shield_c,
      itm_lance,
      itm_hafted_blade_a,
      itm_hafted_blade_b,
      itm_hafted_blade_c,
      itm_hafted_blade_d,
      itm_hafted_blade_e,
      itm_hafted_blade_f,
      itm_arabian_horse_a,
      itm_arabian_horse_b,
      itm_arabian_horse_c,
      itm_arabian_horse_d,
      itm_mail_boots_a,
      itm_mail_boots_b,
      itm_mail_boots_c
    ],
    def_attrib|level(35),
    wp(240),
    knows_common|knows_ironflesh_10|knows_power_strike_7|knows_riding_8,
    swadian_face_young_1,
    swadian_face_middle_2
  ],

  # Stormguard units
  # Mountaineer - Thunderguard - Stormbringers - Avalanche Warriors
  [
    "stormguard_mountaineer",
    "Stormguard Mountaineer",
    "Stormguard Mountaineers",
    tf_guarantee_armor|tf_guarantee_boots,
    0,
    0,
    fac_kingdom_12,
    [
      itm_pilgrim_hood,
      itm_stormguard_aketon_a,
      itm_stormguard_aketon_a_v1,
      itm_stormguard_aketon_b,
      itm_leather_gloves,
      itm_hatchet,
      itm_falchion,
      itm_pickaxe,
      itm_tab_shield_tauria_a,
      itm_boar_spear,
      itm_poulaines_d
    ],
    def_attrib|level(5),
    wp(60),
    knows_common,
    swadian_face_younger_1,
    swadian_face_middle_2
  ],

  [
    "stormguard_thunderguard",
    "Stormguard Thunderguard",
    "Stormguard Thunderguards",
    tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_shield,
    0,
    0,
    fac_kingdom_12,
    [
      itm_stormguard_helmet_a,
      itm_stormguard_pointy_helmet_a,
      itm_stormguard_pointy_helmet_b,
      itm_stormguard_aketon_a,
      itm_stormguard_aketon_a_v1,
      itm_stormguard_aketon_b,
      itm_stormguard_aketon_b_v1,
      itm_stormguard_aketon_plated_a,
      itm_leather_gloves,
      itm_crusader_sword_a,
      itm_crusader_sword_b,
      itm_pickaxe,
      itm_tab_shield_tauria_a,
      itm_boar_spear,
      itm_broad_spear,
      itm_poulaines_d
    ],
    def_attrib|level(10),
    wp(90),
    knows_common,
    swadian_face_young_1,
    swadian_face_middle_2
  ],

  [
    "stormguard_stormbringer",
    "Srormguard Stormbringer",
    "Srormguard Stormbringers",
    tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_helmet,
    0,
    0,
    fac_kingdom_12,
    [
      itm_stormguard_helmet_b,
      itm_stormguard_helmet_c,
      itm_stormguard_pointy_helmet_c,
      itm_stormguard_pointy_helmet_d,
      itm_stormguard_pointy_helmet_e,
      itm_stormguard_aketon_plated_a,
      itm_stormguard_aketon_plated_a_v1,
      itm_stormguard_aketon_plated_a_v2,
      itm_stormguard_aketon_plated_b,
      itm_stormguard_aketon_plated_b_v1,
      itm_axe_crusader_a,
      itm_crusader_sword_a,
      itm_crusader_sword_b,
      itm_tab_shield_tauria_a,
      itm_tab_shield_heater_c,
      itm_two_handed_battle_axe_2,
      itm_leather_gloves,
      itm_m_gloves_a,
      itm_leather_boots_a,
    ],
    def_attrib|level(15),
    wp(120)|wp_two_handed(50),
    knows_common,
    swadian_face_young_1,
    swadian_face_middle_2
  ],

  [
    "stormguard_avalanche_warrior",
    "Stormguard Avalanche Warrior",
    "Stormguard Avalanche Warriors",
    tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_gloves,
    0,
    0,
    fac_kingdom_12,
    [
      itm_stormguard_pointy_helmet_d,
      itm_stormguard_pointy_helmet_e,
      itm_stormguard_helmet_c,
      itm_stormguard_pointy_helmet_mail_a,
      itm_stormguard_pointy_helmet_mail_b,
      itm_stormguard_aketon_plated_b,
      itm_stormguard_aketon_plated_b_v1,
      itm_stormguard_hauberk_a,
      itm_stormguard_hauberk_a_v1,
      itm_stormguard_hauberk_a_v2,
      itm_stormguard_hauberk_a_v3,
      itm_coat_of_plates,
      itm_coat_of_plates_v1,
      itm_coat_of_plates_v2,
      itm_old_mail_gloves,
      itm_mail_mittens,
      itm_m_gloves_a,
      itm_axe_crusader_a,
      itm_axe_crusader_b,
      itm_mace_4,
      itm_crusader_sword_b,
      itm_crusader_sword_c,
      itm_shield_heater_d,
      itm_tab_shield_tauria_a,
      itm_sword_of_war,
      itm_throwing_spears,
      itm_leather_boots_a,
    ],
    def_attrib|level(20),
    wp(150)|wp_two_handed(50),
    knows_common,
    swadian_face_young_1,
    swadian_face_middle_2
  ],

  # Avalanche Warriors - Lightning Riders
  [
    "stormguard_lightning_rider",
    "Stormguard Lightning Rider",
    "Stormguard Lightning Riders",
    tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_gloves|tf_mounted|tf_guarantee_horse,
    0,
    0,
    fac_kingdom_12,
    [
      itm_stormguard_pointy_helmet_mail_a,
      itm_stormguard_pointy_helmet_mail_b,
      itm_stormguard_pointy_helmet_mail_c,
      itm_stormguard_pointy_helmet_mail_d,
      itm_coat_of_plates,
      itm_coat_of_plates_v1,
      itm_coat_of_plates,
      itm_coat_of_plates_v1,
      itm_coat_of_plates_v2,
      itm_stormguard_heavy_hauberk_a,
      itm_stormguard_heavy_hauberk_a_v1,
      itm_m_gloves_a,
      itm_old_mail_gloves,
      itm_mail_mittens,
      itm_axe_crusader_a,
      itm_axe_crusader_b,
      itm_axe_crusader_1,
      itm_tab_shield_tauria_a,
      itm_crusader_long_sword_c,
      itm_crusader_long_sword_b,
      itm_light_lance,
      itm_throwing_spears,
      itm_warhorse,
      itm_black_knight_horse_a,
      itm_mail_boots_a,
      itm_mail_boots_b,
      itm_mail_boots_c,
      itm_leather_boots_a,
    ],
    def_attrib|level(25),
    wp(180),
    knows_common|knows_riding_5,
    swadian_face_young_1,
    swadian_face_middle_2
  ],

  # Avalanche Warriors - Tempest Sentinels - Elite Stormguard
  [
    "stormguard_tempest_sentinel",
    "Stormguard Tempest Sentinel",
    "Stormguard Tempest Sentinels",
    tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_gloves,
    0,
    0,
    fac_kingdom_12,
    [
      itm_stormguard_pointy_helmet_mail_a,
      itm_stormguard_pointy_helmet_mail_b,
      itm_stormguard_pointy_helmet_mail_c,
      itm_stormguard_pointy_helmet_mail_d,
      itm_stormguard_hauberk_a,
      itm_stormguard_hauberk_a_v1,
      itm_stormguard_hauberk_a_v2,
      itm_stormguard_hauberk_a_v3,
      itm_coat_of_plates,
      itm_coat_of_plates_v1,
      itm_coat_of_plates_v2,
      itm_stormguard_aketon_plated_b,
      itm_stormguard_aketon_plated_b_v1,      
      itm_m_gauntlets_a,
      itm_m_gauntlets_b,
      itm_one_handed_battle_axe_c,
      itm_tab_shield_tauria_b,
      itm_crusader_long_sword_a,
      itm_crusader_long_sword_b,
      itm_sword_of_war,
      itm_war_axe,
      itm_shortened_voulge,
      itm_throwing_spears,
      itm_mail_boots_a,
      itm_mail_boots_b,
      itm_mail_boots_c
    ],
    def_attrib|level(25),
    wp(180)|wp_two_handed(50),
    knows_common|knows_power_throw_6,
    swadian_face_young_1,
    swadian_face_middle_2
  ],

  [
    "stormguard_elite_stormguard",
    "Stormguard Elite",
    "Stormguard Elite",
    tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_gloves,
    0,
    0,
    fac_kingdom_12,
    [
      itm_stormguard_elite_helmet_a,
      itm_stormguard_elite_helmet_b,
      itm_stormguard_elite_helmet_c,
      itm_coat_of_plates_v3,
      itm_stormguard_heavy_hauberk_a,
      itm_stormguard_heavy_hauberk_a_v1,
      itm_m_gauntlets_b,
      itm_crusader_long_sword_a,
      itm_k_long_sword_c,
      itm_k_long_sword_b,
      itm_axe_crusader_1,
      itm_tab_shield_tauria_b,
      itm_bec_de_corbin_a,
      itm_bec_de_corbin,
      itm_simple_poleaxe,
      itm_heavy_throwing_axes,
      itm_throwing_spears,
      itm_plate_boots_a,
      itm_plate_boots_b
    ],
    def_attrib|level(30),
    wp(210)|wp_polearm(50),
    knows_common|knows_power_throw_9,
    swadian_face_young_1,
    swadian_face_middle_2
  ],

  # silver rose units
  [
    "silver_rose_novice",
    "Silver Rose Novice",
    "Silver Rose Novice",
    tf_guarantee_armor|tf_guarantee_boots,
    0,
    0,
    fac_kingdom_1,
    [
      itm_scythe,
      itm_hatchet,
      itm_pitch_fork,
      itm_stones,
      itm_pickaxe,
      itm_tab_shield_heater_a,
      itm_tab_shield_round_a,
      itm_aketon_silver_rose_a,
      itm_aketon_silver_rose_b,
      itm_aketon_silver_rose_c,
      itm_leather_silver_rose_a,
      itm_leather_silver_rose_b,
      itm_arming_cap,
      itm_cervelliere_light_a,
      itm_cervelliere_light_b,
      itm_old_leather_gloves,
      itm_hose_e
    ],
    def_attrib|level(5),
    wp(60),
    knows_common,
    swadian_face_younger_1,
    swadian_face_middle_2
  ],

  #peasant - retainer - footman - man-at-arms -  knight
  [
    "silver_rose_levy",
    "Silver Rose Levy",
    "Silver Rose Levy",
    tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet,
    0,
    0,
    fac_kingdom_1,
    [
      itm_falshion_1,
      itm_crusader_sword_a,
      itm_crusader_sword_b,
      itm_crusader_sword_c,
      itm_swadia_oval_shield_1,
      itm_swadia_oval_shield_2,
      itm_leather_silver_rose_c,
      itm_leather_silver_rose_d,
      itm_silver_rose_recruit_plated_a,
      itm_silver_rose_recruit_plated_b,
      itm_cervelliere_light_a,
      itm_cervelliere_light_b,
      itm_cervelliere_a,
      itm_cervelliere_b,
      itm_cervelliere_c,
      itm_cervelliere_d,
      itm_cervelliere_e,
      itm_cervelliere_f,
      itm_cervelliere_g,
      itm_cervelliere_h,
      itm_cervelliere_i,
      itm_cervelliere_j,
      itm_cervelliere_k,
      itm_cervelliere_l,
      itm_cervelliere_m,
      itm_cervelliere_n,
      itm_cervelliere_o,
      itm_leather_gloves,
      itm_hose_e
    ],
    def_attrib|level(10),
    wp(90),
    knows_common,
    swadian_face_younger_1,
    swadian_face_middle_2
  ],

  [
    "silver_rose_scout",
    "Silver Rose Scout",
    "Silver Rose Scouts",
    tf_mounted|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,
    0,
    0,
    fac_kingdom_1,
    [
      itm_crusader_sword_a,
      itm_crusader_sword_b,
      itm_crusader_sword_c,
      itm_swadia_oval_shield_1,
      itm_swadia_oval_shield_2,
      itm_silver_rose_recruit_plated_a,
      itm_silver_rose_recruit_plated_b,
      itm_silver_rose_scout_helmet_a,
      itm_silver_rose_scout_helmet_b,
      itm_leather_gloves,
      itm_hunter,
      itm_hose_e
    ],
    def_attrib|level(15),
    wp(120),
    knows_common|knows_riding_3,
    swadian_face_young_1,
    swadian_face_old_2
  ],

  [
    "silver_rose_milita",
    "Silver Rose Militia",
    "Silver Rose Militia",
    tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_helmet,
    0,
    0,
    fac_kingdom_1,
    [
      itm_crusader_sword_a,
      itm_crusader_sword_b,
      itm_crusader_sword_c,
      itm_crusader_spear_inf_a,
      itm_crusader_spear_inf_b,
      itm_crusader_spear_inf_c,
      itm_swadia_oval_shield_1,
      itm_swadia_oval_shield_2,
      itm_silver_rose_recruit_plated_c,
      itm_silver_rose_recruit_plated_d,
      itm_cervelliere_a,
      itm_cervelliere_b,
      itm_cervelliere_c,
      itm_silver_rose_sallet_a,
      itm_silver_rose_sallet_b,
      itm_silver_rose_sallet_c,
      itm_leather_gloves,
      itm_m_gloves_a,
      itm_leather_boots_a
    ],
    def_attrib|level(15),
    wp(120),
    knows_common,
    swadian_face_young_1,
    swadian_face_old_2
  ],

  [
    "silver_rose_footman",
    "Silver Rose Footman",
    "Silver Rose Footmen",
    tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_helmet,
    0,
    0,
    fac_kingdom_1,
    [
      itm_crusader_long_sword_a,
      itm_shortened_bill,
      itm_winged_mace,
      itm_flanged_mace,
      itm_crusader_spear_inf_a,
      itm_swadia_footman_shield_1,
      itm_swadia_footman_shield_2,
      itm_silver_rose_mail_a,
      itm_silver_rose_mail_b,
      itm_silver_rose_sallet_closed_a,
      itm_silver_rose_sallet_closed_b,
      itm_silver_rose_sallet_closed_c,
      itm_silver_rose_kettle_hat_a,
      itm_silver_rose_kettle_hat_b,
      itm_leather_gloves,
      itm_m_gloves_a,
      itm_leather_boots_a
    ],
    def_attrib|level(20),
    wp_melee(150),
    knows_common|knows_ironflesh_3|knows_shield_2|knows_athletics_2|knows_power_strike_2,
    swadian_face_young_1,
    swadian_face_old_2
  ],

  [
    "silver_rose_hacker",
    "Silver Rose Hacker",
    "Silver Rose Hackers",
    tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,
    0,
    0,
    fac_kingdom_1,
    [
      itm_shortened_bill,
      itm_m_mace_knight,
      itm_swadia_footman_shield_1,
      itm_swadia_footman_shield_2,
      itm_silver_rose_mail_a,
      itm_silver_rose_mail_a_v1,
      itm_silver_rose_mail_b,
      itm_silver_rose_mail_b_v1,
      itm_silver_rose_brigandine_a,
      itm_silver_rose_brigandine_b,
      itm_silver_rose_kettle_hat_a,
      itm_silver_rose_kettle_hat_b,
      itm_mail_coif,
      itm_cervelliere_mail_a,
      itm_cervelliere_mail_b,
      itm_cervelliere_mail_c,
      itm_cervelliere_coif_a,
      itm_cervelliere_coif_b,
      itm_cervelliere_coif_mail_a,
      itm_cervelliere_coif_mail_b,
      itm_leather_gloves,
      itm_m_gloves_a,
      itm_mail_boots_a
    ],
    def_attrib|str_22|agi_25|level(25),
    wp_melee(180)|wp_one_handed(50),
    knows_common|knows_ironflesh_5|knows_power_strike_4|knows_athletics_5,
    swadian_face_middle_1,
    swadian_face_old_2
  ],

  [
    "silver_rose_infantry",
    "Silver Rose Infantry",
    "Silver Rose Infantry",
    tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet,
    0,
    0,
    fac_kingdom_1,
    [
      itm_pike,
      itm_fighting_pick,
      itm_bastard_sword_a,
      itm_sword_medieval_a,
      itm_sword_medieval_b_small,
      itm_swadia_footman_shield_1,
      itm_swadia_footman_shield_2,
      itm_swadia_footman_shield_3,
      itm_swadia_footman_shield_4,
      itm_silver_rose_brigandine_a,
      itm_silver_rose_brigandine_b,
      itm_silver_rose_brigandine_c,
      itm_silver_rose_brigandine_c_v1,
      itm_silver_rose_brigandine_c_v2,
      itm_silver_rose_sallet_mail_a,
      itm_silver_rose_sallet_mail_b,
      itm_cervelliere_mail_c,
      itm_silver_rose_sallet_mail_a,
      itm_silver_rose_sallet_mail_b,
      itm_silver_rose_sallet_mail_c,
      itm_old_mail_gloves,
      itm_m_gloves_a,
      itm_mail_boots_a
    ],
    def_attrib|level(25),
    wp_melee(180),
    knows_common|knows_riding_3|knows_ironflesh_4|knows_power_strike_3|knows_shield_3|knows_athletics_3,
    swadian_face_middle_1,
    swadian_face_old_2
  ],

  [
    "silver_rose_sergeant",
    "Silver Rose Sergeant",
    "Silver Rose Sergeants",
    tf_mounted|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet,
    0,
    0,
    fac_kingdom_1,
    [
      itm_axe_crusader_a,
      itm_axe_crusader_b,
      itm_crusader_long_sword_c,
      itm_crusader_long_sword_b,
      itm_crusader_spear_inf_a,
      itm_swadia_footman_shield_1,
      itm_swadia_footman_shield_2,
      itm_swadia_footman_shield_3,
      itm_swadia_footman_shield_4,
      itm_m_sergant_helmet_a,
      itm_silver_rose_plate_a,
      itm_silver_rose_plate_b,
      itm_silver_rose_recruit_plated_e,
      itm_m_gloves_a,
      itm_m_gauntlets_a,
      itm_plate_boots_a,
      itm_plate_boots_b
    ],
    def_attrib|str_30|agi_20|level(30),
    wp_melee(210)|wp_one_handed(50)|wp_polearm(50),
    knows_common|knows_shield_4|knows_ironflesh_4|knows_power_strike_4|knows_athletics_4,
    swadian_face_middle_1,
    swadian_face_older_2
  ],

  [
    "silver_rose_crossbowman",
    "Silver Rose Crossbowman",
    "Silver Rose Crossbowmen",
    tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet,
    0,
    0,
    fac_kingdom_1,
    [
      itm_bolts,
      itm_light_crossbow,
      itm_hunting_crossbow,
      itm_shortened_bill,
      itm_winged_mace,
      itm_flanged_mace,
      itm_swadia_oval_shield_1,
      itm_swadia_oval_shield_2,
      itm_silver_rose_gambeson_a,
      itm_silver_rose_gambeson_b,
      itm_hose_e
    ],
    def_attrib|level(20),
    wp(150),
    knows_common|knows_riding_2|knows_ironflesh_1,
    swadian_face_young_1,
    swadian_face_middle_2
  ],

  [
    "silver_rose_trained_crossbowman",
    "Silver Rose Trained Crossbowman",
    "Silver Rose Trained Crossbowmen",
    tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet,
    0,
    0,
    fac_kingdom_1,
    [
      itm_bolts,
      itm_crossbow,
      itm_light_crossbow,
      itm_shortened_bill,
      itm_winged_mace,
      itm_flanged_mace,
      itm_crusader_sword_a,
      itm_crusader_sword_b,
      itm_crusader_sword_c,
      itm_swadia_oval_shield_1,
      itm_swadia_oval_shield_2,
      itm_silver_rose_gambeson_a,
      itm_silver_rose_gambeson_a_v1,
      itm_silver_rose_gambeson_b,
      itm_silver_rose_gambeson_b_v1,
      itm_silver_rose_capelina_a,
      itm_silver_rose_capelina_b,
      itm_leather_gloves,
      itm_hose_e
    ],
    def_attrib|level(25),
    wp(180)|wp_crossbow(50),
    knows_common|knows_riding_2|knows_ironflesh_1|knows_athletics_1,
    swadian_face_young_1,
    swadian_face_old_2
  ],

  [
    "silver_rose_sharpshooter",
    "Silver Rose Sharpshooter",
    "Silver Rose Sharpshooters",
    tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet,
    0,
    0,
    fac_kingdom_1,
    [
      itm_bolts,
      itm_crossbow,
      itm_crossbow,
      itm_heavy_crossbow,
      itm_shortened_bill,
      itm_m_mace_knight,
      itm_axe_crusader_1,
      itm_winged_mace,
      itm_flanged_mace,
      itm_crusader_sword_a,
      itm_crusader_sword_b,
      itm_crusader_sword_c,
      itm_silver_rose_recruit_plated_c,
      itm_silver_rose_recruit_plated_d,
      itm_swadia_oval_shield_1,
      itm_swadia_oval_shield_2,
      itm_silver_rose_capelina_c,
      itm_silver_rose_capelina_mail_a,
      itm_leather_gloves,
      itm_m_gloves_a,
      itm_leather_boots_a
    ],
    def_attrib|level(30),
    wp(210)|wp_crossbow(50),
    knows_common|knows_power_draw_3|knows_ironflesh_1|knows_power_strike_1|knows_athletics_2,
    swadian_face_middle_1,
    swadian_face_older_2
  ],

  [
    "silver_rose_horseman",
    "Silver Rose Horseman",
    "Silver Rose Horsemen",
    tf_mounted|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_horse|tf_guarantee_shield,
    0,
    0,
    fac_kingdom_1,
    [
      itm_morningstar,
      itm_swadia_oval_shield_1,
      itm_swadia_oval_shield_2,
      itm_silver_rose_mail_a,
      itm_silver_rose_mail_b,
      itm_silver_rose_sallet_a,
      itm_silver_rose_sallet_b,
      itm_silver_rose_sallet_c,
      itm_hunter,
      itm_hunter,
      itm_hunter_b,
      itm_hunter_c,
      itm_m_gloves_a,
      itm_leather_boots_a,
      itm_mail_boots_a
    ],
    def_attrib|level(30),
    wp_melee(210),
    knows_common|knows_riding_3|knows_ironflesh_4|knows_power_strike_4|knows_shield_3|knows_athletics_3,
    swadian_face_middle_1,
    swadian_face_old_2
  ],

  [
    "silver_rose_man_at_arms",
    "Silver Rose Man at Arms",
    "Silver Rose Men at Arms",
    tf_mounted|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_horse|tf_guarantee_shield,
    0,
    0,
    fac_kingdom_1,
    [
      itm_lance,
      itm_crusader_long_sword_a,
      itm_crusader_long_sword_b,
      itm_crusader_long_sword_c,
      itm_swadia_kite_shield_1,
      itm_swadia_kite_shield_2,
      itm_silver_rose_brigandine_a,
      itm_silver_rose_brigandine_b,
      itm_silver_rose_sallet_a,
      itm_silver_rose_sallet_b,
      itm_silver_rose_sallet_c,
      itm_silver_rose_sallet_d,
      itm_silver_rose_sallet_e,
      itm_silver_rose_sallet_f,
      itm_m_gloves_a,
      itm_hunter,
      itm_hunter_b,
      itm_hunter_c,
      itm_hunter_d,
      itm_mail_boots_a,
      itm_leather_boots_a,
      itm_plate_boots_b
    ],
    def_attrib|level(35),
    wp_melee(240),
    knows_common|knows_riding_4|knows_ironflesh_5|knows_shield_2|knows_power_strike_5,
    swadian_face_young_1,
    swadian_face_old_2
  ],

  [
    "silver_rose_knight",
    "Silver Rose Knight",
    "Silver Rose Knights",
    tf_mounted|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_horse|tf_guarantee_shield,
    0,
    0,
    fac_kingdom_1,
    [
      itm_crusader_knight_spear_a,
      itm_k_long_sword_a,
      itm_k_long_sword_b,
      itm_k_long_sword_c,
      itm_swadia_heater_shield_1,
      itm_swadia_heater_shield_2,
      itm_silver_rose_plate_a,
      itm_silver_rose_plate_b,
      itm_silver_rose_plate_c,
      itm_silver_rose_sallet_f,
      itm_silver_rose_sallet_mail_c,
      itm_m_gauntlets_a,
      itm_silver_rose_heavy_horse_a,
      itm_plate_boots_a,
      itm_plate_boots_b,
      itm_mail_boots_a
    ],
    def_attrib|level(40),
    wp_melee(270),
    knows_common|knows_riding_5|knows_shield_5|knows_ironflesh_8|knows_power_strike_8,
    swadian_face_middle_1,
    swadian_face_older_2
  ],

  ["swadian_messenger","Swadian Messenger","Swadian Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_1,
   [itm_sword_medieval_a,itm_leather_jerkin,itm_courser,itm_leather_gloves,itm_light_crossbow,itm_bolts],
   str_7 | agi_21 | int_4 | cha_4|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5,swadian_face_young_1, swadian_face_old_2],
  ["swadian_deserter","Swadian Deserter","Swadian Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_bolts,itm_light_crossbow,itm_hunting_crossbow,itm_dagger,itm_club,itm_voulge,itm_wooden_shield,itm_leather_jerkin,itm_padded_cloth,itm_padded_coif,itm_footman_helmet,itm_iron_crown_nasal_a],
   def_attrib|level(14),wp(80),knows_common|knows_riding_2|knows_ironflesh_1,swadian_face_young_1, swadian_face_old_2],
  ["swadian_prison_guard","Prison Guard","Prison Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_awlpike,itm_pike,itm_great_sword,itm_morningstar,itm_sword_medieval_b,itm_tab_shield_heater_c,itm_coat_of_plates,itm_plate_armor,itm_bascinet_3,itm_black_helmet,itm_bascinet,itm_bascinet_3,itm_leather_gloves],
   def_attrib|level(25),wp(130),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
  ["swadian_castle_guard","Castle Guard","Castle Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_awlpike,itm_pike,itm_great_sword,itm_morningstar,itm_sword_medieval_b,itm_tab_shield_heater_c,itm_tab_shield_heater_d,itm_coat_of_plates,itm_plate_armor,itm_bascinet_3,itm_black_helmet,itm_bascinet,itm_bascinet_3,itm_leather_gloves],
   def_attrib|level(25),wp(130),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],

  # Vaegir watchman?
  [
    "chornovalley_recruit",
    "Chornovalley Recruit",
    "Chornovalley Recruits",
    tf_guarantee_boots|tf_guarantee_armor,
    0,
    0,
    fac_kingdom_2,
    [
      itm_mace_1,
      itm_hand_axe,
      itm_cudgel,
      itm_axe,
      itm_stones,
      itm_tab_shield_kite_a,
      itm_chornovalley_vest_c,
      itm_chornovalley_vest_b,
      itm_chornovalley_vest_a,
      itm_chornovalley_aketon_a,
      itm_chornovalley_aketon_b,
      itm_chornovalley_skullcap_helmet_a,
      itm_chornovalley_skullcap_helmet_a_v1,
      itm_chornovalley_skullcap_helmet_b,
      itm_chornovalley_skullcap_helmet_b_v1,      
      itm_leather_shoes_a,
      itm_leather_shoes_b,
      itm_leather_shoes_c
    ],
    def_attrib|level(5),
    wp(60),
    knows_common,
    vaegir_face_younger_1,
    vaegir_face_middle_2
  ],

  [
    "chornovalley_scout",
    "Chornovalley Scout",
    "Chornovalley Scouts",
    tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,
    0,
    0,
    fac_kingdom_2,
    [
      itm_winged_mace,
      itm_fighting_axe,
      itm_tab_shield_kite_b,
      itm_chornovalley_skullcap_helmet_c,
      itm_chornovalley_skullcap_helmet_c_v1,
      itm_chornovalley_footman_helmet_a,
      itm_chornovalley_footman_helmet_a_v1,
      itm_chornovalley_lamellar_vest_a,
      itm_chornovalley_lamellar_vest_b,
      itm_chornovalley_lamellar_vest_c,
      itm_chornovalley_lamellar_vest_d,
      itm_leather_gloves,
      itm_leather_shoes_a,
      itm_leather_shoes_b,
      itm_leather_shoes_c
    ],
    def_attrib|level(10),
    wp(90),
    knows_common,
    vaegir_face_young_1,
    vaegir_face_middle_2
  ],

  [
    "chornovalley_hunter",
    "Chornovalley Hunter",
    "Chornovalley Hunters",
    tf_guarantee_all,
    0,
    0,
    fac_kingdom_2,
    [
      itm_arrows,
      itm_hunting_bow,
      itm_mace_1,
      itm_hand_axe,
      itm_cudgel,
      itm_hatchet,
      itm_chornovalley_vest_c,
      itm_chornovalley_skullcap_helmet_c,
      itm_chornovalley_skullcap_helmet_c_v1,
      itm_leather_shoes_a,
      itm_leather_shoes_b,
      itm_leather_shoes_c
    ],
    def_attrib|level(15),
    wp(120)|wp_archery(50),
    knows_ironflesh_1|knows_power_draw_2|knows_power_throw_1,
    vaegir_face_young_1,
    vaegir_face_old_2
  ],

  [
    "chornovalley_longbowman",
    "Chornovalley Longbowman",
    "Chornovalley Longbowmen",
    tf_guarantee_all,
    0,
    0,
    fac_kingdom_2,
    [
      itm_arrows,
      itm_long_bow,
      itm_heavy_infantry_axe,
      itm_falchion,
      itm_chornovalley_vest_c,
      itm_chornovalley_footman_helmet_a,
      itm_chornovalley_footman_helmet_a_v1,
      itm_chornovalley_footman_helmet_b,
      itm_light_leather_boots_a,
      itm_light_leather_boots_b,
      itm_light_leather_boots_c
    ],
    def_attrib|level(20),
    wp(150)|wp_archery(50),
    knows_ironflesh_1|knows_power_draw_4|knows_athletics_6|knows_power_throw_1,
    vaegir_face_young_1,
    vaegir_face_older_2
  ],

  [
    "chornovalley_warrior",
    "Chornovalley Warrior",
    "Chornovalley Warriors",
    tf_guarantee_all,
    0,
    0,
    fac_kingdom_2,
    [
      itm_fighting_axe,
      itm_norman_shield_1,
      itm_battle_trident,
      itm_boar_spear,
      itm_broad_spear,
      itm_tongue_spear,
      itm_chornovalley_footman_helmet_a,
      itm_chornovalley_footman_helmet_a_v1,
      itm_chornovalley_footman_helmet_b,
      itm_chornovalley_mail_a,
      itm_chornovalley_mail_b,
      itm_m_gloves_a,
      itm_light_leather_boots_a,
      itm_light_leather_boots_b,
      itm_light_leather_boots_c
    ],
    def_attrib|level(15),
    wp_melee(120),
    knows_athletics_2|knows_ironflesh_4|knows_power_strike_2|knows_shield_2,
    vaegir_face_young_1,
    vaegir_face_old_2
  ],

  [
    "chornovalley_sheriff",
    "Chornovalley Sheriff",
    "Chornovalley Sheriffs",
    tf_guarantee_all,
    0,
    0,
    fac_kingdom_2,
    [
      itm_m_two_handed_heavy_axe_a,
      itm_m_two_handed_heavy_axe_b,
      itm_norman_shield_2,
      itm_battle_trident,
      itm_chornovalley_infantry_helmet_a,
      itm_chornovalley_infantry_helmet_b,
      itm_chornovalley_infantry_helmet_c,
      itm_chornovalley_heavy_mail_a,
      itm_chornovalley_heavy_mail_b,
      itm_leather_gloves,
      itm_m_gloves_a,
      itm_scale_gauntlets,
      itm_lamellar_gauntlets,
      itm_mail_boots_a,
      itm_mail_boots_b,
      itm_mail_boots_c
    ],
    def_attrib|level(20),
    wp_melee(150),
    knows_athletics_3|knows_ironflesh_5|knows_power_strike_3|knows_shield_2,
    vaegir_face_young_1,
    vaegir_face_older_2
  ],

  [
    "chornovalley_sergeant",
    "Chornovalley Sergeant",
    "Chornovalley Sergeants",
    tf_guarantee_all,
    0,
    0,
    fac_kingdom_2,
    [
      itm_m_two_handed_heavy_axe_a,
      itm_m_two_handed_heavy_axe_b,
      itm_norman_shield_2,
      itm_battle_trident,
      itm_chornovalley_infantry_helmet_a,
      itm_chornovalley_infantry_helmet_b,
      itm_chornovalley_infantry_helmet_c,
      itm_chornovalley_heavy_mail_b,
      itm_chornovalley_heavy_mail_b_v1,
      itm_chornovalley_heavy_lamellar_a,
      itm_chornovalley_heavy_lamellar_b,
      itm_chornovalley_heavy_lamellar_c,
      itm_scale_gauntlets,
      itm_lamellar_gauntlets,
      itm_mail_boots_a,
      itm_mail_boots_b,
      itm_mail_boots_c
    ],
    def_attrib|level(25),
    wp_melee(180),
    knows_athletics_7|knows_ironflesh_9|knows_power_strike_7|knows_shield_2,
    vaegir_face_young_1,
    vaegir_face_older_2
  ],

  [
    "chornovalley_gunslider",
    "Chornovalley Gunslider",
    "Chornovalley Gunsliders",
    tf_mounted|tf_guarantee_all,
    0,
    0,
    fac_kingdom_2,
    [
      itm_heavy_infantry_axe,
      itm_chornovalley_infantry_helmet_a,
      itm_chornovalley_infantry_helmet_b,
      itm_chornovalley_infantry_helmet_c,
      itm_chornovalley_lamellar_vest_b,
      itm_m_gloves_a,
      itm_pistol_a,
      itm_pistol_b,
      itm_cartridges,
      itm_mail_boots_a,
      itm_mail_boots_b,
      itm_mail_boots_c
    ],
    def_attrib|level(25),
    wp_melee(180)|wp_firearm(50),
    knows_riding_2|knows_athletics_9|knows_shield_2|knows_ironflesh_5|knows_power_strike_4,
    vaegir_face_middle_1,
    vaegir_face_older_2
  ],
  
  [
    "chornovalley_horseman",
    "Chornovalley Horseman",
    "Chornovalley Horsemen",
    tf_guarantee_all,
    0,
    0,
    fac_kingdom_2,
    [
      itm_heavy_infantry_axe,
      itm_lance,
      itm_tab_shield_kite_cav_a,
      itm_chornovalley_footman_helmet_a,
      itm_chornovalley_footman_helmet_b,
      itm_chornovalley_mail_a,
      itm_chornovalley_mail_b,
      itm_m_gloves_a,
      itm_hunter,
      itm_mail_boots_a,
      itm_mail_boots_b,
      itm_mail_boots_c
    ],
    def_attrib|level(20),
    wp(150),
    knows_riding_3|knows_ironflesh_3|knows_power_strike_3,
    vaegir_face_young_1,
    vaegir_face_older_2
  ],

  [
    "chornovalley_knight",
    "Chornovalley Knight",
    "Chornovalley Knights",
    tf_guarantee_all,
    0,
    0,
    fac_kingdom_2,
    [
      itm_bardiche,
      itm_great_bardiche,
      itm_war_axe,
      itm_fighting_axe,
      itm_lance,
      itm_tab_shield_kite_cav_b,
      itm_chornovalley_infantry_helmet_a,
      itm_chornovalley_infantry_helmet_b,
      itm_chornovalley_infantry_helmet_c,
      itm_chornovalley_heavy_lamellar_a,
      itm_chornovalley_heavy_lamellar_b,
      itm_chornovalley_heavy_lamellar_c,
      itm_scale_gauntlets,
      itm_lamellar_gauntlets,
      itm_hunter,
      itm_mail_boots_a,
      itm_mail_boots_b,
      itm_mail_boots_c
    ],
    def_attrib|level(25),
    wp(180),
    knows_riding_4|knows_shield_2|knows_ironflesh_4|knows_power_strike_4,
    vaegir_face_middle_1,
    vaegir_face_older_2
  ],

  ["vaegir_messenger","Vaegir Messenger","Vaegir Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_2,
   [itm_sword_medieval_b,itm_leather_jerkin,itm_courser,itm_leather_gloves,itm_short_bow,itm_arrows],
   str_7 | agi_21 | int_4 | cha_4|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_deserter","Vaegir Deserter","Vaegir Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_arrows,itm_spiked_mace,itm_axe,itm_falchion,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_javelin,itm_javelin,itm_steppe_cap,itm_nomad_cap,itm_leather_vest,itm_leather_vest,itm_nomad_armor],
   str_10 | agi_5 | int_4 | cha_4|level(14),wp(80),knows_ironflesh_1|knows_power_draw_1,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_prison_guard","Prison Guard","Prison Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_ashwood_pike,itm_battle_fork,itm_bardiche,itm_battle_axe,itm_fighting_axe,itm_tab_shield_kite_b,itm_studded_leather_coat,itm_chornovalley_heavy_mail_b,itm_mail_coif,itm_mail_coif,itm_mail_coif,itm_spiked_helmet,itm_leather_gloves],
   def_attrib|level(24),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,vaegir_face_middle_1, vaegir_face_older_2],
  ["vaegir_castle_guard","Castle Guard","Castle Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_ashwood_pike,itm_battle_fork,itm_bardiche,itm_battle_axe,itm_fighting_axe,itm_tab_shield_kite_d,itm_studded_leather_coat,itm_chornovalley_heavy_mail_b,itm_mail_coif,itm_mail_coif,itm_mail_coif,itm_spiked_helmet,itm_leather_gloves],
   def_attrib|level(24),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,vaegir_face_middle_1, vaegir_face_older_2],

  ["celestial_recruit","Celestial Recruit","Celestial Recruits",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_3,
   [itm_studded_club, itm_hammer, itm_club, itm_tab_shield_round_a, itm_celestial_coif_a, itm_celestial_coif_b, itm_celestial_aketon_a,itm_celestial_aketon_b,itm_celestial_aketon_c,itm_celestial_aketon_d],
   def_attrib|level(5),wp(60),knows_common|knows_athletics_3|knows_power_draw_2|knows_horse_archery_2,swadian_face_young_1, swadian_face_old_2],

  # hergit warrior -> khergit sworsman -> khergit veteran -> khergit champion
  ["celestial_milita","Celestial Milita","Celestial Milita",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_3, [itm_studded_club, itm_falchion, itm_m_glaive_b, itm_m_glaive_a, itm_military_scythe, itm_tab_shield_heater_a, itm_tab_shield_heater_b ,itm_celestial_light_sallet_a,itm_celestial_light_sallet_b,itm_celestial_light_sallet_c, itm_celestial_aketon_a,itm_celestial_aketon_b,itm_celestial_aketon_c,itm_celestial_aketon_d, itm_mt_leather_gloves_a], def_attrib|level(10),wp(90),knows_shield_2|knows_ironflesh_4|knows_power_strike_4,swadian_face_younger_1, swadian_face_old_2],

  ["celestial_hunter","Celestial Hunter","Celestial Hunters",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_kingdom_3, [itm_studded_club, itm_falchion, itm_axe, itm_hunting_crossbow, itm_bolts, itm_tab_shield_heater_a, itm_tab_shield_heater_b, itm_celestial_coif_a, itm_celestial_coif_b, itm_m_celestial_padded_cloth_a, itm_m_celestial_padded_cloth_b, itm_mt_leather_gloves_a], def_attrib|level(10),wp(90)|wp_crossbow(50),knows_common|knows_athletics_5,swadian_face_younger_1, swadian_face_old_2],
  ["celestial_crossbowman","Celestial Crossbowman","Celestial Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_kingdom_3, [itm_studded_club, itm_winged_mace, itm_falchion, itm_military_hammer, itm_strange_winged_mace, itm_flanged_mace, itm_heavy_mace_a, itm_sniper_crossbow, itm_heavy_crossbow, itm_bolts, itm_steel_bolts, itm_piercing_bolts, itm_tab_shield_heater_b, itm_tab_shield_heater_c, itm_celestial_light_sallet_a, itm_celestial_light_sallet_b,itm_celestial_light_sallet_c, itm_m_celestial_mail_a, itm_m_celestial_mail_b, itm_mt_leather_gloves_a], def_attrib|level(15),wp(120)|wp_crossbow(50),knows_common|knows_athletics_8|knows_power_strike_3,swadian_face_younger_1, swadian_face_old_2],

  ["celestial_armsman","Celestial Armsman","Celestial Armsmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_3, [itm_winged_mace, itm_falchion, itm_military_hammer, itm_strange_winged_mace, itm_flanged_mace, itm_heavy_mace_a, itm_metal_flanged_mace, itm_m_glaive_b, itm_m_glaive_a, itm_military_scythe, itm_tab_shield_heater_b, itm_tab_shield_heater_c , itm_celestial_sallet_a, itm_celestial_sallet_b, itm_celestial_sallet_c, itm_celestial_visored_sallet_a, itm_celestial_visored_sallet_b, itm_celestial_visored_sallet_c, itm_celestial_aketon_breastplate_a, itm_celestial_aketon_breastplate_b, itm_m_gloves_a, itm_leather_gloves, itm_mt_leather_gloves_a], def_attrib|level(15),wp(120),knows_common|knows_ironflesh_5|knows_shield_1|knows_power_strike_2,swadian_face_young_1, swadian_face_older_2],

  ["celestial_foot_knight","Celestial Foot Knight","Celestial Foot Knights",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_3,
   [itm_m_glaive_b, itm_m_glaive_a, itm_military_scythe, itm_m_ashwood_pike_a, itm_celestial_sallet_with_plume_a, itm_celestial_sallet_with_plume_b, itm_celestial_sallet_with_plume_c, itm_m_celestial_breastplate_a, itm_m_celestial_breastplate_b, itm_m_celestial_breastplate_c, itm_m_celestial_breastplate_d, itm_m_gloves_a, itm_leather_gloves, itm_mt_leather_gloves_a],
   def_attrib|level(15),wp(120)|wp_polearm(50),knows_athletics_6|knows_ironflesh_5|knows_power_strike_5,swadian_face_young_1, swadian_face_older_2],

  ["celestial_sergeant","Celestial Sergeant","Celestial Sergeants",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_3,
   [itm_m_glaive_b, itm_m_glaive_a, itm_military_scythe, itm_m_ashwood_pike_a, itm_celestial_sallet_on_mail_a, itm_celestial_sallet_on_mail_b, itm_celestial_sallet_on_mail_c, itm_m_celestial_breastplate_heavy_a, itm_m_celestial_breastplate_heavy_b, itm_m_gloves_a],
   def_attrib|level(20),wp(150),knows_power_strike_5|knows_ironflesh_3|knows_athletics_6|knows_shield_1,swadian_face_middle_1, swadian_face_older_2],
  ["celestial_lancer","Celestial Lancer","Celestial Lancers",tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac_kingdom_3,
   [itm_lance, itm_m_one_handed_knight_axe_a, itm_m_one_handed_knight_axe_b, itm_m_two_handed_knight_axe_b, itm_m_mace_knight, itm_m_mace_knight_pierce, itm_shield_heater_d, itm_celestial_bascinet_visored_a, itm_celestial_bascinet_visored_b, itm_celestial_bascinet_visored_c, itm_m_celestial_plate_c, itm_m_celestial_plate_d, itm_m_gloves_a, itm_m_gauntlets_a, itm_m_gauntlets_b, itm_warhorse],
   def_attrib|level(20),wp(150),knows_riding_7|knows_power_strike_9|knows_ironflesh_7|knows_shield_2,swadian_face_middle_1, swadian_face_older_2],

  ["celestial_commander","Celestial Commander","Celestial Commanders",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_3,
   [itm_bec_de_corbin_a, itm_m_pole_hammer_a, itm_m_pole_hammer_b, itm_m_war_hammer_a, itm_celestial_bascinet_a, itm_celestial_bascinet_b, itm_celestial_bascinet_c, itm_m_celestial_plate_a, itm_m_celestial_plate_b, itm_m_mace_knight, itm_m_mace_knight_pierce, itm_shield_heater_d, itm_m_gauntlets_a, itm_m_gauntlets_b],
   def_attrib|level(25),wp(180)|wp_polearm(50),knows_power_strike_8|knows_ironflesh_10|knows_shield_8|knows_athletics_8,swadian_face_middle_1, swadian_face_older_2],

  ["khergit_messenger","Khergit Messenger","Khergit Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_3,
   [itm_sword_khergit_2,itm_leather_jerkin,itm_courser,itm_leather_gloves,itm_short_bow,itm_arrows],
   str_7 | agi_21 | int_4 | cha_4|level(25),wp(125),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,khergit_face_young_1, khergit_face_older_2],
  ["khergit_deserter","Khergit Deserter","Khergit Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_arrows,itm_spiked_mace,itm_axe,itm_sword_khergit_1,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_javelin,itm_javelin,itm_steppe_cap,itm_nomad_cap_b,itm_khergit_armor,itm_steppe_armor,itm_tribal_warrior_outfit],
   str_10 | agi_5 | int_4 | cha_4|level(14),wp(80),knows_ironflesh_1|knows_power_draw_1,khergit_face_young_1, khergit_face_older_2],
  ["khergit_prison_guard","Prison Guard","Prison Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_sword_khergit_3,itm_tab_shield_small_round_b,itm_tab_shield_small_round_a,itm_lamellar_vest_khergit,itm_chornovalley_heavy_mail_b,itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_leather_warrior_cap],
   def_attrib|level(24),wp(130),knows_athletics_5|knows_shield_2|knows_ironflesh_5,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_castle_guard","Castle Guard","Castle Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_sword_khergit_4,itm_tab_shield_small_round_b,itm_tab_shield_small_round_a,itm_lamellar_vest_khergit,itm_chornovalley_heavy_mail_b,itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_leather_warrior_cap],
   def_attrib|level(24),wp(130),knows_athletics_5|knows_shield_2|knows_ironflesh_5,khergit_face_middle_1, khergit_face_older_2],

  [
    "iron_crown_recruit",
    "Iron Crown Recruit",
    "Iron Crown Recruits",
    tf_guarantee_armor,0,0,
    fac_kingdom_4,
    [
      itm_axe,
      itm_hand_axe,
      itm_hatchet,
      itm_boar_spear,
      itm_tab_shield_round_a,
      itm_tab_shield_kite_a,
      itm_m_iron_crown_aketon_a,
      itm_m_iron_crown_aketon_b,
      itm_m_iron_crown_leather_vest_a,
      itm_m_iron_crown_leather_vest_b,
      itm_common_hood,
      itm_hood_d,
      itm_iron_crown_scullcap_a,
      itm_iron_crown_scullcap_b,
      itm_leather_gloves
    ],
    def_attrib|level(5),
    wp(60),
    knows_power_strike_1|knows_power_throw_1|knows_riding_1|knows_athletics_1,
    nord_face_younger_1,
    nord_face_old_2
  ],

  [
    "iron_crown_raider",
    "Iron Crown Raider",
    "Iron Crown Raiders",
    tf_guarantee_armor|tf_guarantee_shield,
    0,
    0,
    fac_kingdom_4,
    [
      itm_fighting_axe,
      itm_falchion,
      itm_heavy_mace_a,
      itm_one_handed_war_axe_a,
      itm_spear,
      itm_boar_spear,
      itm_tab_shield_round_a,
      itm_tab_shield_round_b,
      itm_iron_crown_nasal_a,
      itm_iron_crown_nasal_reinforced_a,
      itm_iron_crown_footman_helmet_a,
      itm_m_iron_crown_leather_vest_a,
      itm_m_iron_crown_leather_vest_a,
      itm_m_iron_crown_scale_vest_a,
      itm_m_iron_crown_scale_vest_b,
      itm_leather_gloves,
      itm_m_gloves_a
    ],
    def_attrib|level(10),
    wp(90),
    knows_ironflesh_2|knows_power_strike_3|knows_riding_2|knows_athletics_2|knows_shield_1,
    nord_face_young_1,
    nord_face_old_2
  ],

  [
    "iron_crown_footman",
    "Iron Crown Footman",
    "Iron Crown Footmen",
    tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,
    0,
    0,
    fac_kingdom_4,
    [
      itm_one_handed_war_axe_a,
      itm_one_handed_war_axe_b,
      itm_one_handed_battle_axe_a,
      itm_two_handed_axe,
      itm_winged_mace,
      itm_strange_winged_mace,
      itm_flanged_mace,
      itm_tab_shield_round_b,
      itm_iron_crown_nasal_a,
      itm_iron_crown_nasal_b,
      itm_iron_crown_nasal_reinforced_a,
      itm_iron_crown_nasal_reinforced_b,
      itm_iron_crown_footman_helmet_a,
      itm_iron_crown_footman_helmet_b,
      itm_m_iron_crown_scale_vest_c,
      itm_m_iron_crown_scale_vest_d,
      itm_m_iron_crown_armor_a,
      itm_m_iron_crown_armor_b,
      itm_m_gloves_a,
      itm_mail_mittens,
      itm_old_mail_gloves
    ],
    def_attrib|level(15),
    wp(120),
    knows_ironflesh_3|knows_power_strike_3|knows_power_throw_2|knows_riding_2|knows_athletics_3|knows_shield_2,
    nord_face_young_1,
    nord_face_old_2
  ],

  [
    "iron_crown_man_at_arms",
    "Iron Crown Man-at-Arms",
    "Iron Crown Men-at-Arms",
    tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,
    0,
    0,
    fac_kingdom_4,
    [
      itm_one_handed_war_axe_b,
      itm_winged_mace,
      itm_strange_winged_mace,
      itm_flanged_mace,
      itm_war_spear,
      itm_light_throwing_axes,
      itm_iron_crown_nasal_c,
      itm_iron_crown_nasal_reinforced_b,
      itm_iron_crown_nasal_reinforced_c,
      itm_iron_crown_footman_helmet_b,
      itm_iron_crown_bascinet_a,
      itm_iron_crown_bascinet_b,
      itm_m_iron_crown_hauberk_a,
      itm_m_iron_crown_hauberk_b,
      itm_one_handed_battle_axe_a,
      itm_two_handed_battle_axe_2,
      itm_tab_shield_round_c,
      itm_mail_mittens,
      itm_old_mail_gloves,
      itm_scale_gauntlets,
      itm_lamellar_gauntlets
    ],
    def_attrib|level(20),
    wp(150),
    knows_ironflesh_4|knows_power_strike_4|knows_power_throw_3|knows_riding_2|knows_athletics_4|knows_shield_3,
    nord_face_young_1,
    nord_face_older_2
  ],

  [
    "iron_crown_vetaran",
    "Iron Crown Veteran",
    "Iron Crown Veterans",
    tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,
    0,
    0,
    fac_kingdom_4,
    [
      itm_one_handed_battle_axe_b,
      itm_great_axe,
      itm_tab_shield_round_d,
      itm_light_throwing_axes,
      itm_iron_crown_nasal_reinforced_c,
      itm_iron_crown_nasal_c,
      itm_iron_crown_bascinet_a,
      itm_iron_crown_bascinet_b,
      itm_m_iron_crown_hauberk_c,
      itm_m_iron_crown_brigandine_mail_a,
      itm_m_iron_crown_brigandine_mail_b,
      itm_old_mail_gloves,
      itm_scale_gauntlets,
      itm_lamellar_gauntlets
    ],
    def_attrib|level(25),
    wp(180),
    knows_ironflesh_5|knows_power_strike_5|knows_riding_3|knows_athletics_5|knows_shield_4,
    nord_face_young_1,
    nord_face_older_2
  ],

  [
    "iron_crown_champion",
    "Iron Crown Champion",
    "Iron Crown Champions",
    tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,
    0,
    0,
    fac_kingdom_4,
    [
      itm_warhammer,
      itm_great_axe,
      itm_long_axe,
      itm_long_axe_b,
      itm_one_handed_battle_axe_c,
      itm_tab_shield_round_e,
      itm_throwing_spears,
      itm_throwing_spears,
      itm_throwing_spears,
      itm_iron_crown_bascinet_mail_a,
      itm_iron_crown_bascinet_mail_b,
      itm_iron_crown_winged_helmet_a,
      itm_iron_crown_winged_helmet_b,
      itm_iron_crown_footman_helmet_c,
      itm_m_iron_crown_scale_a,
      itm_m_iron_crown_scale_b,
      itm_old_mail_gloves,
      itm_scale_gauntlets,
      itm_lamellar_gauntlets
    ],
    def_attrib|level(30),
    wp(210),
    knows_ironflesh_9|knows_power_strike_7|knows_power_throw_5|knows_riding_2|knows_athletics_7|knows_shield_6,
    nord_face_middle_1,
    nord_face_older_2
],

[
  "iron_crown_halberdier",
  "Iron Crown Halberdier",
  "Iron Crown Halberdiers",
  tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_gloves,
  0,
  0,
  fac_kingdom_4,
  [
    itm_elegant_poleaxe,
    itm_poleaxe_a,
    itm_english_bill,
    itm_swiss_halberd,
    itm_crusader_sword_a,
    itm_tab_shield_round_d,
    itm_iron_crown_bascinet_a,
    itm_iron_crown_bascinet_b,
    itm_iron_crown_bascinet_mail_a,
    itm_iron_crown_bascinet_mail_b,
    itm_m_iron_crown_hauberk_c,
    itm_m_iron_crown_brigandine_mail_a,
    itm_m_iron_crown_brigandine_mail_b,
    itm_old_mail_gloves,
    itm_scale_gauntlets,
    itm_lamellar_gauntlets
  ],
  def_attrib|level(25),
  wp(180)|wp_polearm(180),
  knows_ironflesh_6|knows_power_strike_7|knows_athletics_8,
  nord_face_young_1,
  nord_face_older_2
],

[
  "iron_crown_skirmisher",
  "Iron Crown Skirmisher",
  "Iron Crown Skirmisher",
  tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,
  0,
  0,
  fac_kingdom_4,
  [
    itm_bolts,
    itm_bolts,
    itm_hunting_crossbow,
    itm_crossbow,
    itm_falchion,
    itm_flanged_mace,
    itm_mace_1,
    itm_hatchet,
    itm_m_iron_crown_aketon_a,
    itm_m_iron_crown_aketon_b,
    itm_iron_crown_scullcap_a,
    itm_iron_crown_scullcap_b,
    itm_leather_gloves
  ],
  def_attrib|level(10),
  wp(90)|wp_archery(50),
  knows_ironflesh_1|knows_power_draw_2|knows_athletics_2,
  nord_face_young_1,
  nord_face_old_2
],

[
  "iron_crown_trained_skirmisher",
  "Iron Crown Trained Skirmisher",
  "Iron Crown Trained Skirmishers",
  tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,
  0,
  0,
  fac_kingdom_4,
  [
    itm_bolts,
    itm_bolts,
    itm_steel_bolts,
    itm_heavy_crossbow,
    itm_crossbow,
    itm_shortened_bill,
    itm_flanged_mace,
    itm_heavy_mace_a,
    itm_mace_2,
    itm_mace_3,
    itm_m_iron_crown_brigandine_a,
    itm_m_iron_crown_brigandine_b,
    itm_iron_crown_nasal_b,
    itm_iron_crown_footman_helmet_b,
    itm_m_gloves_a
  ],
  def_attrib|level(15),
  wp(120)|wp_archery(50),
  knows_ironflesh_5|knows_athletics_5|knows_power_draw_6,
  nord_face_young_1,
  nord_face_old_2
],

["nord_messenger","Nord Messenger","Nord Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_4,
  [itm_sword_viking_2,itm_leather_jerkin,itm_courser,itm_leather_gloves,itm_short_bow,itm_arrows],
  str_7 | agi_21 | int_4 | cha_4|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,nord_face_young_1, nord_face_older_2],
["nord_deserter","Nord Deserter","Nord Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
  [itm_arrows,itm_spiked_mace,itm_axe,itm_falchion,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_javelin,itm_javelin,itm_steppe_cap,itm_nomad_cap,itm_leather_vest,itm_leather_vest,itm_nomad_armor],
  str_10 | agi_5 | int_4 | cha_4|level(14),wp(80),knows_ironflesh_1|knows_power_draw_1,nord_face_young_1, nord_face_older_2],
["nord_prison_guard","Prison Guard","Prison Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_4,
  [itm_ashwood_pike,itm_battle_fork,itm_battle_axe,itm_fighting_axe,itm_tab_shield_round_d,itm_mail_hauberk,itm_mail_coif,itm_mail_coif,itm_mail_coif,itm_spiked_helmet,itm_leather_gloves],
  def_attrib|level(24),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,nord_face_middle_1, nord_face_older_2],
["nord_castle_guard","Castle Guard","Castle Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_4,
  [itm_ashwood_pike,itm_battle_fork,itm_battle_axe,itm_fighting_axe,itm_tab_shield_round_d,itm_tab_shield_round_e,itm_mail_hauberk,itm_heraldic_mail_with_tabard,itm_mail_coif,itm_mail_coif,itm_mail_coif,itm_spiked_helmet,itm_leather_gloves],
  def_attrib|level(24),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,nord_face_middle_1, nord_face_older_2],

[
  "alpine_recruit",
  "Alpine Recruit",
  "Alpine Recruits",
  tf_guarantee_boots|tf_guarantee_armor,
  0,
  0,
  fac_kingdom_5,
  [
    itm_pitch_fork,
    itm_voulge_short,
    itm_falchion,
    itm_shortened_bill,
    itm_felt_hat_b,
    itm_m_coif_cloth_a,
    itm_arming_cap,
    itm_m_coif_alternate_a,
    itm_mace_1,
    itm_shield_kite_k,
    itm_m_alpine_aketon_a,
    itm_m_alpine_aketon_b,
    itm_old_leather_gloves
  ],
  def_attrib|level(5),
  wp(60),
  knows_common|knows_power_draw_2|knows_ironflesh_1,
  rhodok_face_younger_1,
  rhodok_face_old_2
],

[
  "alpine_levy",
  "Alpine Levy",
  "Alpine Levy",
  tf_guarantee_boots|tf_guarantee_armor,
  0,
  0,
  fac_kingdom_5,
  [
    itm_spear,
    itm_mace_2,
    itm_mace_3,
    itm_mace_4,
    itm_shield_kite_k,
    itm_alpine_leather_vest_a,
    itm_alpine_leather_vest_b,
    itm_arming_cap,
    itm_alpine_chapel_a,
    itm_alpine_chapel_b,
    itm_alpine_chapel_c,
    itm_m_gloves_a,
    itm_old_leather_gloves,
    itm_leather_gloves
  ],
  def_attrib|level(10),
  wp(90),
  knows_common|knows_power_draw_2|knows_ironflesh_1,
  rhodok_face_young_1,
  rhodok_face_old_2
],

[
  "alpine_footman",
  "Alpine Footman",
  "Alpine Footmen",
  tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,
  0,
  0,
  fac_kingdom_5,
  [
    itm_crusader_sword,
    itm_sword_medieval_c_long,
    itm_sword_medieval_d_long,
    itm_grosse_messer,
    itm_shield_kite_i,
    itm_shield_kite_k,
    itm_alpine_footman_helmet_a,
    itm_alpine_footman_helmet_b,
    itm_alpine_footman_helmet_c,
    itm_m_alpine_corrazina_a,
    itm_m_alpine_corrazina_b,
    itm_m_gloves_a,
    itm_leather_gloves,
    itm_decorated_leather_gloves_a
  ],
  def_attrib|level(10),
  wp(90)|wp_one_handed(50),
  knows_common|knows_ironflesh_2|knows_shield_1|knows_power_strike_2|knows_athletics_1,
  rhodok_face_young_1,
  rhodok_face_old_2
],

[
  "alpine_swordsman",
  "Alpine Swordsman",
  "Alpine Swordsmen",
  tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
  0,
  0,
  fac_kingdom_5,
  [
    itm_crusader_sword,
    itm_morningstar,
    itm_grosse_messer_b,
    itm_german_bastard_sword,
    itm_shield_kite_i,
    itm_shield_kite_k,
    itm_alpine_footman_helmet_a,
    itm_alpine_footman_helmet_b,
    itm_alpine_footman_helmet_c,
    itm_m_alpine_corrazina_a,
    itm_m_alpine_corrazina_b,
    itm_m_alpine_corrazina_full_a,
    itm_m_alpine_corrazina_full_b,
    itm_m_gloves_a,
    itm_mail_mittens,
    itm_old_mail_gloves
  ],
  def_attrib|level(15),
  wp(120)|wp_one_handed(50),
  knows_common|knows_ironflesh_5|knows_shield_1|knows_power_strike_5|knows_athletics_1,
  rhodok_face_young_1,
  rhodok_face_old_2
],

[
  "alpine_elite_swordsman",
  "Alpine Elite Swordsman",
  "Alpine Elite Swordsmen",
  tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,
  0,
  0,
  fac_kingdom_5,
  [
    itm_crusader_sword,
    itm_morningstar,
    itm_grosse_messer_b,
    itm_german_bastard_sword,
    itm_shield_kite_i,
    itm_shield_kite_k,
    itm_alpine_footman_helmet_mail_a,
    itm_alpine_footman_helmet_mail_b,
    itm_alpine_footman_helmet_mail_c,
    itm_m_alpine_corrazina_full_a,
    itm_m_alpine_corrazina_full_b,
    itm_m_alpine_corrazina_full_c,
    itm_m_gloves_a,
    itm_mail_mittens,
    itm_old_mail_gloves
  ],
  def_attrib|level(20),
  wp(150)|wp_one_handed(50),
  knows_common|knows_ironflesh_8|knows_shield_6|knows_power_strike_8|knows_athletics_5,
  rhodok_face_young_1,
  rhodok_face_old_2
],

[
  "alpine_spearman",
  "Alpine Spearman",
  "Alpine Spearmen",
  tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,
  0,
  0,
  fac_kingdom_5,
  [
    itm_crusader_spear_inf_a,
    itm_crusader_spear_inf_b,
    itm_crusader_spear_inf_c,
    itm_tab_shield_pavise_b,
    itm_falchion,
    itm_shortened_bill,
    itm_alpine_footman_helmet_a,
    itm_alpine_footman_helmet_b,
    itm_alpine_footman_helmet_c,
    itm_alpine_chapel_padded_a,
    itm_alpine_chapel_padded_b,
    itm_alpine_chapel_padded_c,
    itm_alpine_chapel_padded_d,
    itm_alpine_leather_vest_a,
    itm_alpine_leather_vest_b,
    itm_m_gloves_a,
    itm_leather_gloves
  ],
  def_attrib|level(15),
  wp(120),
  knows_common|knows_ironflesh_2|knows_shield_1|knows_power_strike_2|knows_athletics_1,
  rhodok_face_young_1,
  rhodok_face_old_2
],

[
  "alpine_scout",
  "Alpine Scout",
  "Alpine Scouts",
  tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_horse,
  0,
  0,
  fac_kingdom_5,
  [
    itm_crusader_spear_inf_a,
    itm_crusader_spear_inf_b,
    itm_crusader_spear_inf_c,
    itm_m_mace_knight,
    itm_shield_heater_d,
    itm_m_mace_knight_pierce,
    itm_m_alpine_corrazina_a,
    itm_m_alpine_corrazina_b,
    itm_alpine_chapel_a,
    itm_alpine_chapel_b,
    itm_alpine_chapel_c,
    itm_m_gloves_a,
    itm_saddle_horse
  ],
  def_attrib|level(20),
  wp(150),
  knows_common|knows_ironflesh_5|knows_riding_4|knows_shield_3|knows_power_strike_4|knows_athletics_3,
  rhodok_face_young_1,
  rhodok_face_old_2
],

[
  "alpine_horseman",
  "Alpine Horseman",
  "Alpine Horsemen",
  tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_horse,
  0,
  0,
  fac_kingdom_5,
  [
    itm_crusader_knight_spear_a,
    itm_crusader_knight_spear_b,
    itm_shield_heater_d,
    itm_morningstar,
    itm_m_mace_knight,
    itm_m_mace_knight_pierce,
    itm_alpine_chapel_a,
    itm_alpine_chapel_b,
    itm_alpine_chapel_c,
    itm_m_alpine_corrazina_full_a,
    itm_m_alpine_corrazina_full_b,
    itm_m_alpine_corrazina_full_c,
    itm_m_gloves_a,
    itm_hunter
  ],
  def_attrib|level(25),
  wp(180),
  knows_common|knows_ironflesh_6|knows_shield_7|knows_power_strike_6|knows_riding_7,
  rhodok_face_young_1,
  rhodok_face_old_2
],

[
  "alpine_trained_spearman",
  "Alpine Trained Spearman",
  "Alpine Trained Spearmen",
  tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,
  0,
  0,
  fac_kingdom_5,
  [
    itm_crusader_spear_inf_a,
    itm_crusader_spear_inf_b,
    itm_crusader_spear_inf_c,
    itm_side_sword,
    itm_grosse_messer,
    itm_tab_shield_pavise_c,
    itm_alpine_chapel_mail_a,
    itm_alpine_chapel_mail_b,
    itm_alpine_footman_helmet_b,
    itm_alpine_footman_helmet_c,
    itm_alpine_footman_helmet_mail_a,
    itm_alpine_heavy_leather_vest_a,
    itm_alpine_heavy_leather_vest_b,
    itm_m_gloves_a
  ],
  def_attrib|level(20),
  wp(150)|wp_polearm(50),
  knows_common|knows_ironflesh_3|knows_shield_2|knows_power_strike_2|knows_athletics_2,
  rhodok_face_young_1,
  rhodok_face_older_2
],

[
  "alpine_veteran_spearman",
  "Alpine Veteran Spearman",
  "Alpine Veteran Spearmen",
  tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,
  0,
  0,
  fac_kingdom_5,
  [
    itm_crusader_spear_a,
    itm_crusader_spear_b,
    itm_crusader_spear_c,
    itm_italian_sword,
    itm_italian_falchion,
    itm_side_sword,
    itm_grosse_messer,
    itm_tab_shield_pavise_c,
    itm_alpine_footman_helmet_mail_a,
    itm_alpine_footman_helmet_mail_b,
    itm_alpine_footman_helmet_mail_c,
    itm_alpine_footman_helmet_b,
    itm_alpine_footman_helmet_c,
    itm_alpine_breastplate_a,
    itm_alpine_breastplate_b,
    itm_alpine_breastplate_c,
    itm_m_gauntlets_b,
    itm_m_gauntlets_a
  ],
  def_attrib|level(25),
  wp(180)|wp_polearm(50),
  knows_common|knows_ironflesh_5|knows_shield_3|knows_power_strike_4|knows_athletics_3,
  rhodok_face_young_1,
  rhodok_face_older_2
],

[
  "alpine_man_at_arms",
  "Alpine Man-at-Arms",
  "Alpine Men-at-Arms",
  tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,
  0,
  0,
  fac_kingdom_5,
  [
    itm_swiss_halberd,
    itm_crusader_spear_a,
    itm_crusader_spear_b,
    itm_crusader_spear_c,
    itm_italian_sword,
    itm_italian_falchion,
    itm_side_sword,
    itm_grosse_messer,
    itm_tab_shield_pavise_d,
    itm_alpine_chapel_mail_a,
    itm_alpine_chapel_mail_b,
    itm_alpine_chapel_mail_c,
    itm_alpine_chapel_mail_d,
    itm_alpine_footman_helmet_visored_mail_a,
    itm_alpine_footman_helmet_visored_mail_b,
    itm_alpine_footman_helmet_visored_a,
    itm_alpine_footman_helmet_visored_b,
    itm_m_alpine_full_plate_a,
    itm_m_alpine_full_plate_b,
    itm_alpine_breastplate_heavy_a,
    itm_alpine_breastplate_heavy_b,
    itm_m_gauntlets_b,
    itm_m_gauntlets_a
  ],
  def_attrib|level(30),
  wp(210)|wp_polearm(50),
  knows_common|knows_ironflesh_9|knows_shield_5|knows_power_strike_9|knows_athletics_6,
  rhodok_face_middle_1,
  rhodok_face_older_2
],

[
  "alpine_crossbowman",
  "Alpine Crossbowman",
  "Alpine Crossbowmen",
  tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,
  0,
  0,
  fac_kingdom_5,
  [
    itm_sword_medieval_a,
    itm_falchion,
    itm_club_with_spike_head,
    itm_tab_shield_pavise_b,
    itm_crossbow,
    itm_bolts,
    itm_m_alpine_aketon_a,
    itm_m_alpine_aketon_b,
    itm_alpine_chapel_a,
    itm_alpine_chapel_b,
    itm_alpine_chapel_c,
    itm_m_gloves_a
  ],
  def_attrib|level(15),
  wp(120)|wp_crossbow(50),
  knows_common|knows_ironflesh_2|knows_shield_1|knows_power_strike_1|knows_athletics_2,
  rhodok_face_young_1,
  rhodok_face_older_2
],

[
  "alpine_trained_crossbowman",
  "Alpine Trained Crossbowman",
  "Alpine Trained Crossbowmen",
  tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,
  0,
  0,
  fac_kingdom_5,
  [
    itm_sword_medieval_a,
    itm_sword_medieval_b_small,
    itm_club_with_spike_head,
    itm_tab_shield_pavise_b,
    itm_crossbow,
    itm_bolts,
    itm_alpine_chapel_padded_a,
    itm_alpine_chapel_padded_b,
    itm_alpine_chapel_padded_c,
    itm_m_alpine_corrazina_a,
    itm_m_alpine_corrazina_b,
    itm_m_gloves_a
  ],
  def_attrib|level(20),
  wp(150)|wp_crossbow(50),
  knows_common|knows_ironflesh_1|knows_shield_2|knows_power_strike_2|knows_athletics_3,
  rhodok_face_young_1,
  rhodok_face_older_2
],

[
  "alpine_veteran_crossbowman",
  "Alpine Veteran Crossbowman",
  "Alpine Veteran Crossbowmen",
  tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,
  0,
  0,
  fac_kingdom_5,
  [
    itm_sword_medieval_a,
    itm_sword_medieval_b_small,
    itm_fighting_pick,
    itm_club_with_spike_head,
    itm_tab_shield_pavise_b,
    itm_tab_shield_pavise_c,
    itm_heavy_crossbow,
    itm_bolts,
    itm_m_alpine_corrazina_a,
    itm_m_alpine_corrazina_full_b,
    itm_m_alpine_corrazina_full_c,
    itm_alpine_leather_vest_a,
    itm_alpine_heavy_leather_vest_a,
    itm_alpine_chapel_mail_a,
    itm_alpine_chapel_mail_b,
    itm_m_gloves_a
  ],
  def_attrib|level(25),
  wp(180)|wp_crossbow(50),
  knows_common|knows_ironflesh_2|knows_shield_3|knows_power_strike_3|knows_athletics_4,
  rhodok_face_middle_1,
  rhodok_face_older_2
],

[
  "alpine_sharpshooter",
  "Alpine Sharpshooter",
  "Alpine Sharpshooters",
  tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,
  0,
  0,
  fac_kingdom_5,
  [
    itm_sword_medieval_b,
    itm_military_pick,
    itm_military_hammer,
    itm_tab_shield_pavise_c,
    itm_sniper_crossbow,
    itm_steel_bolts,
    itm_m_alpine_corrazina_b,
    itm_m_alpine_corrazina_full_a,
    itm_m_alpine_corrazina_full_b,
    itm_m_alpine_corrazina_full_c,
    itm_alpine_heavy_leather_vest_a,
    itm_alpine_heavy_leather_vest_b,
    itm_alpine_breastplate_a,
    itm_alpine_breastplate_b,
    itm_alpine_breastplate_c,
    itm_alpine_breastplate_d,
    itm_alpine_chapel_mail_a,
    itm_alpine_chapel_mail_b,
    itm_m_gloves_a
  ],
  def_attrib|level(30),
  wp(210)|wp_crossbow(50),
  knows_common|knows_ironflesh_3|knows_shield_4|knows_power_strike_4|knows_athletics_6,
  rhodok_face_middle_1,
  rhodok_face_older_2
],

["rhodok_messenger","Rhodok Messenger","Rhodok Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_5,
   [itm_sword_medieval_b,itm_leather_jerkin,itm_courser,itm_leather_gloves,itm_short_bow,itm_arrows],
   def_attrib|agi_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,rhodok_face_middle_1, rhodok_face_older_2],
["rhodok_deserter","Rhodok Deserter","Rhodok Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
  [itm_arrows,itm_spiked_mace,itm_axe,itm_falchion,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_javelin,itm_javelin,itm_steppe_cap,itm_nomad_cap,itm_leather_vest,itm_leather_vest,itm_nomad_armor],
   def_attrib|str_10|level(14),wp(80),knows_ironflesh_1|knows_power_draw_1,rhodok_face_middle_1, rhodok_face_older_2],
["rhodok_prison_guard","Prison Guard","Prison Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_5,
  [itm_ashwood_pike,itm_battle_fork,itm_battle_axe,itm_fighting_axe,itm_tab_shield_pavise_b,itm_bascinet_2,itm_m_celestial_plate_b,itm_leather_gloves],
   def_attrib|level(24),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,rhodok_face_middle_1, rhodok_face_older_2],
["rhodok_castle_guard","Castle Guard","Castle Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_5,
  [itm_ashwood_pike,itm_battle_fork,itm_battle_axe,itm_fighting_axe,itm_tab_shield_pavise_c,itm_bascinet_2,itm_m_celestial_plate_b,itm_leather_gloves],
  def_attrib|level(24),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,rhodok_face_middle_1, rhodok_face_older_2],
#peasant - retainer - footman - man-at-arms -  knight

[
  "solarian_recruit",
  "Solarian Recruit",
  "Solarian Recruits",
  tf_guarantee_boots|tf_guarantee_armor,
  0,
  0,
  fac_kingdom_6,
  [
    itm_solarian_spear_a,
    itm_hatchet,
    itm_club,
    itm_stones,
    itm_solarian_round_shield_a,
    itm_solarian_turban_a,
    itm_solarian_turban_b,
    itm_solarian_turban_c,
    itm_solarian_aketon_a,
    itm_solarian_aketon_b,
    itm_solarian_robe_a,
    itm_solarian_robe_b,
    itm_solarian_robe_c
  ],
  def_attrib|level(5),
  wp(60),
  knows_common|knows_athletics_1,
  swadian_face_younger_1,
  swadian_face_middle_2
],

[
  "solarian_footman",
  "Solarian Footman",
  "Solarian Footmen",
  tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,
  0,
  0,
  fac_kingdom_6,
  [
    itm_solarian_spear_b,
    itm_falshion_2,
    itm_solarian_round_shield_a,
    itm_solarian_turban_a,
    itm_solarian_turban_b,
    itm_solarian_turban_c,
    itm_solarian_helmet_a,
    itm_solarian_helmet_b,
    itm_solarian_helmet_c,
    itm_solarian_helmet_d,
    itm_solarian_scale_vest_a,
    itm_solarian_scale_vest_b,
    itm_solarian_scale_vest_c,
    itm_solarian_scale_vest_d,
    itm_solarian_scale_vest_e,
    itm_leather_gloves
  ],
  def_attrib|level(10),
  wp(90),
  knows_common|knows_athletics_2,
  swadian_face_young_1,
  swadian_face_old_2
],

[
  "solarian_veteran_footman",
  "Solarian Veteran Footman",
  "Solarian Veteran Footmen",
  tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,
  0,
  0,
  fac_kingdom_6,
  [
    itm_solarian_spear_b,
    itm_arabian_sword_a,
    itm_arabian_sword_b,
    itm_jarid,
    itm_arabian_sword_a,
    itm_mace_3,
    itm_solarian_round_shield_a,
    itm_solarian_helmet_warrior_a,
    itm_solarian_helmet_warrior_b,
    itm_solarian_mail_vest_a,
    itm_solarian_mail_vest_b,
    itm_solarian_mail_vest_c,
    itm_solarian_mail_vest_d,
    itm_solarian_mail_vest_e,
    itm_solarian_mail_vest_f,
    itm_leather_gloves,
    itm_eastern_scale_gloves_a
  ],
  def_attrib|level(15),
  wp(120),
  knows_common|knows_athletics_2|knows_power_throw_2|knows_ironflesh_1|knows_power_strike_2|knows_shield_2,
  swadian_face_young_1,
  swadian_face_old_2
],

[
  "solarian_infantry",
  "Solarian Infantry",
  "Solarian Infantries",
  tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,
  0,
  0,
  fac_kingdom_6,
  [
    itm_jarid,
    itm_sarranid_axe_a,
    itm_arabian_sword_b,
    itm_mace_3,
    itm_solarian_spear_b,
    itm_solarian_round_shield_a,
    itm_solarian_ridge_helmet_a,
    itm_solarian_ridge_helmet_b,
    itm_solarian_ridge_helmet_c,
    itm_solarian_armor_a,
    itm_solarian_armor_b,
    itm_solarian_armor_c,
    itm_solarian_armor_d,
    itm_mail_mittens,
    itm_eastern_scale_gloves_a,
    itm_eastern_scale_gloves_b
  ],
  def_attrib|level(20),
  wp(150),
  knows_common|knows_riding_3|knows_ironflesh_2|knows_power_strike_3|knows_shield_3 | knows_power_throw_3|knows_athletics_3,
  swadian_face_middle_1,
  swadian_face_old_2
],

[
  "solarian_guard",
  "Solarian Guard",
  "Solarian Guards",
  tf_mounted|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,
  0,
  0,
  fac_kingdom_6,
  [
    itm_military_pick,
    itm_sarranid_two_handed_axe_a,
    itm_jarid,
    itm_scimitar_b,
    itm_solarian_spear_b,
    itm_mace_4,
    itm_solarian_oval_shield_a,
    itm_solarian_oval_shield_b,
    itm_solarian_heavy_helmet_a,
    itm_solarian_heavy_helmet_b,
    itm_solarian_heavy_helmet_c,
    itm_solarian_heavy_helmet_d,
    itm_solarian_heavy_helmet_e,
    itm_solarian_armor_scale_a,
    itm_solarian_armor_scale_b,
    itm_solarian_armor_scale_c,
    itm_eastern_scale_gloves_b
  ],
  def_attrib|level(25),
  wp(180),
  knows_common|knows_shield_3|knows_ironflesh_10|knows_power_strike_8|knows_power_throw_4|knows_athletics_9,
  swadian_face_middle_1,
  swadian_face_older_2
],

[
  "solarian_skirmisher",
  "Solarian Skirmisher",
  "Solarian Skirmishers",
  tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,
  0,
  0,
  fac_kingdom_6,
  [
    itm_jarid,
    itm_jarid,
    itm_arabian_sword_a,
    itm_spiked_club,
    itm_solarian_oval_shield_a,
    itm_solarian_turban_a,
    itm_solarian_turban_b,
    itm_solarian_turban_c,
    itm_solarian_aketon_a,
    itm_solarian_aketon_b,
    itm_leather_gloves,
    itm_old_leather_gloves
  ],
  def_attrib|level(15),
  wp(120),
  knows_common|knows_riding_2|knows_power_throw_2|knows_ironflesh_1|knows_athletics_3,
  swadian_face_young_1,
  swadian_face_middle_2
],

[
  "solarian_archer",
  "Solarian Archer",
  "Solarian Archers",
  tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,
  0,
  0,
  fac_kingdom_6,
  [
    itm_arrows,
    itm_arrows,
    itm_nomad_bow,
    itm_arabian_sword_a,
    itm_solarian_turban_a,
    itm_solarian_turban_b,
    itm_solarian_turban_c,
    itm_solarian_robe_a,
    itm_solarian_robe_b,
    itm_solarian_robe_c,
    itm_leather_gloves,
    itm_old_leather_gloves
  ],
  def_attrib|level(20),
  wp(150),
  knows_common|knows_power_draw_3|knows_ironflesh_2|knows_power_throw_3|knows_athletics_4,
  swadian_face_young_1,
  swadian_face_old_2
],

[
  "solarian_master_archer",
  "Solarian Master Archer",
  "Solarian Master Archers",
  tf_guarantee_ranged|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,
  0,
  0,
  fac_kingdom_6,
  [
    itm_barbed_arrows,
    itm_barbed_arrows,
    itm_arabian_sword_b,
    itm_mace_3,
    itm_strong_bow,
    itm_nomad_bow,
    itm_solarian_ridge_helmet_a,
    itm_solarian_ridge_helmet_b,
    itm_solarian_ridge_helmet_c,
    itm_solarian_armor_a,
    itm_solarian_armor_b,
    itm_leather_gloves,
    itm_old_leather_gloves
  ],
  def_attrib|level(25),
  wp(180),
  knows_common|knows_power_draw_4|knows_power_throw_4|knows_ironflesh_3|knows_athletics_5,
  swadian_face_middle_1,
  swadian_face_older_2
],

[
  "solarian_horseman",
  "Solarian Horseman",
  "Solarian Horsemen",
  tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,
  0,
  0,
  fac_kingdom_6,
  [
    itm_arabian_sword_b,
    itm_scimitar_b,
    itm_mace_4,
    itm_solarian_lance_a,
    itm_solarian_lance_b,
    itm_solarian_oval_shield_c,
    itm_solarian_ridge_helmet_a,
    itm_solarian_ridge_helmet_b,
    itm_solarian_ridge_helmet_c,
    itm_solarian_armor_a,
    itm_solarian_armor_b,
    itm_solarian_armor_c,
    itm_solarian_armor_d,
    itm_eastern_scale_gloves_a,
    itm_old_mail_gloves,
    itm_mail_mittens,
    itm_saracin_hard_horses_a_v1,
    itm_saracin_hard_horses_b_v1,
    itm_saracin_hard_horses_c_v1,
    itm_saracin_hard_horses_d_v1
  ],
  def_attrib|level(20),
  wp_melee(150),
  knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3,
  swadian_face_young_1,
  swadian_face_old_2
],

[
  "solarian_knight",
  "Solarian Knight",
  "Solarian Knights",
  tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,
  0,
  0,
  fac_kingdom_6,
  [
    itm_solarian_lance_c,
    itm_solarian_lance_d,
    itm_scimitar_b,
    itm_sarranid_two_handed_mace_1,
    itm_sarranid_cavalry_sword,
    itm_solarian_oval_shield_d,
    itm_solarian_oval_shield_c,
    itm_solarian_helmet_mask_a,
    itm_solarian_helmet_mask_b,
    itm_solarian_armor_scale_a,
    itm_solarian_armor_scale_b,
    itm_solarian_armor_scale_c,
    itm_eastern_scale_gloves_b,
    itm_eastern_scale_gloves_a,
    itm_saracin_hard_horses_a,
    itm_saracin_hard_horses_b,
    itm_saracin_hard_horses_c,
    itm_saracin_hard_horses_d
  ],
  def_attrib|level(25),
  wp_melee(180),
  knows_common|knows_riding_6|knows_shield_5|knows_ironflesh_8|knows_power_strike_9,
  swadian_face_middle_1,
  swadian_face_older_2
],

["sarranid_messenger","Sarranid Messenger","Sarranid Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_6,
[itm_lance,itm_arabian_sword_b,itm_scimitar_b,itm_mace_4,itm_tab_shield_small_round_b,
itm_solarian_armor_scale_a,itm_solarian_helmet_a,itm_courser,itm_hunter],
def_attrib|level(20),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
["sarranid_deserter","Sarranid Deserter","Sarranid Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
[itm_lance,itm_arabian_sword_b,itm_scimitar_b,itm_mace_4,itm_tab_shield_small_round_b,
itm_solarian_armor_scale_a,itm_solarian_turban_c,itm_arabian_horse_a],
def_attrib|level(20),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
["sarranid_prison_guard","Prison Guard","Prison Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_6,
[itm_arabian_sword_b,itm_scimitar_b,itm_war_spear,itm_mace_4,itm_solarian_armor_a,itm_solarian_helmet_a,itm_solarian_helmet_a,itm_solarian_helmet_warrior_a,itm_mail_mittens,itm_leather_gloves,itm_tab_shield_kite_d],
def_attrib|level(25),wp_melee(135)|wp_throwing(100),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,swadian_face_middle_1, swadian_face_older_2],
["sarranid_castle_guard","Castle Guard","Castle Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_6,
[itm_arabian_sword_b,itm_scimitar_b,itm_war_spear,itm_mace_4,itm_solarian_armor_a,itm_solarian_helmet_a,itm_solarian_helmet_a,itm_solarian_helmet_warrior_a,itm_mail_mittens,itm_leather_gloves,itm_tab_shield_kite_d],
def_attrib|level(25),wp_melee(135)|wp_throwing(100),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,swadian_face_middle_1, swadian_face_older_2],

  #        Looter
  #        /        \
  #      Bandit   Outlaw
  #      /      \         /    
  # Pillager   Marauder  Highwayman
  #                     |
  #               Bandit Lord
  ["looter","Looter","Looters",tf_guarantee_armor|tf_guarantee_boots,0,0,fac_outlaws,
   [itm_stormguard_aketon_a, itm_stormguard_aketon_plated_a, itm_stormguard_aketon_b, itm_m_aketon_a, itm_neutral_aketon_a, itm_neutral_aketon_b, itm_stormguard_aketon_a, itm_stormguard_aketon_b, itm_m_plain_round_shield_a, itm_m_plain_round_shield_b, itm_m_plain_round_shield_c, itm_m_plain_round_shield_d, itm_m_plain_round_shield_e, itm_grosse_messer, itm_falchion, itm_italian_falchion, itm_boar_spear, itm_head_wrappings, itm_leather_cap, itm_black_hood, itm_black_hood, itm_arming_cap, itm_arming_cap, itm_m_coif_cloth_a, itm_m_coif_cloth_b, itm_m_swadia_common_helmet_b, itm_padded_coif_full, itm_leather_gloves],
   def_attrib|level(5),wp(60),knows_common,bandit_face1, bandit_face2],
  ["bandit","Bandit","Bandits",tf_guarantee_armor|tf_guarantee_boots,0,0,fac_outlaws, [itm_stormguard_aketon_plated_a, itm_stormguard_aketon_b, itm_neutral_aketon_c, itm_stormguard_hauberk_a, itm_hauberk_neutral_a, itm_m_plain_round_shield_a, itm_m_plain_round_shield_b, itm_m_plain_round_shield_c, itm_m_plain_round_shield_d, itm_m_plain_round_shield_e,itm_grosse_messer_b, itm_italian_falchion, itm_partisan, itm_guisarme, itm_german_hunting_spear, itm_hunting_crossbow, itm_bolts, itm_m_swadia_common_helmet_b, itm_m_swadia_common_helmet_a, itm_m_swadia_common_helmet_c, itm_m_coif_alternate_a, itm_leather_gloves, itm_m_gloves_a], def_attrib|level(10),wp(90),knows_common|knows_power_draw_1,bandit_face1, bandit_face2],

  ["pillager","Pillager","Pillagers",tf_guarantee_all,0,0,fac_outlaws, [itm_m_hauberk_a, itm_m_hauberk_b, itm_m_hauberk_c, itm_m_gloves_a, itm_tab_shield_heater_b, itm_grosse_messer, itm_italian_falchion, itm_italian_sword, itm_heavy_crossbow, itm_steel_bolts, itm_padded_coif, itm_mail_coif, itm_kettle_hat], def_attrib|level(12),wp(70),knows_common|knows_power_draw_1|knows_riding_2,bandit_face1, bandit_face2],

  ["marauder","Marauder","Marauders",tf_guarantee_all,0,0,fac_outlaws, [itm_m_brigandine_b, itm_german_poleaxe, itm_simple_poleaxe, itm_elegant_poleaxe, itm_english_bill, itm_swiss_halberd, itm_bascinet, itm_bascinet_2, itm_bascinet_3], def_attrib|level(16),wp(90),knows_common|knows_power_draw_1|knows_riding_2,bandit_face1, bandit_face2],

  ["outlaw","Outlaw","Outlaws",tf_guarantee_all,0,0,fac_outlaws, [itm_m_aketon_a, itm_m_aketon_b, itm_m_hauberk_a, itm_tab_shield_small_round_a, itm_tab_shield_small_round_b, itm_grosse_messer, itm_espada_eslavona_a,itm_espada_eslavona_b, itm_milanese_sword, itm_spear, itm_hunting_crossbow, itm_bolts, itm_saddle_horse], def_attrib|level(10),wp(60),knows_common|knows_riding_2,bandit_face1, bandit_face2],
  ["highwayman","Highwayman","Highwaymen",tf_guarantee_all,0,0,fac_outlaws, [itm_m_hauberk_a, itm_m_hauberk_b, itm_m_hauberk_c, itm_m_brigandine_c, itm_m_brigandine_e, itm_tab_shield_small_round_c, itm_grosse_messer_b, itm_italian_falchion, itm_italian_sword, itm_partisan, itm_guisarme, itm_lance, itm_hunting_crossbow, itm_bolts, itm_saddle_horse], def_attrib|level(16),wp(90),knows_common|knows_riding_5|knows_riding_2,bandit_face1, bandit_face2],
  ["bandit_lord","Bandit Lord","Bandit Lords",tf_guarantee_all,0,0,fac_outlaws, [itm_m_gauntlets_a, itm_shirt, itm_hunting_crossbow, itm_bolts, itm_warhorse], knight_attrib_5|level(25),wp(245),knows_common|knows_power_draw_1|knows_riding_5|knows_ironflesh_10|knows_power_strike_6,bandit_face1, bandit_face2],

  ["cultist_acolyte","Twilight Veil Acolyte","Twilight Veil Acolytes",tf_guarantee_all,0,0,fac_outlaws, [itm_old_leather_gloves, itm_robe, itm_pilgrim_disguise, itm_mt_hood_a3, itm_pilgrim_hood, itm_studded_club, itm_pickaxe, itm_one_handed_battle_axe_c, itm_tab_shield_pavise_a], def_attrib|str_15|agi_15|level(12),wp(100),knows_common|knows_ironflesh_3,bandit_face1, bandit_face2],
  ["dark_cultist","Twilight Veil Cultist","Twilight Veil Cultists",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_outlaws, [itm_old_mail_gloves, itm_robe, itm_pilgrim_disguise, itm_mt_hood_a3, itm_pilgrim_hood, itm_winged_mace, itm_morningstar, itm_one_handed_battle_axe_c, itm_tab_shield_pavise_a], def_attrib|str_15|agi_15|level(17), wp(140), knows_common|knows_ironflesh_3, bandit_face1, bandit_face2],
  ["occultist","Twilight Veil Occultist","Twilight Veil Occultists",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws, [itm_old_mail_gloves, itm_robe, itm_pilgrim_disguise, itm_heretics_coif_a, itm_heretics_coif_b, itm_winged_mace, itm_morningstar, itm_one_handed_battle_axe_c, itm_crusader_spear_inf_a, itm_crusader_spear_inf_b, itm_crusader_spear_inf_c, itm_tab_shield_pavise_a, itm_tab_shield_pavise_b], def_attrib|str_20|agi_20|level(24), wp(240), knows_common|knows_ironflesh_5, bandit_face1, bandit_face2],
  ["veilweaver", "Veilweaver", "Veilweavers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws, [itm_old_mail_gloves, itm_robe_on_mail_a, itm_robe_on_mail_b, itm_heretics_coif_a, itm_heretics_coif_b, itm_winged_mace, itm_morningstar, itm_one_handed_battle_axe_c, itm_crusader_spear_inf_a, itm_crusader_spear_inf_b, itm_crusader_spear_inf_c, itm_tab_shield_pavise_c, itm_tab_shield_pavise_b], def_attrib|str_26|agi_25|level(28), wp(320), knows_common|knows_ironflesh_10|knows_power_strike_8, bandit_face1, bandit_face2],
  ["veiled_inquisitor", "Veiled Inquisitor", "Veiled Inquisitors", tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws, [itm_mt_gauntlets_a, itm_robe_on_mail_a, itm_robe_on_mail_b, itm_great_helmet_heretics, itm_winged_mace, itm_morningstar, itm_one_handed_battle_axe_c, itm_lance, itm_tab_shield_tauria_a, itm_black_knight_horse_a], def_attrib|str_30|agi_25|level(28), wp(320), knows_common|knows_ironflesh_10|knows_power_strike_8, bandit_face1, bandit_face2],


  ["brigand","Brigand","Brigands",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_outlaws,
   [itm_arrows,itm_spiked_mace,itm_sword_viking_1,itm_falchion,itm_wooden_shield,itm_hide_covered_round_shield,itm_long_bow,itm_leather_cap,itm_leather_jerkin,itm_saddle_horse],
   def_attrib|level(16),wp(90),knows_common|knows_power_draw_3,bandit_face1, bandit_face2],
  ["mountain_bandit","Mountain Bandit","Mountain Bandits",tf_guarantee_armor|tf_guarantee_boots,0,0,fac_outlaws,
   [itm_arrows,itm_sword_viking_1,itm_boar_spear,itm_hatchet,itm_hand_axe,itm_falchion,itm_short_bow,itm_javelin,itm_spiked_club,itm_fur_covered_shield,itm_hide_covered_round_shield,
    itm_arming_cap,itm_black_hood,itm_m_coif_cloth_a,itm_m_hauberk_mountain_a,itm_m_hauberk_mountain_b,itm_m_hauberk_mountain_c,itm_m_hauberk_mountain_d],
   def_attrib|level(11),wp(90),knows_common|knows_power_draw_2,rhodok_face_young_1, rhodok_face_old_2],
  ["forest_bandit","Forest Bandit","Forest Bandits",tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_boots,0,0,fac_outlaws,
   [itm_arrows,itm_shortened_voulge,itm_one_handed_battle_axe_a,itm_hunting_bow,
    itm_felt_hat_b, itm_itm_felt_hat_a, itm_itm_felt_hat_b, itm_itm_felt_hat_c, itm_itm_felt_hat_d, itm_m_aketon_forest_a, itm_m_aketon_forest_b, itm_m_aketon_forest_c, itm_m_gloves_a, itm_leather_gloves],
   def_attrib|level(11),wp(90),knows_common|knows_power_draw_3,swadian_face_young_1, swadian_face_old_2],
  ["sea_raider","Sea Raider","Sea Raiders",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_outlaws,
   [itm_arrows,itm_sword_viking_1,itm_sword_viking_2,itm_fighting_axe,itm_war_axe,itm_battle_axe,itm_spear,itm_war_spear,itm_tab_shield_round_b,itm_tab_shield_round_c,itm_long_bow,itm_javelin,itm_throwing_axes,itm_m_hauberk_navy_a,itm_m_hauberk_navy_b,itm_m_hauberk_navy_c,itm_m_brigandine_navy_c],
   def_attrib|level(16),wp(110),knows_ironflesh_2|knows_power_strike_2|knows_power_draw_3|knows_power_throw_2|knows_riding_1|knows_athletics_2,nord_face_young_1, nord_face_old_2],
  ["steppe_bandit","Steppe Bandit","Steppe Bandits",tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_helmet|tf_mounted,0,0,fac_outlaws,
   [itm_arrows,itm_sword_khergit_1,itm_winged_mace,itm_spear, itm_light_lance,itm_nomad_bow,itm_nomad_bow,itm_short_bow,itm_jarid,itm_stepper_nomad_helmet_a,itm_stepper_nomad_helmet_b,itm_tribe_vest_a,itm_tribe_vest_b,itm_leather_covered_round_shield,itm_leather_covered_round_shield,  itm_saddle_horse,itm_steppe_horse,itm_steppe_horse],
   def_attrib|level(12),wp(100),knows_riding_4|knows_horse_archery_3|knows_power_draw_3,khergit_face_young_1, khergit_face_old_2],
  ["steppe_bandit_warrior","Steppe Warrior Bandit","Steppe Warrior Bandits",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_helmet|tf_mounted,0,0,fac_outlaws,
   [itm_arrows,itm_sword_khergit_1, itm_sword_khergit_2, itm_winged_mace, itm_spear, itm_light_lance,itm_nomad_bow,itm_nomad_bow,itm_short_bow,itm_jarid,itm_stepper_nomad_helmet_c,itm_stepper_nomad_helmet_d,itm_tribe_vest_c,itm_tribe_armor_a, itm_tribe_armor_b, itm_leather_covered_round_shield,itm_leather_covered_round_shield,  itm_steppe_horse,itm_steppe_horse_b],
   def_attrib|level(15),wp(130),knows_riding_4|knows_horse_archery_5|knows_power_draw_5,khergit_face_young_1, khergit_face_old_2],
  ["steppe_bandit_leader","Steppe Bandit Leader","Steppe Bandit Leaders",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_helmet|tf_mounted,0,0,fac_outlaws,
   [itm_khergit_arrows, itm_barbed_arrows, itm_sword_khergit_3, itm_sword_khergit_4, itm_lance, itm_khergit_bow,itm_nomad_bow, itm_strong_bow, itm_jarid, itm_stepper_nomad_helmet_e , itm_tribe_armor_c, itm_tribe_armor_d, itm_leather_covered_round_shield,itm_leather_covered_round_shield, itm_steppe_horse,itm_steppe_horse_b],
   def_attrib|level(25),wp(230),knows_riding_6|knows_horse_archery_6|knows_power_draw_6|knows_ironflesh_6,khergit_face_young_1, khergit_face_old_2],
  ["taiga_bandit","Taiga Bandit","Taiga Bandits",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_outlaws,
   [itm_arrows, itm_sword_khergit_1, itm_winged_mace, itm_spear, itm_light_lance, itm_nomad_bow, itm_nomad_bow,itm_short_bow, itm_jarid, itm_javelin, itm_nomad_cap, itm_fur_hat, itm_nomad_cap_b, itm_pilgrim_hood, itm_padded_coif, itm_leather_vest, itm_leather_vest_reinfoced, itm_chornovalley_vest_c, itm_red_tunic, itm_ragged_outfit, itm_tribal_warrior_outfit, itm_leather_covered_round_shield, itm_leather_covered_round_shield],
   def_attrib|level(15),wp(110),knows_common|knows_power_draw_4|knows_power_throw_3,vaegir_face_young_1, vaegir_face_old_2],

  ["desert_bandit","Piaktu Bandit","Piaktu Bandits",tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_outlaws,
   [itm_arrows, itm_arabian_sword_a, itm_winged_mace, itm_spear, itm_jarid, itm_nomad_bow, itm_short_bow, itm_jarid, itm_m_desert_bandit_a, itm_m_desert_bandit_b, itm_m_desert_bandit_c, itm_m_desert_bandit_d, itm_m_bandit_turban_a, itm_m_bandit_turban_b, itm_m_bandit_turban_c, itm_m_bandit_turban_d, itm_leather_gloves, itm_leather_covered_round_shield, itm_leather_covered_round_shield],
   def_attrib|level(12),wp(100),knows_riding_4|knows_power_draw_3,khergit_face_young_1, khergit_face_old_2],
  ["desert_bandit_master","Piaktu Assasin","Piaktu Assasins",tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_outlaws,
   [itm_arrows, itm_arabian_sword_a, itm_arabian_sword_b, itm_arabian_sword_c, itm_solarian_spear_a, itm_solarian_spear_b, itm_jarid, itm_nomad_bow, itm_short_bow, itm_jarid, itm_m_desert_bandit_a, itm_m_desert_bandit_b, itm_m_desert_bandit_c, itm_m_desert_bandit_d, itm_piaktu_mask_a, itm_piaktu_mask_b, itm_decorated_leather_gloves_a,  itm_solarian_oval_shield_a, itm_solarian_oval_shield_b, itm_solarian_round_shield_a, itm_solarian_round_shield_b],
   def_attrib|level(18),wp(160),knows_riding_4|knows_power_draw_3,khergit_face_young_1, khergit_face_old_2],
  ["desert_bandit_horseman","Piaktu Horseman","Piaktu Horsemen",tf_guarantee_armor|tf_guarantee_helmet|tf_mounted|tf_guarantee_horse,0,0,fac_outlaws,
   [itm_arabian_sword_a, itm_arabian_sword_b, itm_arabian_sword_c, itm_solarian_lance_a, itm_solarian_lance_b, itm_piaktu_coat_a, itm_piaktu_coat_b, itm_piaktu_mask_d, itm_piaktu_mask_c, itm_mail_mittens, itm_m_gloves_a,  itm_solarian_oval_shield_a, itm_solarian_oval_shield_b, itm_solarian_round_shield_a, itm_solarian_round_shield_b, itm_arabian_horse_a, itm_arabian_horse_b],
   def_attrib|level(21),wp(180),knows_riding_4|knows_power_strike_3|knows_ironflesh_4,khergit_face_young_1, khergit_face_old_2],
  ["desert_bandit_ronin","Piaktu Ronin","Piaktu Ronins",tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_outlaws,
   [itm_khergit_sword_two_handed_a, itm_khergit_sword_two_handed_b, itm_piaktu_ronin_armor_a, itm_piaktu_ronin_armor_b, itm_piaktu_helmet_a, itm_piaktu_helmet_b, itm_piaktu_helmet_c, itm_eastern_scale_gloves_a, itm_eastern_scale_gloves_b],
   def_attrib|level(21),wp(180),knows_athletics_4|knows_power_strike_3|knows_ironflesh_5,khergit_face_young_1, khergit_face_old_2],
  ["desert_bandit_leader","Piaktu Leader","Piaktu Leaders",tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_mounted|tf_guarantee_horse,0,0,fac_outlaws,
   [itm_khergit_sword_two_handed_a, itm_khergit_sword_two_handed_b, itm_sarranid_cavalry_sword, itm_arabian_sword_d, itm_arabian_sword_c, itm_solarian_lance_c, itm_solarian_lance_d, itm_piaktu_leader_armor_a, itm_piaktu_leader_helmet_a, itm_eastern_scale_gloves_a, itm_eastern_scale_gloves_b, itm_solarian_oval_shield_a, itm_solarian_oval_shield_b, itm_solarian_round_shield_a, itm_solarian_round_shield_b, itm_saracin_hard_horses_a, itm_saracin_hard_horses_d],
   def_attrib|level(27),wp(240),knows_riding_4|knows_athletics_4|knows_power_strike_3|knows_ironflesh_5,khergit_face_young_1, khergit_face_old_2],

  ["black_celestial_armsman","Black Khergit Horseman","Black Khergit Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_black_khergits,
   [itm_arrows,itm_sword_khergit_2,itm_scimitar,itm_scimitar,itm_winged_mace,itm_spear,itm_lance,itm_khergit_bow,itm_khergit_bow,itm_nomad_bow,itm_nomad_bow,itm_steppe_cap,itm_nomad_cap,itm_khergit_war_helmet,itm_khergit_war_helmet,itm_mail_hauberk,itm_chornovalley_heavy_mail_b,itm_plate_covered_round_shield,itm_plate_covered_round_shield,itm_saddle_horse,itm_steppe_horse],
   def_attrib|level(21),wp(100),knows_riding_3|knows_ironflesh_3|knows_horse_archery_3|knows_power_draw_3,khergit_face_young_1, khergit_face_old_2],

  ["manhunter","Manhunter","Manhunters",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_manhunters,
   [itm_mace_3,itm_winged_mace,itm_footman_helmet,itm_padded_cloth,itm_aketon_green,itm_aketon_green,itm_wooden_shield,itm_sumpter_horse],
   def_attrib|level(10),wp(50),knows_common,bandit_face1, bandit_face2],
  ["slave_driver","Slave Driver","Slave Drivers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse ,0,0,fac_slavers,
   [itm_club_with_spike_head,itm_bascinet_3,itm_tribal_warrior_outfit,itm_nordic_shield,itm_leather_gloves,itm_steppe_horse],
   def_attrib|level(14),wp(80),knows_common,bandit_face1, bandit_face2],
  ["slave_hunter","Slave Hunter","Slave Hunters",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield ,0,0,fac_slavers,
   [itm_winged_mace,itm_maul,itm_kettle_hat,itm_stormguard_hauberk_a,itm_tab_shield_round_c,itm_leather_gloves,itm_courser],
   def_attrib|level(18),wp(90),knows_common,bandit_face1, bandit_face2],
  ["slave_crusher","Slave Crusher","Slave Crushers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield ,0,0,fac_slavers,
   [itm_sledgehammer,itm_spiked_mace,itm_mail_hauberk,itm_bascinet_2,itm_bascinet_3,itm_mail_mittens,itm_tab_shield_round_d,itm_hunter],
   def_attrib|level(22),wp(110),knows_common|knows_riding_4|knows_power_strike_3,bandit_face1, bandit_face2],
  ["slaver_chief","Slaver Chief","Slaver Chiefs",tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac_slavers,
   [itm_military_hammer,itm_warhammer,itm_brigandine_red,itm_steel_shield,itm_scale_gauntlets,itm_mail_mittens,itm_bascinet_3,itm_warhorse],
   def_attrib|level(26),wp(130),knows_common|knows_riding_4|knows_power_strike_5,bandit_face1, bandit_face2],

  # SUMMONED TROOPS BEGIN
  ["minor_summoned_entity","Minor Summoned Entity","Minor Summoned Entities",tf_awakened,0,0,fac_outlaws,[itm_hunting_bow, itm_arrows, itm_stones, itm_hunting_crossbow, itm_bolts, itm_falchion, itm_dagger, itm_cleaver, itm_knife, itm_wooden_stick, itm_shortened_spear, itm_tab_shield_round_a, itm_tab_shield_tauria_a], def_attrib|level(1),wp(50),knows_common|knows_power_draw_2|knows_power_throw_2,skeleton_face1, skeleton_face1],
  # SUMMONED TROOPS END

  ["follower_woman","Camp Follower","Camp Follower",tf_female|tf_guarantee_armor,0,0,fac_commoners,
   [itm_bolts,itm_light_crossbow,itm_short_bow,itm_crossbow,itm_nordic_shield,itm_hide_covered_round_shield,itm_hatchet,itm_hand_axe,itm_voulge,itm_fighting_pick,itm_club,itm_dress,itm_woolen_dress, itm_skullcap],
   def_attrib|level(5),wp(70),knows_common,refugee_face1,refugee_face2],
  ["hunter_woman","Huntress","Huntresses",tf_female|tf_guarantee_armor,0,0,fac_commoners,
   [itm_bolts,itm_arrows,itm_light_crossbow,itm_short_bow,itm_crossbow,itm_nordic_shield,itm_hide_covered_round_shield,itm_hatchet,itm_hand_axe,itm_voulge,itm_fighting_pick,itm_club,itm_dress,itm_leather_jerkin, itm_skullcap],
   def_attrib|level(10),wp(85),knows_common|knows_power_strike_1,refugee_face1,refugee_face2],
  ["fighter_woman","Camp Defender","Camp Defenders",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_bolts,itm_arrows,itm_light_crossbow,itm_short_bow,itm_crossbow,itm_fur_covered_shield,itm_hide_covered_round_shield,itm_hatchet,itm_voulge,itm_stormguard_hauberk_a,itm_m_hauberk_navy_c, itm_skullcap],
   def_attrib|level(16),wp(100),knows_common|knows_riding_3|knows_power_strike_2|knows_athletics_2|knows_ironflesh_1,refugee_face1,refugee_face2],
  ["sword_sister","Sword Sister","Sword Sisters",tf_female|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_horse,0,0,fac_commoners,
   [itm_bolts,itm_sword_medieval_b,itm_sword_khergit_3,itm_plate_covered_round_shield,itm_tab_shield_small_round_c, itm_crossbow,itm_plate_armor,itm_coat_of_plates,itm_bascinet_3,itm_black_helmet,itm_courser,itm_leather_gloves],
   def_attrib|level(22),wp(140),knows_common|knows_power_strike_3|knows_riding_5|knows_athletics_3|knows_ironflesh_2|knows_shield_2,refugee_face1,refugee_face2],

  ["refugee","Refugee","Refugees",tf_female|tf_guarantee_armor,0,0,fac_commoners,
   [itm_knife,itm_pitch_fork,itm_sickle,itm_hatchet,itm_club,itm_dress,itm_robe,itm_woolen_dress, itm_headcloth, itm_woolen_hood],
   def_attrib|level(1),wp(45),knows_common,refugee_face1,refugee_face2],
  ["peasant_woman","Peasant Woman","Peasant Women",tf_female|tf_guarantee_armor,0,0,fac_commoners,
   [itm_knife,itm_pitch_fork,itm_sickle,itm_hatchet,itm_club,itm_dress,itm_woolen_dress, itm_headcloth, itm_woolen_hood],
   def_attrib|level(1),wp(40),knows_common,refugee_face1,refugee_face2],

  ["caravan_master","Caravan Master","Caravan Masters",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_commoners,
   [itm_sword_medieval_c,itm_fur_coat,itm_saddle_horse,
    itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,
    itm_leather_jacket, itm_leather_cap],
   def_attrib|level(9),wp(100),knows_common|knows_riding_4|knows_ironflesh_3,mercenary_face_1, mercenary_face_2],

  ["kidnapped_girl","Kidnapped Girl","Kidnapped Girls",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_commoners,
   [itm_dress],
   def_attrib|level(2),wp(50),knows_common|knows_riding_2,woman_face_1, woman_face_2],


#This troop is the troop marked as soldiers_end and town_walkers_begin
 ["town_walker_1","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_short_tunic, itm_linen_tunic,itm_fur_coat, itm_coarse_tunic, itm_tabard, itm_leather_vest, itm_arena_tunic_white, itm_leather_apron, itm_shirt, itm_arena_tunic_green, itm_arena_tunic_blue, itm_fur_hat, itm_leather_cap, itm_straw_hat, itm_felt_hat],
   def_attrib|level(4),wp(60),knows_common,man_face_young_1, man_face_old_2],
 ["town_walker_2","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_blue_dress, itm_dress, itm_woolen_dress, itm_peasant_dress, itm_wimple_a, itm_wimple_with_veil, itm_female_hood],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
 ["khergit_townsman","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [itm_solarian_turban_a,itm_solarian_turban_b,itm_solarian_robe_a, itm_solarian_aketon_a],
   def_attrib|level(4),wp(60),knows_common,swadian_face_younger_1, swadian_face_middle_2],
 ["khergit_townswoman","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_blue_dress, itm_dress, itm_woolen_dress, itm_peasant_dress, itm_wimple_a, itm_wimple_with_veil, itm_female_hood],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
 ["sarranid_townsman","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [itm_solarian_turban_a,itm_solarian_turban_b,itm_solarian_robe_a, itm_solarian_aketon_a],
   def_attrib|level(4),wp(60),knows_common,swadian_face_younger_1, swadian_face_middle_2],
 ["sarranid_townswoman","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_sarranid_common_dress, itm_sarranid_common_dress_b, itm_sarranid_felt_head_cloth, itm_sarranid_felt_head_cloth_b],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
  
#This troop is the troop marked as town_walkers_end and village_walkers_begin
 ["village_walker_1","Villager","Villagers",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_short_tunic, itm_linen_tunic, itm_coarse_tunic, itm_leather_vest, itm_leather_apron, itm_shirt,       itm_fur_hat, itm_leather_cap, itm_straw_hat, itm_felt_hat],
   def_attrib|level(4),wp(60),knows_common,man_face_younger_1, man_face_older_2],
 ["village_walker_2","Villager","Villagers",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_blue_dress, itm_dress, itm_woolen_dress, itm_peasant_dress,   itm_wimple_a, itm_wimple_with_veil, itm_female_hood],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],

#This troop is the troop marked as village_walkers_end and spy_walkers_begin
 ["spy_walker_1","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_short_tunic, itm_linen_tunic, itm_coarse_tunic, itm_tabard, itm_leather_vest, itm_robe, itm_leather_apron, itm_shirt,       itm_fur_hat, itm_leather_cap, itm_straw_hat, itm_felt_hat],
   def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_old_2],
 ["spy_walker_2","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_blue_dress, itm_dress, itm_woolen_dress, itm_peasant_dress,   itm_wimple_a, itm_wimple_with_veil, itm_female_hood],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],

["beggar_male","Beggar","Beggars",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners, [itm_robe, itm_pilgrim_disguise, itm_pilgrim_hood], def_attrib|level(4),wp(60),knows_common,swadian_face_younger_1, swadian_face_middle_2],
["beggar_female","Beggar","Beggars",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners, [itm_robe, itm_pilgrim_disguise, itm_pilgrim_hood], def_attrib|level(4),wp(60),knows_common,woman_face_1,woman_face_2],

# Ryan END

#This troop is the troop marked as spy_walkers_end
# Zendar
  ["tournament_master","Tournament Master","Tournament Master",tf_hero, scn_zendar_center|entry(1),reserved,  fac_commoners,[itm_nomad_armor],def_attrib|level(2),wp(20),knows_common,0x000000000008414401e28f534c8a2d09],
  ["trainer","Trainer","Trainer",tf_hero, scn_zendar_center|entry(2),reserved,  fac_commoners,[itm_leather_jerkin],def_attrib|level(2),wp(20),knows_common,0x00000000000430c701ea98836781647f],
  ["Constable_Hareck","Constable Hareck","Constable Hareck",tf_hero, scn_zendar_center|entry(5),reserved,  fac_commoners,[itm_leather_jacket],def_attrib|level(5),wp(20),knows_common,0x00000000000c41c001fb15234eb6dd3f],

# Ryan BEGIN
  ["Ramun_the_slave_trader","Ramun, the slave trader","Ramun, the slave trader",tf_hero, no_scene,reserved, fac_commoners,[itm_leather_jacket],def_attrib|level(5),wp(20),knows_common,0x0000000fd5105592385281c55b8e44eb00000000001d9b220000000000000000],

  ["guide","Quick Jimmy","Quick Jimmy",tf_hero, no_scene,0,  fac_commoners,[itm_coarse_tunic],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x00000000000c318301f24e38a36e38e3],
# Ryan END

  ["Xerina","Xerina","Xerina",tf_hero|tf_female, scn_the_happy_boar|entry(5),reserved,  fac_commoners,[itm_leather_jerkin],def_attrib|str_15|agi_15|level(39),wp(312),knows_power_strike_5|knows_ironflesh_5|knows_riding_6|knows_power_draw_4|knows_athletics_8|knows_shield_3,0x00000001ac0820074920561d0b51e6ed00000000001d40ed0000000000000000],
  ["Dranton","Dranton","Dranton",tf_hero, scn_the_happy_boar|entry(2),reserved,  fac_commoners,[itm_leather_vest],def_attrib|str_15|agi_14|level(42),wp(324),knows_power_strike_5|knows_ironflesh_7|knows_riding_4|knows_power_draw_4|knows_athletics_4|knows_shield_3,0x0000000a460c3002470c50f3502879f800000000001ce0a00000000000000000],
  ["Kradus","Kradus","Kradus",tf_hero, scn_the_happy_boar|entry(3),reserved,  fac_commoners,[itm_padded_leather],def_attrib|str_15|agi_14|level(43),wp(270),knows_power_strike_5|knows_ironflesh_7|knows_riding_4|knows_power_draw_4|knows_athletics_4|knows_shield_3,0x0000000f5b1052c61ce1a9521db1375200000000001ed31b0000000000000000],


#Tutorial
  ["tutorial_trainer","Training Ground Master","Training Ground Master",tf_hero, 0, 0, fac_commoners,[itm_robe],def_attrib|level(2),wp(20),knows_common,0x000000000008414401e28f534c8a2d09],
  ["tutorial_student_1","{!}tutorial_student_1","{!}tutorial_student_1",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_sword, itm_practice_shield, itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_padded_coif,itm_iron_crown_nasal_a],
   def_attrib|level(2),wp(20),knows_common, swadian_face_young_1, swadian_face_old_2],
  ["tutorial_student_2","{!}tutorial_student_2","{!}tutorial_student_2",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_sword, itm_practice_shield, itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_padded_coif,itm_iron_crown_nasal_a],
   def_attrib|level(2),wp(20),knows_common, swadian_face_young_1, swadian_face_old_2],
  ["tutorial_student_3","{!}tutorial_student_3","{!}tutorial_student_3",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_staff, itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_padded_coif,itm_iron_crown_nasal_a],
   def_attrib|level(2),wp(20),knows_common, swadian_face_young_1, swadian_face_old_2],
  ["tutorial_student_4","{!}tutorial_student_4","{!}tutorial_student_4",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_staff, itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_padded_coif,itm_iron_crown_nasal_a],
   def_attrib|level(2),wp(20),knows_common, swadian_face_young_1, swadian_face_old_2],

#Sargoth
  #halkard, hardawk. lord_taucard lord_caupard. lord_paugard

#Salt mine
  ["Galeas","Galeas","Galeas",tf_hero, 0, reserved, fac_commoners,[itm_leather_jacket],def_attrib|level(5),wp(20),knows_common,0x000000000004718201c073191a9bb10c],

#Dhorak keep

  ["farmer_from_bandit_village","Farmer","Farmers",tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_linen_tunic,itm_coarse_tunic,itm_shirt],
   def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_older_2],

  ["trainer_1","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_1|entry(6),reserved,  fac_commoners,[itm_leather_jerkin],def_attrib|level(2),wp(20),knows_common,0x0000000d0d1030c74ae8d661b651c6840000000000000e220000000000000000],
  ["trainer_2","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_2|entry(6),reserved,  fac_commoners,[itm_nomad_vest],def_attrib|level(2),wp(20),knows_common,0x0000000e5a04360428ec253846640b5d0000000000000ee80000000000000000],
  ["trainer_3","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_3|entry(6),reserved,  fac_commoners,[itm_padded_leather],def_attrib|level(2),wp(20),knows_common,0x0000000e4a0445822ca1a11ab1e9eaea0000000000000f510000000000000000],
  ["trainer_4","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_4|entry(6),reserved,  fac_commoners,[itm_leather_jerkin],def_attrib|level(2),wp(20),knows_common,0x0000000e600452c32ef8e5bb92cf1c970000000000000fc20000000000000000],
  ["trainer_5","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_5|entry(6),reserved,  fac_commoners,[itm_leather_vest],def_attrib|level(2),wp(20),knows_common,0x0000000e77082000150049a34c42ec960000000000000e080000000000000000],

# Ransom brokers.
  ["ransom_broker_1","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_vest],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_2","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_tabard],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_3","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_vest],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_4","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_short_tunic],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_5","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_gambeson],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_6","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_blue_gambeson],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_7","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_red_gambeson],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_8","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_9","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_vest],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_10","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_jacket],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],

# Tavern traveler.
  ["tavern_traveler_1","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_2","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_tabard],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_3","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_vest],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_4","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_blue_gambeson],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_5","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_short_tunic],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_6","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_7","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_jacket],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_8","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_tabard],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_9","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_10","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_jacket],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],

# Tavern traveler.
  ["tavern_bookseller_1","Book_Merchant","Book_Merchant",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,
               itm_book_tactics, itm_book_persuasion, itm_book_wound_treatment_reference, itm_book_leadership, 
               itm_book_intelligence, itm_book_training_reference, itm_book_surgery_reference],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_bookseller_2","Book_Merchant","Book_Merchant",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,
               itm_book_wound_treatment_reference, itm_book_leadership, itm_book_intelligence, itm_book_trade, 
               itm_book_engineering, itm_book_weapon_mastery],def_attrib|level(5),wp(20),knows_common,merchant_face_1, merchant_face_2],

# Tavern minstrel.
  ["tavern_minstrel_1","Wandering Minstrel","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_leather_jacket,  itm_lute],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2], #lute
  ["tavern_minstrel_2","Wandering Bard","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_tunic_with_green_cape,  itm_lyre],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],  #early harp/lyre
  ["tavern_minstrel_3","Wandering Ashik","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_nomad_robe,  itm_lute],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2], #lute/oud or rebab
  ["tavern_minstrel_4","Wandering Skald","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_fur_coat,  itm_lyre],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2], #No instrument or lyre
  ["tavern_minstrel_5","Wandering Troubadour","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_short_tunic,  itm_lute],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2], #Lute or Byzantine/Occitan lyra
  
#NPC system changes begin
#Companions
  ["kingdom_heroes_including_player_begin",  "kingdom_heroes_including_player_begin",  "kingdom_heroes_including_player_begin",  tf_hero, 0,reserved,  fac_kingdom_1,[],          lord_attrib,wp(220),knows_lord_1, 0x000000000010918a01f248377289467d],

  ["npc1","Hurey","Hurey",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_ragged_outfit,itm_studded_club],
   str_11|agi_13|int_12|cha_7|level(3),wp(110),knows_tracker_npc|knows_tactics_3|
   knows_ironflesh_3|knows_power_strike_1|knows_pathfinding_3|knows_athletics_2|knows_tracking_1|knows_riding_2, #skills 2/3 player at that level
   0x0000000e730065c420db6db6db6ddeff00000000001db6f00000000000000000],
  ["npc2","Mesym","Mesym", tf_hero|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,[itm_stormguard_aketon_plated_a,itm_m_pole_hammer_a],
   str_17|agi_7|int_11|cha_12|level(8),wp(170),knows_trainer_3|knows_weapon_master_4|knows_ironflesh_5|knows_athletics_2|knows_leadership_3,
   0x0000000bff003440209b6e38e06dbeff00000000001f36e10000000000000000],
  ["npc3","Evel Droby","Evel Droby",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[ itm_hunter_c, itm_rich_outfit, itm_mt_leather_gloves_a,itm_royal_mace_decorated],
   str_6|agi_9|int_18|cha_9|level(1),wp(20),knows_wound_treatment_5|knows_trade_1|knows_first_aid_4|knows_surgery_5|knows_athletics_1|knows_riding_4,
   0x00000004a204300436db6db6db6dfeff00000000001db6db0000000000000000],
  ["npc4","Ilhan","Ilhan",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_stormguard_aketon_a, itm_heavy_infantry_axe, itm_mt_leather_gloves_a, itm_throwing_knives],
   str_10|agi_19|int_13|cha_10|level(10),wp(145),knows_weapon_master_2|knows_power_strike_2|knows_riding_2|knows_athletics_5|knows_looting_5|knows_power_throw_7|knows_tactics_2|knows_leadership_2,
   0x0000000b7d00130020db6db6db6dbeff00000000001db6e80000000000000000],
  ["npc5","Gyliam Gare","Gyliam Gare",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_banded_armor, itm_bascinet_3, itm_m_gloves_a, itm_shortened_bill, itm_light_rifle_a, itm_cartridges],
   str_23|agi_17|int_12|cha_17|level(15),wp(180)|wp_firearm(260),knows_warrior_npc|
   knows_riding_2|knows_horse_archery_3|knows_leadership_5|knows_weapon_master_5,
   0x0000000dff00115420db6db6db6dbeff00000000001db6e80000000000000000],
  ["npc6","Ames","Ames",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_saddle_horse, itm_chornovalley_vest_a, itm_hatchet],
   str_10|agi_12|int_16|cha_18|level(3),wp(65),knows_riding_2|knows_trade_6|knows_inventory_management_5|knows_trainer_1|knows_leadership_1,
  0x0000000d401001cf20db6db6db6dfeff00000000001db6d00000000000000000],
  ["npc7","Malia Willey","Malia Willey",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_gambeson,itm_spear],
   str_8|agi_9|int_10|cha_6|level(2),wp(80),knows_tracker_npc|
   knows_tracking_5|knows_athletics_8|knows_spotting_5|knows_pathfinding_8|knows_power_draw_2,
   0x000000031f08000206d86db64b4db6db00000000001db6c30000000000000000],
  ["npc8","Eryet Allard","Eryet Allard",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_tribal_warrior_outfit, itm_sword_viking_1],
   str_9|agi_10|int_9|cha_10|level(7),wp(90),knows_warrior_npc|
   knows_weapon_master_3|knows_power_strike_2|knows_athletics_2|knows_leadership_3|knows_tactics_1,
   0x0000000ffe08000300db6db6496208d400000000001d86fc0000000000000000],
  ["npc9","Aduhash","Aduhash",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_mkk_mamluke_a,itm_eastern_scale_gloves_a, itm_sarranid_two_handed_mace_1, itm_m_bandit_turban_a],
   str_25|agi_17|int_12|cha_14|level(16),wp(200),knows_warrior_npc|
   knows_weapon_master_5|knows_riding_3|knows_athletics_3|knows_leadership_1|knows_power_strike_6,
   0x00000001900471c6125b69fcdb6dbeff00000000001db6fb0000000000000000],
  ["npc10","Zela","Zela",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_coat_of_plates, itm_medium_rifle_f, itm_cartridges, itm_scottish_sword, itm_tab_shield_pavise_d, itm_m_gauntlets_a],
   str_15|agi_13|int_9|cha_11|level(8),wp(105)|wp_firearm(300),knows_warrior_npc|
   knows_weapon_master_5|knows_tactics_1|knows_leadership_1|knows_ironflesh_5|knows_trainer_4|knows_first_aid_2,
   0x0000000190042348058365c91c7d8eff00000000001de6fb0000000000000000],
  ["npc11","Jane","Jane",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_studded_leather_coat, itm_falshion_1],
   str_8|agi_11|int_10|cha_10|level(2),wp(70),knows_merchant_npc|
   knows_weapon_master_1|knows_first_aid_1|knows_wound_treatment_2,
   0x00000006000c000206186196918db8e400000000001d48c40000000000000000],
  ["npc12","Pai Khoi-Kao","Pai Khoi-Kao",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_lamellar_vest, itm_light_rifle_d, itm_cartridges, itm_flanged_mace, itm_m_gloves_a],
   str_12|agi_17|int_13|cha_7|level(4),wp(85)|wp_firearm(200),   knows_merchant_npc|
   knows_ironflesh_1|knows_power_strike_1|knows_surgery_4|knows_wound_treatment_3|knows_first_aid_3,
   0x00000001bf044383201d6a24da6dbcff00000000001db6f80000000000000000],
  ["npc13","Dondo","Dondo",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_m_hauberk_mountain_d, itm_m_gloves_a, itm_m_scimitar_a],
   str_9|agi_13|int_12|cha_8|level(3),wp(80),knows_warrior_npc|
   knows_riding_2|knows_leadership_2|knows_athletics_2|knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_1,
   0x00000001bf0474d420dc6a36ea6dbcff00000000001db6f80000000000000000],
  ["npc14","Elrel","Elrel",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_shirt, itm_sword_medieval_b_small],
   str_9|agi_8|int_11|cha_8|level(5),wp(100),knows_warrior_npc|
   knows_trainer_4|knows_weapon_master_3|knows_power_strike_1,
   0x00000001be00024545136dc11b79fcdb00000000001db6e80000000000000000],
  ["npc15","Phamas","Phamas",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_robe, itm_maul, itm_eastern_scale_gloves_b],
   str_9|agi_9|int_12|cha_8|level(7),wp(80),knows_warrior_npc|
   knows_tactics_2|knows_engineer_4|knows_trade_3|knows_tracking_1|knows_spotting_1,
   0x0000000fb110600020db6dd9226dbf7f00000000001db6f80000000000000000],
  ["npc16","Kina","Kina",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_short_tunic,  itm_battle_trident],
   str_12|agi_11|int_8|cha_7|level(2),wp(80),knows_tracker_npc|
   knows_power_strike_4|knows_athletics_2,
   0x00000000000c3001009849a2494288cb00000000001da6830000000000000000],
#NPC system changes end

# Special NPCs
  ["quartermaster","Quartermaster","Quartermaster",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_leather_jerkin,itm_club],
    str_7|agi_7|int_7|cha_7|level(1),wp(40),knows_common,swadian_face_older_2,swadian_face_old_2],

#governers olgrel rasevas                                                                        Horse          Bodywear                Footwear_in                     Footwear_out                    Armor                       Weapon                  Shield                  Headwaer
  ["kingdom_1_lord",  "King Chamond II",  "Chamond",  tf_hero, 0,reserved,  fac_kingdom_1,[itm_silver_rose_heavy_horse_a,   itm_rich_outfit,   itm_silver_rose_plate_b, itm_m_gauntlets_a,    itm_german_bastard_sword, itm_shield_heater_d, itm_m_knigh_helm_c],          knight_attrib_5,wp(220),knight_skills_5|knows_trainer_5, 0x0000000f6d10244606db6db6db6dcafe00000000001db8fb0000000000000000,swadian_face_older_2],
  ["kingdom_2_lord",  "King Zbosek Jasnyi",  "Zbosek",  tf_hero, 0,reserved,  fac_kingdom_2,[itm_hunter,    itm_courtly_outfit,                     itm_chornovalley_heavy_lamellar_b, itm_m_gauntlets_a,      itm_german_bastard_sword,      itm_shield_kite_k,      itm_chornovalley_infantry_helmet_c, itm_great_bardiche],    knight_attrib_5,wp(220),knight_skills_5|knows_trainer_5, 0x0000000ec804450506db6db6db6ddb7f00000000001db6fb0000000000000000, vaegir_face_old_2],
  ["kingdom_3_lord",  "King Solarius I",  "Solarius",  tf_hero, 0,reserved,  fac_kingdom_3,[itm_warhorse,   itm_tabard,   itm_m_celestial_plate_heavy_a, itm_m_gauntlets_b, itm_lance, itm_m_mace_knight_pierce, itm_shield_heater_d, itm_m_bascinet_a], knight_attrib_5,wp(220),knight_skills_5|knows_trainer_6, 0x0000000e400c529014c56db6db6dffff00000000001f76f80000000000000000,khergit_face_old_2],
  ["kingdom_4_lord",  "King Ognvar Vidison",  "Ognvar Vidison",  tf_hero, 0,reserved,  fac_kingdom_4,[itm_hunter,    itm_nobleman_outfit,                                 itm_m_iron_crown_scale_b,  itm_lamellar_gauntlets,    itm_war_axe,           itm_tab_shield_round_e,    itm_iron_crown_king_helmet_a, itm_one_handed_war_axe_a],            knight_attrib_5,wp(220),knight_skills_5|knows_trainer_5, 0x0000000e000c2191061b6ddde3227fff00000000001d033b0000000000000000, nord_face_older_2],
  ["kingdom_5_lord",  "King Graveth III",  "Graveth",  tf_hero, 0,reserved,  fac_kingdom_5,[itm_warhorse,  itm_tabard,                              itm_m_alpine_full_plate_a,  itm_m_gauntlets_a,         itm_crusader_sword,         itm_shield_heater_d,        itm_alpine_footman_helmet_visored_mail_b],         knight_attrib_5,wp(220),knight_skills_4|knows_trainer_5, 0x0000000eff10231106a46dda936dff3c00000000001fb63b0000000000000000, rhodok_face_old_2],
  ["kingdom_6_lord",  "Sultan Iman",  "Iman",  tf_hero, 0,reserved,  fac_kingdom_6,[itm_saracen_horse_sultan,     itm_eastern_sultan_armor_a, itm_solarian_heavy_helmet_e,  itm_decorated_leather_gloves_b,      itm_sarranid_mace_1,    itm_maa_camel_rider_shield_f],         knight_attrib_4,wp(220),knight_skills_5|knows_trainer_5, 0x0000000a7f10311416db6ddedb6ddb6e00000000001dc6f90000000000000000, rhodok_face_old_2],
  ["kingdom_7_lord", "King Marko", "Marko", tf_hero, 0, reserved, fac_kingdom_7,[itm_mt_horse_b3, itm_nerpa_shirt_a,   itm_m_nerpa_coat_of_plates_heavy_b, itm_m_gauntlets_b, itm_longsword, itm_steel_shield, itm_nerpa_barbuta_mail_b, itm_jarid, itm_heavy_lance],knight_attrib_5,wp(350),knight_skills_5|knows_trainer_5|knows_ironflesh_10, 0x0000000eff10414936db6db6db6e3b7500000000001db6db0000000000000000,swadian_face_older_2],
  ["kingdom_8_lord", "Red Demon Hairako", "Hairako", tf_hero, 0, reserved, fac_kingdom_8,[itm_steppe_horse_d, itm_tabard, itm_eastern_scale_gloves_b, itm_hairako_full_mail_b, itm_hairako_mail_helmet_d, itm_javelin, itm_solarian_lance_d, itm_tab_shield_tauria_b, itm_sarranid_cavalry_sword],knight_attrib_5,wp(350),knight_skills_5|knows_trainer_5|knows_ironflesh_10|knows_riding_10|knows_power_throw_10, 0x0000000e001051c736db6db6db6e3b7500000000001db6db0000000000000000,swadian_face_older_2],
  ["kingdom_9_lord", "King Anastas", "Anastas", tf_hero, 0, reserved, fac_kingdom_9,[ itm_rich_outfit,  itm_m_tauria_brigandine_b, itm_m_gauntlets_a, itm_m_munitions_helm_a, itm_mt_horse_b3, itm_great_lance, itm_tab_shield_tauria_c, itm_crusader_sword],knight_attrib_5,wp(350),knight_skills_5|knows_trainer_5|knows_ironflesh_10|knows_riding_10, 0x0000000e9310428636db6df8eb0dfd7500000000001db6db0000000000000000,swadian_face_older_2],
  ["kingdom_10_lord", "King Asmadias", "Asmadias", tf_hero, 0, reserved, fac_kingdom_10,[ itm_tabard,  itm_m_elen_plated_leather_b, itm_m_gauntlets_b, itm_elen_great_helm_c, itm_warhorse, itm_tab_shield_tauria_b, itm_k_long_sword_c, itm_danish_greatsword],knight_attrib_5,wp(425),knight_skills_5|knows_trainer_5|knows_ironflesh_10, 0x0000000e801015c036db6db6db6e5d7f00000000001db6db0000000000000000,swadian_face_older_2],
  ["kingdom_11_lord", "Sultan Zahir al-Adid", "Zahir", tf_hero, 0, reserved, fac_kingdom_11,[itm_arabian_horse_d,     itm_mkk_mamluke_c, itm_adid_elite_helmet_a, itm_decorated_leather_gloves_b, itm_sarranid_mace_1, itm_eastern_round_shield_a, itm_lance],knight_attrib_5,wp(425),knight_skills_5|knows_trainer_5|knows_ironflesh_10, 0x0000000fff04644436db6db7d76dfced00000000001db6eb0000000000000000,swadian_face_older_2],
  ["kingdom_12_lord", "King Darius Stormbane", "Darius", tf_hero, 0, reserved, fac_kingdom_12,[itm_black_knight_horse_a,    itm_nobleman_outfit,   itm_coat_of_plates_v3, itm_m_gauntlets_b, itm_german_poleaxe, itm_grosse_messer_b, itm_m_knigh_helm_d],knight_attrib_5,wp(350),knight_skills_5|knows_trainer_5|knows_ironflesh_10|knows_riding_10, 0x0000000e800441d236c36c379a6dff3f00000000001dc93b0000000000000000,swadian_face_older_2],

#    Imbrea   Belinda Ruby Qaelmas Rose    Willow 
#  Alin  Ganzo            Zelka Rabugti
#  Qlurzach Ruhbus Givea_alsev  Belanz        Bendina  
# Dunga        Agatha     Dibus Crahask
  
#                                                                               Horse                   Bodywear                Armor                               Footwear_in                 Footwear_out                        Headwear                    Weapon               Shield
  #Swadian civilian clothes: itm_courtly_outfit itm_gambeson itm_blue_gambeson itm_red_gambeson itm_nobleman_outfit itm_rich_outfit itm_short_tunic itm_tabard
  #Older knights with higher skills moved to top
  ["knight_1_1", "Sir Gileon", "Gileon", tf_hero, 0, reserved,  fac_kingdom_1, [itm_silver_rose_heavy_horse_a,   itm_rich_outfit,itm_silver_rose_plate_b, itm_m_gauntlets_a,    itm_longsword,itm_shield_heater_d,itm_m_knigh_helm_c],   knight_attrib_5,wp(230),knight_skills_5|knows_trainer_1|knows_trainer_3, 0x0000000efe086192149e6cc71b6dff3f00000000001cd4f90000000000000000, swadian_face_older_2],
  ["knight_1_2", "Sir Ander", "Ander", tf_hero, 0, reserved,  fac_kingdom_1, [itm_silver_rose_heavy_horse_a,   itm_rich_outfit,itm_silver_rose_plate_b, itm_m_gauntlets_b,    itm_sarranid_mace_1,itm_shield_heater_d,itm_m_knigh_helm_f],       knight_attrib_5,wp(240),knight_skills_5, 0x0000000fb80064c004db6e355c6decff00000000001e26f80000000000000000, swadian_face_young_2],
  ["knight_1_3", "Sir Wilhye Balley", "Wilhye Balley", tf_hero, 0, reserved,  fac_kingdom_1, [itm_silver_rose_heavy_horse_a,   itm_rich_outfit,itm_silver_rose_plate_a, itm_m_gauntlets_b,    itm_crusader_sword,itm_shield_heater_d,itm_m_sergant_helmet_a],  knight_attrib_5,wp(260),knight_skills_5|knows_trainer_3, 0x0000000bbe0c428516db6db6db6dffff00000000001db6f90000000000000000, swadian_face_young_2],
  ["knight_1_4", "Sir Rewis Bailey", "Rewis Bailey", tf_hero, 0, reserved,  fac_kingdom_1, [itm_silver_rose_heavy_horse_a,   itm_rich_outfit,itm_silver_rose_plate_b, itm_m_gauntlets_a,    itm_german_bastard_sword,itm_shield_heater_d,itm_m_knigh_helm_a],    knight_attrib_5,wp(180),knight_skills_5|knows_trainer_4, 0x0000000b3000101436db6db6db6ddd6e00000000001db6db0000000000000000, swadian_face_older_2],
  ["knight_1_5", "Sir Chiles", "Chiles", tf_hero, 0, reserved,  fac_kingdom_1, [itm_silver_rose_heavy_horse_a,   itm_rich_outfit,itm_silver_rose_plate_a, itm_m_gauntlets_a,    itm_german_bastard_sword,itm_shield_heater_d,itm_m_knigh_helm_b],      knight_attrib_4,wp(200),knight_skills_4|knows_trainer_6, 0x0000000d7f00329136db6db6db6dfeff00000000001db6fb0000000000000000, swadian_face_older_2],
  ["knight_1_6", "Sir Drobert", "Drobert", tf_hero, 0, reserved,  fac_kingdom_1, [itm_silver_rose_heavy_horse_a,   itm_rich_outfit, itm_m_gauntlets_a,    itm_grosse_messer_b,itm_shield_heater_d,itm_m_knigh_helm_f], knight_attrib_5,wp(240),knight_skills_4|knows_trainer_4, 0x0000000e3f08034920db6db6db6dfeff00000000001de6f80000000000000000, swadian_face_older_2],
  ["knight_1_7", "Sir Richye Bexley", "Richye Bexley", tf_hero, 0, reserved,  fac_kingdom_1, [itm_silver_rose_heavy_horse_a,   itm_rich_outfit, itm_m_gauntlets_a,    itm_danish_greatsword,itm_shield_heater_d,itm_irish_sword,itm_m_sergant_helmet_a], knight_attrib_5,wp(290),knight_skills_4|knows_trainer_4, 0x0000000e4000354436db6db6db6dfeff00000000001dd6fb0000000000000000, swadian_face_young_2],
  ["knight_1_8", "Sir Rancent", "Rancent", tf_hero, 0, reserved,  fac_kingdom_1, [itm_silver_rose_heavy_horse_a,   itm_rich_outfit,itm_silver_rose_plate_a, itm_m_gauntlets_b,    itm_german_bastard_sword,itm_shield_heater_d,itm_sword_of_war,itm_m_knigh_helm_b],  knight_attrib_4,wp(250),knight_skills_4, 0x0000000fb308349431db6db6db6dfeff00000000001fd6fb0000000000000000, swadian_face_older_2],

#Swadian younger knights  
  ["knight_1_9", "Sir Ethes Tere", "Ethes Tere", tf_hero, 0, reserved,  fac_kingdom_1, [itm_silver_rose_heavy_horse_a,   itm_rich_outfit, itm_m_gauntlets_b,    itm_crusader_sword,itm_shield_kite_k,itm_m_sergant_helmet_a],    knight_attrib_3,wp(160),knight_skills_3, 0x000000032b0c450f20c7b1b6db6dfeff00000000001c76f80000000000000000, swadian_face_old_2],
  ["knight_1_10", "Sir Sterey Moore", "Sterey Moore", tf_hero, 0, reserved,  fac_kingdom_1, [itm_silver_rose_heavy_horse_a,   itm_rich_outfit, itm_m_gloves_a,    itm_italian_falchion,itm_shield_heater_d,itm_m_sergant_helmet_a],   knight_attrib_3,wp(190),knight_skills_3, 0x0000000e4a0c634612e46edd29577eff00000000001c57380000000000000000, swadian_face_older_2],
  ["knight_1_11", "Sir Gery Yourner", "Gery Yourner", tf_hero, 0, reserved,  fac_kingdom_1, [itm_silver_rose_heavy_horse_a,   itm_rich_outfit, itm_leather_gloves,    itm_english_longsword,itm_shield_heater_d,itm_m_sergant_helmet_a],       knight_attrib_3,wp(220),knight_skills_3, 0x0000000e540c259416936ea8e3adffbf00000000001e44fd0000000000000000, swadian_face_older_2],
  ["knight_1_12", "Sir Symas Gelnne", "Symas Gelnne", tf_hero, 0, reserved,  fac_kingdom_1, [itm_silver_rose_heavy_horse_a,   itm_rich_outfit, itm_m_gauntlets_a,    itm_military_pick,itm_shield_kite_k,itm_m_sergant_helmet_a],    knight_attrib_3,wp(130),knight_skills_3, 0x000000003f082286201b6db6db6dfefe00000000001e76f80000000000000000, swadian_face_older_2],
  ["knight_1_13", "Sir Finy", "Finy", tf_hero, 0, reserved,  fac_kingdom_1, [itm_silver_rose_heavy_horse_a,   itm_rich_outfit,itm_silver_rose_brigandine_b, itm_m_gauntlets_b,    itm_morningstar,itm_shield_heater_d,itm_m_sergant_helmet_a],   knight_attrib_2,wp(160),knight_skills_2, 0x00000000170833c520db6db6db6dfefe00000000001c56f80000000000000000, swadian_face_older_2],
  ["knight_1_14", "Sir Froguy Warre", "Froguy Warre", tf_hero, 0, reserved,  fac_kingdom_1, [itm_silver_rose_heavy_horse_a,   itm_rich_outfit,itm_silver_rose_brigandine_a, itm_m_gauntlets_a,    itm_crusader_sword,itm_shield_kite_k,itm_m_sergant_helmet_a],    knight_attrib_2,wp(190),knight_skills_3|knows_trainer_6, 0x000000001708648021036db6db6dfefe00000000001df6380000000000000000, swadian_face_older_2],
  ["knight_1_15", "Sir James", "James", tf_hero, 0, reserved,  fac_kingdom_1, [itm_silver_rose_heavy_horse_a,   itm_rich_outfit, itm_m_gauntlets_b,    itm_irish_sword,itm_shield_kite_k,itm_m_sergant_helmet_a,itm_crossbow, itm_bolts],      knight_attrib_4,wp(140),knight_skills_2, 0x00000000170804c736db6db6db6dbf3c00000000001db6ff0000000000000000, swadian_face_young_2],
  ["knight_1_16", "Sir Gerey", "Gerey", tf_hero, 0, reserved,  fac_kingdom_1, [itm_silver_rose_heavy_horse_a,   itm_rich_outfit,itm_silver_rose_brigandine_a, itm_m_gauntlets_b,    itm_crusader_sword,itm_shield_heater_d,itm_m_knigh_helm_e],   knight_attrib_1,wp(130),knight_skills_2, 0x0000000ebf08251106db6dbe9b6dbf3c00000000001df6f80000000000000000, swadian_face_young_2],
  ["knight_1_17", "Sir Arthur", "Arthur", tf_hero, 0, reserved,  fac_kingdom_1, [itm_silver_rose_heavy_horse_a,   itm_rich_outfit, itm_m_gauntlets_b,itm_longsword,itm_shield_kite_k,itm_m_sergant_helmet_a],    knight_attrib_2,wp(190),knight_skills_1|knows_trainer_4, 0x000000019a0061543a4d44a8eb6edf3f00000000001d477d0000000000000000, swadian_face_young_2],
  ["knight_1_18", "Sir Stiny Seve", "Stiny Seve", tf_hero, 0, reserved,  fac_kingdom_1, [itm_silver_rose_heavy_horse_a,   itm_rich_outfit,itm_silver_rose_brigandine_a, itm_scale_gauntlets,itm_lance,   itm_crusader_sword,itm_shield_kite_g,itm_m_sergant_helmet_a],   knight_attrib_3,wp(210),knight_skills_1, 0x00000001a70c32c836db6db6db6dfefb00000000001db6fb0000000000000000, swadian_face_young_2],
  ["knight_1_19", "Sir Edward", "Edward", tf_hero, 0, reserved,  fac_kingdom_1, [itm_silver_rose_heavy_horse_a,   itm_rich_outfit,itm_silver_rose_brigandine_b, itm_m_gauntlets_b,    itm_side_sword,itm_shield_kite_k,itm_bec_de_corbin,itm_m_sergant_helmet_a],    knight_attrib_1,wp(120),knight_skills_1, 0x00000001be1035c636db6db7db6deb6d00000000001dd6f30000000000000000, swadian_face_young_2],
  ["knight_1_20", "Sir Wilhye", "Wilhye", tf_hero, 0, reserved,  fac_kingdom_1, [itm_silver_rose_heavy_horse_a,   itm_rich_outfit,itm_silver_rose_brigandine_a, itm_m_gloves_a,    itm_irish_sword,itm_shield_kite_k,itm_m_sergant_helmet_a],   knight_attrib_2,wp(150),knight_skills_1, 0x00000001be1040c536db6dbd1b6deb6d00000000001dd6f30000000000000000, swadian_face_young_2],



  ["knight_2_1", "Lord-Commander Vacla", "Vacla", tf_hero, 0, reserved,  fac_kingdom_2, [itm_hunter,itm_fur_coat,itm_chornovalley_heavy_lamellar_b,itm_chornovalley_infantry_helmet_c,    itm_scale_gauntlets,itm_bardiche, itm_mace_3,itm_norman_shield_1],    knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x0000000cda1021c506db6db6db6dffbe00000000001db6ea0000000000000000, vaegir_face_middle_2],
  ["knight_2_2", "Lord-Commander Zita", "Zita", tf_hero, 0, reserved,  fac_kingdom_2, [itm_hunter,itm_fur_coat,itm_chornovalley_heavy_lamellar_a,itm_chornovalley_infantry_helmet_c,    itm_scale_gauntlets,itm_bardiche, itm_mace_3,itm_norman_shield_1],    knight_attrib_2,wp(160),knight_skills_2, 0x0000000cc004329236db6db6db6dbfff00000000001db6fb0000000000000000, vaegir_face_old_2],
  ["knight_2_3", "Lord-Commander Besla", "Besla", tf_hero, 0, reserved,  fac_kingdom_2, [itm_hunter,itm_fur_coat,itm_chornovalley_heavy_lamellar_b, itm_chornovalley_infantry_helmet_b, itm_mail_mittens,itm_war_axe, itm_one_handed_war_axe_a,itm_norman_shield_1],     knight_attrib_3,wp(190),knight_skills_3, 0x0000000cc004128906db6db92b6dffff00000000001e46f90000000000000000, vaegir_face_older_2],
  ["knight_2_4", "Lord-Commander Mira", "Mira", tf_hero, 0, reserved,  fac_kingdom_2, [itm_hunter,itm_fur_coat,itm_chornovalley_heavy_lamellar_a, itm_chornovalley_infantry_helmet_b, itm_mail_mittens,itm_war_axe, itm_one_handed_battle_axe_a,itm_norman_shield_1],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000ca40403d320047279ef6dcfbf00000000001ec6f90000000000000000, vaegir_face_older_2],
  ["knight_2_5", "Lord-Commander Bisla", "Bisla", tf_hero, 0, reserved,  fac_kingdom_2, [itm_hunter,itm_fur_coat,itm_chornovalley_heavy_mail_b,itm_chornovalley_infantry_helmet_c,itm_mail_mittens,itm_bardiche, itm_one_handed_war_axe_b,itm_norman_shield_1],       knight_attrib_5,wp(250),knight_skills_5, 0x0000000cb50411d406db6db71b6d9edf00000000001d36e30000000000000000, vaegir_face_older_2],
  ["knight_2_6", "Lord-Commander Rivoi", "Rivoi", tf_hero, 0, reserved,  fac_kingdom_2, [itm_hunter,itm_fur_coat,itm_chornovalley_heavy_lamellar_a,itm_chornovalley_infantry_helmet_a,itm_mail_mittens,itm_war_axe, itm_one_handed_battle_axe_b,itm_norman_shield_1],   knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x0000000c8600334520d36dd1116f1f3f00000000001db8fb0000000000000000, vaegir_face_middle_2],
  ["knight_2_7", "Lord-Commander Bora", "Bora", tf_hero, 0, reserved,  fac_kingdom_2, [itm_hunter,itm_fur_coat,itm_chornovalley_heavy_lamellar_b, itm_chornovalley_infantry_helmet_a,   itm_mail_mittens,itm_great_bardiche, itm_one_handed_battle_axe_a,itm_norman_shield_1],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x0000000c800422cd22db69c75b88cfcf00000000001c46ba0000000000000000, vaegir_face_old_2],
  ["knight_2_8", "Lord-Commander Bohda", "Bohda", tf_hero, 0, reserved,  fac_kingdom_2, [itm_hunter,itm_fur_coat,itm_chornovalley_heavy_lamellar_a, itm_chornovalley_infantry_helmet_a,   itm_mail_mittens,itm_war_axe, itm_one_handed_war_axe_a,itm_norman_shield_1],    knight_attrib_3,wp(200),knight_skills_3|knows_trainer_5, 0x00000004cb1015c6075c6d39686dbeff00000000001db6fb0000000000000000, vaegir_face_older_2],
  ["knight_2_9", "Lord-Commander Rosta", "Rosta", tf_hero, 0, reserved,  fac_kingdom_2, [itm_hunter,itm_fur_coat,itm_chornovalley_heavy_mail_a, itm_chornovalley_infantry_helmet_a,   itm_mail_mittens,itm_war_axe, itm_one_handed_war_axe_b,itm_norman_shield_1],    knight_attrib_4,wp(230),knight_skills_4, 0x00000004cb10354736db6db6db6ddaee00000000001db6db0000000000000000, vaegir_face_older_2],
  ["knight_2_10", "Lord-Commander Rosla", "Rosla", tf_hero, 0, reserved,  fac_kingdom_2, [itm_hunter,itm_fur_coat,itm_chornovalley_heavy_lamellar_a, itm_chornovalley_infantry_helmet_a,   itm_mail_mittens,itm_war_axe, itm_mace_4,itm_norman_shield_1],      knight_attrib_5,wp(260),knight_skills_5|knows_trainer_6, 0x00000004eb0412d106db6db8ab6deede00000000001db6b00000000000000000, vaegir_face_older_2],
  ["knight_2_11", "Lord-Commander Mira", "Mira", tf_hero, 0, reserved,  fac_kingdom_2, [itm_hunter,itm_fur_coat,itm_chornovalley_heavy_lamellar_b, itm_chornovalley_infantry_helmet_a,   itm_mail_mittens,itm_war_axe, itm_mace_4,itm_norman_shield_1],    knight_attrib_1,wp(130),knight_skills_1, 0x00000004c500028608d386449d6d4d3700000000001edaf20000000000000000, vaegir_face_middle_2],
  ["knight_2_12", "Lord-Commander Zela", "Zela", tf_hero, 0, reserved,  fac_kingdom_2, [itm_hunter,itm_fur_coat,itm_chornovalley_heavy_mail_b, itm_chornovalley_infantry_helmet_a,   itm_mail_mittens,itm_war_axe, itm_mace_4,itm_norman_shield_1],    knight_attrib_2,wp(170),knight_skills_2, 0x00000004da00014368db7259117fcf3f00000000001db6f20000000000000000, vaegir_face_old_2],
  ["knight_2_13", "Lord-Commander Jara", "Jara", tf_hero, 0, reserved,  fac_kingdom_2, [itm_hunter,itm_fur_coat,itm_chornovalley_heavy_mail_b, itm_chornovalley_infantry_helmet_a,   itm_mail_mittens,itm_war_axe, itm_mace_3,itm_norman_shield_4],     knight_attrib_3,wp(190),knight_skills_3, 0x00000004c30c254822db6ec69b6dfcff00000000001eb6ba0000000000000000, vaegir_face_older_2],
  ["knight_2_14", "Lord-Commander Boha", "Boha", tf_hero, 0, reserved,  fac_kingdom_2, [itm_hunter,itm_fur_coat,itm_chornovalley_heavy_mail_a, itm_chornovalley_infantry_helmet_a,   itm_mail_mittens,itm_bardiche, itm_mace_4,itm_norman_shield_4],    knight_attrib_4,wp(220),knight_skills_4|knows_trainer_6, 0x0000000dc40c22d4204769bedb6dfeff00000000001c66f80000000000000000, vaegir_face_older_2],
  ["knight_2_15", "Lord-Commander Vata", "Vata", tf_hero, 0, reserved,  fac_kingdom_2, [itm_hunter,itm_fur_coat,itm_chornovalley_heavy_mail_b, itm_chornovalley_footman_helmet_b,   itm_mail_mittens,itm_one_handed_battle_axe_b,itm_norman_shield_4],       knight_attrib_5,wp(250),knight_skills_5, 0x0000000dc708000020dccdf5e7b67eff00000000001f70f80000000000000000, vaegir_face_older_2],
  ["knight_2_16", "Lord-Commander Vojta", "Vojta", tf_hero, 0, reserved,  fac_kingdom_2, [itm_hunter,itm_fur_coat,itm_chornovalley_mail_b, itm_chornovalley_footman_helmet_b,   itm_mail_mittens,itm_bardiche, itm_one_handed_battle_axe_a,itm_norman_shield_1],   knight_attrib_1,wp(120),knight_skills_1, 0x000000009610034f06c36db6db6decff00000000001dbf380000000000000000, vaegir_face_middle_2],
  ["knight_2_17", "Lord-Commander Stecha", "Stecha", tf_hero, 0, reserved,  fac_kingdom_2, [itm_hunter,itm_fur_coat,itm_chornovalley_mail_a, itm_chornovalley_footman_helmet_b,   itm_mail_mittens,itm_bardiche, itm_mace_4,itm_norman_shield_3],     knight_attrib_2,wp(150),knight_skills_2, 0x00000000b90c008606db6db0dba1eb1f00000000001dd6c00000000000000000, vaegir_face_old_2],
  ["knight_2_18", "Lord-Commander Lava", "Lava", tf_hero, 0, reserved,  fac_kingdom_2, [itm_hunter,itm_fur_coat,itm_chornovalley_lamellar_vest_b, itm_chornovalley_footman_helmet_b,   itm_mail_mittens,itm_spear, itm_grosse_messer,itm_norman_shield_1],    knight_attrib_3,wp(180),knight_skills_3, 0x00000000a70801c304146d8fe76eff7f00000000001eb6f80000000000000000, vaegir_face_older_2],
  ["knight_2_19", "Lord-Commander Veko", "Veko", tf_hero, 0, reserved,  fac_kingdom_2, [itm_hunter,itm_fur_coat,itm_chornovalley_mail_b, itm_chornovalley_footman_helmet_b,   itm_mail_mittens,itm_bardiche, itm_one_handed_battle_axe_c,itm_norman_shield_2],    knight_attrib_4,wp(210),knight_skills_4|knows_trainer_4, 0x00000000850001c206db6db6d36deb3600000000001db6f80000000000000000, vaegir_face_older_2],
  ["knight_2_20", "Lord-Commander Vojar", "Vojar", tf_hero, 0, reserved,  fac_kingdom_2, [itm_hunter,itm_fur_coat,itm_chornovalley_mail_a, itm_chornovalley_footman_helmet_b,   itm_mail_mittens, itm_one_handed_battle_axe_a,itm_norman_shield_1],      knight_attrib_5,wp(240),knight_skills_5|knows_trainer_5, 0x000000003f0c000530db6db6db6d8efe00000000001c36fb0000000000000000, vaegir_face_older_2],

#khergit civilian clothes: itm_leather_vest, itm_nomad_vest, itm_nomad_robe, itm_lamellar_vest,itm_tribal_warrior_outfit
  ["knight_3_1", "Lord Solarion", "Solarion", tf_hero, 0, reserved,  fac_kingdom_3, [itm_warhorse, itm_gambeson,   itm_m_celestial_plate_heavy_a, itm_m_gauntlets_b, itm_lance, itm_m_mace_knight_pierce, itm_shield_heater_d, itm_m_bascinet_b],  knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3|knows_power_draw_4, 0x0000000e700031cd041f6db6db6dfeff00000000001df6f80000000000000000, khergit_face_middle_2],
  ["knight_3_2", "Lord Astraleon",  "Astraleon", tf_hero, 0, reserved,  fac_kingdom_3, [itm_warhorse, itm_tabard,   itm_m_celestial_plate_a, itm_m_gauntlets_b, itm_lance, itm_m_mace_knight_pierce, itm_shield_heater_d, itm_m_bascinet_a], knight_attrib_2,wp(160),knight_skills_2|knows_power_draw_4, 0x0000000e4900224c049c6db6db6dfeff00000000001df6f00000000000000000, khergit_face_old_2],
  ["knight_3_3", "Lord Celestrian",  "Celestrian", tf_hero, 0, reserved,  fac_kingdom_3, [itm_warhorse, itm_tabard,   itm_m_celestial_plate_heavy_a, itm_m_gauntlets_b, itm_lance, itm_m_mace_knight_pierce, itm_shield_heater_d, itm_m_bascinet_b],  knight_attrib_3,wp(190),knight_skills_3|knows_trainer_5|knows_power_draw_4, 0x0000000e7f002390049f85badb687eff00000000001cf7380000000000000000, khergit_face_older_2],
  ["knight_3_4", "Lord Radiantus", "Radiantus", tf_hero, 0, reserved,  fac_kingdom_3, [itm_warhorse, itm_tabard,   itm_m_celestial_plate_a, itm_m_gauntlets_b, itm_lance, itm_m_mace_knight_pierce, itm_shield_heater_d, itm_m_bascinet_b],  knight_attrib_4,wp(220),knight_skills_4|knows_power_draw_4, 0x000000095c003350048785badb687fff00000000001cf7380000000000000000, khergit_face_older_2],
  ["knight_3_5", "Lord Luminarius",  "Luminarius", tf_hero, 0, reserved,  fac_kingdom_3, [itm_warhorse, itm_gambeson,   itm_m_celestial_plate_b, itm_m_gauntlets_b, itm_lance, itm_m_mace_knight_pierce, itm_shield_heater_d, itm_m_bascinet_b],  knight_attrib_5,wp(250),knight_skills_5|knows_power_draw_4, 0x000000095c003111048785badb695d7f00000000001df7380000000000000000, khergit_face_older_2],
  ["knight_3_6", "Lord Astrafar", "Astrafar", tf_hero, 0, reserved,  fac_kingdom_3, [itm_warhorse, itm_tabard,   itm_m_celestial_plate_a, itm_m_gauntlets_b, itm_lance, itm_m_mace_knight_pierce, itm_shield_heater_d, itm_bascinet_3], knight_attrib_1,wp(130),knight_skills_1|knows_power_draw_4, 0x000000095c003192048785badb6d7d7f00000000001e77380000000000000000, khergit_face_middle_2],
  ["knight_3_7", "Lord Zephyrion","Zephyrion", tf_hero, 0, reserved,  fac_kingdom_3, [itm_warhorse, itm_tabard,   itm_m_celestial_plate_b, itm_m_gauntlets_b, itm_lance, itm_m_mace_knight_pierce, itm_shield_heater_d, itm_bascinet_3], knight_attrib_2,wp(160),knight_skills_2|knows_power_draw_4, 0x000000095c0041d4048785badb6d7d7f00000000001e77380000000000000000, khergit_face_old_2],
  ["knight_3_8", "Lord Starcaster", "Starcaster", tf_hero, 0, reserved,  fac_kingdom_3, [itm_warhorse, itm_tabard,   itm_m_celestial_plate_a, itm_m_gauntlets_b, itm_lance, itm_m_mace_knight_pierce, itm_shield_heater_d, itm_bascinet_3],  knight_attrib_3,wp(190),knight_skills_3|knows_power_draw_4, 0x000000095c005280048785badb6d7d7f00000000001e77380000000000000000, khergit_face_older_2],
  ["knight_3_9", "Lord Dawnbringer","Dawnbringer", tf_hero, 0, reserved,  fac_kingdom_3, [itm_warhorse, itm_gambeson,   itm_m_celestial_plate_b, itm_m_gauntlets_b, itm_lance, itm_m_mace_knight_pierce, itm_shield_heater_d, itm_bascinet_3],  knight_attrib_4,wp(220),knight_skills_4|knows_power_draw_4, 0x000000095c00434d048785badb6d7d7f00000000001ff7380000000000000000, khergit_face_older_2],
  ["knight_3_10", "Lord Solisar","Solisar", tf_hero, 0, reserved,  fac_kingdom_3, [itm_warhorse, itm_tabard,   itm_m_celestial_plate_a, itm_m_gauntlets_b, itm_lance, itm_m_mace_knight_pierce, itm_shield_heater_d, itm_bascinet_3], knight_attrib_5,wp(250),knight_skills_5|knows_trainer_6|knows_power_draw_4, 0x000000095c00338c040c85badb6d7d7f00000000001de7380000000000000000, khergit_face_older_2],
  ["knight_3_11", "Lord Aelion", "Aelion", tf_hero, 0, reserved,  fac_kingdom_3, [itm_warhorse, itm_tabard,   itm_m_celestial_plate_b, itm_m_gauntlets_b, itm_lance, itm_m_mace_knight_pierce, itm_shield_heater_d, itm_bascinet_3],  knight_attrib_1,wp(150),knight_skills_1|knows_power_draw_4, 0x000000095c0054500acc85badb6d7d7f00000000001d47380000000000000000, khergit_face_middle_2],
  ["knight_3_12", "Lord Eclipsar", "Eclipsar", tf_hero, 0, reserved,  fac_kingdom_3, [itm_warhorse, itm_tabard,   itm_m_celestial_plate_b, itm_m_gauntlets_b, itm_lance, itm_m_mace_knight, itm_shield_heater_d, itm_bascinet_3], knight_attrib_2,wp(190),knight_skills_2|knows_power_draw_4, 0x000000095c00301420cf85badb6d7d7f00000000001dc7380000000000000000, khergit_face_old_2],
  ["knight_3_13", "Lord Stellarian","Stellarian", tf_hero, 0, reserved,  fac_kingdom_3, [itm_warhorse, itm_tabard,   itm_m_celestial_plate_a, itm_m_gauntlets_b, itm_lance, itm_m_mace_knight, itm_shield_heater_d, itm_bascinet_3],  knight_attrib_3,wp(200),knight_skills_3|knows_trainer_3|knows_power_draw_4, 0x000000095c0045d320cf85badb6d7d7f00000000001dc7380000000000000000, khergit_face_older_2],
  ["knight_3_14", "Lord Crescentius",  "Crescentius", tf_hero, 0, reserved,  fac_kingdom_3, [itm_warhorse, itm_tabard,   itm_m_celestial_plate_b, itm_m_gauntlets_b, itm_lance, itm_m_mace_knight_pierce, itm_shield_heater_d, itm_bascinet_3],  knight_attrib_4,wp(300),knight_skills_4|knows_trainer_6|knows_power_draw_4, 0x000000094000508020cf85badb6d7d7f00000000001dc7380000000000000000, khergit_face_older_2],
  ["knight_3_15", "Lord Daybreaken", "Daybreaken", tf_hero, 0, reserved,  fac_kingdom_3, [itm_warhorse, itm_tabard,   itm_m_celestial_breastplate_heavy_b, itm_m_gauntlets_b, itm_lance, itm_strange_winged_mace, itm_shield_heater_d, itm_bascinet_3],  knight_attrib_5,wp(240),knight_skills_5|knows_trainer_4|knows_power_draw_4, 0x00000009400041d420cf85badb6d7d7f00000000001dc7380000000000000000, khergit_face_older_2],
  ["knight_3_16", "Lord Zenithor","Zenithor", tf_hero, 0, reserved,  fac_kingdom_3, [itm_warhorse, itm_tabard,   itm_m_celestial_plate_a, itm_m_gauntlets_b, itm_lance, itm_m_mace_knight_pierce, itm_shield_heater_d, itm_bascinet_3],  knight_attrib_1,wp(120),knight_skills_1|knows_power_draw_4, 0x000000094000328520cf85badb6d7d7f00000000001dc7380000000000000000, khergit_face_middle_2],
  ["knight_3_17", "Lord Astraclad", "Astraclad", tf_hero, 0, reserved,  fac_kingdom_3, [itm_warhorse, itm_tabard,   itm_m_celestial_breastplate_heavy_a, itm_m_gauntlets_b, itm_lance, itm_m_mace_knight_pierce, itm_shield_heater_d, itm_bascinet_3],  knight_attrib_2,wp(150),knight_skills_2|knows_power_draw_4, 0x000000094000534620cf85badb6d7d7f00000000001ff7380000000000000000, khergit_face_old_2],
  ["knight_3_18", "Lord Celestium", "Celestium", tf_hero, 0, reserved,  fac_kingdom_3, [itm_warhorse, itm_tabard,   itm_m_celestial_breastplate_heavy_a, itm_m_gauntlets_b, itm_lance, itm_strange_winged_mace, itm_shield_heater_d, itm_bascinet_3],   knight_attrib_3,wp(180),knight_skills_3|knows_trainer_4|knows_power_draw_4, 0x000000097f00338720cf85badb6d7d7f00000000001cf7380000000000000000, khergit_face_older_2],
  ["knight_3_19", "Lord Astronius","Astronius", tf_hero, 0, reserved,  fac_kingdom_3, [itm_warhorse, itm_tabard,   itm_m_celestial_breastplate_heavy_b, itm_m_gauntlets_b, itm_lance, itm_shortened_bill, itm_shield_heater_d, itm_bascinet_2],  knight_attrib_4,wp(210),knight_skills_4|knows_trainer_5|knows_power_draw_4, 0x000000097f00434920cf85badb6d7d7f00000000001fd7380000000000000000, khergit_face_older_2],
  ["knight_3_20", "Lord Phoebus","Phoebus", tf_hero, 0, reserved,  fac_kingdom_3, [itm_warhorse, itm_tabard,   itm_m_celestial_breastplate_c, itm_m_gauntlets_b, itm_lance, itm_m_mace_knight, itm_shield_heater_d, itm_bascinet_3],  knight_attrib_5,wp(240),knight_skills_5|knows_power_draw_4, 0x000000097f00348d211f8dbfdb6d7f7f00000000001ff7780000000000000000, khergit_face_older_2],

  ["knight_4_1", "Viscount Jarni Authfrinson", "Jarni Authfrinson", tf_hero, 0, reserved,  fac_kingdom_4, [itm_rich_outfit,  itm_m_iron_crown_scale_b,     itm_iron_crown_footman_helmet_c, itm_mail_mittens, itm_great_axe, itm_tab_shield_round_d, itm_throwing_axes], knight_attrib_1,wp(130),knight_skills_1, 0x0000000f9300229206db6db6db6dfef600000000001db6f00000000000000000, nord_face_middle_2],
  ["knight_4_2", "Viscount Arnvim", "Arnvim", tf_hero, 0, reserved,  fac_kingdom_4, [ itm_short_tunic,  itm_m_iron_crown_scale_a,   itm_iron_crown_footman_helmet_b, itm_scale_gauntlets, itm_one_handed_battle_axe_c,  itm_tab_shield_round_d, itm_throwing_axes],  knight_attrib_2,wp(160),knight_skills_2|knows_trainer_3, 0x0000000f8d04138436db6db6db6db6ff00000000001db6fb0000000000000000, nord_face_old_2],
  ["knight_4_3", "Viscount Vasti Ansgarson", "Vasti Ansgarson", tf_hero, 0, reserved,  fac_kingdom_4, [itm_warhorse, itm_rich_outfit,  itm_m_iron_crown_scale_b,      itm_scale_gauntlets,   itm_iron_crown_footman_helmet_a,   itm_great_axe, itm_tab_shield_round_e, itm_throwing_axes],  knight_attrib_3,wp(190),knight_skills_3, 0x0000000f8008128412dc6ca636513a7f00000000001f44f80000000000000000, nord_face_older_2],
  ["knight_4_4", "Viscount Hrabbi Laeingrieson", "Hrabbi Laeingrieson", tf_hero, 0, reserved,  fac_kingdom_4, [itm_hunter,   itm_leather_vest,   itm_m_iron_crown_brigandine_mail_b,      itm_scale_gauntlets,  itm_iron_crown_footman_helmet_c, itm_fighting_pick, itm_tab_shield_round_e, itm_throwing_axes],  knight_attrib_4,wp(210),knight_skills_4, 0x0000000fbb0c51c9345b6d36db6dfeff00000000001db6fb0000000000000000, nord_face_older_2],
  ["knight_4_5", "Viscount Stoste Elsnarson", "Stoste Elsnarson", tf_hero, 0, reserved,  fac_kingdom_4, [  itm_fur_coat,   itm_m_iron_crown_brigandine_mail_b,       itm_scale_gauntlets, itm_iron_crown_footman_helmet_c, itm_bastard_sword_b, itm_tab_shield_round_e, itm_throwing_axes, itm_throwing_axes], knight_attrib_5,wp(250),knight_skills_5, 0x0000000fae102307204469e91b6dfef700000000001e56f80000000000000000, nord_face_older_2],
  ["knight_4_6", "Viscount Holti Skellison", "Holti Skellison", tf_hero, 0, reserved,  fac_kingdom_4, [   itm_nomad_robe,   itm_m_iron_crown_scale_a,     itm_iron_crown_nasal_reinforced_c, itm_mail_mittens,   itm_warhammer_b, itm_tab_shield_round_d],   knight_attrib_1,wp(130),knight_skills_1, 0x00000004ae101349204469e91b6dfef700000000001d46f80000000000000000, nord_face_middle_2],
  ["knight_4_7", "Viscount Arlir", "Arlir", tf_hero, 0, reserved,  fac_kingdom_4, [  itm_fur_coat,   itm_m_iron_crown_brigandine_mail_b,     itm_iron_crown_nasal_reinforced_b, itm_m_gauntlets_a,   itm_sword_viking_3, itm_shortened_military_scythe,  itm_tab_shield_round_d],   knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x00000004ba0c0187128c4db6db6ddd3f00000000001db6f00000000000000000, nord_face_old_2],
  ["knight_4_8", "Viscount Asker", "Asker", tf_hero, 0, reserved,  fac_kingdom_4, [ itm_rich_outfit,  itm_m_iron_crown_brigandine_mail_a,        itm_iron_crown_nasal_reinforced_b, itm_m_gauntlets_a, itm_warhammer,  itm_tab_shield_round_e, itm_throwing_axes],   knight_attrib_3,wp(190),knight_skills_3, 0x000000048a0c2354645469b91b6dbeff00000000001ec6fb0000000000000000, nord_face_older_2],
  ["knight_4_9", "Viscount Berglja", "Berglja", tf_hero, 0, reserved,  fac_kingdom_4, [itm_warhorse, itm_nomad_robe,   itm_m_iron_crown_brigandine_mail_b,     itm_iron_crown_nasal_reinforced_c, itm_m_gloves_a, itm_arrows, itm_long_bow,   itm_one_handed_battle_axe_c,  itm_tab_shield_round_e],  knight_attrib_4,wp(220),knight_skills_4|knows_trainer_5|knows_power_draw_4, 0x00000004b604229434a26934db6dbefb00000000001d36f10000000000000000, nord_face_older_2],
  ["knight_4_10", "Viscount Arikr", "Arikr", tf_hero, 0, reserved,  fac_kingdom_4, [itm_hunter,   itm_courtly_outfit,   itm_m_iron_crown_scale_b,      itm_m_gauntlets_a,  itm_iron_crown_nasal_reinforced_c ,itm_great_axe, itm_tab_shield_round_e],  knight_attrib_5,wp(250),knight_skills_5|knows_trainer_6, 0x00000003c110128176db6db6db6dfeff00000000001c76fb0000000000000000, nord_face_older_2],
  ["knight_4_11", "Viscount Oslat", "Oslat", tf_hero, 0, reserved,  fac_kingdom_4, [ itm_rich_outfit,  itm_m_iron_crown_brigandine_mail_a,     itm_iron_crown_nasal_reinforced_a,  itm_m_gauntlets_b,  itm_great_bardiche, itm_tab_shield_round_d], knight_attrib_1,wp(140),knight_skills_1, 0x00000001ed102005211c45bb236e5efd00000000001ef2f80000000000000000, nord_face_middle_2],
  ["knight_4_12", "Viscount Berti Beinison", "Berti Beinison", tf_hero, 0, reserved,  fac_kingdom_4, [ itm_short_tunic,  itm_m_iron_crown_brigandine_mail_b,   itm_iron_crown_nasal_reinforced_c,  itm_m_gauntlets_b,  itm_one_handed_battle_axe_c,  itm_tab_shield_round_d],  knight_attrib_2,wp(200),knight_skills_2, 0x00000001f3103252125b6db6db6dbeff00000000001dc6f80000000000000000, nord_face_old_2],
  ["knight_4_13", "Viscount Haukri Gadison", "Haukri Gadison", tf_hero, 0, reserved,  fac_kingdom_4, [itm_warhorse, itm_rich_outfit,  itm_m_iron_crown_brigandine_mail_b,      itm_scale_gauntlets,   itm_iron_crown_nasal_c,   itm_maul, itm_tab_shield_round_e],  knight_attrib_3,wp(250),knight_skills_3|knows_trainer_3, 0x00000001d71001c920db6db6db6ddff700000000001c56f80000000000000000, nord_face_older_2],
  ["knight_4_14", "Viscount Kari", "Kari", tf_hero, 0, reserved,  fac_kingdom_4, [  itm_leather_vest,   itm_m_iron_crown_brigandine_mail_b,     itm_iron_crown_nasal_b, itm_scale_gauntlets, itm_fighting_pick, itm_tab_shield_round_e, itm_throwing_axes],  knight_attrib_4,wp(200),knight_skills_4, 0x00000001f800028712db6da55c6dfefe00000000001e46b80000000000000000, nord_face_older_2],
  ["knight_4_15", "Viscount Butre", "Butre", tf_hero, 0, reserved,  fac_kingdom_4, [itm_hunter,   itm_leather_jacket,   itm_m_iron_crown_brigandine_mail_a,    itm_scale_gauntlets,  itm_iron_crown_nasal_reinforced_c, itm_sword_of_war, itm_tab_shield_round_e], knight_attrib_5,wp(290),knight_skills_5|knows_trainer_6, 0x00000001f110435412db6db6946dfeff00000000001e26f10000000000000000, nord_face_older_2],
  ["knight_4_16", "Viscount Fastri Therison", "Fastri Therison", tf_hero, 0, reserved,  fac_kingdom_4, [   itm_nomad_robe,   itm_m_iron_crown_brigandine_mail_a,     itm_iron_crown_nasal_reinforced_c, itm_mail_mittens,   itm_maul, itm_tab_shield_round_d, itm_throwing_axes],   knight_attrib_1,wp(120),knight_skills_1, 0x00000001cc0c058420d35128dc6ddaf600000000001db6f90000000000000000, nord_face_middle_2],
  ["knight_4_17", "Viscount Kjarki", "Kjarki", tf_hero, 0, reserved,  fac_kingdom_4, [  itm_fur_coat,   itm_m_iron_crown_brigandine_mail_a,     itm_iron_crown_nasal_c, itm_mail_mittens,   itm_sword_viking_3,  itm_tab_shield_round_d, itm_throwing_axes],   knight_attrib_2,wp(150),knight_skills_2|knows_trainer_4, 0x00000001e808028a36db6db6db6dfcf600000000001db6fb0000000000000000, nord_face_old_2],
  ["knight_4_18", "Viscount Thore Geirrison", "Thore Geirrison", tf_hero, 0, reserved,  fac_kingdom_4, [ itm_rich_outfit,  itm_m_iron_crown_brigandine_b,      itm_iron_crown_nasal_c, itm_scale_gauntlets, itm_sword_viking_3, itm_sword_of_war,  itm_iron_crown_nasal_a],   knight_attrib_3,wp(180),knight_skills_3, 0x00000001e808120836db6db6db6dfcf600000000001db6fb0000000000000000, nord_face_older_2],
  ["knight_4_19", "Viscount Grimi Thorstison", "Grimi Thorstison", tf_hero, 0, reserved,  fac_kingdom_4, [itm_warhorse, itm_nomad_robe,   itm_m_iron_crown_brigandine_a,   itm_iron_crown_nasal_b, itm_scale_gauntlets,   itm_one_handed_battle_axe_c,  itm_tab_shield_round_e, itm_throwing_axes],  knight_attrib_4,wp(210),knight_skills_4|knows_trainer_5, 0x00000001c008314712db6db6db6ddefe00000000001cc6bb0000000000000000, nord_face_older_2],
  ["knight_4_20", "Viscount There Hognison", "There Hognison", tf_hero, 0, reserved,  fac_kingdom_4, [itm_hunter,   itm_courtly_outfit,   itm_m_iron_crown_brigandine_b,      itm_scale_gauntlets,  itm_iron_crown_nasal_reinforced_c,itm_great_axe, itm_tab_shield_round_e, itm_throwing_axes],  knight_attrib_5,wp(240),knight_skills_5, 0x00000001c0082191365b6db6db6d8ef600000000001db6ff0000000000000000, nord_face_older_2],

  ["knight_5_1", "Count Atris", "Atris", tf_hero, 0, reserved,  fac_kingdom_5, [itm_hunter,itm_tabard,   itm_m_alpine_full_plate_a,itm_alpine_footman_helmet_visored_b,itm_m_gauntlets_a, itm_morningstar,itm_shield_heater_d, itm_guisarme],     knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x000000079e00625116db6db6db6ddaed00000000001db6ea0000000000000000, rhodok_face_middle_2],
  ["knight_5_2", "Count Giersa", "Giersa", tf_hero, 0, reserved,  fac_kingdom_5, [itm_hunter,itm_tabard,   itm_m_alpine_full_plate_a,itm_alpine_footman_helmet_visored_b,itm_m_gauntlets_b, itm_crusader_sword,itm_shield_heater_d, itm_bec_de_corbin],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x00000007bc00019416db6db6db6ddaed00000000001db6ea0000000000000000, rhodok_face_old_2],
  ["knight_5_3", "Count Amartz", "Amartz", tf_hero, 0, reserved,  fac_kingdom_5, [itm_hunter,itm_tabard,   itm_m_alpine_full_plate_a,itm_alpine_footman_helmet_visored_b,itm_m_gauntlets_b, itm_longsword,itm_shield_heater_d, itm_poleaxe_a],    knight_attrib_3,wp(190),knight_skills_3, 0x00000007bc00414916db6db6db6ddaed00000000001db6ea0000000000000000, rhodok_face_older_2],
  ["knight_5_4", "Count Resa", "Resa", tf_hero, 0, reserved,  fac_kingdom_5, [itm_hunter,itm_tabard,   itm_m_alpine_corrazina_full_c,itm_alpine_footman_helmet_visored_a,itm_m_gauntlets_b, itm_longsword,itm_shield_heater_d, itm_elegant_poleaxe],    knight_attrib_4,wp(220),knight_skills_4, 0x00000007ac00300936db6db6db6decee00000000001db6f30000000000000000, rhodok_face_older_2],
  ["knight_5_5", "Count Jaufre", "Jaufre", tf_hero, 0, reserved,  fac_kingdom_5, [itm_hunter,itm_tabard,   itm_m_alpine_corrazina_full_b,itm_alpine_footman_helmet_visored_a,itm_m_gauntlets_a, itm_morningstar,itm_shield_heater_d, itm_guisarme], knight_attrib_5,wp(250),knight_skills_5, 0x00000007860400cf049b6db6db6ddef700000000001db6e80000000000000000, rhodok_face_older_2],
  ["knight_5_6", "Count Ulis", "Ulis", tf_hero, 0, reserved,  fac_kingdom_5, [itm_hunter,itm_tabard,   itm_m_alpine_corrazina_full_c,itm_alpine_footman_helmet_mail_c,itm_m_gauntlets_a, itm_grosse_messer_b,itm_shield_heater_d, itm_poleaxe_a],    knight_attrib_1,wp(130),knight_skills_1, 0x00000007840405cf3edb6db6db6dbef600000000001e36fb0000000000000000, rhodok_face_middle_2],
  ["knight_5_7", "Count Girve", "Girve", tf_hero, 0, reserved,  fac_kingdom_5, [itm_hunter,itm_tabard,   itm_m_alpine_full_plate_a,itm_alpine_footman_helmet_mail_c,itm_m_gauntlets_a, itm_grosse_messer_b,itm_shield_heater_d, itm_german_poleaxe],     knight_attrib_2,wp(160),knight_skills_2, 0x00000007bd10101316db69b6db6dbcf700000000001db6f00000000000000000, rhodok_face_old_2],
  ["knight_5_8", "Count Anaics", "Anaics", tf_hero, 0, reserved,  fac_kingdom_5, [itm_hunter,itm_tabard,   itm_m_alpine_corrazina_full_c,itm_alpine_footman_helmet_mail_b,itm_m_gloves_a, itm_grosse_messer_b,itm_shield_heater_d, itm_english_bill],    knight_attrib_3,wp(190),knight_skills_3|knows_trainer_3, 0x000000078b00019236db6db8d36dfefe00000000001d453b0000000000000000, rhodok_face_older_2],

  ["knight_5_9", "Count Robertr", "Robertr", tf_hero, 0, reserved,  fac_kingdom_5, [itm_saddle_horse,itm_tabard,   itm_m_alpine_corrazina_full_c,itm_alpine_footman_helmet_mail_b,itm_m_gauntlets_a, itm_morningstar,itm_shield_heater_d, itm_guisarme],   knight_attrib_4,wp(220),knight_skills_4|knows_trainer_6, 0x00000007ac10151436db6db6db6deeff00000000001db6f90000000000000000, rhodok_face_older_2],
  ["knight_5_10", "Count Tibalts", "Tibalts", tf_hero, 0, reserved,  fac_kingdom_5, [itm_saddle_horse,itm_tabard,   itm_m_alpine_corrazina_full_b,itm_alpine_footman_helmet_mail_c,itm_m_gauntlets_a, itm_morningstar,itm_shield_heater_d, itm_english_bill],  knight_attrib_5,wp(250),knight_skills_5|knows_trainer_4, 0x000000079600609112ec40aad2b8ff7f00000000001e36f80000000000000000, rhodok_face_older_2],
  ["knight_5_11", "Count Jausa", "Jausa", tf_hero, 0, reserved,  fac_kingdom_5, [itm_saddle_horse,itm_tabard,   itm_m_alpine_corrazina_full_a,itm_alpine_footman_helmet_mail_a,itm_m_gauntlets_a, itm_german_bastard_sword,itm_shield_heater_d, itm_poleaxe_a],     knight_attrib_1,wp(130),knight_skills_1, 0x00000007a0001047208d723913adcd7700000000001d4cb80000000000000000, rhodok_face_middle_2],
  ["knight_5_12", "Count Seli", "Seli", tf_hero, 0, reserved,  fac_kingdom_5, [itm_saddle_horse,itm_tabard,   itm_m_alpine_corrazina_full_c,itm_alpine_footman_helmet_mail_a,itm_m_gauntlets_a, itm_side_sword,itm_shield_heater_d, itm_guisarme],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_5, 0x000000079d08420a12db6db6db6dff7f00000000001c76f80000000000000000, rhodok_face_old_2],
  ["knight_5_13", "Count Gauda", "Gauda", tf_hero, 0, reserved,  fac_kingdom_5, [itm_saddle_horse,itm_tabard,   itm_m_alpine_corrazina_full_b,itm_alpine_footman_helmet_mail_a,itm_m_gauntlets_a, itm_side_sword,itm_shield_heater_d, itm_german_poleaxe],    knight_attrib_3,wp(190),knight_skills_3, 0x000000078a04018158db6dd69c8decf600000000001db6f20000000000000000, rhodok_face_older_2],
  ["knight_5_14", "Count Girve", "Girve", tf_hero, 0, reserved,  fac_kingdom_5, [itm_saddle_horse,itm_tabard,   itm_m_alpine_corrazina_full_a,itm_alpine_footman_helmet_mail_c,itm_m_gauntlets_a, itm_italian_sword,itm_shield_heater_d, itm_guisarme],    knight_attrib_4,wp(220),knight_skills_4, 0x00000007a00c3548491b72599b55ff3700000000001d58bb0000000000000000, rhodok_face_older_2],
  ["knight_5_15", "Count Ganeus", "Ganeus", tf_hero, 0, reserved,  fac_kingdom_5, [itm_saddle_horse,itm_tabard,   itm_m_alpine_corrazina_full_b,itm_alpine_footman_helmet_mail_c,itm_m_gauntlets_a, itm_morningstar,itm_shield_heater_d, itm_poleaxe_a], knight_attrib_5,wp(250),knight_skills_5, 0x00000007ab08350512e46d299c3dff7f00000000001d36b80000000000000000, rhodok_face_older_2],
  ["knight_5_16", "Count Giri", "Giri", tf_hero, 0, reserved,  fac_kingdom_5, [itm_saddle_horse,itm_tabard,   itm_m_alpine_corrazina_full_c,itm_alpine_footman_helmet_c,itm_m_gauntlets_a, itm_italian_sword,itm_shield_heater_d, itm_guisarme],    knight_attrib_1,wp(120),knight_skills_1, 0x000000079110124536eb71c6d36ddeff00000000001d36fb0000000000000000, rhodok_face_middle_2],
  ["knight_5_17", "Count Sego", "Sego", tf_hero, 0, reserved,  fac_kingdom_5, [itm_saddle_horse,itm_tabard,   itm_m_alpine_corrazina_full_b,itm_alpine_footman_helmet_c,itm_m_gauntlets_a, itm_morningstar,itm_shield_heater_d, itm_english_bill],     knight_attrib_2,wp(150),knight_skills_2, 0x00000007860c554f201b6db6db6efeff00000000001ff6f10000000000000000, rhodok_face_old_2],
  ["knight_5_18", "Count Bove", "Bove", tf_hero, 0, reserved,  fac_kingdom_5, [itm_saddle_horse,itm_tabard,   itm_m_alpine_corrazina_b,itm_alpine_footman_helmet_c,itm_m_gauntlets_a, itm_side_sword,itm_shield_heater_d, itm_guisarme],    knight_attrib_3,wp(180),knight_skills_3, 0x00000007b40424460edb6db6db6ddafe00000000001db6b80000000000000000, rhodok_face_older_2],
  ["knight_5_19", "Count Giersa", "Giersa", tf_hero, 0, reserved,  fac_kingdom_5, [itm_saddle_horse,itm_tabard,   itm_m_alpine_corrazina_b,itm_alpine_footman_helmet_a,itm_m_gauntlets_a, itm_german_bastard_sword,itm_shield_heater_d, itm_danish_greatsword],   knight_attrib_4,wp(210),knight_skills_4|knows_trainer_5, 0x00000007a70c40c8131b6db6db6dfcf600000000001cc5390000000000000000, rhodok_face_older_2],
  ["knight_5_20", "Count Reli", "Reli", tf_hero, 0, reserved,  fac_kingdom_5, [itm_saddle_horse,itm_tabard,   itm_m_alpine_corrazina_a,itm_alpine_footman_helmet_b,itm_m_gauntlets_a, itm_morningstar,itm_shield_heater_d, itm_poleaxe_a],  knight_attrib_5,wp(240),knight_skills_5|knows_trainer_6, 0x00000007810042946d138ee50a71fcf700000000001ec7610000000000000000, rhodok_face_older_2],

  ["knight_6_1", "Emir Jaha", "Jaha", tf_hero, 0, reserved,  fac_kingdom_6, [itm_saracin_hard_horses_a_v1,itm_mkk_mamluke_a,itm_solarian_helmet_mask_b, itm_eastern_scale_gloves_b,itm_heavy_lance, itm_sarranid_cavalry_sword,itm_tab_shield_small_round_c],     knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x0000000af80c335420db6dcadb6dbef600000000001dd6f80000000000000000, rhodok_face_middle_2],
  ["knight_6_2", "Emir Khara", "Khara", tf_hero, 0, reserved,  fac_kingdom_6, [itm_saracin_hard_horses_b_v1,itm_mkk_mamluke_b,itm_solarian_helmet_mask_b, itm_eastern_scale_gloves_b,itm_heavy_lance, itm_sarranid_cavalry_sword,itm_tab_shield_small_round_c],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x0000000af80c544620db6dcadb6dbef600000000001dd6f80000000000000000, rhodok_face_old_2],
  ["knight_6_3", "Emir Khamra", "Khamra", tf_hero, 0, reserved,  fac_kingdom_6, [itm_saracin_hard_horses_c_v1,itm_mkk_mamluke_c,itm_solarian_helmet_mask_a, itm_eastern_scale_gloves_a,itm_heavy_lance, itm_sarranid_cavalry_sword,itm_tab_shield_small_round_c],    knight_attrib_3,wp(190),knight_skills_3, 0x0000000af80c628020db6dcadb6dbef600000000001dd6f80000000000000000, rhodok_face_older_2],
  ["knight_6_4", "Emir Raima", "Raima", tf_hero, 0, reserved,  fac_kingdom_6, [itm_saracin_hard_horses_c_v1,itm_mkk_mamluke_c,itm_solarian_helmet_mask_b, itm_eastern_scale_gloves_a,itm_heavy_lance, itm_sarranid_cavalry_sword,itm_tab_shield_small_round_c],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000ac00c229120db6dcadb6dbef600000000001dd6f80000000000000000, rhodok_face_older_2],
  ["knight_6_5", "Emir Taizzah", "Taizzah", tf_hero, 0, reserved,  fac_kingdom_6, [itm_saracin_hard_horses_b_v1,itm_mkk_mamluke_b,itm_solarian_helmet_mask_b, itm_eastern_scale_gloves_a,itm_heavy_lance, itm_sarranid_cavalry_sword,itm_tab_shield_small_round_c], knight_attrib_5,wp(250),knight_skills_5, 0x0000000ac00c421220db6dcadb6dbef600000000001dd6f80000000000000000, rhodok_face_older_2],
  ["knight_6_6", "Emir Rana", "Rana", tf_hero, 0, reserved,  fac_kingdom_6, [itm_saracin_hard_horses_c_v1,itm_mkk_mamluke_a,itm_solarian_helmet_mask_a, itm_eastern_scale_gloves_b,itm_heavy_lance, itm_sarranid_cavalry_sword,itm_tab_shield_small_round_c],    knight_attrib_1,wp(130),knight_skills_1, 0x0000000ac00c525420db6dcadb6dbef600000000001dd6f80000000000000000, rhodok_face_middle_2],
  ["knight_6_7", "Emir Taquw", "Taquw", tf_hero, 0, reserved,  fac_kingdom_6, [itm_saracin_hard_horses_a_v1,itm_mkk_mamluke_b,itm_solarian_helmet_mask_b, itm_eastern_scale_gloves_b,itm_heavy_lance, itm_sarranid_cavalry_sword,itm_tab_shield_small_round_c],     knight_attrib_2,wp(160),knight_skills_2, 0x0000000ac00c500520db6dcadb6dbef600000000001dd6f80000000000000000, rhodok_face_old_2],
  ["knight_6_8", "Emir Jizah", "Jizah", tf_hero, 0, reserved,  fac_kingdom_6, [itm_saracin_hard_horses_c_v1,itm_mkk_mamluke_c,itm_solarian_heavy_helmet_c, itm_mail_mittens,itm_heavy_lance, itm_sarranid_cavalry_sword,itm_tab_shield_small_round_c],    knight_attrib_3,wp(190),knight_skills_3|knows_trainer_3, 0x0000000ac00c75c620db6dcadb6dbef600000000001dd6f80000000000000000, rhodok_face_older_2],
  ["knight_6_9", "Emir Raha", "Raha", tf_hero, 0, reserved,  fac_kingdom_6, [itm_saracin_hard_horses_a_v1,itm_mkk_mamluke_a,itm_solarian_heavy_helmet_d, itm_mail_mittens,itm_heavy_lance, itm_sarranid_cavalry_sword,itm_tab_shield_small_round_c],   knight_attrib_4,wp(220),knight_skills_4|knows_trainer_6, 0x0000000ac00c710720db6dcadb6dbef600000000001dd6f80000000000000000, rhodok_face_older_2],
  ["knight_6_10", "Emir Nasla", "Nasla", tf_hero, 0, reserved,  fac_kingdom_6, [itm_saracin_hard_horses_d_v1,itm_mkk_mamluke_b,itm_solarian_helmet_mask_a, itm_mail_mittens,itm_heavy_lance, itm_sarranid_cavalry_sword,itm_tab_shield_small_round_c],  knight_attrib_5,wp(250),knight_skills_5|knows_trainer_4, 0x0000000af80c114620db6dcadb6dbef600000000001dd6f80000000000000000, rhodok_face_older_2],
  ["knight_6_11", "Emir Bura", "Bura", tf_hero, 0, reserved,  fac_kingdom_6, [itm_saracin_hard_horses_d_v1,itm_solarian_armor_scale_a,itm_solarian_helmet_mask_b, itm_mail_mittens,itm_heavy_lance, itm_sarranid_cavalry_sword,itm_tab_shield_small_round_c],     knight_attrib_1,wp(130),knight_skills_1, 0x0000000af80c318420db6dcadb6dbef600000000001dd6f80000000000000000, rhodok_face_middle_2],
  ["knight_6_12", "Emir Majmi", "Majmi", tf_hero, 0, reserved,  fac_kingdom_6, [itm_saracin_hard_horses_a_v1,itm_solarian_armor_scale_a,itm_solarian_heavy_helmet_c, itm_leather_gloves,itm_heavy_lance, itm_sarranid_cavalry_sword,itm_tab_shield_small_round_c],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_5, 0x0000000af80c51c420db6dcadb6dbef600000000001dd6f80000000000000000, rhodok_face_old_2],
  ["knight_6_13", "Emir Madha", "Madha", tf_hero, 0, reserved,  fac_kingdom_6, [itm_saracin_hard_horses_a_v1,itm_solarian_armor_scale_a,itm_solarian_heavy_helmet_d, itm_leather_gloves,itm_heavy_lance, itm_sarranid_cavalry_sword,itm_tab_shield_small_round_c],    knight_attrib_3,wp(190),knight_skills_3, 0x0000000af80c728320db6dcadb6dbef600000000001dd6f80000000000000000, rhodok_face_older_2],
  ["knight_6_14", "Emir Qaiquw", "Qaiquw", tf_hero, 0, reserved,  fac_kingdom_6, [itm_saracin_hard_horses_b_v1,itm_solarian_armor_scale_c,itm_solarian_heavy_helmet_c, itm_leather_gloves,itm_heavy_lance, itm_sarranid_cavalry_sword,itm_tab_shield_small_round_c],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000af80c72c020db6dcadb6dbef600000000001dd6f80000000000000000, rhodok_face_older_2],
  ["knight_6_15", "Emir Maila", "Maila", tf_hero, 0, reserved,  fac_kingdom_6, [itm_saracin_hard_horses_a_v1,itm_solarian_armor_scale_a,itm_solarian_heavy_helmet_e, itm_leather_gloves,itm_heavy_lance, itm_sarranid_cavalry_sword,itm_tab_shield_small_round_c], knight_attrib_5,wp(250),knight_skills_5, 0x0000000ac00c029020db6dcadb6dbef600000000001dd6f80000000000000000, rhodok_face_older_2],
  
  ["knight_6_16", "Emir Shaira", "Shaira", tf_hero, 0, reserved,  fac_kingdom_6, [itm_saracin_hard_horses_a_v1,itm_solarian_armor_scale_c,itm_solarian_helmet_d, itm_leather_gloves,itm_heavy_lance, itm_sarranid_cavalry_sword,itm_tab_shield_small_round_c],    knight_attrib_1,wp(120),knight_skills_1, 0x0000000aff0c630a20db6dcadb6dbef600000000001dd6f80000000000000000, rhodok_face_middle_2],
  ["knight_6_17", "Emir Arjah", "Arjah", tf_hero, 0, reserved,  fac_kingdom_6, [itm_saracin_hard_horses_d_v1,itm_solarian_armor_scale_c,itm_adid_helmet_a, itm_leather_gloves,itm_heavy_lance, itm_sarranid_cavalry_sword,itm_tab_shield_small_round_c],     knight_attrib_2,wp(150),knight_skills_2, 0x0000000aff0c034920db6dcadb6dbef600000000001dd6f80000000000000000, rhodok_face_old_2],
  ["knight_6_18", "Emir Sayli", "Sayli", tf_hero, 0, reserved,  fac_kingdom_6, [itm_saracin_hard_horses_c_v1,itm_solarian_armor_a,itm_adid_helmet_b, itm_leather_gloves,itm_heavy_lance, itm_sarranid_cavalry_sword,itm_tab_shield_small_round_c],    knight_attrib_3,wp(180),knight_skills_3, 0x0000000aff0c134820db6dcadb6dbef600000000001dd6f80000000000000000, rhodok_face_older_2],
  ["knight_6_19", "Emir Bami", "Bami", tf_hero, 0, reserved,  fac_kingdom_6, [itm_saracin_hard_horses_b_v1,itm_solarian_armor_b,itm_adid_helmet_c, itm_leather_gloves,itm_heavy_lance, itm_sarranid_cavalry_sword,itm_tab_shield_small_round_c],   knight_attrib_4,wp(210),knight_skills_4|knows_trainer_5, 0x0000000aff0c328720db6dcadb6dbef600000000001dd6f80000000000000000, rhodok_face_older_2],
  ["knight_6_20", "Emir Makka", "Makka", tf_hero, 0, reserved,  fac_kingdom_6, [itm_saracin_hard_horses_a_v1,itm_solarian_armor_c,itm_solarian_helmet_c, itm_leather_gloves,itm_heavy_lance, itm_sarranid_cavalry_sword,itm_tab_shield_small_round_c],  knight_attrib_5,wp(240),knight_skills_5|knows_trainer_6, 0x0000000ac00c624620db6dcadb6dbef600000000001dd6f80000000000000000, rhodok_face_older_2],

  ["knight_7_1", "Duke Evelyn Silvermoor", "Evelyn", tf_hero, 0, reserved, fac_kingdom_7, [itm_mt_horse_b3, itm_nerpa_shirt_a,   itm_m_nerpa_coat_of_plates_heavy_b, itm_m_gauntlets_b, itm_longsword, itm_steel_shield, itm_nerpa_barbuta_mail_b, itm_jarid, itm_heavy_lance], knight_attrib_5,wp(250),knight_skills_5, 0x0000000e4408239436db6db6db6dddad00000000001db6fb0000000000000000, rhodok_face_older_2],
  ["knight_7_2", "Duke Roland Stormcrest", "Roland", tf_hero, 0, reserved, fac_kingdom_7, [itm_mt_horse_b3, itm_nerpa_shirt_a,   itm_m_nerpa_coat_of_plates_heavy_b, itm_m_gauntlets_b, itm_longsword, itm_steel_shield, itm_nerpa_barbuta_mail_b, itm_jarid, itm_heavy_lance], knight_attrib_5,wp(250),knight_skills_5, 0x0000000c4408335336db6db6db6dddad00000000001db6f80000000000000000, rhodok_face_older_2],
  ["knight_7_3", "Duke Hugo Stonehelm", "Hugo", tf_hero, 0, reserved, fac_kingdom_7, [itm_mt_horse_b3, itm_nerpa_shirt_a,   itm_m_nerpa_coat_of_plates_heavy_b, itm_m_gauntlets_b, itm_longsword, itm_steel_shield, itm_nerpa_barbuta_mail_b, itm_jarid, itm_heavy_lance], knight_attrib_5,wp(250),knight_skills_5, 0x0000000fc408431137db6db6db0dfdb600000000001db6f80000000000000000, rhodok_face_older_2],
  ["knight_7_4", "Duke Cedric Ironwood", "Cedric", tf_hero, 0, reserved, fac_kingdom_7, [itm_mt_horse_b3, itm_nerpa_shirt_a,   itm_m_nerpa_coat_of_plates_heavy_b, itm_m_gauntlets_b, itm_longsword, itm_steel_shield, itm_nerpa_barbuta_mail_b, itm_jarid, itm_heavy_lance], knight_attrib_5,wp(250),knight_skills_5, 0x00000003840802cf06db6db6db6ddffe00000000001db6f80000000000000000, rhodok_face_older_2],
  ["knight_7_5", "Duke Aldric Blackwater", "Aldric", tf_hero, 0, reserved, fac_kingdom_7, [itm_mt_horse_b3, itm_nerpa_shirt_a,   itm_m_nerpa_coat_of_plates_heavy_a, itm_m_gauntlets_a, itm_military_cleaver_c, itm_steel_shield, itm_nerpa_barbuta_mail_b, itm_throwing_knives, itm_lance], knight_attrib_5,wp(250),knight_skills_5, 0x000000038408129106db6db6db6ddffe00000000001db6f80000000000000000, rhodok_face_older_2],
  ["knight_7_6", "Duke Thaddeus Ravenshore", "Thaddeus", tf_hero, 0, reserved, fac_kingdom_7, [itm_mt_horse_b3, itm_nerpa_shirt_a,   itm_m_nerpa_coat_of_plates_heavy_a, itm_m_gauntlets_a, itm_grosse_messer_b, itm_steel_shield, itm_nerpa_barbuta_mail_b, itm_throwing_knives, itm_lance], knight_attrib_5,wp(250),knight_skills_5, 0x00000003800822c904db6db6db6ddffe00000000001fb6f80000000000000000, rhodok_face_older_2],
  ["knight_7_7", "Duke Leopold Goldenfield", "Leopold", tf_hero, 0, reserved, fac_kingdom_7, [itm_mt_horse_b3, itm_nerpa_shirt_a,   itm_m_nerpa_coat_of_plates_heavy_a, itm_m_gauntlets_a, itm_military_cleaver_b, itm_steel_shield, itm_nerpa_barbuta_mail_b, itm_throwing_knives, itm_lance], knight_attrib_5,wp(250),knight_skills_5, 0x0000000bbf08248536db6db6db6debad00000000001db6db0000000000000000, rhodok_face_older_2],
  ["knight_7_8", "Duke Magnus Stormpeak", "Magnus", tf_hero, 0, reserved, fac_kingdom_7, [itm_mt_horse_b3, itm_nerpa_shirt_a,   itm_m_nerpa_coat_of_plates_heavy_a, itm_m_gauntlets_a, itm_grosse_messer_b, itm_tab_shield_pavise_d, itm_nerpa_barbuta_mail_b, itm_throwing_knives, itm_lance], knight_attrib_5,wp(250),knight_skills_5, 0x0000000e8008344f36db6db6db6debad00000000001db6fb0000000000000000, rhodok_face_older_2],

  # younger knights
  ["knight_7_9", "Duke Ashton", "Ashton", tf_hero, 0, reserved,  fac_kingdom_7, [itm_mt_horse_b3, itm_nerpa_shirt_a,   itm_m_nerpa_coat_of_plates_heavy_b, itm_m_gauntlets_a, itm_longsword, itm_shield_heater_d, itm_nerpa_barbuta_mail_a, itm_throwing_knives, itm_lance],    knight_attrib_3,wp(160),knight_skills_3, 0x0000000ac400314520db6db6db6dfcff00000000001db6f80000000000000000, swadian_face_old_2],
  ["knight_7_10", "Duke Zelenn", "Zelenn", tf_hero, 0, reserved,  fac_kingdom_7, [itm_mt_horse_b3, itm_nerpa_shirt_a,   itm_m_nerpa_coat_of_plates_heavy_a, itm_m_gauntlets_a, itm_longsword, itm_shield_heater_d, itm_nerpa_barbuta_mail_b, itm_lance],   knight_attrib_3,wp(190),knight_skills_3, 0x0000000ac400418620db6db6db6dfcff00000000001db6f80000000000000000, swadian_face_older_2],
  ["knight_7_11", "Duke Cangann", "Cangann", tf_hero, 0, reserved,  fac_kingdom_7, [itm_mt_horse_b3, itm_nerpa_shirt_a,   itm_m_nerpa_coat_of_plates_medium_b, itm_m_gauntlets_a, itm_longsword, itm_tab_shield_pavise_d, itm_nerpa_barbuta_open_padded_b, itm_lance],       knight_attrib_3,wp(220),knight_skills_3, 0x0000000ac00071c620db6db6db6dfcff00000000001db6f80000000000000000, swadian_face_older_2],
  ["knight_7_12", "Duke Yrosh", "Yrosh", tf_hero, 0, reserved,  fac_kingdom_7, [itm_mt_horse_b3, itm_nerpa_shirt_a,   itm_m_nerpa_coat_of_plates_heavy_a, itm_m_gauntlets_a, itm_longsword, itm_tab_shield_pavise_d, itm_nerpa_barbuta_open_padded_b, itm_lance],    knight_attrib_3,wp(130),knight_skills_3, 0x0000000ac00020c520db6db6db6dfcff00000000001db6f80000000000000000, swadian_face_older_2],
  ["knight_7_13", "Duke Liber", "Liber", tf_hero, 0, reserved,  fac_kingdom_7, [itm_mt_horse_b3, itm_nerpa_shirt_a,   itm_m_nerpa_coat_of_plates_medium_b, itm_m_gauntlets_a, itm_grosse_messer_b, itm_tab_shield_pavise_d, itm_nerpa_barbuta_open_padded_b, itm_war_darts, itm_lance],   knight_attrib_2,wp(160),knight_skills_2, 0x0000000afd00314420db6db6db6dfcff00000000001db6f80000000000000000, swadian_face_older_2],
  ["knight_7_14", "Duke George", "George", tf_hero, 0, reserved,  fac_kingdom_7, [itm_mt_horse_b3, itm_nerpa_shirt_a,   itm_m_nerpa_coat_of_plates_medium_b, itm_m_gauntlets_a, itm_side_sword, itm_steel_shield, itm_nerpa_barbuta_mail_a, itm_war_darts, itm_lance],    knight_attrib_2,wp(190),knight_skills_3|knows_trainer_6, 0x0000000ac000028420db6db6db6dfcff00000000001db6f80000000000000000, swadian_face_older_2],
  ["knight_7_15", "Duke Jay", "Jay", tf_hero, 0, reserved,  fac_kingdom_7, [itm_mt_horse_b3, itm_nerpa_shirt_a,   itm_m_nerpa_coat_of_plates_medium_b, itm_m_gauntlets_a, itm_side_sword, itm_shield_heater_d, itm_nerpa_barbuta_open_padded_b, itm_war_darts, itm_lance],      knight_attrib_4,wp(140),knight_skills_2, 0x0000000afd00629420db6db6db6dfcff00000000001db6f80000000000000000, swadian_face_young_2],
  ["knight_7_16", "Duke Itreth", "Itreth", tf_hero, 0, reserved,  fac_kingdom_7, [itm_mt_horse_b3, itm_nerpa_shirt_a,   itm_m_nerpa_coat_of_plates_medium_b, itm_m_gauntlets_a, itm_side_sword, itm_shield_heater_d, itm_nerpa_barbuta_open_padded_b, itm_darts, itm_lance],   knight_attrib_1,wp(130),knight_skills_2, 0x0000000afd00520020db6db6db6dfcff00000000001db6f80000000000000000, swadian_face_young_2],
  ["knight_7_17", "Duke Zac", "Zac", tf_hero, 0, reserved,  fac_kingdom_7, [itm_mt_horse_b3, itm_nerpa_shirt_a,   itm_m_nerpa_coat_of_plates_medium_b, itm_m_gloves_a, itm_grosse_messer_b, itm_shield_heater_d, itm_nerpa_barbuta_a, itm_darts, itm_lance],    knight_attrib_2,wp(190),knight_skills_1|knows_trainer_4, 0x0000000ac40021c620db6db6db6dfcff00000000001db6f80000000000000000, swadian_face_young_2],
  ["knight_7_18", "Duke Hudson", "Hudson", tf_hero, 0, reserved,  fac_kingdom_7, [itm_mt_horse_b3, itm_nerpa_shirt_a,   itm_m_nerpa_coat_of_plates_medium_a, itm_m_gloves_a, itm_crusader_sword, itm_steel_shield, itm_nerpa_barbuta_open_padded_b, itm_lance],   knight_attrib_3,wp(210),knight_skills_1, 0x0000000ac400320a20db6db6db6dfcff00000000001db6f80000000000000000, swadian_face_young_2],
  ["knight_7_19", "Duke Lommas", "Lommas", tf_hero, 0, reserved,  fac_kingdom_7, [itm_mt_horse_b3, itm_nerpa_shirt_a,   itm_m_nerpa_coat_of_plates_medium_a, itm_m_gloves_a, itm_crusader_sword, itm_steel_shield, itm_nerpa_barbuta_b, itm_lance],    knight_attrib_1,wp(120),knight_skills_1, 0x0000000ac400424720db6db6db6dfcff00000000001db6f80000000000000000, swadian_face_young_2],
  ["knight_7_20", "Duke Jazo", "Jazo", tf_hero, 0, reserved,  fac_kingdom_7, [itm_mt_horse_b3, itm_nerpa_shirt_a,   itm_m_nerpa_coat_of_plates_medium_b, itm_m_gauntlets_b, itm_crusader_sword, itm_steel_shield, itm_nerpa_barbuta_open_nasal, itm_lance],   knight_attrib_2,wp(150),knight_skills_1, 0x0000000ac400528820db6db6db6dfcff00000000001db6f80000000000000000, swadian_face_young_2],

  ["knight_8_1", "Chieftain Kael Bloodclaw", "Kael", tf_hero, 0, reserved, fac_kingdom_8, [itm_steppe_horse_d, itm_tabard, itm_eastern_scale_gloves_b, itm_hairako_full_mail_b, itm_hairako_mail_helmet_d, itm_javelin, itm_solarian_lance_a, itm_tab_shield_tauria_b, itm_sarranid_cavalry_sword], knight_attrib_5,wp(250),knight_skills_5, 0x0000000e8008344f36db6db6db6debad00000000001db6fb0000000000000000, rhodok_face_older_2],
  ["knight_8_2", "Chieftain Tatsuya Flameheart", "Tatsuya", tf_hero, 0, reserved, fac_kingdom_8, [itm_steppe_horse_d, itm_tabard, itm_eastern_scale_gloves_a, itm_hairako_full_mail_b, itm_hairako_mail_helmet_a, itm_throwing_spears, itm_solarian_lance_b, itm_tab_shield_tauria_b, itm_arabian_sword_a], knight_attrib_5,wp(250),knight_skills_5, 0x0000000e400401c636db6db6db6db6db00000000001db6db0000000000000000, rhodok_face_older_2],
  ["knight_8_3", "Chieftain Akira Stormcaller", "Akira", tf_hero, 0, reserved, fac_kingdom_8, [itm_steppe_horse_b, itm_tabard,  itm_eastern_scale_gloves_b, itm_hairako_full_mail_b, itm_hairako_mail_helmet_b, itm_javelin, itm_solarian_lance_c, itm_tab_shield_tauria_b, itm_arabian_sword_b], knight_attrib_5,wp(250),knight_skills_5, 0x0000000e7f041386061e69d89b6dbef700000000001dc6f80000000000000000, rhodok_face_older_2],
  ["knight_8_4", "Chieftain Haru Ironhoof", "Haru", tf_hero, 0, reserved, fac_kingdom_8, [itm_steppe_horse_c, itm_tabard, itm_eastern_scale_gloves_b, itm_hairako_full_mail_a, itm_hairako_mail_helmet_d, itm_javelin, itm_solarian_lance_a, itm_tab_shield_tauria_b, itm_arabian_sword_c], knight_attrib_5,wp(250),knight_skills_5, 0x0000000e7f042345061e69d89b6dbef700000000001dc6f80000000000000000, rhodok_face_older_2],
  ["knight_8_5", "Chieftain Takeshi Silentclaw", "Takeshi", tf_hero, 0, reserved, fac_kingdom_8, [itm_steppe_horse, itm_tabard,  itm_eastern_scale_gloves_b, itm_hairako_full_mail_b, itm_hairako_mail_helmet_d, itm_javelin, itm_solarian_lance_b, itm_tab_shield_tauria_b, itm_arabian_sword_c], knight_attrib_5,wp(250),knight_skills_5, 0x0000000e7f0411ca061e69d89b6dbef700000000001dc6f80000000000000000, rhodok_face_older_2],
  ["knight_8_6", "Chieftain Hiro Wildheart", "Hiro", tf_hero, 0, reserved, fac_kingdom_8, [itm_steppe_horse_d, itm_tabard,  itm_eastern_scale_gloves_b, itm_hairako_full_mail_a, itm_hairako_mail_helmet_b, itm_javelin, itm_solarian_lance_a, itm_tab_shield_tauria_b, itm_arabian_sword_c], knight_attrib_5,wp(250),knight_skills_5, 0x0000000e7f0421c9061e69d89b6dbef700000000001dc6f80000000000000000, rhodok_face_older_2],
  ["knight_8_7", "Chieftain Yukio Frostblade", "Yukio", tf_hero, 0, reserved, fac_kingdom_8, [itm_steppe_horse_d, itm_tabard,  itm_eastern_scale_gloves_b, itm_hairako_full_mail_a, itm_hairako_mail_helmet_a, itm_throwing_spears, itm_solarian_lance_c, itm_tab_shield_tauria_b, itm_arabian_sword_d], knight_attrib_5,wp(250),knight_skills_5, 0x0000000e7f042188061e69d89b6dbef700000000001dc6f80000000000000000, rhodok_face_older_2],
  ["knight_8_8", "Chieftain Kenta Stormfury", "Kenta", tf_hero, 0, reserved, fac_kingdom_8, [itm_steppe_horse_b, itm_tabard,  itm_eastern_scale_gloves_a, itm_hairako_full_mail_a, itm_hairako_mail_helmet_d, itm_throwing_spears, itm_solarian_lance_a, itm_tab_shield_tauria_b, itm_arabian_sword_d], knight_attrib_5,wp(250),knight_skills_5, 0x0000000e7f0405c6061e69d89b6dbef700000000001dc6f80000000000000000, rhodok_face_older_2],

  # younger knights
  ["knight_8_9", "Chieftain Ninezzuu", "Ninezzuu", tf_hero, 0, reserved, fac_kingdom_8, [itm_steppe_horse_d, itm_tabard, itm_eastern_scale_gloves_b, itm_hairako_long_coat_scale_d, itm_hairako_mail_helmet_d, itm_javelin, itm_tab_shield_tauria_b, itm_arabian_sword_d],    knight_attrib_3,wp(160),knight_skills_3, 0x0000000e7f046554061e69d89b6dbef700000000001dc6f80000000000000000, swadian_face_old_2],
  ["knight_8_10", "Chieftain Ningusu", "Ningusu", tf_hero, 0, reserved, fac_kingdom_8, [itm_steppe_horse_b, itm_tabard, itm_eastern_scale_gloves_b, itm_hairako_long_coat_scale_a, itm_hairako_mail_helmet_d, itm_javelin, itm_tab_shield_tauria_b, itm_arabian_sword_d],   knight_attrib_3,wp(190),knight_skills_3, 0x0000000e7f045450061e69d89b6dbef700000000001dc6f80000000000000000, swadian_face_older_2],
  ["knight_8_11", "Chieftain Nabu", "Nabu", tf_hero, 0, reserved, fac_kingdom_8, [itm_steppe_horse, itm_tabard, itm_eastern_scale_gloves_b, itm_hairako_long_coat_scale_a, itm_hairako_mail_helmet_d, itm_javelin, itm_tab_shield_tauria_b, itm_arabian_sword_a],       knight_attrib_3,wp(220),knight_skills_3, 0x0000000e7f044448061e69d89b6dbef700000000001dc6f80000000000000000, swadian_face_older_2],
  ["knight_8_12", "Chieftain Ammardum", "Ammardum", tf_hero, 0, reserved, fac_kingdom_8, [itm_steppe_horse_c, itm_tabard, itm_mail_mittens, itm_hairako_long_coat_scale_d, itm_hairako_mail_helmet_d, itm_javelin, itm_tab_shield_tauria_b, itm_arabian_sword_a],    knight_attrib_3,wp(130),knight_skills_3, 0x0000000e7f0443c6061e69d89b6dbef700000000001dc6f80000000000000000, swadian_face_older_2],
  ["knight_8_13", "Chieftain Nina", "Nina", tf_hero, 0, reserved, fac_kingdom_8, [itm_steppe_horse_d, itm_tabard, itm_mail_mittens, itm_hairako_long_coat_scale_a, itm_hairako_nasal_helmet_e, itm_javelin, itm_tab_shield_tauria_b, itm_arabian_sword_a],   knight_attrib_2,wp(160),knight_skills_2, 0x0000000e7f043383061e69d89b6dbef700000000001dc6f80000000000000000, swadian_face_older_2],
  ["knight_8_14", "Chieftain Adarar", "Adarar", tf_hero, 0, reserved, fac_kingdom_8, [itm_steppe_horse_d, itm_tabard, itm_mail_mittens, itm_hairako_long_coat_scale_a, itm_hairako_nasal_helmet_e, itm_javelin, itm_tab_shield_tauria_b, itm_arabian_sword_b],    knight_attrib_2,wp(190),knight_skills_3|knows_trainer_6, 0x0000000e7f042342061e69d89b6dbef700000000001dc6f80000000000000000, swadian_face_older_2],
  ["knight_8_15", "Chieftain Adus", "Adus", tf_hero, 0, reserved, fac_kingdom_8, [itm_steppe_horse, itm_tabard, itm_mail_mittens, itm_hairako_long_coat_scale_a, itm_hairako_nasal_helmet_e, itm_javelin, itm_tab_shield_tauria_b, itm_arabian_sword_b],      knight_attrib_4,wp(140),knight_skills_2, 0x0000000e7f041300061e69d89b6dbef700000000001dc6f80000000000000000, swadian_face_young_2],
  ["knight_8_16", "Chieftain Nezzu", "Nezzu", tf_hero, 0, reserved, fac_kingdom_8, [itm_steppe_horse_d, itm_tabard, itm_mail_mittens, itm_hairako_long_coat_scale_d, itm_hairako_nasal_helmet_e, itm_javelin, itm_tab_shield_tauria_b, itm_arabian_sword_b],   knight_attrib_1,wp(130),knight_skills_2, 0x0000000e630402d4061e69d89b6dbef700000000001dc6f80000000000000000, swadian_face_young_2],
  ["knight_8_17", "Chieftain Nebilu", "Nebilu", tf_hero, 0, reserved, fac_kingdom_8, [itm_steppe_horse, itm_tabard, itm_decorated_leather_gloves_a, itm_hairako_long_coat_scale_b, itm_hairako_nasal_helmet_e, itm_javelin, itm_battle_trident, itm_tab_shield_tauria_b, itm_arabian_sword_b],    knight_attrib_2,wp(190),knight_skills_1|knows_trainer_4, 0x0000000e63046294061e69d89b6dbef700000000001dc6f80000000000000000, swadian_face_young_2],
  ["knight_8_18", "Chieftain Maamuzi", "Maamuzi", tf_hero, 0, reserved, fac_kingdom_8, [itm_steppe_horse_b, itm_tabard, itm_decorated_leather_gloves_a, itm_hairako_long_coat_scale_a, itm_hairako_nasal_helmet_a, itm_battle_trident, itm_tab_shield_tauria_b, itm_arabian_sword_b],   knight_attrib_3,wp(210),knight_skills_1, 0x0000000e63044251061e69d89b6dbef700000000001dc6f80000000000000000, swadian_face_young_2],
  ["knight_8_19", "Chieftain Annikan", "Annikan", tf_hero, 0, reserved, fac_kingdom_8, [itm_steppe_horse_b, itm_tabard, itm_decorated_leather_gloves_a, itm_hairako_long_coat_scale_b, itm_hairako_nasal_helmet_a, itm_battle_trident, itm_tab_shield_tauria_b, itm_arabian_sword_c],    knight_attrib_1,wp(120),knight_skills_1, 0x0000000e630431cb061e69d89b6dbef700000000001dc6f80000000000000000, swadian_face_young_2],
  ["knight_8_20", "Chieftain Milkadea", "Milkadea", tf_hero, 0, reserved, fac_kingdom_8, [itm_steppe_horse, itm_tabard, itm_old_mail_gloves, itm_hairako_long_coat_scale_a, itm_hairako_nasal_helmet_a, itm_battle_trident, itm_tab_shield_tauria_b, itm_arabian_sword_c],   knight_attrib_2,wp(150),knight_skills_1, 0x0000000e7f04228b061e69d89b6dbef700000000001dc6f80000000000000000, swadian_face_young_2],

  ["knight_9_1", "Knight Jamond", "Jamond", tf_hero, 0, reserved, fac_kingdom_9,[ itm_rich_outfit,  itm_m_tauria_brigandine_b, itm_m_gauntlets_a, itm_m_munitions_helm_a, itm_mt_horse_b, itm_great_lance, itm_tab_shield_tauria_c, itm_crusader_sword],knight_attrib_5,wp(350),knight_skills_5|knows_trainer_5|knows_ironflesh_10|knows_riding_10, 0x000000018004054626db6db6db6dbeff00000000001db6eb0000000000000000,swadian_face_older_2],
  ["knight_9_2", "Knight Wearda", "Wearda", tf_hero, 0, reserved, fac_kingdom_9,[ itm_short_tunic,  itm_m_tauria_brigandine_a, itm_m_gauntlets_a, itm_m_munitions_helm_b, itm_mt_horse_b, itm_great_lance, itm_tab_shield_tauria_c, itm_crusader_sword],knight_attrib_5,wp(350),knight_skills_5|knows_trainer_5|knows_ironflesh_10|knows_riding_10, 0x000000018004150526db6db6db6dbeff00000000001db6e30000000000000000,swadian_face_older_2],
  ["knight_9_3", "Knight Wealdther", "Wealdther", tf_hero, 0, reserved, fac_kingdom_9,[ itm_short_tunic,  itm_m_tauria_brigandine_b, itm_m_gauntlets_b, itm_m_pepperpot_d, itm_mt_horse_b2, itm_great_lance, itm_tab_shield_tauria_c, itm_crusader_sword],knight_attrib_5,wp(350),knight_skills_5|knows_trainer_5|knows_ironflesh_10|knows_riding_10, 0x000000018004058426db6db6db6dbeff00000000001db6e30000000000000000,swadian_face_older_2],
  ["knight_9_4", "Knight Eallan", "Eallan", tf_hero, 0, reserved, fac_kingdom_9,[ itm_short_tunic,  itm_m_tauria_brigandine_a, itm_m_gauntlets_a, itm_m_munitions_helm_a, itm_mt_horse_b2, itm_great_lance, itm_tab_shield_tauria_c, itm_morningstar],knight_attrib_5,wp(350),knight_skills_5|knows_trainer_5|knows_ironflesh_10|knows_riding_10, 0x000000018004249426db6db6db6dbeff00000000001db6e30000000000000000,swadian_face_older_2],
  ["knight_9_5", "Knight Ichohn", "Ichohn", tf_hero, 0, reserved, fac_kingdom_9,[ itm_short_tunic,  itm_m_tauria_brigandine_a, itm_m_gauntlets_a, itm_m_munitions_helm_b, itm_mt_horse_b2, itm_great_lance, itm_tab_shield_tauria_c, itm_crusader_sword],knight_attrib_5,wp(350),knight_skills_5|knows_trainer_5|knows_ironflesh_10|knows_riding_10, 0x000000018004245226db6db6db6dbeff00000000001db6e30000000000000000,swadian_face_older_2],
  ["knight_9_6", "Knight Hony Pycey", "Hony Pycey", tf_hero, 0, reserved, fac_kingdom_9,[ itm_rich_outfit,  itm_m_tauria_brigandine_a, itm_m_gloves_a, itm_m_munitions_helm_b, itm_mt_horse_b, itm_great_lance, itm_tab_shield_tauria_c, itm_crusader_sword],knight_attrib_5,wp(350),knight_skills_5|knows_trainer_5|knows_ironflesh_10|knows_riding_10, 0x000000018004041026db6db6db6dbeff00000000001db6e30000000000000000,swadian_face_older_2],
  ["knight_9_7", "Knight Behrtio", "Behrtio", tf_hero, 0, reserved, fac_kingdom_9,[ itm_rich_outfit,  itm_m_tauria_plate_mail_b, itm_m_gauntlets_a, itm_m_munitions_helm_a, itm_mt_horse_b, itm_great_lance, itm_tab_shield_tauria_c, itm_crusader_sword],knight_attrib_5,wp(350),knight_skills_5|knows_trainer_5|knows_ironflesh_10|knows_riding_10, 0x00000001800405c526db6db6db6dbeff00000000001db6e30000000000000000,swadian_face_older_2],
  ["knight_9_8", "Knight Ulfrith", "Ulfrith", tf_hero, 0, reserved, fac_kingdom_9,[ itm_short_tunic,  itm_m_tauria_plate_mail_b, itm_old_mail_gloves, itm_m_pepperpot_d, itm_mt_horse_b, itm_great_lance, itm_tab_shield_tauria_c, itm_crusader_sword],knight_attrib_5,wp(350),knight_skills_5|knows_trainer_5|knows_ironflesh_10|knows_riding_10, 0x000000018004114426db6db6db6dbeff00000000001db6e30000000000000000,swadian_face_older_2],

  # younger knights
  ["knight_9_9", "Knight Debeorht", "Debeorht", tf_hero, 0, reserved, fac_kingdom_9, [ itm_short_tunic,  itm_m_tauria_vest_heavy_b, itm_m_gloves_a, itm_m_pepperpot_a, itm_mt_horse_b, itm_guisarme, itm_tab_shield_tauria_b, itm_military_pick],    knight_attrib_3,wp(160),knight_skills_3, 0x000000018004218526db6db6db6dbeff00000000001db6e30000000000000000, swadian_face_old_2],
  ["knight_9_10", "Knight Eorcald", "Eorcald", tf_hero, 0, reserved, fac_kingdom_9, [ itm_short_tunic,  itm_m_tauria_vest_heavy_b, itm_m_gauntlets_b, itm_m_pepperpot_d, itm_mt_horse_b, itm_great_lance, itm_tab_shield_tauria_b, itm_crusader_sword],   knight_attrib_3,wp(190),knight_skills_3, 0x000000018004128526db6db6db6dbeff00000000001db6e30000000000000000, swadian_face_older_2],
  ["knight_9_11", "Knight Robern Quinte", "Robern Quinte", tf_hero, 0, reserved, fac_kingdom_9, [ itm_short_tunic,  itm_m_tauria_vest_heavy_b, itm_m_gauntlets_b, itm_m_pepperpot_c, itm_mt_horse_b, itm_great_lance, itm_tab_shield_tauria_b, itm_military_pick],       knight_attrib_3,wp(220),knight_skills_3, 0x00000001800402d426db6db6db6dbeff00000000001db6e30000000000000000, swadian_face_older_2],
  ["knight_9_12", "Knight Jamart", "Jamart", tf_hero, 0, reserved, fac_kingdom_9, [ itm_short_tunic,  itm_m_tauria_plate_mail_b, itm_old_mail_gloves, itm_mt_horse_b, itm_great_lance, itm_tab_shield_tauria_b, itm_military_pick],       knight_attrib_3,wp(220),knight_skills_3, 0x000000018004014826db6db6db6dbeff00000000001db6e30000000000000000, swadian_face_older_2],
  ["knight_9_13", "Knight Chury", "Chury", tf_hero, 0, reserved, fac_kingdom_9, [ itm_short_tunic,  itm_m_tauria_vest_heavy_a, itm_old_mail_gloves, itm_m_pepperpot_c, itm_mt_horse_b, itm_great_lance, itm_tab_shield_tauria_b, itm_military_pick],       knight_attrib_3,wp(220),knight_skills_3, 0x000000018004210526db6db6db6dbeff00000000001db6e30000000000000000, swadian_face_older_2],
  ["knight_9_14", "Knight Aered", "Aered", tf_hero, 0, reserved, fac_kingdom_9, [ itm_short_tunic,  itm_m_tauria_vest_heavy_a, itm_old_mail_gloves, itm_m_pepperpot_c, itm_mt_horse_b, itm_great_lance, itm_tab_shield_tauria_b, itm_military_pick],       knight_attrib_3,wp(220),knight_skills_3, 0x00000001800410c426db6db6db6dbeff00000000001db6e30000000000000000, swadian_face_older_2],
  ["knight_9_15", "Knight Wige", "Wige", tf_hero, 0, reserved, fac_kingdom_9, [ itm_short_tunic,  itm_m_tauria_plate_mail_b, itm_old_mail_gloves, itm_m_pepperpot_b, itm_mt_horse_b, itm_great_lance, itm_tab_shield_tauria_b, itm_crusader_sword],       knight_attrib_3,wp(220),knight_skills_3, 0x000000018004009426db6db6db6dbeff00000000001db6e30000000000000000, swadian_face_older_2],
  ["knight_9_16", "Knight Wine", "Wine", tf_hero, 0, reserved, fac_kingdom_9, [ itm_short_tunic, itm_m_tauria_vest_heavy_b, itm_m_gloves_a, itm_m_pepperpot_c, itm_mt_horse_b, itm_great_lance, itm_tab_shield_tauria_b, itm_crusader_sword],       knight_attrib_3,wp(220),knight_skills_3, 0x000000018004205426db6db6db6dbeff00000000001db6e30000000000000000, swadian_face_older_2],
  ["knight_9_17", "Knight Freward", "Freward", tf_hero, 0, reserved, fac_kingdom_9, [ itm_short_tunic, itm_m_tauria_plate_mail_b, itm_old_mail_gloves, itm_mail_coif, itm_mt_horse_b, itm_great_lance, itm_tab_shield_tauria_a, itm_crusader_sword],       knight_attrib_3,wp(220),knight_skills_3, 0x000000018004000626db6db6db6dbeff00000000001db6e30000000000000000, swadian_face_older_2],
  ["knight_9_18", "Knight Ceolfre", "Ceolfre", tf_hero, 0, reserved, fac_kingdom_9, [ itm_short_tunic, itm_m_tauria_vest_heavy_b, itm_old_mail_gloves, itm_mail_coif, itm_mt_horse_b, itm_great_lance, itm_tab_shield_tauria_a, itm_crusader_sword],       knight_attrib_3,wp(220),knight_skills_3, 0x000000018004100526db6db6db6dbeff00000000001db6e30000000000000000, swadian_face_older_2],
  ["knight_9_19", "Knight Afod", "Afod", tf_hero, 0, reserved, fac_kingdom_9, [ itm_rich_outfit,  itm_m_tauria_plate_mail_b, itm_old_mail_gloves, itm_mail_coif, itm_mt_horse_b, itm_great_lance, itm_tab_shield_tauria_a, itm_crusader_sword],       knight_attrib_3,wp(220),knight_skills_3, 0x00000001800425c526db6db6db6dbeff00000000001db6e30000000000000000, swadian_face_older_2],
  ["knight_9_20", "Knight Aethelm", "Aethelm", tf_hero, 0, reserved, fac_kingdom_9, [ itm_rich_outfit,  itm_m_tauria_vest_heavy_b, itm_old_mail_gloves, itm_m_pepperpot_c, itm_mt_horse_b, itm_great_lance, itm_tab_shield_tauria_a, itm_crusader_sword],       knight_attrib_3,wp(220),knight_skills_3, 0x00000001800404c626db6db6db6dbeff00000000001db6e30000000000000000, swadian_face_older_2],

  ["knight_10_1", "Noble Egnor", "Egnor", tf_hero, 0, reserved, fac_kingdom_10,[ itm_tabard,  itm_m_elen_plated_leather_b, itm_m_gauntlets_b, itm_elen_great_helm_b, itm_warhorse, itm_k_long_sword_c, itm_danish_greatsword],knight_attrib_5,wp(350),knight_skills_5|knows_trainer_5|knows_ironflesh_10|knows_riding_10, 0x00000001aa10420721036db6d36e5efe00000000001db6f80000000000000000,swadian_face_older_2],
  ["knight_10_2", "Noble Golure", "Golure", tf_hero, 0, reserved, fac_kingdom_10,[ itm_tabard,  itm_m_elen_plated_leather_b, itm_m_gauntlets_b, itm_elen_great_helm_a, itm_warhorse, itm_tab_shield_tauria_b, itm_k_long_sword_a, itm_danish_greatsword],knight_attrib_5,wp(350),knight_skills_5|knows_trainer_5|knows_ironflesh_10|knows_riding_10, 0x00000001aa10624821036db6d36e5efe00000000001db6f80000000000000000,swadian_face_older_2],
  ["knight_10_3", "Noble Finasaer", "Finasaer", tf_hero, 0, reserved, fac_kingdom_10,[ itm_tabard,  itm_m_elen_plated_leather_a, itm_m_gauntlets_b, itm_elen_nasal_mail_c, itm_warhorse, itm_tab_shield_tauria_b, itm_k_long_sword_c, itm_glaive_a],knight_attrib_5,wp(350),knight_skills_5|knows_trainer_5|knows_ironflesh_10|knows_riding_10, 0x00000001bf10128821036db6d36e5efe00000000001db6f80000000000000000,swadian_face_older_2],
  ["knight_10_4", "Noble Mahtata", "Mahtata", tf_hero, 0, reserved, fac_kingdom_10,[ itm_tabard,  itm_m_elen_plated_leather_b, itm_m_gauntlets_b, itm_elen_nasal_mail_c, itm_warhorse, itm_k_long_sword_b, itm_danish_greatsword],knight_attrib_5,wp(350),knight_skills_5|knows_trainer_5|knows_ironflesh_10|knows_riding_10, 0x00000001bf1022c921036db6d36e5efe00000000001db6f80000000000000000,swadian_face_older_2],
  ["knight_10_5", "Noble Alatad", "Alatad", tf_hero, 0, reserved, fac_kingdom_10,[ itm_tabard,  itm_m_elen_plated_leather_b, itm_m_gauntlets_b, itm_elen_nasal_mail_b, itm_warhorse, itm_tab_shield_tauria_b, itm_k_long_sword_b, itm_danish_greatsword],knight_attrib_5,wp(350),knight_skills_5|knows_trainer_5|knows_ironflesh_10|knows_riding_10, 0x00000001bf10334a21036db6d36e5efe00000000001db6f80000000000000000,swadian_face_older_2],
  ["knight_10_6", "Noble Galinor", "Galinor", tf_hero, 0, reserved, fac_kingdom_10,[ itm_tabard,  itm_m_elen_plated_leather_a, itm_m_gauntlets_b, itm_elen_nasal_mail_b, itm_warhorse, itm_crusader_long_sword_c, itm_glaive_a],knight_attrib_5,wp(350),knight_skills_5|knows_trainer_5|knows_ironflesh_10|knows_riding_10, 0x00000001bf10419121036db6d36e5efe00000000001db6f80000000000000000,swadian_face_older_2],
  ["knight_10_7", "Noble Elelroth", "Elelroth", tf_hero, 0, reserved, fac_kingdom_10,[ itm_tabard, itm_m_elen_plated_leather_a, itm_m_gauntlets_b, itm_elen_nasal_mail_b, itm_warhorse, itm_crusader_long_sword_b, itm_glaive_a],knight_attrib_5,wp(350),knight_skills_5|knows_trainer_5|knows_ironflesh_10|knows_riding_10, 0x00000001bf1061d421036db6d36e5efe00000000001db6f80000000000000000,swadian_face_older_2],
  ["knight_10_8", "Noble Eliolad", "Eliolad", tf_hero, 0, reserved, fac_kingdom_10,[ itm_tabard, itm_m_elen_plated_leather_a, itm_m_gauntlets_b, itm_elen_nasal_mail_b, itm_warhorse, itm_crusader_long_sword_c, itm_glaive_a],knight_attrib_5,wp(350),knight_skills_5|knows_trainer_5|knows_ironflesh_10|knows_riding_10, 0x00000001bf10121421036db6d36e5efe00000000001db6f80000000000000000,swadian_face_older_2],

  # younger knights
  ["knight_10_9", "Noble Olar", "Olar", tf_hero, 0, reserved, fac_kingdom_10, [ itm_tabard, itm_m_elen_lamellar_d, itm_m_gauntlets_b, itm_elen_nasal_mail_a, itm_crusader_long_sword_a, itm_danish_greatsword],    knight_attrib_3,wp(160),knight_skills_3, 0x00000001bf10228121036db6d36e5efe00000000001db6f80000000000000000, swadian_face_old_2],
  ["knight_10_10", "Noble Elelrol", "Elelrol", tf_hero, 0, reserved, fac_kingdom_10, [ itm_tabard,  itm_m_elen_lamellar_a, itm_m_gauntlets_b, itm_elen_nasal_mail_a, itm_tab_shield_tauria_b, itm_crusader_long_sword_b, itm_glaive_b],   knight_attrib_3,wp(190),knight_skills_3, 0x00000001bf10331421036db6d36e5efe00000000001db6f80000000000000000, swadian_face_older_2],
  ["knight_10_11", "Noble Legali", "Legali", tf_hero, 0, reserved, fac_kingdom_10, [ itm_tabard,  itm_m_elen_lamellar_b, itm_m_gauntlets_b, itm_elen_nasal_mail_a, itm_warhorse, itm_tab_shield_tauria_b, itm_crusader_long_sword_b, itm_glaive_b],       knight_attrib_3,wp(220),knight_skills_3, 0x00000001801065c421036db6d36e5efe00000000001db6f80000000000000000, swadian_face_older_2],
  ["knight_10_12", "Noble Finrethel", "Finrethel", tf_hero, 0, reserved, fac_kingdom_10, [ itm_tabard,  itm_m_elen_lamellar_c, itm_m_gauntlets_b, itm_elen_nasal_mail_a, itm_warhorse, itm_crusader_long_sword_a, itm_glaive_b],       knight_attrib_3,wp(220),knight_skills_3, 0x000000018010010621036db6d36e5efe00000000001db6f80000000000000000, swadian_face_older_2],
  ["knight_10_13", "Noble Eros", "Eros", tf_hero, 0, reserved, fac_kingdom_10, [ itm_tabard, itm_m_elen_lamellar_c, itm_m_gauntlets_b, itm_elen_nasal_mail_a, itm_warhorse, itm_crusader_long_sword_b, itm_glaive_b],       knight_attrib_3,wp(220),knight_skills_3, 0x00000001801001c721036db6d36e5efe00000000001db6f80000000000000000, swadian_face_older_2],
  ["knight_10_14", "Noble Lathonel", "Lathonel", tf_hero, 0, reserved, fac_kingdom_10, [ itm_tabard, itm_m_elen_lamellar_c, itm_m_gauntlets_b, itm_elen_nasal_padded_b, itm_tab_shield_tauria_c, itm_winged_mace, itm_glaive_b],       knight_attrib_3,wp(220),knight_skills_3, 0x000000018010228721036db6d36e5efe00000000001db6f80000000000000000, swadian_face_older_2],
  ["knight_10_15", "Noble Elror", "Elror", tf_hero, 0, reserved, fac_kingdom_10, [ itm_tabard, itm_m_elen_lamellar_c, itm_m_gauntlets_b, itm_elen_nasal_padded_b, itm_tab_shield_tauria_c, itm_royal_winged_mace_decorated, itm_danish_greatsword],       knight_attrib_3,wp(220),knight_skills_3, 0x000000018010128821036db6d36e5efe00000000001db6f80000000000000000, swadian_face_older_2],
  ["knight_10_16", "Noble Elethol", "Elethol", tf_hero, 0, reserved, fac_kingdom_10, [ itm_tabard, itm_m_elen_lamellar_b, itm_m_gauntlets_b, itm_elen_nasal_padded_b, itm_royal_winged_mace_decorated, itm_danish_greatsword],       knight_attrib_3,wp(220),knight_skills_3, 0x000000018010724921036db6d36e5efe00000000001db6f80000000000000000, swadian_face_older_2],
  ["knight_10_17", "Noble Galebre", "Galebre", tf_hero, 0, reserved, fac_kingdom_10, [ itm_tabard, itm_m_elen_lamellar_b, itm_m_gauntlets_b, itm_elen_nasal_padded_b, itm_warhorse, itm_royal_winged_mace_decorated, itm_danish_greatsword],       knight_attrib_3,wp(220),knight_skills_3, 0x0000000b8010414521036db6d36e5efe00000000001cd6f80000000000000000, swadian_face_older_2],
  ["knight_10_18", "Noble Goneli", "Goneli", tf_hero, 0, reserved, fac_kingdom_10, [ itm_tabard,  itm_m_elen_lamellar_a, itm_m_gloves_a, itm_elen_nasal_padded_b, itm_royal_winged_mace_decorated, itm_war_bow, itm_barbed_arrows],       knight_attrib_3,wp(220),knight_skills_3|knows_power_draw_8|knows_athletics_10, 0x00000001801031c521036db6d36e5efe00000000001db6f80000000000000000, swadian_face_older_2],
  ["knight_10_19", "Noble Alanwel", "Alanwel", tf_hero, 0, reserved, fac_kingdom_10, [ itm_tabard,  itm_m_elen_lamellar_c, itm_m_gloves_a, itm_elen_nasal_padded_a, itm_strange_winged_mace_decorated, itm_war_bow, itm_bodkin_arrows],       knight_attrib_3,wp(220),knight_skills_3|knows_power_draw_8|knows_athletics_10, 0x0000000b8010318421036db6d36e5efe00000000001db6f80000000000000000, swadian_face_older_2],
  ["knight_10_20", "Noble Diredior", "Diredior", tf_hero, 0, reserved, fac_kingdom_10, [ itm_tabard,  itm_m_elen_lamellar_a, itm_m_gloves_a, itm_elen_nasal_padded_a, itm_strange_winged_mace, itm_war_bow, itm_arrows],       knight_attrib_3,wp(220),knight_skills_3|knows_power_draw_8|knows_athletics_10, 0x000000018010720621036db6d36e5efe00000000001db6f80000000000000000, swadian_face_older_2],

  # Adid knights
  ["knight_11_1", "Vizier Malik ibn Rahim", "Malik", tf_hero, 0, reserved, fac_kingdom_11, [ itm_shirt, itm_arabian_horse_a, itm_mkk_mamluke_a, itm_eastern_scale_gloves_a, itm_adid_elite_helmet_a, itm_scimitar_b, itm_eastern_round_shield_a], knight_attrib_5,wp(250),knight_skills_5, 0x0000000e8004615436db6dd79f6df92f00000000001db6eb0000000000000000, rhodok_face_older_2],
  ["knight_11_2", "Vizier Khalid al-Qadir", "Khalid", tf_hero, 0, reserved, fac_kingdom_11, [ itm_shirt, itm_arabian_horse_b, itm_mkk_mamluke_b, itm_eastern_scale_gloves_a, itm_adid_elite_helmet_a, itm_scimitar_b, itm_eastern_round_shield_b], knight_attrib_5,wp(250),knight_skills_5, 0x0000000dff0471d314db6dd79f6df92f00000000001db6f80000000000000000, rhodok_face_older_2],
  ["knight_11_3", "Vizier Tariq ibn Ziyad", "Tariq", tf_hero, 0, reserved, fac_kingdom_11, [ itm_shirt, itm_arabian_horse_c, itm_mkk_black_scale_a, itm_eastern_scale_gloves_b, itm_adid_cavalry_helmet_a, itm_scimitar_b, itm_eastern_round_shield_b, itm_strong_bow, itm_barbed_arrows], knight_attrib_5,wp(250),knight_skills_5, 0x0000000da104728d34dba1d79f7dffff00000000001db73c0000000000000000, rhodok_face_older_2],
  ["knight_11_4", "Vizier Zahir ibn al-Hakam", "Zahir", tf_hero, 0, reserved, fac_kingdom_11, [ itm_shirt, itm_arabian_horse_b, itm_mkk_mamluke_c, itm_eastern_scale_gloves_a, itm_adid_cavalry_helmet_a, itm_lance, itm_eastern_round_shield_a, itm_scimitar_b], knight_attrib_5,wp(250),knight_skills_5, 0x0000000d8004634534db6daf9f6dfdb600000000001e493c0000000000000000, rhodok_face_older_2],
  ["knight_11_5", "Vizier Faris al-Jabbar", "Faris", tf_hero, 0, reserved, fac_kingdom_11, [ itm_shirt, itm_arabian_horse_a, itm_mkk_mamluke_a, itm_eastern_scale_gloves_a, itm_adid_cavalry_helmet_a, itm_sarranid_mace_1, itm_eastern_round_shield_c, itm_hunting_crossbow, itm_steel_bolts], knight_attrib_5,wp(250),knight_skills_5, 0x0000000dff04644934db6dab176dff7f00000000001e4b3c0000000000000000, rhodok_face_older_2],
  ["knight_11_6", "Vizier Ud'in ibn Laa'ni al-Mee", "Ud'in", tf_hero, 0, reserved, fac_kingdom_11, [ itm_shirt, itm_arabian_horse_a, itm_mkk_mamluke_a, itm_eastern_scale_gloves_a, itm_adid_cavalry_helmet_a, itm_sarranid_mace_1, itm_eastern_round_shield_c, itm_hunting_crossbow, itm_steel_bolts], knight_attrib_5,wp(250),knight_skills_5, 0x0000000f4700229336db6db6db6dfcf700000000001db6fb0000000000000000, rhodok_face_older_2],
  ["knight_11_7", "Vizier Ullah al-Ad", "Ullah", tf_hero, 0, reserved, fac_kingdom_11, [ itm_shirt, itm_arabian_horse_a, itm_mkk_black_scale_a, itm_eastern_scale_gloves_a, itm_adid_cavalry_helmet_a, itm_sarranid_mace_1, itm_eastern_round_shield_c, itm_hunting_crossbow, itm_steel_bolts], knight_attrib_5,wp(250),knight_skills_5, 0x000000003f00228936db6db6db6dfcf700000000001db6fb0000000000000000, rhodok_face_older_2],
  ["knight_11_8", "Vizier Zuha ibn Feeqah al-Matrai", "Zuha", tf_hero, 0, reserved, fac_kingdom_11, [ itm_shirt, itm_arabian_horse_b, itm_mkk_black_scale_a, itm_eastern_scale_gloves_b, itm_adid_cavalry_helmet_a, itm_sarranid_mace_1, itm_eastern_round_shield_c, itm_hunting_crossbow, itm_steel_bolts], knight_attrib_5,wp(250),knight_skills_5, 0x000000003f0072c736db6db6db6dfcf700000000001db6fb0000000000000000, rhodok_face_older_2],

  ["knight_11_9", "Vizier Baha ibn Samee al-Fi", "Baha", tf_hero, 0, reserved, fac_kingdom_11, [ itm_shirt, itm_arabian_horse_b, itm_mkk_black_scale_a, itm_eastern_scale_gloves_b, itm_adid_helmet_a, itm_sarranid_mace_1, itm_tab_shield_tauria_a, itm_hunting_crossbow, itm_steel_bolts], knight_attrib_5,wp(250),knight_skills_5, 0x000000003f00735436db6db6db6dfcf700000000001db6fb0000000000000000, rhodok_face_older_2],
  ["knight_11_10", "Vizier Awad al-Habaii", "Awad", tf_hero, 0, reserved, fac_kingdom_11, [ itm_shirt, itm_arabian_horse_b, itm_mkk_black_scale_b, itm_eastern_scale_gloves_b, itm_adid_helmet_a, itm_sarranid_mace_1, itm_tab_shield_tauria_a, itm_hunting_crossbow, itm_steel_bolts], knight_attrib_5,wp(250),knight_skills_5, 0x000000003f00628836db6db6db6dfcf700000000001db6fb0000000000000000, rhodok_face_older_2],
  ["knight_11_11", "Vizier Abu Samee Waha al-Ha", "Abu", tf_hero, 0, reserved, fac_kingdom_11, [ itm_shirt, itm_arabian_horse_c, itm_mkk_black_scale_b, itm_mail_mittens, itm_adid_helmet_a, itm_sarranid_mace_1, itm_tab_shield_tauria_a, itm_hunting_crossbow, itm_steel_bolts], knight_attrib_5,wp(250),knight_skills_5, 0x000000003f00728636db6db6db6dfcf700000000001db6fb0000000000000000, rhodok_face_older_2],
  ["knight_11_12", "Vizier Sa'khiy ibn Waha al-Sirai", "Sa'khiy", tf_hero, 0, reserved, fac_kingdom_11, [ itm_shirt, itm_arabian_horse_c, itm_mkk_black_scale_b, itm_mail_mittens, itm_adid_helmet_b, itm_sarranid_mace_1, itm_tab_shield_tauria_a, itm_hunting_crossbow, itm_steel_bolts], knight_attrib_5,wp(250),knight_skills_5, 0x000000003f00730336db6db6db6dfcf700000000001db6fb0000000000000000, rhodok_face_older_2],
  ["knight_11_13", "Vizier Abu Sa'qud Ma'ul al-Sa", "Abu Sa'qud", tf_hero, 0, reserved, fac_kingdom_11, [ itm_shirt, itm_arabian_horse_c, itm_mkk_black_scale_b, itm_mail_mittens, itm_adid_helmet_b, itm_sarranid_mace_1, itm_tab_shield_tauria_a, itm_hunting_crossbow, itm_steel_bolts], knight_attrib_5,wp(250),knight_skills_5, 0x000000003f00428020db6db6db6dfcf700000000001ed4b80000000000000000, rhodok_face_older_2],
  ["knight_11_14", "Vizier Zaafi ibn Dee'sa al-Taa", "Zaafi", tf_hero, 0, reserved, fac_kingdom_11, [ itm_shirt, itm_arabian_horse_c, itm_mkk_black_scale_c, itm_old_mail_gloves, itm_adid_helmet_b, itm_sarranid_axe_a, itm_tab_shield_tauria_a, itm_hunting_crossbow, itm_steel_bolts], knight_attrib_5,wp(250),knight_skills_5, 0x000000003f00314f21c0edb6dbfdffff00000000001ff1380000000000000000, rhodok_face_older_2],
  ["knight_11_15", "Vizier Idreed ibn Ni'taa al-Sa", "Idreed", tf_hero, 0, reserved, fac_kingdom_11, [ itm_shirt, itm_arabian_horse_a, itm_mkk_black_scale_a, itm_old_mail_gloves, itm_adid_helmet_c, itm_sarranid_axe_a, itm_tab_shield_tauria_a, itm_hunting_crossbow, itm_steel_bolts], knight_attrib_5,wp(250),knight_skills_5, 0x000000003f00619436db6db6db6dfcf700000000001db6fb0000000000000000, rhodok_face_older_2],
  ["knight_11_16", "Vizier Muni ibn Jaaha al-Majmii", "Muni", tf_hero, 0, reserved, fac_kingdom_11, [ itm_shirt, itm_arabian_horse_a, itm_mkk_black_scale_a, itm_old_mail_gloves, itm_adid_helmet_c, itm_sarranid_axe_a, itm_tab_shield_tauria_a, itm_hunting_crossbow, itm_steel_bolts], knight_attrib_5,wp(250),knight_skills_5, 0x000000003f00324020db6db6db6dfcf700000000001ed4b80000000000000000, rhodok_face_older_2],
  ["knight_11_17", "Vizier Wiya'ni ibn Ullan al-Ni", "Wiya'ni", tf_hero, 0, reserved, fac_kingdom_11, [ itm_shirt, itm_arabian_horse_a, itm_mkk_black_scale_a, itm_old_mail_gloves, itm_adid_helmet_c, itm_sarranid_mace_1, itm_tab_shield_tauria_a, itm_hunting_crossbow, itm_steel_bolts], knight_attrib_5,wp(250),knight_skills_5, 0x000000003f0071cb20db6db6db6dfcf700000000001ed4b80000000000000000, rhodok_face_older_2],
  ["knight_11_18", "Vizier Sa'qib ibn Sa'on al-Jubii", "Sa'qib", tf_hero, 0, reserved, fac_kingdom_11, [ itm_shirt, itm_arabian_horse_a, itm_m_desert_bandit_b, itm_decorated_leather_gloves_a, itm_adid_helmet_a, itm_sarranid_mace_1, itm_tab_shield_tauria_a, itm_hunting_crossbow, itm_steel_bolts], knight_attrib_5,wp(250),knight_skills_5, 0x000000003f00628936db6db6db6dfcf700000000001db6fb0000000000000000, rhodok_face_older_2],
  ["knight_11_19", "Vizier Faary ibn Mee'id al-Sa", "Faary", tf_hero, 0, reserved, fac_kingdom_11, [ itm_shirt, itm_arabian_horse_b, itm_m_desert_bandit_c, itm_decorated_leather_gloves_a, itm_adid_helmet_c, itm_sarranid_axe_b, itm_tab_shield_tauria_a, itm_hunting_crossbow, itm_steel_bolts], knight_attrib_5,wp(250),knight_skills_5, 0x000000003f00718a36db6db6db6dfcf700000000001db6fb0000000000000000, rhodok_face_older_2],
  ["knight_11_20", "Vizier Ry'sa al-Anuti", "Ry'sa", tf_hero, 0, reserved, fac_kingdom_11, [ itm_shirt, itm_arabian_horse_b, itm_m_desert_bandit_b, itm_decorated_leather_gloves_a, itm_adid_helmet_b, itm_sarranid_axe_b, itm_tab_shield_tauria_a, itm_hunting_crossbow, itm_steel_bolts], knight_attrib_5,wp(250),knight_skills_5, 0x000000003f0061c736db6db6db6dfcf700000000001db6fb0000000000000000, rhodok_face_older_2],

  # Stormguard Knights
  ["knight_12_1", "Lord Alistair Stormrider", "Alistair", tf_hero, 0, reserved, fac_kingdom_12, [itm_black_knight_horse_a, itm_nobleman_outfit,   itm_m_gauntlets_a, itm_coat_of_plates_v3, itm_m_knigh_helm_d, itm_sword_of_war, itm_tab_shield_tauria_b, itm_grosse_messer_b], knight_attrib_5,wp(250),knight_skills_5, 0x0000000dbf04500636db6db71b4dff3f00000000001db6f30000000000000000, rhodok_face_older_2],
  ["knight_12_2", "Lady Seraphina Windwhisper", "Seraphina", tf_hero|tf_female, 0, reserved, fac_kingdom_12, [itm_black_knight_horse_a, itm_nobleman_outfit,   itm_coat_of_plates_v3, itm_m_gloves_a, itm_light_lance, itm_tab_shield_tauria_b, itm_german_bastard_sword, itm_m_knigh_helm_d, itm_throwing_daggers], knight_attrib_5,wp(250),knight_skills_5, 0x0000000ec004000736db6db6db6db6db00000000001db6db0000000000000000, rhodok_face_older_2],
  ["knight_12_3", "Lord Cedric Stoneheart", "Cedric", tf_hero, 0, reserved, fac_kingdom_12, [itm_black_knight_horse_a, itm_nobleman_outfit,   itm_black_armor, itm_m_gauntlets_a, itm_m_knigh_helm_d], knight_attrib_5,wp(250),knight_skills_5|knows_ironflesh_10|knows_power_strike_10, 0x0000000fff04228920c67127686fff3f00000000001dc9380000000000000000, rhodok_face_older_2],
  ["knight_12_2", "Lady Elara Stormsong", "Elara", tf_hero|tf_female, 0, reserved, fac_kingdom_12, [itm_black_knight_horse_a, itm_nobleman_outfit,   itm_m_gloves_a, itm_black_armor, itm_double_sided_lance, itm_bascinet, itm_throwing_daggers], knight_attrib_5,wp(250),knight_skills_5, 0x0000000ec004000736db6db6db6db6db00000000001db6db0000000000000000, rhodok_face_older_2],
  ["knight_12_5", "Lord Gareth Ironhand", "Gareth", tf_hero, 0, reserved, fac_kingdom_12, [itm_hunter, itm_nobleman_outfit,   itm_black_armor, itm_m_gloves_a, itm_sword_of_war, itm_tab_shield_tauria_b, itm_light_lance, itm_bascinet], knight_attrib_5,wp(250),knight_skills_5, 0x0000000aff0844c630db6db6db0dcfff00000000001db6fb0000000000000000, rhodok_face_older_2],
  ["knight_12_6", "Lord Tasco", "Tasco", tf_hero, 0, reserved, fac_kingdom_12, [itm_hunter, itm_nobleman_outfit,   itm_black_armor, itm_m_gloves_a, itm_sword_of_war, itm_tab_shield_tauria_b, itm_light_lance, itm_bascinet], knight_attrib_5,wp(250),knight_skills_5, 0x00000000350801c13a9292b75aaeff3f00000000001e46f60000000000000000, rhodok_face_older_2],
  ["knight_12_7", "Lord Muirue", "Muirue", tf_hero, 0, reserved, fac_kingdom_12, [itm_hunter, itm_nobleman_outfit,   itm_black_armor, itm_m_gloves_a, itm_sword_of_war, itm_tab_shield_tauria_b, itm_light_lance, itm_bascinet], knight_attrib_5,wp(250),knight_skills_5, 0x000000002700200618848998a361febf00000000001e3ef90000000000000000, rhodok_face_older_2],
  ["knight_12_8", "Lord Aniod", "Aniod", tf_hero, 0, reserved, fac_kingdom_12, [itm_hunter, itm_nobleman_outfit,  itm_black_armor, itm_m_gloves_a, itm_sword_of_war, itm_tab_shield_tauria_b, itm_light_lance, itm_bascinet], knight_attrib_5,wp(250),knight_skills_5, 0x00000000331002d1613cb2965b2d7f3f00000000001da77c0000000000000000, rhodok_face_older_2],

  ["knight_12_9", "Lord Vorti", "Vorti", tf_hero, 0, reserved, fac_kingdom_12, [itm_hunter_f, itm_nobleman_outfit,  itm_coat_of_plates, itm_m_gloves_a, itm_sword_of_war, itm_tab_shield_tauria_b, itm_light_lance, itm_bascinet], knight_attrib_5,wp(250),knight_skills_5, 0x000000000d002287566491341b2afebe00000000001f693b0000000000000000, rhodok_face_older_2],
  ["knight_12_10", "Lord Vati", "Vati", tf_hero, 0, reserved, fac_kingdom_12, [itm_hunter_d, itm_nobleman_outfit,  itm_coat_of_plates, itm_m_gloves_a, itm_sword_of_war, itm_tab_shield_tauria_b, itm_light_lance, itm_bascinet], knight_attrib_5,wp(250),knight_skills_5, 0x00000000060852142353723ceed17eff00000000001cd33c0000000000000000, rhodok_face_older_2],
  ["knight_12_11", "Lord Epon", "Epon", tf_hero, 0, reserved, fac_kingdom_12, [itm_hunter, itm_nobleman_outfit,  itm_coat_of_plates, itm_m_gloves_a, itm_sword_of_war, itm_tab_shield_tauria_b, itm_light_lance, itm_bascinet], knight_attrib_5,wp(250),knight_skills_5, 0x00000000220814c755136c9ba6c97eff00000000001ca9bd0000000000000000, rhodok_face_older_2],
  ["knight_12_12", "Lord Comgi", "Comgi", tf_hero, 0, reserved, fac_kingdom_12, [itm_hunter, itm_nobleman_outfit,  itm_coat_of_plates, itm_m_gloves_a, itm_sword_of_war, itm_tab_shield_tauria_b, itm_light_lance, itm_bascinet], knight_attrib_5,wp(250),knight_skills_5, 0x00000000000850c32b1949b46b99ffbf00000000001e36fd0000000000000000, rhodok_face_older_2],
  ["knight_12_13", "Lord Algoil", "Algoil", tf_hero, 0, reserved, fac_kingdom_12, [itm_hunter_f, itm_nobleman_outfit,  itm_coat_of_plates, itm_m_gloves_a, itm_sword_of_war, itm_tab_shield_heater_c, itm_light_lance, itm_bascinet], knight_attrib_5,wp(250),knight_skills_5, 0x00000000090c10c537232d3b5bc57f3f00000000001e41790000000000000000, rhodok_face_older_2],
  ["knight_12_14", "Lord Slorue", "Slorue", tf_hero, 0, reserved, fac_kingdom_12, [itm_hunter_b, itm_nobleman_outfit,  itm_coat_of_plates, itm_m_gloves_a, itm_sword_of_war, itm_tab_shield_tauria_b, itm_light_lance, itm_bascinet], knight_attrib_5,wp(250),knight_skills_5, 0x000000000e1000d1331b91c6cc54ffbf00000000001e353b0000000000000000, rhodok_face_older_2],
  ["knight_12_15", "Lord Corca", "Corca", tf_hero, 0, reserved, fac_kingdom_12, [itm_hunter_b, itm_nobleman_outfit,  itm_coat_of_plates_v1, itm_m_gloves_a, itm_sword_of_war, itm_tab_shield_heater_d, itm_light_lance, itm_bascinet], knight_attrib_5,wp(250),knight_skills_5, 0x000000000a04504914cc4d199aaa7e7f00000000001d43b80000000000000000, rhodok_face_older_2],
  ["knight_12_16", "Lord Sesne", "Sesne", tf_hero, 0, reserved, fac_kingdom_12, [itm_hunter_b, itm_nobleman_outfit,  itm_coat_of_plates_v1, itm_m_gloves_a, itm_sword_of_war, itm_tab_shield_heater_d, itm_light_lance, itm_bascinet], knight_attrib_5,wp(250),knight_skills_5, 0x000000000d0c0589449569b71c75ff7f00000000001e387e0000000000000000, rhodok_face_older_2],
  ["knight_12_17", "Lord Cormi", "Cormi", tf_hero, 0, reserved, fac_kingdom_12, [itm_hunter_e, itm_nobleman_outfit,  itm_coat_of_plates_v1, itm_m_gloves_a, itm_sword_of_war, itm_tab_shield_heater_d, itm_light_lance, itm_bascinet], knight_attrib_5,wp(250),knight_skills_5, 0x000000000b0021c546db6e242b517f3f00000000001e19bc0000000000000000, rhodok_face_older_2],
  ["knight_12_18", "Lord Arix", "Arix", tf_hero, 0, reserved, fac_kingdom_12, [itm_hunter_c, itm_nobleman_outfit,  itm_coat_of_plates_v1, itm_m_gloves_a, itm_sword_of_war, itm_tab_shield_tauria_a, itm_light_lance, itm_bascinet], knight_attrib_5,wp(250),knight_skills_5, 0x000000001604628f429b763cec8d7f7f00000000001d49630000000000000000, rhodok_face_older_2],
  ["knight_12_19", "Lord Goloy", "Goloy", tf_hero, 0, reserved, fac_kingdom_12, [itm_hunter_c, itm_nobleman_outfit,   itm_stormguard_aketon_plated_b_v1, itm_m_gloves_a, itm_sword_of_war, itm_tab_shield_tauria_b, itm_light_lance, itm_bascinet], knight_attrib_5,wp(250),knight_skills_5, 0x000000003e08130416cbacb4e451feff00000000001e5afb0000000000000000, rhodok_face_older_2],
  ["knight_12_20", "Lord Drigo", "Drigo", tf_hero, 0, reserved, fac_kingdom_12, [itm_hunter_d, itm_nobleman_outfit,   itm_stormguard_hauberk_a, itm_m_gloves_a, itm_war_axe, itm_tab_shield_tauria_a, itm_light_lance, itm_bascinet], knight_attrib_5,wp(250),knight_skills_5, 0x000000000000258116b3d5d5124cffff00000000001ee0fb0000000000000000, rhodok_face_older_2],
  
  ["kingdom_1_pretender",  "Lady Isolla of Suno",       "Isolla",  tf_hero|tf_female|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_1,[itm_charger,   itm_rich_outfit,                 itm_stormguard_hauberk_a,      itm_sword_medieval_c_small,      itm_tab_shield_small_round_c,       itm_bascinet],          lord_attrib,wp(220),knight_skills_5, 0x00000000ef00000237dc71b90c31631200000000001e371b0000000000000000],
#claims pre-salic descent

  ["kingdom_2_pretender",  "Prince Valdym the Bastard", "Valdym",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_2,[itm_hunter,    itm_courtly_outfit,                                itm_chornovalley_heavy_mail_b,       itm_military_pick,      itm_tab_shield_heater_b,      itm_flat_topped_helmet],    lord_attrib,wp(220),knight_skills_5, 0x00000000200412142452ed631b30365c00000000001c94e80000000000000000, vaegir_face_middle_2],
#had his patrimony falsified

  ["kingdom_3_pretender",  "Dustum Khan",               "Dustum",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_3,[itm_courser,   itm_nomad_robe,                                     itm_khergit_guard_armor,         itm_sword_khergit_2,              itm_tab_shield_small_round_c,       itm_bascinet_3],      lord_attrib,wp(220),knight_skills_5, 0x000000065504310b30d556b51238f66100000000001c256d0000000000000000, khergit_face_middle_2],
#of the family

  ["kingdom_4_pretender",  "Lethwin Far-Seeker",   "Lethwin",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_4,[itm_hunter,    itm_tabard,                                 itm_brigandine_red,           itm_sword_medieval_c,           itm_tab_shield_heater_cav_a,    itm_kettle_hat],            lord_attrib,wp(220),knight_skills_5, 0x00000004340c01841d89949529a6776a00000000001c910a0000000000000000, nord_face_young_2],
#dispossessed and wronged

  ["kingdom_5_pretender",  "Lord Kastor of Veluca",  "Kastor",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_5,[itm_warhorse,  itm_nobleman_outfit,                             itm_mail_hauberk,           itm_sword_medieval_c,         itm_tab_shield_heater_d,        itm_spiked_helmet],         lord_attrib,wp(220),knight_skills_5, 0x0000000bed1031051da9abc49ecce25e00000000001e98680000000000000000, rhodok_face_old_2],
#republican

  ["kingdom_6_pretender",  "Arwa the Pearled One",       "Arwa",  tf_hero|tf_female|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_6,[itm_arabian_horse_b, itm_solarian_armor_scale_a, itm_sarranid_cavalry_sword,      itm_tab_shield_small_round_c],          lord_attrib,wp(220),knight_skills_5, 0x000000050b003004072d51c293a9a70b00000000001dd6a90000000000000000],

##  ["kingdom_1_lord_a", "Kingdom 1 Lord A", "Kingdom 1 Lord A", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse,itm_leather_jacket,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_b", "Kingdom 1 Lord B", "Kingdom 1 Lord B", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse,itm_leather_jacket,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_c", "Kingdom 1 Lord C", "Kingdom 1 Lord C", tf_hero, 0,reserved,  fac_kingdom_3,[itm_saddle_horse,itm_leather_jacket,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_d", "Kingdom 1 Lord D", "Kingdom 1 Lord D", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse,itm_leather_jacket,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_e", "Kingdom 1 Lord E", "Kingdom 1 Lord E", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse,itm_leather_jacket,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_f", "Kingdom 1 Lord F", "Kingdom 1 Lord F", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse,itm_leather_jacket,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_g", "Kingdom 1 Lord G", "Kingdom 1 Lord G", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse,itm_leather_jacket,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_h", "Kingdom 1 Lord H", "Kingdom 1 Lord H", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse,itm_leather_jacket,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_i", "Kingdom 1 Lord I", "Kingdom 1 Lord I", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse,itm_leather_jacket,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_j", "Kingdom 1 Lord J", "Kingdom 1 Lord J", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse,itm_leather_jacket,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_k", "Kingdom 1 Lord K", "Kingdom 1 Lord K", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse,itm_leather_jacket,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_l", "Kingdom 1 Lord L", "Kingdom 1 Lord L", tf_hero, 0,reserved,  fac_kingdom_3,[itm_saddle_horse,itm_leather_jacket,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_m", "Kingdom 1 Lord M", "Kingdom 1 Lord M", tf_hero, 0,reserved,  fac_kingdom_3,[itm_saddle_horse,itm_leather_jacket,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_n", "Kingdom 1 Lord N", "Kingdom 1 Lord N", tf_hero, 0,reserved,  fac_kingdom_3,[itm_saddle_horse,itm_leather_jacket,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],



#  ["town_1_ruler_a", "King Harlaus",  "King Harlaus",  tf_hero, scn_town_1_castle|entry(9),reserved,  fac_swadians,[itm_saddle_horse,itm_courtly_outfit],def_attrib|level(2),wp(20),knows_common, 0x000000000010908101e36db44b75b6dd],
#  ["town_2_ruler_a", "Duke Taugard",  "Duke Taugard",  tf_hero, scn_town_2_castle|entry(9),reserved,  fac_swadians,[itm_saddle_horse,itm_courtly_outfit],def_attrib|level(2),wp(20),knows_common, 0x000000000000310401e06db86375f6da],
#  ["town_3_ruler_a", "Count Grimar",  "Count Grimar",  tf_hero, scn_town_3_castle|entry(9),reserved, fac_swadians,[itm_saddle_horse,itm_leather_jacket],def_attrib|level(2),wp(20),knows_common, 0x000000000004430301e46136eb75bc0a],
#  ["town_4_ruler_a", "Count Haxalye", "Count Haxalye", tf_hero, scn_town_4_castle|entry(9),reserved,  fac_swadians,[itm_saddle_horse,itm_leather_jacket],def_attrib|level(2),wp(20),knows_common, 0x000000000010918701e77136e905bc0e
#  ["town_5_ruler_a", "Count Belicha", "Count Belicha", tf_hero, scn_town_5_castle|entry(9),reserved, fac_swadians,[itm_saddle_horse,itm_leather_jacket],def_attrib|level(2),wp(20),knows_common, 0x00000000000421c801e7713729c5b8ce],
#  ["town_6_ruler_a", "Count Nourbis", "Count Nourbis", tf_hero, scn_town_6_castle|entry(9),reserved,  fac_swadians,[itm_saddle_horse,itm_leather_jacket],def_attrib|level(2),wp(20),knows_common, 0x00000000000c640501e371b72bcdb724],
#  ["town_7_ruler_a", "Count Rhudolg", "Count Rhudolg", tf_hero, scn_town_7_castle|entry(9),reserved,  fac_swadians,[itm_saddle_horse,itm_leather_jacket],def_attrib|level(2),wp(20),knows_common, 0x00000000000c710201fa51b7286db721],
 
#  ["town_8_ruler_b", "King Yaroglek", "King_yaroglek", tf_hero, scn_town_8_castle|entry(9),reserved,  fac_vaegirs,[itm_saddle_horse,itm_leather_jacket],def_attrib|level(2),wp(20),knows_common, 0x000000000000128801f294ca6d66d555],
#  ["town_9_ruler_b", "Count Aolbrug", "Count_Aolbrug", tf_hero, scn_town_9_castle|entry(9),reserved,  fac_vaegirs,[itm_saddle_horse,itm_leather_jacket],def_attrib|level(2),wp(20),knows_common, 0x000000000004234401f26a271c8d38ea],
#  ["town_10_ruler_b","Count Rasevas", "Count_Rasevas", tf_hero, scn_town_10_castle|entry(9),reserved, fac_vaegirs,[itm_saddle_horse,itm_leather_jacket],def_attrib|level(2),wp(20),knows_common, 0x00000000001032c201f38e269372471c],
#  ["town_11_ruler_b","Count Leomir",  "Count_Leomir",  tf_hero, scn_town_11_castle|entry(9),reserved,  fac_vaegirs,[itm_saddle_horse,itm_leather_jacket],def_attrib|level(2),wp(20),knows_common, 0x00000000000c538001f55148936d3895],
#  ["town_12_ruler_b","Count Haelbrad","Count_Haelbrad",tf_hero, scn_town_12_castle|entry(9),reserved,  fac_vaegirs,[itm_saddle_horse,itm_leather_jacket],def_attrib|level(2),wp(20),knows_common, 0x00000000000410c701f38598ac8aaaab],
#  ["town_13_ruler_b","Count Mira",    "Count_Mira",    tf_hero, scn_town_13_castle|entry(9),reserved, fac_vaegirs,[itm_saddle_horse,itm_leather_jacket],def_attrib|level(2),wp(20),knows_common, 0x000000000004204401f390c515555594],
#  ["town_14_ruler_b","Count Camechaw","Count_Camechaw",tf_hero, scn_town_14_castle|entry(9),reserved,  fac_vaegirs,[itm_saddle_horse,itm_leather_jacket],def_attrib|level(2),wp(20),knows_common, 0x000000000008318101f390c515555594],

##  ["kingdom_2_lord_a", "Kingdom 2 Lord A", "Kingdom 2 Lord A", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jacket,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_b", "Kingdom 2 Lord B", "Kingdom 2 Lord B", tf_hero, 0,reserved,  fac_kingdom_11,[itm_saddle_horse,itm_leather_jacket,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_c", "Kingdom 2 Lord C", "Kingdom 2 Lord C", tf_hero, 0,reserved,  fac_kingdom_12,[itm_saddle_horse,itm_leather_jacket,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_d", "Kingdom 2 Lord D", "Kingdom 2 Lord D", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jacket,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_e", "Kingdom 2 Lord E", "Kingdom 2 Lord E", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jacket,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_f", "Kingdom 2 Lord F", "Kingdom 2 Lord F", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jacket,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_g", "Kingdom 2 Lord G", "Kingdom 2 Lord G", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jacket,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_h", "Kingdom 2 Lord H", "Kingdom 2 Lord H", tf_hero, 0,reserved,  fac_kingdom_11,[itm_saddle_horse,itm_leather_jacket,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_i", "Kingdom 2 Lord I", "Kingdom 2 Lord I", tf_hero, 0,reserved,  fac_kingdom_11,[itm_saddle_horse,itm_leather_jacket,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_j", "Kingdom 2 Lord J", "Kingdom 2 Lord J", tf_hero, 0,reserved,  fac_kingdom_11,[itm_saddle_horse,itm_leather_jacket,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_k", "Kingdom 2 Lord K", "Kingdom 2 Lord K", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jacket,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_l", "Kingdom 2 Lord L", "Kingdom 2 Lord L", tf_hero, 0,reserved,  fac_kingdom_12,[itm_saddle_horse,itm_leather_jacket,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_m", "Kingdom 2 Lord M", "Kingdom 2 Lord M", tf_hero, 0,reserved,  fac_kingdom_12,[itm_saddle_horse,itm_leather_jacket,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_n", "Kingdom 2 Lord N", "Kingdom 2 Lord N", tf_hero, 0,reserved,  fac_kingdom_12,[itm_saddle_horse,itm_leather_jacket,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],



#Royal family members

  ["knight_1_1_wife","Error - knight_1_1_wife should not appear in game","knight_1_1_wife",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_commoners, [itm_lady_dress_ruby ,   itm_turret_hat_ruby],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],

  #Swadian ladies - eight mothers, eight daughters, four sisters
  ["kingdom_1_lady_1","Lady Anna","Anna",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
  ["kingdom_1_lady_2","Lady Nelda","Nelda",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
  ["knight_1_lady_3","Lady Bela","Bela",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,  [], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
  ["knight_1_lady_4","Lady Elina","Elina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,  [], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000],
  ["kingdom_l_lady_5","Lady Constanis","Constanis",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_6","Lady Vera","Vera",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],
  ["kingdom_1_lady_7","Lady Auberina","Auberina",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_8","Lady Tibal","Tibal",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000],
  ["kingdom_1_lady_9","Lady Magar","Magar",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_10","Lady Thedosa","Thedosa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000],
  ["kingdom_1_lady_11","Lady Melisar","Melisar",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_12","Lady Irena","Irena",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,  0x000000003f04100148d245d6526d456b00000000001e3b350000000000000000],
  ["kingdom_l_lady_13","Lady Philenna","Philenna",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_14","Lady Sonadel","Sonadel",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000],
  ["kingdom_1_lady_15","Lady Boadila","Boadila",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_16","Lady Elys","Elys",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003b080003531e8932e432bb5a000000000008db6a0000000000000000],
  ["kingdom_1_lady_17","Lady Johana","Johana",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000446e4b4c2cc5234d200000000001ea3120000000000000000],
  ["kingdom_1_lady_18","Lady Bernatys","Bernatys",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000000083006465800000901161200000000001e38cc0000000000000000],
  ["kingdom_1_lady_19","Lady Enricata","Enricata",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
  ["kingdom_1_lady_20","Lady Gaeta","Gaeta",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_2],
  
  #Vaegir ladies
  ["kingdom_2_lady_1","Lady Junitha","Junitha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_2","Lady Katia","Katia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_3","Lady Seomis","Seomis",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_4","Lady Drina","Drina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_2_lady_5","Lady Nesha","Nesha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_6","Lady Tabath","Tabath",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_7","Lady Pelaeka","Pelaeka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_8","Lady Haris","Haris",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_2_lady_9","Lady Vayen","Vayen",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_10","Lady Joaka","Joaka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_11","Lady Tejina","Tejina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_12","Lady Olekseia","Olekseia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_2_lady_13","Lady Myntha","Myntha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_14","Lady Akilina","Akilina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_15","Lady Sepana","Sepana",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_16","Lady Iarina","Iarina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_2_lady_17","Lady Sihavan","Sihavan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_18","Lady Erenchina","Erenchina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_19","Lady Tamar","Tamar",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_20","Lady Valka","Valka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [itm_green_dress], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],


  ["kingdom_3_lady_1","Lady Borge","Borge",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_1],
  ["kingdom_3_lady_2","Lady Tuan","Tuan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_green_dress],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
  ["kingdom_3_lady_3","Lady Mahraz","Mahraz",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [itm_red_dress], def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_2],
  ["kingdom_3_lady_4","Lady Ayasu","Ayasu",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_red_dress], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],
  ["kingdom_3_lady_5","Lady Ravin","Ravin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_green_dress],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
  ["kingdom_3_lady_6","Lady Ruha","Ruha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_green_dress],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
  ["kingdom_3_lady_7","Lady Chedina","Chedina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
  ["kingdom_3_lady_8","Lady Kefra","Kefra",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
  ["kingdom_3_lady_9","Lady Nirvaz","Nirvaz",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001940c3006019c925165d1129b00000000001d13240000000000000000],
  ["kingdom_3_lady_10","Lady Dulua","Dulua",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
  ["kingdom_3_lady_11","Lady Selik","Selik",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000019b083005389591941379b8d100000000001e63150000000000000000],
  ["kingdom_3_lady_12","Lady Thalatha","Thalatha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],
  ["kingdom_3_lady_13","Lady Yasreen","Yasreen",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
  ["kingdom_3_lady_14","Lady Nadha","Nadha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_1],
  ["kingdom_3_lady_15","Lady Zenur","Zenur",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress], def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_2],
  ["kingdom_3_lady_16","Lady Arjis","Zenur",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001ad003001628c54b05d2e48b200000000001d56e60000000000000000],
  ["kingdom_3_lady_17","Lady Atjahan", "Atjahan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001a700300265cb6db15d6db6da00000000001f82180000000000000000],
  ["kingdom_3_lady_18","Lady Qutala","Qutala",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
  ["kingdom_3_lady_19","Lady Hindal","Hindal",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
  ["kingdom_3_lady_20","Lady Mechet","Mechet",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],
  
  
  
  ["kingdom_4_lady_1","Lady Jadeth","Jadeth",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_4_lady_2","Lady Miar","Miar",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_4_lady_3","Lady Dria","Dria",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["kingdom_4_lady_4","Lady Glunde","Glunde",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["kingdom_4_lady_5","Lady Loeka","Loeka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_4_lady_6","Lady Bryn","Bryn",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_4_lady_7","Lady Eir","Eir",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["knight_4_2b_daughter_1","Lady Thera","Thera",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["kingdom_4_lady_9","Lady Hild","Hild",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["knight_4_2c_wife_1","Lady Endegrid","Endegrid",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_4_lady_11","Lady Herjasa","Herjasa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["knight_4_2c_daughter","Lady Svipul","Svipul",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["knight_4_1b_wife","Lady Ingunn","Ingunn",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_4_lady_14","Lady Kaeteli","Kaeteli",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["knight_4_1b_daughter","Lady Eilif","Eilif",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["knight_4_2b_daughter_2","Lady Gudrun","Gudrun",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["kingdom_4_lady_17","Lady Bergit","Bergit",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["knight_4_2c_wife_2","Lady Aesa","Aesa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["knight_4_1c_daughter","Lady Alfrun","Alfrun",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["kingdom_4_lady_20","Lady Afrid","Afrid",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],


  ["kingdom_5_lady_1","Lady Brina","Brina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
  ["kingdom_5_lady_2","Lady Aliena","Aliena",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
  ["kingdom_5_lady_3","Lady Aneth","Aneth",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_lady_4","Lady Reada","Reada",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  ["kingdom_5_5_wife","Lady Saraten","Saraten",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
  ["kingdom_5_2b_wife_1","Lady Baotheia","Baotheia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000bf0400035913aa236b4d975a00000000001eb69c0000000000000000],
  ["kingdom_5_1c_daughter_1","Lady Eleandra","Eleandra",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_2c_daughter_1","Lady Meraced","Meraced",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  ["kingdom_5_1c_wife_1","Lady Adelisa","Adelisa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
  ["kingdom_5_2c_wife_1","Lady Calantina","Calantina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
  ["kingdom_5_1c_daughter_2","Lady Forbesa","Forbesa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_2c_daughter_2","Lady Claudora","Claudora",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  ["kingdom_5_1b_wife","Lady Anais","Anais",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
  ["kingdom_5_2b_wife_2","Lady Miraeia","Miraeia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
  ["kingdom_5_1c_daughter_3","Lady Agasia","Agasia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_lady_16","Lady Geneiava","Geneiava",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  ["kingdom_5_1c_wife_2","Lady Gwenael","Gwenael",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
  ["kingdom_5_2c_wife_2","Lady Ysueth","Ysueth",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
  ["kingdom_5_1c_daughter_4","Lady Ellian","Ellian",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_lady_20","Lady Timethi","Timethi",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  
#Sarranid ladies
  ["kingdom_6_lady_1","Lady Rayma","Rayma",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,  itm_sarranid_head_cloth],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
  ["kingdom_6_lady_2","Lady Thanaikha","Thanaikha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
  ["kingdom_6_lady_3","Lady Sulaha","Sulaha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,  [itm_sarranid_lady_dress], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
  ["kingdom_6_lady_4","Lady Shatha","Shatha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,  [itm_sarranid_lady_dress], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000],
  ["kingdom_6_lady_5","Lady Bawthan","Bawthan",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_6_lady_6","Lady Mahayl","Mahayl",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],
  ["kingdom_6_lady_7","Lady Isna","Isna",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_6_lady_8","Lady Siyafan","Siyafan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000],
  ["kingdom_6_lady_9","Lady Ifar","Ifar",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_6_lady_10","Lady Yasmin","Yasmin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000],
  ["kingdom_6_lady_11","Lady Dula","Dula",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_6_lady_12","Lady Ruwa","Ruwa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,  0x000000003f04100148d245d6526d456b00000000001e3b350000000000000000],
  ["kingdom_6_lady_13","Lady Luqa","Luqa",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_6_lady_14","Lady Zandina","Zandina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000],
  ["kingdom_6_lady_15","Lady Lulya","Lulya",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_6_lady_16","Lady Zahara","Zahara",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003b080003531e8932e432bb5a000000000008db6a0000000000000000],
  ["kingdom_6_lady_17","Lady Safiya","Safiya",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000446e4b4c2cc5234d200000000001ea3120000000000000000],
  ["kingdom_6_lady_18","Lady Khalisa","Khalisa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000000083006465800000901161200000000001e38cc0000000000000000],
  ["kingdom_6_lady_19","Lady Janab","Janab",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
  ["kingdom_6_lady_20","Lady Sur","Sur",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_2],

  ["kingdom_7_lady_1","Lady Erin Reeve","Erin Reeve",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_lady_dress_blue,  itm_sarranid_head_cloth],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
  ["kingdom_7_lady_2","Lady Ealurg","Ealurg",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
  ["kingdom_7_lady_3","Lady Wifru","Wifru",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7,  [itm_lady_dress_blue], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
  ["kingdom_7_lady_4","Lady Jane","Jane",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7,  [itm_lady_dress_blue], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000],
  ["kingdom_7_lady_5","Lady Hilda","Hilda",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_lady_dress_blue],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_7_lady_6","Lady Maly","Maly",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],
  ["kingdom_7_lady_7","Lady Arran","Arran",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_lady_dress_blue],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_7_lady_8","Lady Egild","Egild",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000],
  ["kingdom_7_lady_9","Lady Heva","Heva",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_7_lady_10","Lady Burghwe","Burghwe",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_lady_dress_blue],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000],
  ["kingdom_7_lady_11","Lady Hilia","Hilia",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_lady_dress_blue],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_7_lady_12","Lady Jane","Jane",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,  0x000000003f04100148d245d6526d456b00000000001e3b350000000000000000],
  ["kingdom_7_lady_13","Lady Atel","Atel",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_7_lady_14","Lady Alhhild","Alhhild",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_lady_dress_blue],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000],
  ["kingdom_7_lady_15","Lady Joane","Joane",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_7_lady_16","Lady Beatra","Beatra",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_lady_dress_blue],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003b080003531e8932e432bb5a000000000008db6a0000000000000000],
  ["kingdom_7_lady_17","Lady Sabeth Hawte","Sabeth Hawte",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000446e4b4c2cc5234d200000000001ea3120000000000000000],
  ["kingdom_7_lady_18","Lady Cece","Cece",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_lady_dress_blue],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000000083006465800000901161200000000001e38cc0000000000000000],
  ["kingdom_7_lady_19","Lady Adburh","Adburh",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
  ["kingdom_7_lady_20","Lady Cyna","Cyna",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [itm_lady_dress_blue],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_2],

  ["kingdom_8_lady_1","Lady Sila","Sila",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_lady_dress_blue,  itm_sarranid_head_cloth],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
  ["kingdom_8_lady_2","Lady Ninla","Ninla",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
  ["kingdom_8_lady_3","Lady Abag","Abag",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8,  [itm_lady_dress_blue], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
  ["kingdom_8_lady_4","Lady Saga","Saga",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8,  [itm_lady_dress_blue], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000],
  ["kingdom_8_lady_5","Lady Inlit","Inlit",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_lady_dress_blue],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_8_lady_6","Lady Suna","Suna",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],
  ["kingdom_8_lady_7","Lady Ninhub","Ninhub",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_lady_dress_blue],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_8_lady_8","Lady Ninki","Ninki",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000],
  ["kingdom_8_lady_9","Lady Ilil","Ilil",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_8_lady_10","Lady Nindur","Nindur",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_lady_dress_blue],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000],
  ["kingdom_8_lady_11","Lady Ninduk","Ninduk",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_lady_dress_blue],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_8_lady_12","Lady Saga","Saga",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,  0x000000003f04100148d245d6526d456b00000000001e3b350000000000000000],
  ["kingdom_8_lady_13","Lady Sidur","Sidur",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_8_lady_14","Lady Ninga","Ninga",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_lady_dress_blue],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000],
  ["kingdom_8_lady_15","Lady Ayammeshki","Ayammeshki",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_8_lady_16","Lady Nanna","Nanna",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_lady_dress_blue],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003b080003531e8932e432bb5a000000000008db6a0000000000000000],
  ["kingdom_8_lady_17","Lady Ingag","Ingag",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000446e4b4c2cc5234d200000000001ea3120000000000000000],
  ["kingdom_8_lady_18","Lady Ayarum","Ayarum",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_lady_dress_blue],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000000083006465800000901161200000000001e38cc0000000000000000],
  ["kingdom_8_lady_19","Lady Ayabit","Ayabit",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
  ["kingdom_8_lady_20","Lady Shuba","Shuba",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_lady_dress_blue],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_2],

  ["kingdom_9_lady_1","Lady Elyn","Elyn",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_lady_dress_blue,  itm_sarranid_head_cloth],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
  ["kingdom_9_lady_2","Lady Bride","Bride",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
  ["kingdom_9_lady_3","Lady Cece","Cece",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9,  [itm_lady_dress_ruby], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
  ["kingdom_9_lady_4","Lady Elyn Teray","Elyn Teray",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9,  [itm_lady_dress_ruby], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000],
  ["kingdom_9_lady_5","Lady Bily","Bily",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_lady_dress_ruby],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_9_lady_6","Lady Abet","Abet",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],
  ["kingdom_9_lady_7","Lady Mera","Mera",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_lady_dress_ruby],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_9_lady_8","Lady Lucie Gare","Lucie Gare",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000],
  ["kingdom_9_lady_9","Lady Sabeatr","Sabeatr",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_9_lady_10","Lady Cily","Cily",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_lady_dress_ruby],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000],
  ["kingdom_9_lady_11","Lady Anel","Anel",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_lady_dress_ruby],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_9_lady_12","Lady Efril","Efril",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,  0x000000003f04100148d245d6526d456b00000000001e3b350000000000000000],
  ["kingdom_9_lady_13","Lady Marget","Marget",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_9_lady_14","Lady Atet Payne","Atet Payne",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_lady_dress_ruby],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000],
  ["kingdom_9_lady_15","Lady Marget Vaughey","Marget Vaughey",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_9_lady_16","Lady Ellyn","Ellyn",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_lady_dress_ruby],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003b080003531e8932e432bb5a000000000008db6a0000000000000000],
  ["kingdom_9_lady_17","Lady Argell Righte","Argell Righte",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000446e4b4c2cc5234d200000000001ea3120000000000000000],
  ["kingdom_9_lady_18","Lady Jane","Jane",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_lady_dress_ruby],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000000083006465800000901161200000000001e38cc0000000000000000],
  ["kingdom_9_lady_19","Lady Enet","Enet",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
  ["kingdom_9_lady_20","Lady Beatra","Beatra",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [itm_lady_dress_ruby],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_2],
  
  ["kingdom_10_lady_1","Lady Elys","Elys",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10, [itm_lady_dress_ruby,  itm_sarranid_head_cloth],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
  ["kingdom_10_lady_2","Lady Lyse Vere","Lyse Vere",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10, [itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
  ["kingdom_10_lady_3","Lady Eryen","Eryen",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10,  [itm_lady_dress_ruby], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
  ["kingdom_10_lady_4","Lady Eryn Finchey","Eryn Finchey",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10,  [itm_lady_dress_ruby], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000],
  ["kingdom_10_lady_5","Lady Sarrey Gysby","Sarrey Gysby",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10, [itm_lady_dress_ruby],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_10_lady_6","Lady Hone Dreyne","Hone Dreyne",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10, [itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],
  ["kingdom_10_lady_7","Lady Benne","Benne",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10, [itm_lady_dress_ruby],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_10_lady_8","Lady Abell Finchey","Abell Finchey",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10, [itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000],
  ["kingdom_10_lady_9","Lady Sarra","Sarra",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10, [itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_10_lady_10","Lady Auciel","Auciel",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10, [itm_lady_dress_ruby],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000],
  ["kingdom_10_lady_11","Lady Jane","Jane",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10, [itm_lady_dress_ruby],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_10_lady_12","Lady Mery","Mery",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10, [itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,  0x000000003f04100148d245d6526d456b00000000001e3b350000000000000000],
  ["kingdom_10_lady_13","Lady Brose Aver","Brose Aver",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10, [itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_10_lady_14","Lady Suse","Suse",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10, [itm_lady_dress_ruby],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000],
  ["kingdom_10_lady_15","Lady Mery Rowe","Mery Rowe",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10, [itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_10_lady_16","Lady Joane Tere","Joane Tere",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10, [itm_lady_dress_ruby],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003b080003531e8932e432bb5a000000000008db6a0000000000000000],
  ["kingdom_10_lady_17","Lady Malia","Malia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10, [itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000446e4b4c2cc5234d200000000001ea3120000000000000000],
  ["kingdom_10_lady_18","Lady Elin","Elin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10, [itm_lady_dress_ruby],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000000083006465800000901161200000000001e38cc0000000000000000],
  ["kingdom_10_lady_19","Lady Joane","Joane",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10, [itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
  ["kingdom_10_lady_20","Lady Joane Flerke","Joane Flerke",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10, [itm_lady_dress_ruby],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_2],

  ["kingdom_11_lady_1","Lady Yaelah Weidi","Yaelah Weidi",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [itm_lady_dress_green,  itm_sarranid_head_cloth],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
  ["kingdom_11_lady_2","Lady Jethra Rosenb","Jethra Rosenb",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [itm_lady_dress_ruby],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
  ["kingdom_11_lady_3","Lady Ariel Jero","Ariel Jero",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11,  [itm_lady_dress_green], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
  ["kingdom_11_lady_4","Lady Sheba Mani","Sheba Mani",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11,  [itm_lady_dress_green], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000],
  ["kingdom_11_lady_5","Lady Anar Goni","Anar Goni",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_11_lady_6","Lady Amith Goloh","Amith Goloh",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [itm_lady_dress_ruby],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],
  ["kingdom_11_lady_7","Lady Bara Mani","Bara Mani",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_11_lady_8","Lady Adah Denhel","Adah Denhel",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [itm_lady_dress_ruby],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000],
  ["kingdom_11_lady_9","Lady Mera Rossman","Mera Rossman",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [itm_lady_dress_ruby],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_11_lady_10","Lady Elav Gottor","Elav Gottor",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000],
  ["kingdom_11_lady_11","Lady Avit Rayeshav","Avit Rayeshav",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_11_lady_12","Lady Arar Inskir","Arar Inskir",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [itm_lady_dress_ruby],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,  0x000000003f04100148d245d6526d456b00000000001e3b350000000000000000],
  ["kingdom_11_lady_13","Lady Yaelil Golomst","Yaelil Golomst",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [itm_lady_dress_ruby],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_11_lady_14","Lady Elah Pinsky","Elah Pinsky",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000],
  ["kingdom_11_lady_15","Lady Shana Dermoh","Shana Dermoh",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [itm_lady_dress_ruby],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_11_lady_16","Lady Agag Daro","Agag Daro",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003b080003531e8932e432bb5a000000000008db6a0000000000000000],
  ["kingdom_11_lady_17","Lady Maela Bermach","Maela Bermach",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [itm_lady_dress_ruby],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000446e4b4c2cc5234d200000000001ea3120000000000000000],
  ["kingdom_11_lady_18","Lady Orpah Nero","Orpah Nero",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000000083006465800000901161200000000001e38cc0000000000000000],
  ["kingdom_11_lady_19","Lady Tala Zahad","Tala Zahad",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [itm_lady_dress_ruby],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
  ["kingdom_11_lady_20","Lady Anar Pazy","Anar Pazy",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [itm_lady_dress_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_2],

  ["kingdom_12_lady_1","Lady Garda","Garda",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12, [itm_lady_dress_blue,  itm_sarranid_head_cloth],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
  ["kingdom_12_lady_2","Lady Cina","Cina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12, [itm_lady_dress_ruby],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
  ["kingdom_12_lady_3","Lady Disebe","Disebe",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12,  [itm_lady_dress_blue], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
  ["kingdom_12_lady_4","Lady Aradard","Aradard",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12,  [itm_lady_dress_blue], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000],
  ["kingdom_12_lady_5","Lady Ardalad","Ardalad",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12, [itm_lady_dress_blue],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_12_lady_6","Lady Adadel","Adadel",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12, [itm_lady_dress_ruby],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],
  ["kingdom_12_lady_7","Lady Radborga","Radborga",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12, [itm_lady_dress_blue],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_12_lady_8","Lady Eresuuis","Eresuuis",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12, [itm_lady_dress_ruby],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000],
  ["kingdom_12_lady_9","Lady Indanard","Indanard",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12, [itm_lady_dress_ruby],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_12_lady_10","Lady Hildisa","Hildisa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12, [itm_lady_dress_blue],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000],
  ["kingdom_12_lady_11","Lady Creda","Creda",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12, [itm_lady_dress_blue],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_12_lady_12","Lady Thinilda","Thinilda",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12, [itm_lady_dress_ruby],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,  0x000000003f04100148d245d6526d456b00000000001e3b350000000000000000],
  ["kingdom_12_lady_13","Lady Indis","Indis",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12, [itm_lady_dress_ruby],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_12_lady_14","Lady Rude","Rude",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12, [itm_lady_dress_blue],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000],
  ["kingdom_12_lady_15","Lady Thieta","Thieta",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12, [itm_lady_dress_ruby],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_12_lady_16","Lady Egekis","Egekis",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12, [itm_lady_dress_blue],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003b080003531e8932e432bb5a000000000008db6a0000000000000000],
  ["kingdom_12_lady_17","Lady Hilda","Hilda",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12, [itm_lady_dress_ruby],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000446e4b4c2cc5234d200000000001ea3120000000000000000],
  ["kingdom_12_lady_18","Lady Windise","Windise",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12, [itm_lady_dress_blue],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000000083006465800000901161200000000001e38cc0000000000000000],
  ["kingdom_12_lady_19","Lady Thilda","Thilda",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12, [itm_lady_dress_blue],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
  ["kingdom_12_lady_20","Lady Bergunda","Bergunda",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12, [itm_lady_dress_blue],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_2],

#  ["kingdom_11_lord_daughter","kingdom_11_lord_daughter","kingdom_11_lord_daughter",tf_hero|tf_female,0,reserved,fac_kingdom_10,  [ itm_lady_dress_blue ,   itm_turret_hat_blue], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008300701c08d34a450ce43],
#  ["kingdom_13_lord_daughter","kingdom_13_lord_daughter","kingdom_13_lord_daughter",tf_hero|tf_female,0,reserved,fac_kingdom_10,  [ itm_lady_dress_green,   itm_turret_hat_green], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008000401db10a45b41d6d8],
##  ["kingdom_1_lady_a","kingdom_1_lady_a","kingdom_1_lady_a",tf_hero|tf_female,0,reserved,fac_kingdom_1, [   itm_lady_dress_blue ,   itm_turret_hat_blue],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008500201d8ad93708e4694],
##  ["kingdom_1_lady_b","kingdom_1_lady_b","kingdom_1_lady_b",tf_hero|tf_female,0,reserved,fac_kingdom_1, [   itm_lady_dress_ruby ,   itm_turret_hat_ruby],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000004000101c3ae68e0e944ac],
##  ["kingdom_2_lady_a","Kingdom 2 Lady a","Kingdom 2 Lady a",tf_hero|tf_female,0,reserved,fac_kingdom_2, [               itm_lady_dress_green,   itm_turret_hat_green],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008100501d8ad93708e4694],
##  ["kingdom_2_lady_b","Kingdom 2 Lady b","Kingdom 2 Lady b",tf_hero|tf_female,0,reserved,fac_kingdom_2, [               itm_lady_dress_blue ,   itm_turret_hat_blue],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000004000401d8ad93708e4694],
##  ["kingdom_3_lady_a","Kingdom 3 Lady a","Kingdom 3 Lady a",tf_hero|tf_female,0,reserved,fac_kingdom_3, [               itm_lady_dress_ruby ,   itm_turret_hat_ruby],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000010500301d8ad93708e4694],
##
##  ["kingdom_3_lady_b","Kingdom 3 Lady b","Kingdom 3 Lady b",tf_hero|tf_female,0,reserved,fac_kingdom_3,  [                         itm_lady_dress_ruby ,   itm_turret_hat_ruby], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000000100601d8b08d76d14a24],
##  ["kingdom_4_lady_a","Kingdom 4 Lady a","Kingdom 4 Lady a",tf_hero|tf_female,0,reserved,fac_kingdom_4,  [                         itm_lady_dress_green,   itm_turret_hat_green], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000010500601d8ad93708e4694],
##  ["kingdom_4_lady_b","Kingdom 4 Lady b","Kingdom 4 Lady b",tf_hero|tf_female,0,reserved,fac_kingdom_4,  [                         itm_lady_dress_blue ,   itm_turret_hat_blue], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008500201d8ad93708e4694],

  ["heroes_end", "{!}heroes end", "{!}heroes end", tf_hero, 0,reserved,  fac_neutral,[itm_saddle_horse,itm_leather_jacket],def_attrib|level(2),wp(20),knows_common, 0x000000000008318101f390c515555594],
#Merchants                                                                              AT                      SILAH                   ZIRH                        BOT                         Head_wear
##  ["merchant_1", "merchant_1_F", "merchant_1_F",tf_hero|tf_female,  0,0, fac_kingdom_1,[itm_courser,            itm_fighting_axe,       itm_leather_jerkin,                   itm_straw_hat],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008200201e54c137a940c91],
##  ["merchant_2", "merchant_2", "merchant_2", tf_hero,               0,0, fac_kingdom_2,[itm_saddle_horse,       itm_arming_sword,       itm_light_leather,                                      ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000000000601db6db6db6db6db],
##  ["merchant_3", "merchant_3", "merchant_3", tf_hero,               0,0, fac_kingdom_3,[itm_courser,            itm_nordic_sword,       itm_leather_jerkin,                                     ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008100701db6db6db6db6db],
##  ["merchant_4", "merchant_4_F", "merchant_4_F",tf_hero|tf_female,  0,0, fac_kingdom_4,[itm_saddle_horse,       itm_falchion,           itm_light_leather,                                        ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000010500401e54c137a945c91],
##  ["merchant_5", "merchant_5", "merchant_5", tf_hero,               0,0, fac_kingdom_5,[itm_saddle_horse,       itm_sword,              itm_ragged_outfit,                                       ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008038001e54c135a945c91],
##  ["merchant_6", "merchant_6", "merchant_6", tf_hero,               0,0, fac_kingdom_1,[itm_saddle_horse,      itm_scimitar,           itm_leather_jerkin,                                   ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000000248e01e54c1b5a945c91],
##  ["merchant_7", "merchant_7_F", "merchant_7_F",tf_hero|tf_female,  0,0, fac_kingdom_2,[itm_hunter,            itm_arming_sword,       itm_padded_leather,                                       ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000004200601c98ad39c97557a],
##  ["merchant_8", "merchant_8", "merchant_8", tf_hero,               0,0, fac_kingdom_3,[itm_saddle_horse,      itm_nordic_sword,       itm_light_leather,                    itm_woolen_hood],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000001095ce01d6aad3a497557a],
##  ["merchant_9", "merchant_9", "merchant_9", tf_hero,               0,0, fac_kingdom_4,[itm_saddle_horse,      itm_sword,              itm_padded_leather,                                      ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000010519601ec26ae99898697],
##  ["merchant_10","merchant_10","merchant_10",tf_hero,               0,0, fac_merchants,[itm_hunter,             itm_bastard_sword,      itm_light_leather,                                      ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000884c401f6837d3294e28a],
##  ["merchant_11","merchant_11","merchant_11",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_sword,              itm_leather_jacket,                                     ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000c450501e289dd2c692694],
##  ["merchant_12","merchant_12","merchant_12",tf_hero,               0,0, fac_merchants,[itm_hunter,             itm_falchion,           itm_leather_jerkin,                                      ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000c660a01e5af3cb2763401],
##  ["merchant_13","merchant_13","merchant_13",tf_hero,               0,0, fac_merchants,[itm_sumpter_horse,      itm_nordic_sword,       itm_padded_leather,                                   ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000001001d601ec912a89e4d534],
##  ["merchant_14","merchant_14","merchant_14",tf_hero,               0,0, fac_merchants,[itm_courser,            itm_bastard_sword,      itm_light_leather,                                       ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000004335601ea2c04a8b6a394],
##  ["merchant_15","merchant_15","merchant_15",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_sword,              itm_padded_leather,                     itm_fur_hat],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008358e01dbf27b6436089d],
##  ["merchant_16","merchant_16_F","merchant_16_F",tf_hero|tf_female, 0,0, fac_merchants,[itm_hunter,             itm_bastard_sword,      itm_light_leather,                                       ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000c300101db0b9921494add],
##  ["merchant_17","merchant_17","merchant_17",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_sword,              itm_leather_jacket,                                       ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008740f01e945c360976a0a],
##  ["merchant_18","merchant_18","merchant_18",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_nordic_sword,       itm_padded_leather,                                   ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008020c01fc2db3b4c97685],
##  ["merchant_19","merchant_19","merchant_19",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_falchion,           itm_leather_jerkin,                                     ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008118301f02af91892725b],
##  ["merchant_20","merchant_20_F","merchant_20_F",tf_hero|tf_female, 0,0, fac_merchants,[itm_courser,            itm_arming_sword,       itm_padded_leather,                                   ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000010500401f6837d27688212],

  
#Seneschals
  ["town_1_seneschal", "{!}Town 1 Seneschal", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic], def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["town_2_seneschal", "{!}Town 2 Seneschal", "{!}Town 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_padded_leather,     ],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["town_3_seneschal", "{!}Town 3 Seneschal", "{!}Town 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic], def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["town_4_seneschal", "{!}Town 4 Seneschal", "{!}Town 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_blue_gambeson],     def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["town_5_seneschal", "{!}Town 5 Seneschal", "{!}Town 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     ],   def_attrib|level(2),wp(20),knows_common, 0x000000000000249101e7898999ac54c6],
  ["town_6_seneschal", "{!}Town 6 Seneschal", "{!}Town 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_red_gambeson],   def_attrib|level(2),wp(20),knows_common, 0x000000000010360b01cef8b57553d34e],
  ["town_7_seneschal", "{!}Town 7 Seneschal", "{!}Town7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     ],   def_attrib|level(2),wp(20),knows_common, 0x000000000000018101f9487aa831dce4],
  ["town_8_seneschal", "{!}Town 8 Seneschal", "{!}Town 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_red_gambeson],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["town_9_seneschal", "{!}Town 9 Seneschal", "{!}Town 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic], def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["town_10_seneschal", "{!}Town 10 Seneschal", "{!}Town 10 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     ],     def_attrib|level(2),wp(20),knows_common, 0x000000000010230c01ef41badb50465e],
  ["town_11_seneschal", "{!}Town 11 Seneschal", "{!}Town 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jacket],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["town_12_seneschal", "{!}Town 12 Seneschal", "{!}Town 12 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_coarse_tunic], def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["town_13_seneschal", "{!}Town 13 Seneschal", "{!}Town 13 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     ],   def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["town_14_seneschal", "{!}Town 14 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_15_seneschal", "{!}Town 15 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_16_seneschal", "{!}Town 16 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_17_seneschal", "{!}Town17 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_18_seneschal", "{!}Town 18 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_19_seneschal", "{!}Town 19 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_20_seneschal", "{!}Town 20 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_21_seneschal", "{!}Town 21 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_22_seneschal", "{!}Town 22 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],

  ["castle_1_seneschal", "{!}Castle 1 Seneschal", "{!}Castle 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic],    def_attrib|level(2),wp(20),knows_common, 0x000000000010360b01cef8b57553d34e],
  ["castle_2_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_nomad_armor],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_3_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_4_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_5_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_6_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_7_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_blue_gambeson],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_8_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_9_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_10_seneschal", "{!}Castle 10 Seneschal", "{!}Castle 10 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_11_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_12_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_nomad_armor],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_13_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_14_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_15_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_16_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_17_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_blue_gambeson],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_18_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_19_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_20_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_21_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_22_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_nomad_armor],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_23_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_24_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_25_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_26_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_27_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_blue_gambeson],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_28_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_29_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_30_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_31_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_32_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_nomad_armor],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_33_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_34_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_35_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_36_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_37_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_blue_gambeson],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_38_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_39_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_40_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_41_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_42_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_43_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_44_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_45_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_46_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_47_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_48_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_49_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],

#Arena Masters
  ["town_1_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_1_arena|entry(52),reserved,   fac_commoners,[itm_coarse_tunic],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_2_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_2_arena|entry(52),reserved,   fac_commoners,[itm_linen_tunic],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_3_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_3_arena|entry(52),reserved,   fac_commoners,[itm_nomad_armor],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_4_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_4_arena|entry(52),reserved,   fac_commoners,[itm_coarse_tunic],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_5_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_5_arena|entry(52),reserved,   fac_commoners,[itm_linen_tunic],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_6_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_6_arena|entry(52),reserved,   fac_commoners,[itm_leather_jerkin], def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_7_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_7_arena|entry(52),reserved,   fac_commoners,[itm_padded_leather],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_8_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_8_arena|entry(52),reserved,   fac_commoners,[itm_linen_tunic],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_9_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_9_arena|entry(52),reserved,   fac_commoners,[itm_padded_leather], def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_10_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_10_arena|entry(52),reserved,  fac_commoners,[itm_nomad_armor],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_11_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_11_arena|entry(52),reserved,  fac_commoners,[itm_coarse_tunic],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_12_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_12_arena|entry(52),reserved,  fac_commoners,[itm_leather_jerkin],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_13_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_13_arena|entry(52),reserved,  fac_commoners,[itm_coarse_tunic],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_14_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_14_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_15_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_15_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_16_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_16_arena|entry(52),reserved,  fac_commoners,[itm_fur_coat],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_17_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_17_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_18_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_18_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_19_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_19_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_20_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_20_arena|entry(52),reserved,  fac_commoners,[itm_fur_coat],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_21_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_21_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_22_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_22_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],

# Armor Merchants
  #arena_masters_end = zendar_armorer

  ["town_1_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_2_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_woolen_dress,          itm_straw_hat       ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_3_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_red      ],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_4_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_red_gambeson],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_5_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_6_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_7_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_8_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_leather],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_9_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_blue_gambeson],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_10_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_11_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_12_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_red_gambeson],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_13_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jacket],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_14_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_woolen_dress, itm_headcloth],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_15_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_blue_gambeson],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_16_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_17_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_18_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_woolen_dress,         itm_headcloth       ],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_19_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_blue_gambeson   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_20_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_21_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_22_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_sarranid_common_dress,         itm_sarranid_head_cloth       ],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],

# Weapon merchants

  ["town_1_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,      itm_straw_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_2_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_3_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_4_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_5_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_6_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_7_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_8_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_woolen_dress,     itm_straw_hat],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_9_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_10_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_11_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jacket],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_12_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_13_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_red,     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_14_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_blue,     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_15_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jacket],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_16_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_17_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_green,     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_18_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_19_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jacket],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_20_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_21_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_green],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_22_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],

#Tavern keepers

  ["town_1_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_1_tavern|entry(9),0,   fac_commoners,[itm_leather_apron],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_2_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_2_tavern|entry(9),0,   fac_commoners,[itm_leather_apron],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_3_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_3_tavern|entry(9),0,   fac_commoners,[itm_woolen_dress],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_4_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_4_tavern|entry(9),0,   fac_commoners,[itm_leather_apron],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_5_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_5_tavern|entry(9),0,   fac_commoners,[itm_leather_apron],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_6_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_6_tavern|entry(9),0,   fac_commoners,[itm_woolen_dress],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_7_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_7_tavern|entry(9),0,   fac_commoners,[itm_woolen_dress,              itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_8_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_8_tavern|entry(9),0,   fac_commoners,[itm_leather_apron],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_9_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_9_tavern|entry(9),0,   fac_commoners,[itm_woolen_dress],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_10_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_10_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_11_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_11_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_12_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_12_tavern|entry(9),0,  fac_commoners,[itm_leather_apron],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_13_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_13_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,             itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_14_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_14_tavern|entry(9),0,  fac_commoners,[itm_shirt],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_15_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_15_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_16_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_16_tavern|entry(9),0,  fac_commoners,[itm_leather_apron],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_17_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_17_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,             itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_18_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_18_tavern|entry(9),0,  fac_commoners,[itm_shirt],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_19_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_19_tavern|entry(9),0,  fac_commoners,[itm_sarranid_dress_a],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_20_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_20_tavern|entry(9),0,  fac_commoners,[itm_solarian_robe_a],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_21_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_21_tavern|entry(9),0,  fac_commoners,[itm_sarranid_common_dress,             itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_22_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_22_tavern|entry(9),0,  fac_commoners,[itm_solarian_aketon_a],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],

#Goods Merchants

  ["town_1_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_1_store|entry(9),0, fac_commoners,     [itm_coarse_tunic                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_2_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_2_store|entry(9),0, fac_commoners,     [itm_leather_apron                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_3_merchant", "Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_3_store|entry(9),0, fac_commoners,     [itm_dress,           itm_straw_hat   ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_4_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_4_store|entry(9),0, fac_commoners,     [itm_leather_apron                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_5_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_5_store|entry(9),0, fac_commoners,     [itm_nomad_armor                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_6_merchant", "Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_6_store|entry(9),0, fac_commoners,     [itm_woolen_dress                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_7_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_7_store|entry(9),0, fac_commoners,     [itm_leather_jerkin                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_8_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_8_store|entry(9),0, fac_commoners,     [itm_leather_apron                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_9_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_9_store|entry(9),0, fac_commoners,     [itm_leather_apron                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_10_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_10_store|entry(9),0, fac_commoners,    [itm_leather_jerkin                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_11_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_11_store|entry(9),0, fac_commoners,    [itm_leather_apron                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_12_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_12_store|entry(9),0, fac_commoners,    [itm_woolen_dress,    itm_female_hood ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_13_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_13_store|entry(9),0, fac_commoners,    [itm_dress,           itm_straw_hat   ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_14_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_14_store|entry(9),0, fac_commoners,    [itm_leather_apron                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_15_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_15_store|entry(9),0, fac_commoners,    [itm_leather_apron                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_16_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_16_store|entry(9),0, fac_commoners,    [itm_woolen_dress,    itm_female_hood ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_17_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_17_store|entry(9),0, fac_commoners,    [itm_dress,           itm_straw_hat   ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_18_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_18_store|entry(9),0, fac_commoners,    [itm_leather_apron                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_19_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_19_store|entry(9),0, fac_commoners,    [itm_leather_apron                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_20_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_20_store|entry(9),0, fac_commoners,    [itm_sarranid_common_dress_b,   itm_sarranid_felt_head_cloth_b  ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_21_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_21_store|entry(9),0, fac_commoners,    [itm_sarranid_dress_a,           itm_sarranid_felt_head_cloth  ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_22_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_22_store|entry(9),0, fac_commoners,    [itm_leather_apron                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],

  ["salt_mine_merchant","Barezan","Barezan",                tf_hero|tf_is_merchant, scn_salt_mine|entry(1),0, fac_commoners,        [itm_leather_apron],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x00000000000c528601ea69b6e46dbdb6],

# Horse Merchants

  ["town_1_horse_merchant","Horse Merchant","{!}Town 1 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_blue_dress,                 itm_female_hood],   def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_2_horse_merchant","Horse Merchant","{!}Town 2 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_linen_tunic],                      def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_3_horse_merchant","Horse Merchant","{!}Town 3 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_nomad_armor],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_4_horse_merchant","Horse Merchant","{!}Town 4 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_leather_jerkin],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_5_horse_merchant","Horse Merchant","{!}Town 5 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_dress,                    itm_woolen_hood],   def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_6_horse_merchant","Horse Merchant","{!}Town 6 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_7_horse_merchant","Horse Merchant","{!}Town 7 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_8_horse_merchant","Horse Merchant","{!}Town 8 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_9_horse_merchant","Horse Merchant","{!}Town 9 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_leather_jerkin],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_10_horse_merchant","Horse Merchant","{!}Town 10 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_blue_dress,                itm_straw_hat],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_11_horse_merchant","Horse Merchant","{!}Town 11 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_nomad_armor],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_12_horse_merchant","Horse Merchant","{!}Town 12 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_leather_jacket],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_13_horse_merchant","Horse Merchant","{!}Town 13 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_coarse_tunic],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_14_horse_merchant","Horse Merchant","{!}Town 14 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_peasant_dress,             itm_headcloth],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_15_horse_merchant","Horse Merchant","{!}Town 15 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_nomad_armor],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_16_horse_merchant","Horse Merchant","{!}Town 16 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_leather_jacket],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_17_horse_merchant","Horse Merchant","{!}Town 17 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_coarse_tunic],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_18_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_peasant_dress,             itm_headcloth],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_19_horse_merchant","Horse Merchant","{!}Town 15 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_nomad_armor],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_20_horse_merchant","Horse Merchant","{!}Town 16 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_solarian_robe_a],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_21_horse_merchant","Horse Merchant","{!}Town 17 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_solarian_aketon_a],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_22_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_sarranid_common_dress_b,             itm_sarranid_felt_head_cloth_b],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],


#Town Mayors    #itm_courtly_outfit itm_gambeson itm_blue_gambeson itm_red_gambeson itm_nobleman_outfit itm_rich_outfit
  ["town_1_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_courtly_outfit], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["town_2_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_gambeson,     ],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_3_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_blue_gambeson], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_4_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_fur_coat],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_5_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_nobleman_outfit,     ],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_6_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_red_gambeson],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_7_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_rich_outfit,     ],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_8_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_red_gambeson],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_9_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_courtly_outfit], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_10_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     ],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_11_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_leather_jacket],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_12_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_red_gambeson], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_13_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_nobleman_outfit],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_14_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_blue_gambeson],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_15_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_leather_jacket],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_16_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_fur_coat], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_17_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_nobleman_outfit],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_18_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_blue_gambeson],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_19_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_solarian_robe_a],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_20_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_solarian_robe_a], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_21_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_solarian_robe_a],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_22_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_solarian_robe_a],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],


#Village stores
  ["village_1_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic,  itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_2_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_3_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_4_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic,  itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_5_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic],def_attrib|level(2),wp(20),knows_inventory_management_10,                      man_face_old_1, man_face_older_2],
  ["village_6_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_7_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_8_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic,  itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_9_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic,  itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,         man_face_old_1, man_face_older_2],
  ["village_10_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_11_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_12_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe,  itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_13_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_14_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_15_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic,  itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_16_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic,  itm_leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_17_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_18_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic,  itm_leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_19_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic,  itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_20_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic,  itm_leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_21_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe,  itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_22_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_23_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic,  itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_24_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_25_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat],def_attrib|level(2),wp(20),knows_inventory_management_10,                      man_face_old_1, man_face_older_2],
  ["village_26_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe,  itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_27_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic,  itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_28_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_29_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_30_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe,  itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_31_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_32_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_33_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe,  itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_34_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_35_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_36_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_37_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_38_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_39_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_40_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_41_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_42_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_43_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe,  itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_44_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_45_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_46_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_47_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_48_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_49_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_50_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_51_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe,  itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_52_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_53_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic,  itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_54_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_55_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_56_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe,  itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_57_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic,  itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_58_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_59_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_60_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe,  itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_61_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe,  itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_62_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_63_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic,  itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_64_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_65_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_66_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe,  itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_67_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic,  itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_68_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_69_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_70_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe,  itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_71_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe,  itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_72_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_73_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic,  itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_74_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_75_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_76_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat,  itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_77_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic,  itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_78_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_79_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_80_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe,  itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_81_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_82_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_83_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat,  itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_84_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_85_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_86_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_87_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_88_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_89_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_90_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_solarian_robe_a],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_91_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_solarian_robe_a],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_92_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_93_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_solarian_robe_a,  itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_94_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_solarian_robe_a, itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_95_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_solarian_aketon_a],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_96_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_97_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_solarian_robe_a],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_98_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_solarian_robe_a],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_99_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_100_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_solarian_robe_a],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_101_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_solarian_aketon_a],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_102_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_103_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_solarian_robe_a,  itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_104_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_105_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_solarian_aketon_a],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_106_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_107_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_108_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_solarian_aketon_a],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_109_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_solarian_aketon_a],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_110_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
# Place extra merchants before this point
  ["merchants_end","merchants_end","merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],

  #Used for player enterprises
  ["town_1_master_craftsman", "{!}Town 1 Craftsman", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_2_master_craftsman", "{!}Town 2 Craftsman", "{!}Town 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_padded_leather,     ],   def_attrib|level(2),wp(20),knows_common, 0x0000000f010811c92d3295e46a96c72300000000001f5a980000000000000000],
  ["town_3_master_craftsman", "{!}Town 3 Craftsman", "{!}Town 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic], def_attrib|level(2),wp(20),knows_common, 0x000000001b083203151d2ad5648e52b400000000001b172e0000000000000000],
  ["town_4_master_craftsman", "{!}Town 4 Craftsman", "{!}Town 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron],     def_attrib|level(2),wp(20),knows_common, 0x000000001a10114f091b2c259cd4c92300000000000228dd0000000000000000],
  ["town_5_master_craftsman", "{!}Town 5 Craftsman", "{!}Town 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     ],   def_attrib|level(2),wp(20),knows_common, 0x000000000d1044c578598cd92b5256db00000000001f23340000000000000000],
  ["town_6_master_craftsman", "{!}Town 6 Craftsman", "{!}Town 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron],   def_attrib|level(2),wp(20),knows_common, 0x000000001f046285493eaf1b048abcdb00000000001a8aad0000000000000000],
  ["town_7_master_craftsman", "{!}Town 7 Craftsman", "{!}Town 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     ],   def_attrib|level(2),wp(20),knows_common, 0x000000002b0052c34c549225619356d400000000001cc6e60000000000000000],
  ["town_8_master_craftsman", "{!}Town 8 Craftsman", "{!}Town 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron],   def_attrib|level(2),wp(20),knows_common, 0x0000000fdb0c20465b6e51e8a12c82d400000000001e148c0000000000000000],
  ["town_9_master_craftsman", "{!}Town 9 Craftsman", "{!}Town 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic], def_attrib|level(2),wp(20),knows_common, 0x00000009f7005246071db236e296a45300000000001a8b0a0000000000000000],
  ["town_10_master_craftsman", "{!}Town 10 Craftsman", "{!}Town 10 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     ],     def_attrib|level(2),wp(20),knows_common, 0x00000009f71012c2456a921aa379321a000000000012c6d90000000000000000],
  ["town_11_master_craftsman", "{!}Town 11 Craftsman", "{!}Town 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron],   def_attrib|level(2),wp(20),knows_common, 0x00000009f308514428db71b9ad70b72400000000001dc9140000000000000000],
  ["town_12_master_craftsman", "{!}Town 12 Seneschal", "{!}Town 12 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_coarse_tunic], def_attrib|level(2),wp(20),knows_common, 0x00000009e90825863853a5b91cd71a5b00000000000598db0000000000000000],
  ["town_13_master_craftsman", "{!}Town 13 Seneschal", "{!}Town 13 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     ],   def_attrib|level(2),wp(20),knows_common, 0x00000009fa0c708f274c8eb4c64e271300000000001eb69a0000000000000000],
  ["town_14_master_craftsman", "{!}Town 14 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron],     def_attrib|level(2),wp(20),knows_common, 0x00000007590c3206155c8b475a4e439a00000000001f489a0000000000000000],
  ["town_15_master_craftsman", "{!}Town 15 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron],     def_attrib|level(2),wp(20),knows_common, 0x00000007440022d04b2c6cb7d3723d5a00000000001dc90a0000000000000000],
  ["town_16_master_craftsman", "{!}Town 16 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron],     def_attrib|level(2),wp(20),knows_common, 0x00000007680c3586054b8e372e4db65c00000000001db7230000000000000000],
  ["town_17_master_craftsman", "{!}Town 17 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron],     def_attrib|level(2),wp(20),knows_common, 0x0000000766046186591b564cec85d2e200000000001e4cea0000000000000000],
  ["town_18_master_craftsman", "{!}Town 18 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron],     def_attrib|level(2),wp(20),knows_common, 0x0000000e7e0075523a6aa9b6da61e8dd00000000001d96d30000000000000000],
  ["town_19_master_craftsman", "{!}Town 19 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_solarian_robe_a],     def_attrib|level(2),wp(20),knows_common, 0x000000002408314852a432e88aaa42e100000000001e284e0000000000000000],
  ["town_20_master_craftsman", "{!}Town 20 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_solarian_aketon_a],     def_attrib|level(2),wp(20),knows_common, 0x000000001104449136e44cbd1c9352bc000000000005e8d10000000000000000],
  ["town_21_master_craftsman", "{!}Town 21 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_solarian_robe_a],     def_attrib|level(2),wp(20),knows_common, 0x00000000131032d3351c6e43226ec96c000000000005b5240000000000000000],
  ["town_22_master_craftsman", "{!}Town 22 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_solarian_aketon_a],     def_attrib|level(2),wp(20),knows_common, 0x00000000200c658a5723b1a3148dc455000000000015ab920000000000000000],
  
  
  
# Chests
  ["zendar_chest","{!}Zendar Chest","{!}Zendar Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,
   [],def_attrib|level(18),wp(60),knows_common, 0],
  ["tutorial_chest_1","{!}Melee Weapons Chest","{!}Melee Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_tutorial_sword, itm_tutorial_axe, itm_tutorial_spear, itm_tutorial_club, itm_tutorial_battle_axe],def_attrib|level(18),wp(60),knows_common, 0],
  ["tutorial_chest_2","{!}Ranged Weapons Chest","{!}Ranged Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_tutorial_short_bow, itm_tutorial_arrows, itm_tutorial_crossbow, itm_tutorial_bolts, itm_tutorial_throwing_daggers],def_attrib|level(18),wp(60),knows_common, 0],
  ["bonus_chest_1","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_strange_armor,itm_strange_short_sword],def_attrib|level(18),wp(60),knows_common, 0],
  ["bonus_chest_2","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_strange_boots,itm_strange_sword],def_attrib|level(18),wp(60),knows_common, 0],
  ["bonus_chest_3","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_strange_helmet,itm_strange_great_sword],def_attrib|level(18),wp(60),knows_common, 0],

  # New chests
  ["bonus_chest_4", "{!}Bonus Chest", "{!}Bonus Chest", tf_hero|tf_inactive, 0, reserved, fac_neutral, [], def_attrib|level(18), wp(60), knows_common, 0],
  ["bonus_chest_5", "{!}Bonus Chest", "{!}Bonus Chest", tf_hero|tf_inactive, 0, reserved, fac_neutral, [itm_black_helmet, itm_axe_crusader_1], def_attrib|level(18), wp(60), knows_common, 0],

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

# Add Extra Quest NPCs below this point  

  ["local_merchant","Local Merchant","Local Merchants",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["tax_rebel","Peasant Rebel","Peasant Rebels",tf_guarantee_armor,0,reserved,fac_commoners,
   [itm_cleaver,itm_knife,itm_pitch_fork,itm_sickle,itm_club,itm_stones,itm_leather_cap,itm_felt_hat,itm_felt_hat,itm_linen_tunic,itm_coarse_tunic],
   def_attrib|level(4),wp(60),knows_common,vaegir_face1, vaegir_face2],
  ["trainee_peasant","Peasant","Peasants",tf_guarantee_armor,0,reserved,fac_commoners,
   [itm_cleaver,itm_knife,itm_pitch_fork,itm_sickle,itm_club,itm_stones,itm_leather_cap,itm_felt_hat,itm_felt_hat,itm_linen_tunic,itm_coarse_tunic],
   def_attrib|level(4),wp(60),knows_common,vaegir_face1, vaegir_face2],
  ["fugitive","Nervous Man","Nervous Men",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_short_tunic,itm_linen_tunic,itm_coarse_tunic, itm_tabard, itm_leather_vest,     itm_fur_hat, itm_leather_cap, itm_sword_medieval_b, itm_throwing_daggers],
   def_attrib|str_24|agi_25|level(26),wp(180),knows_common|knows_power_throw_6|knows_power_strike_6|knows_ironflesh_9,man_face_middle_1, man_face_old_2],
   
  ["belligerent_drunk","Belligerent Drunk","Belligerent Drunks",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_short_tunic,itm_linen_tunic,itm_coarse_tunic, itm_tabard, itm_leather_vest,     itm_fur_hat, itm_leather_cap, itm_sword_viking_1],
   def_attrib|str_20|agi_8|level(15),wp(120),knows_common|knows_power_strike_2|knows_ironflesh_9,    bandit_face1, bandit_face2],

  ["hired_assassin","Hired Assassin","Hired Assassin",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners, #they look like belligerent drunks
   [itm_short_tunic,itm_linen_tunic,itm_coarse_tunic, itm_tabard, itm_leather_vest,     itm_fur_hat, itm_leather_cap, itm_sword_viking_1],
   def_attrib|str_20|agi_16|level(20),wp(180),knows_common|knows_power_strike_5|knows_ironflesh_3,    bandit_face1, bandit_face2],

  ["fight_promoter","Rough-Looking Character","Rough-Looking Character",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_short_tunic,itm_linen_tunic,itm_coarse_tunic, itm_tabard, itm_leather_vest,     itm_fur_hat, itm_leather_cap, itm_sword_viking_1],
   def_attrib|str_20|agi_16|level(20),wp(180),knows_common|knows_power_strike_5|knows_ironflesh_3,    bandit_face1, bandit_face2],

   
   
  ["spy","Ordinary Townsman","Ordinary Townsmen", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
   [itm_sword_viking_1,itm_leather_jerkin,itm_courser,itm_leather_gloves],
   def_attrib|agi_11|level(20),wp(130),knows_common,man_face_middle_1, man_face_older_2],
   
  ["spy_partner","Unremarkable Townsman","Unremarkable Townsmen", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
   [itm_sword_medieval_b,itm_leather_jerkin,itm_courser,itm_leather_gloves],
   def_attrib|agi_11|level(10),wp(130),knows_common,vaegir_face1, vaegir_face2],

   ["nurse_for_lady","Nurse","Nurse",tf_female|tf_guarantee_armor,0,reserved,fac_commoners,
   [itm_robe, itm_black_hood],
   def_attrib|level(4),wp(60),knows_common,woman_face_1, woman_face_2],   
   ["temporary_minister","Minister","Minister",tf_guarantee_armor|tf_guarantee_boots,0,reserved,fac_commoners,
   [itm_rich_outfit],
   def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_older_2],   
   
  ["quick_battle_6_player", "{!}quick_battle_6_player", "{!}quick_battle_6_player", tf_hero, 0, reserved,  fac_player_faction, [itm_padded_cloth, itm_skullcap, itm_sword_medieval_b,  itm_crossbow, itm_bolts, itm_plate_covered_round_shield],    knight_attrib_1,wp(130),knight_skills_1, 0x000000000008010b01f041a9249f65fd],

#Multiplayer ai troops
  ["silver_rose_trained_crossbowman_multiplayer_ai","Swadian Crossbowman","Swadian Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_bolts,itm_crossbow,itm_sword_medieval_a,itm_tab_shield_heater_b,
    itm_leather_jerkin,itm_leather_armor,itm_iron_crown_nasal_a],
   def_attrib|level(19),wp_melee(90)|wp_crossbow(100),knows_common|knows_ironflesh_4|knows_athletics_6|knows_shield_5|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
  ["silver_rose_infantry_multiplayer_ai","Swadian Infantry","Swadian Infantry",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_1,
   [itm_pike,itm_bastard_sword_a,itm_tab_shield_heater_c,
    itm_studded_leather_coat,itm_flat_topped_helmet],
   def_attrib|level(19),wp_melee(105),knows_common|knows_ironflesh_5|knows_shield_4|knows_power_strike_5|knows_athletics_4,swadian_face_middle_1, swadian_face_old_2],
  ["silver_rose_man_at_arms_multiplayer_ai","Swadian Man at Arms","Swadian Men at Arms",tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac_kingdom_1,
   [itm_lance,itm_bastard_sword_a,itm_tab_shield_heater_cav_a,
    itm_m_celestial_breastplate_heavy_b,itm_elen_nasal_padded_b,itm_hunter],
   def_attrib|level(19),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_4|knows_shield_4|knows_power_strike_4|knows_athletics_1,swadian_face_young_1, swadian_face_old_2],
  ["chornovalley_longbowman_multiplayer_ai","Vaegir Archer","Vaegir Archers",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_arrows,itm_scimitar,itm_nomad_bow,
    itm_leather_vest,itm_spiked_helmet,itm_nomad_cap],
   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_4|knows_power_draw_5|knows_athletics_6|knows_shield_2,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_spearman_multiplayer_ai","Vaegir Spearman","Vaegir Spearmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_2,
   [itm_padded_leather,itm_spiked_helmet,itm_nomad_cap, itm_spear, itm_tab_shield_kite_b, itm_mace_1, itm_javelin],
   def_attrib|str_12|level(19),wp_melee(90),knows_ironflesh_4|knows_athletics_6|knows_power_throw_3|knows_power_strike_3|knows_shield_2,vaegir_face_young_1, vaegir_face_older_2],
  ["chornovalley_horseman_multiplayer_ai","Vaegir Horseman","Vaegir Horsemen",tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac_kingdom_2,
   [itm_battle_axe,itm_scimitar,itm_lance,itm_tab_shield_kite_cav_a,
     itm_studded_leather_coat,itm_lamellar_vest,itm_spiked_helmet,itm_saddle_horse],
   def_attrib|level(19),wp(100),knows_riding_4|knows_ironflesh_4|knows_power_strike_4|knows_shield_3,vaegir_face_young_1, vaegir_face_older_2],
  ["khergit_dismounted_lancer_multiplayer_ai","Khergit Dismounted Lancer","Khergit Dismounted Lancer",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_3,
   [itm_sword_khergit_4,itm_spiked_mace,itm_one_handed_war_axe_b,itm_one_handed_war_axe_a,itm_hafted_blade_a,itm_hafted_blade_b,itm_heavy_lance,itm_lance,
    itm_khergit_cavalry_helmet,itm_khergit_war_helmet,itm_lamellar_vest_khergit,itm_tribal_warrior_outfit,itm_leather_gloves,itm_mail_mittens,itm_tab_shield_small_round_b,itm_tab_shield_small_round_c],
   def_attrib|level(19),wp(100),knows_riding_4|knows_power_strike_1|knows_power_draw_4|knows_power_throw_2|knows_ironflesh_1|knows_horse_archery_1,khergit_face_middle_1, khergit_face_older_2],
  ["celestial_sergeant_multiplayer_ai","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_khergit_3,itm_khergit_bow,itm_khergit_arrows,itm_tab_shield_small_round_b,
    itm_khergit_cavalry_helmet,itm_tribal_warrior_outfit,itm_steppe_horse],
   def_attrib|level(19),wp(90)|wp_archery(100),knows_riding_6|knows_power_draw_5|knows_shield_2|knows_horse_archery_5,khergit_face_middle_1, khergit_face_older_2],
  ["celestial_lancer_multiplayer_ai","Khergit Lancer","Khergit Lancers",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_3,
   [itm_sword_khergit_4,itm_spiked_mace,itm_one_handed_war_axe_b,itm_one_handed_war_axe_a,itm_hafted_blade_a,itm_hafted_blade_b,itm_heavy_lance,itm_lance,
    itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_khergit_war_helmet,itm_lamellar_vest_khergit,itm_chornovalley_heavy_mail_b,itm_leather_gloves,itm_mail_mittens,itm_scale_gauntlets,itm_tab_shield_small_round_b,itm_tab_shield_small_round_c,itm_courser],
   def_attrib|level(19),wp(100),knows_riding_7|knows_power_strike_2|knows_power_draw_4|knows_power_throw_2|knows_ironflesh_1|knows_horse_archery_1,khergit_face_middle_1, khergit_face_older_2],
  ["iron_crown_vetaran_multiplayer_ai","Nord Footman","Nord Footmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_4,
   [itm_sword_viking_2,itm_one_handed_battle_axe_b,itm_two_handed_axe,itm_tab_shield_round_d,itm_throwing_axes,
    itm_mail_coif,itm_iron_crown_nasal_b,itm_mail_hauberk,itm_leather_gloves],
   def_attrib|level(19),wp(130),knows_ironflesh_3|knows_power_strike_5|knows_power_throw_3|knows_athletics_5|knows_shield_3,nord_face_young_1, nord_face_older_2],
  ["nord_scout_multiplayer_ai","Nord Scout","Nord Scouts",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_javelin,itm_sword_viking_1,itm_two_handed_axe,itm_spear,itm_tab_shield_round_a,
    itm_skullcap,itm_iron_crown_scullcap_a,itm_leather_jerkin,itm_saddle_horse],
   def_attrib|level(19),wp(100),knows_riding_5|knows_ironflesh_2|knows_power_strike_2|knows_shield_1|knows_horse_archery_2|knows_power_throw_3,nord_face_young_1, nord_face_older_2],
  ["iron_crown_trained_skirmisher_multiplayer_ai","Nord Archer","Nord Archers",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_arrows,itm_two_handed_axe,itm_sword_viking_2,itm_short_bow,
    itm_leather_jerkin,itm_blue_tunic,itm_footman_helmet,itm_leather_cap],
   def_attrib|str_11|level(19),wp_melee(80)|wp_archery(110),knows_ironflesh_4|knows_power_strike_2|knows_shield_1|knows_power_draw_5|knows_athletics_6,nord_face_young_1, nord_face_old_2],
  ["alpine_veteran_crossbowman_multiplayer_ai","Rhodok Crossbowman","Rhodok Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_fighting_pick,itm_club_with_spike_head,itm_maul,itm_tab_shield_pavise_c,itm_heavy_crossbow,itm_bolts,
    itm_leather_cap,itm_padded_leather],
   def_attrib|level(19),wp_melee(100)|wp_crossbow(120),knows_common|knows_ironflesh_4|knows_shield_5|knows_power_strike_3|knows_athletics_6,rhodok_face_middle_1, rhodok_face_older_2],
  ["alpine_veteran_spearman_multiplayer_ai","Rhodok Spearman","Rhodok Spearmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_5,
   [itm_ashwood_pike,itm_war_spear,itm_pike,itm_club_with_spike_head,itm_sledgehammer,itm_tab_shield_pavise_c,itm_sword_medieval_a,
    itm_leather_cap,itm_m_hauberk_navy_c,itm_ragged_outfit],
   def_attrib|level(19),wp(115),knows_common|knows_ironflesh_5|knows_shield_3|knows_power_strike_4|knows_athletics_3,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_scout_multiplayer_ai","Rhodok Scout","Rhodok Scouts",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_5,
   #TODO: Change weapons, copied from Nord Scout
   [itm_sword_medieval_a,itm_tab_shield_heater_cav_a,itm_light_lance,itm_skullcap,itm_aketon_green,
    itm_ragged_outfit,itm_saddle_horse],
   def_attrib|level(19),wp(100),knows_riding_5|knows_ironflesh_2|knows_power_strike_2|knows_shield_1|knows_horse_archery_2|knows_power_throw_3,rhodok_face_young_1, rhodok_face_older_2],
  ["solarian_infantry_multiplayer_ai","Sarranid Infantry","Sarranid Infantries",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_6,
   [itm_solarian_armor_scale_a,itm_solarian_helmet_warrior_a,itm_arabian_sword_b,itm_mace_3,itm_spear,itm_tab_shield_kite_c],
   def_attrib|level(20),wp_melee(105),knows_common|knows_riding_3|knows_ironflesh_2|knows_shield_3,swadian_face_middle_1, swadian_face_old_2],
  ["solarian_archer_multiplayer_ai","Sarranid Archer","Sarranid Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [itm_arrows,itm_nomad_bow,itm_arabian_sword_a,itm_solarian_mail_vest_a,itm_solarian_helmet_a,itm_solarian_turban_b,itm_solarian_turban_c],
   def_attrib|level(19),wp_melee(90)|wp_archery(100),knows_common|knows_riding_2|knows_ironflesh_1,swadian_face_young_1, swadian_face_old_2],
  ["solarian_horseman_multiplayer_ai","Sarranid Horseman","Sarranid Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_6,
   [itm_lance,itm_arabian_sword_b,itm_scimitar_b,itm_mace_4,itm_tab_shield_small_round_b,
    itm_solarian_armor_scale_a,itm_solarian_helmet_warrior_a,itm_courser,itm_hunter],
   def_attrib|level(20),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],

   
   
#Multiplayer troops (they must have the base items only, nothing else)
  ["silver_rose_trained_crossbowman_multiplayer","Swadian Crossbowman","Swadian Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_bolts,itm_crossbow,itm_sword_medieval_b_small,itm_tab_shield_heater_a,itm_red_shirt],
   str_14 | agi_15 |def_attrib_multiplayer|level(19),wpe(90,60,180,90),knows_common_multiplayer|knows_ironflesh_2|knows_athletics_4|knows_shield_5|knows_power_strike_2|knows_riding_1,swadian_face_young_1, swadian_face_old_2],
  ["silver_rose_infantry_multiplayer","Swadian Infantry","Swadian Infantry",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_sword_medieval_a,itm_tab_shield_heater_a,itm_red_tunic],
   str_15 | agi_15 |def_attrib_multiplayer|level(20),wpex(105,130,110,40,60,110),knows_common_multiplayer|knows_ironflesh_5|knows_shield_4|knows_power_strike_4|knows_power_throw_2|knows_athletics_6|knows_riding_1,swadian_face_middle_1, swadian_face_old_2],
  ["silver_rose_man_at_arms_multiplayer","Swadian Man at Arms","Swadian Men at Arms",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_lance,itm_sword_medieval_a,itm_tab_shield_heater_a,
    itm_red_tunic,itm_saddle_horse],
   str_14 | agi_16 |def_attrib_multiplayer|level(20),wp_melee(110),knows_common_multiplayer|knows_riding_5|knows_ironflesh_3|knows_shield_2|knows_power_throw_2|knows_power_strike_3|knows_athletics_3,swadian_face_young_1, swadian_face_old_2],
#  ["swadian_mounted_crossbowman_multiplayer","Swadian Mounted Crossbowman","Swadian Mounted Crossbowmen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_1,
#   [itm_bolts,itm_light_crossbow,itm_tab_shield_heater_cav_a,itm_bastard_sword_a,
#    itm_red_shirt,itm_saddle_horse],
#   def_attrib_multiplayer|level(20),wp_melee(100)|wp_crossbow(120),knows_common_multiplayer|knows_riding_4|knows_shield_3|knows_ironflesh_3|knows_horse_archery_2|knows_power_strike_3|knows_athletics_2|knows_shield_2,swadian_face_young_1, swadian_face_old_2],
  ["chornovalley_longbowman_multiplayer","Vaegir Archer","Vaegir Archers",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_arrows,itm_mace_1,itm_nomad_bow,
    itm_linen_tunic],
   str_14 | agi_14 |def_attrib_multiplayer|str_12|level(19),wpe(80,150,60,80),knows_common_multiplayer|knows_ironflesh_2|knows_power_draw_7|knows_athletics_3|knows_shield_2|knows_riding_1,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_spearman_multiplayer","Vaegir Spearman","Vaegir spearman",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_spear, itm_tab_shield_kite_a, itm_mace_1,
    itm_linen_tunic],
   str_15 | agi_15 |def_attrib_multiplayer|str_12|level(19),wpex(110,100,130,30,50,120),knows_common_multiplayer|knows_ironflesh_4|knows_shield_2|knows_power_throw_3|knows_power_strike_4|knows_athletics_6|knows_riding_1,vaegir_face_young_1, vaegir_face_older_2],
  ["chornovalley_horseman_multiplayer","Vaegir Horseman","Vaegir Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_scimitar,itm_lance,itm_tab_shield_kite_cav_a,
    itm_linen_tunic,itm_saddle_horse],
   str_16 | agi_15 |def_attrib_multiplayer|level(19),wpe(110,90,60,110),knows_common_multiplayer|knows_riding_5|knows_ironflesh_4|knows_power_strike_3|knows_shield_3|knows_power_throw_4|knows_horse_archery_1,vaegir_face_young_1, vaegir_face_older_2],
  ["celestial_sergeant_multiplayer","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_khergit_1,itm_nomad_bow,itm_arrows,
    itm_khergit_armor,itm_leather_steppe_cap_a,itm_steppe_horse],
   str_15 | agi_18 |def_attrib_multiplayer|level(21),wpe(70,142,60,100),knows_common_multiplayer|knows_riding_2|knows_power_draw_5|knows_horse_archery_3|knows_athletics_3|knows_shield_1,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_infantry_multiplayer","Khergit Infantry","Khergit Infantries",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_khergit_1,itm_spear,itm_tab_shield_small_round_a,
    itm_steppe_armor,itm_leather_gloves],
   str_14 | agi_15 |def_attrib_multiplayer|level(19),wp(110),knows_common_multiplayer|knows_ironflesh_3|knows_power_throw_3|knows_shield_4|knows_power_strike_3|knows_athletics_6|knows_riding_1,khergit_face_middle_1, khergit_face_older_2],
  ["celestial_lancer_multiplayer","Khergit Lancer","Khergit Lancers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_khergit_1,itm_lance,itm_tab_shield_small_round_a,
    itm_khergit_armor,itm_leather_steppe_cap_a,itm_steppe_horse],
   str_15 | agi_14 |def_attrib_multiplayer|level(21),wp(115),knows_common_multiplayer|knows_riding_6|knows_ironflesh_3|knows_power_throw_3|knows_shield_4|knows_power_strike_3|knows_athletics_4,khergit_face_middle_1, khergit_face_older_2],
  ["iron_crown_trained_skirmisher_multiplayer","Nord Archer","Nord Archers",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_arrows,itm_sword_viking_2_small,itm_short_bow,
    itm_blue_tunic],
   str_15 | agi_14 |def_attrib_multiplayer|str_11|level(15),wpe(90,150,60,80),knows_common_multiplayer|knows_ironflesh_2|knows_power_strike_2|knows_shield_3|knows_power_draw_5|knows_athletics_3|knows_riding_1,nord_face_young_1, nord_face_old_2],
  ["iron_crown_vetaran_multiplayer","Nord Huscarl","Nord Huscarls",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_sword_viking_1,itm_one_handed_war_axe_a,itm_tab_shield_round_a,
    itm_blue_tunic],
   str_17 | agi_15 |def_attrib_multiplayer|level(24),wpex(110,135,100,40,60,140),knows_common_multiplayer|knows_ironflesh_4|knows_power_strike_5|knows_power_throw_4|knows_athletics_6|knows_shield_3|knows_riding_1,nord_face_young_1, nord_face_older_2],
  ["nord_scout_multiplayer","Nord Scout","Nord Scouts",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_javelin,itm_sword_viking_1,itm_spear,itm_tab_shield_small_round_a,
    itm_blue_tunic,itm_saddle_horse],
   str_16 | agi_15 |def_attrib_multiplayer|level(19),wp(105),knows_common_multiplayer|knows_riding_6|knows_ironflesh_2|knows_power_strike_2|knows_shield_1|knows_horse_archery_3|knows_power_throw_3|knows_athletics_3,vaegir_face_young_1, vaegir_face_older_2],
  ["alpine_veteran_crossbowman_multiplayer","Rhodok Crossbowman","Rhodok Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_crossbow,itm_bolts,itm_fighting_pick,itm_tab_shield_pavise_a,
    itm_tunic_with_green_cape],
   str_16 | agi_15 |def_attrib_multiplayer|level(20),wpe(100,60,180,90),knows_common_multiplayer|knows_ironflesh_2|knows_shield_2|knows_power_strike_2|knows_athletics_4|knows_riding_1,rhodok_face_middle_1, rhodok_face_older_2],
  ["alpine_man_at_arms_multiplayer","Rhodok Sergeant","Rhodok Sergeants",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_fighting_pick,itm_tab_shield_pavise_a,itm_spear,
    itm_green_tunic],
   str_16 | agi_14 |def_attrib_multiplayer|level(20),wpex(110,100,140,30,50,110),knows_common_multiplayer|knows_ironflesh_4|knows_shield_5|knows_power_strike_4|knows_power_throw_1|knows_athletics_6|knows_riding_1,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_horseman_multiplayer","Rhodok Horseman","Rhodok Horsemen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_sword_medieval_a,itm_tab_shield_heater_cav_a, itm_light_lance, 
    itm_green_tunic,itm_saddle_horse],
   str_15 | agi_15 |def_attrib_multiplayer|level(20),wp(100),knows_common_multiplayer|knows_riding_4|knows_ironflesh_3|knows_shield_3|knows_power_strike_3|knows_power_throw_1|knows_athletics_3,rhodok_face_middle_1, rhodok_face_older_2],
  ["solarian_archer_multiplayer","Sarranid Archer","Sarranid Archers",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_arrows,itm_arabian_sword_a,itm_nomad_bow,
    itm_solarian_robe_a],
   str_15 | agi_16 |def_attrib_multiplayer|str_12|level(19),wpe(80,150,60,80),knows_common_multiplayer|knows_ironflesh_4|knows_power_draw_5|knows_athletics_3|knows_shield_2|knows_riding_1|knows_weapon_master_1,vaegir_face_young_1, vaegir_face_older_2],
  ["solarian_footman_multiplayer","Sarranid Footman","Sarranid footman",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_bamboo_spear, itm_tab_shield_kite_a, itm_arabian_sword_a,
    itm_solarian_robe_a],
   str_14 | agi_15 |def_attrib_multiplayer|str_12|level(19),wpex(110,100,130,30,50,120),knows_common_multiplayer|knows_ironflesh_4|knows_shield_2|knows_power_throw_3|knows_power_strike_4|knows_athletics_6|knows_riding_1,vaegir_face_young_1, vaegir_face_older_2],
  ["solarian_knight_multiplayer","Sarranid Mamluke","Sarranid Mamluke",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_arabian_sword_a,itm_lance,itm_tab_shield_small_round_a,
    itm_solarian_robe_a, itm_saddle_horse],
   str_15 | agi_14 |def_attrib_multiplayer|level(19),wpe(110,90,60,110),knows_common_multiplayer|knows_riding_5|knows_ironflesh_3|knows_power_strike_2|knows_shield_3|knows_power_throw_2|knows_weapon_master_1,vaegir_face_young_1, vaegir_face_older_2],


   ["multiplayer_end","{!}multiplayer_end","{!}multiplayer_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],
   
   #Player history array
  ["log_array_entry_type",            "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_entry_time",            "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_actor",                 "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_center_object",         "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_center_object_lord",    "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_center_object_faction", "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_troop_object",          "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_troop_object_faction",  "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_faction_object",        "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],

  ["quick_battle_troop_1","Sir Artorio of Nerpa","Sir Artorio of Nerpa", tf_hero,0,0,fac_kingdom_1, [itm_m_brigandine_a, itm_m_gauntlets_b,  itm_tab_shield_pavise_d, itm_throwing_spears, itm_german_poleaxe],str_30|agi_30|int_12|cha_12|level(55),wpex(400,300,500,200,200,350),knows_athletics_10|knows_shield_7|knows_weapon_master_7|knows_power_throw_8|knows_power_strike_9|knows_ironflesh_10,0x0000000e7f10400836db6db6db6ddbb600000000001db6db0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_2","Borato","Borato", tf_hero,0,0,fac_kingdom_1,[itm_m_brigandine_b, itm_m_gloves_a,  itm_tab_shield_heater_d, itm_italian_falchion, itm_sniper_crossbow, itm_steel_bolts], str_30|agi_30|int_11|cha_18|level(54),wpex(400,100,200,450,100,100),knows_athletics_10|knows_shield_10|knows_weapon_master_10|knows_power_strike_8|knows_ironflesh_8,0x000000097f1065c636db6db6db6ddbb600000000001db6db0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_3","Francisco","Francisco", tf_hero,0,0,fac_kingdom_1, [itm_m_knigh_helm_f, itm_shirt, itm_m_gauntlets_b, itm_tab_shield_heater_cav_b, itm_crusader_sword, itm_danish_greatsword, itm_heavy_lance, itm_mt_horse_c2], str_30|agi_30|int_11|cha_18|level(54),wpex(400,400,400,100,100,100),knows_athletics_10|knows_shield_10|knows_riding_10|knows_weapon_master_10|knows_power_strike_8|knows_ironflesh_8,0x000000000010014536db6db6db6ddbb600000000001db6db0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_4","Elindero the Tower","Elindero the Tower", tf_hero,0,0,fac_kingdom_1, [itm_shirt, itm_m_gauntlets_b, itm_steel_shield, itm_side_sword, itm_english_bill, itm_mt_horse_c2], str_30|agi_30|int_11|cha_18|level(54),wpex(400,200,450,100,100,100),knows_athletics_10|knows_shield_10|knows_weapon_master_10|knows_power_strike_8|knows_ironflesh_8,0x0000000f3f10219436db6db6db6ddbb600000000001db6db0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_5","Sir Skolle","Sir Skolle", tf_hero,0,0,fac_kingdom_1, [itm_shirt, itm_m_gauntlets_a, itm_plate_covered_round_shield, itm_longsword], str_30|agi_30|int_11|cha_18|level(54),wpex(600,200,200,100,100,100),knows_athletics_10|knows_shield_10|knows_weapon_master_10|knows_power_strike_8|knows_ironflesh_8,0x0000000fff10321336db6db6db6ddbb600000000001db6db0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_6","Xan","Xan", tf_hero,0,0,fac_kingdom_1, [itm_steppe_horse, itm_eastern_scale_gloves_b, itm_hairako_mail_helmet_d, itm_hairako_full_mail_b, itm_strong_bow, itm_barbed_arrows, itm_plate_covered_round_shield], str_30|agi_30|int_11|cha_18|level(54),wpex(450,200,200,450,100,100),knows_athletics_6|knows_shield_10|knows_weapon_master_10|knows_power_strike_8|knows_ironflesh_8|knows_riding_10,0x0000000fff08338536db6db6db6ddb6d00000000001db6db0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_7","Gylas","Gylas", tf_hero,0,0,fac_kingdom_1, [itm_m_gloves_a,  itm_m_coif_alternate_a, itm_war_bow, itm_bodkin_arrows, itm_bodkin_arrows, itm_espada_eslavona_b, itm_m_brigandine_c], str_30|agi_30|int_11|cha_18|level(54),wpex(240,200,200,500,100,100),knows_athletics_6|knows_shield_5|knows_weapon_master_10|knows_power_strike_8|knows_ironflesh_8|knows_power_draw_10,0x0000000fff08338536db6db6db6ddb6d00000000001db6db0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_8","Hamart Boley","Hamart Boley", tf_hero,0,0,fac_kingdom_1, [itm_m_gloves_a,  itm_war_bow, itm_barbed_arrows, itm_side_sword, itm_m_elen_vest_e, itm_mt_hood_a3], str_30|agi_30|int_11|cha_18|level(54),wpex(240,200,200,500,100,100),knows_athletics_10|knows_shield_5|knows_weapon_master_10|knows_power_strike_8|knows_ironflesh_8|knows_power_draw_10,0x00000006ff00219436db6db6db6dff6500000000001db6db0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_9","Eward","Eward", tf_hero,0,0,fac_kingdom_1, [ itm_heavy_throwing_axes, itm_tab_shield_round_e], str_30|agi_30|int_11|cha_18|level(56),wpex(240,500,100,100,100,400),knows_athletics_10|knows_shield_5|knows_weapon_master_10|knows_power_strike_10|knows_ironflesh_10,0x0000000ff108330906db6db6db6ddb6c00000000001db6f80000000000000000, swadian_face_old_2],
  ["quick_battle_troop_10","Axlerd Githal","Axlerd Githal", tf_hero,0,0,fac_kingdom_1, [], str_30|agi_30|int_11|cha_18|level(56),wpex(500,500,100,100,100,100),knows_athletics_10|knows_shield_5|knows_weapon_master_10|knows_power_strike_10|knows_ironflesh_10,0x0000000fff08434906076c3a1b1dffff00000000001db6380000000000000000, swadian_face_old_2],
  ["quick_battle_troop_11","Ezzenmer","Ezzenmer", tf_hero,0,0,fac_kingdom_1, [], str_30|agi_30|int_11|cha_18|level(69),wpex(0,900,0,0,0,0),knows_athletics_10|knows_weapon_master_10|knows_power_strike_10|knows_ironflesh_10,0x0000000fff08738006056c3a1b1dffff00000000001db6380000000000000000, swadian_face_old_2],
  ["quick_battle_troop_12","Bronze Ganaka","Bronze Ganaka", tf_hero,0,0,fac_kingdom_1, [itm_battle_fork,  itm_m_gloves_a], str_30|agi_30|int_11|cha_18|level(54),wpex(0,0,900,0,0,0),knows_athletics_10|knows_weapon_master_10|knows_power_strike_10|knows_ironflesh_10,0x0000000e7f08244036db6db6db6edd6d00000000001db6f30000000000000000, swadian_face_old_2],

  ["quick_battle_troops_end","{!}quick_battle_troops_end","{!}quick_battle_troops_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],

  ["tutorial_fighter_1","Novice Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_linen_tunic],
   def_attrib|level(1),wp_melee(10),knows_athletics_1|knows_ironflesh_2|knows_shield_2,0x000000088c1073144252b1929a85569300000000000496a50000000000000000, vaegir_face_older_2],
  ["tutorial_fighter_2","Novice Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_green_tunic],
   def_attrib|level(1),wp_melee(10),knows_athletics_1|knows_ironflesh_2|knows_shield_2,0x000000088b08049056ab56566135c46500000000001dda1b0000000000000000, vaegir_face_older_2],
  ["tutorial_fighter_3","Regular Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_green_tunic],
   def_attrib|level(9),wp_melee(50),knows_athletics_1|knows_ironflesh_2|knows_shield_2,0x00000008bc00400654914a3b0d0de74d00000000001d584e0000000000000000, vaegir_face_older_2],
  ["tutorial_fighter_4","Veteran Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_linen_tunic],
   def_attrib|level(16),wp_melee(110),knows_athletics_1|knows_ironflesh_3|knows_power_strike_2|knows_shield_2,0x000000089910324a495175324949671800000000001cd8ab0000000000000000, vaegir_face_older_2],
  ["tutorial_archer_1","Archer","Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_2,
   [itm_leather_jerkin,itm_leather_vest,itm_chornovalley_footman_helmet_a,itm_chornovalley_skullcap_helmet_b,itm_chornovalley_skullcap_helmet_a,itm_nomad_cap],
   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_athletics_2|knows_power_throw_1,vaegir_face_young_1, vaegir_face_older_2],
  ["tutorial_master_archer","Archery Trainer","Archery Trainer",tf_hero,0,0,fac_kingdom_2,
   [itm_linen_tunic],
   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_athletics_2|knows_power_throw_1,0x0000000ea508540642f34d461d2d54a300000000001d5d9a0000000000000000, vaegir_face_older_2],
  ["tutorial_rider_1","Rider","{!}Vaegir Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_green_tunic,itm_hunter, itm_saddle_horse,itm_leather_gloves],
   def_attrib|level(24),wp(130),knows_riding_4|knows_shield_2|knows_ironflesh_3|knows_power_strike_2,vaegir_face_middle_1, vaegir_face_older_2],
  ["tutorial_rider_2","Horse archer","{!}Khergit Horse Archers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac_kingdom_3,
   [itm_tribal_warrior_outfit,itm_nomad_robe,itm_tab_shield_small_round_a,itm_steppe_horse],
   def_attrib|level(14),wp(80)|wp_archery(110),knows_riding_5|knows_power_draw_3|knows_ironflesh_1|knows_horse_archery_4|knows_power_throw_1,khergit_face_young_1, khergit_face_older_2],
  ["tutorial_master_horseman","Riding Trainer","Riding Trainer",tf_hero,0,0,fac_kingdom_2,
   [itm_leather_vest],
   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_athletics_2|knows_power_throw_1,0x0000000ea0084140478a692894ba185500000000001d4af30000000000000000, vaegir_face_older_2],
   
  ["swadian_merchant", "Merchant of Praven", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_4, [itm_sword_two_handed_a, itm_courtly_outfit], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["vaegir_merchant", "Merchant of Reyvadin", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_5, [itm_sword_two_handed_a, itm_nobleman_outfit], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["khergit_merchant", "Merchant of Tulga", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_1, [itm_sword_two_handed_a, itm_red_gambeson], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["nord_merchant", "Merchant of Sargoth", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_2, [itm_sword_two_handed_a, itm_red_gambeson], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["rhodok_merchant", "Merchant of Jelkala", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_3, [itm_sword_two_handed_a, itm_leather_jerkin], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["sarranid_merchant", "Merchant of Shariz", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_6, [itm_sword_two_handed_a, itm_solarian_robe_a], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],       
  ["startup_merchants_end","startup_merchants_end","startup_merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],
 
  ["sea_raider_leader","Sea Raider Captain","Sea Raider Captains",tf_hero|tf_guarantee_all_wo_ranged,0,0,fac_outlaws,
   [itm_arrows,itm_sword_viking_1,itm_sword_viking_2,itm_fighting_axe,itm_battle_axe,itm_spear,itm_nordic_shield,itm_nordic_shield,itm_nordic_shield,itm_wooden_shield,itm_long_bow,itm_javelin,itm_throwing_axes,
    itm_mail_coif,itm_mail_coif,itm_footman_helmet,itm_stormguard_hauberk_a,itm_m_hauberk_navy_c,itm_mail_hauberk],
   def_attrib|level(24),wp(110),knows_ironflesh_2|knows_power_strike_2|knows_power_draw_3|knows_power_throw_2|knows_riding_1|knows_athletics_2,nord_face_young_1, nord_face_old_2],

  ["looter_leader","Robber","Looters",tf_hero,0,0,fac_outlaws,
   [itm_hatchet,itm_club,itm_butchering_knife,itm_falchion,itm_rawhide_coat,itm_stones,itm_nomad_armor,itm_nomad_armor,itm_woolen_cap,itm_woolen_cap],
   def_attrib|level(4),wp(20),knows_common,0x00000001b80032473ac49738206626b200000000001da7660000000000000000, bandit_face2],
   
  ["bandit_leaders_end","bandit_leaders_end","bandit_leaders_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],   
  
  ["relative_of_merchant", "Merchant's Brother", "{!}Prominent",tf_hero,0,0,fac_kingdom_2,
   [itm_linen_tunic],
   def_attrib|level(1),wp_melee(10),knows_athletics_1|knows_ironflesh_2|knows_shield_2, 0x00000000320410022d2595495491afa400000000001d9ae30000000000000000, mercenary_face_2],   
   
  ["relative_of_merchants_end","relative_of_merchants_end","relative_of_merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],     

  ["silver_rose_trained_crossbowman_multiplayer_coop_tier_1","Swadian Crossbowman","Swadian Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_hunting_crossbow,itm_bolts,itm_fighting_pick,itm_tab_shield_heater_a,itm_arming_cap,itm_padded_cloth],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["silver_rose_infantry_multiplayer_coop_tier_1","Swadian Infantry","Swadian Infantry",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_spiked_club,itm_tab_shield_heater_b,itm_felt_hat,itm_leather_apron],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["silver_rose_man_at_arms_multiplayer_coop_tier_1","Swadian Man at Arms","Swadian Men at Arms",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_light_lance,itm_sword_medieval_b_small,itm_tab_shield_heater_a,itm_leather_cap,itm_leather_gloves,itm_padded_cloth,itm_warhorse],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["chornovalley_longbowman_multiplayer_coop_tier_1","Vaegir Archer","Vaegir Archers",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_arrows,itm_axe,itm_hunting_bow,itm_linen_tunic],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["vaegir_spearman_multiplayer_coop_tier_1","Vaegir Spearman","Vaegir spearman",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_tab_shield_kite_a, itm_axe,itm_rawhide_coat],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["chornovalley_horseman_multiplayer_coop_tier_1","Vaegir Horseman","Vaegir Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_spear,itm_tab_shield_kite_cav_a,itm_linen_tunic,itm_hunter],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["celestial_sergeant_multiplayer_coop_tier_1","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_khergit_1,itm_nomad_bow,itm_arrows,itm_steppe_armor,itm_steppe_horse],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["khergit_infantry_multiplayer_coop_tier_1","Khergit Infantry","Khergit Infantries",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_khergit_1,itm_tab_shield_small_round_a,itm_steppe_armor,itm_leather_gloves],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["celestial_lancer_multiplayer_coop_tier_1","Khergit Lancer","Khergit Lancers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_spear,itm_tab_shield_small_round_a,itm_steppe_armor,itm_steppe_cap,itm_leather_gloves,itm_courser],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["iron_crown_trained_skirmisher_multiplayer_coop_tier_1","Nord Archer","Nord Archers",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_arrows,itm_sword_viking_2_small,itm_short_bow,itm_blue_tunic],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["iron_crown_vetaran_multiplayer_coop_tier_1","Nord Huscarl","Nord Huscarls",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_sword_viking_1,itm_one_handed_war_axe_a,itm_tab_shield_round_a,itm_blue_tunic],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["nord_scout_multiplayer_coop_tier_1","Nord Scout","Nord Scouts",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_javelin,itm_war_spear,itm_tab_shield_small_round_a,itm_blue_tunic,itm_saddle_horse],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["alpine_veteran_crossbowman_multiplayer_coop_tier_1","Rhodok Crossbowman","Rhodok Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_crossbow,itm_bolts,itm_fighting_pick,itm_tab_shield_pavise_a,itm_tunic_with_green_cape],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["alpine_man_at_arms_multiplayer_coop_tier_1","Rhodok Sergeant","Rhodok Sergeants",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_military_cleaver_b,itm_tab_shield_pavise_a,itm_darts,itm_green_tunic,itm_leather_cap],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["rhodok_horseman_multiplayer_coop_tier_1","Rhodok Horseman","Rhodok Horsemen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_tab_shield_heater_cav_a, itm_light_lance, itm_green_tunic,itm_padded_coif,itm_saddle_horse],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["solarian_archer_multiplayer_coop_tier_1","Sarranid Archer","Sarranid Archers",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_arrows,itm_sarranid_mace_1,itm_short_bow,itm_solarian_robe_a],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["solarian_footman_multiplayer_coop_tier_1","Sarranid Footman","Sarranid footman",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_tab_shield_kite_a, itm_sarranid_axe_a,itm_solarian_robe_a],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["solarian_knight_multiplayer_coop_tier_1","Sarranid Mamluke","Sarranid Mamluke",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_lance,itm_tab_shield_small_round_a,itm_solarian_robe_a, itm_arabian_horse_a],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],

  ["silver_rose_trained_crossbowman_multiplayer_coop_tier_2","Swadian Crossbowman","Swadian Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_spiked_club,itm_crossbow,itm_bolts,itm_tab_shield_heater_b,itm_arming_cap,itm_red_gambeson],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["silver_rose_infantry_multiplayer_coop_tier_2","Swadian Infantry","Swadian Infantry",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_sword_medieval_b,itm_tab_shield_heater_c,itm_spear,itm_mail_coif,itm_leather_gloves,itm_mail_with_tunic_red],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["silver_rose_man_at_arms_multiplayer_coop_tier_2","Swadian Man at Arms","Swadian Men at Arms",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_lance,itm_sword_medieval_a,itm_tab_shield_heater_b,itm_black_helmet,itm_leather_gloves,itm_m_hauberk_mountain_c,itm_warhorse],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["chornovalley_longbowman_multiplayer_coop_tier_2","Vaegir Archer","Vaegir Archers",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_barbed_arrows,itm_axe,itm_nomad_bow,itm_leather_vest,itm_chornovalley_skullcap_helmet_b],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["vaegir_spearman_multiplayer_coop_tier_2","Vaegir Spearman","Vaegir spearman",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_javelin,itm_scimitar,itm_tab_shield_kite_b,itm_leather_jerkin,itm_chornovalley_footman_helmet_b,itm_leather_gloves],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["chornovalley_horseman_multiplayer_coop_tier_2","Vaegir Horseman","Vaegir Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_war_spear,itm_tab_shield_kite_cav_b,itm_javelin,itm_studded_leather_coat,itm_leather_gloves,itm_chornovalley_footman_helmet_b,itm_hunter],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["celestial_sergeant_multiplayer_coop_tier_2","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_khergit_2,itm_khergit_bow,itm_barbed_arrows,itm_steppe_armor,itm_leather_steppe_cap_a,itm_steppe_horse],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["khergit_infantry_multiplayer_coop_tier_2","Khergit Infantry","Khergit Infantries",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_khergit_2,itm_tab_shield_small_round_b,itm_javelin,itm_tribal_warrior_outfit,itm_leather_gloves],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["celestial_lancer_multiplayer_coop_tier_2","Khergit Lancer","Khergit Lancers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_war_spear,itm_tab_shield_small_round_b,itm_javelin,itm_tribal_warrior_outfit,itm_leather_steppe_cap_b,itm_courser],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["iron_crown_trained_skirmisher_multiplayer_coop_tier_2","Nord Archer","Nord Archers",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_arrows,itm_sword_viking_2,itm_long_bow,itm_leather_jerkin,itm_iron_crown_scullcap_a],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["iron_crown_vetaran_multiplayer_coop_tier_2","Nord Huscarl","Nord Huscarls",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_one_handed_war_axe_a,itm_tab_shield_round_b,itm_throwing_axes,itm_leather_jerkin,itm_iron_crown_nasal_a,itm_leather_gloves],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["nord_scout_multiplayer_coop_tier_2","Nord Scout","Nord Scouts",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_javelin,itm_lance,itm_tab_shield_small_round_a,itm_leather_jerkin,itm_leather_gloves,itm_iron_crown_nasal_a,itm_saddle_horse],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["alpine_veteran_crossbowman_multiplayer_coop_tier_2","Rhodok Crossbowman","Rhodok Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_heavy_crossbow,itm_bolts,itm_club_with_spike_head,itm_tab_shield_pavise_b,itm_leather_armor,itm_leather_gloves,itm_leather_cap],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["alpine_man_at_arms_multiplayer_coop_tier_2","Rhodok Sergeant","Rhodok Sergeants",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_military_cleaver_b,itm_tab_shield_pavise_b,itm_war_darts,itm_padded_cloth,itm_leather_gloves,itm_iron_crown_nasal_a],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["rhodok_horseman_multiplayer_coop_tier_2","Rhodok Horseman","Rhodok Horsemen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_tab_shield_heater_cav_b, itm_heavy_lance,itm_javelin,itm_padded_cloth,itm_leather_gloves,itm_iron_crown_nasal_a,itm_saddle_horse],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["solarian_archer_multiplayer_coop_tier_2","Sarranid Archer","Sarranid Archers",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_barbed_arrows,itm_sarranid_mace_1,itm_nomad_bow,itm_solarian_mail_vest_a,itm_solarian_turban_c,itm_leather_gloves],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["solarian_footman_multiplayer_coop_tier_2","Sarranid Footman","Sarranid footman",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_tab_shield_kite_b, itm_sarranid_axe_b,itm_javelin,itm_solarian_mail_vest_a,itm_solarian_turban_c,itm_leather_gloves],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["solarian_knight_multiplayer_coop_tier_2","Sarranid Mamluke","Sarranid Mamluke",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_heavy_lance,itm_tab_shield_small_round_b,itm_javelin,itm_solarian_mail_vest_a, itm_solarian_turban_c,itm_leather_gloves,itm_arabian_horse_a],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],

  ["silver_rose_trained_crossbowman_multiplayer_coop_tier_3","Swadian Crossbowman","Swadian Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_sword_medieval_b,itm_heavy_crossbow,itm_steel_bolts,itm_tab_shield_heater_c,itm_bascinet_3,itm_leather_jerkin],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["silver_rose_infantry_multiplayer_coop_tier_3","Swadian Infantry","Swadian Infantry",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_bastard_sword_a,itm_awlpike,itm_tab_shield_heater_c,itm_bascinet,itm_mail_mittens,itm_m_celestial_breastplate_heavy_b],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["silver_rose_man_at_arms_multiplayer_coop_tier_3","Swadian Man at Arms","Swadian Men at Arms",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_heavy_lance,itm_bastard_sword_b,itm_tab_shield_heater_cav_a,itm_flat_topped_helmet,itm_mail_mittens,itm_m_celestial_breastplate_heavy_b,itm_warhorse],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["chornovalley_longbowman_multiplayer_coop_tier_3","Vaegir Archer","Vaegir Archers",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_barbed_arrows,itm_scimitar_b,itm_strong_bow,itm_leather_jerkin,itm_chornovalley_footman_helmet_a,itm_leather_gloves],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["vaegir_spearman_multiplayer_coop_tier_3","Vaegir Spearman","Vaegir spearman",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_scimitar_b, itm_tab_shield_kite_b,itm_javelin,itm_chornovalley_heavy_mail_b,itm_chornovalley_footman_helmet_b,itm_leather_gloves],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["chornovalley_horseman_multiplayer_coop_tier_3","Vaegir Horseman","Vaegir Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_heavy_lance,itm_tab_shield_kite_cav_b, itm_javelin,itm_chornovalley_heavy_mail_b,itm_chornovalley_footman_helmet_b,itm_hunter,itm_mail_mittens],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["celestial_sergeant_multiplayer_coop_tier_3","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_khergit_3,itm_strong_bow,itm_khergit_arrows,itm_tribal_warrior_outfit,itm_leather_steppe_cap_c,itm_steppe_horse],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["khergit_infantry_multiplayer_coop_tier_3","Khergit Infantry","Khergit Infantries",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_hafted_blade_a,itm_javelin,itm_leather_steppe_cap_c,itm_chornovalley_heavy_mail_b,itm_mail_mittens],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["celestial_lancer_multiplayer_coop_tier_3","Khergit Lancer","Khergit Lancers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_heavy_lance,itm_tab_shield_small_round_a,itm_chornovalley_heavy_mail_b,itm_leather_steppe_cap_c,itm_courser],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["iron_crown_trained_skirmisher_multiplayer_coop_tier_3","Nord Archer","Nord Archers",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_barbed_arrows,itm_sword_viking_3,itm_long_bow,itm_leather_jerkin,itm_iron_crown_scullcap_b,itm_leather_gloves],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["iron_crown_vetaran_multiplayer_coop_tier_3","Nord Huscarl","Nord Huscarls",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_one_handed_war_axe_b,itm_tab_shield_round_d,itm_heavy_throwing_axes,itm_stormguard_hauberk_a,itm_iron_crown_footman_helmet_b],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["nord_scout_multiplayer_coop_tier_3","Nord Scout","Nord Scouts",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_throwing_spears,itm_heavy_lance,itm_tab_shield_small_round_b,itm_stormguard_hauberk_a,itm_iron_crown_nasal_b,itm_saddle_horse],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["alpine_veteran_crossbowman_multiplayer_coop_tier_3","Rhodok Crossbowman","Rhodok Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_sniper_crossbow,itm_steel_bolts,itm_military_cleaver_c,itm_tab_shield_pavise_c,itm_padded_cloth,itm_iron_crown_nasal_a,itm_leather_gloves],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["alpine_man_at_arms_multiplayer_coop_tier_3","Rhodok Sergeant","Rhodok Sergeants",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_tab_shield_pavise_c,itm_military_cleaver_c,itm_javelin,itm_ragged_outfit,itm_kettle_hat,itm_mail_mittens],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["rhodok_horseman_multiplayer_coop_tier_3","Rhodok Horseman","Rhodok Horsemen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_javelin,itm_tab_shield_heater_cav_b, itm_heavy_lance, itm_ragged_outfit,itm_bascinet_2,itm_mail_mittens,itm_saddle_horse],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["solarian_archer_multiplayer_coop_tier_3","Sarranid Archer","Sarranid Archers",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_khergit_arrows,itm_sarranid_mace_1,itm_nomad_bow,itm_solarian_mail_vest_a,itm_solarian_helmet_a,itm_leather_gloves],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["solarian_footman_multiplayer_coop_tier_3","Sarranid Footman","Sarranid footman",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_jarid, itm_tab_shield_kite_c, itm_sarranid_axe_b,itm_solarian_armor_scale_a,itm_solarian_helmet_a,itm_mail_mittens],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["solarian_knight_multiplayer_coop_tier_3","Sarranid Mamluke","Sarranid Mamluke",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_heavy_lance,itm_tab_shield_small_round_b,itm_jarid,itm_solarian_mail_vest_f,itm_solarian_helmet_warrior_a,itm_mail_mittens,itm_arabian_horse_a],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],

  ["silver_rose_trained_crossbowman_multiplayer_coop_tier_4","Swadian Crossbowman","Swadian Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_sword_medieval_b,itm_sniper_crossbow,itm_steel_bolts,itm_tab_shield_heater_c,itm_black_helmet,itm_leather_gloves,itm_m_hauberk_mountain_c],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["silver_rose_infantry_multiplayer_coop_tier_4","Swadian Infantry","Swadian Infantry",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_bastard_sword_b,itm_awlpike_long,itm_tab_shield_heater_d,itm_bascinet_3,itm_m_gauntlets_b,itm_coat_of_plates],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["silver_rose_man_at_arms_multiplayer_coop_tier_4","Swadian Man at Arms","Swadian Men at Arms",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_great_lance,itm_morningstar,itm_tab_shield_heater_cav_b,itm_great_helmet,itm_m_gauntlets_b,itm_coat_of_plates_red,itm_warhorse],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["chornovalley_longbowman_multiplayer_coop_tier_4","Vaegir Archer","Vaegir Archers",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_barbed_arrows,itm_bardiche,itm_war_bow,itm_lamellar_vest,itm_chornovalley_footman_helmet_b,itm_leather_gloves],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["vaegir_spearman_multiplayer_coop_tier_4","Vaegir Spearman","Vaegir spearman",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_bardiche,itm_javelin,itm_chornovalley_heavy_lamellar_c,itm_chornovalley_infantry_helmet_b,itm_mail_mittens],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["chornovalley_horseman_multiplayer_coop_tier_4","Vaegir Horseman","Vaegir Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_heavy_lance,itm_tab_shield_kite_cav_b,itm_javelin,itm_chornovalley_heavy_lamellar_c,itm_hunter,itm_chornovalley_infantry_helmet_b,itm_scale_gauntlets],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["celestial_sergeant_multiplayer_coop_tier_4","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_hafted_blade_b,itm_strong_bow,itm_khergit_arrows,itm_lamellar_vest_khergit,itm_khergit_guard_helmet,itm_steppe_horse],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["khergit_infantry_multiplayer_coop_tier_4","Khergit Infantry","Khergit Infantries",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_hafted_blade_b,itm_tab_shield_small_round_a,itm_jarid,itm_chornovalley_heavy_lamellar_c,itm_khergit_war_helmet,itm_lamellar_gauntlets],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["celestial_lancer_multiplayer_coop_tier_4","Khergit Lancer","Khergit Lancers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_great_lance,itm_tab_shield_small_round_c,itm_chornovalley_heavy_lamellar_c,itm_khergit_war_helmet,itm_lamellar_gauntlets,itm_courser],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["iron_crown_trained_skirmisher_multiplayer_coop_tier_4","Nord Archer","Nord Archers",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_khergit_arrows,itm_sword_viking_3,itm_long_bow,itm_m_hauberk_navy_c,itm_iron_crown_nasal_a,itm_leather_gloves],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["iron_crown_vetaran_multiplayer_coop_tier_4","Nord Huscarl","Nord Huscarls",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_great_axe,itm_tab_shield_round_e,itm_heavy_throwing_axes,itm_banded_armor,itm_iron_crown_footman_helmet_c],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["nord_scout_multiplayer_coop_tier_4","Nord Scout","Nord Scouts",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_throwing_spears,itm_great_lance,itm_tab_shield_small_round_c,itm_mail_hauberk,itm_iron_crown_footman_helmet_b,itm_saddle_horse],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["alpine_veteran_crossbowman_multiplayer_coop_tier_4","Rhodok Crossbowman","Rhodok Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_sniper_crossbow,itm_steel_bolts,itm_sledgehammer,itm_tab_shield_pavise_d,itm_mail_with_tunic_green,itm_kettle_hat,itm_leather_gloves],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["alpine_man_at_arms_multiplayer_coop_tier_4","Rhodok Sergeant","Rhodok Sergeants",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_two_handed_cleaver,itm_tab_shield_pavise_d,itm_javelin,itm_m_celestial_plate_b,itm_m_gauntlets_b,itm_m_bascinet_b],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["rhodok_horseman_multiplayer_coop_tier_4","Rhodok Horseman","Rhodok Horsemen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_javelin,itm_tab_shield_heater_cav_b, itm_great_lance, itm_m_celestial_plate_b,itm_m_gauntlets_b,itm_m_bascinet_b,itm_saddle_horse],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["solarian_archer_multiplayer_coop_tier_4","Sarranid Archer","Sarranid Archers",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_khergit_arrows,itm_sarranid_two_handed_mace_1,itm_strong_bow,itm_solarian_armor_scale_a,itm_solarian_helmet_a,itm_leather_gloves],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["solarian_footman_multiplayer_coop_tier_4","Sarranid Footman","Sarranid footman",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_bamboo_spear, itm_tab_shield_kite_c, itm_arabian_sword_a,itm_solarian_armor_scale_c,itm_solarian_helmet_mask_b,itm_scale_gauntlets],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["solarian_knight_multiplayer_coop_tier_4","Sarranid Mamluke","Sarranid Mamluke",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_arabian_sword_a,itm_lance,itm_tab_shield_small_round_c,itm_mkk_mamluke_a,itm_solarian_helmet_mask_b,itm_scale_gauntlets,itm_arabian_horse_a],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],

   ["coop_faction_troop_templates_end","{!}multiplayer_end","{!}multiplayer_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],
   #tier 1
  ["npc1_1","Hurey","Hurey",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_khergit_armor,itm_knife, itm_courser],
   str_16|agi_17|int_6|cha_30|level(25),wpex(250,80,140,160,90,250),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_ironflesh_1|knows_power_strike_7|knows_pathfinding_3|knows_athletics_5|knows_tracking_1|knows_riding_6|knows_power_throw_7|knows_power_draw_5, #skills 2/3 player at that level
   0x0000000e730065c420db6db6db6ddeff00000000001db6f00000000000000000],
  ["npc2_1","Mesym","Mesym", tf_hero|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,[itm_linen_tunic,itm_club, itm_saddle_horse],
   str_14|agi_17|int_6|cha_30|level(25),wpex(240,130,170,150,170,90),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_trade_2|knows_weapon_master_1|knows_ironflesh_1|knows_wound_treatment_1|knows_athletics_5|knows_first_aid_1|knows_leadership_1|knows_riding_4|knows_power_strike_7|knows_power_draw_3|knows_power_throw_3,
   0x0000000bff003440209b6e38e06dbeff00000000001f36e10000000000000000],
  ["npc3_1","Evel Droby","Evel Droby",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_dress,itm_knife, itm_hunter],
   str_24|agi_13|int_6|cha_30|level(25),wpex(190,80,240,180,180,80),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_wound_treatment_1|knows_trade_1|knows_first_aid_3|knows_surgery_1|knows_athletics_6|knows_riding_8|knows_power_strike_5|knows_power_draw_3|knows_power_throw_3,
   0x00000004a204300436db6db6db6dfeff00000000001db6db0000000000000000],
  ["npc4_1","Ilhan","Ilhan",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_leather_jerkin, itm_sword_medieval_a, itm_hunter],
   str_20|agi_13|int_6|cha_30|level(25),wpex(210,230,200,90,100,95),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_weapon_master_2|knows_power_strike_9|knows_riding_8|knows_athletics_7|knows_power_throw_3|knows_first_aid_1|knows_surgery_1|knows_tactics_2|knows_leadership_2|knows_power_draw_2,
   0x0000000b7d00130020db6db6db6dbeff00000000001db6e80000000000000000],
  ["npc5_1","Gyliam Gare","Gyliam Gare",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_nomad_vest, itm_sword_khergit_1, itm_steppe_horse],
   str_18|agi_13|int_6|cha_30|level(25),wpex(160,80,130,250,50,230),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_riding_7|knows_horse_archery_9|knows_power_draw_8|knows_leadership_2|knows_weapon_master_1|knows_power_strike_5|knows_power_throw_8|knows_athletics_5,
   0x0000000dff00115420db6db6db6dbeff00000000001db6e80000000000000000],
  ["npc6_1","Ames","Ames",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_tabard, itm_sword_medieval_a, itm_sumpter_horse],
   str_20|agi_19|int_6|cha_30|level(25),wpex(240,210,180,90,100,80),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_riding_7|knows_weapon_master_2|knows_athletics_8|knows_trainer_1|knows_leadership_1|knows_power_strike_7|knows_power_draw_2|knows_power_throw_3,
  0x0000000d401001cf20db6db6db6dfeff00000000001db6d00000000000000000],
  ["npc7_1","Malia Willey","Malia Willey",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_ragged_outfit, itm_hunting_bow, itm_arrows, itm_quarter_staff, itm_arabian_horse_b],
   str_16|agi_13|int_6|cha_30|level(25),wpex(90,80,230,280,110,130),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_tracking_2|knows_athletics_8|knows_spotting_1|knows_pathfinding_1|knows_power_draw_10|knows_riding_4|knows_power_strike_6|knows_power_throw_5,
   0x000000031f08000206d86db64b4db6db00000000001db6c30000000000000000],
  ["npc8_1","Eryet Allard","Eryet Allard",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_tribal_warrior_outfit, itm_sword_viking_1, itm_courser],
   str_18|agi_15|int_6|cha_30|level(25),wpex(190,250,80,120,80,250),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_weapon_master_3|knows_athletics_10|knows_leadership_3|knows_tactics_1|knows_riding_4|knows_power_strike_10|knows_power_draw_2|knows_power_throw_8,
   0x0000000ffe08000300db6db6496208d400000000001d86fc0000000000000000],
  ["npc9_1","Aduhash","Aduhash",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_tabard, itm_sword_medieval_b_small, itm_courser],
   str_22|agi_19|int_6|cha_30|level(25),wpex(80,230,130,220,70,160),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_weapon_master_1|knows_riding_4|knows_athletics_6|knows_leadership_1|knows_tactics_1|knows_power_strike_4|knows_power_draw_7|knows_power_throw_5,
   0x00000001900471c6125b69fcdb6dbeff00000000001db6fb0000000000000000],
  ["npc10_1","Zela","Zela",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_padded_leather, itm_crossbow, itm_bolts, itm_pickaxe, itm_saddle_horse],
   str_24|agi_19|int_6|cha_30|level(25),wpex(170,80,80,160,290,150),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_weapon_master_3|knows_tactics_1|knows_leadership_1|knows_ironflesh_3|knows_trainer_2|knows_first_aid_2|knows_riding_4|knows_power_strike_5|knows_power_draw_5|knows_power_throw_5|knows_athletics_7,
   0x0000000190042348058365c91c7d8eff00000000001de6fb0000000000000000],
  ["npc11_1","Jane","Jane",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_leather_apron, itm_falchion,  itm_sumpter_horse],
   str_16|agi_17|int_6|cha_30|level(25),wpex(140,230,130,80,210,170),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_weapon_master_1|knows_first_aid_1|knows_wound_treatment_2|knows_ironflesh_3|knows_inventory_management_5|knows_riding_4|knows_power_strike_5|knows_power_draw_2|knows_power_throw_7|knows_athletics_5,
   0x00000006000c000206186196918db8e400000000001d48c40000000000000000],
  ["npc12_1","Pai Khoi-Kao","Pai Khoi-Kao",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_pilgrim_disguise, itm_staff, itm_sumpter_horse],
   str_16|agi_17|int_6|cha_30|level(25),wpex(120,110,290,80,110,120),   knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_ironflesh_1|knows_power_strike_7|knows_surgery_4|knows_wound_treatment_3|knows_first_aid_3|knows_riding_4|knows_power_draw_2|knows_power_throw_3|knows_athletics_7,
   0x00000001bf044383201d6a24da6dbcff00000000001db6f80000000000000000],
  ["npc13_1","Dondo","Dondo",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_nomad_robe, itm_scimitar, itm_courser],
   str_14|agi_17|int_6|cha_30|level(25),wpex(250,80,140,210,110,140),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_riding_9|knows_leadership_2|knows_athletics_5|knows_ironflesh_2|knows_power_strike_6|knows_weapon_master_1|knows_power_draw_7|knows_power_throw_4,
   0x00000001bf0474d420dc6a36ea6dbcff00000000001db6f80000000000000000],
  ["npc14_1","Elrel","Elrel",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_nobleman_outfit, itm_sword_medieval_b_small, itm_courser],
   str_18|agi_19|int_6|cha_30|level(25),wpex(280,170,170,170,170,180),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_trainer_4|knows_weapon_master_3|knows_leadership_2|knows_power_strike_1|knows_riding_7|knows_power_strike_7|knows_power_draw_6|knows_power_throw_6|knows_athletics_8,
   0x00000001be00024545136dc11b79fcdb00000000001db6e80000000000000000],
  ["npc15_1","Phamas","Phamas",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_rich_outfit, itm_sword_medieval_b_small, itm_hunter],
   str_18|agi_13|int_6|cha_30|level(25),wpex(190,290,130,210,90,90),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_tactics_2|knows_engineer_4|knows_trade_3|knows_tracking_1|knows_spotting_1|knows_riding_6|knows_power_strike_7|knows_power_draw_7|knows_power_throw_3|knows_athletics_5,
   0x0000000fb110600020db6dd9226dbf7f00000000001db6f80000000000000000],
  ["npc16_1","Kina","Kina",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_peasant_dress, itm_dagger, itm_throwing_knives, itm_saddle_horse],
   str_14|agi_17|int_6|cha_30|level(25),wpex(260,10,100,160,30,300),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_power_throw_10|knows_athletics_10|knows_power_strike_8|knows_riding_4|knows_power_draw_5,
   0x00000000000c3001009849a2494288cb00000000001da6830000000000000000],
   
    #tier 2
  ["npc1_2","Hurey","Hurey",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_leather_steppe_cap_c,itm_leather_gloves,itm_nomad_robe,itm_sword_medieval_b_small, itm_courser],
   str_16|agi_17|int_12|cha_7|level(14),wp(60),knows_tracker_npc|
   knows_ironflesh_1|knows_power_strike_1|knows_pathfinding_3|knows_athletics_2|knows_tracking_1|knows_riding_2, #skills 2/3 player at that level
   0x0000000e730065c420db6db6db6ddeff00000000001db6f00000000000000000],
  ["npc2_2","Mesym","Mesym", tf_hero|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,[itm_footman_helmet,itm_padded_leather,itm_mace_2,itm_tab_shield_small_round_a, itm_saddle_horse],
   str_14|agi_17|int_11|cha_6|level(14),wp(40),knows_merchant_npc|
   knows_trade_2|knows_weapon_master_1|knows_ironflesh_1|knows_wound_treatment_1|knows_athletics_2|knows_first_aid_1|knows_leadership_1,
   0x0000000bff003440209b6e38e06dbeff00000000001f36e10000000000000000],
  ["npc3_2","Evel Droby","Evel Droby",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_head_wrappings,itm_leather_jerkin,itm_sword_medieval_b_small, itm_hunter],
   str_24|agi_13|int_11|cha_6|level(14),wp(20),knows_merchant_npc|
   knows_wound_treatment_1|knows_trade_1|knows_first_aid_3|knows_surgery_1|knows_athletics_1|knows_riding_1,
   0x00000004a204300436db6db6db6dfeff00000000001db6db0000000000000000],
  ["npc4_2","Ilhan","Ilhan",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_kettle_hat,itm_leather_gloves,itm_studded_leather_coat,itm_sword_medieval_c,itm_tab_shield_heater_c, itm_hunter],
   str_20|agi_13|int_13|cha_10|level(27),wp(110),knows_warrior_npc|
   knows_weapon_master_2|knows_power_strike_2|knows_riding_2|knows_athletics_2|knows_power_throw_2|knows_first_aid_1|knows_surgery_1|knows_tactics_2|knows_leadership_2,
   0x0000000b7d00130020db6db6db6dbeff00000000001db6e80000000000000000],
  ["npc5_2","Gyliam Gare","Gyliam Gare",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sword_khergit_2, itm_tab_shield_small_round_b, itm_leather_steppe_cap_b, itm_tribal_warrior_outfit,  itm_steppe_horse],
   str_18|agi_13|int_12|cha_7|level(23),wp(90),knows_warrior_npc|
   knows_riding_2|knows_horse_archery_3|knows_power_draw_3|knows_leadership_2|knows_weapon_master_1,
   0x0000000dff00115420db6db6db6dbeff00000000001db6e80000000000000000],
  ["npc6_2","Ames","Ames",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_bastard_sword_a, itm_mail_coif, itm_mail_with_tunic_red,  itm_sumpter_horse],
   str_20|agi_19|int_10|cha_5|level(25),wp(105),knows_warrior_npc|
   knows_riding_2|knows_weapon_master_2|knows_power_strike_2|knows_athletics_3|knows_trainer_1|knows_leadership_1,
  0x0000000d401001cf20db6db6db6dfeff00000000001db6d00000000000000000],
  ["npc7_2","Malia Willey","Malia Willey",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_voulge, itm_short_bow, itm_barbed_arrows, itm_iron_crown_nasal_b, itm_leather_gloves, itm_studded_leather_coat,  itm_arabian_horse_b],
   str_16|agi_13|int_10|cha_6|level(17),wp(80),knows_tracker_npc|
   knows_tracking_2|knows_athletics_2|knows_spotting_1|knows_pathfinding_1|knows_power_draw_2,
   0x000000031f08000206d86db64b4db6db00000000001db6c30000000000000000],
  ["npc8_2","Eryet Allard","Eryet Allard",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sword_viking_2, itm_mail_coif, itm_m_hauberk_navy_c,  itm_courser],
   str_18|agi_15|int_9|cha_10|level(26),wp(90),knows_warrior_npc|
   knows_weapon_master_3|knows_power_strike_2|knows_athletics_2|knows_leadership_3|knows_tactics_1,
   0x0000000ffe08000300db6db6496208d400000000001d86fc0000000000000000],
  ["npc9_2","Aduhash","Aduhash",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sword_medieval_c, itm_chornovalley_skullcap_helmet_a, itm_leather_vest,  itm_courser],
   str_22|agi_19|int_7|cha_8|level(17),wp(100),knows_warrior_npc|
   knows_weapon_master_1|knows_riding_1|knows_athletics_1|knows_leadership_1|knows_tactics_1|knows_power_strike_1,
   0x00000001900471c6125b69fcdb6dbeff00000000001db6fb0000000000000000],
  ["npc10_2","Zela","Zela",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_military_sickle_a, itm_heavy_crossbow, itm_bolts, itm_mail_coif, itm_leather_gloves, itm_aketon_green,  itm_saddle_horse],
   str_24|agi_19|int_9|cha_11|level(27),wp(105),knows_warrior_npc|
   knows_weapon_master_3|knows_tactics_1|knows_leadership_1|knows_ironflesh_3|knows_trainer_2|knows_first_aid_2,
   0x0000000190042348058365c91c7d8eff00000000001de6fb0000000000000000],
  ["npc11_2","Jane","Jane",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sarranid_axe_a, itm_arming_cap, itm_leather_gloves, itm_padded_cloth,  itm_sumpter_horse],
   str_16|agi_17|int_10|cha_10|level(26),wp(70),knows_merchant_npc|
   knows_weapon_master_1|knows_first_aid_1|knows_wound_treatment_2|knows_ironflesh_3|knows_inventory_management_5,
   0x00000006000c000206186196918db8e400000000001d48c40000000000000000],
  ["npc12_2","Pai Khoi-Kao","Pai Khoi-Kao",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_iron_staff, itm_padded_coif, itm_leather_gloves, itm_pilgrim_disguise,  itm_sumpter_horse],
   str_16|agi_17|int_13|cha_7|level(20),wp(30),   knows_merchant_npc|
   knows_ironflesh_1|knows_power_strike_1|knows_surgery_4|knows_wound_treatment_3|knows_first_aid_3,
   0x00000001bf044383201d6a24da6dbcff00000000001db6f80000000000000000],
  ["npc13_2","Dondo","Dondo",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_scimitar, itm_tab_shield_small_round_b, itm_solarian_turban_c, itm_solarian_scale_vest_c,  itm_courser],
   str_14|agi_17|int_12|cha_8|level(19),wp(80),knows_warrior_npc|
   knows_riding_2|knows_leadership_2|knows_athletics_2|knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_1,
   0x00000001bf0474d420dc6a36ea6dbcff00000000001db6f80000000000000000],
  ["npc14_2","Elrel","Elrel",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sword_medieval_b, itm_tab_shield_heater_c, itm_mail_coif, itm_studded_leather_coat,  itm_courser],
   str_18|agi_19|int_11|cha_8|level(23),wp(100),knows_warrior_npc|
   knows_trainer_4|knows_weapon_master_3|knows_leadership_2|knows_power_strike_1,
   0x00000001be00024545136dc11b79fcdb00000000001db6e80000000000000000],
  ["npc15_2","Phamas","Phamas",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_long_axe, itm_black_helmet, itm_leather_gloves, itm_red_gambeson,  itm_hunter],
   str_18|agi_13|int_12|cha_8|level(25),wp(80),knows_warrior_npc|
   knows_tactics_2|knows_engineer_4|knows_trade_3|knows_tracking_1|knows_spotting_1,
   0x0000000fb110600020db6dd9226dbf7f00000000001db6f80000000000000000],
  ["npc16_2","Kina","Kina",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sword_viking_2_small, itm_light_throwing_axes, itm_black_helmet, itm_leather_gloves, itm_leather_jerkin,  itm_saddle_horse],
   str_14|agi_17|int_8|cha_7|level(17),wp(80),knows_tracker_npc|
   knows_power_throw_3|knows_athletics_2|knows_power_strike_1,
   0x00000000000c3001009849a2494288cb00000000001da6830000000000000000],

  #tier 3
  ["npc1_3","Hurey","Hurey",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_khergit_war_helmet,itm_lamellar_gauntlets,itm_lamellar_vest_khergit,itm_sword_medieval_c_small, itm_courser],
   str_16|agi_17|int_12|cha_7|level(14),wp(60),knows_tracker_npc|
   knows_ironflesh_1|knows_power_strike_1|knows_pathfinding_3|knows_athletics_2|knows_tracking_1|knows_riding_2, #skills 2/3 player at that level
   0x0000000e730065c420db6db6db6ddeff00000000001db6f00000000000000000],
  ["npc2_3","Mesym","Mesym", tf_hero|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,[itm_iron_crown_scullcap_b,itm_leather_gloves,itm_m_hauberk_navy_c,itm_mace_3,itm_tab_shield_small_round_b, itm_saddle_horse],
   str_14|agi_17|int_11|cha_6|level(14),wp(40),knows_merchant_npc|
   knows_trade_2|knows_weapon_master_1|knows_ironflesh_1|knows_wound_treatment_1|knows_athletics_2|knows_first_aid_1|knows_leadership_1,
   0x0000000bff003440209b6e38e06dbeff00000000001f36e10000000000000000],
  ["npc3_3","Evel Droby","Evel Droby",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_skullcap,itm_leather_gloves,itm_stormguard_hauberk_a,itm_sword_medieval_c_small, itm_hunter],
   str_24|agi_13|int_11|cha_6|level(14),wp(20),knows_merchant_npc|
   knows_wound_treatment_1|knows_trade_1|knows_first_aid_3|knows_surgery_1|knows_athletics_1|knows_riding_1,
   0x00000004a204300436db6db6db6dfeff00000000001db6db0000000000000000],
  ["npc4_3","Ilhan","Ilhan",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_bascinet_2,itm_leather_gloves,itm_m_celestial_plate_b,itm_sword_medieval_c_long,itm_tab_shield_heater_c, itm_hunter],
   str_20|agi_13|int_13|cha_10|level(27),wp(110),knows_warrior_npc|
   knows_weapon_master_2|knows_power_strike_2|knows_riding_2|knows_athletics_2|knows_power_throw_2|knows_first_aid_1|knows_surgery_1|knows_tactics_2|knows_leadership_2,
   0x0000000b7d00130020db6db6db6dbeff00000000001db6e80000000000000000],
  ["npc5_3","Gyliam Gare","Gyliam Gare",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_scimitar, itm_tab_shield_small_round_c, itm_khergit_cavalry_helmet, itm_leather_gloves, itm_lamellar_vest,  itm_steppe_horse],
   str_18|agi_13|int_12|cha_7|level(23),wp(90),knows_warrior_npc|
   knows_riding_2|knows_horse_archery_3|knows_power_draw_3|knows_leadership_2|knows_weapon_master_1,
   0x0000000dff00115420db6db6db6dbeff00000000001db6e80000000000000000],
  ["npc6_3","Ames","Ames",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_bastard_sword_b, itm_flat_topped_helmet, itm_mail_mittens, itm_m_hauberk_mountain_c,  itm_sumpter_horse],
   str_20|agi_19|int_10|cha_5|level(25),wp(105),knows_warrior_npc|
   knows_riding_2|knows_weapon_master_2|knows_power_strike_2|knows_athletics_3|knows_trainer_1|knows_leadership_1,
  0x0000000d401001cf20db6db6db6dfeff00000000001db6d00000000000000000],
  ["npc7_3","Malia Willey","Malia Willey",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_long_bardiche, itm_strong_bow, itm_barbed_arrows, itm_mail_coif, itm_leather_gloves, itm_mail_hauberk, itm_arabian_horse_b],
   str_16|agi_13|int_10|cha_6|level(17),wp(80),knows_tracker_npc|
   knows_tracking_2|knows_athletics_2|knows_spotting_1|knows_pathfinding_1|knows_power_draw_2,
   0x000000031f08000206d86db64b4db6db00000000001db6c30000000000000000],
  ["npc8_3","Eryet Allard","Eryet Allard",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_battle_axe, itm_iron_crown_footman_helmet_b, itm_leather_gloves, itm_mail_hauberk,  itm_courser],
   str_18|agi_15|int_9|cha_10|level(26),wp(90),knows_warrior_npc|
   knows_weapon_master_3|knows_power_strike_2|knows_athletics_2|knows_leadership_3|knows_tactics_1,
   0x0000000ffe08000300db6db6496208d400000000001d86fc0000000000000000],
  ["npc9_3","Aduhash","Aduhash",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sword_medieval_c_long, itm_chornovalley_footman_helmet_b, itm_leather_gloves, itm_lamellar_vest,  itm_courser],
   str_22|agi_19|int_7|cha_8|level(17),wp(100),knows_warrior_npc|
   knows_weapon_master_1|knows_riding_1|knows_athletics_1|knows_leadership_1|knows_tactics_1|knows_power_strike_1,
   0x00000001900471c6125b69fcdb6dbeff00000000001db6fb0000000000000000],
  ["npc10_3","Zela","Zela",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_military_pick, itm_heavy_crossbow, itm_steel_bolts, itm_kettle_hat, itm_leather_gloves, itm_mail_with_tunic_green,  itm_saddle_horse],
   str_24|agi_19|int_9|cha_11|level(27),wp(105),knows_warrior_npc|
   knows_weapon_master_3|knows_tactics_1|knows_leadership_1|knows_ironflesh_3|knows_trainer_2|knows_first_aid_2,
   0x0000000190042348058365c91c7d8eff00000000001de6fb0000000000000000],
  ["npc11_3","Jane","Jane",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sarranid_axe_b, itm_arming_cap, itm_leather_gloves, itm_m_celestial_breastplate_heavy_b,  itm_sumpter_horse],
   str_16|agi_17|int_10|cha_10|level(26),wp(70),knows_merchant_npc|
   knows_weapon_master_1|knows_first_aid_1|knows_wound_treatment_2|knows_ironflesh_3|knows_inventory_management_5,
   0x00000006000c000206186196918db8e400000000001d48c40000000000000000],
  ["npc12_3","Pai Khoi-Kao","Pai Khoi-Kao",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_iron_staff, itm_mail_coif, itm_mail_mittens, itm_pilgrim_disguise,  itm_sumpter_horse],
   str_16|agi_17|int_13|cha_7|level(20),wp(30),   knows_merchant_npc|
   knows_ironflesh_1|knows_power_strike_1|knows_surgery_4|knows_wound_treatment_3|knows_first_aid_3,
   0x00000001bf044383201d6a24da6dbcff00000000001db6f80000000000000000],
  ["npc13_3","Dondo","Dondo",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_scimitar, itm_tab_shield_small_round_c, itm_solarian_helmet_a, itm_solarian_armor_a, itm_courser],
   str_14|agi_17|int_12|cha_8|level(19),wp(80),knows_warrior_npc|
   knows_riding_2|knows_leadership_2|knows_athletics_2|knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_1,
   0x00000001bf0474d420dc6a36ea6dbcff00000000001db6f80000000000000000],
  ["npc14_3","Elrel","Elrel",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sword_medieval_c, itm_tab_shield_heater_c, itm_bascinet_2, itm_leather_gloves, itm_m_celestial_plate_b,  itm_courser],
   str_18|agi_19|int_11|cha_8|level(23),wp(100),knows_warrior_npc|
   knows_trainer_4|knows_weapon_master_3|knows_leadership_2|knows_power_strike_1,
   0x00000001be00024545136dc11b79fcdb00000000001db6e80000000000000000],
  ["npc15_3","Phamas","Phamas",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_long_axe_b, itm_bascinet_3, itm_mail_mittens, itm_m_hauberk_mountain_c,  itm_hunter],
   str_18|agi_13|int_12|cha_8|level(25),wp(80),knows_warrior_npc|
   knows_tactics_2|knows_engineer_4|knows_trade_3|knows_tracking_1|knows_spotting_1,
   0x0000000fb110600020db6dd9226dbf7f00000000001db6f80000000000000000],
  ["npc16_3","Kina","Kina",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sword_viking_2_small, itm_throwing_axes, itm_chornovalley_skullcap_helmet_b, itm_leather_gloves, itm_lamellar_vest,  itm_saddle_horse],
   str_14|agi_17|int_8|cha_7|level(17),wp(80),knows_tracker_npc|
   knows_power_throw_3|knows_athletics_2|knows_power_strike_1,
   0x00000000000c3001009849a2494288cb00000000001da6830000000000000000],

   #tier 4
  ["npc1_4","Hurey","Hurey",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_khergit_guard_helmet,itm_lamellar_gauntlets,itm_khergit_guard_armor,itm_sword_viking_3_small, itm_courser],
   str_16|agi_17|int_12|cha_7|level(14),wp(60),knows_tracker_npc|
   knows_ironflesh_1|knows_power_strike_1|knows_pathfinding_3|knows_athletics_2|knows_tracking_1|knows_riding_2, #skills 2/3 player at that level
   0x0000000e730065c420db6db6db6ddeff00000000001db6f00000000000000000],
  ["npc2_4","Mesym","Mesym", tf_hero|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,[itm_mail_coif,itm_mail_mittens,itm_mail_hauberk,itm_mace_4,itm_tab_shield_small_round_c, itm_saddle_horse],
   str_14|agi_17|int_11|cha_6|level(14),wp(40),knows_merchant_npc|
   knows_trade_2|knows_weapon_master_1|knows_ironflesh_1|knows_wound_treatment_1|knows_athletics_2|knows_first_aid_1|knows_leadership_1,
   0x0000000bff003440209b6e38e06dbeff00000000001f36e10000000000000000],
  ["npc3_4","Evel Droby","Evel Droby",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_bascinet_3,itm_m_gauntlets_b,itm_plate_armor,itm_sword_viking_3_small, itm_hunter],
   str_24|agi_13|int_11|cha_6|level(14),wp(20),knows_merchant_npc|
   knows_wound_treatment_1|knows_trade_1|knows_first_aid_3|knows_surgery_1|knows_athletics_1|knows_riding_1,
   0x00000004a204300436db6db6db6dfeff00000000001db6db0000000000000000],
  ["npc4_4","Ilhan","Ilhan",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_m_bascinet_b,itm_scale_gauntlets,itm_heraldic_mail_with_tabard,itm_sword_medieval_d_long,itm_tab_shield_heater_d, itm_hunter],
   str_20|agi_13|int_13|cha_10|level(27),wp(110),knows_warrior_npc|
   knows_weapon_master_2|knows_power_strike_2|knows_riding_2|knows_athletics_2|knows_power_throw_2|knows_first_aid_1|knows_surgery_1|knows_tactics_2|knows_leadership_2,
   0x0000000b7d00130020db6db6db6dbeff00000000001db6e80000000000000000],
  ["npc5_4","Gyliam Gare","Gyliam Gare",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_scimitar_b, itm_tab_shield_small_round_c, itm_khergit_guard_helmet, itm_scale_gauntlets, itm_chornovalley_heavy_mail_b,  itm_steppe_horse],
   str_18|agi_13|int_12|cha_7|level(23),wp(90),knows_warrior_npc|
   knows_riding_2|knows_horse_archery_3|knows_power_draw_3|knows_leadership_2|knows_weapon_master_1,
   0x0000000dff00115420db6db6db6dbeff00000000001db6e80000000000000000],
  ["npc6_4","Ames","Ames",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sword_two_handed_b, itm_bascinet, itm_m_gauntlets_b, itm_cuir_bouilli,  itm_sumpter_horse],
   str_20|agi_19|int_10|cha_5|level(25),wp(105),knows_warrior_npc|
   knows_riding_2|knows_weapon_master_2|knows_power_strike_2|knows_athletics_3|knows_trainer_1|knows_leadership_1,
  0x0000000d401001cf20db6db6db6dfeff00000000001db6d00000000000000000],
  ["npc7_4","Malia Willey","Malia Willey",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_great_long_bardiche, itm_war_bow, itm_khergit_arrows, itm_iron_crown_footman_helmet_b, itm_scale_gauntlets, itm_heraldic_mail_with_tabard,  itm_arabian_horse_b],
   str_16|agi_13|int_10|cha_6|level(17),wp(80),knows_tracker_npc|
   knows_tracking_2|knows_athletics_2|knows_spotting_1|knows_pathfinding_1|knows_power_draw_2,
   0x000000031f08000206d86db64b4db6db00000000001db6c30000000000000000],
  ["npc8_4","Eryet Allard","Eryet Allard",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_great_axe, itm_iron_crown_footman_helmet_c, itm_mail_mittens, itm_banded_armor,  itm_courser],
   str_18|agi_15|int_9|cha_10|level(26),wp(90),knows_warrior_npc|
   knows_weapon_master_3|knows_power_strike_2|knows_athletics_2|knows_leadership_3|knows_tactics_1,
   0x0000000ffe08000300db6db6496208d400000000001d86fc0000000000000000],
  ["npc9_4","Aduhash","Aduhash",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_bastard_sword_b, itm_chornovalley_infantry_helmet_b, itm_lamellar_gauntlets, itm_banded_armor,  itm_courser],
   str_22|agi_19|int_7|cha_8|level(17),wp(100),knows_warrior_npc|
   knows_weapon_master_1|knows_riding_1|knows_athletics_1|knows_leadership_1|knows_tactics_1|knows_power_strike_1,
   0x00000001900471c6125b69fcdb6dbeff00000000001db6fb0000000000000000],
  ["npc10_4","Zela","Zela",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_military_pick, itm_sniper_crossbow, itm_steel_bolts, itm_m_bascinet_b, itm_mail_mittens, itm_m_celestial_plate_b, itm_saddle_horse],
   str_24|agi_19|int_9|cha_11|level(27),wp(105),knows_warrior_npc|
   knows_weapon_master_3|knows_tactics_1|knows_leadership_1|knows_ironflesh_3|knows_trainer_2|knows_first_aid_2,
   0x0000000190042348058365c91c7d8eff00000000001de6fb0000000000000000],
  ["npc11_4","Jane","Jane",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sarranid_two_handed_axe_a, itm_great_helmet, itm_m_gauntlets_b, itm_brigandine_red,  itm_sumpter_horse],
   str_16|agi_17|int_10|cha_10|level(26),wp(70),knows_merchant_npc|
   knows_weapon_master_1|knows_first_aid_1|knows_wound_treatment_2|knows_ironflesh_3|knows_inventory_management_5,
   0x00000006000c000206186196918db8e400000000001d48c40000000000000000],
  ["npc12_4","Pai Khoi-Kao","Pai Khoi-Kao",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_iron_staff, itm_kettle_hat, itm_m_gauntlets_b, itm_m_celestial_plate_b,  itm_sumpter_horse],
   str_16|agi_17|int_13|cha_7|level(20),wp(30),   knows_merchant_npc|
   knows_ironflesh_1|knows_power_strike_1|knows_surgery_4|knows_wound_treatment_3|knows_first_aid_3,
   0x00000001bf044383201d6a24da6dbcff00000000001db6f80000000000000000],
  ["npc13_4","Dondo","Dondo",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_scimitar_b, itm_tab_shield_small_round_c, itm_solarian_helmet_mask_b, itm_scale_gauntlets, itm_mkk_mamluke_a, itm_courser],
   str_14|agi_17|int_12|cha_8|level(19),wp(80),knows_warrior_npc|
   knows_riding_2|knows_leadership_2|knows_athletics_2|knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_1,
   0x00000001bf0474d420dc6a36ea6dbcff00000000001db6f80000000000000000],
  ["npc14_4","Elrel","Elrel",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sword_medieval_d_long, itm_tab_shield_heater_d, itm_great_helmet, itm_m_gauntlets_b, itm_heraldic_mail_with_surcoat,  itm_courser],
   str_18|agi_19|int_11|cha_8|level(23),wp(100),knows_warrior_npc|
   knows_trainer_4|knows_weapon_master_3|knows_leadership_2|knows_power_strike_1,
   0x00000001be00024545136dc11b79fcdb00000000001db6e80000000000000000],
  ["npc15_4","Phamas","Phamas",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_long_axe_c, itm_m_bascinet_b, itm_scale_gauntlets, itm_heraldic_mail_with_surcoat,  itm_hunter],
   str_18|agi_13|int_12|cha_8|level(25),wp(80),knows_warrior_npc|
   knows_tactics_2|knows_engineer_4|knows_trade_3|knows_tracking_1|knows_spotting_1,
   0x0000000fb110600020db6dd9226dbf7f00000000001db6f80000000000000000],
  ["npc16_4","Kina","Kina",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sword_viking_3_small, itm_heavy_throwing_axes, itm_chornovalley_footman_helmet_b, itm_lamellar_gauntlets, itm_chornovalley_heavy_mail_b,  itm_saddle_horse],
   str_14|agi_17|int_8|cha_7|level(17),wp(80),knows_tracker_npc|
   knows_power_throw_3|knows_athletics_2|knows_power_strike_1,
   0x00000000000c3001009849a2494288cb00000000001da6830000000000000000],

   ["coop_companion_equipment_ui_0","{!}multiplayer_end","{!}multiplayer_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],
   ["coop_companion_equipment_ui_0_f","{!}multiplayer_end","{!}multiplayer_end", tf_female, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],
   ["coop_companion_equipment_ui_1","{!}multiplayer_end","{!}multiplayer_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],
   ["coop_companion_equipment_ui_1_f","{!}multiplayer_end","{!}multiplayer_end", tf_female, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],
   ["coop_companion_equipment_sets_end","{!}multiplayer_end","{!}multiplayer_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],

  ##diplomacy begin
  #SB : fixed plural name (hero name), TODO actually use name/gender in hiring dialogues
  ["dplmc_chamberlain","Chamberlain Aubrey de Vere", "Aubrey de Vere",tf_hero|tf_male,0,0,fac_commoners,[itm_tabard], def_attrib|level(10), wp(40),knows_inventory_management_10,0x0000000dfc0c238838e571c8d469c91b00000000001e39230000000000000000],

  ["dplmc_constable","Constable Miles de Gloucester","Miles de Gloucester",tf_hero|tf_male,0,0,fac_commoners,[itm_dplmc_coat_of_plates_red_constable],
   knight_attrib_4,wp_melee(200),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_4|knows_athletics_4,0x0000000b4b1015054b1b4d591cba28d300000000001e472b0000000000000000],

  ["dplmc_chancellor","Chancellor Herfast","Herfast",tf_hero|tf_male,0,0,fac_commoners,[itm_nobleman_outfit],def_attrib|level(10), wp(40),knows_inventory_management_10, 0x00000009a20c21cf491bad28a28628d400000000001e371a0000000000000000],

  ["dplmc_messenger","Messenger","Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_neutral,
   [itm_sword_medieval_a,itm_leather_jerkin,itm_courser,itm_leather_gloves,itm_light_crossbow,itm_bolts],
   def_attrib|agi_21|int_30|cha_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_leadership_7,man_face_young_1,man_face_old_2],
  ["dplmc_scout","Scout","Scouts",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_neutral,
   [itm_sword_medieval_a,itm_leather_jerkin,itm_courser,itm_leather_gloves,itm_light_crossbow,itm_bolts],
   def_attrib|agi_21|int_30|cha_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_leadership_7,man_face_young_1,man_face_old_2],
# recruiter kit begin
  ["dplmc_recruiter","Recruiter","Recruiter",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_neutral,
   [itm_sword_medieval_a,itm_leather_jerkin,itm_courser,itm_leather_gloves,itm_light_crossbow,itm_bolts],
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

upgrade(troops,"menegras_halberdier","experienced_menegras_halberdier")
upgrade(troops,"experienced_menegras_halberdier","menegras_halberdier_veteran")

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
upgrade(troops,"elen_novice","elen_footman")
upgrade2(troops,"elen_footman","elen_fighter","elen_archer")

upgrade(troops,"elen_fighter","elen_light_infantry")
upgrade(troops,"elen_light_infantry","elen_heavy_infantry")
upgrade(troops,"elen_heavy_infantry", "elen_cheif")

upgrade2(troops,"elen_archer","elen_experienced_archer", "elen_sniper")

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

# native
upgrade2(troops,"silver_rose_levy","silver_rose_milita","silver_rose_scout")

upgrade2(troops,"silver_rose_milita","silver_rose_footman","silver_rose_crossbowman")
upgrade2(troops,"silver_rose_footman","silver_rose_hacker","silver_rose_infantry")
upgrade2(troops,"silver_rose_infantry","silver_rose_sergeant","silver_rose_horseman")
upgrade(troops,"silver_rose_crossbowman","silver_rose_trained_crossbowman")

upgrade(troops,"silver_rose_trained_crossbowman","silver_rose_sharpshooter")

upgrade(troops,"silver_rose_horseman","silver_rose_man_at_arms")
upgrade(troops,"silver_rose_man_at_arms","silver_rose_knight")

upgrade(troops,"chornovalley_recruit","chornovalley_scout")
upgrade2(troops,"chornovalley_scout","chornovalley_warrior", "chornovalley_hunter")
upgrade(troops,"chornovalley_hunter","chornovalley_longbowman")

upgrade2(troops,"chornovalley_warrior","chornovalley_sheriff", "chornovalley_horseman")
upgrade2(troops,"chornovalley_sheriff","chornovalley_gunslider","chornovalley_sergeant")

upgrade(troops,"chornovalley_horseman","chornovalley_knight")

upgrade2(troops,"celestial_recruit","celestial_milita","celestial_hunter")
upgrade(troops,"celestial_hunter","celestial_crossbowman")

upgrade2(troops,"celestial_milita","celestial_armsman","celestial_foot_knight")
upgrade2(troops,"celestial_armsman","celestial_lancer","celestial_sergeant")
upgrade(troops,"celestial_sergeant","celestial_commander")

upgrade2(troops,"iron_crown_recruit","iron_crown_raider","iron_crown_skirmisher")
upgrade(troops,"iron_crown_raider","iron_crown_footman")
upgrade(troops,"iron_crown_footman","iron_crown_man_at_arms")
upgrade2(troops,"iron_crown_man_at_arms","iron_crown_vetaran", "iron_crown_halberdier")
upgrade(troops,"iron_crown_vetaran","iron_crown_champion")

upgrade(troops,"iron_crown_skirmisher","iron_crown_trained_skirmisher")

upgrade2(troops,"alpine_recruit","alpine_levy","alpine_footman")
upgrade(troops,"alpine_footman","alpine_swordsman")
upgrade(troops,"alpine_swordsman","alpine_elite_swordsman")

upgrade2(troops,"alpine_levy","alpine_spearman","alpine_crossbowman")
upgrade2(troops,"alpine_spearman","alpine_trained_spearman", "alpine_scout")
upgrade(troops,"alpine_scout","alpine_horseman")
upgrade(troops,"alpine_trained_spearman","alpine_veteran_spearman")
upgrade(troops,"alpine_veteran_spearman","alpine_man_at_arms")

upgrade(troops,"alpine_crossbowman","alpine_trained_crossbowman")
upgrade(troops,"alpine_trained_crossbowman","alpine_veteran_crossbowman") #new 1.126
upgrade(troops,"alpine_veteran_crossbowman","alpine_sharpshooter")


upgrade(troops,"solarian_recruit","solarian_footman")

upgrade2(troops,"solarian_footman","solarian_veteran_footman","solarian_skirmisher")
upgrade2(troops,"solarian_veteran_footman","solarian_horseman","solarian_infantry")
upgrade(troops,"solarian_infantry","solarian_guard")
upgrade(troops,"solarian_skirmisher","solarian_archer")

upgrade(troops,"solarian_archer","solarian_master_archer")

upgrade(troops,"solarian_horseman","solarian_knight")


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
upgrade(troops,"dark_cultist","occultist")
upgrade2(troops,"occultist","veilweaver","veiled_inquisitor")

#new tree connections
upgrade(troops,"mountain_bandit","alpine_recruit")
upgrade(troops,"forest_bandit","silver_rose_levy")
upgrade(troops,"steppe_bandit","steppe_bandit_warrior")
upgrade(troops,"steppe_bandit_warrior","steppe_bandit_leader")

upgrade(troops,"taiga_bandit","chornovalley_recruit")
upgrade(troops,"sea_raider","iron_crown_recruit")
upgrade(troops,"desert_bandit","desert_bandit_master")
upgrade2(troops,"desert_bandit_master","desert_bandit_horseman","desert_bandit_ronin")
upgrade(troops,"desert_bandit_horseman","desert_bandit_leader")
#new tree connections ended

# upgrade2(troops,"bandit","brigand","mercenary_swordsman")
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
