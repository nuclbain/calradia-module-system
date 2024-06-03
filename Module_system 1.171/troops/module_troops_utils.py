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


def wpe(m, a, c, t):
    n = 0
    n |= wp_one_handed(m)
    n |= wp_two_handed(m)
    n |= wp_polearm(m)
    n |= wp_archery(a)
    n |= wp_crossbow(c)
    n |= wp_throwing(t)
    return n


def wpex(o, w, p, a, c, t):
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


# Skills
knows_common = (
    knows_riding_1
    | knows_trade_2
    | knows_inventory_management_2
    | knows_prisoner_management_1
    | knows_leadership_1
)
knows_common_multiplayer = (
    knows_trade_10
    | knows_inventory_management_10
    | knows_prisoner_management_10
    | knows_leadership_10
    | knows_spotting_10
    | knows_pathfinding_10
    | knows_tracking_10
    | knows_engineer_10
    | knows_first_aid_10
    | knows_surgery_10
    | knows_wound_treatment_10
    | knows_tactics_10
    | knows_trainer_10
    | knows_looting_10
)
def_attrib = str_7 | agi_5 | int_4 | cha_4
tier_one_attrib = str_15 | agi_12 | int_8 | cha_8
tier_two_attrib = str_21 | agi_19 | int_12 | cha_12
tier_three_attrib = str_29 | agi_25 | int_16 | cha_16
def_attrib_multiplayer = int_30 | cha_30


knows_lord_1 = (
    knows_riding_3
    | knows_trade_2
    | knows_inventory_management_2
    | knows_tactics_4
    | knows_prisoner_management_4
    | knows_leadership_7
)

knows_warrior_npc = (
    knows_weapon_master_2
    | knows_ironflesh_1
    | knows_athletics_1
    | knows_power_strike_2
    | knows_riding_2
    | knows_shield_1
    | knows_inventory_management_2
)
knows_merchant_npc = (
    knows_riding_2 | knows_trade_3 | knows_inventory_management_3
)  # knows persuasion
knows_tracker_npc = (
    knows_weapon_master_1
    | knows_athletics_2
    | knows_spotting_2
    | knows_pathfinding_2
    | knows_tracking_2
    | knows_ironflesh_1
    | knows_inventory_management_2
)

lord_attrib = str_20 | agi_20 | int_20 | cha_20 | level(38)

knight_attrib_1 = str_15 | agi_14 | int_8 | cha_16 | level(22)
knight_attrib_2 = str_16 | agi_16 | int_10 | cha_18 | level(26)
knight_attrib_3 = str_18 | agi_17 | int_12 | cha_20 | level(30)
knight_attrib_4 = str_19 | agi_19 | int_13 | cha_22 | level(35)
knight_attrib_5 = str_20 | agi_20 | int_15 | cha_25 | level(41)
knight_skills_1 = (
    knows_riding_3
    | knows_ironflesh_2
    | knows_power_strike_3
    | knows_athletics_1
    | knows_tactics_2
    | knows_prisoner_management_1
    | knows_leadership_3
)
knight_skills_2 = (
    knows_riding_4
    | knows_ironflesh_3
    | knows_power_strike_4
    | knows_athletics_2
    | knows_tactics_3
    | knows_prisoner_management_2
    | knows_leadership_5
)
knight_skills_3 = (
    knows_riding_5
    | knows_ironflesh_4
    | knows_power_strike_5
    | knows_athletics_3
    | knows_tactics_4
    | knows_prisoner_management_2
    | knows_leadership_6
)
knight_skills_4 = (
    knows_riding_6
    | knows_ironflesh_5
    | knows_power_strike_6
    | knows_athletics_4
    | knows_tactics_5
    | knows_prisoner_management_3
    | knows_leadership_7
)
knight_skills_5 = (
    knows_riding_7
    | knows_ironflesh_6
    | knows_power_strike_7
    | knows_athletics_5
    | knows_tactics_6
    | knows_prisoner_management_3
    | knows_leadership_9
)

# These face codes are generated by the in-game face generator.
# Enable edit mode and press ctrl+E in face generator screen to obtain face codes.


reserved = 0

no_scene = 0

swadian_face_younger_1 = (
    0x0000000000000001124000000020000000000000001C00800000000000000000
)
swadian_face_young_1 = (
    0x0000000400000001124000000020000000000000001C00800000000000000000
)
swadian_face_middle_1 = (
    0x0000000800000001124000000020000000000000001C00800000000000000000
)
swadian_face_old_1 = 0x0000000D00000001124000000020000000000000001C00800000000000000000
swadian_face_older_1 = (
    0x0000000FC0000001124000000020000000000000001C00800000000000000000
)

swadian_face_younger_2 = (
    0x00000000000062C76DDCDF7FEEFBFFFF00000000001EFDBC0000000000000000
)
swadian_face_young_2 = (
    0x00000003C00062C76DDCDF7FEEFBFFFF00000000001EFDBC0000000000000000
)
swadian_face_middle_2 = (
    0x00000007C00062C76DDCDF7FEEFBFFFF00000000001EFDBC0000000000000000
)
swadian_face_old_2 = 0x0000000BC00062C76DDCDF7FEEFBFFFF00000000001EFDBC0000000000000000
swadian_face_older_2 = (
    0x0000000FC00062C76DDCDF7FEEFBFFFF00000000001EFDBC0000000000000000
)

vaegir_face_younger_1 = (
    0x0000000000000001124000000020000000000000001C00800000000000000000
)
vaegir_face_young_1 = 0x0000000400000001124000000020000000000000001C00800000000000000000
vaegir_face_middle_1 = (
    0x0000000800000001124000000020000000000000001C00800000000000000000
)
vaegir_face_old_1 = 0x0000000D00000001124000000020000000000000001C00800000000000000000
vaegir_face_older_1 = 0x0000000FC0000001124000000020000000000000001C00800000000000000000

vaegir_face_younger_2 = (
    0x000000003F00230C4DEEFFFFFFFFFFFF00000000001EFFF90000000000000000
)
vaegir_face_young_2 = 0x00000003BF00230C4DEEFFFFFFFFFFFF00000000001EFFF90000000000000000
vaegir_face_middle_2 = (
    0x00000007BF00230C4DEEFFFFFFFFFFFF00000000001EFFF90000000000000000
)
vaegir_face_old_2 = 0x0000000CBF00230C4DEEFFFFFFFFFFFF00000000001EFFF90000000000000000
vaegir_face_older_2 = 0x0000000FF100230C4DEEFFFFFFFFFFFF00000000001EFFF90000000000000000

khergit_face_younger_1 = (
    0x0000000009003109207000000000000000000000001C80470000000000000000
)
khergit_face_young_1 = (
    0x00000003C9003109207000000000000000000000001C80470000000000000000
)
khergit_face_middle_1 = (
    0x00000007C9003109207000000000000000000000001C80470000000000000000
)
khergit_face_old_1 = 0x0000000B89003109207000000000000000000000001C80470000000000000000
khergit_face_older_1 = (
    0x0000000FC9003109207000000000000000000000001C80470000000000000000
)

khergit_face_younger_2 = (
    0x000000003F0061CD6D7FFBDF9DF6EBEE00000000001FFB7F0000000000000000
)
khergit_face_young_2 = (
    0x00000003BF0061CD6D7FFBDF9DF6EBEE00000000001FFB7F0000000000000000
)
khergit_face_middle_2 = (
    0x000000077F0061CD6D7FFBDF9DF6EBEE00000000001FFB7F0000000000000000
)
khergit_face_old_2 = 0x0000000B3F0061CD6D7FFBDF9DF6EBEE00000000001FFB7F0000000000000000
khergit_face_older_2 = (
    0x0000000FFF0061CD6D7FFBDF9DF6EBEE00000000001FFB7F0000000000000000
)

nord_face_younger_1 = 0x0000000000000001124000000020000000000000001C00800000000000000000
nord_face_young_1 = 0x0000000400000001124000000020000000000000001C00800000000000000000
nord_face_middle_1 = 0x0000000800000001124000000020000000000000001C00800000000000000000
nord_face_old_1 = 0x0000000D00000001124000000020000000000000001C00800000000000000000
nord_face_older_1 = 0x0000000FC0000001124000000020000000000000001C00800000000000000000

nord_face_younger_2 = 0x00000000310023084DEEFFFFFFFFFFFF00000000001EFFF90000000000000000
nord_face_young_2 = 0x00000003B10023084DEEFFFFFFFFFFFF00000000001EFFF90000000000000000
nord_face_middle_2 = 0x00000008310023084DEEFFFFFFFFFFFF00000000001EFFF90000000000000000
nord_face_old_2 = 0x0000000C710023084DEEFFFFFFFFFFFF00000000001EFFF90000000000000000
nord_face_older_2 = 0x0000000FF10023084DEEFFFFFFFFFFFF00000000001EFFF90000000000000000

rhodok_face_younger_1 = (
    0x0000000009002003140000000000000000000000001C80400000000000000000
)
rhodok_face_young_1 = 0x0000000449002003140000000000000000000000001C80400000000000000000
rhodok_face_middle_1 = (
    0x0000000849002003140000000000000000000000001C80400000000000000000
)
rhodok_face_old_1 = 0x0000000CC9002003140000000000000000000000001C80400000000000000000
rhodok_face_older_1 = 0x0000000FC9002003140000000000000000000000001C80400000000000000000

rhodok_face_younger_2 = (
    0x00000000000062C76DDCDF7FEEFBFFFF00000000001EFDBC0000000000000000
)
rhodok_face_young_2 = 0x00000003C00062C76DDCDF7FEEFBFFFF00000000001EFDBC0000000000000000
rhodok_face_middle_2 = (
    0x00000007C00062C76DDCDF7FEEFBFFFF00000000001EFDBC0000000000000000
)
rhodok_face_old_2 = 0x0000000BC00062C76DDCDF7FEEFBFFFF00000000001EFDBC0000000000000000
rhodok_face_older_2 = 0x0000000FC00062C76DDCDF7FEEFBFFFF00000000001EFDBC0000000000000000

man_face_younger_1 = 0x0000000000000001124000000020000000000000001C00800000000000000000
man_face_young_1 = 0x0000000400000001124000000020000000000000001C00800000000000000000
man_face_middle_1 = 0x0000000800000001124000000020000000000000001C00800000000000000000
man_face_old_1 = 0x0000000D00000001124000000020000000000000001C00800000000000000000
man_face_older_1 = 0x0000000FC0000001124000000020000000000000001C00800000000000000000

man_face_younger_2 = 0x000000003F0052064DEEFFFFFFFFFFFF00000000001EFFF90000000000000000
man_face_young_2 = 0x00000003BF0052064DEEFFFFFFFFFFFF00000000001EFFF90000000000000000
man_face_middle_2 = 0x00000007BF0052064DEEFFFFFFFFFFFF00000000001EFFF90000000000000000
man_face_old_2 = 0x0000000BFF0052064DEEFFFFFFFFFFFF00000000001EFFF90000000000000000
man_face_older_2 = 0x0000000FFF0052064DEEFFFFFFFFFFFF00000000001EFFF90000000000000000

merchant_face_1 = man_face_young_1
merchant_face_2 = man_face_older_2

woman_face_1 = 0x0000000000000001000000000000000000000000001C00000000000000000000
woman_face_2 = 0x00000003BF0030067FF7FBFFEFFF6DFF00000000001F6DBF0000000000000000

swadian_woman_face_1 = (
    0x0000000180102006124925124928924900000000001C92890000000000000000
)
swadian_woman_face_2 = (
    0x00000001BF1000061DB6D75DB6B6DBAD00000000001C92890000000000000000
)

khergit_woman_face_1 = (
    0x0000000180103006124925124928924900000000001C92890000000000000000
)
khergit_woman_face_2 = (
    0x00000001AF1030025B6EB6DD6DB6DD6D00000000001EEDAE0000000000000000
)

refugee_face1 = woman_face_1
refugee_face2 = woman_face_2
girl_face1 = woman_face_1
girl_face2 = woman_face_2

skeleton_face1 = 0x0000000180000000000000000000000000000000000000000000000000000000
skeleton_face2 = 0x0000000180000000000000000000000000000000000000000000000000000000

mercenary_face_1 = 0x0000000000000000000000000000000000000000001C00000000000000000000
mercenary_face_2 = 0x0000000CFF00730B6DB6DB6DB7FBFFFF00000000001EFFFE0000000000000000

vaegir_face1 = vaegir_face_young_1
vaegir_face2 = vaegir_face_older_2

bandit_face1 = man_face_young_1
bandit_face2 = man_face_older_2

undead_face1 = 0x00000000002000000000000000000000
undead_face2 = 0x000000000020010000001FFFFFFFFFFF

# NAMES:
#

tf_guarantee_all = (
    tf_guarantee_boots
    | tf_guarantee_armor
    | tf_guarantee_gloves
    | tf_guarantee_helmet
    | tf_guarantee_horse
    | tf_guarantee_shield
    | tf_guarantee_ranged
)
tf_guarantee_all_wo_ranged = (
    tf_guarantee_boots
    | tf_guarantee_armor
    | tf_guarantee_gloves
    | tf_guarantee_helmet
    | tf_guarantee_horse
    | tf_guarantee_shield
)
