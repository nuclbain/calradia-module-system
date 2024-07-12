from module_constants import *
from ID_factions import *
from header_items import  *
from header_operations import *
from header_triggers import *

####################################################################################################################
#  Each item record contains the following fields:
#  1) Item id: used for referencing items in other files.
#     The prefix itm_ is automatically added before each item id.
#  2) Item name. Name of item as it'll appear in inventory window
#  3) List of meshes.  Each mesh record is a tuple containing the following fields:
#    3.1) Mesh name.
#    3.2) Modifier bits that this mesh matches.
#     Note that the first mesh record is the default.
#  4) Item flags. See header_items.py for a list of available flags.
#  5) Item capabilities. Used for which animations this item is used with. See header_items.py for a list of available flags.
#  6) Item value.
#  7) Item stats: Bitwise-or of various stats about the item such as:
#      weight, abundance, difficulty, head_armor, body_armor,leg_armor, etc...
#  8) Modifier bits: Modifiers that can be applied to this item.
#  9) [Optional] Triggers: List of simple triggers to be associated with the item.
#  10) [Optional] Factions: List of factions that item can be found as merchandise.
####################################################################################################################

# Some constants for ease of use.
imodbits_none = 0
imodbits_horse_basic = imodbit_swaybacked|imodbit_lame|imodbit_spirited|imodbit_heavy|imodbit_stubborn
imodbits_cloth  = imodbit_tattered | imodbit_ragged | imodbit_sturdy | imodbit_thick | imodbit_hardened
imodbits_armor  = imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_plate  = imodbit_cracked | imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_polearm = imodbit_cracked | imodbit_bent | imodbit_balanced
imodbits_shield  = imodbit_cracked | imodbit_battered |imodbit_thick | imodbit_reinforced
imodbits_sword   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered
imodbits_sword_high   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered|imodbit_masterwork
imodbits_axe   = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_mace   = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_pick   = imodbit_rusty | imodbit_chipped | imodbit_balanced | imodbit_heavy
imodbits_bow = imodbit_cracked | imodbit_bent | imodbit_strong |imodbit_masterwork
imodbits_crossbow = imodbit_cracked | imodbit_bent | imodbit_masterwork
imodbits_missile   = imodbit_bent | imodbit_large_bag
imodbits_thrown   = imodbit_bent | imodbit_heavy| imodbit_balanced| imodbit_large_bag
imodbits_thrown_minus_heavy = imodbit_bent | imodbit_balanced| imodbit_large_bag

imodbits_horse_good = imodbit_spirited|imodbit_heavy
imodbits_good   = imodbit_sturdy | imodbit_thick | imodbit_hardened | imodbit_reinforced
imodbits_bad    = imodbit_rusty | imodbit_chipped | imodbit_tattered | imodbit_ragged | imodbit_cracked | imodbit_bent
# Replace winged mace/spiked mace with: Flanged mace / Knobbed mace?
# Fauchard (majowski glaive) 
items = [
# item_name, mesh_name, item_properties, item_capabilities, slot_no, cost, bonus_flags, weapon_flags, scale, view_dir, pos_offset
 ["no_item","INVALID ITEM", [("invalid_item",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],

 ["tutorial_spear", "Spear", [("spear",0)], itp_type_polearm| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear, 0 , weight(4.5)|difficulty(0)|spd_rtng(80) | weapon_length(158)|swing_damage(0 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm ],
 ["tutorial_club", "Club", [("club_v3",0)], itp_type_one_handed_wpn| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar, 0 , weight(2.5)|difficulty(0)|spd_rtng(95) | weapon_length(95)|swing_damage(11 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
 ["tutorial_battle_axe", "Battle Axe", [("battle_ax",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(5)|difficulty(0)|spd_rtng(88) | weapon_length(108)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["tutorial_arrows","Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(3)|abundance(160)|weapon_length(95)|thrust_damage(0,pierce)|max_ammo(20),imodbits_missile],
 ["tutorial_bolts","Bolts", [("crusade_bolt",0),("flying_missile",ixmesh_flying_ammo),("crusade_bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|abundance(90)|weapon_length(55)|thrust_damage(0,pierce)|max_ammo(18),imodbits_missile],
 ["tutorial_short_bow", "Short Bow", [("short_bow",0),("short_bow_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 0 , weight(1)|difficulty(0)|spd_rtng(98) | shoot_speed(49) | thrust_damage(12 ,  pierce  ),imodbits_bow ],
 ["tutorial_crossbow", "Crossbow", [("crossbow",0)], itp_type_crossbow |itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 0 , weight(3)|difficulty(0)|spd_rtng(42)|  shoot_speed(68) | thrust_damage(32,pierce)|max_ammo(1),imodbits_crossbow ],
 ["tutorial_throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|difficulty(0)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16 ,  cut)|max_ammo(14)|weapon_length(0),imodbits_missile ],
 ["tutorial_saddle_horse", "Saddle Horse", [("saddle_horse",0)], itp_type_horse, 0, 0,abundance(90)|body_armor(3)|difficulty(0)|horse_speed(40)|horse_maneuver(38)|horse_charge(8),imodbits_horse_basic],
 ["tutorial_shield", "Kite Shield", [("shield_kite_a",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(150),imodbits_shield ],
 ["tutorial_staff_no_attack","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_parry_polearm|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(0,blunt) | thrust_damage(0,blunt),imodbits_none],
 ["tutorial_staff","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(16,blunt) | thrust_damage(16,blunt),imodbits_none],
 ["tutorial_sword", "Sword", [("long_sword",0),("scab_longsw_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 0 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(102)|swing_damage(18 , cut) | thrust_damage(15 ,  pierce),imodbits_sword ],
 ["tutorial_axe", "Axe", [("luc_iron_ax",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(4)|difficulty(0)|spd_rtng(91) | weapon_length(108)|swing_damage(19 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

 ["tutorial_dagger","Dagger", [("practice_dagger",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(40)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],


 ["horse_meat","Horse Meat", [("raw_meat",0)], itp_type_goods|itp_consumable|itp_food, 0, 12,weight(40)|food_quality(30)|max_ammo(40),imodbits_none],
# Items before this point are hardwired and their order should not be changed!
 ["practice_sword","Practice Sword", [("practice_sword",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_wooden_parry|itp_wooden_attack, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(22,blunt)|thrust_damage(20,blunt),imodbits_none],
 ["heavy_practice_sword","Heavy Practice Sword", [("heavy_practicesword",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_wooden_parry|itp_wooden_attack, itc_greatsword,
    21, weight(6.25)|spd_rtng(94)|weapon_length(128)|swing_damage(30,blunt)|thrust_damage(24,blunt),imodbits_none],
 ["practice_dagger","Practice Dagger", [("practice_dagger",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry|itp_wooden_attack, itc_dagger|itcf_carry_dagger_front_left, 2,weight(0.5)|spd_rtng(110)|weapon_length(47)|swing_damage(16,blunt)|thrust_damage(14,blunt),imodbits_none],
 ["practice_axe", "Practice Axe", [("hatchet_k2",0)], itp_type_one_handed_wpn| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 24 , weight(2) | spd_rtng(95) | weapon_length(75) | swing_damage(24, blunt) | thrust_damage(0, pierce), imodbits_axe],
 ["arena_axe", "Axe", [("arena_axe",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 137 , weight(1.5)|spd_rtng(100) | weapon_length(69)|swing_damage(24 , blunt) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["arena_sword", "Sword", [("arena_sword_one_handed",0),("sword_medieval_b_scabbard", ixmesh_carry),], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 243 , weight(1.5)|spd_rtng(99) | weapon_length(95)|swing_damage(22 , blunt) | thrust_damage(20 ,  blunt),imodbits_sword_high ],
 ["arena_sword_two_handed",  "Two Handed Sword", [("arena_sword_two_handed",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back,
 670 , weight(2.75)|spd_rtng(93) | weapon_length(110)|swing_damage(30 , blunt) | thrust_damage(24 ,  blunt),imodbits_sword_high ],
 ["arena_lance",         "Lance", [("arena_lance",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff|itcf_carry_spear,
 90 , weight(2.5)|spd_rtng(96) | weapon_length(150)|swing_damage(20 , blunt) | thrust_damage(25 ,  blunt),imodbits_polearm ],
 ["practice_staff","Practice Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,9, weight(2.5)|spd_rtng(103) | weapon_length(118)|swing_damage(18,blunt) | thrust_damage(18,blunt),imodbits_none],
 ["practice_lance","Practice Lance", [("joust_of_peace",0)], itp_couchable|itp_type_polearm|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_greatlance, 18,weight(4.25)|spd_rtng(58)|weapon_length(240)|swing_damage(0,blunt)|thrust_damage(15,blunt),imodbits_none],
 ["practice_shield","Practice Shield", [("shield_round_a",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 20,weight(3.5)|body_armor(1)|hit_points(200)|spd_rtng(100)|shield_width(50),imodbits_none],
 ["practice_bow","Practice Bow", [("hunting_bow",0), ("hunting_bow_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bow_back, 0, weight(1.5)|spd_rtng(90) | shoot_speed(40) | thrust_damage(21, blunt),imodbits_bow ],
##                                                     ("hunting_bow",0)],                  itp_type_bow|itp_two_handed|itp_primary|itp_attach_left_hand, itcf_shoot_bow, 4,weight(1.5)|spd_rtng(90)|shoot_speed(40)|thrust_damage(19,blunt),imodbits_none],
 ["practice_crossbow", "Practice Crossbow", [("crusaders_crossbows_a",0)], itp_type_crossbow |itp_primary|itp_two_handed ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 0, weight(3)|spd_rtng(42)| shoot_speed(68) | thrust_damage(32,blunt)|max_ammo(1),imodbits_crossbow],
 ["practice_javelin", "Practice Javelins", [("javelin",0),("javelins_quiver_new", ixmesh_carry)], itp_type_thrown |itp_primary|itp_next_item_as_melee,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 0, weight(5) | spd_rtng(91) | shoot_speed(28) | thrust_damage(27, blunt) | max_ammo(50) | weapon_length(75), imodbits_thrown],
 ["practice_javelin_melee", "practice_javelin_melee", [("javelin",0)], itp_type_polearm|itp_primary|itp_penalty_with_shield|itp_wooden_parry , itc_staff, 0, weight(1)|difficulty(0)|spd_rtng(91) |swing_damage(12, blunt)| thrust_damage(14,  blunt)|weapon_length(75),imodbits_polearm ],
 ["practice_throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16, blunt)|max_ammo(10)|weapon_length(0),imodbits_thrown ],
 ["practice_throwing_daggers_100_amount", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16, blunt)|max_ammo(100)|weapon_length(0),imodbits_thrown ],
# ["cheap_shirt","Cheap Shirt", [("shirt",0)], itp_type_body_armor|itp_covers_legs, 0, 4,weight(1.25)|body_armor(3),imodbits_none],
 ["practice_horse","Practice Horse", [("saddle_horse",0)], itp_type_horse, 0, 37,body_armor(10)|horse_speed(40)|horse_maneuver(37)|horse_charge(14),imodbits_none],
 ["practice_arrows","Practice Arrows", [("arena_arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(80),imodbits_missile],
## ["practice_arrows","Practice Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo)], itp_type_arrows, 0, 31,weight(1.5)|weapon_length(95)|max_ammo(80),imodbits_none],
 ["practice_bolts","Practice Bolts", [("crusade_bolt",0),("flying_missile",ixmesh_flying_ammo),("crusade_bolt_bag", ixmesh_carry),("crusade_bolt_bag", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|weapon_length(55)|max_ammo(49),imodbits_missile],
 ["practice_arrows_10_amount","Practice Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(10),imodbits_missile],
 ["practice_arrows_100_amount","Practice Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(100),imodbits_missile],
 ["practice_bolts_9_amount","Practice Bolts", [("crusade_bolt",0),("flying_missile",ixmesh_flying_ammo),("crusade_bolt_bag", ixmesh_carry),("crusade_bolt_bag", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|weapon_length(55)|max_ammo(9),imodbits_missile],
 ["practice_boots", "Practice Boots", [("boot_nomad_a",0)], itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 11 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10), imodbits_cloth ],
 ["red_tourney_armor","Red Tourney Armor", [("tourn_armor_a",0)], itp_type_body_armor|itp_covers_legs, 0, 152,weight(15.0)|body_armor(20)|leg_armor(6),imodbits_none],
 ["blue_tourney_armor","Blue Tourney Armor", [("mail_shirt",0)], itp_type_body_armor|itp_covers_legs, 0, 152,weight(15.0)|body_armor(20)|leg_armor(6),imodbits_none],
 ["green_tourney_armor","Green Tourney Armor", [("leather_vest",0)], itp_type_body_armor|itp_covers_legs, 0, 152,weight(15.0)|body_armor(20)|leg_armor(6),imodbits_none],
 ["gold_tourney_armor","Gold Tourney Armor", [("padded_armor",0)], itp_type_body_armor|itp_covers_legs, 0, 152,weight(15.0)|body_armor(20)|leg_armor(6),imodbits_none],
 ["red_tourney_helmet","Red Tourney Helmet",[("flattop_helmet",0)],itp_type_head_armor,0,126, weight(2)|head_armor(16),imodbits_none],
 ["blue_tourney_helmet","Blue Tourney Helmet",[("segmented_helm",0)],itp_type_head_armor,0,126, weight(2)|head_armor(16),imodbits_none],
 ["green_tourney_helmet","Green Tourney Helmet",[("hood_c",0)],itp_type_head_armor,0,126, weight(2)|head_armor(16),imodbits_none],
 ["gold_tourney_helmet","Gold Tourney Helmet",[("hood_a",0)],itp_type_head_armor,0,126, weight(2)|head_armor(16),imodbits_none],

["arena_shield_red", "Shield", [("arena_shield_red",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|weapon_length(60),imodbits_shield ],
["arena_shield_blue", "Shield", [("arena_shield_blue",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|weapon_length(60),imodbits_shield ],
["arena_shield_green", "Shield", [("arena_shield_green",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|weapon_length(60),imodbits_shield ],
["arena_shield_yellow", "Shield", [("arena_shield_yellow",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|weapon_length(60),imodbits_shield ],

["arena_armor_white", "Arena Armor White", [("Arena_Armor_White",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
["arena_armor_red", "Arena Armor Red", [("Arena_Armor_Red",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
["arena_armor_blue", "Arena Armor Blue", [("Arena_Armor_Blue",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
["arena_armor_green", "Arena Armor Green", [("Arena_Armor_Green",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
["arena_armor_yellow", "Arena Armor Yellow", [("Arena_Armor_Yellow",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
["arena_tunic_white", "Arena Tunic White ", [("Arena_Shirt_A",0)], itp_type_body_armor |itp_covers_legs ,0, 47 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth ],
["arena_tunic_red", "Arena Tunic Red", [("Arena_Shirt_E",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth ], 
["arena_tunic_blue", "Arena Tunic Blue", [("Arena_Shirt_C",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth ], 
["arena_tunic_green", "Arena Tunic Green", [("Arena_Shirt_B",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth ],
["arena_tunic_yellow", "Arena Tunic Yellow", [("Arena_Shirt_D",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth ],
#headwear
["arena_helmet_red", "Arena Helmet Red", [("arena_helmetR",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_helmet_blue", "Arena Helmet Blue", [("arena_helmetB",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_helmet_green", "Arena Helmet Green", [("arena_helmetG",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_helmet_yellow", "Arena Helmet Yellow", [("arena_helmetY",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["steppe_helmet_white", "Steppe Helmet White", [("steppe_helmetW",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate ], 
["steppe_helmet_red", "Steppe Helmet Red", [("steppe_helmetR",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate ], 
["steppe_helmet_blue", "Steppe Helmet Blue", [("steppe_helmetB",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate ], 
["steppe_helmet_green", "Steppe Helmet Green", [("steppe_helmetG",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate ], 
["steppe_helmet_yellow", "Steppe Helmet Yellow", [("steppe_helmetY",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate ], 
["tourney_helm_white", "Tourney Helm White", [("tourney_helmR",0)], itp_type_head_armor|itp_covers_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["tourney_helm_red", "Tourney Helm Red", [("tourney_helmR",0)], itp_type_head_armor|itp_covers_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["tourney_helm_blue", "Tourney Helm Blue", [("tourney_helmB",0)], itp_type_head_armor|itp_covers_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["tourney_helm_green", "Tourney Helm Green", [("tourney_helmG",0)], itp_type_head_armor|itp_covers_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["tourney_helm_yellow", "Tourney Helm Yellow", [("tourney_helmY",0)], itp_type_head_armor|itp_covers_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_turban_red", "Arena Turban", [("tuareg_open",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_turban_blue", "Arena Turban", [("tuareg_open",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_turban_green", "Arena Turban", [("tuareg_open",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_turban_yellow", "Arena Turban", [("tuareg_open",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],

# A treatise on The Method of Mechanical Theorems Archimedes
 
#This book must be at the beginning of readable books
 ["book_tactics","De Re Militari", [("book_a",0)], itp_type_book, 0, 4000,weight(2)|abundance(100),imodbits_none],
 ["book_persuasion","Rhetorica ad Herennium", [("book_b",0)], itp_type_book, 0, 5000,weight(2)|abundance(100),imodbits_none],
 ["book_leadership","The Life of Alixenus the Great", [("book_d",0)], itp_type_book, 0, 4200,weight(2)|abundance(100),imodbits_none],
 ["book_intelligence","Essays on Logic", [("book_e",0)], itp_type_book, 0, 2900,weight(2)|abundance(100),imodbits_none],
 ["book_trade","A Treatise on the Value of Things", [("book_f",0)], itp_type_book, 0, 3100,weight(2)|abundance(100),imodbits_none],
 ["book_weapon_mastery", "On the Art of Fighting with Swords", [("book_d",0)], itp_type_book, 0, 4200,weight(2)|abundance(100),imodbits_none],
 ["book_engineering","Method of Mechanical Theorems", [("book_open",0)], itp_type_book, 0, 4000,weight(2)|abundance(100),imodbits_none],

#Reference books
#This book must be at the beginning of reference books
 ["book_wound_treatment_reference","The Book of Healing", [("book_c",0)], itp_type_book, 0, 3500,weight(2)|abundance(100),imodbits_none],
 ["book_training_reference","Manual of Arms", [("book_open",0)], itp_type_book, 0, 3500,weight(2)|abundance(100),imodbits_none],
 ["book_surgery_reference","The Great Book of Surgery", [("book_c",0)], itp_type_book, 0, 3500,weight(2)|abundance(100),imodbits_none],

 #other trade goods (first one is spice)
 ["spice","Spice", [("spice_sack",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 880,weight(40)|abundance(25)|max_ammo(50),imodbits_none],
 ["salt","Salt", [("salt_sack",0)], itp_merchandise|itp_type_goods, 0, 255,weight(50)|abundance(120),imodbits_none],


 #["flour","Flour", [("salt_sack",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 40,weight(50)|abundance(100)|food_quality(45)|max_ammo(50),imodbits_none],

 ["oil","Oil", [("oil",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 450,weight(50)|abundance(60)|max_ammo(50),imodbits_none],

 ["pottery","Pottery", [("jug",0)], itp_merchandise|itp_type_goods, 0, 100,weight(50)|abundance(90),imodbits_none],

 ["raw_flax","Flax Bundle", [("raw_flax",0)], itp_merchandise|itp_type_goods, 0, 150,weight(40)|abundance(90),imodbits_none],
 ["linen","Linen", [("linen",0)], itp_merchandise|itp_type_goods, 0, 250,weight(40)|abundance(90),imodbits_none],

 ["wool","Wool", [("wool_sack",0)], itp_merchandise|itp_type_goods, 0, 130,weight(40)|abundance(90),imodbits_none],
 ["wool_cloth","Wool Cloth", [("wool_cloth",0)], itp_merchandise|itp_type_goods, 0, 250,weight(40)|abundance(90),imodbits_none],

 ["raw_silk","Raw Silk", [("raw_silk_bundle",0)], itp_merchandise|itp_type_goods, 0, 600,weight(30)|abundance(90),imodbits_none],
 ["raw_dyes","Dyes", [("dyes",0)], itp_merchandise|itp_type_goods, 0, 200,weight(10)|abundance(90),imodbits_none],
 ["velvet","Velvet", [("velvet",0)], itp_merchandise|itp_type_goods, 0, 1025,weight(40)|abundance(30),imodbits_none],

 ["cheap_smithing_material","Common Materials", [("Common_Materials",0), ("Common_Materials.1",0), ("Common_Materials.2",0)], itp_merchandise|itp_type_goods, 0,120,weight(60)|abundance(60),imodbits_none],
 ["regular_smithing_material","Uncommon Materials", [("Uncommon_Materials",0), ("Uncommon_Materials.1",0), ("Uncommon_Materials.2",0)], itp_merchandise|itp_type_goods, 0,400,weight(60)|abundance(60),imodbits_none],
 ["expensive_smithing_material","Rare Materials", [("Rare_Materials",0), ("Rare_Materials.1",0), ("Rare_Materials.2",0)], itp_merchandise|itp_type_goods, 0,1200,weight(60)|abundance(60),imodbits_none],
 ["iron","Iron", [("iron",0)], itp_merchandise|itp_type_goods, 0,264,weight(60)|abundance(60),imodbits_none],
 ["tools","Tools", [("iron_hammer",0)], itp_merchandise|itp_type_goods, 0, 410,weight(50)|abundance(90),imodbits_none],
 ["weaponsmith_tools","Weaponsmith Toolkit", [("Weaponsmith_Tools",0), ("Weaponsmith_Tools.1",0), ("Weaponsmith_Tools.2",0)], itp_merchandise|itp_type_goods, 0, 2500,weight(50)|abundance(90),imodbits_none],
 ["armorer_tools","Armorer Toolkit", [("Armorer_Tools",0), ("Armorer_Tools.1",0), ("Armorer_Tools.2",0)], itp_merchandise|itp_type_goods, 0, 2500,weight(50)|abundance(90),imodbits_none],

 ["raw_leather","Hides", [("leatherwork_inventory",0)], itp_merchandise|itp_type_goods, 0, 120,weight(40)|abundance(90),imodbits_none],
 ["leatherwork","Leatherwork", [("leatherwork_frame",0)], itp_merchandise|itp_type_goods, 0, 220,weight(40)|abundance(90),imodbits_none],
 
 ["raw_date_fruit","Date Fruit", [("date_inventory",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 120,weight(40)|food_quality(10)|max_ammo(10),imodbits_none],
 ["furs","Furs", [("fur_pack",0)], itp_merchandise|itp_type_goods, 0, 391,weight(40)|abundance(90),imodbits_none],

 ["wine","Wine", [("amphora_slim",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 220,weight(30)|abundance(60)|max_ammo(50),imodbits_none],
 ["ale","Ale", [("ale_barrel",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 120,weight(30)|abundance(70)|max_ammo(50),imodbits_none],

# ["dry_bread", "wheat_sack", itp_type_goods|itp_consumable, 0, slt_none,view_goods,95,weight(2),max_ammo(50),imodbits_none],
#foods (first one is smoked_fish)
 ["smoked_fish","Smoked Fish", [("smoked_fish",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 65,weight(15)|abundance(110)|food_quality(50)|max_ammo(50),imodbits_none],
 ["cheese","Cheese", [("cheese_b",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 75,weight(6)|abundance(110)|food_quality(40)|max_ammo(30),imodbits_none],
 ["honey","Honey", [("honey_pot",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 220,weight(5)|abundance(110)|food_quality(40)|max_ammo(30),imodbits_none],
 ["sausages","Sausages", [("sausages",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 85,weight(10)|abundance(110)|food_quality(40)|max_ammo(40),imodbits_none],
 ["cabbages","Cabbages", [("cabbage",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 30,weight(15)|abundance(110)|food_quality(40)|max_ammo(50),imodbits_none],
 ["dried_meat","Dried Meat", [("smoked_meat",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 85,weight(15)|abundance(100)|food_quality(70)|max_ammo(50),imodbits_none],
 ["apples","Fruit", [("apple_basket",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 44,weight(20)|abundance(110)|food_quality(40)|max_ammo(50),imodbits_none],
 ["raw_grapes","Grapes", [("grapes_inventory",0)], itp_merchandise|itp_consumable|itp_type_goods, 0, 75,weight(40)|abundance(90)|food_quality(10)|max_ammo(10),imodbits_none], #x2 for wine
 ["raw_olives","Olives", [("olive_inventory",0)], itp_merchandise|itp_consumable|itp_type_goods, 0, 100,weight(40)|abundance(90)|food_quality(10)|max_ammo(10),imodbits_none], #x3 for oil
 ["grain","Grain", [("wheat_sack",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 30,weight(30)|abundance(110)|food_quality(40)|max_ammo(50),imodbits_none],

 ["cattle_meat","Beef", [("raw_meat",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 80,weight(20)|abundance(100)|food_quality(80)|max_ammo(50),imodbits_none],
 ["bread","Bread", [("bread_a",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 50,weight(30)|abundance(110)|food_quality(40)|max_ammo(50),imodbits_none],
 ["chicken","Chicken", [("chicken",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 95,weight(10)|abundance(110)|food_quality(40)|max_ammo(50),imodbits_none],
 ["pork","Pork", [("pork",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 75,weight(15)|abundance(100)|food_quality(70)|max_ammo(50),imodbits_none],
 ["butter","Butter", [("butter_pot",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 150,weight(6)|abundance(110)|food_quality(40)|max_ammo(30),imodbits_none],
 

 #Would like to remove flour altogether and reduce chicken, pork and butter (perishables) to non-trade items. Apples could perhaps become a generic "fruit", also representing dried fruit and grapes
 # Armagan: changed order so that it'll be easier to remove them from trade goods if necessary.
#************************************************************************************************
# ITEMS before this point are hardcoded into item_codes.h and their order should not be changed!
#************************************************************************************************

# Quest Items

 ["siege_supply","Supplies", [("ale_barrel",0)], itp_type_goods, 0, 96,weight(40)|abundance(70),imodbits_none],
 ["quest_wine","Wine", [("amphora_slim",0)], itp_type_goods, 0, 46,weight(40)|abundance(60)|max_ammo(50),imodbits_none],
 ["quest_ale","Ale", [("ale_barrel",0)], itp_type_goods, 0, 31,weight(40)|abundance(70)|max_ammo(50),imodbits_none],

 
# Tutorial Items

 ["tutorial_sword", "Sword", [("long_sword",0),("scab_longsw_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 0 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(102)|swing_damage(18 , cut) | thrust_damage(15 ,  pierce),imodbits_sword ],
 ["tutorial_axe", "Axe", [("luc_iron_ax",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(4)|difficulty(0)|spd_rtng(91) | weapon_length(108)|swing_damage(19 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["tutorial_spear", "Spear", [("spear",0)], itp_type_polearm| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear, 0 , weight(4.5)|difficulty(0)|spd_rtng(80) | weapon_length(158)|swing_damage(0 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm ],
 ["tutorial_club", "Club", [("club",0)], itp_type_one_handed_wpn| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar, 0 , weight(2.5)|difficulty(0)|spd_rtng(95) | weapon_length(95)|swing_damage(11 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
 ["tutorial_battle_axe", "Battle Axe", [("battle_ax",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(5)|difficulty(0)|spd_rtng(88) | weapon_length(108)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["tutorial_arrows","Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(3)|abundance(160)|weapon_length(95)|thrust_damage(0,pierce)|max_ammo(20),imodbits_missile],
 ["tutorial_bolts","Bolts", [("crusade_bolt",0),("flying_missile",ixmesh_flying_ammo),("crusade_bolt_bag", ixmesh_carry),("crusade_bolt_bag", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|abundance(90)|weapon_length(63)|thrust_damage(0,pierce)|max_ammo(18),imodbits_missile],
 ["tutorial_short_bow", "Short Bow", [("short_bow",0),("short_bow_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 0 , weight(1)|difficulty(0)|spd_rtng(98) | shoot_speed(49) | thrust_damage(12 ,  pierce  ),imodbits_bow ],
 ["tutorial_crossbow", "Crossbow", [("crusaders_crossbows_a",0)], itp_type_crossbow |itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 0 , weight(3)|difficulty(0)|spd_rtng(42)|  shoot_speed(68) | thrust_damage(32,pierce)|max_ammo(1),imodbits_crossbow ],
 ["tutorial_throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|difficulty(0)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16 ,  cut)|max_ammo(14)|weapon_length(0),imodbits_missile ],
 ["tutorial_saddle_horse", "Saddle Horse", [("saddle_horse",0)], itp_type_horse, 0, 0,abundance(90)|body_armor(3)|difficulty(0)|horse_speed(40)|horse_maneuver(38)|horse_charge(8),imodbits_horse_basic],
 ["tutorial_shield", "Kite Shield", [("shield_kite_a",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(150),imodbits_shield ],
 ["tutorial_staff_no_attack","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_parry_polearm|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(0,blunt) | thrust_damage(0,blunt),imodbits_none],
 ["tutorial_staff","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(16,blunt) | thrust_damage(16,blunt),imodbits_none],

# Horses: sumpter horse/ pack horse, saddle horse, steppe horse, warm blood, geldling, stallion,   war mount, charger, 
# Carthorse, hunter, heavy hunter, hackney, palfrey, courser, destrier.

# imodbit_swaybacked|imodbit_lame|imodbit_spirited|imodbit_heavy|imodbit_stubborn
 ["sumpter_horse","Sumpter Horse", [("horse_bandits_a",0), ("horse_bandits_a.1",0), ("horse_bandits_a",0), ("horse_bandits_a.1",0)], itp_merchandise|itp_type_horse, 0, 134,abundance(90)|hit_points(100)|body_armor(14)|difficulty(1)|horse_speed(37)|horse_maneuver(39)|horse_charge(9)|horse_scale(100),imodbits_horse_basic],

 ["saddle_horse","Saddle Horse", [("horse_bandits_b",0),("horse_bandits_b.1",0)], itp_merchandise|itp_type_horse, 0, 240,abundance(90)|hit_points(100)|body_armor(8)|difficulty(1)|horse_speed(45)|horse_maneuver(44)|horse_charge(10)|horse_scale(104),imodbits_horse_basic],
 ["saddle_horse_b","Saddle Horse", [("horse_bandits_d",0),("horse_bandits_d.1",0)], itp_merchandise|itp_type_horse, 0, 240,abundance(90)|hit_points(100)|body_armor(8)|difficulty(1)|horse_speed(45)|horse_maneuver(44)|horse_charge(10)|horse_scale(104),imodbits_horse_basic],

 ["steppe_horse","Steppe Horse", [("bandits_horse_a",0),("bandits_horse_a.1",0)], itp_merchandise|itp_type_horse, 0, 192,abundance(80)|hit_points(120)|body_armor(10)|difficulty(2)|horse_speed(40)|horse_maneuver(51)|horse_charge(8)|horse_scale(98),imodbits_horse_basic, [], [fac_kingdom_2, fac_kingdom_3]],
 ["steppe_horse_b","Steppe Horse", [("bandits_horse_b",0),("bandits_horse_b.1",0)], itp_merchandise|itp_type_horse, 0, 192,abundance(80)|hit_points(120)|body_armor(10)|difficulty(2)|horse_speed(40)|horse_maneuver(51)|horse_charge(8)|horse_scale(98),imodbits_horse_basic, [], [fac_kingdom_2, fac_kingdom_3]],
 ["steppe_horse_c","Steppe Horse", [("bandits_horse_c",0),("bandits_horse_c.1",0)], itp_merchandise|itp_type_horse, 0, 192,abundance(80)|hit_points(120)|body_armor(10)|difficulty(2)|horse_speed(40)|horse_maneuver(51)|horse_charge(8)|horse_scale(98),imodbits_horse_basic, [], [fac_kingdom_2, fac_kingdom_3]],
 ["steppe_horse_d","Steppe Horse", [("bandits_horse_d",0),("bandits_horse_d.1",0)], itp_merchandise|itp_type_horse, 0, 201,abundance(80)|hit_points(130)|body_armor(13)|difficulty(2)|horse_speed(45)|horse_maneuver(54)|horse_charge(9)|horse_scale(98),imodbits_horse_basic, [], [fac_kingdom_2, fac_kingdom_3]],

 ["arabian_horse_a","Desert Horse", [("Arabs_horse_a",0), ("Arabs_horse_a.1",0)], itp_merchandise|itp_type_horse, 0, 550,abundance(80)|hit_points(110)|body_armor(10)|difficulty(2)|horse_speed(42)|horse_maneuver(50)|horse_charge(12)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_3, fac_kingdom_6]],
 ["arabian_horse_b","Desert Horse", [("Arabs_horse_b",0), ("Arabs_horse_b.1",0)], itp_merchandise|itp_type_horse, 0, 550,abundance(80)|hit_points(110)|body_armor(10)|difficulty(2)|horse_speed(42)|horse_maneuver(50)|horse_charge(12)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_3, fac_kingdom_6]],
 ["arabian_horse_c","Desert Horse", [("Arabs_horse_c",0), ("Arabs_horse_c.1",0)], itp_merchandise|itp_type_horse, 0, 550,abundance(80)|hit_points(110)|body_armor(10)|difficulty(2)|horse_speed(42)|horse_maneuver(50)|horse_charge(12)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_3, fac_kingdom_6]],
 ["arabian_horse_d","Desert Horse", [("Arabs_horse_d",0), ("Arabs_horse_d.1",0)], itp_merchandise|itp_type_horse, 0, 550,abundance(80)|hit_points(110)|body_armor(10)|difficulty(2)|horse_speed(42)|horse_maneuver(50)|horse_charge(12)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_3, fac_kingdom_6]],

 ["courser","Courser", [("horse_bandits_c",0),("horse_bandits_c.1",0)], itp_merchandise|itp_type_horse, 0, 600,abundance(70)|body_armor(12)|hit_points(110)|difficulty(2)|horse_speed(50)|horse_maneuver(44)|horse_charge(12)|horse_scale(106),imodbits_horse_basic|imodbit_champion],

 ["hunter","Hunter", [("European_horse_a",0),("European_horse_a.1",0)], itp_merchandise|itp_type_horse, 0, 810,abundance(60)|hit_points(160)|body_armor(18)|difficulty(3)|horse_speed(43)|horse_maneuver(44)|horse_charge(24)|horse_scale(108),imodbits_horse_basic|imodbit_champion],
 ["hunter_b","Hunter", [("European_horse_b",0),("European_horse_b.1",0)], itp_merchandise|itp_type_horse, 0, 810,abundance(60)|hit_points(160)|body_armor(18)|difficulty(3)|horse_speed(43)|horse_maneuver(44)|horse_charge(24)|horse_scale(108),imodbits_horse_basic|imodbit_champion],
 ["hunter_c","Hunter", [("European_horse_c",0),("European_horse_c.1",0)], itp_merchandise|itp_type_horse, 0, 810,abundance(60)|hit_points(160)|body_armor(18)|difficulty(3)|horse_speed(43)|horse_maneuver(44)|horse_charge(24)|horse_scale(108),imodbits_horse_basic|imodbit_champion],
 ["hunter_d","Hunter", [("European_horse_d",0),("European_horse_d.1",0)], itp_merchandise|itp_type_horse, 0, 810,abundance(60)|hit_points(160)|body_armor(18)|difficulty(3)|horse_speed(43)|horse_maneuver(44)|horse_charge(24)|horse_scale(108),imodbits_horse_basic|imodbit_champion],
 ["hunter_e","Hunter", [("European_horse_e",0),("European_horse_e.1",0)], itp_merchandise|itp_type_horse, 0, 810,abundance(60)|hit_points(160)|body_armor(18)|difficulty(3)|horse_speed(43)|horse_maneuver(44)|horse_charge(24)|horse_scale(108),imodbits_horse_basic|imodbit_champion],
 ["hunter_f","Hunter", [("European_horse_f",0),("European_horse_f.1",0)], itp_merchandise|itp_type_horse, 0, 810,abundance(60)|hit_points(160)|body_armor(18)|difficulty(3)|horse_speed(43)|horse_maneuver(44)|horse_charge(24)|horse_scale(108),imodbits_horse_basic|imodbit_champion],

 ["warhorse","War Horse", [("Warhorse_A",0), ("Warhorse_A.1",0)], itp_merchandise|itp_type_horse, 0, 1224,abundance(50)|hit_points(165)|body_armor(40)|difficulty(4)|horse_speed(40)|horse_maneuver(41)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_12, fac_kingdom_5, fac_kingdom_9]],
 ["elen_warhorse_a","Elen War Horse", [("Warhorse_Elen_B",0), ("Warhorse_Elen_B.1",0)], itp_merchandise|itp_type_horse, 0, 1109,abundance(50)|hit_points(165)|body_armor(37)|difficulty(4)|horse_speed(40)|horse_maneuver(41)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_10]],
 ["elen_warhorse_b","Elen War Horse", [("Warhorse_Elen_A",0), ("Warhorse_Elen_A.1",0)], itp_merchandise|itp_type_horse, 0, 1227,abundance(50)|hit_points(165)|body_armor(42)|difficulty(4)|horse_speed(40)|horse_maneuver(41)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_10]],

 ["charger","Charger", [("Charger_A",0), ("Charger_A.1",0), ("Charger_A.2",0)], itp_merchandise|itp_type_horse, 0, 1811,abundance(40)|hit_points(165)|body_armor(58)|difficulty(4)|horse_speed(40)|horse_maneuver(44)|horse_charge(32)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1, fac_kingdom_5]],

["silver_rose_heavy_horse_a","Silver Rose Knight Horse", [("Silver_Rose_Knight_Horse_A",0), ("Silver_Rose_Knight_Horse_A.1",0)], itp_merchandise|itp_type_horse, 0, 1499,abundance(50)|hit_points(165)|body_armor(27)|difficulty(4)|horse_speed(43)|horse_maneuver(45)|horse_charge(30)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1]],
["black_knight_horse_a","Knight Horse", [("Black_Knight_Horse_A",0), ("Black_Knight_Horse_A.1",0)], itp_merchandise|itp_type_horse, 0, 1499,abundance(20)|hit_points(180)|body_armor(35)|difficulty(4)|horse_speed(50)|horse_maneuver(45)|horse_charge(35)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1]],

["mt_horse_b","Heavy Plated Horse", [("horse3",0)], itp_merchandise|itp_type_horse, 0, 2999,abundance(50)|hit_points(220)|body_armor(50)|difficulty(4)|horse_speed(52)|horse_maneuver(50)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_9]],
["mt_horse_b2","Heavy Plated Horse", [("horse4",0)], itp_merchandise|itp_type_horse, 0, 2999,abundance(50)|hit_points(220)|body_armor(50)|difficulty(4)|horse_speed(52)|horse_maneuver(50)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_9]],
["mt_horse_b3","Heavy Plated Champion Horse", [("horse6",0)], itp_merchandise|itp_type_horse, 0, 3999,abundance(30)|hit_points(300)|body_armor(70)|difficulty(5)|horse_speed(52)|horse_maneuver(50)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_9]],

["mt_horse_c","Knighty Horse", [("horse5_1",0), ("horse5_1.1",0)], itp_merchandise|itp_type_horse, 0, 1699,abundance(50)|hit_points(165)|body_armor(40)|difficulty(4)|horse_speed(52)|horse_maneuver(50)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_9]],
["mt_horse_c2","Knighty Horse", [("horse5_1_a",0), ("horse5_1_a.1",0)], itp_merchandise|itp_type_horse, 0, 1699,abundance(50)|hit_points(165)|body_armor(40)|difficulty(4)|horse_speed(52)|horse_maneuver(50)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_9]],
["mt_horse_c3","Knighty Horse", [("horse5_2",0), ("horse5_2.1",0)], itp_merchandise|itp_type_horse, 0, 1699,abundance(50)|hit_points(165)|body_armor(40)|difficulty(4)|horse_speed(52)|horse_maneuver(50)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_9]],
["mt_horse_c4","Knighty Horse", [("horse5_2_a",0), ("horse5_2_a.1",0)], itp_merchandise|itp_type_horse, 0, 1699,abundance(50)|hit_points(165)|body_armor(40)|difficulty(4)|horse_speed(52)|horse_maneuver(50)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_9]],
["mt_horse_c5","Knighty Horse", [("horse5_3",0), ("horse5_3.1",0)], itp_merchandise|itp_type_horse, 0, 1699,abundance(50)|hit_points(165)|body_armor(40)|difficulty(4)|horse_speed(52)|horse_maneuver(50)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_9]],
["mt_horse_c6","Knighty Horse", [("horse5_3_a",0), ("horse5_3_a.1",0)], itp_merchandise|itp_type_horse, 0, 1699,abundance(50)|hit_points(165)|body_armor(40)|difficulty(4)|horse_speed(52)|horse_maneuver(50)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_9]],
["mt_horse_c7","Knighty Horse", [("horse5_4",0), ("horse5_4.1",0)], itp_merchandise|itp_type_horse, 0, 1699,abundance(50)|hit_points(165)|body_armor(40)|difficulty(4)|horse_speed(52)|horse_maneuver(50)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_9]],
["mt_horse_c8","Knighty Horse", [("horse5_4_a",0), ("horse5_4_a.1",0)], itp_merchandise|itp_type_horse, 0, 1699,abundance(50)|hit_points(165)|body_armor(40)|difficulty(4)|horse_speed(52)|horse_maneuver(50)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_9]],
["mt_horse_c9","Knighty Horse", [("horse5_5",0), ("horse5_5.1",0)], itp_merchandise|itp_type_horse, 0, 1699,abundance(50)|hit_points(165)|body_armor(40)|difficulty(4)|horse_speed(52)|horse_maneuver(50)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_9]],
["mt_horse_c10","Knighty Horse", [("horse5_5_a",0), ("horse5_5_a.1",0)], itp_merchandise|itp_type_horse, 0, 1699,abundance(50)|hit_points(165)|body_armor(40)|difficulty(4)|horse_speed(52)|horse_maneuver(50)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_9]],
["mt_horse_c11","Knighty Horse", [("horse7",0), ("horse7.1",0)], itp_merchandise|itp_type_horse, 0, 1699,abundance(50)|hit_points(165)|body_armor(40)|difficulty(4)|horse_speed(52)|horse_maneuver(50)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_9]],

#whalebone crossbow, yew bow, war bow, arming sword 
 ["arrows","Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows|itp_merchandise|itp_default_ammo, itcf_carry_quiver_back, 
 72,weight(3)|abundance(160)|weapon_length(95)|thrust_damage(1,pierce)|max_ammo(30),imodbits_missile],
 ["khergit_arrows","Khergit Arrows", [("arrow_b",0),("flying_missile",ixmesh_flying_ammo),("quiver_b", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 
 410,weight(3.5)|abundance(30)|weapon_length(95)|thrust_damage(3,pierce)|max_ammo(30),imodbits_missile],
 ["barbed_arrows","Barbed Arrows", [("barbed_arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver_d", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 
 124,weight(3)|abundance(70)|weapon_length(95)|thrust_damage(2,pierce)|max_ammo(30),imodbits_missile],
 ["bodkin_arrows","Bodkin Arrows", [("piercing_arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver_c", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 
 350,weight(3)|abundance(50)|weapon_length(91)|thrust_damage(3,pierce)|max_ammo(28),imodbits_missile],
 ["bolts","Bolts", [("crusade_bolt",0),("flying_missile",ixmesh_flying_ammo),("crusade_bolt_bag", ixmesh_carry),("crusade_bolt_bag", ixmesh_carry|imodbit_large_bag)], itp_type_bolts|itp_merchandise|itp_default_ammo|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical, 
 64,weight(2.25)|abundance(90)|weapon_length(63)|thrust_damage(1,pierce)|max_ammo(29),imodbits_missile],
 ["steel_bolts","Heaby Bolts", [("crusade_bolt_heavy",0),("flying_missile",ixmesh_flying_ammo),("crusade_bolt_bag_heavy", ixmesh_carry)], itp_type_bolts|itp_merchandise|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical, 
 210,weight(2.5)|abundance(20)|weapon_length(63)|thrust_damage(2,pierce)|max_ammo(29),imodbits_missile],
 ["piercing_bolts","Piercing Bolts", [("crusade_bolt_heavy_pierce",0),("flying_missile",ixmesh_flying_ammo),("crusade_bolt_bag_heavy_pierce", ixmesh_carry)], itp_type_bolts|itp_merchandise|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical, 
 210,weight(2.5)|abundance(20)|weapon_length(63)|thrust_damage(6,pierce)|max_ammo(29),imodbits_missile],

 ["cartridges","Cartridges", [("cartridge_a",0)], itp_type_bullets|itp_merchandise|itp_can_penetrate_shield|itp_default_ammo, 0, 
 41,weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(1,pierce)|max_ammo(50),imodbits_missile],

["pilgrim_disguise", "Pilgrim Disguise", [("Outcast_Robe_A",0)], 0| itp_type_body_armor |itp_covers_legs |itp_civilian ,0, 25 , weight(2)|abundance(100)|head_armor(0)|body_armor(19)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["pilgrim_hood", "Pilgrim Hood", [("Pilgrim_Hood_A",0)], 0| itp_type_head_armor |itp_civilian  ,0, 35 , weight(1.25)|abundance(100)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

# ARMOR
#handwear
["leather_gloves_a","Cheap Leather Gloves", [("Leather_Gloves_A_L",0)], itp_merchandise|itp_type_hand_armor,0, 60, weight(0.25)|abundance(100)|body_armor(1)|difficulty(0),imodbits_cloth],
["leather_gloves_a_v1","Leather Gloves", [("Leather_Gloves_A_v1_L",0)], itp_merchandise|itp_type_hand_armor,0, 90, weight(0.25)|abundance(100)|body_armor(2)|difficulty(0),imodbits_cloth],

["leather_gloves_b","Long Cheap Leather Gloves", [("Leather_Gloves_B_L",0)], itp_merchandise|itp_type_hand_armor,0, 120, weight(0.3)|abundance(100)|body_armor(3)|difficulty(0),imodbits_cloth],
["leather_gloves_b_v1","Long Leather Gloves", [("Leather_Gloves_B_v1_L",0)], itp_merchandise|itp_type_hand_armor,0, 150, weight(0.3)|abundance(100)|body_armor(4)|difficulty(0),imodbits_cloth],

["mail_mittens_a","Mail Mittens", [("Mail_Gloves_A_L",0)], itp_merchandise|itp_type_hand_armor,0, 150, weight(0.5)|abundance(100)|body_armor(4)|difficulty(8),imodbits_armor],
["mail_mittens_a_v1","Mail Mittens", [("Mail_Gloves_A_v1_L",0)], itp_merchandise|itp_type_hand_armor,0, 180, weight(0.5)|abundance(100)|body_armor(5)|difficulty(9),imodbits_armor],

["plate_gauntlets_a","Cheap Plate Gauntlets", [("Plate_Gauntlets_A_L",0)], itp_merchandise|itp_type_hand_armor,0, 710, weight(0.75)|abundance(100)|body_armor(6)|difficulty(10),imodbits_armor],
["plate_gauntlets_a_v1","Cheap Plate Gauntlets", [("Plate_Gauntlets_A_v1_L",0)], itp_merchandise|itp_type_hand_armor,0, 740, weight(0.75)|abundance(100)|body_armor(7)|difficulty(10),imodbits_armor],
["plate_gauntlets_a_v2","Cheap Plate Gauntlets", [("Plate_Gauntlets_A_v2_L",0)], itp_merchandise|itp_type_hand_armor,0, 770, weight(0.75)|abundance(100)|body_armor(8)|difficulty(11),imodbits_armor],

["plate_gauntlets_b","Plate Gauntlets", [("Plate_Gauntlets_B_L",0)], itp_merchandise|itp_type_hand_armor,0, 840, weight(0.85)|abundance(100)|body_armor(8)|difficulty(11),imodbits_armor],
["plate_gauntlets_b_v1","Plate Gauntlets", [("Plate_Gauntlets_B_v1_L",0)], itp_merchandise|itp_type_hand_armor,0, 870, weight(0.85)|abundance(100)|body_armor(9)|difficulty(12),imodbits_armor],

["eastern_scale_gloves_a","Eastern Scale Gloves", [("gauntlets_arabs_a_L", 0)], itp_type_hand_armor|itp_merchandise, 0,710, weight(0.75)|abundance(100)|body_armor(5), imodbit_lordly, [], [fac_kingdom_6]],
["eastern_scale_gloves_b","Eastern Decorated Scale Gloves", [("gauntlets_arabs_b_L", 0)], itp_type_hand_armor|itp_merchandise, 0,919, weight(0.75)|abundance(100)|body_armor(6), imodbit_lordly, [], [fac_kingdom_6]],
["scale_gauntlets","Scale Gauntlets", [("glove5_L",0)], itp_merchandise|itp_type_hand_armor,0, 710, weight(0.75)|abundance(100)|body_armor(5)|difficulty(0),imodbits_armor],
["lamellar_gauntlets","Lamellar Gauntlets", [("glove6_L",0)], itp_merchandise|itp_type_hand_armor,0, 910, weight(0.9)|abundance(100)|body_armor(6)|difficulty(0),imodbits_armor],

["mt_gauntlets_a","Plate Gauntlets Gothic", [("glove1_L",0)], itp_merchandise|itp_type_hand_armor,0, 799, weight(0.75)|abundance(100)|body_armor(6)|difficulty(0),imodbits_armor, [], [fac_kingdom_10, fac_kingdom_9]],
["mt_gauntlets_a2","Plate Gauntlets Gothic", [("glove2_L",0)], itp_merchandise|itp_type_hand_armor,0, 799, weight(0.75)|abundance(100)|body_armor(6)|difficulty(0),imodbits_armor, [], [fac_kingdom_10, fac_kingdom_9]],
["mt_gauntlets_b","Mail Gloves", [("glove3_L",0)], itp_merchandise|itp_type_hand_armor,0, 599, weight(0.75)|abundance(100)|body_armor(5)|difficulty(0),imodbits_armor, [], [fac_kingdom_10, fac_kingdom_9]],

# BOOTS BEGIN
["sandals_a", "Sandals", [("Sandals_A",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian, 0, 5, weight(0.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],

["hose_a", "Blue Hose", [("Hose_A",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian, 0, 30, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
["hose_b", "Brown Hose", [("Hose_B",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian, 0, 30, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
["hose_c", "Green Hose", [("Hose_C",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian, 0, 30, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
["hose_d", "Grey Hose", [("Hose_D",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian, 0, 30, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
["hose_d_v1", "Grey Hose", [("Hose_D_v1",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian, 0, 30, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
["hose_e", "Red Hose", [("Hose_E",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian, 0, 30, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
["hose_f", "Yellow Hose", [("Hose_F",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian, 0, 30, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],

["poulaines_a", "Blue Poulaines", [("Poulaines_A",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian, 0, 32, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["poulaines_b", "Brown Poulaines", [("Poulaines_B",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian, 0, 32, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["poulaines_c", "Green Poulaines", [("Poulaines_C",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian, 0, 32, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["poulaines_d", "Grey Poulaines", [("Poulaines_D",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian, 0, 32, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["poulaines_d_v1", "Grey Poulaines", [("Poulaines_D_v1",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian, 0, 32, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["poulaines_e", "Red Poulaines", [("Poulaines_E",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian, 0, 32, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["poulaines_f", "Yellow Poulaines", [("Poulaines_F",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian, 0, 32, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],

["leather_shoes_a", "Leather Shoes", [("Leather_Shoes_A",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian, 0, 69, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["leather_shoes_a_v1", "Leather Shoes", [("Leather_Shoes_A_v1",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian, 0, 69, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["leather_shoes_b", "Leather Shoes", [("Leather_Shoes_B",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian, 0, 69, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["leather_shoes_b_v1", "Leather Shoes", [("Leather_Shoes_B_v1",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian, 0, 69, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],

["light_leather_boots_a", "Light Leather Boots", [("Light_Leather_Boots_A",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian, 0, 87, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(14)|difficulty(0) ,imodbits_cloth ],
["light_leather_boots_a_v1", "Light Leather Boots", [("Light_Leather_Boots_A_v1",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian, 0, 87, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(14)|difficulty(0) ,imodbits_cloth ],
["light_leather_boots_b", "Light Leather Boots", [("Light_Leather_Boots_B",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian, 0, 87, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(14)|difficulty(0) ,imodbits_cloth ],
["light_leather_boots_b_v1", "Light Leather Boots", [("Light_Leather_Boots_B_v1",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian, 0, 87, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(14)|difficulty(0) ,imodbits_cloth ],
["light_leather_boots_c", "Light Leather Boots", [("Light_Leather_Boots_C",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian, 0, 87, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(14)|difficulty(0) ,imodbits_cloth ],
["light_leather_boots_c_v1", "Light Leather Boots", [("Light_Leather_Boots_C_v1",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian, 0, 87, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(14)|difficulty(0) ,imodbits_cloth ],

["leather_boots_a", "Leather Boots", [("Leather_Boots_A",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian, 0, 131, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth],
["leather_boots_b", "Hide & Leather Boots", [("Leather_Boots_B",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian, 0, 131, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth],
["leather_boots_c", "Hunting Leather Boots", [("Leather_Boots_C",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian, 0, 131, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth],

["military_boots_a", "Military Boots", [("Milita_Boots_A",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature, 0, 197, weight(1.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(18)|difficulty(0) ,imodbits_armor],
["military_boots_b", "Military Boots", [("Milita_Boots_B",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature, 0, 197, weight(1.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(18)|difficulty(0) ,imodbits_armor],

["mail_boots_a", "Mail Boots", [("Mail_Boots_A",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature, 0, 297, weight(2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(24)|difficulty(0) ,imodbits_armor],
["mail_boots_b", "Mail Boots", [("Mail_Boots_B",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature, 0, 297, weight(2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(24)|difficulty(0) ,imodbits_armor],
["mail_boots_c", "Mail Boots", [("Mail_Boots_C",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature, 0, 297, weight(2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(24)|difficulty(0) ,imodbits_armor],

["plate_boots_a", "Plate Boots", [("Steel_Greaves_A",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature, 0, 497, weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(31)|difficulty(7), imodbits_armor],
["plate_boots_b", "Plate Boots", [("Steel_Greaves_B",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature, 0, 437, weight(2.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(28)|difficulty(7), imodbits_armor],

["desert_boots_a", "Desert Boots", [("Desert_Boots_A",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian, 0, 27, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
["desert_boots_b", "Desert Boots", [("Desert_Boots_B",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian, 0, 27, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],

["desert_nomad_boots_a", "Desert Nomad Boots", [("Desert_Nomad_Boots_A",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian, 0, 87, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth],
["desert_nomad_boots_b", "Desert Nomad Boots", [("Desert_Nomad_Boots_B",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian, 0, 87, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth],
["desert_nomad_boots_c", "Desert Nomad Boots", [("Desert_Nomad_Boots_C",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian, 0, 87, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth],

["desert_rich_boots_a", "Desert High Boots", [("Eastern_Leather_Boots_A",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian, 0, 102, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(14)|difficulty(0) ,imodbits_cloth],
["desert_rich_boots_b", "Desert High Boots", [("Eastern_Leather_Boots_B",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian, 0, 102, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(14)|difficulty(0) ,imodbits_cloth],

["desert_leather_boots_a", "Desert Leather Boots", [("Desert_Leather_Boots_A",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian, 0, 131, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth],
["desert_leather_boots_b", "Desert Leather Boots", [("Desert_Leather_Boots_B",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature|itp_civilian, 0, 131, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth],

["desert_mail_boots_a", "Desert Mail Boots", [("Eastern_Mail_Boots_A",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature, 0, 367, weight(2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(0) ,imodbits_armor],
["desert_mail_boots_b", "Desert Mail Boots with Spurs", [("Eastern_Mail_Boots_B",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature, 0, 367, weight(2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(0) ,imodbits_armor],

["desert_heavy_boots_a", "Desert Heavy Boots", [("Desert_Heavy_Boots_A",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature, 0, 407, weight(2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(26)|difficulty(7), imodbits_armor],
["desert_heavy_boots_b", "Desert Heavy Boots", [("Desert_Heavy_Boots_B",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature, 0, 407, weight(2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(26)|difficulty(7), imodbits_armor],
# BOOTS END

["sarranid_head_cloth", "Lady Head Cloth", [("tulbent",0)],  itp_type_head_armor | itp_doesnt_cover_hair |itp_civilian |itp_attach_armature,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["sarranid_head_cloth_b", "Lady Head Cloth", [("tulbent_b",0)],  itp_type_head_armor | itp_doesnt_cover_hair |itp_civilian |itp_attach_armature,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["sarranid_felt_head_cloth", "Head Cloth", [("common_tulbent",0)],  itp_type_head_armor  |itp_civilian |itp_attach_armature,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["sarranid_felt_head_cloth_b", "Head Cloth", [("common_tulbent_b",0)],  itp_type_head_armor  |itp_civilian |itp_attach_armature,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

#bodywear
["lady_dress_ruby", "Lady Dress", [("lady_dress_r",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["lady_dress_green", "Lady Dress", [("lady_dress_g",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["lady_dress_blue", "Lady Dress", [("lady_dress_b",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["red_dress", "Red Dress", [("red_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["brown_dress", "Brown Dress", [("brown_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["green_dress", "Green Dress", [("green_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["khergit_lady_dress", "Khergit Lady Dress", [("khergit_lady_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["khergit_lady_dress_b", "Khergit Leather Lady Dress", [("khergit_lady_dress_b",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["sarranid_lady_dress", "Eastern Lady Dress", [("sarranid_lady_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["sarranid_lady_dress_b", "Eastern Lady Dress", [("sarranid_lady_dress_b",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["sarranid_common_dress", "Eastern Dress", [("sarranid_common_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["sarranid_common_dress_b", "Eastern Dress", [("sarranid_common_dress_b",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["leather_jacket", "Merchant Jacket", [("Leather_Jacket_A",0)], itp_merchandise| itp_type_body_armor | itp_covers_legs  |itp_civilian ,0, 250 , weight(3)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(15)|difficulty(0) ,imodbits_cloth ],

#NEW:
["rawhide_coat", "Rawhide Coat", [("Rawhide_Coat_A",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 12 , weight(5)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
#NEW: was lthr_armor_a
["leather_armor", "Leather Armor", [("Leather_Cuirass_A",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs  ,0, 65 , weight(7)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["heavy_leather_vest_mail", "Heavy Leather Armor", [("Leather_Cuirass_B",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian,0, 1099 , weight(20)|abundance(100)|head_armor(0)|body_armor(41)|leg_armor(10)|difficulty(9) ,imodbits_cloth ],
["fur_coat", "Fur Coat", [("Fur_Coat_A",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 157 , weight(6)|abundance(100)|head_armor(0)|body_armor(13)|leg_armor(10)|difficulty(0) ,imodbits_armor ],



#for future:
["coat", "Coat", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["leather_coat", "Leather Coat", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["mail_coat", "Coat of Mail", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["long_mail_coat", "Long Coat of Mail", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["mail_with_tunic_red", "Mail with Tunic", [("Arena_Armor_Red",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(8), imodbits_armor ],
["mail_with_tunic_green", "Mail with Tunic", [("Arena_Armor_Green",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(8), imodbits_armor ],
["hide_coat", "Hide Coat", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["merchant_outfit", "Merchant Outfit", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["homespun_dress", "Homespun Dress", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["thick_coat", "Thick Coat", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["coat_with_cape", "Coat with Cape", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["steppe_outfit", "Steppe Outfit", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["nordic_outfit", "Nordic Outfit", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["nordic_armor", "Nordic Armor", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["hide_armor", "Hide Armor", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["cloaked_tunic", "Cloaked Tunic", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["sleeveless_tunic", "Sleeveless Tunic", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["sleeveless_leather_tunic", "Sleeveless Leather Tunic", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["linen_shirt", "Linen Shirt", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["wool_coat", "Wool Coat", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
#end

["dress", "Dress", [("dress",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["blue_dress", "Blue Dress", [("Common_Dress_B",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["peasant_dress", "Peasant Dress", [("Common_Dress_A",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ], 
["woolen_dress", "Woolen Dress", [("woolen_dress",0)], itp_merchandise| itp_type_body_armor|itp_civilian  |itp_covers_legs ,0,
 10 , weight(1.75)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["shirt", "Shirt", [("Burlap_Tunic_A",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 31 , weight(1)|abundance(100)|head_armor(0)|body_armor(5)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
 #NEW: was "linen_tunic"
["linen_tunic", "Linen Tunic", [("Shirt_A",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 61 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(13)|difficulty(0) ,imodbits_cloth ],

["tunic_with_green_cape", "Peasant Tunic", [("Peasant_Tunic_A",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 62 , weight(1)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(8)|difficulty(0) ,imodbits_cloth ], 

#TODO:
 ["red_shirt", "Red Shirt", [("Shirt_C",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
 ["red_tunic", "Red Tunic", [("Arena_Shirt_E",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],

 ["green_tunic", "Green Tunic", [("Arena_Shirt_B",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
 ["blue_tunic", "Blue Tunic", [("Arena_Shirt_C",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 80 , weight(1)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["robe", "Robe", [("Outcast_Robe_B",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 31 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["robe_on_mail_a", "Robe on Mail", [("Cultist_Armor_A",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0, 385 , weight(14.0)|abundance(3)|head_armor(0)|body_armor(35)|leg_armor(14)|difficulty(0) ,imodbits_armor ],
["robe_on_mail_b", "Robe on Mail", [("Cultist_Armor_B",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0, 385 , weight(14.0)|abundance(3)|head_armor(0)|body_armor(35)|leg_armor(14)|difficulty(0) ,imodbits_armor ],
#NEW: was coarse_tunic
["coarse_tunic", "Tunic with vest", [("Coarse_Tunic_Revised_A",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 47 , weight(2)|abundance(100)|head_armor(0)|body_armor(11)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["leather_apron", "Peasant Leather Vest", [("Peasant_Tunic_B",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 87 , weight(3)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
#NEW: was leather_vest
["leather_vest", "Leather Vest", [("Leather_Vest_Revised_A",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 146 , weight(4)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(15)|difficulty(0) ,imodbits_cloth ],
["leather_vest_reinfoced", "Leather Vest", [("Leather_Vest_Revised_B",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 246 , weight(4)|abundance(100)|head_armor(0)|body_armor(23)|leg_armor(15)|difficulty(0) ,imodbits_cloth ],
["steppe_armor", "Steppe Armor", [("Leather_Lamellar_A",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 195 , weight(5)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],

["blue_gambeson", "Blue & Red Gambeson", [("Gambeson_Two_Tones_A",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 270 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["red_gambeson", "Red & Yellow Gambeson", [("Gambeson_Two_Tones_B",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 295 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(14)|difficulty(0) ,imodbits_cloth ],
["gambeson", "Light Blue Gambeson", [("Gambeson_One_Tone_A",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 260 , weight(5)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],

#NEW: was aketon_a
["padded_cloth", "Aketon", [("Gambeson_A",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 297 , weight(11)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
#NEW:
["aketon_green", "Padded Cloth", [("Padded_Cloth_Revised_A",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 297 , weight(11)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

# MENEGRAS ARMOR START
["menegras_aketon_a", "Menegras House Aketon", [("Aketon_Menegras_A",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,337 , weight(11)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], [] ],
["menegras_aketon_b", "Menegras House Aketon with Kneekops", [("Aketon_Menegras_B",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,489 , weight(17)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(13)|difficulty(7) ,imodbits_armor, [], [] ],

["menegras_brigandine_a", "Menegras House Brigandine", [("Brigandine_Menegras_A",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,899 , weight(21)|abundance(100)|head_armor(0)|body_armor(36)|leg_armor(12)|difficulty(6) ,imodbits_armor, [], [] ],
["menegras_brigandine_b", "Menegras House Brigandine on Mail", [("Brigandine_Menegras_B",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1299 , weight(25)|abundance(100)|head_armor(0)|body_armor(42)|leg_armor(18)|difficulty(7) ,imodbits_armor, [], [] ],
["menegras_brigandine_c", "Menegras House Brigandine With Plates", [("Brigandine_Menegras_C",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1399 , weight(24)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(16)|difficulty(7) ,imodbits_armor, [], [] ],
["menegras_brigandine_d", "Menegras House Heavy Brigandine", [("Brigandine_Menegras_D",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1671 , weight(26)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(23)|difficulty(9) ,imodbits_armor, [], [] ],
# MENEGRAS ARMOR END

["coat_of_plates", "Coat of Plates", [("Coat_Of_Plates_B",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1228 , weight(21)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(18)|difficulty(9) ,imodbits_armor ],
["coat_of_plates_v1", "Coat of Plates with Decorations", [("Coat_Of_Plates_B_v1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1228 , weight(21)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(18)|difficulty(9) ,imodbits_armor ],
["coat_of_plates_v2", "Coat of Plates", [("Coat_Of_Plates_B_v2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1328 , weight(21)|abundance(100)|head_armor(0)|body_armor(47)|leg_armor(18)|difficulty(9) ,imodbits_armor ],
["coat_of_plates_v3", "Coat of Plates", [("Coat_Of_Plates_B_v3",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1628 , weight(23)|abundance(100)|head_armor(0)|body_armor(51)|leg_armor(21)|difficulty(10) ,imodbits_armor ],

 #NEW: was "leather_jerkin"
["leather_jerkin", "Leather Jerkin", [("Rough_Leather_Jerkin_A",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 421 , weight(6)|abundance(100)|head_armor(0)|body_armor(23)|leg_armor(15)|difficulty(0) ,imodbits_cloth ],
["nomad_vest", "Nomad Vest", [("Nomad_Vest_A",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 360 , weight(7)|abundance(50)|head_armor(0)|body_armor(22)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["ragged_outfit", "Ragged Outfit", [("Padded_Cloth_Cloacked_B",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 390 , weight(7)|abundance(100)|head_armor(0)|body_armor(23)|leg_armor(16)|difficulty(0) ,imodbits_cloth ],
 #NEW: was padded_leather
["padded_leather", "Padded Leather", [("Leather_Vest_A",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian,0, 454 , weight(12)|abundance(100)|head_armor(0)|body_armor(27)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["m_leather_vest_a", "Leather Vest", [("Leather_Vest_B",0), ("Leather_Vest_B.1",0), ("Leather_Vest_B.2",0), ("Leather_Vest_B.3",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian,0, 454 , weight(12)|abundance(100)|head_armor(0)|body_armor(27)|leg_armor(14)|difficulty(0) ,imodbits_cloth ],
["tribal_warrior_outfit", "Tribal Warrior Outfit", [("Rough_Leather_Fur_A",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 520 , weight(14)|abundance(100)|head_armor(0)|body_armor(30)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["nomad_robe", "Nomad Robe", [("Robe_A",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0,
 610 , weight(15)|abundance(100)|head_armor(0)|body_armor(32)|leg_armor(18)|difficulty(7) ,imodbits_cloth ],
["nomad_armor", "Nomad Armor", [("Robe_B",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs   ,0, 25 , weight(2)|abundance(100)|head_armor(0)|body_armor(24)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["nomad_robe_b", "Nomad Robe", [("Robe_C",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0, 610 , weight(15)|abundance(100)|head_armor(0)|body_armor(32)|leg_armor(18)|difficulty(7) ,imodbits_cloth ],
["khergit_armor", "Nomad Jacket", [("Robe_D",0)], itp_merchandise| itp_type_body_armor | itp_covers_legs ,0, 38 , weight(2)|abundance(100)|head_armor(0)|body_armor(24)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

#["heraldric_armor", "Heraldric Armor", [("tourn_armor_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 442 , weight(17)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(8)|difficulty(7) ,imodbits_armor ],
#NEW: was "std_lthr_coat"
["studded_leather_coat", "Studded Leather Coat", [("Rough_Leather_Jerkin_Mail_A",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 690 , weight(14)|abundance(100)|head_armor(0)|body_armor(36)|leg_armor(18)|difficulty(7) ,imodbits_armor ],

["lamellar_vest", "Lamellar Vest", [("Lamellar_Vest_A",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 970 , weight(18)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_cloth ],

["lamellar_vest_khergit", "Lamellar Vest", [("Lamellar_Vest_B",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 970 , weight(18)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_cloth ],

["banded_armor", "Banded Armor", [("Banded_Armor_A",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2710 , weight(23)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(15)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_12] ],
#NEW: was hard_lthr_a
["cuir_bouilli", "Cuir Bouilli", [("Cuir_Bouilli_A",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3100 , weight(24)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(19)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_12] ],
["coat_of_plates_red", "Coat of Plates", [("Coat_Of_Plates_A",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,1945 , weight(22)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(18)|difficulty(10) ,imodbits_armor ],

 ["sarranid_dress_a", "Dress", [("woolen_dress",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 33 , weight(1)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
 ["sarranid_dress_b", "Dress", [("woolen_dress",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 33 , weight(1)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],

#Quest-specific - perhaps can be used for prisoners, 
["burlap_tunic", "Burlap Tunic", [("Burlap_Tunic_A",0)], itp_type_body_armor  |itp_covers_legs ,0,
 5 , weight(1)|abundance(100)|head_armor(0)|body_armor(3)|leg_armor(1)|difficulty(0) ,imodbits_armor ],

# Removed old heraldic items
["heraldic_mail_with_surcoat", "Heraldic Mail with Surcoat", [("heraldic_armor_new_a",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 3454 , weight(22)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(17)|difficulty(7) ,imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_a", ":agent_no", ":troop_no")])]],
["heraldic_mail_with_tunic", "Heraldic Mail", [("heraldic_armor_new_b",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 3520 , weight(22)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(16)|difficulty(7) ,imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_b", ":agent_no", ":troop_no")])]],
["heraldic_mail_with_tunic_b", "Heraldic Mail", [("heraldic_armor_new_c",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 3610 , weight(22)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(16)|difficulty(7) ,imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_c", ":agent_no", ":troop_no")])]],
["heraldic_mail_with_tabard", "Heraldic Mail with Tabard", [("heraldic_armor_new_d",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 3654 , weight(21)|abundance(100)|head_armor(0)|body_armor(51)|leg_armor(15)|difficulty(7) ,imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_d", ":agent_no", ":troop_no")])]],

# ARMORS START
# Armor Diffuculty is equal to the Armor / 3
# Armor Price is equal to the (Armor * 30) + 33 - difficulty + (100 - abundance) * 5.5
# Armor variants are based on modifiers
# There is different color options for some armors
# TODO: Implement in-game recoloring
# TODO: Implement in-game upgrading (will change the model to the next variant)
# Using item_has_modifier operation to check for possible upgrades?

[
    "brown_shirt_a",
    "Brown Shirt",
    [
        ("Brown_Shirt_A", 0),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian,
    0, 20,
    weight(2)|abundance(100)|head_armor(0)|body_armor(5)|leg_armor(3)|difficulty(0),
    imodbits_none,
    [], [fac_kingdom_2]
],

[
    "brown_shirt_a_v1",
    "Brown Adventurer Shirt",
    [
        ("Brown_Shirt_A_v1", 0),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian,
    0, 12,
    weight(2)|abundance(100)|head_armor(0)|body_armor(4)|leg_armor(2)|difficulty(0),
    imodbits_none,
    [], [fac_kingdom_2]
],

[
    "rough_brown_shirt_a",
    "Brown Rough Shirt",
    [
        ("Brown_Rough_Shirt_A", 0),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian,
    0, 35,
    weight(2)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(4)|difficulty(0),
    imodbits_none,
    [], [fac_kingdom_2]
],

[
    "rough_brown_shirt_a_v1",
    "Brown Rough Shirt with Ornamentation",
    [
        ("Brown_Rough_Shirt_A_v1", 0),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian,
    0, 35,
    weight(2)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(4)|difficulty(0),
    imodbits_none,
    [], [fac_kingdom_2]
],

[
    "rough_gray_shirt_a",
    "Gray Rough Shirt",
    [
        ("Gray_Rough_Shirt_A", 0),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian,
    0, 35,
    weight(2)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(4)|difficulty(0),
    imodbits_none,
    [], [fac_kingdom_4]
],

[   
    "purple_shirt_a",
    "Purple Shirt",
    [
        ("Purple_Shirt_A", 0),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian,
    0, 20,
    weight(2)|abundance(100)|head_armor(0)|body_armor(5)|leg_armor(3)|difficulty(0),
    imodbits_none,
    [], [fac_kingdom_7]
],

[
    "purple_shirt_a_v1",
    "Purple Shirt",
    [
        ("Purple_Shirt_A_v1", 0),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian,
    0, 20,
    weight(2)|abundance(100)|head_armor(0)|body_armor(5)|leg_armor(3)|difficulty(0),
    imodbits_none,
    [], [fac_kingdom_7]
],

[
    "purple_shirt_a_v2",
    "Purple Shirt",
    [
        ("Purple_Shirt_A_v2", 0),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian,
    0, 20,
    weight(2)|abundance(100)|head_armor(0)|body_armor(5)|leg_armor(3)|difficulty(0),
    imodbits_none,
    [], [fac_kingdom_7]
],

[
    "hairako_shirt_a",
    "Hairako Shirt",
    [
        ("Hairako_Shirt_A", 0),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian,
    0, 79,
    weight(2)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(5)|difficulty(0),
    imodbits_none,
    [], [fac_kingdom_8]
],

# TUNICS START
# For tunics, the difficulty is 0, and the price is (Armor * 15)
[
    "tunic_a",
    "Tunic",
    [
        ("Revised_Tunic_A", 0),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian,
    0, 165,
    weight(2)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(5)|difficulty(0),
    imodbits_none,
    [], [fac_kingdom_12]
],

[
    "tunic_b",
    "Tunic",
    [
        ("Revised_Tunic_B", 0),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian,
    0, 165,
    weight(2)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(5)|difficulty(0),
    imodbits_none,
    [], [fac_kingdom_12]
],

[
    "tunic_c",
    "Tunic",
    [
        ("Revised_Tunic_C", 0),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian,
    0, 165,
    weight(2)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(5)|difficulty(0),
    imodbits_none,
    [], [fac_kingdom_12]
],

[
    "tunic_d",
    "Tunic with Vest",
    [
        ("Revised_Tunic_D", 0),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian,
    0, 195,
    weight(2)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(5)|difficulty(0),
    imodbits_none,
    [], [fac_kingdom_12]
],

[
    "tunic_e",
    "Tunic with Leather Vest",
    [
        ("Revised_Tunic_E", 0),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian,
    0, 240,
    weight(2)|abundance(100)|head_armor(0)|body_armor(11)|leg_armor(5)|difficulty(0),
    imodbits_none,
    [], [fac_kingdom_12]
],
# TUNICS END

# TABARDS START
[
    "tabard_a",
    "Tabard",
    [
        ("Revised_Tabard_A", 0),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian,
    0, 543,
    weight(3)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(5)|difficulty(0),
    imodbits_none,
    [], [fac_kingdom_12]
],

[
    "tabard_a_v1",
    "Lightly Plated Tabard",
    [
        ("Revised_Tabard_A_v1", 0),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 656,
    weight(8)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(5)|difficulty(7),
    imodbits_none,
    [], [fac_kingdom_12]
],

[
    "tabard_a_v2",
    "Plated Tabard",
    [
        ("Revised_Tabard_A_v2", 0),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 982,
    weight(14)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(12)|difficulty(11),
    imodbits_none,
    [], [fac_kingdom_12]
],

[
    "tabard_b",
    "Tabard",
    [
        ("Revised_Tabard_B", 0),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian,
    0, 543,
    weight(3)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(5)|difficulty(0),
    imodbits_none,
    [], [fac_kingdom_12]
],

[
    "tabard_c",
    "Tabard",
    [
        ("Revised_Tabard_C", 0),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian,
    0, 543,
    weight(3)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(5)|difficulty(0),
    imodbits_none,
    [], [fac_kingdom_12]
],

[
    "tabard_d",
    "Tabard",
    [
        ("Revised_Tabard_D", 0),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian,
    0, 543,
    weight(3)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(5)|difficulty(0),
    imodbits_none,
    [], [fac_kingdom_12]
],

[
    "tabard_e",
    "Tabard",
    [
        ("Revised_Tabard_E", 0),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian,
    0, 543,
    weight(3)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(5)|difficulty(0),
    imodbits_none,
    [], [fac_kingdom_12]
],

[
    "tabard_f",
    "Tabard",
    [
        ("Revised_Tabard_F", 0),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs | itp_civilian,
    0, 543,
    weight(3)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(5)|difficulty(0),
    imodbits_none,
    [], [fac_kingdom_12]
],
# TABARDS END

# AKETONS START
[
    "white_aketon_a", 
    "Aketon", 
    [
        ("White_Aketon_A", 0),
        ("White_Aketon_A_ragged", imodbit_ragged),
        ("White_Aketon_A_tattered", imodbit_tattered),
        ("White_Aketon_A_sturdy", imodbit_sturdy),
        ("White_Aketon_A_thick", imodbit_thick),
        ("White_Aketon_A_hardened", imodbit_hardened),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 864,
    weight(7)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(8)|difficulty(9),
    imodbit_ragged | imodbit_tattered | imodbit_sturdy | imodbit_thick | imodbit_hardened,
    [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_5, fac_kingdom_7, fac_kingdom_9, fac_kingdom_10]
],

[
    "white_aketon_heraldic_a", 
    "Aketon", 
    [
        ("White_Aketon_Heraldic_A.base", 0),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 864,
    weight(7)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(8)|difficulty(9),
    imodbits_none,
    [
        (
            ti_on_init_item,
            [
                (store_trigger_param_1, ":agent_no"),
                (store_trigger_param_2, ":troop_no"),
                (call_script, "script_shield_item_set_banner", "tableau_heraldic_aketon_a", ":agent_no", ":troop_no"),
                # Manually set mesh after heraldic was applied to avoid applying heraldic to all meshes
                (cur_item_add_mesh, "@White_Aketon_Heraldic_A.arms"),
                (cur_item_add_mesh, "@White_Aketon_Heraldic_A.hose"),
            ]
        )
    ],
    [fac_kingdom_1, fac_kingdom_3, fac_kingdom_5, fac_kingdom_7, fac_kingdom_9, fac_kingdom_10]
],

[
    "white_aketon_b", 
    "Aketon with Plates", 
    [
        ("White_Aketon_B", 0),
        ("White_Aketon_B_thick", imodbit_thick),
        ("White_Aketon_B_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1188,
    weight(14)|abundance(95)|head_armor(0)|body_armor(25)|leg_armor(13)|difficulty(13),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_5, fac_kingdom_7, fac_kingdom_9, fac_kingdom_10]
],

[
    "olive_aketon_a", 
    "Olive Painted Aketon", 
    [
        ("Olive_Aketon_A", 0),
        ("Olive_Aketon_A_thick", imodbit_thick),
        ("Olive_Aketon_A_hardened", imodbit_hardened),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 864,
    weight(7)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(8)|difficulty(9),
    imodbit_thick | imodbit_hardened,
    [], [fac_kingdom_3]
],

[
    "olive_aketon_a_v1", 
    "Olive Painted Aketon", 
    [
        ("Olive_Aketon_A_v1", 0),
        ("Olive_Aketon_A_v1_thick", imodbit_thick),
        ("Olive_Aketon_A_v1_hardened", imodbit_hardened),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 864,
    weight(7)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(8)|difficulty(9),
    imodbit_thick | imodbit_hardened,
    [], [fac_kingdom_3]
],

[
    "olive_aketon_a_v2",
    "Olive Painted Aketon",
    [
        ("Olive_Aketon_A_v2", 0),
        ("Olive_Aketon_A_v2_thick", imodbit_thick),
        ("Olive_Aketon_A_v2_hardened", imodbit_hardened),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 864,
    weight(7)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(8)|difficulty(9),
    imodbit_thick | imodbit_hardened,
    [], [fac_kingdom_3]
],

[
    "olive_aketon_a_v3",
    "Olive Painted Aketon",
    [
        ("Olive_Aketon_A_v3", 0),
        ("Olive_Aketon_A_v3_thick", imodbit_thick),
        ("Olive_Aketon_A_v3_hardened", imodbit_hardened),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 864,
    weight(7)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(8)|difficulty(9),
    imodbit_thick | imodbit_hardened,
    [], [fac_kingdom_3]
],

[
    "olive_aketon_b", 
    "Olive Painted Aketon with Plates", 
    [
        ("Olive_Aketon_B", 0),
        ("Olive_Aketon_B_thick", imodbit_thick),
        ("Olive_Aketon_B_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1188,
    weight(14)|abundance(95)|head_armor(0)|body_armor(25)|leg_armor(13)|difficulty(13),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_3]
],

[
    "olive_aketon_b_v1", 
    "Olive Painted Aketon with Plates", 
    [
        ("Olive_Aketon_B_v1", 0),
        ("Olive_Aketon_B_v1_thick", imodbit_thick),
        ("Olive_Aketon_B_v1_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1188,
    weight(14)|abundance(95)|head_armor(0)|body_armor(25)|leg_armor(13)|difficulty(13),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_3]
],

[
    "olive_aketon_b_v2", 
    "Olive Painted Aketon with Plates", 
    [
        ("Olive_Aketon_B_v2", 0),
        ("Olive_Aketon_B_v2_thick", imodbit_thick),
        ("Olive_Aketon_B_v2_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1188,
    weight(14)|abundance(95)|head_armor(0)|body_armor(25)|leg_armor(13)|difficulty(13),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_3]
],

[
    "olive_aketon_b_v3", 
    "Olive Painted Aketon with Plates", 
    [
        ("Olive_Aketon_B_v3", 0),
        ("Olive_Aketon_B_v3_thick", imodbit_thick),
        ("Olive_Aketon_B_v3_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1188,
    weight(14)|abundance(95)|head_armor(0)|body_armor(25)|leg_armor(13)|difficulty(13),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_3]
],

[
    "brown_aketon_a",
    "Brown Painted Aketon",
    [
        ("Brown_Aketon_A", 0),
        ("Brown_Aketon_A_thick", imodbit_thick),
        ("Brown_Aketon_A_hardened", imodbit_hardened),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 864,
    weight(7)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(8)|difficulty(9),
    imodbit_thick | imodbit_hardened,
    [], [fac_kingdom_2]
],

[
    "brown_aketon_a_v1",
    "Brown Painted Aketon",
    [
        ("Brown_Aketon_A_v1", 0),
        ("Brown_Aketon_A_v1_thick", imodbit_thick),
        ("Brown_Aketon_A_v1_hardened", imodbit_hardened),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 864,
    weight(7)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(8)|difficulty(9),
    imodbit_thick | imodbit_hardened,
    [], [fac_kingdom_2]
],

[
    "brown_aketon_a_v2",
    "Brown Painted Aketon",
    [
        ("Brown_Aketon_A_v2", 0),
        ("Brown_Aketon_A_v2_thick", imodbit_thick),
        ("Brown_Aketon_A_v2_hardened", imodbit_hardened),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 864,
    weight(7)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(8)|difficulty(9),
    imodbit_thick | imodbit_hardened,
    [], [fac_kingdom_2]
],

[
    "brown_aketon_b", 
    "Brown Painted Aketon with Plates", 
    [
        ("Brown_Aketon_B", 0),
        ("Brown_Aketon_B_thick", imodbit_thick),
        ("Brown_Aketon_B_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1188,
    weight(14)|abundance(95)|head_armor(0)|body_armor(25)|leg_armor(13)|difficulty(13),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_2]
],

[
    "brown_aketon_b_v1", 
    "Brown Painted Aketon with Plates", 
    [
        ("Brown_Aketon_B_v1", 0),
        ("Brown_Aketon_B_v1_thick", imodbit_thick),
        ("Brown_Aketon_B_v1_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1188,
    weight(14)|abundance(95)|head_armor(0)|body_armor(25)|leg_armor(13)|difficulty(13),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_2]
],

[
    "brown_aketon_b_v2", 
    "Brown Painted Aketon with Plates", 
    [
        ("Brown_Aketon_B_v2", 0),
        ("Brown_Aketon_B_v2_thick", imodbit_thick),
        ("Brown_Aketon_B_v2_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1188,
    weight(14)|abundance(95)|head_armor(0)|body_armor(25)|leg_armor(13)|difficulty(13),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_2]
],

[
    "red_aketon_a",
    "Red Painted Aketon",
    [
        ("Red_Aketon_A", 0),
        ("Red_Aketon_A_thick", imodbit_thick),
        ("Red_Aketon_A_hardened", imodbit_hardened),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 864,
    weight(7)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(8)|difficulty(9),
    imodbit_thick | imodbit_hardened,
    [], [fac_kingdom_1]
],

[
    "red_aketon_a_v1",
    "Red Painted Aketon",
    [
        ("Red_Aketon_A_v1", 0),
        ("Red_Aketon_A_v1_thick", imodbit_thick),
        ("Red_Aketon_A_v1_hardened", imodbit_hardened),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 864,
    weight(7)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(8)|difficulty(9),
    imodbit_thick | imodbit_hardened,
    [], [fac_kingdom_1]
],

[
    "red_aketon_a_v2",
    "Red Painted Aketon",
    [
        ("Red_Aketon_A_v2", 0),
        ("Red_Aketon_A_v2_thick", imodbit_thick),
        ("Red_Aketon_A_v2_hardened", imodbit_hardened),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 864,
    weight(7)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(8)|difficulty(9),
    imodbit_thick | imodbit_hardened,
    [], [fac_kingdom_1]
],

[
    "red_aketon_b", 
    "Red Painted Aketon with Plates", 
    [
        ("Red_Aketon_B", 0),
        ("Red_Aketon_B_thick", imodbit_thick),
        ("Red_Aketon_B_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1188,
    weight(14)|abundance(95)|head_armor(0)|body_armor(25)|leg_armor(13)|difficulty(13),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_1]
],

[
    "red_aketon_b_v1", 
    "Red Painted Aketon with Plates", 
    [
        ("Red_Aketon_B_v1", 0),
        ("Red_Aketon_B_v1_thick", imodbit_thick),
        ("Red_Aketon_B_v1_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1188,
    weight(14)|abundance(95)|head_armor(0)|body_armor(25)|leg_armor(13)|difficulty(13),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_1]
],

[
    "red_aketon_b_v2", 
    "Red Painted Aketon with Plates", 
    [
        ("Red_Aketon_B_v2", 0),
        ("Red_Aketon_B_v2_thick", imodbit_thick),
        ("Red_Aketon_B_v2_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1188,
    weight(14)|abundance(95)|head_armor(0)|body_armor(25)|leg_armor(13)|difficulty(13),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_1]
],

[
    "gray_aketon_a",
    "Gray Painted Aketon",
    [
        ("Gray_Aketon_A", 0),
        ("Gray_Aketon_A_thick", imodbit_thick),
        ("Gray_Aketon_A_hardened", imodbit_hardened),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 864,
    weight(7)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(8)|difficulty(9),
    imodbit_thick | imodbit_hardened,
    [], [fac_kingdom_4]
],

[
    "gray_aketon_a_v1",
    "Gray Painted Aketon",
    [
        ("Gray_Aketon_A_v1", 0),
        ("Gray_Aketon_A_v1_thick", imodbit_thick),
        ("Gray_Aketon_A_v1_hardened", imodbit_hardened),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 864,
    weight(7)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(8)|difficulty(9),
    imodbit_thick | imodbit_hardened,
    [], [fac_kingdom_4]
],

[
    "gray_aketon_a_v2",
    "Gray Painted Aketon",
    [
        ("Gray_Aketon_A_v2", 0),
        ("Gray_Aketon_A_v2_thick", imodbit_thick),
        ("Gray_Aketon_A_v2_hardened", imodbit_hardened),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 864,
    weight(7)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(8)|difficulty(9),
    imodbit_thick | imodbit_hardened,
    [], [fac_kingdom_4]
],

[
    "gray_aketon_b", 
    "Gray Painted Aketon with Plates", 
    [
        ("Gray_Aketon_B", 0),
        ("Gray_Aketon_B_thick", imodbit_thick),
        ("Gray_Aketon_B_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1188,
    weight(14)|abundance(95)|head_armor(0)|body_armor(25)|leg_armor(13)|difficulty(13),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_4]
],

[
    "gray_aketon_b_v1", 
    "Gray Painted Aketon with Plates", 
    [
        ("Gray_Aketon_B_v1", 0),
        ("Gray_Aketon_B_v1_thick", imodbit_thick),
        ("Gray_Aketon_B_v1_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1188,
    weight(14)|abundance(95)|head_armor(0)|body_armor(25)|leg_armor(13)|difficulty(13),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_4]
],

[
    "gray_aketon_b_v2", 
    "Gray Painted Aketon with Plates", 
    [
        ("Gray_Aketon_B_v2", 0),
        ("Gray_Aketon_B_v2_thick", imodbit_thick),
        ("Gray_Aketon_B_v2_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1188,
    weight(14)|abundance(95)|head_armor(0)|body_armor(25)|leg_armor(13)|difficulty(13),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_4]
],

[
    "navy_aketon_a",
    "Navy Painted Aketon",
    [
        ("Navy_Aketon_A", 0),
        ("Navy_Aketon_A_thick", imodbit_thick),
        ("Navy_Aketon_A_hardened", imodbit_hardened),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 864,
    weight(7)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(8)|difficulty(9),
    imodbit_thick | imodbit_hardened,
    [], [fac_kingdom_4, fac_kingdom_12]
],

[
    "navy_aketon_a_v1",
    "Navy Painted Aketon",
    [
        ("Navy_Aketon_A_v1", 0),
        ("Navy_Aketon_A_v1_thick", imodbit_thick),
        ("Navy_Aketon_A_v1_hardened", imodbit_hardened),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 864,
    weight(7)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(8)|difficulty(9),
    imodbit_thick | imodbit_hardened,
    [], [fac_kingdom_4, fac_kingdom_12]
],

[
    "navy_aketon_b", 
    "Navy Painted Aketon with Plates", 
    [
        ("Navy_Aketon_B", 0),
        ("Navy_Aketon_B_thick", imodbit_thick),
        ("Navy_Aketon_B_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1188,
    weight(14)|abundance(95)|head_armor(0)|body_armor(25)|leg_armor(13)|difficulty(13),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_4, fac_kingdom_12]
],

[
    "navy_aketon_b_v1", 
    "Navy Painted Aketon with Plates", 
    [
        ("Navy_Aketon_B_v1", 0),
        ("Navy_Aketon_B_v1_thick", imodbit_thick),
        ("Navy_Aketon_B_v1_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1188,
    weight(14)|abundance(95)|head_armor(0)|body_armor(25)|leg_armor(13)|difficulty(13),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_4, fac_kingdom_12]
],

[
    "green_aketon_a",
    "Green Painted Aketon",
    [
        ("Green_Aketon_A", 0),
        ("Green_Aketon_A_thick", imodbit_thick),
        ("Green_Aketon_A_hardened", imodbit_hardened),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 864,
    weight(7)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(8)|difficulty(9),
    imodbit_thick | imodbit_hardened,
    [], [fac_kingdom_5]
],

[
    "green_aketon_a_v1",
    "Green Painted Aketon",
    [
        ("Green_Aketon_A_v1", 0),
        ("Green_Aketon_A_v1_thick", imodbit_thick),
        ("Green_Aketon_A_v1_hardened", imodbit_hardened),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 864,
    weight(7)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(8)|difficulty(9),
    imodbit_thick | imodbit_hardened,
    [], [fac_kingdom_5]
],

[
    "green_aketon_a_v2",
    "Green Painted Aketon",
    [
        ("Green_Aketon_A_v2", 0),
        ("Green_Aketon_A_v2_thick", imodbit_thick),
        ("Green_Aketon_A_v2_hardened", imodbit_hardened),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 864,
    weight(7)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(8)|difficulty(9),
    imodbit_thick | imodbit_hardened,
    [], [fac_kingdom_5]
],

[
    "green_aketon_b",
    "Green Painted Aketon with Plates",
    [
        ("Green_Aketon_B", 0),
        ("Green_Aketon_B_thick", imodbit_thick),
        ("Green_Aketon_B_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1188,
    weight(14)|abundance(95)|head_armor(0)|body_armor(25)|leg_armor(13)|difficulty(13),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_5]
],

[
    "green_aketon_b_v1",
    "Green Painted Aketon with Plates",
    [
        ("Green_Aketon_B_v1", 0),
        ("Green_Aketon_B_v1_thick", imodbit_thick),
        ("Green_Aketon_B_v1_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1188,
    weight(14)|abundance(95)|head_armor(0)|body_armor(25)|leg_armor(13)|difficulty(13),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_5]
],

[
    "green_aketon_b_v2",
    "Green Painted Aketon with Plates",
    [
        ("Green_Aketon_B_v2", 0),
        ("Green_Aketon_B_v2_thick", imodbit_thick),
        ("Green_Aketon_B_v2_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1188,
    weight(14)|abundance(95)|head_armor(0)|body_armor(25)|leg_armor(13)|difficulty(13),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_5]
],

[
    "yellow_aketon_a",
    "Yellow Painted Aketon",
    [
        ("Yellow_Aketon_A", 0),
        ("Yellow_Aketon_A_thick", imodbit_thick),
        ("Yellow_Aketon_A_hardened", imodbit_hardened),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 864,
    weight(7)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(8)|difficulty(9),
    imodbit_thick | imodbit_hardened,
    [], [fac_kingdom_6]
],

[
    "yellow_aketon_a_v1",
    "Yellow Painted Aketon",
    [
        ("Yellow_Aketon_A_v1", 0),
        ("Yellow_Aketon_A_v1_thick", imodbit_thick),
        ("Yellow_Aketon_A_v1_hardened", imodbit_hardened),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 864,
    weight(7)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(8)|difficulty(9),
    imodbit_thick | imodbit_hardened,
    [], [fac_kingdom_6]
],

[
    "yellow_aketon_b",
    "Yellow Painted Aketon with Plates",
    [("Yellow_Aketon_B", 0)],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1188,
    weight(14)|abundance(95)|head_armor(0)|body_armor(25)|leg_armor(13)|difficulty(13),
    imodbits_none,
    [], [fac_kingdom_6]
],

[
    "yellow_aketon_b_v1",
    "Yellow Painted Aketon with Plates",
    [("Yellow_Aketon_B_v1", 0)],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1188,
    weight(14)|abundance(95)|head_armor(0)|body_armor(25)|leg_armor(13)|difficulty(13),
    imodbits_none,
    [], [fac_kingdom_6]
],

[
    "purple_aketon_a",
    "Purple Painted Aketon",
    [
        ("Purple_Aketon_A", 0),
        ("Purple_Aketon_A_thick", imodbit_thick),
        ("Purple_Aketon_A_hardened", imodbit_hardened),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 864,
    weight(7)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(8)|difficulty(9),
    imodbit_thick | imodbit_hardened,
    [], [fac_kingdom_6]
],
# AKETONS END

# POURPOINTS START
[
    "white_pourpoint_a",
    "Pourpoint",
    [
        ("White_Pourpoint_A", 0),
        ("White_Pourpoint_A_tattered", imodbit_tattered),
        ("White_Pourpoint_A_sturdy", imodbit_sturdy),
        ("White_Pourpoint_A_thick", imodbit_thick),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 864,
    weight(7)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(8)|difficulty(9),
    imodbit_tattered | imodbit_sturdy | imodbit_thick,
    [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_5, fac_kingdom_7, fac_kingdom_9, fac_kingdom_10]
],

[
    "red_pourpoint_a",
    "Red Painted Pourpoint",
    [
        ("Red_Pourpoint_A", 0),
        ("Red_Pourpoint_A_tattered", imodbit_tattered),
        ("Red_Pourpoint_A_sturdy", imodbit_sturdy),
        ("Red_Pourpoint_A_thick", imodbit_thick),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 864,
    weight(7)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(8)|difficulty(9),
    imodbit_tattered | imodbit_sturdy | imodbit_thick,
    [], [fac_kingdom_1]
],

[
    "brown_pourpoint_a",
    "Brown Painted Pourpoint",
    [
        ("Brown_Pourpoint_A", 0),
        ("Brown_Pourpoint_A_tattered", imodbit_tattered),
        ("Brown_Pourpoint_A_sturdy", imodbit_sturdy),
        ("Brown_Pourpoint_A_thick", imodbit_thick),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 864,
    weight(7)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(8)|difficulty(9),
    imodbit_tattered | imodbit_sturdy | imodbit_thick,
    [], [fac_kingdom_2]
],

[
    "yellow_pourpoint_a",
    "Yellow Painted Pourpoint",
    [
        ("Yellow_Pourpoint_A", 0),
        ("Yellow_Pourpoint_A_sturdy", imodbit_sturdy),
        ("Yellow_Pourpoint_A_thick", imodbit_thick),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 864,
    weight(7)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(8)|difficulty(9),
    imodbit_sturdy | imodbit_thick,
    [], [fac_kingdom_6]
],
# POURPOINTS END

# LEATHER ARMORS START
[
    "gray_leather_armor_a",
    "Leather Armor on Gray Painted Aketon",
    [
        ("Gray_Leather_Armor_A", 0),
        ("Gray_Leather_Armor_A_thick", imodbit_thick),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1012,
    weight(11)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(8)|difficulty(11),
    imodbit_thick,
    [], [fac_kingdom_4]
],

[
    "gray_leather_armor_a_v1",
    "Leather Armor onf Gray Painted Aketon",
    [
        ("Gray_Leather_Armor_A_v1", 0),
        ("Gray_Leather_Armor_A_v1_thick", imodbit_thick),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1012,
    weight(11)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(8)|difficulty(11),
    imodbit_thick,
    [], [fac_kingdom_4]
],

[
    "gray_leather_armor_a_v2",
    "Leather Armor on Gray Painted Aketon",
    [
        ("Gray_Leather_Armor_A_v2", 0),
        ("Gray_Leather_Armor_A_v2_thick", imodbit_thick),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1012,
    weight(11)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(8)|difficulty(11),
    imodbit_thick,
    [], [fac_kingdom_4]
],

[
    "gray_leather_armor_b",
    "Leather Armor with Plates on Gray Painted Aketon",
    [
        ("Gray_Leather_Armor_B", 0),
        ("Gray_Leather_Armor_B_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1337,
    weight(14)|abundance(95)|head_armor(0)|body_armor(30)|leg_armor(13)|difficulty(14),
    imodbit_reinforced,
    [], [fac_kingdom_4]
],

[
    "gray_leather_armor_b_v1",
    "Leather Armor with Plates on Gray Painted Aketon",
    [
        ("Gray_Leather_Armor_B_v1", 0),
        ("Gray_Leather_Armor_B_v1_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1337,
    weight(14)|abundance(95)|head_armor(0)|body_armor(30)|leg_armor(13)|difficulty(14),
    imodbit_reinforced,
    [], [fac_kingdom_4]
],

[
    "gray_leather_armor_b_v2",
    "Leather Armor with Plates on Gray Painted Aketon",
    [
        ("Gray_Leather_Armor_B_v2", 0),
        ("Gray_Leather_Armor_B_v2_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1337,
    weight(14)|abundance(95)|head_armor(0)|body_armor(30)|leg_armor(13)|difficulty(14),
    imodbit_reinforced,
    [], [fac_kingdom_4]
],

[
    "purple_leather_armor_a",
    "Leather Armor on Purple Shirt",
    [
        ("Purple_Leather_Armor_A", 0),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 630,
    weight(5)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(5)|difficulty(0),
    imodbits_none,
    [], [fac_kingdom_7]
],

[
    "hairako_leather_armor_a",
    "Hairako Leather Armor",
    [
        ("Hairako_Leather_Armor_A", 0),
        ("Hairako_Leather_Armor_A_thick", imodbit_thick),
        ("Hairako_Leather_Armor_A_hardened", imodbit_hardened),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1012,
    weight(11)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(8)|difficulty(11),
    imodbit_thick | imodbit_hardened,
    [], [fac_kingdom_8]
],

[
    "hairako_leather_armor_a_v1",
    "Hairako Leather Armor",
    [
        ("Hairako_Leather_Armor_A_v1", 0),
        ("Hairako_Leather_Armor_A_v1_thick", imodbit_thick),
        ("Hairako_Leather_Armor_A_v1_hardened", imodbit_hardened),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1012,
    weight(11)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(8)|difficulty(11),
    imodbit_thick | imodbit_hardened,
    [], [fac_kingdom_8]
],

[
    "hairako_leather_armor_b",
    "Hairako Leather Armor with Plates",
    [
        ("Hairako_Leather_Armor_B", 0),
        ("Hairako_Leather_Armor_B_hardened", imodbit_hardened),
        ("Hairako_Leather_Armor_B_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1544,
    weight(16)|abundance(95)|head_armor(0)|body_armor(35)|leg_armor(15)|difficulty(17),
    imodbit_hardened | imodbit_reinforced,
    [], [fac_kingdom_8]
],

[
    "hairako_leather_armor_b_v1",
    "Hairako Leather Armor with Plates",
    [
        ("Hairako_Leather_Armor_B_v1", 0),
        ("Hairako_Leather_Armor_B_v1_hardened", imodbit_hardened),
        ("Hairako_Leather_Armor_B_v1_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1544,
    weight(16)|abundance(95)|head_armor(0)|body_armor(35)|leg_armor(15)|difficulty(17),
    imodbit_hardened | imodbit_reinforced,
    [], [fac_kingdom_8]
],
# LEATHER ARMORS END

# COAT OF PLATES START
[
    "purple_coat_of_plates_a",
    "Coat of Plates on Purple Painted Aketon",
    [
        ("Purple_Aketon_Coat_A", 0),
        ("Purple_Aketon_Coat_A_thick", imodbit_thick),
        ("Purple_Aketon_Coat_A_hardened", imodbit_hardened),
        ("Purple_Aketon_Coat_A_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 982,
    weight(15)|abundance(100)|head_armor(0)|body_armor(24)|leg_armor(8)|difficulty(11),
    imodbit_thick | imodbit_hardened | imodbit_reinforced,
    [], [fac_kingdom_7]
],

[
    "purple_coat_of_plates_a_v1",
    "Coat of Plates on Purple Painted Aketon",
    [
        ("Purple_Aketon_Coat_A_v1", 0),
        ("Purple_Aketon_Coat_A_v1_thick", imodbit_thick),
        ("Purple_Aketon_Coat_A_v1_hardened", imodbit_hardened),
        ("Purple_Aketon_Coat_A_v1_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 982,
    weight(15)|abundance(100)|head_armor(0)|body_armor(24)|leg_armor(8)|difficulty(11),
    imodbit_thick | imodbit_hardened | imodbit_reinforced,
    [], [fac_kingdom_7]
],

[
    "purple_coat_of_plates_b",
    "Plated Coat of Plates on Purple Painted Aketon",
    [
        ("Purple_Aketon_Coat_B", 0),
        ("Purple_Aketon_Coat_B_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1278,
    weight(18)|abundance(95)|head_armor(0)|body_armor(28)|leg_armor(13)|difficulty(14),
    imodbit_reinforced,
    [], [fac_kingdom_7]
],

[
    "purple_coat_of_plates_b_v1",
    "Plated Coat of Plates on Purple Painted Aketon",
    [
        ("Purple_Aketon_Coat_B_v1", 0),
        ("Purple_Aketon_Coat_B_v1_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1278,
    weight(18)|abundance(95)|head_armor(0)|body_armor(28)|leg_armor(13)|difficulty(14),
    imodbit_reinforced,
    [], [fac_kingdom_7]
],

[
    "purple_coat_of_plates_c",
    "Mail Coat of Plates on Purple Painted Aketon",
    [
        ("Purple_Aketon_Coat_C", 0),
        ("Purple_Aketon_Coat_C_thick", imodbit_thick),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1602,
    weight(22)|abundance(90)|head_armor(0)|body_armor(36)|leg_armor(15)|difficulty(18),
    imodbit_thick,
    [], [fac_kingdom_7]
],

[
    "purple_coat_of_plates_c_v1",
    "Mail Coat of Plates on Purple Painted Aketon",
    [
        ("Purple_Aketon_Coat_C_v1", 0),
        ("Purple_Aketon_Coat_C_v1_thick", imodbit_thick),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1602,
    weight(22)|abundance(90)|head_armor(0)|body_armor(36)|leg_armor(15)|difficulty(18),
    imodbit_thick,
    [], [fac_kingdom_7]
],

[
    "purple_coat_of_plates_d",
    "Heavy Mail Coat of Plates on Purple Painted Aketon",
    [
        ("Purple_Aketon_Coat_D", 0),
        ("Purple_Aketon_Coat_D_thick", imodbit_thick),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1893,
    weight(26)|abundance(80)|head_armor(0)|body_armor(42)|leg_armor(17)|difficulty(20),
    imodbit_thick,
    [], [fac_kingdom_7]
],

[
    "purple_coat_of_plates_d_v1",
    "Heavy Mail Coat of Plates on Purple Painted Aketon",
    [
        ("Purple_Aketon_Coat_D_v1", 0),
        ("Purple_Aketon_Coat_D_v1_thick", imodbit_thick),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1893,
    weight(26)|abundance(80)|head_armor(0)|body_armor(42)|leg_armor(17)|difficulty(20),
    imodbit_thick,
    [], [fac_kingdom_7]
],
# COAT OF PLATES END
[
    "lamellar_cuirass_a",
    "Lamellar Cuirass",
    [
        ("Lamellar_Cuirass_A", 0),
        ("Lamellar_Cuirass_A_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1300,
    weight(13)|abundance(80)|head_armor(0)|body_armor(30)|leg_armor(9)|difficulty(13),
    imodbit_reinforced,
    [], [fac_kingdom_3]
],

[
    "lamellar_cuirass_a_v1",
    "Lamellar Cuirass",
    [
        ("Lamellar_Cuirass_A_v1", 0),
        ("Lamellar_Cuirass_A_v1_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1300,
    weight(13)|abundance(80)|head_armor(0)|body_armor(30)|leg_armor(9)|difficulty(13),
    imodbit_reinforced,
    [], [fac_kingdom_3]
],

# CHURBURG START
[
    "white_churburg_a",
    "Churburg",
    [
        ("White_Churburg_A", 0),
        ("White_Churburg_A_thick", imodbit_thick),
        ("White_Churburg_A_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1304,
    weight(15)|abundance(90)|head_armor(0)|body_armor(32)|leg_armor(9)|difficulty(14),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_5, fac_kingdom_7, fac_kingdom_9, fac_kingdom_10]
],

[
    "white_churburg_b",
    "Plated Churburg",
    [
        ("White_Churburg_B", 0),
        ("White_Churburg_B_thick", imodbit_thick),
        ("White_Churburg_B_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1512,
    weight(18)|abundance(90)|head_armor(0)|body_armor(35)|leg_armor(13)|difficulty(16),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_5, fac_kingdom_7, fac_kingdom_9, fac_kingdom_10]
],

[
    "white_churburg_c",
    "Heavy Plated Churburg",
    [
        ("White_Churburg_C", 0),
        ("White_Churburg_C_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1745,
    weight(22)|abundance(80)|head_armor(0)|body_armor(39)|leg_armor(15)|difficulty(18),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_5, fac_kingdom_7, fac_kingdom_9, fac_kingdom_10]
],

[
    "olive_churburg_a",
    "Churburg on Olive Painted Pourpoint",
    [
        ("Olive_Churburg_A", 0),
        ("Olive_Churburg_A_thick", imodbit_thick),
        ("Olive_Churburg_A_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1304,
    weight(15)|abundance(90)|head_armor(0)|body_armor(32)|leg_armor(9)|difficulty(14),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_3]
],

[
    "olive_churburg_b",
    "Plated Churburg on Olive Painted Pourpoint",
    [
        ("Olive_Churburg_B", 0),
        ("Olive_Churburg_B_thick", imodbit_thick),
        ("Olive_Churburg_B_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1512,
    weight(18)|abundance(90)|head_armor(0)|body_armor(35)|leg_armor(13)|difficulty(16),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_3]
],

[
    "olive_churburg_mail_a",
    "Churburg with Mail on Olive Painted Pourpoint",
    [
        ("Olive_Churburg_Mail_A", 0),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1512,
    weight(20)|abundance(90)|head_armor(0)|body_armor(37)|leg_armor(11)|difficulty(16),
    imodbits_none,
    [], [fac_kingdom_3]
],

[
    "olive_churburg_mail_b",
    "Plated Churburg with Mail on Olive Painted Pourpoint",
    [
        ("Olive_Churburg_Mail_B", 0),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1745,
    weight(24)|abundance(90)|head_armor(0)|body_armor(41)|leg_armor(13)|difficulty(18),
    imodbits_none,
    [], [fac_kingdom_3]
],

[
    "olive_churburg_mail_c",
    "Heavy Plated Churburg with Mail on Olive Painted Pourpoint",
    [
        ("Olive_Churburg_Mail_C", 0),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 2071,
    weight(28)|abundance(80)|head_armor(0)|body_armor(45)|leg_armor(20)|difficulty(22),
    imodbits_none,
    [], [fac_kingdom_3]
],

[
    "red_churburg_a",
    "Churburg on Red Pourpoint",
    [
        ("Red_Churburg_A", 0),
        ("Red_Churburg_A_thick", imodbit_thick),
        ("Red_Churburg_A_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1304,
    weight(15)|abundance(90)|head_armor(0)|body_armor(32)|leg_armor(9)|difficulty(14),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_1]
],

[
    "red_churburg_b",
    "Plated Churburg on Red Pourpoint",
    [
        ("Red_Churburg_B", 0),
        ("Red_Churburg_B_thick", imodbit_thick),
        ("Red_Churburg_B_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1512,
    weight(18)|abundance(90)|head_armor(0)|body_armor(35)|leg_armor(13)|difficulty(16),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_1]
],

[
    "red_churburg_c",
    "Heavy Plated Churburg on Red Pourpoint",
    [
        ("Red_Churburg_C", 0),
        ("Red_Churburg_C_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1745,
    weight(22)|abundance(80)|head_armor(0)|body_armor(39)|leg_armor(15)|difficulty(18),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_1]
],

[
    "red_churburg_mail_a",
    "Churburg with Mail on Red Pourpoint",
    [
        ("Red_Churburg_Mail_A", 0),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1512,
    weight(20)|abundance(90)|head_armor(0)|body_armor(37)|leg_armor(11)|difficulty(16),
    imodbits_none,
    [], [fac_kingdom_1]
],

[
    "red_churburg_mail_b",
    "Plated Churburg with Mail on Red Pourpoint",
    [
        ("Red_Churburg_Mail_B", 0),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1745,
    weight(24)|abundance(90)|head_armor(0)|body_armor(41)|leg_armor(13)|difficulty(18),
    imodbits_none,
    [], [fac_kingdom_1]
],

[
    "red_churburg_mail_c",
    "Heavy Plated Churburg with Mail on Red Pourpoint",
    [
        ("Red_Churburg_Mail_C", 0),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 2071,
    weight(28)|abundance(80)|head_armor(0)|body_armor(45)|leg_armor(20)|difficulty(22),
    imodbits_none,
    [], [fac_kingdom_1]
],

[
    "red_churburg_mail_c_v1",
    "Heavy Plated Decorated Churburg with Mail on Red Pourpoint",
    [
        ("Red_Churburg_Mail_C_v1", 0),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 2236,
    weight(28)|abundance(50)|head_armor(0)|body_armor(45)|leg_armor(20)|difficulty(22),
    imodbits_none,
    [], [fac_kingdom_1]
],

[
    "green_churburg_a",
    "Churburg on Green Pourpoint",
    [
        ("Green_Churburg_A", 0),
        ("Green_Churburg_A_thick", imodbit_thick),
        ("Green_Churburg_A_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1304,
    weight(15)|abundance(90)|head_armor(0)|body_armor(32)|leg_armor(9)|difficulty(14),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_5]
],

[
    "green_churburg_a_v1",
    "Churburg on Green Pourpoint",
    [
        ("Green_Churburg_A_v1", 0),
        ("Green_Churburg_A_v1_thick", imodbit_thick),
        ("Green_Churburg_A_v1_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1304,
    weight(15)|abundance(90)|head_armor(0)|body_armor(32)|leg_armor(9)|difficulty(14),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_5]
],

[
    "green_churburg_b",
    "Plated Churburg on Green Pourpoint",
    [
        ("Green_Churburg_B", 0),
        ("Green_Churburg_B_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1512,
    weight(18)|abundance(90)|head_armor(0)|body_armor(35)|leg_armor(13)|difficulty(16),
    imodbit_reinforced,
    [], [fac_kingdom_5]
],

[
    "green_churburg_b_v1",
    "Plated Churburg on Green Pourpoint",
    [
        ("Green_Churburg_B_v1", 0),
        ("Green_Churburg_B_v1_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1512,
    weight(18)|abundance(90)|head_armor(0)|body_armor(35)|leg_armor(13)|difficulty(16),
    imodbit_reinforced,
    [], [fac_kingdom_5]
],

[
    "green_churburg_c",
    "Heavy Plated Churburg on Green Pourpoint",
    [
        ("Green_Churburg_C", 0),
        ("Green_Churburg_C_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1745,
    weight(22)|abundance(80)|head_armor(0)|body_armor(39)|leg_armor(15)|difficulty(18),
    imodbit_reinforced,
    [], [fac_kingdom_5]
],

[
    "green_churburg_c_v1",
    "Heavy Plated Churburg on Green Pourpoint",
    [
        ("Green_Churburg_C_v1", 0),
        ("Green_Churburg_C_v1_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1745,
    weight(22)|abundance(80)|head_armor(0)|body_armor(39)|leg_armor(15)|difficulty(18),
    imodbit_reinforced,
    [], [fac_kingdom_5]
],
# CHURBURG END

# HAUBERKS START
[
    "white_hauberk_a",
    "Hauberk",
    [
        ("White_Hauberk_A", 0),
        ("White_Hauberk_A_rusty", imodbit_rusty),
        ("White_Hauberk_A_thick", imodbit_thick),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1393,
    weight(20)|abundance(90)|head_armor(0)|body_armor(35)|leg_armor(9)|difficulty(15),
    imodbit_rusty | imodbit_thick,
    [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_5, fac_kingdom_7, fac_kingdom_9, fac_kingdom_10]
],

[
    "olive_hauberk_a",
    "Hauberk on Olive Painted Aketon",
    [
        ("Olive_Hauberk_A", 0),
        ("Olive_Hauberk_A_thick", imodbit_thick),
        ("Olive_Hauberk_A_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1393,
    weight(20)|abundance(90)|head_armor(0)|body_armor(35)|leg_armor(9)|difficulty(15),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_3]
],

[
    "olive_hauberk_a_v1",
    "Hauberk on Olive Painted Aketon",
    [
        ("Olive_Hauberk_A_v1", 0),
        ("Olive_Hauberk_A_v1_thick", imodbit_thick),
        ("Olive_Hauberk_A_v1_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1393,
    weight(20)|abundance(90)|head_armor(0)|body_armor(35)|leg_armor(9)|difficulty(15),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_3]
],

[
    "olive_hauberk_a_v2",
    "Hauberk on Olive Painted Aketon",
    [
        ("Olive_Hauberk_A_v2", 0),
        ("Olive_Hauberk_A_v2_thick", imodbit_thick),
        ("Olive_Hauberk_A_v2_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1393,
    weight(20)|abundance(90)|head_armor(0)|body_armor(35)|leg_armor(9)|difficulty(15),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_3]
],

[
    "olive_hauberk_a_v3",
    "Hauberk on Olive Painted Aketon",
    [
        ("Olive_Hauberk_A_v3", 0),
        ("Olive_Hauberk_A_v3_thick", imodbit_thick),
        ("Olive_Hauberk_A_v3_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1393,
    weight(20)|abundance(90)|head_armor(0)|body_armor(35)|leg_armor(9)|difficulty(15),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_3]
],

[
    "olive_hauberk_b",
    "Plated Hauberk on Olive Painted Aketon",
    [
        ("Olive_Hauberk_B", 0),
        ("Olive_Hauberk_B_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1512,
    weight(23)|abundance(90)|head_armor(0)|body_armor(38)|leg_armor(13)|difficulty(17),
    imodbit_reinforced,
    [], [fac_kingdom_3]
],

[
    "olive_hauberk_b_v1",
    "Plated Hauberk on Olive Painted Aketon",
    [
        ("Olive_Hauberk_B_v1", 0),
        ("Olive_Hauberk_B_v1_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1512,
    weight(23)|abundance(90)|head_armor(0)|body_armor(38)|leg_armor(13)|difficulty(17),
    imodbit_reinforced,
    [], [fac_kingdom_3]
],

[
    "olive_hauberk_b_v2",
    "Plated Hauberk on Olive Painted Aketon",
    [
        ("Olive_Hauberk_B_v2", 0),
        ("Olive_Hauberk_B_v2_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1512,
    weight(23)|abundance(90)|head_armor(0)|body_armor(38)|leg_armor(13)|difficulty(17),
    imodbit_reinforced,
    [], [fac_kingdom_3]
],

[
    "olive_hauberk_b_v3",
    "Plated Hauberk on Olive Painted Aketon",
    [
        ("Olive_Hauberk_B_v3", 0),
        ("Olive_Hauberk_B_v3_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1512,
    weight(23)|abundance(90)|head_armor(0)|body_armor(38)|leg_armor(13)|difficulty(17),
    imodbit_reinforced,
    [], [fac_kingdom_3]
],

[
    "brown_hauberk_a",
    "Hauberk on Brown Painted Aketon",
    [
        ("Brown_Hauberk_A", 0),
        ("Brown_Hauberk_A_thick", imodbit_thick),
        ("Brown_Hauberk_A_hardened", imodbit_hardened),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1393,
    weight(20)|abundance(90)|head_armor(0)|body_armor(35)|leg_armor(9)|difficulty(15),
    imodbit_thick | imodbit_hardened,
    [], [fac_kingdom_2]
],

[
    "brown_hauberk_a_v1",
    "Hauberk on Brown Painted Aketon",
    [
        ("Brown_Hauberk_A_v1", 0),
        ("Brown_Hauberk_A_v1_thick", imodbit_thick),
        ("Brown_Hauberk_A_v1_hardened", imodbit_hardened),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1393,
    weight(20)|abundance(90)|head_armor(0)|body_armor(35)|leg_armor(9)|difficulty(15),
    imodbit_thick | imodbit_hardened,
    [], [fac_kingdom_2]
],

[
    "brown_hauberk_a_v2",
    "Hauberk on Brown Painted Aketon",
    [
        ("Brown_Hauberk_A_v2", 0),
        ("Brown_Hauberk_A_v2_thick", imodbit_thick),
        ("Brown_Hauberk_A_v2_hardened", imodbit_hardened),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1393,
    weight(20)|abundance(90)|head_armor(0)|body_armor(35)|leg_armor(9)|difficulty(15),
    imodbit_thick | imodbit_hardened,
    [], [fac_kingdom_2]
],

[
    "red_hauberk_a",
    "Hauberk on Red Painted Aketon",
    [
        ("Red_Hauberk_A", 0),
        ("Red_Hauberk_A_thick", imodbit_thick),
        ("Red_Hauberk_A_hardened", imodbit_hardened),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1393,
    weight(20)|abundance(90)|head_armor(0)|body_armor(35)|leg_armor(9)|difficulty(15),
    imodbit_thick | imodbit_hardened,
    [], [fac_kingdom_1]
],

[
    "red_hauberk_a_v1",
    "Hauberk on Red Painted Aketon",
    [
        ("Red_Hauberk_A_v1", 0),
        ("Red_Hauberk_A_v1_thick", imodbit_thick),
        ("Red_Hauberk_A_v1_hardened", imodbit_hardened),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1393,
    weight(20)|abundance(90)|head_armor(0)|body_armor(35)|leg_armor(9)|difficulty(15),
    imodbit_thick | imodbit_hardened,
    [], [fac_kingdom_1]
],

[
    "red_hauberk_a_v2",
    "Hauberk on Red Painted Aketon",
    [
        ("Red_Hauberk_A_v2", 0),
        ("Red_Hauberk_A_v2_thick", imodbit_thick),
        ("Red_Hauberk_A_v2_hardened", imodbit_hardened),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1393,
    weight(20)|abundance(90)|head_armor(0)|body_armor(35)|leg_armor(9)|difficulty(15),
    imodbit_thick | imodbit_hardened,
    [], [fac_kingdom_1]
],

[
    "gray_hauberk_a",
    "Hauberk on Gray Painted Aketon",
    [
        ("Gray_Hauberk_A", 0),
        ("Gray_Hauberk_A_thick", imodbit_thick),
        ("Gray_Hauberk_A_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1393,
    weight(20)|abundance(90)|head_armor(0)|body_armor(35)|leg_armor(9)|difficulty(15),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_4]
],

[
    "gray_hauberk_a_v1",
    "Hauberk on Gray Painted Aketon",
    [
        ("Gray_Hauberk_A_v1", 0),
        ("Gray_Hauberk_A_v1_thick", imodbit_thick),
        ("Gray_Hauberk_A_v1_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1393,
    weight(20)|abundance(90)|head_armor(0)|body_armor(35)|leg_armor(9)|difficulty(15),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_4]
],

[
    "gray_hauberk_a_v2",
    "Hauberk on Gray Painted Aketon",
    [
        ("Gray_Hauberk_A_v2", 0),
        ("Gray_Hauberk_A_v2_thick", imodbit_thick),
        ("Gray_Hauberk_A_v2_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1393,
    weight(20)|abundance(90)|head_armor(0)|body_armor(35)|leg_armor(9)|difficulty(15),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_4]
],

[
    "gray_hauberk_b",
    "Plated Hauberk on Gray Painted Aketon",
    [
        ("Gray_Hauberk_B", 0),
        ("Gray_Hauberk_B_thick", imodbit_thick),
        ("Gray_Hauberk_B_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1688,
    weight(24)|abundance(85)|head_armor(0)|body_armor(38)|leg_armor(15)|difficulty(18),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_4]
],

[
    "gray_hauberk_b_v1",
    "Plated Hauberk on Gray Painted Aketon",
    [
        ("Gray_Hauberk_B_v1", 0),
        ("Gray_Hauberk_B_v1_thick", imodbit_thick),
        ("Gray_Hauberk_B_v1_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1688,
    weight(24)|abundance(85)|head_armor(0)|body_armor(38)|leg_armor(15)|difficulty(18),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_4]
],

[
    "navy_hauberk_a",
    "Hauberk on Navy Painted Aketon",
    [
        ("Navy_Hauberk_A", 0),
        ("Navy_Hauberk_A_thick", imodbit_thick),
        ("Navy_Hauberk_A_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1393,
    weight(20)|abundance(90)|head_armor(0)|body_armor(35)|leg_armor(9)|difficulty(15),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_4, fac_kingdom_12]
],

[
    "navy_hauberk_a_v1",
    "Hauberk on Navy Painted Aketon",
    [
        ("Navy_Hauberk_A_v1", 0),
        ("Navy_Hauberk_A_v1_thick", imodbit_thick),
        ("Navy_Hauberk_A_v1_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1393,
    weight(20)|abundance(90)|head_armor(0)|body_armor(35)|leg_armor(9)|difficulty(15),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_4, fac_kingdom_12]
],

[
    "green_hauberk_a",
    "Hauberk on Green Painted Aketon",
    [
        ("Green_Hauberk_A", 0),
        ("Green_Hauberk_A_thick", imodbit_thick),
        ("Green_Hauberk_A_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1393,
    weight(20)|abundance(90)|head_armor(0)|body_armor(35)|leg_armor(9)|difficulty(15),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_5]
],

[
    "green_hauberk_a_v1",
    "Hauberk on Green Painted Aketon",
    [
        ("Green_Hauberk_A_v1", 0),
        ("Green_Hauberk_A_v1_thick", imodbit_thick),
        ("Green_Hauberk_A_v1_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1393,
    weight(20)|abundance(90)|head_armor(0)|body_armor(35)|leg_armor(9)|difficulty(15),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_5]
],

[
    "green_hauberk_a_v2",
    "Hauberk on Green Painted Aketon",
    [
        ("Green_Hauberk_A_v2", 0),
        ("Green_Hauberk_A_v2_thick", imodbit_thick),
        ("Green_Hauberk_A_v2_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1393,
    weight(20)|abundance(90)|head_armor(0)|body_armor(35)|leg_armor(9)|difficulty(15),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_5]
],

[
    "yellow_hauberk_a",
    "Hauberk on Yellow Painted Aketon",
    [
        ("Yellow_Hauberk_A", 0),
        ("Yellow_Hauberk_A_thick", imodbit_thick),
        ("Yellow_Hauberk_A_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1487,
    weight(21)|abundance(90)|head_armor(0)|body_armor(38)|leg_armor(9)|difficulty(16),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_6]
],

[
    "yellow_hauberk_a_v1",
    "Hauberk on Yellow Painted Aketon",
    [
        ("Yellow_Hauberk_A_v1", 0),
        ("Yellow_Hauberk_A_v1_thick", imodbit_thick),
        ("Yellow_Hauberk_A_v1_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1487,
    weight(21)|abundance(90)|head_armor(0)|body_armor(38)|leg_armor(9)|difficulty(16),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_6]
],

[
    "yellow_hauberk_b",
    "Plated Hauberk on Yellow Painted Aketon",
    [("Yellow_Hauberk_B", 0)],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1718,
    weight(24)|abundance(85)|head_armor(0)|body_armor(40)|leg_armor(15)|difficulty(19),
    imodbits_none,
    [], [fac_kingdom_6]
],

[
    "yellow_hauberk_b_v1",
    "Plated Hauberk on Yellow Painted Aketon",
    [("Yellow_Hauberk_B_v1", 0)],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1718,
    weight(24)|abundance(85)|head_armor(0)|body_armor(40)|leg_armor(15)|difficulty(19),
    imodbits_none,
    [], [fac_kingdom_6]
],

[
    "yellow_hauberk_c",
    "Heavy Plated Hauberk on Yellow Painted Aketon",
    [
        ("Yellow_Hauberk_C", 0),
        ("Yellow_Hauberk_C_thick", imodbit_thick),
        ("Yellow_Hauberk_C_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1956,
    weight(28)|abundance(80)|head_armor(0)|body_armor(44)|leg_armor(20)|difficulty(21),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_6]
],

[
    "yellow_hauberk_c_v1",
    "Heavy Plated Hauberk on Yellow Painted Aketon",
    [
        ("Yellow_Hauberk_C_v1", 0),
        ("Yellow_Hauberk_C_v1_thick", imodbit_thick),
        ("Yellow_Hauberk_C_v1_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1956,
    weight(28)|abundance(80)|head_armor(0)|body_armor(44)|leg_armor(20)|difficulty(21),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_6]
],

[
    "purple_hauberk_a",
    "Hauberk on Purple Painted Aketon",
    [
        ("Purple_Hauberk_A", 0),
        ("Purple_Hauberk_A_thick", imodbit_thick),
        ("Purple_Hauberk_A_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1487,
    weight(21)|abundance(90)|head_armor(0)|body_armor(38)|leg_armor(9)|difficulty(16),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_7]
],

[
    "hairako_hauberk_a",
    "Hauberk on Hairako Painted Aketon",
    [
        ("Hairako_Hauberk_A", 0),
        ("Hairako_Hauberk_A_thick", imodbit_thick),
        ("Hairako_Hauberk_A_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1487,
    weight(21)|abundance(90)|head_armor(0)|body_armor(38)|leg_armor(9)|difficulty(16),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_8]
],

[
    "hairako_hauberk_b",
    "Plated Hauberk on Hairako Painted Aketon",
    [
        ("Hairako_Hauberk_B", 0),
        ("Hairako_Hauberk_B_thick", imodbit_thick),
        ("Hairako_Hauberk_B_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1718,
    weight(24)|abundance(85)|head_armor(0)|body_armor(40)|leg_armor(15)|difficulty(19),
    imodbit_thick | imodbit_reinforced,
    [], [fac_kingdom_8]
],
# HAUBERKS END

# BRIGANDINES START
[
    "white_brigandine_a",
    "Brigandine",
    [
        ("White_Brigandine_A", 0),
        ("White_Brigandine_A_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1571,
    weight(18)|abundance(90)|head_armor(0)|body_armor(38)|leg_armor(12)|difficulty(17),
    imodbit_reinforced,
    [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_5, fac_kingdom_7, fac_kingdom_9, fac_kingdom_10]
],

[
    "olive_brigandine_a",
    "Olive Painted Brigandine",
    [
        ("Olive_Brigandine_A", 0),
        ("Olive_Brigandine_A_thick", imodbit_thick),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1571,
    weight(18)|abundance(90)|head_armor(0)|body_armor(38)|leg_armor(12)|difficulty(17),
    imodbit_thick,
    [], [fac_kingdom_3]
],

[
    "olive_brigandine_a_v1",
    "Olive Painted Brigandine",
    [
        ("Olive_Brigandine_A_v1", 0),
        ("Olive_Brigandine_A_v1_thick", imodbit_thick),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1571,
    weight(18)|abundance(90)|head_armor(0)|body_armor(38)|leg_armor(12)|difficulty(17),
    imodbit_thick,
    [], [fac_kingdom_3]
],

[
    "olive_brigandine_b",
    "Olive Painted Brigandine on Mail",
    [
        ("Olive_Brigandine_B", 0),
        ("Olive_Brigandine_B_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1804,
    weight(22)|abundance(80)|head_armor(0)|body_armor(42)|leg_armor(14)|difficulty(19),
    imodbit_reinforced,
    [], [fac_kingdom_3]
],

[
    "olive_brigandine_b_v1",
    "Olive Painted Brigandine on Mail",
    [
        ("Olive_Brigandine_B_v1", 0),
        ("Olive_Brigandine_B_v1_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1804,
    weight(22)|abundance(80)|head_armor(0)|body_armor(42)|leg_armor(14)|difficulty(19),
    imodbit_reinforced,
    [], [fac_kingdom_3]
],

[
    "olive_brigandine_c",
    "Olive Painted Leather Armor with Plates",
    [
        ("Olive_Brigandine_C", 0),
        ("Olive_Brigandine_C_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1804,
    weight(22)|abundance(80)|head_armor(0)|body_armor(42)|leg_armor(14)|difficulty(19),
    imodbit_reinforced,
    [], [fac_kingdom_3]
],

[
    "olive_brigandine_d",
    "Olive Painted Armor with Plates",
    [
        ("Olive_Brigandine_D", 0),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1893,
    weight(20)|abundance(80)|head_armor(0)|body_armor(41)|leg_armor(18)|difficulty(20),
    imodbits_none,
    [], [fac_kingdom_3]
],

[
    "olive_brigandine_d_v1",
    "Olive Painted Armor with Plates",
    [
        ("Olive_Brigandine_D_v1", 0),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1893,
    weight(20)|abundance(80)|head_armor(0)|body_armor(41)|leg_armor(18)|difficulty(20),
    imodbits_none,
    [], [fac_kingdom_3],
],

[
    "brown_brigandine_a",
    "Brown Painted Brigandine",
    [
        ("Brown_Brigandine_A", 0),
        ("Brown_Brigandine_A_thick", imodbit_thick),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1571,
    weight(18)|abundance(90)|head_armor(0)|body_armor(38)|leg_armor(12)|difficulty(17),
    imodbit_thick,
    [], [fac_kingdom_2]
],

[
    "brown_brigandine_a_v1",
    "Brown Painted Brigandine",
    [
        ("Brown_Brigandine_A_v1", 0),
        ("Brown_Brigandine_A_v1_thick", imodbit_thick),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1571,
    weight(18)|abundance(90)|head_armor(0)|body_armor(38)|leg_armor(12)|difficulty(17),
    imodbit_thick,
    [], [fac_kingdom_2]
],

[
    "brown_brigandine_b",
    "Brown Painted Brigandine on Mail",
    [
        ("Brown_Brigandine_B", 0),
        ("Brown_Brigandine_B_hardened", imodbit_hardened),
        ("Brown_Brigandine_B_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1804,
    weight(22)|abundance(80)|head_armor(0)|body_armor(42)|leg_armor(14)|difficulty(19),
    imodbit_hardened | imodbit_reinforced,
    [], [fac_kingdom_2]
],

[
    "brown_brigandine_b_v1",
    "Brown Painted Brigandine on Mail",
    [
        ("Brown_Brigandine_B_v1", 0),
        ("Brown_Brigandine_B_v1_hardened", imodbit_hardened),
        ("Brown_Brigandine_B_v1_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1804,
    weight(22)|abundance(80)|head_armor(0)|body_armor(42)|leg_armor(14)|difficulty(19),
    imodbit_hardened | imodbit_reinforced,
    [], [fac_kingdom_2]
],

[
    "red_brigandine_a",
    "Red Painted Brigandine",
    [
        ("Red_Brigandine_A", 0),
        ("Red_Brigandine_A_thick", imodbit_thick),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1571,
    weight(18)|abundance(90)|head_armor(0)|body_armor(38)|leg_armor(12)|difficulty(17),
    imodbit_thick,
    [], [fac_kingdom_1]
],

[
    "red_brigandine_a_v1",
    "Red Painted Brigandine",
    [
        ("Red_Brigandine_A_v1", 0),
        ("Red_Brigandine_A_v1_thick", imodbit_thick),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1571,
    weight(18)|abundance(90)|head_armor(0)|body_armor(38)|leg_armor(12)|difficulty(17),
    imodbit_thick,
    [], [fac_kingdom_1]
],

[
    "red_brigandine_b",
    "Red Painted Brigandine on Mail",
    [
        ("Red_Brigandine_B", 0),
        ("Red_Brigandine_B_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1804,
    weight(22)|abundance(80)|head_armor(0)|body_armor(42)|leg_armor(14)|difficulty(19),
    imodbit_reinforced,
    [], [fac_kingdom_1]
],

[
    "red_brigandine_b_v1",
    "Red Painted Brigandine on Mail",
    [
        ("Red_Brigandine_B_v1", 0),
        ("Red_Brigandine_B_v1_reinforced", imodbit_reinforced),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1804,
    weight(22)|abundance(80)|head_armor(0)|body_armor(42)|leg_armor(14)|difficulty(19),
    imodbit_reinforced,
    [], [fac_kingdom_1]
],

[
    "red_brigandine_c",
    "Red Painted Brigandine with Plates",
    [
        ("Red_Brigandine_C", 0),
        ("Red_Brigandine_C_thick", imodbit_thick),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1893,
    weight(20)|abundance(80)|head_armor(0)|body_armor(41)|leg_armor(18)|difficulty(20),
    imodbit_thick,
    [], [fac_kingdom_1]
],

[
    "red_brigandine_c_v1",
    "Red Painted Brigandine with Plates",
    [
        ("Red_Brigandine_C_v1", 0),
        ("Red_Brigandine_C_v1_thick", imodbit_thick),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 1893,
    weight(20)|abundance(80)|head_armor(0)|body_armor(41)|leg_armor(18)|difficulty(20),
    imodbit_thick,
    [], [fac_kingdom_1]
],

[
    "red_brigandine_d",
    "Red Painted Brigandine on Mail with Plates",
    [
        ("Red_Brigandine_D", 0),
        ("Red_Brigandine_D_thick", imodbit_thick),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 2181,
    weight(24)|abundance(70)|head_armor(0)|body_armor(45)|leg_armor(20)|difficulty(22),
    imodbit_thick,
    [], [fac_kingdom_1]
],

[
    "red_brigandine_d_v1",
    "Red Painted Brigandine on Mail with Plates",
    [
        ("Red_Brigandine_D_v1", 0),
        ("Red_Brigandine_D_v1_thick", imodbit_thick),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 2181,
    weight(24)|abundance(70)|head_armor(0)|body_armor(45)|leg_armor(20)|difficulty(22),
    imodbit_thick,
    [], [fac_kingdom_1]
],
# BRIGANDINES END

# PLATE ARMORS START
[
    "full_plate_armor_a",
    "Full Plate Armor",
    [
        ("Plate_Armor_A", 0),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 2830,
    weight(29)|abundance(50)|head_armor(0)|body_armor(57)|leg_armor(28)|difficulty(28),
    imodbits_none,
    [], [fac_kingdom_1, fac_kingdom_3, fac_kingdom_5, fac_kingdom_7, fac_kingdom_9, fac_kingdom_10]
],

[
    "full_plate_armor_b",
    "Full Plate Armor",
    [
        ("Plate_Armor_B", 0),
    ],
    itp_merchandise | itp_type_body_armor | itp_covers_legs,
    0, 2830,
    weight(29)|abundance(50)|head_armor(0)|body_armor(57)|leg_armor(28)|difficulty(28),
    imodbits_none,
    [], [fac_kingdom_1, fac_kingdom_3]
],
# PLATE ARMORS END

# ARMORS END

# HELMETS START
# Helmet Diffuculty is equal to the Armor / 3.5
# Helmet Price is equal to the (Armor * 10.5) + 9 - difficulty + (100 - abundance) * 2.5
["felt_a", "Felt Hat", [("Revised_Felt_A",0), ("Revised_Felt_A_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature|itp_civilian, 0, 51, weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0), imodbits_cloth],
["felt_a_v1", "Felt Hat with Feather", [("Revised_Felt_A_v1",0), ("Revised_Felt_A_v1_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature|itp_civilian, 0, 51, weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0), imodbits_cloth],
["felt_a_v2", "Felt Hat on Arming Cap", [("Revised_Felt_A_v2",0), ("Revised_Felt_A_v2_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature|itp_civilian, 0, 104, weight(1)|abundance(100)|head_armor(9)|body_armor(0)|leg_armor(0)|difficulty(0), imodbits_cloth],

["felt_b", "Felt Hat", [("Revised_Felt_B",0), ("Revised_Felt_B_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature|itp_civilian, 0, 51, weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0), imodbits_cloth],
["felt_b_v1", "Felt Hat on Hood", [("Revised_Felt_B_v1",0), ("Revised_Felt_B_v1_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature|itp_civilian, 0, 93, weight(1)|abundance(100)|head_armor(6)|body_armor(2)|leg_armor(0)|difficulty(0), imodbits_cloth],

["adventurer_hood_a", "Adventurer Hood", [("Adventurers_Hood_A",0), ("Adventurers_Hood_A_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature|itp_civilian, 0, 93, weight(1)|abundance(100)|head_armor(6)|body_armor(2)|leg_armor(0)|difficulty(0), imodbits_cloth],

["arming_cap_a", "Arming Cap", [("Revised_Arming_Cap_A",0), ("Revised_Arming_Cap_A_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 104, weight(1)|abundance(100)|head_armor(9)|body_armor(0)|leg_armor(0)|difficulty(0), imodbits_none],

["padded_coif_a", "Padded Coif", [("Revised_Padded_Coif_A",0), ("Revised_Padded_Coif_A_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 156, weight(1)|abundance(100)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(0), imodbits_cloth],
["padded_coif_a_v1", "Padded Coif on Hood", [("Revised_Padded_Coif_A_v1",0), ("Revised_Padded_Coif_A_v1_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 209, weight(1.5)|abundance(100)|head_armor(16)|body_armor(3)|leg_armor(0)|difficulty(0), imodbits_cloth],
["padded_coif_b", "Padded Coif", [("Revised_Padded_Coif_B",0), ("Revised_Padded_Coif_B_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 156, weight(1)|abundance(100)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(0), imodbits_cloth],
["padded_coif_b_v1", "Padded Coif on Hood", [("Revised_Padded_Coif_B_v1",0), ("Revised_Padded_Coif_B_v1_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 209, weight(1.5)|abundance(100)|head_armor(16)|body_armor(3)|leg_armor(0)|difficulty(0), imodbits_cloth],

["cervelliere_a", "Cervelliere on Arming Cap", [("Revised_Cervelliere_A",0), ("Revised_Cervelliere_A_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 252, weight(1)|abundance(100)|head_armor(24)|body_armor(0)|leg_armor(0)|difficulty(7), imodbits_armor],
["cervelliere_a_v1", "Cervelliere on Padded", [("Revised_Cervelliere_A_v1",0), ("Revised_Cervelliere_A_v1_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 315, weight(1.5)|abundance(100)|head_armor(26)|body_armor(4)|leg_armor(0)|difficulty(9), imodbits_armor],
["cervelliere_a_v2", "Cervelliere on Mail", [("Revised_Cervelliere_A_v2",0), ("Revised_Cervelliere_A_v2_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 369, weight(2)|abundance(95)|head_armor(28)|body_armor(6)|leg_armor(0)|difficulty(10), imodbits_armor],
["cervelliere_a_v3", "Cervelliere on Mail", [("Revised_Cervelliere_A_v3",0), ("Revised_Cervelliere_A_v3_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 379, weight(2)|abundance(95)|head_armor(29)|body_armor(6)|leg_armor(0)|difficulty(10), imodbits_armor],

["cervelliere_b", "Cervelliere on Arming Cap", [("Revised_Cervelliere_B",0), ("Revised_Cervelliere_B_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 252, weight(1)|abundance(100)|head_armor(24)|body_armor(0)|leg_armor(0)|difficulty(7), imodbits_armor],
["cervelliere_b_v1", "Cervelliere on Padded", [("Revised_Cervelliere_B_v1",0), ("Revised_Cervelliere_B_v1_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 315, weight(1.5)|abundance(100)|head_armor(26)|body_armor(4)|leg_armor(0)|difficulty(9), imodbits_armor],
["cervelliere_b_v2", "Cervelliere on Mail", [("Revised_Cervelliere_B_v2",0), ("Revised_Cervelliere_B_v2_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 369, weight(2)|abundance(95)|head_armor(28)|body_armor(6)|leg_armor(0)|difficulty(10), imodbits_armor],
["cervelliere_b_v3", "Cervelliere on Mail", [("Revised_Cervelliere_B_v3",0), ("Revised_Cervelliere_B_v3_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 379, weight(2)|abundance(95)|head_armor(29)|body_armor(6)|leg_armor(0)|difficulty(10), imodbits_armor],

["flat_top_a", "Flat Top on Arming Cap", [("Revised_Flat_Top_A",0), ("Revised_Flat_Top_A_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 315, weight(1.5)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(9), imodbits_armor],
["flat_top_a_v1", "Flat Top on Hood", [("Revised_Flat_Top_A_v1",0), ("Revised_Flat_Top_A_v1_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 347, weight(1.5)|abundance(100)|head_armor(31)|body_armor(2)|leg_armor(0)|difficulty(9), imodbits_armor],
["flat_top_a_v2", "Flat Top on Padding", [("Revised_Flat_Top_A_v2",0), ("Revised_Flat_Top_A_v2_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 390, weight(2)|abundance(95)|head_armor(32)|body_armor(4)|leg_armor(0)|difficulty(10), imodbits_armor],
["flat_top_a_v3", "Flat Top on Mail", [("Revised_Flat_Top_A_v3",0), ("Revised_Flat_Top_A_v3_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 443, weight(2.5)|abundance(90)|head_armor(34)|body_armor(6)|leg_armor(0)|difficulty(11), imodbits_armor],
["flat_top_a_v4", "Flat Top on Mail", [("Revised_Flat_Top_A_v4",0), ("Revised_Flat_Top_A_v4_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 453, weight(2.5)|abundance(90)|head_armor(35)|body_armor(6)|leg_armor(0)|difficulty(12), imodbits_armor],

["flat_top_b", "Flat Top with Noseguard on Arming Cap", [("Revised_Flat_Top_B",0), ("Revised_Flat_Top_B_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 336, weight(1.5)|abundance(100)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(9), imodbits_armor],
["flat_top_b_v1", "Flat Top with Noseguard on Hood", [("Revised_Flat_Top_B_v1",0), ("Revised_Flat_Top_B_v1_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 367, weight(1.5)|abundance(100)|head_armor(33)|body_armor(2)|leg_armor(0)|difficulty(10), imodbits_armor],
["flat_top_b_v2", "Flat Top with Noseguard on Padding", [("Revised_Flat_Top_B_v2",0), ("Revised_Flat_Top_B_v2_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 410, weight(1.5)|abundance(95)|head_armor(34)|body_armor(4)|leg_armor(0)|difficulty(11), imodbits_armor],
["flat_top_b_v3", "Flat Top with Noseguard on Mail", [("Revised_Flat_Top_B_v3",0), ("Revised_Flat_Top_B_v3_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 463, weight(1.5)|abundance(90)|head_armor(36)|body_armor(6)|leg_armor(0)|difficulty(12), imodbits_armor],
["flat_top_b_v4", "Flat Top with Noseguard on Mail", [("Revised_Flat_Top_B_v4",0), ("Revised_Flat_Top_B_v4_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 474, weight(1.5)|abundance(90)|head_armor(37)|body_armor(6)|leg_armor(0)|difficulty(12), imodbits_armor],

["chapel_a", "Chapel", [("Revised_Chapel_A",0), ("Revised_Chapel_A_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 326, weight(1.5)|abundance(100)|head_armor(31)|body_armor(0)|leg_armor(0)|difficulty(9), imodbits_armor],
["chapel_a_v1", "Chapel on Arming Cap", [("Revised_Chapel_A_v1",0), ("Revised_Chapel_A_v1_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 336, weight(1.5)|abundance(100)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(9), imodbits_armor],
["chapel_a_v2", "Chapel on Hood", [("Revised_Chapel_A_v2",0), ("Revised_Chapel_A_v2_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 379, weight(2)|abundance(95)|head_armor(33)|body_armor(2)|leg_armor(0)|difficulty(10), imodbits_armor],
["chapel_a_v3", "Chapel on Padding", [("Revised_Chapel_A_v3",0), ("Revised_Chapel_A_v3_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 433, weight(2)|abundance(90)|head_armor(35)|body_armor(4)|leg_armor(0)|difficulty(11), imodbits_armor],

["chapel_b", "Chapel", [("Revised_Chapel_B",0), ("Revised_Chapel_B_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 326, weight(1.5)|abundance(100)|head_armor(31)|body_armor(0)|leg_armor(0)|difficulty(9), imodbits_armor],
["chapel_b_v1", "Chapel on Arming Cap", [("Revised_Chapel_B_v1",0), ("Revised_Chapel_B_v1_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 336, weight(1.5)|abundance(100)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(9), imodbits_armor],
["chapel_b_v2", "Chapel on Hood", [("Revised_Chapel_B_v2",0), ("Revised_Chapel_B_v2_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 379, weight(2)|abundance(95)|head_armor(33)|body_armor(2)|leg_armor(0)|difficulty(10), imodbits_armor],
["chapel_b_v3", "Chapel on Padding", [("Revised_Chapel_B_v3",0), ("Revised_Chapel_B_v3_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 433, weight(2)|abundance(90)|head_armor(35)|body_armor(4)|leg_armor(0)|difficulty(11), imodbits_armor],

["chapel_c", "Chapel", [("Revised_Chapel_C",0), ("Revised_Chapel_C_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 326, weight(1.5)|abundance(100)|head_armor(31)|body_armor(0)|leg_armor(0)|difficulty(9), imodbits_armor],
["chapel_c_v1", "Chapel on Arming Cap", [("Revised_Chapel_C_v1",0), ("Revised_Chapel_C_v1_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 336, weight(1.5)|abundance(100)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(9), imodbits_armor],
["chapel_c_v2", "Chapel on Hood", [("Revised_Chapel_C_v2",0), ("Revised_Chapel_C_v2_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 379, weight(2)|abundance(95)|head_armor(33)|body_armor(2)|leg_armor(0)|difficulty(10), imodbits_armor],
["chapel_c_v3", "Chapel on Padding", [("Revised_Chapel_C_v3",0), ("Revised_Chapel_C_v3_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 433, weight(2)|abundance(90)|head_armor(35)|body_armor(4)|leg_armor(0)|difficulty(11), imodbits_armor],

["chapel_alpine_a", "Chapel", [("Revised_Chapel_Alpine_A",0), ("Revised_Chapel_Alpine_A_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 336, weight(1)|abundance(100)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(9), imodbits_armor],
["chapel_alpine_a_v1", "Chapel on Hood", [("Revised_Chapel_Alpine_A_v1",0), ("Revised_Chapel_Alpine_A_v1_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 395, weight(1.25)|abundance(100)|head_armor(35)|body_armor(2)|leg_armor(0)|difficulty(10), imodbits_armor],
["chapel_alpine_a_v2", "Chapel on Padded", [("Revised_Chapel_Alpine_A_v2",0), ("Revised_Chapel_Alpine_A_v2_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 453, weight(1.5)|abundance(95)|head_armor(37)|body_armor(4)|leg_armor(0)|difficulty(12), imodbits_armor],
["chapel_alpine_a_v3", "Chapel on Mail", [("Revised_Chapel_Alpine_A_v3",0), ("Revised_Chapel_Alpine_A_v3_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 493, weight(2)|abundance(90)|head_armor(39)|body_armor(6)|leg_armor(0)|difficulty(14), imodbits_armor],

["morion_a", "Morion", [("Revised_Morion_A",0), ("Revised_Morion_A_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 326, weight(1.5)|abundance(100)|head_armor(31)|body_armor(0)|leg_armor(0)|difficulty(9), imodbits_armor],
["morion_a_v1", "Morion on Arming Cap", [("Revised_Morion_A_v1",0), ("Revised_Morion_A_v1_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 336, weight(1.5)|abundance(100)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(9), imodbits_armor],
["morion_a_v2", "Morion on Hood", [("Revised_Morion_A_v2",0), ("Revised_Morion_A_v2_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 379, weight(2)|abundance(95)|head_armor(33)|body_armor(2)|leg_armor(0)|difficulty(10), imodbits_armor],

["morion_b", "Morion", [("Revised_Morion_B",0), ("Revised_Morion_B_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 367, weight(2)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(10), imodbits_armor],
["morion_b_v1", "Morion on Arming Cap", [("Revised_Morion_B_v1",0), ("Revised_Morion_B_v1_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 401, weight(2)|abundance(95)|head_armor(37)|body_armor(0)|leg_armor(0)|difficulty(11), imodbits_armor],
["morion_b_v2", "Morion on Hood", [("Revised_Morion_B_v2",0), ("Revised_Morion_B_v2_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 420, weight(2.5)|abundance(95)|head_armor(37)|body_armor(2)|leg_armor(0)|difficulty(11), imodbits_armor],
["morion_b_v3", "Morion on Padding", [("Revised_Morion_B_v3",0), ("Revised_Morion_B_v3_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 441, weight(2.5)|abundance(95)|head_armor(37)|body_armor(4)|leg_armor(0)|difficulty(12), imodbits_armor],
["morion_b_v4", "Morion on Mail", [("Revised_Morion_B_v4",0), ("Revised_Morion_B_v4_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 493, weight(3)|abundance(90)|head_armor(39)|body_armor(6)|leg_armor(0)|difficulty(13), imodbits_armor],
["morion_b_v5", "Morion on Mail", [("Revised_Morion_B_v5",0), ("Revised_Morion_B_v5_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 504, weight(3)|abundance(90)|head_armor(40)|body_armor(6)|leg_armor(0)|difficulty(13), imodbits_armor],

["eyeslot_kettlehat_a", "Kettle Hat", [("Revised_Kettlehat_A",0), ("Revised_Kettlehat_A_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 336, weight(1)|abundance(100)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(9), imodbits_armor],
["eyeslot_kettlehat_a_v1", "Kettle Hat on Arming Cap", [("Revised_Kettlehat_A_v1",0), ("Revised_Kettlehat_A_v1_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 347, weight(1)|abundance(100)|head_armor(33)|body_armor(0)|leg_armor(0)|difficulty(9), imodbits_armor],
["eyeslot_kettlehat_a_v2", "Kettle Hat on Hood", [("Revised_Kettlehat_A_v2",0), ("Revised_Kettlehat_A_v2_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 390, weight(1.5)|abundance(95)|head_armor(34)|body_armor(2)|leg_armor(0)|difficulty(10), imodbits_armor],
["eyeslot_kettlehat_a_v3", "Kettle Hat on Mail", [("Revised_Kettlehat_A_v3",0), ("Revised_Kettlehat_A_v3_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 493, weight(2)|abundance(90)|head_armor(39)|body_armor(6)|leg_armor(0)|difficulty(13), imodbits_armor],

["sallet_a", "Sallet", [("Revised_Sallet_A",0), ("Revised_Sallet_A_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 367, weight(2)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(10), imodbits_armor],
["sallet_a_v1", "Sallet on Arming Cap", [("Revised_Sallet_A_v1",0), ("Revised_Sallet_A_v1_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 401, weight(2)|abundance(95)|head_armor(37)|body_armor(0)|leg_armor(0)|difficulty(11), imodbits_armor],
["sallet_a_v2", "Sallet on Hood", [("Revised_Sallet_A_v2",0), ("Revised_Sallet_A_v2_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 420, weight(2.5)|abundance(95)|head_armor(37)|body_armor(2)|leg_armor(0)|difficulty(11), imodbits_armor],
["sallet_a_v3", "Sallet on Padding", [("Revised_Sallet_A_v3",0), ("Revised_Sallet_A_v3_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 441, weight(2.5)|abundance(95)|head_armor(37)|body_armor(4)|leg_armor(0)|difficulty(12), imodbits_armor],
["sallet_a_v4", "Sallet on Mail", [("Revised_Sallet_A_v4",0), ("Revised_Sallet_A_v4_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 493, weight(3)|abundance(90)|head_armor(39)|body_armor(6)|leg_armor(0)|difficulty(13), imodbits_armor],
["sallet_a_v5", "Sallet on Mail", [("Revised_Sallet_A_v5",0), ("Revised_Sallet_A_v5_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 504, weight(3)|abundance(90)|head_armor(40)|body_armor(6)|leg_armor(0)|difficulty(13), imodbits_armor],

["sallet_b", "Sallet with Open Visor", [("Revised_Sallet_B",0), ("Revised_Sallet_B_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 401, weight(2)|abundance(95)|head_armor(37)|body_armor(0)|leg_armor(0)|difficulty(11), imodbits_armor],
["sallet_b_v1", "Sallet with Open Visor on Arming Cap", [("Revised_Sallet_B_v1",0), ("Revised_Sallet_B_v1_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 441, weight(2.5)|abundance(95)|head_armor(39)|body_armor(0)|leg_armor(0)|difficulty(12), imodbits_armor],
["sallet_b_v2", "Sallet with Open Visor on Hood", [("Revised_Sallet_B_v2",0), ("Revised_Sallet_B_v2_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 465, weight(2.5)|abundance(90)|head_armor(40)|body_armor(2)|leg_armor(0)|difficulty(13), imodbits_armor],
["sallet_b_v3", "Sallet with Open Visor on Padding", [("Revised_Sallet_B_v3",0), ("Revised_Sallet_B_v3_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 496, weight(2.5)|abundance(85)|head_armor(42)|body_armor(4)|leg_armor(0)|difficulty(13), imodbits_armor],
["sallet_b_v4", "Sallet with Open Visor on Mail", [("Revised_Sallet_B_v4",0), ("Revised_Sallet_B_v4_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 517, weight(2.5)|abundance(85)|head_armor(42)|body_armor(4)|leg_armor(0)|difficulty(13), imodbits_armor],
["sallet_b_v5", "Sallet with Open Visor on Mail", [("Revised_Sallet_B_v5",0), ("Revised_Sallet_B_v5_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 528, weight(2.5)|abundance(85)|head_armor(43)|body_armor(4)|leg_armor(0)|difficulty(13), imodbits_armor],

["sallet_c", "Sallet with Closed Visor", [("Revised_Sallet_C",0), ("Revised_Sallet_C_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 441, weight(2.5)|abundance(95)|head_armor(39)|body_armor(0)|leg_armor(0)|difficulty(12), imodbits_armor],
["sallet_c_v1", "Sallet with Closed Visor on Arming Cap", [("Revised_Sallet_C_v1",0), ("Revised_Sallet_C_v1_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 465, weight(2.5)|abundance(90)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(13), imodbits_armor],
["sallet_c_v2", "Sallet with Closed Visor on Hood", [("Revised_Sallet_C_v2",0), ("Revised_Sallet_C_v2_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 496, weight(2.5)|abundance(85)|head_armor(42)|body_armor(2)|leg_armor(0)|difficulty(13), imodbits_armor],
["sallet_c_v3", "Sallet with Closed Visor on Padding", [("Revised_Sallet_C_v3",0), ("Revised_Sallet_C_v3_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 517, weight(2.5)|abundance(85)|head_armor(42)|body_armor(4)|leg_armor(0)|difficulty(13), imodbits_armor],
["sallet_c_v4", "Sallet with Closed Visor on Mail", [("Revised_Sallet_C_v4",0), ("Revised_Sallet_C_v4_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 528, weight(2.5)|abundance(85)|head_armor(43)|body_armor(4)|leg_armor(0)|difficulty(13), imodbits_armor],
["sallet_c_v5", "Sallet with Closed Visor on Mail", [("Revised_Sallet_C_v5",0), ("Revised_Sallet_C_v5_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 539, weight(2.5)|abundance(85)|head_armor(44)|body_armor(4)|leg_armor(0)|difficulty(13), imodbits_armor],

["sallet_d", "Sallet", [("Revised_Sallet_D",0), ("Revised_Sallet_D_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 367, weight(2)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(10), imodbits_armor],
["sallet_d_v1", "Sallet on Arming Cap", [("Revised_Sallet_D_v1",0), ("Revised_Sallet_D_v1_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 401, weight(2)|abundance(95)|head_armor(37)|body_armor(0)|leg_armor(0)|difficulty(11), imodbits_armor],
["sallet_d_v2", "Sallet on Hood", [("Revised_Sallet_D_v2",0), ("Revised_Sallet_D_v2_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 420, weight(2.5)|abundance(95)|head_armor(37)|body_armor(2)|leg_armor(0)|difficulty(11), imodbits_armor],
["sallet_d_v3", "Sallet on Padding", [("Revised_Sallet_D_v3",0), ("Revised_Sallet_D_v3_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 441, weight(2.5)|abundance(95)|head_armor(37)|body_armor(4)|leg_armor(0)|difficulty(12), imodbits_armor],
["sallet_d_v4", "Sallet on Mail", [("Revised_Sallet_D_v4",0), ("Revised_Sallet_D_v4_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 493, weight(3)|abundance(90)|head_armor(39)|body_armor(6)|leg_armor(0)|difficulty(13), imodbits_armor],
["sallet_d_v5", "Sallet on Mail", [("Revised_Sallet_D_v5",0), ("Revised_Sallet_D_v5_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 504, weight(3)|abundance(90)|head_armor(40)|body_armor(6)|leg_armor(0)|difficulty(13), imodbits_armor],

# CELESTIAL HELMETS START
["celestial_sallet_a", "Sallet", [("Celestial_Sallet_A",0), ("Celestial_Sallet_A_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 367, weight(2)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(10), imodbits_armor],
["celestial_sallet_a_v1", "Sallet on Arming Cap", [("Celestial_Sallet_A_v1",0), ("Celestial_Sallet_A_v1_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 401, weight(2)|abundance(95)|head_armor(37)|body_armor(0)|leg_armor(0)|difficulty(11), imodbits_armor],
["celestial_sallet_a_v2", "Sallet on Hood", [("Celestial_Sallet_A_v2",0), ("Celestial_Sallet_A_v2_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 420, weight(2.5)|abundance(95)|head_armor(37)|body_armor(2)|leg_armor(0)|difficulty(11), imodbits_armor],
["celestial_sallet_a_v3", "Sallet on Padding", [("Celestial_Sallet_A_v3",0), ("Celestial_Sallet_A_v3_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 441, weight(2.5)|abundance(95)|head_armor(37)|body_armor(4)|leg_armor(0)|difficulty(12), imodbits_armor],
["celestial_sallet_a_v4", "Sallet on Mail", [("Celestial_Sallet_A_v4",0), ("Celestial_Sallet_A_v4_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 493, weight(3)|abundance(90)|head_armor(39)|body_armor(6)|leg_armor(0)|difficulty(13), imodbits_armor],
["celestial_sallet_a_v5", "Sallet on Mail", [("Celestial_Sallet_A_v5",0), ("Celestial_Sallet_A_v5_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 504, weight(3)|abundance(90)|head_armor(40)|body_armor(6)|leg_armor(0)|difficulty(13), imodbits_armor],

["celestial_sallet_b", "Sallet with Open Visor", [("Celestial_Sallet_B",0), ("Celestial_Sallet_B_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 401, weight(2)|abundance(95)|head_armor(37)|body_armor(0)|leg_armor(0)|difficulty(11), imodbits_armor],
["celestial_sallet_b_v1", "Sallet with Open Visor on Arming Cap", [("Celestial_Sallet_B_v1",0), ("Celestial_Sallet_B_v1_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 441, weight(2.5)|abundance(95)|head_armor(39)|body_armor(0)|leg_armor(0)|difficulty(12), imodbits_armor],
["celestial_sallet_b_v2", "Sallet with Open Visor on Hood", [("Celestial_Sallet_B_v2",0), ("Celestial_Sallet_B_v2_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 465, weight(2.5)|abundance(90)|head_armor(40)|body_armor(2)|leg_armor(0)|difficulty(13), imodbits_armor],
["celestial_sallet_b_v3", "Sallet with Open Visor on Padding", [("Celestial_Sallet_B_v3",0), ("Celestial_Sallet_B_v3_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 496, weight(2.5)|abundance(85)|head_armor(42)|body_armor(4)|leg_armor(0)|difficulty(13), imodbits_armor],
["celestial_sallet_b_v4", "Sallet with Open Visor on Mail", [("Celestial_Sallet_B_v4",0), ("Celestial_Sallet_B_v4_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 517, weight(2.5)|abundance(85)|head_armor(42)|body_armor(4)|leg_armor(0)|difficulty(13), imodbits_armor],
["celestial_sallet_b_v5", "Sallet with Open Visor on Mail", [("Celestial_Sallet_B_v5",0), ("Celestial_Sallet_B_v5_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 528, weight(2.5)|abundance(85)|head_armor(43)|body_armor(4)|leg_armor(0)|difficulty(13), imodbits_armor],

["celestial_sallet_c", "Sallet with Closed Visor", [("Celestial_Sallet_C",0), ("Celestial_Sallet_C_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 441, weight(2.5)|abundance(95)|head_armor(39)|body_armor(0)|leg_armor(0)|difficulty(12), imodbits_armor],
["celestial_sallet_c_v1", "Sallet with Closed Visor on Arming Cap", [("Celestial_Sallet_C_v1",0), ("Celestial_Sallet_C_v1_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 465, weight(2.5)|abundance(90)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(13), imodbits_armor],
["celestial_sallet_c_v2", "Sallet with Closed Visor on Hood", [("Celestial_Sallet_C_v2",0), ("Celestial_Sallet_C_v2_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 496, weight(2.5)|abundance(85)|head_armor(42)|body_armor(2)|leg_armor(0)|difficulty(13), imodbits_armor],
["celestial_sallet_c_v3", "Sallet with Closed Visor on Padding", [("Celestial_Sallet_C_v3",0), ("Celestial_Sallet_C_v3_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 517, weight(2.5)|abundance(85)|head_armor(42)|body_armor(4)|leg_armor(0)|difficulty(13), imodbits_armor],
["celestial_sallet_c_v4", "Sallet with Closed Visor on Mail", [("Celestial_Sallet_C_v4",0), ("Celestial_Sallet_C_v4_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 528, weight(2.5)|abundance(85)|head_armor(43)|body_armor(4)|leg_armor(0)|difficulty(13), imodbits_armor],
["celestial_sallet_c_v5", "Sallet with Closed Visor on Mail", [("Celestial_Sallet_C_v5",0), ("Celestial_Sallet_C_v5_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 539, weight(2.5)|abundance(85)|head_armor(44)|body_armor(4)|leg_armor(0)|difficulty(13), imodbits_armor],

["celestial_sallet_d", "Sallet with Closed Visor on Bevor", [("Celestial_Sallet_D",0), ("Celestial_Sallet_D_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 651, weight(3)|abundance(60)|head_armor(47)|body_armor(6)|leg_armor(0)|difficulty(15), imodbits_armor],
["celestial_sallet_d_v1", "Sallet with Closed Visor on Bevor", [("Celestial_Sallet_D_v1",0), ("Celestial_Sallet_D_v1_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 652, weight(3)|abundance(60)|head_armor(47)|body_armor(6)|leg_armor(0)|difficulty(15), imodbits_armor],
# CELESTIAL HELMETS END

# SOLARIAN HELMETS START
["yellow_turban_a", "Turban", [("Yellow_Turban_A",0), ("Yellow_Turban_A_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 104, weight(1)|abundance(100)|head_armor(9)|body_armor(0)|leg_armor(0)|difficulty(0), imodbits_cloth, [], [fac_kingdom_6]],
["yellow_turban_b", "Turban", [("Yellow_Turban_B",0), ("Yellow_Turban_B_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 104, weight(1)|abundance(100)|head_armor(9)|body_armor(0)|leg_armor(0)|difficulty(0), imodbits_cloth, [], [fac_kingdom_6]],
["yellow_turban_c", "Turban", [("Yellow_Turban_C",0), ("Yellow_Turban_C_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 104, weight(1)|abundance(100)|head_armor(9)|body_armor(0)|leg_armor(0)|difficulty(0), imodbits_cloth, [], [fac_kingdom_6]],

["yellow_turban_chapel_a", "Chapel on Turban", [("Yellow_Turban_Chapel_A",0), ("Yellow_Turban_Chapel_A_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 356, weight(1)|abundance(100)|head_armor(32)|body_armor(2)|leg_armor(0)|difficulty(10), imodbits_armor, [], [fac_kingdom_6]],
["yellow_turban_chapel_a_v1", "Chapel on Turban", [("Yellow_Turban_Chapel_A_v1",0), ("Yellow_Turban_Chapel_A_v1_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 377, weight(1)|abundance(100)|head_armor(33)|body_armor(3)|leg_armor(0)|difficulty(10), imodbits_armor, [], [fac_kingdom_6]],

["yellow_turban_sallet_a", "Sallet on Turban", [("Yellow_Turban_Sallet_A",0), ("Yellow_Turban_Sallet_A_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 433, weight(1.5)|abundance(90)|head_armor(37)|body_armor(2)|leg_armor(0)|difficulty(11), imodbits_armor, [], [fac_kingdom_6]],
["yellow_turban_sallet_a_v1", "Sallet on Turban", [("Yellow_Turban_Sallet_A_v1",0), ("Yellow_Turban_Sallet_A_v1_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 453, weight(1.5)|abundance(90)|head_armor(38)|body_armor(3)|leg_armor(0)|difficulty(12), imodbits_armor, [], [fac_kingdom_6]],

["solarian_footman_helmet_a", "Footman Helmet on Turban", [("Solarian_Footman_Helmet_A",0), ("Solarian_Footman_Helmet_A_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 446, weight(1.5)|abundance(85)|head_armor(37)|body_armor(2)|leg_armor(0)|difficulty(11), imodbits_armor, [], [fac_kingdom_6]],
["solarian_footman_helmet_a_v1", "Footman Helmet on Turban", [("Solarian_Footman_Helmet_A_v1",0), ("Solarian_Footman_Helmet_A_v1_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 467, weight(1.5)|abundance(85)|head_armor(38)|body_armor(3)|leg_armor(0)|difficulty(12), imodbits_armor, [], [fac_kingdom_6]],

["solarian_footman_helmet_b", "Masked Footman Helmet on Padded", [("Solarian_Footman_Helmet_B",0), ("Solarian_Footman_Helmet_B_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 519, weight(1.5)|abundance(80)|head_armor(41)|body_armor(4)|leg_armor(0)|difficulty(13), imodbits_armor, [], [fac_kingdom_6]],
["solarian_footman_helmet_b_v1", "Masked Footman Helmet on Mail", [("Solarian_Footman_Helmet_B_v1",0), ("Solarian_Footman_Helmet_B_v1_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 560, weight(1.75)|abundance(80)|head_armor(43)|body_armor(6)|leg_armor(0)|difficulty(14), imodbits_armor, [], [fac_kingdom_6]],
# SOLARIAN HELMETS END

# MENEGRAS HELMETS START
["menegras_sallet_a", "Menegras Sallet", [("Menegras_Sallet_A",0), ("Menegras_Sallet_A_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_civilian|itp_attach_armature ,0, 463 , weight(2)|abundance(90)|head_armor(38)|body_armor(4)|leg_armor(0)|difficulty(12), imodbits_armor],
["menegras_sallet_b", "Menegras Sallet open Visor", [("Menegras_Sallet_B",0), ("Menegras_Sallet_B_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_civilian|itp_attach_armature ,0, 496 , weight(2.5)|abundance(85)|head_armor(40)|body_armor(4)|leg_armor(0)|difficulty(13), imodbits_armor],
["menegras_sallet_c", "Menegras Sallet closed Visor", [("Menegras_Sallet_C",0), ("Menegras_Sallet_C_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_civilian|itp_attach_armature ,0, 517 , weight(2.5)|abundance(85)|head_armor(42)|body_armor(4)|leg_armor(0)|difficulty(13), imodbits_armor],

["menegras_kettlehat_a", "Menegras Kettle Hat", [("Menegras_Kettlehat_A",0), ("Menegras_Kettlehat_A_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_civilian|itp_attach_armature ,0, 465 , weight(2)|abundance(85)|head_armor(37)|body_armor(4)|leg_armor(0)|difficulty(12), imodbits_armor],

["menegras_chapel_a", "Menegras Chapel de Fer", [("Menegras_Chapel_A",0), ("Menegras_Chapel_A_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_civilian|itp_attach_armature ,0, 465 , weight(2)|abundance(85)|head_armor(37)|body_armor(4)|leg_armor(0)|difficulty(12), imodbits_armor],
["menegras_chapel_b", "Menegras Chapel de Fer", [("Menegras_Chapel_B",0), ("Menegras_Chapel_B_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_civilian|itp_attach_armature ,0, 465 , weight(2)|abundance(85)|head_armor(37)|body_armor(4)|leg_armor(0)|difficulty(12), imodbits_armor],
# MENEGRAS HELMETS END

# NASAL HELMETS START
["nasal_helmet_a", "Nasal Helmet", [("Revised_Nasal_A",0), ("Revised_Nasal_A_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature ,0, 372 , weight(2)|abundance(90)|head_armor(33)|body_armor(0)|leg_armor(0)|difficulty(9), imodbits_armor],
["nasal_helmet_a_v1", "Nasal Helmet on Hood", [("Revised_Nasal_A_v1",0), ("Revised_Nasal_A_v1_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature ,0, 412 , weight(2.5)|abundance(90)|head_armor(35)|body_armor(2)|leg_armor(0)|difficulty(11), imodbits_armor],
["nasal_helmet_a_v2", "Nasal Helmet on Padding", [("Revised_Nasal_A_v2",0), ("Revised_Nasal_A_v2_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature ,0, 465 , weight(3)|abundance(90)|head_armor(37)|body_armor(4)|leg_armor(0)|difficulty(12), imodbits_armor],
["nasal_helmet_a_v3", "Nasal Helmet on Mail", [("Revised_Nasal_A_v3",0), ("Revised_Nasal_A_v3_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature ,0, 493 , weight(3.5)|abundance(90)|head_armor(39)|body_armor(6)|leg_armor(0)|difficulty(13), imodbits_armor],
["nasal_helmet_a_v4", "Nasal Helmet on Mail", [("Revised_Nasal_A_v4",0), ("Revised_Nasal_A_v4_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature ,0, 504 , weight(3.5)|abundance(90)|head_armor(40)|body_armor(6)|leg_armor(0)|difficulty(13), imodbits_armor],

["nasal_helmet_b", "Nasal Helmet", [("Revised_Nasal_B",0), ("Revised_Nasal_B_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature ,0, 372 , weight(2)|abundance(90)|head_armor(33)|body_armor(0)|leg_armor(0)|difficulty(9), imodbits_armor],
["nasal_helmet_b_v1", "Nasal Helmet on Hood", [("Revised_Nasal_B_v1",0), ("Revised_Nasal_B_v1_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature ,0, 412 , weight(2.5)|abundance(90)|head_armor(35)|body_armor(2)|leg_armor(0)|difficulty(11), imodbits_armor],
["nasal_helmet_b_v2", "Nasal Helmet on Padding", [("Revised_Nasal_B_v2",0), ("Revised_Nasal_B_v2_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature ,0, 465 , weight(3)|abundance(90)|head_armor(37)|body_armor(4)|leg_armor(0)|difficulty(12), imodbits_armor],
["nasal_helmet_b_v3", "Nasal Helmet on Mail", [("Revised_Nasal_B_v3",0), ("Revised_Nasal_B_v3_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature ,0, 493 , weight(3.5)|abundance(90)|head_armor(39)|body_armor(6)|leg_armor(0)|difficulty(13), imodbits_armor],
["nasal_helmet_b_v4", "Nasal Helmet on Mail", [("Revised_Nasal_B_v4",0), ("Revised_Nasal_B_v4_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature ,0, 504 , weight(3.5)|abundance(90)|head_armor(40)|body_armor(6)|leg_armor(0)|difficulty(13), imodbits_armor],

["facemask_a", "Facemask Helmet", [("Facemask_Helm_A",0), ("Facemask_Helm_A_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature ,0, 424 , weight(2)|abundance(85)|head_armor(35)|body_armor(2)|leg_armor(0)|difficulty(11), imodbits_armor],
["facemask_a_v1", "Facemask Helmet on Padding", [("Facemask_Helm_A_v1",0), ("Facemask_Helm_A_v1_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature ,0, 465 , weight(2.5)|abundance(85)|head_armor(37)|body_armor(4)|leg_armor(0)|difficulty(12), imodbits_armor],
["facemask_a_v2", "Facemask Helmet on Mail", [("Facemask_Helm_A_v2",0), ("Facemask_Helm_A_v2_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature ,0, 506 , weight(3)|abundance(85)|head_armor(39)|body_armor(6)|leg_armor(0)|difficulty(13), imodbits_armor],
["facemask_a_v3", "Facemask Helmet on Mail", [("Facemask_Helm_A_v3",0), ("Facemask_Helm_A_v3_inv",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature ,0, 517 , weight(3)|abundance(85)|head_armor(40)|body_armor(6)|leg_armor(0)|difficulty(13), imodbits_armor],
# NASAL HELMETS END

# HELMETS END

# WEAPONS START
# Difficulty: Biggest damage type / 3
# Price: speed + length + damage combined - difficulty
[
    "falchion_a",
    "Falchion",
    [
        ("Revised_Falchion_A",0),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_merchandise | itp_primary,
    itc_scimitar | itcf_carry_sword_left_hip,
    181,
    weight(2.5) | difficulty(9) | spd_rtng(98) | weapon_length(64) | swing_damage(28, cut) | thrust_damage(0, pierce), 
    imodbits_sword
],

[
    "falchion_a_v1",
    "Falchion",
    [
        ("Revised_Falchion_A_v1",0),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_merchandise | itp_primary,
    itc_scimitar | itcf_carry_sword_left_hip,
    183,
    weight(2.5) | difficulty(10) | spd_rtng(98) | weapon_length(66) | swing_damage(29, cut) | thrust_damage(0, pierce), 
    imodbits_sword
],

[   
    "falchion_a_v2",
    "Falchion",
    [
        ("Revised_Falchion_A_v2",0),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_merchandise | itp_primary,
    itc_scimitar | itcf_carry_sword_left_hip,
    193,
    weight(2.5) | difficulty(10) | spd_rtng(97) | weapon_length(76) | swing_damage(30, cut) | thrust_damage(0, pierce),
    imodbits_sword
],

[
    "falchion_b",
    "Low Quality Falchion",
    [
        ("Revised_Falchion_B",0),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_merchandise | itp_primary,
    itc_scimitar | itcf_carry_sword_left_hip,
    175,
    weight(2) | difficulty(8) | spd_rtng(96) | weapon_length(62) | swing_damage(25, cut) | thrust_damage(0, pierce),
    imodbits_sword
],

[
    "falchion_b_v1",
    "Low Quality Falchion",
    [
        ("Revised_Falchion_B_v1",0),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_merchandise | itp_primary,
    itc_scimitar | itcf_carry_sword_left_hip,
    180,
    weight(2.25) | difficulty(9) | spd_rtng(96) | weapon_length(66) | swing_damage(27, cut) | thrust_damage(0, pierce), 
    imodbits_sword
],

[
    "falchion_b_v2",
    "Low Quality Falchion",
    [
        ("Revised_Falchion_B_v2",0),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_merchandise | itp_primary,
    itc_scimitar | itcf_carry_sword_left_hip,
    187,
    weight(2.25) | difficulty(9) | spd_rtng(95) | weapon_length(72) | swing_damage(28, cut) | thrust_damage(0, pierce),
    imodbits_sword
],

[
    "falchion_c",
    "Good Quality Falchion",
    [
        ("Revised_Falchion_C",0),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_merchandise | itp_primary,
    itc_scimitar | itcf_carry_sword_left_hip,
    191,
    weight(2.5) | difficulty(9) | spd_rtng(99) | weapon_length(64) | swing_damage(30, cut) | thrust_damage(0, pierce), 
    imodbits_sword
],

[
    "falchion_c_v1",
    "Good Quality Falchion",
    [
        ("Revised_Falchion_C_v1",0),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_merchandise | itp_primary,
    itc_scimitar | itcf_carry_sword_left_hip,
    197,
    weight(2.5) | difficulty(10) | spd_rtng(99) | weapon_length(66) | swing_damage(31, cut) | thrust_damage(0, pierce), 
    imodbits_sword
],

[   
    "falchion_c_v2",
    "Good Quality Falchion",
    [
        ("Revised_Falchion_C_v2",0),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_merchandise | itp_primary,
    itc_scimitar | itcf_carry_sword_left_hip,
    203,
    weight(2.5) | difficulty(11) | spd_rtng(99) | weapon_length(76) | swing_damage(32, cut) | thrust_damage(0, pierce),
    imodbits_sword
],

# SHORT SWORDS START
[
    "sword_short_a",
    "Short Sword",
    [
        ("Revised_Short_Sword_A",0),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_merchandise | itp_primary,
    itc_longsword | itcf_carry_sword_left_hip,
    203,
    weight(1.5) | difficulty(9) | spd_rtng(98) | weapon_length(75) | swing_damage(27, cut) | thrust_damage(22,  pierce),
    imodbits_sword_high
],

[
    "sword_short_a_v1",
    "Short Sword",
    [
        ("Revised_Short_Sword_A_v1",0),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_merchandise | itp_primary,
    itc_longsword | itcf_carry_sword_left_hip,
    217,
    weight(2.0) | difficulty(9) | spd_rtng(98) | weapon_length(88) | swing_damage(28, cut) | thrust_damage(22,  pierce),
    imodbits_sword_high
],

[
    "sword_short_a_v2",
    "Short Sword",
    [
        ("Revised_Short_Sword_A_v2",0),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_merchandise | itp_primary,
    itc_longsword | itcf_carry_sword_left_hip,
    218,
    weight(2.0) | difficulty(9) | spd_rtng(98) | weapon_length(88) | swing_damage(27, cut) | thrust_damage(24,  pierce),
    imodbits_sword_high
],

[   
    "sword_short_b",
    "Good Quality Short Sword",
    [
        ("Revised_Short_Sword_B",0),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_merchandise | itp_primary,
    itc_longsword | itcf_carry_sword_left_hip,
    217,
    weight(1.5) | difficulty(9) | spd_rtng(99) | weapon_length(75) | swing_damage(28, cut) | thrust_damage(23,  pierce),
    imodbits_sword_high
],

[
    "sword_short_b_v1",
    "Good Quality Short Sword",
    [
        ("Revised_Short_Sword_B_v1",0),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_merchandise | itp_primary,
    itc_longsword | itcf_carry_sword_left_hip,
    231,
    weight(2.0) | difficulty(9) | spd_rtng(99) | weapon_length(88) | swing_damage(29, cut) | thrust_damage(23,  pierce),
    imodbits_sword_high
],

[
    "sword_short_b_v2",
    "Good Quality Short Sword",
    [
        ("Revised_Short_Sword_B_v2",0),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_merchandise | itp_primary,
    itc_longsword | itcf_carry_sword_left_hip,
    232,
    weight(2.0) | difficulty(9) | spd_rtng(99) | weapon_length(88) | swing_damage(28, cut) | thrust_damage(25,  pierce),
    imodbits_sword_high
],
# SHORT SWORDS END

# REGULAR SWORDS START
[
    "sword_a",
    "Sword",
    [
        ("Revised_Sword_A",0),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_merchandise | itp_primary,
    itc_longsword | itcf_carry_sword_left_hip,
    231,
    weight(2.5) | difficulty(9) | spd_rtng(98) | weapon_length(99) | swing_damage(27, cut) | thrust_damage(22,  pierce),
    imodbits_sword_high
],

[
    "sword_a_v1",
    "Sword",
    [
        ("Revised_Sword_A_v1",0),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_merchandise | itp_primary,
    itc_longsword | itcf_carry_sword_left_hip,
    245,
    weight(3.0) | difficulty(9) | spd_rtng(98) | weapon_length(103) | swing_damage(28, cut) | thrust_damage(22,  pierce),
    imodbits_sword_high
],

[
    "sword_a_v2",
    "Sword",
    [
        ("Revised_Sword_A_v2",0),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_merchandise | itp_primary,
    itc_longsword | itcf_carry_sword_left_hip,
    256,
    weight(3.0) | difficulty(10) | spd_rtng(98) | weapon_length(105) | swing_damage(30, cut) | thrust_damage(24,  pierce),
    imodbits_sword_high
],

[
    "sword_a_v3",
    "Sword",
    [
        ("Revised_Sword_A_v3",0),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_merchandise | itp_primary,
    itc_longsword | itcf_carry_sword_left_hip,
    248,
    weight(3.0) | difficulty(10) | spd_rtng(99) | weapon_length(99) | swing_damage(29, cut) | thrust_damage(24,  pierce),
    imodbits_sword_high
],

[
    "sword_b",
    "Eastern Sword",
    [
        ("Revised_Sword_B",0),
        ("Revised_Sword_B_scabbard",ixmesh_carry),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_merchandise | itp_primary,
    itc_longsword | itcf_carry_sword_left_hip | itcf_show_holster_when_drawn,
    231,
    weight(2.5) | difficulty(9) | spd_rtng(98) | weapon_length(99) | swing_damage(27, cut) | thrust_damage(22,  pierce),
    imodbits_sword_high
],

[
    "sword_b_v1",
    "Eastern Sword",
    [
        ("Revised_Sword_B_v1",0),
        ("Revised_Sword_B_v1_scabbard",ixmesh_carry),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_merchandise | itp_primary,
    itc_longsword | itcf_carry_sword_left_hip | itcf_show_holster_when_drawn,
    229,
    weight(2.0) | difficulty(9) | spd_rtng(98) | weapon_length(88) | swing_damage(28, cut) | thrust_damage(25,  pierce),
    imodbits_sword_high
],

[
    "sword_b_v2",
    "Eastern Sword",
    [
        ("Revised_Sword_B_v2",0),
        ("Revised_Sword_B_v2_scabbard",ixmesh_carry),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_merchandise | itp_primary,
    itc_longsword | itcf_carry_sword_left_hip | itcf_show_holster_when_drawn,
    251,
    weight(2.5) | difficulty(10) | spd_rtng(98) | weapon_length(105) | swing_damage(31, cut) | thrust_damage(22,  pierce),
    imodbits_sword_high
],

[
    "sword_b_v3",
    "Western Thrusting Sword",
    [
        ("Revised_Sword_B_v3",0),
        ("Revised_Sword_B_v3_scabbard",ixmesh_carry),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_merchandise | itp_primary,
    itc_longsword | itcf_carry_sword_left_hip | itcf_show_holster_when_drawn,
    248,
    weight(1.5) | difficulty(10) | spd_rtng(99) | weapon_length(98) | swing_damage(29, cut) | thrust_damage(29,  pierce),
    imodbits_sword_high
],

[
    "sword_b_v4",
    "Western Thrusting Sword",
    [
        ("Revised_Sword_B_v4",0),
        ("Revised_Sword_B_v4_scabbard",ixmesh_carry),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_merchandise | itp_primary,
    itc_longsword | itcf_carry_sword_left_hip | itcf_show_holster_when_drawn,
    251,
    weight(1.5) | difficulty(11) | spd_rtng(99) | weapon_length(101) | swing_damage(30, cut) | thrust_damage(32,  pierce),
    imodbits_sword_high
],
# REGULAR SWORDS END

# KNIGHT SWORDS START
# Abit more expensive because of status
[
    "sword_knight_a",
    "Knight Sword",
    [
        ("Revised_Knight_Sword_A",0),
        ("Revised_Knight_Sword_A_scabbard",ixmesh_carry),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_merchandise | itp_primary,
    itc_longsword | itcf_carry_sword_left_hip | itcf_show_holster_when_drawn,
    445,
    weight(2.0) | difficulty(11) | spd_rtng(99) | weapon_length(101) | swing_damage(33, cut) | thrust_damage(28,  pierce),
    imodbits_sword_high
],

[
    "sword_knight_a_v1",
    "Knight Sword",
    [
        ("Revised_Knight_Sword_A_v1",0),
        ("Revised_Knight_Sword_A_v1_scabbard",ixmesh_carry),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_merchandise | itp_primary,
    itc_longsword | itcf_carry_sword_left_hip | itcf_show_holster_when_drawn,
    445,
    weight(2.0) | difficulty(11) | spd_rtng(99) | weapon_length(101) | swing_damage(33, cut) | thrust_damage(28,  pierce),
    imodbits_sword_high
],

[
    "sword_knight_a_v2",
    "Knight Sword",
    [
        ("Revised_Knight_Sword_A_v2",0),
        ("Revised_Knight_Sword_A_v2_scabbard",ixmesh_carry),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_merchandise | itp_primary,
    itc_longsword | itcf_carry_sword_left_hip | itcf_show_holster_when_drawn,
    445,
    weight(2.0) | difficulty(11) | spd_rtng(99) | weapon_length(101) | swing_damage(33, cut) | thrust_damage(28,  pierce),
    imodbits_sword_high
],
# KNIGHT SWORDS END

# TWO HANDED SWORDS START
# +100 price for two handed
[
    "sword_great_a",
    "Great Sword",
    [
        ("Revised_Great_Sword_A",0),
    ],
    itp_craftable | itp_type_two_handed_wpn | itp_merchandise | itp_two_handed | itp_primary,
    itc_greatsword | itcf_carry_sword_back,
    373,
    weight(3.5) | difficulty(13) | spd_rtng(94) | weapon_length(123) | swing_damage(39, cut) | thrust_damage(30,  pierce),
    imodbits_sword_high
],

[
    "sword_great_a_v1",
    "Great Sword",
    [
        ("Revised_Great_Sword_A_v1",0),
    ],
    itp_craftable | itp_type_two_handed_wpn | itp_merchandise | itp_two_handed | itp_primary,
    itc_greatsword | itcf_carry_sword_back,
    383,
    weight(3.5) | difficulty(13) | spd_rtng(94) | weapon_length(135) | swing_damage(41, cut) | thrust_damage(32,  pierce),
    imodbits_sword_high
],

[
    "sword_great_b",
    "Great Sword of War",
    [
        ("Revised_Great_Sword_B",0),
    ],
    itp_craftable | itp_type_two_handed_wpn | itp_merchandise | itp_two_handed | itp_primary,
    itc_greatsword | itcf_carry_sword_back,
    420,
    weight(4.0) | difficulty(15) | spd_rtng(93) | weapon_length(169) | swing_damage(45, cut) | thrust_damage(28,  pierce),
    imodbits_sword_high
],
# TWO HANDED SWORDS END

# BLUNT WEAPONS START
[
    "hammer_a",
    "Smith's Hammer",
    [
        ("Revised_Hammer_A",0),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_can_knock_down | itp_merchandise | itp_primary | itp_wooden_parry,
    itc_scimitar | itcf_carry_mace_left_hip,
    65,
    weight(1.0) | difficulty(0) | spd_rtng(95) | weapon_length(45) | swing_damage(17, blunt) | thrust_damage(0,  pierce),
    imodbits_mace
],

[
    "mace_a",
    "Knobbed Mace",
    [
        ("Revised_Mace_A",0),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_can_knock_down | itp_merchandise | itp_primary | itp_wooden_parry,
    itc_scimitar | itcf_carry_mace_left_hip,
    177,
    weight(1.5) | difficulty(7) | spd_rtng(99) | weapon_length(65) | swing_damage(21, blunt) | thrust_damage(0,  pierce),
    imodbits_mace
],

[
    "mace_a_v1",
    "Knobbed Mace",
    [
        ("Revised_Mace_A_v1",0),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_can_knock_down | itp_merchandise | itp_primary | itp_wooden_parry,
    itc_scimitar | itcf_carry_mace_left_hip,
    183,
    weight(1.75) | difficulty(8) | spd_rtng(98) | weapon_length(65) | swing_damage(24, blunt) | thrust_damage(0,  pierce),
    imodbits_mace
],

[
    "mace_a_v2",
    "Knobbed Mace",
    [
        ("Revised_Mace_A_v2",0),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_can_knock_down | itp_merchandise | itp_primary | itp_wooden_parry,
    itc_scimitar | itcf_carry_mace_left_hip,
    185,
    weight(1.75) | difficulty(8) | spd_rtng(98) | weapon_length(65) | swing_damage(23, blunt) | thrust_damage(0,  pierce),
    imodbits_mace
],

[
    "mace_a_v3",
    "Knobbed Mace",
    [
        ("Revised_Mace_A_v3",0),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_can_knock_down | itp_merchandise | itp_primary | itp_wooden_parry,
    itc_scimitar | itcf_carry_mace_left_hip,
    187,
    weight(1.75) | difficulty(8) | spd_rtng(98) | weapon_length(65) | swing_damage(24, blunt) | thrust_damage(0,  pierce),
    imodbits_mace
],

[
    "mace_a_v4",
    "Knobbed Mace",
    [
        ("Revised_Mace_A_v4",0),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_can_knock_down | itp_merchandise | itp_primary | itp_wooden_parry,
    itc_scimitar | itcf_carry_mace_left_hip,
    187,
    weight(1.75) | difficulty(8) | spd_rtng(98) | weapon_length(65) | swing_damage(24, blunt) | thrust_damage(0,  pierce),
    imodbits_mace
],

[
    "mace_b",
    "Winged Mace",
    [
        ("Revised_Mace_B",0),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_can_knock_down | itp_merchandise | itp_primary | itp_wooden_parry,
    itc_scimitar | itcf_carry_mace_left_hip,
    191,
    weight(2.0) | difficulty(9) | spd_rtng(99) | weapon_length(55) | swing_damage(27, blunt) | thrust_damage(0,  pierce),
    imodbits_mace
],

[
    "mace_b_v1",
    "Winged Mace",
    [
        ("Revised_Mace_B_v1",0),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_can_knock_down | itp_merchandise | itp_primary | itp_wooden_parry,
    itc_scimitar | itcf_carry_mace_left_hip,
    197,
    weight(2.0) | difficulty(9) | spd_rtng(99) | weapon_length(55) | swing_damage(28, blunt) | thrust_damage(0,  pierce),
    imodbits_mace
],

[
    "mace_b_v2",
    "Winged Mace",
    [
        ("Revised_Mace_B_v2",0),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_can_knock_down | itp_merchandise | itp_primary | itp_wooden_parry,
    itc_scimitar | itcf_carry_mace_left_hip,
    219,
    weight(2.25) | difficulty(10) | spd_rtng(99) | weapon_length(65) | swing_damage(29, blunt) | thrust_damage(0,  pierce),
    imodbits_mace
],

[
    "mace_c",
    "Heavy Winged Mace",
    [
        ("Revised_Mace_C",0),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_can_knock_down | itp_merchandise | itp_primary | itp_wooden_parry,
    itc_scimitar | itcf_carry_mace_left_hip,
    269,
    weight(3.5) | difficulty(11) | spd_rtng(98) | weapon_length(80) | swing_damage(33, blunt) | thrust_damage(0,  pierce),
    imodbits_mace
],

[
    "mace_c_v1",
    "Heavy Winged Mace",
    [
        ("Revised_Mace_C_v1",0),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_can_knock_down | itp_merchandise | itp_primary | itp_wooden_parry,
    itc_scimitar | itcf_carry_mace_left_hip,
    295,
    weight(3.5) | difficulty(12) | spd_rtng(98) | weapon_length(80) | swing_damage(36, blunt) | thrust_damage(0,  pierce),
    imodbits_mace
],
# BLUNT WEAPONS END

# MAULS START
[
    "maul_a",
    "Maul",
    [
        ("Revised_Maul_A",0),
    ],
    itp_craftable | itp_type_two_handed_wpn | itp_merchandise | itp_can_knock_down | itp_primary | itp_two_handed | itp_wooden_parry | itp_wooden_attack | itp_unbalanced,
    itc_nodachi | itcf_carry_spear,
    170,
    weight(4) | difficulty(10) | spd_rtng(85) | weapon_length(65) | swing_damage(30, blunt) | thrust_damage(0,  pierce),
    imodbits_mace
],

[
    "maul_b",
    "Miliatry Hammer",
    [
        ("Revised_Maul_B",0),
    ],
    itp_craftable | itp_type_two_handed_wpn | itp_merchandise | itp_can_knock_down | itp_primary | itp_two_handed | itp_wooden_parry | itp_wooden_attack | itp_unbalanced,
    itc_nodachi | itcf_carry_spear,
    186,
    weight(6) | difficulty(12) | spd_rtng(82) | weapon_length(80) | swing_damage(36, blunt) | thrust_damage(0,  pierce),
    imodbits_mace
],

[
    "maul_b_v1",
    "Miliatry Hammer",
    [
        ("Revised_Maul_B_v1",0),
    ],
    itp_craftable | itp_type_two_handed_wpn | itp_merchandise | itp_can_knock_down | itp_primary | itp_two_handed | itp_wooden_parry | itp_wooden_attack | itp_unbalanced,
    itc_nodachi | itcf_carry_spear,
    190,
    weight(6) | difficulty(12) | spd_rtng(82) | weapon_length(80) | swing_damage(38, blunt) | thrust_damage(0,  pierce),
    imodbits_mace
],
# MAULS END

# PIERCING WEAPONS START
[
    "pickaxe_a",
    "Pickaxe",
    [
        ("Revised_Pickaxe_A",0),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_merchandise | itp_primary | itp_wooden_parry,
    itc_scimitar | itcf_carry_mace_left_hip,
    197,
    weight(1.5) | difficulty(7) | spd_rtng(95) | weapon_length(58) | swing_damage(21, pierce) | thrust_damage(0,  pierce),
    imodbits_mace
],

[
    "pickaxe_a_v1",
    "Great Pickaxe",
    [
        ("Revised_Pickaxe_A_v1",0),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_merchandise | itp_primary | itp_wooden_parry,
    itc_scimitar | itcf_carry_mace_left_hip,
    213,
    weight(1.75) | difficulty(8) | spd_rtng(95) | weapon_length(65) | swing_damage(22, pierce) | thrust_damage(0,  pierce),
    imodbits_mace
],

[
    "military_pick_a",
    "Military Pick",
    [
        ("Revised_Military_Pick_A",0),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_merchandise | itp_primary | itp_wooden_parry,
    itc_scimitar | itcf_carry_mace_left_hip,
    257,
    weight(2.0) | difficulty(8) | spd_rtng(95) | weapon_length(60) | swing_damage(25, pierce) | thrust_damage(0,  pierce),
    imodbits_mace
],

[
    "military_pick_a_v1",
    "Military Pick",
    [
        ("Revised_Military_Pick_A_v1",0),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_merchandise | itp_primary | itp_wooden_parry,
    itc_scimitar | itcf_carry_mace_left_hip,
    263,
    weight(2.5) | difficulty(9) | spd_rtng(95) | weapon_length(60) | swing_damage(27, pierce) | thrust_damage(0,  pierce),
    imodbits_mace
],

[
    "military_pick_a_v2",
    "Military Pick",
    [
        ("Revised_Military_Pick_A_v2",0),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_merchandise | itp_primary | itp_wooden_parry,
    itc_scimitar | itcf_carry_mace_left_hip,
    275,
    weight(2.5) | difficulty(10) | spd_rtng(95) | weapon_length(60) | swing_damage(29, pierce) | thrust_damage(0,  pierce),
    imodbits_mace
],
# PIERCING WEAPONS END

# LIGHT AXES START
[
    "hatchet_a",
    "Hatchet",
    [
        ("Revised_Hatchet_A",0),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_merchandise | itp_primary | itp_secondary | itp_bonus_against_shield | itp_wooden_parry,
    itc_scimitar | itcf_carry_axe_left_hip,
    43,
    weight(2) | difficulty(0) | spd_rtng(97) | weapon_length(45) | swing_damage(23, cut) | thrust_damage(0,  pierce),
    imodbits_axe
],

[
    "hatchet_a_v1",
    "Hatchet with Long Handle",
    [
        ("Revised_Hatchet_A_v1",0),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_merchandise | itp_primary | itp_secondary | itp_bonus_against_shield | itp_wooden_parry,
    itc_scimitar | itcf_carry_axe_left_hip,
    67,
    weight(2.5) | difficulty(0) | spd_rtng(97) | weapon_length(56) | swing_damage(25, cut) | thrust_damage(0,  pierce),
    imodbits_axe
],

[
    "hatchet_b",
    "Hatchet",
    [
        ("Revised_Hatchet_B",0),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_merchandise | itp_primary | itp_secondary | itp_bonus_against_shield | itp_wooden_parry,
    itc_scimitar | itcf_carry_axe_left_hip,
    153,
    weight(2) | difficulty(8) | spd_rtng(99) | weapon_length(45) | swing_damage(26, cut) | thrust_damage(0,  pierce),
    imodbits_axe
],

[
    "hatchet_b_v1",
    "Hatchet with Long Handle",
    [
        ("Revised_Hatchet_B_v1",0),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_merchandise | itp_primary | itp_secondary | itp_bonus_against_shield | itp_wooden_parry,
    itc_scimitar | itcf_carry_axe_left_hip,
    177,
    weight(2.5) | difficulty(9) | spd_rtng(99) | weapon_length(60) | swing_damage(28, cut) | thrust_damage(0,  pierce),
    imodbits_axe
],

[
    "axe_a",
    "Axe",
    [
        ("Revised_Axe_A",0),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_merchandise | itp_primary | itp_secondary | itp_bonus_against_shield | itp_wooden_parry,
    itc_scimitar | itcf_carry_axe_left_hip,
    190,
    weight(2.5) | difficulty(10) | spd_rtng(99) | weapon_length(70) | swing_damage(31, cut) | thrust_damage(0,  pierce),
    imodbits_axe
],

[
    "axe_a_v1",
    "Axe",
    [
        ("Revised_Axe_A_v1",0),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_merchandise | itp_primary | itp_secondary | itp_bonus_against_shield | itp_wooden_parry,
    itc_scimitar | itcf_carry_axe_left_hip,
    191,
    weight(2.5) | difficulty(11) | spd_rtng(99) | weapon_length(70) | swing_damage(33, cut) | thrust_damage(0,  pierce),
    imodbits_axe
],

[
    "axe_a_v2",
    "Axe",
    [
        ("Revised_Axe_A_v2",0),
    ],
    itp_craftable | itp_type_one_handed_wpn | itp_merchandise | itp_primary | itp_secondary | itp_bonus_against_shield | itp_wooden_parry,
    itc_scimitar | itcf_carry_axe_left_hip,
    191,
    weight(2.5) | difficulty(11) | spd_rtng(99) | weapon_length(70) | swing_damage(33, cut) | thrust_damage(0,  pierce),
    imodbits_axe
],
# LIGHT AXES END

# HEAVY AXES START
[
    "heavy_axe_a",
    "Heavy Axe",
    [
        ("Revised_Heavy_Axe_A",0),
    ],
    itp_craftable | itp_type_two_handed_wpn | itp_merchandise | itp_two_handed | itp_primary | itp_bonus_against_shield | itp_wooden_parry,
    itc_nodachi | itcf_carry_axe_back,
    198,
    weight(4) | difficulty(11) | spd_rtng(91) | weapon_length(86) | swing_damage(32, cut) | thrust_damage(0,  pierce),
    imodbits_axe
],

[
    "heavy_war_axe_a",
    "Heavy War Axe",
    [
        ("Revised_Heavy_War_Axe_A",0),
    ],
    itp_craftable | itp_type_two_handed_wpn | itp_merchandise | itp_two_handed | itp_primary | itp_bonus_against_shield | itp_wooden_parry,
    itc_nodachi | itcf_carry_axe_back,
    204,
    weight(3.5) | difficulty(12) | spd_rtng(95) | weapon_length(86) | swing_damage(35, cut) | thrust_damage(0,  pierce),
    imodbits_axe
],

[
    "heavy_war_axe_a_v1",
    "Heavy War Axe",
    [
        ("Revised_Heavy_War_Axe_A_v1",0),
    ],
    itp_craftable | itp_type_two_handed_wpn | itp_merchandise | itp_two_handed | itp_primary | itp_bonus_against_shield | itp_wooden_parry,
    itc_nodachi | itcf_carry_axe_back,
    218,
    weight(3) | difficulty(13) | spd_rtng(98) | weapon_length(86) | swing_damage(35, cut) | thrust_damage(0,  pierce),
    imodbits_axe
],

[
    "heavy_war_axe_b",
    "Heavy War Axe",
    [
        ("Revised_Heavy_War_Axe_B",0),
    ],
    itp_craftable | itp_type_two_handed_wpn | itp_merchandise | itp_two_handed | itp_primary | itp_bonus_against_shield | itp_wooden_parry,
    itc_nodachi | itcf_carry_axe_back,
    210,
    weight(3) | difficulty(13) | spd_rtng(98) | weapon_length(85) | swing_damage(32, cut) | thrust_damage(0,  pierce),
    imodbits_axe
],

[
    "heavy_war_axe_b_v1",
    "Heavy War Axe",
    [
        ("Revised_Heavy_War_Axe_B_v1",0),
    ],
    itp_craftable | itp_type_two_handed_wpn | itp_merchandise | itp_two_handed | itp_primary | itp_bonus_against_shield | itp_wooden_parry,
    itc_nodachi | itcf_carry_axe_back,
    224,
    weight(3) | difficulty(13) | spd_rtng(98) | weapon_length(85) | swing_damage(32, cut) | thrust_damage(0,  pierce),
    imodbits_axe
],

[
    "voulge_a",
    "Voulge",
    [
        ("Revised_Voulge_A",0)
    ],
    itp_craftable | itp_type_two_handed_wpn | itp_merchandise | itp_two_handed | itp_primary | itp_bonus_against_shield | itp_wooden_parry,
    itc_nodachi | itcf_carry_axe_back, 
    129,
    weight(4.5) | difficulty(8) | spd_rtng(87) | weapon_length(119) | swing_damage(30 , cut) | thrust_damage(0 ,  pierce),
    imodbits_axe
],

[
    "bardiche_a",
    "Bardiche",
    [
        ("Revised_Bardiche_A",0)
    ],
    itp_craftable | itp_type_two_handed_wpn | itp_merchandise | itp_two_handed | itp_primary | itp_bonus_against_shield | itp_wooden_parry,
    itc_nodachi | itcf_carry_axe_back,
    198,
    weight(4.25) | difficulty(11) | spd_rtng(95) | weapon_length(100) | swing_damage(32, cut) | thrust_damage(0,  pierce),
    imodbits_axe
],
# HEAVY AXES END

# SPEARS START
[
    "spear_a",
    "Short Spear",
    [
        ("Revised_Spear_A",0),
    ],
    itp_craftable | itp_type_polearm | itp_offset_lance | itp_merchandise | itp_primary | itp_wooden_parry,
    itc_staff | itcf_carry_spear,
    276,
    weight(2.5) | difficulty(8) | spd_rtng(100) | weapon_length(150) | swing_damage(19, blunt) | thrust_damage(25,  pierce),
    imodbits_polearm
],

[
    "spear_a_v1",
    "Short Spear",
    [
        ("Revised_Spear_A_v1",0),
    ],
    itp_craftable | itp_type_polearm | itp_offset_lance | itp_merchandise | itp_primary | itp_wooden_parry,
    itc_staff | itcf_carry_spear,
    283,
    weight(3.0) | difficulty(9) | spd_rtng(100) | weapon_length(150) | swing_damage(22, blunt) | thrust_damage(25,  pierce),
    imodbits_polearm
],

[
    "spear_a_v2",
    "Short Spear",
    [
        ("Revised_Spear_A_v2",0),
    ],
    itp_craftable | itp_type_polearm | itp_offset_lance | itp_merchandise | itp_primary | itp_wooden_parry,
    itc_staff | itcf_carry_spear,
    295,
    weight(3.0) | difficulty(9) | spd_rtng(100) | weapon_length(165) | swing_damage(21, blunt) | thrust_damage(28,  pierce),
    imodbits_polearm
],

[
    "spear_b",
    "Spear",
    [
        ("Revised_Spear_B",0),
    ],
    itp_craftable | itp_type_polearm | itp_offset_lance | itp_merchandise | itp_primary | itp_wooden_parry,
    itc_staff | itcf_carry_spear,
    286,
    weight(2.5) | difficulty(10) | spd_rtng(100) | weapon_length(130) | swing_damage(24, blunt) | thrust_damage(30,  pierce),
    imodbits_polearm
],

[
    "spear_b_v1",
    "Spear",
    [
        ("Revised_Spear_B_v1",0),
    ],
    itp_craftable | itp_type_polearm | itp_offset_lance | itp_merchandise | itp_primary | itp_wooden_parry,
    itc_staff | itcf_carry_spear,
    318,
    weight(3.5) | difficulty(11) | spd_rtng(100) | weapon_length(160) | swing_damage(27, blunt) | thrust_damage(30,  pierce),
    imodbits_polearm
],
# SPEARS END

# LANCES START
# For lances base difficulty is 10 + thrush damage / 3
[
    "lance_a",
    "Lance",
    [
        ("Revised_Lance_A",0)
    ],
    itp_craftable | itp_couchable | itp_type_polearm | itp_merchandise | itp_primary | itp_penalty_with_shield | itp_wooden_parry,
    itc_greatlance,
    312,
    weight(5) | difficulty(16) | spd_rtng(61) | weapon_length(250) | swing_damage(0, cut) | thrust_damage(17,  pierce),
    imodbits_polearm
],

[
    "lance_a_v1",
    "Lance",
    [
        ("Revised_Lance_A_v1",0)
    ],
    itp_craftable | itp_couchable | itp_type_polearm | itp_merchandise | itp_primary | itp_penalty_with_shield | itp_wooden_parry,
    itc_greatlance,
    352,
    weight(5) | difficulty(17) | spd_rtng(55) | weapon_length(275) | swing_damage(0, cut) | thrust_damage(22,  pierce),
    imodbits_polearm
],

[
    "lance_b",
    "Lance",
    [
        ("Revised_Lance_B",0)
    ],
    itp_craftable | itp_couchable | itp_type_polearm | itp_merchandise | itp_primary | itp_penalty_with_shield | itp_wooden_parry,
    itc_greatlance,
    299,
    weight(5) | difficulty(18) | spd_rtng(66) | weapon_length(185) | swing_damage(0, cut) | thrust_damage(24,  pierce),
    imodbits_polearm
],

[
    "lance_b_v1",
    "Lance",
    [
        ("Revised_Lance_B_v1",0)
    ],
    itp_craftable | itp_couchable | itp_type_polearm | itp_merchandise | itp_primary | itp_penalty_with_shield | itp_wooden_parry,
    itc_greatlance,
    339,
    weight(5) | difficulty(17) | spd_rtng(66) | weapon_length(185) | swing_damage(0, cut) | thrust_damage(22,  pierce),
    imodbits_polearm
],

[
    "lance_b_v2",
    "Lance",
    [
        ("Revised_Lance_B_v2",0)
    ],
    itp_craftable | itp_couchable | itp_type_polearm | itp_merchandise | itp_primary | itp_penalty_with_shield | itp_wooden_parry,
    itc_greatlance,
    389,
    weight(5) | difficulty(18) | spd_rtng(66) | weapon_length(190) | swing_damage(0, cut) | thrust_damage(25,  pierce),
    imodbits_polearm
],

[
    "lance_b_v3",
    "Lance",
    [
        ("Revised_Lance_B_v3",0)
    ],
    itp_craftable | itp_couchable | itp_type_polearm | itp_merchandise | itp_primary | itp_penalty_with_shield | itp_wooden_parry,
    itc_greatlance,
    399,
    weight(5) | difficulty(18) | spd_rtng(66) | weapon_length(190) | swing_damage(0, cut) | thrust_damage(25,  pierce),
    imodbits_polearm
],
# LANCES END

# POLEHAMMERS START
# + 125 base price value for polehammers
[
    "polehammer_a",
    "Light Pierce Polehammer",
    [
        ("Revised_Polehammer_A",0)
    ],
    itp_craftable | itp_type_polearm | itp_merchandise | itp_cant_use_on_horseback | itp_primary | itp_penalty_with_shield | itp_wooden_parry | itp_two_handed,
    itc_cutting_spear | itcf_carry_spear,
    429,
    weight(3.0) | difficulty(12) | spd_rtng(91) | weapon_length(160) | swing_damage(35, pierce) | thrust_damage(30, pierce),
    imodbits_polearm
],

[
    "polehammer_b",
    "Simple Polehammer",
    [
        ("Revised_Polehammer_B",0)
    ],
    itp_craftable | itp_type_polearm | itp_merchandise | itp_cant_use_on_horseback | itp_primary | itp_penalty_with_shield | itp_wooden_parry | itp_two_handed,
    itc_cutting_spear | itcf_carry_spear,
    406,
    weight(3.0) | difficulty(11) | spd_rtng(91) | weapon_length(140) | swing_damage(32, blunt) | thrust_damage(29, pierce),
    imodbits_polearm
],

[
    "polehammer_c",
    "Military Polehammer",
    [
        ("Revised_Polehammer_C",0)
    ],
    itp_craftable | itp_type_polearm | itp_merchandise | itp_cant_use_on_horseback | itp_primary | itp_penalty_with_shield | itp_wooden_parry | itp_two_handed,
    itc_cutting_spear | itcf_carry_spear,
    414,
    weight(3.5) | difficulty(12) | spd_rtng(91) | weapon_length(145) | swing_damage(35, blunt) | thrust_damage(30, pierce),
    imodbits_polearm
],

[
    "polehammer_c_v1",
    "Military Polehammer",
    [
        ("Revised_Polehammer_C_v1",0)
    ],
    itp_craftable | itp_type_polearm | itp_merchandise | itp_cant_use_on_horseback | itp_primary | itp_penalty_with_shield | itp_wooden_parry | itp_two_handed,
    itc_cutting_spear | itcf_carry_spear,
    428,
    weight(3.5) | difficulty(12) | spd_rtng(91) | weapon_length(145) | swing_damage(35, blunt) | thrust_damage(30, pierce),
    imodbits_polearm
],

[
    "polehammer_d",
    "Militia Polehammer",
    [
        ("Revised_Polehammer_D",0)
    ],
    itp_craftable | itp_type_polearm | itp_merchandise | itp_cant_use_on_horseback | itp_primary | itp_penalty_with_shield | itp_wooden_parry | itp_two_handed,
    itc_cutting_spear | itcf_carry_spear,
    394,
    weight(2.5) | difficulty(10) | spd_rtng(94) | weapon_length(140) | swing_damage(28, blunt) | thrust_damage(21, blunt),
    imodbits_polearm
],
# POLEHAMMERS END

# POLEAXES START
# + 100 base price value for poleaxes
[
    "poleaxe_a",
    "Footman Poleaxe",
    [
        ("Revised_Poleaxe_A",0)
    ],
    itp_craftable | itp_type_polearm | itp_offset_lance | itp_merchandise | itp_primary | itp_two_handed | itp_wooden_parry,
    itc_staff | itcf_carry_spear,
    381,
    weight(4.5) | difficulty(14) | spd_rtng(85) | weapon_length(125) | swing_damage(42, cut) | thrust_damage(15, blunt),
    imodbits_polearm
],

[
    "poleaxe_b",
    "Military Poleaxe",
    [
        ("Revised_Poleaxe_B",0)
    ],
    itp_craftable | itp_type_polearm | itp_offset_lance | itp_merchandise | itp_primary | itp_two_handed | itp_wooden_parry,
    itc_staff | itcf_carry_spear,
    436,
    weight(5) | difficulty(15) | spd_rtng(85) | weapon_length(150) | swing_damage(42, cut) | thrust_damage(21, pierce),
    imodbits_polearm
],

[
    "poleaxe_c",
    "Military Poleaxe",
    [
        ("Revised_Poleaxe_C",0)
    ],
    itp_craftable | itp_type_polearm | itp_offset_lance | itp_merchandise | itp_primary | itp_two_handed | itp_wooden_parry,
    itc_staff | itcf_carry_spear,
    482,
    weight(5) | difficulty(16) | spd_rtng(85) | weapon_length(160) | swing_damage(44, cut) | thrust_damage(27, pierce),
    imodbits_polearm
],
# POLEAXES END

# POLEARMS START
[
    "polearm_military_scythe_a",
    "Military Scythe",
    [
        ("Revised_Polearm_A",0),
    ],
    itp_craftable | itp_type_polearm | itp_offset_lance | itp_merchandise | itp_primary | itp_penalty_with_shield | itp_wooden_parry,
    itc_staff | itcf_carry_spear,
    285,
    weight(2.5)|difficulty(10)|spd_rtng(95) | weapon_length(155)|swing_damage(30 , cut) | thrust_damage(15 ,  pierce),
    imodbits_polearm
],

[
    "polearm_glaive_a",
    "Glaive",
    [
        ("Revised_Polearm_B",0),
    ],
    itp_craftable | itp_type_polearm | itp_offset_lance | itp_merchandise | itp_primary | itp_penalty_with_shield | itp_wooden_parry,
    itc_staff | itcf_carry_spear,
    288,
    weight(3.0)|difficulty(11)|spd_rtng(95) | weapon_length(155)|swing_damage(32 , cut) | thrust_damage(19 ,  pierce),
    imodbits_polearm
],

[
    "polearm_military_glave_a",
    "Military Glaive",
    [
        ("Revised_Polearm_C",0),
    ],
    itp_craftable | itp_type_polearm | itp_offset_lance | itp_merchandise | itp_primary | itp_penalty_with_shield | itp_wooden_parry,
    itc_staff | itcf_carry_spear,
    293,
    weight(3.5)|difficulty(11)|spd_rtng(93) | weapon_length(165)|swing_damage(33 , cut) | thrust_damage(21 ,  pierce),
    imodbits_polearm
],

[
    "polearm_light_halberd_a",
    "Light Halberd",
    [
        ("Revised_Polearm_D",0),
    ],
    itp_craftable | itp_type_polearm | itp_offset_lance | itp_merchandise | itp_primary | itp_penalty_with_shield | itp_wooden_parry,
    itc_staff | itcf_carry_spear,
    295,
    weight(3.0)|difficulty(11)|spd_rtng(95) | weapon_length(158)|swing_damage(34 , cut) | thrust_damage(23 ,  pierce),
    imodbits_polearm
],

[
    "polearm_light_voulge_a",
    "Light Voulge",
    [
        ("Revised_Polearm_E",0),
    ],
    itp_craftable | itp_type_polearm | itp_offset_lance | itp_merchandise | itp_primary | itp_penalty_with_shield | itp_wooden_parry,
    itc_staff | itcf_carry_spear,
    298,
    weight(2.5)|difficulty(11)|spd_rtng(96) | weapon_length(170)|swing_damage(30 , cut) | thrust_damage(23 ,  pierce),
    imodbits_polearm
],

[
    "polearm_light_voulge_b",
    "Light Voulge",
    [
        ("Revised_Polearm_F",0),
    ],
    itp_craftable | itp_type_polearm | itp_offset_lance | itp_merchandise | itp_primary | itp_penalty_with_shield | itp_wooden_parry,
    itc_staff | itcf_carry_spear,
    321,
    weight(2.25)|difficulty(11)|spd_rtng(98) | weapon_length(170)|swing_damage(30 , cut) | thrust_damage(23 ,  pierce),
    imodbits_polearm
],

[
    "polearm_saxon_voulge_a",
    "Voulge",
    [
        ("Revised_Voulge_B",0),
    ],
    itp_craftable | itp_type_polearm | itp_offset_lance | itp_merchandise | itp_primary | itp_penalty_with_shield | itp_wooden_parry,
    itc_staff | itcf_carry_spear,
    301,
    weight(3.5)|difficulty(11)|spd_rtng(92) | weapon_length(160)|swing_damage(33 , cut) | thrust_damage(23 ,  pierce),
    imodbits_polearm
],

[
    "polearm_saxon_voulge_a_v1",
    "Voulge",
    [
        ("Revised_Voulge_B_v1",0),
    ],
    itp_craftable | itp_type_polearm | itp_offset_lance | itp_merchandise | itp_primary | itp_penalty_with_shield | itp_wooden_parry,
    itc_staff | itcf_carry_spear,
    316,
    weight(3.5)|difficulty(11)|spd_rtng(98) | weapon_length(160)|swing_damage(35 , cut) | thrust_damage(26 ,  pierce),
    imodbits_polearm
],

[
    "polearm_voulge_a",
    "Long Voulge",
    [
        ("Revised_Voulge_C",0),
    ],
    itp_craftable | itp_type_polearm | itp_offset_lance | itp_merchandise | itp_primary | itp_penalty_with_shield | itp_wooden_parry,
    itc_staff | itcf_carry_spear,
    319,
    weight(4.0)|difficulty(11)|spd_rtng(92) | weapon_length(180)|swing_damage(32 , cut) | thrust_damage(26 ,  pierce),
    imodbits_polearm
],

[
    "polearm_voulge_b",
    "Long Voulge",
    [
        ("Revised_Voulge_D",0),
    ],
    itp_craftable | itp_type_polearm | itp_offset_lance | itp_merchandise | itp_primary | itp_penalty_with_shield | itp_wooden_parry,
    itc_staff | itcf_carry_spear,
    293,
    weight(4.0)|difficulty(11)|spd_rtng(92) | weapon_length(160)|swing_damage(32 , cut) | thrust_damage(20, blunt),
    imodbits_polearm
],

[
    "polearm_voulge_c",
    "Long Voulge",
    [
        ("Revised_Voulge_E",0),
    ],
    itp_craftable | itp_type_polearm | itp_offset_lance | itp_merchandise | itp_primary | itp_penalty_with_shield | itp_wooden_parry,
    itc_staff | itcf_carry_spear,
    304,
    weight(4.0)|difficulty(11)|spd_rtng(96) | weapon_length(160)|swing_damage(33 , cut) | thrust_damage(26 ,  pierce),
    imodbits_polearm
],
# POLEARMS END

# HAFTED WEAPONS START
[
    "long_pole_mace_a", "Long Spiked Club",
    [("Revised_Hafted_A",0)],
    itp_type_polearm | itp_can_knock_down | itp_merchandise | itp_primary | itp_wooden_parry,
    itc_staff | itcf_carry_axe_back,
    217, # Price is 317 but - 100 for cheap materials
    weight(3) | difficulty(9) | spd_rtng(94) | weapon_length(120) | swing_damage(25 , pierce) | thrust_damage(15 ,  blunt),
    imodbits_mace
],

[
    "long_pole_mace_b", "Long Hafed Spiked Mace",
    [("Revised_Hafted_B",0)],
    itp_type_polearm | itp_can_knock_down | itp_merchandise | itp_primary | itp_wooden_parry,
    itc_staff | itcf_carry_axe_back,
    337,
    weight(3.5) | difficulty(10) | spd_rtng(92) | weapon_length(139) | swing_damage(28 , pierce) | thrust_damage(18 ,  blunt),
    imodbits_mace
],
# HAFTED WEAPONS END
# WEAPONS END

# SHIELDS START
[
    "oval_shield_heraldic_a",
    "Oval Shield",
    [
        ("shields_archer_tripoli_b", 0),
    ], 
    itp_type_shield|itp_merchandise|itp_wooden_parry,
    itcf_carry_round_shield,
    70,
    weight(2)|abundance(100)|body_armor(1)|hit_points(165)|spd_rtng(100)|shield_width(36),
    imodbit_reinforced,
    [
        (
            ti_on_init_item, 
            [
                (store_trigger_param_1, ":agent_no"),
                (store_trigger_param_2, ":troop_no"),
                (call_script, "script_shield_item_set_banner", "tableau_oval_shield_a", ":agent_no", ":troop_no")
            ]
        )
    ],
    [fac_kingdom_1]
],

[
    "otto_shield_heraldic_a",
    "Shield",
    [
        ("tableau_shield_otto1", 0),
    ], 
    itp_type_shield|itp_merchandise|itp_wooden_parry,
    itcf_carry_round_shield,
    170,
    weight(2)|abundance(100)|body_armor(5)|hit_points(250)|spd_rtng(100)|shield_width(40)|shield_height(55),
    imodbit_reinforced,
    [
        (
            ti_on_init_item, 
            [
                (store_trigger_param_1, ":agent_no"),
                (store_trigger_param_2, ":troop_no"),
                (call_script, "script_shield_item_set_banner", "tableau_otto_shield_a", ":agent_no", ":troop_no")
            ]
        )
    ],
    []
],

[
    "otto_shield_heraldic_a_v1",
    "Shield",
    [
        ("tableau_shield_otto2", 0),
    ], 
    itp_type_shield|itp_merchandise|itp_wooden_parry,
    itcf_carry_round_shield,
    270,
    weight(2)|abundance(100)|body_armor(12)|hit_points(457)|spd_rtng(100)|shield_width(40)|shield_height(55),
    imodbit_reinforced,
    [
        (
            ti_on_init_item, 
            [
                (store_trigger_param_1, ":agent_no"),
                (store_trigger_param_2, ":troop_no"),
                (call_script, "script_shield_item_set_banner", "tableau_otto_shield_b", ":agent_no", ":troop_no")
            ]
        )
    ],
    []
],

[
    "infantry_shield_heraldic_a",
    "Shield",
    [
        ("Shield_Middle_Empire_Infantry_A1_01", 0),
    ], 
    itp_type_shield|itp_merchandise|itp_wooden_parry,
    itcf_carry_round_shield,
    270,
    weight(2)|abundance(100)|body_armor(7)|hit_points(566)|spd_rtng(90)|shield_width(43)|shield_height(67),
    imodbit_reinforced,
    [], []
],

[
    "infantry_shield_heraldic_a_v1",
    "Shield",
    [
        ("Shield_Middle_Empire_Infantry_A2_01", 0),
    ], 
    itp_type_shield|itp_merchandise|itp_wooden_parry,
    itcf_carry_round_shield,
    270,
    weight(2)|abundance(100)|body_armor(7)|hit_points(566)|spd_rtng(90)|shield_width(43)|shield_height(67),
    imodbit_reinforced,
    [], []
],

[
    "infantry_shield_heraldic_a_v2",
    "Shield",
    [
        ("Shield_Middle_Empire_Infantry_A3_01", 0),
    ], 
    itp_type_shield|itp_merchandise|itp_wooden_parry,
    itcf_carry_round_shield,
    270,
    weight(2)|abundance(100)|body_armor(7)|hit_points(566)|spd_rtng(90)|shield_width(43)|shield_height(67),
    imodbit_reinforced,
    [], []
],

[
    "infantry_shield_heraldic_a_v3",
    "Shield",
    [
        ("Shield_Middle_Empire_Infantry_A4_01", 0),
    ], 
    itp_type_shield|itp_merchandise|itp_wooden_parry,
    itcf_carry_round_shield,
    270,
    weight(2)|abundance(100)|body_armor(7)|hit_points(566)|spd_rtng(90)|shield_width(43)|shield_height(67),
    imodbit_reinforced,
    [], []
],

[
    "infantry_shield_heraldic_a_v4",
    "Shield",
    [
        ("Shield_Middle_Empire_Infantry_A5_01", 0),
    ], 
    itp_type_shield|itp_merchandise|itp_wooden_parry,
    itcf_carry_round_shield,
    270,
    weight(2)|abundance(100)|body_armor(7)|hit_points(566)|spd_rtng(90)|shield_width(43)|shield_height(67),
    imodbit_reinforced,
    [], []
],
# SHIELDS END

["turret_hat_ruby", "Turret Hat", [("turret_hat_r",0)], itp_type_head_armor  |itp_civilian|itp_fit_to_head ,0, 70 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ], 
["turret_hat_blue", "Turret Hat", [("turret_hat_b",0)], itp_type_head_armor  |itp_civilian|itp_fit_to_head ,0, 80 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ], 
["turret_hat_green", "Barbette", [("barbette_new",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_fit_to_head,0,70, weight(0.5)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["court_hat", "Turret Hat", [("court_hat",0)], itp_type_head_armor  |itp_civilian|itp_fit_to_head ,0, 80 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ], 
["wimple_a", "Wimple", [("wimple_a_new",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_fit_to_head,0,10, weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["wimple_with_veil", "Wimple with Veil", [("wimple_b_new",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_fit_to_head,0,10, weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],

["headcloth", "Headcloth", [("headcloth_a_new",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["steppe_cap", "Steppe Cap", [("steppe_cap_a_new",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 14 , weight(1)|abundance(100)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["woolen_cap", "Woolen Cap", [("woolen_cap_new",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 2 , weight(1)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["female_hood", "Lady's Hood", [("ladys_hood_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 9 , weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["leather_steppe_cap_a", "Steppe Cap", [("Leather_Cap_A",0),("Leather_Cap_A.1",0),("Leather_Cap_A_inv",ixmesh_inventory),("Leather_Cap_A_inv.1",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature   ,0,
24 , weight(1)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["leather_steppe_cap_b", "Steppe Cap ", [("tattered_steppe_cap_b_new",0)], itp_merchandise|itp_type_head_armor   ,0, 
36 , weight(1)|abundance(100)|head_armor(16)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["leather_steppe_cap_c", "Steppe Cap", [("steppe_cap_a_new",0)], itp_merchandise|itp_type_head_armor   ,0, 51 , weight(1)|abundance(100)|head_armor(16)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["mail_coif", "Mail Coif", [("crusader_koif_a",0)], itp_merchandise| itp_type_head_armor   ,0, 71 , weight(1.25)|abundance(100)|head_armor(22)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_armor ],

["khergit_lady_hat", "Eastern Lady Hat", [("khergit_lady_hat",0)],  itp_type_head_armor   |itp_civilian |itp_doesnt_cover_hair | itp_fit_to_head,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["khergit_lady_hat_b", "Eastern Lady Leather Hat", [("khergit_lady_hat_b",0)], itp_type_head_armor  | itp_doesnt_cover_hair | itp_fit_to_head  |itp_civilian ,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["m_bascinet_a", "Bascinet", [("Revised_Bascinet_B",0),("Revised_Bascinet_B_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 559, weight(2)|abundance(100)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_3] ],
["m_bascinet_b", "Visored Bascinet", [("Revised_Bascinet_A",0),("Revised_Bascinet_A_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 659, weight(2.5)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_3] ],

["great_helmet_heretics", "Great Helmet", [("Heretics_Helmet_A",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0, 995 , weight(2.75)|abundance(100)|head_armor(54)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_plate ],
["great_helmet", "Great Helmet", [("Heretics_Helmet_A",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0, 980 , weight(2.75)|abundance(100)|head_armor(53)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["winged_great_helmet", "Decorated Great Helmet", [("Heretics_Helmet_A",0)], itp_merchandise|itp_type_head_armor|itp_covers_head,0, 1240 , weight(2.75)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],

#WEAPONS
["wooden_stick",         "Wooden Stick", [("wooden_stick",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar, 
4 , weight(2.5)|difficulty(0)|spd_rtng(99) | weapon_length(63)|swing_damage(13 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
["cudgel",         "Cudgel", [("club_v3",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar, 
4 , weight(2.5)|difficulty(0)|spd_rtng(99) | weapon_length(70)|swing_damage(13 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
["hammer",         "Hammer", [("luc_great_hammer_c",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar, 
7 , weight(2)|difficulty(0)|spd_rtng(100) | weapon_length(55)|swing_damage(24 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["club",         "Club", [("club_v3",0)], itp_type_one_handed_wpn|itp_merchandise| itp_can_knock_down|itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar, 
11 , weight(2.5)|difficulty(0)|spd_rtng(98) | weapon_length(70)|swing_damage(20 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
["studded_club", "Studded Club", [("luc_studded_club",0)], itp_type_one_handed_wpn|itp_merchandise| itp_can_knock_down|itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar, 115 , weight(2.5)|difficulty(0)|spd_rtng(98) | weapon_length(80)|swing_damage(26 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],

["winged_mace", "Flanged Mace", [("luc_english_mace_1415",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
122 , weight(3.5)|difficulty(0)|spd_rtng(103) | weapon_length(70)|swing_damage(24 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["strange_winged_mace", "Strange Winged Mace", [("luc_winged_mace_zc",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 259 , weight(3.5)|difficulty(0)|spd_rtng(103) | weapon_length(70)|swing_damage(30 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["strange_winged_mace_decorated", "Decorated Strange Winged Mace", [("luc_winged_mace_zb",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 315 , weight(3.5)|difficulty(0)|spd_rtng(103) | weapon_length(70)|swing_damage(30 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["royal_winged_mace_decorated", "Decorated Royal Winged Mace", [("luc_bronze_mace",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 315 , weight(3.5)|difficulty(0)|spd_rtng(99) | weapon_length(78)|swing_damage(33 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["royal_mace_decorated", "Decorated Royal Mace", [("luc_maciejowski_mace",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 289 , weight(3.0)|difficulty(0)|spd_rtng(99) | weapon_length(70)|swing_damage(29 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],

["flanged_mace", "Flanged Mace", [("luc_english_mace_15th",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
131 , weight(3.5)|difficulty(0)|spd_rtng(99) | weapon_length(70)|swing_damage(25 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["heavy_mace_a", "Heavy Mace", [("luc_khergit_heavy_mace",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
144 , weight(3.5)|difficulty(0)|spd_rtng(99) | weapon_length(75)|swing_damage(28 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["metal_flanged_mace",         "Metal Flanged Mace", [("luc_vaegir_flanged_mace",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
198 , weight(4.0)|difficulty(0)|spd_rtng(95) | weapon_length(78)|swing_damage(29 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["spiked_mace",         "Spiked Mace", [("spiked_mace_new",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
180 , weight(3.5)|difficulty(0)|spd_rtng(98) | weapon_length(70)|swing_damage(28 , blunt) | thrust_damage(0 ,  pierce),imodbits_pick ],
["military_hammer", "Military Hammer", [("military_hammer",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
317 , weight(2)|difficulty(0)|spd_rtng(95) | weapon_length(70)|swing_damage(31 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["maul",         "Maul", [("maul_b",0)], itp_crush_through|itp_craftable|itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down |itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear, 
97 , weight(6)|difficulty(11)|spd_rtng(83) | weapon_length(79)|swing_damage(36 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["sledgehammer", "Sledgehammer", [("luc_greathammer_z1",0)], itp_crush_through|itp_craftable|itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear, 
101 , weight(7)|difficulty(12)|spd_rtng(81) | weapon_length(82)|swing_damage(39, blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["warhammer",         "Great Hammer", [("luc_great_hammer_a",0)], itp_crush_through|itp_craftable|itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear, 
290 , weight(9)|difficulty(14)|spd_rtng(79) | weapon_length(75)|swing_damage(45 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["warhammer_b",         "Great Hammer", [("luc_great_hammer_b",0)], itp_crush_through|itp_craftable|itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear, 290 , weight(9)|difficulty(14)|spd_rtng(79) | weapon_length(75)|swing_damage(45 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["spiked_club",         "Spiked Club", [("luc_spiked_club",0)], itp_craftable|itp_type_one_handed_wpn|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
83 , weight(3)|difficulty(0)|spd_rtng(97) | weapon_length(70)|swing_damage(21 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],
["fighting_pick", "Fighting Pick", [("fighting_pick_new",0)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
108 , weight(1.0)|difficulty(0)|spd_rtng(98) | weapon_length(70)|swing_damage(22 , pierce) | thrust_damage(0 ,  pierce),imodbits_pick ],
["military_pick", "Military Pick", [("luc_horseman_pick",0)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
280 , weight(1.5)|difficulty(0)|spd_rtng(97) | weapon_length(70)|swing_damage(31 , pierce) | thrust_damage(0 ,  pierce),imodbits_pick ],
["morningstar",         "Morningstar", [("luc_morningstar_new",0)], itp_crush_through|itp_craftable|itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry|itp_unbalanced, itc_morningstar|itcf_carry_mace_left_hip, 
305 , weight(4.5)|difficulty(13)|spd_rtng(95) | weapon_length(85)|swing_damage(38 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],


["sickle",         "Sickle", [("sickle",0)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry|itp_wooden_parry, itc_cleaver, 
9 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(40)|swing_damage(20 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["cleaver",         "Cleaver", [("cleaver_new",0)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry|itp_wooden_parry, itc_cleaver, 
14 , weight(1.5)|difficulty(0)|spd_rtng(103) | weapon_length(35)|swing_damage(24 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["knife",         "Knife", [("peasant_knife_new",0)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left, 
18 , weight(0.5)|difficulty(0)|spd_rtng(110) | weapon_length(40)|swing_damage(21 , cut) | thrust_damage(13 ,  pierce),imodbits_sword ],
["butchering_knife", "Butchering Knife", [("khyber_knife_new",0)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_right, 
23 , weight(0.75)|difficulty(0)|spd_rtng(108) | weapon_length(60)|swing_damage(24 , cut) | thrust_damage(17 ,  pierce),imodbits_sword ],
["dagger",         "Dagger", [("dagger_b",0),("dagger_b_scabbard",ixmesh_carry),("dagger_b",imodbits_good),("dagger_b_scabbard",ixmesh_carry|imodbits_good)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn, 
37 , weight(0.75)|difficulty(0)|spd_rtng(109) | weapon_length(47)|swing_damage(22 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high ],

["scimitar",         "Scimitar", [("scimitar_a",0),("scab_scimeter_a", ixmesh_carry)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(1.5)|difficulty(0)|spd_rtng(101) | weapon_length(97)|swing_damage(30 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],
["scimitar_b",         "Elite Scimitar", [("scimitar_b",0),("scab_scimeter_b", ixmesh_carry)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
290 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(103)|swing_damage(32 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],

["arabian_sword_a",         "Solarian Sword", [("saracin_sword_a",0),("scab_saracin_sword_a", ixmesh_carry)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 108 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(97)|swing_damage(26 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high ],
["arabian_sword_b",         "Solarian Arming Sword", [("saracin_sword_b",0),("scab_saracin_sword_b", ixmesh_carry)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 218 , weight(1.7)|difficulty(0)|spd_rtng(99) | weapon_length(97)|swing_damage(28 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high ],
["sarranid_cavalry_sword",         "Solarian Cavalry Sword", [("saracin_sword_d",0),("scab_saracin_sword_d", ixmesh_carry)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 310 , weight(1.5)|difficulty(0)|spd_rtng(98) | weapon_length(103)|swing_damage(28 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high ],
["arabian_sword_d",         "Solarian Guard Sword", [("saracin_sword_c",0),("scab_saracin_sword_c", ixmesh_carry)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,  420 , weight(1.7)|difficulty(0)|spd_rtng(99) | weapon_length(103)|swing_damage(30 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ],
["arabian_sword_c", "Solarian Guard Sword", [("saracin_sword_e",0),("scab_saracin_sword_e", ixmesh_carry)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 460 , weight(1.7)|difficulty(0)|spd_rtng(99) | weapon_length(103)|swing_damage(32 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ],

["fighting_axe", "Fighting Axe", [("luc_burgundian_axe",0)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
77 , weight(2.5)|difficulty(9)|spd_rtng(92) | weapon_length(90)|swing_damage(31 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["heavy_infantry_axe", "Heavy Infantry Axe", [("luc_german_horseman_axe",0)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
179 , weight(2.5)|difficulty(9)|spd_rtng(95) | weapon_length(80)|swing_damage(32 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["axe", "Axe", [("luc_executioners_axe",0)], itp_craftable|itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 
65 , weight(4)|difficulty(8)|spd_rtng(91) | weapon_length(108)|swing_damage(32 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["battle_axe", "Battle Axe", [("luc_battle_axe",0)], itp_craftable|itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 
240 , weight(5)|difficulty(9)|spd_rtng(88) | weapon_length(108)|swing_damage(41 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["war_axe", "War Axe", [("luc_war_axe",0)], itp_craftable|itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 
264 , weight(5)|difficulty(10)|spd_rtng(86) | weapon_length(110)|swing_damage(43 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["khergit_sword_two_handed_a",         "Two Handed Sabre", [("khergit_sword_two_handed_a",0)], itp_craftable|itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back,
 523 , weight(2.75)|difficulty(10)|spd_rtng(96) | weapon_length(120)|swing_damage(40 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],
["khergit_sword_two_handed_b",         "Two Handed Sabre", [("khergit_sword_two_handed_b",0)], itp_craftable|itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back,
 920 , weight(2.75)|difficulty(10)|spd_rtng(96) | weapon_length(120)|swing_damage(44 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],

["two_handed_cleaver", "War Cleaver", [("military_cleaver_a",0)], itp_craftable|itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back,
 640 , weight(2.75)|difficulty(10)|spd_rtng(93) | weapon_length(120)|swing_damage(45 , cut) | thrust_damage(0 ,  cut),imodbits_sword_high ],
["military_cleaver_b", "Soldier's Cleaver", [("military_cleaver_b",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip,
 193 , weight(1.5)|difficulty(0)|spd_rtng(96) | weapon_length(95)|swing_damage(31 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],
["military_cleaver_c", "Military Cleaver", [("military_cleaver_c",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip,
 263 , weight(1.5)|difficulty(0)|spd_rtng(96) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],

["military_sickle_a", "Military Sickle", [("military_sickle_a",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 220 , weight(1.0)|difficulty(9)|spd_rtng(100) | weapon_length(75)|swing_damage(26 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe ],

["bastard_sword_a", "Bastard Sword", [("bastard_sword_a",0),("bastard_sword_a_scabbard", ixmesh_carry)], itp_craftable|itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 294 , weight(2.0)|difficulty(9)|spd_rtng(98) | weapon_length(101)|swing_damage(35 , cut) | thrust_damage(26 ,  pierce),imodbits_sword_high ],
["bastard_sword_b", "Heavy Bastard Sword", [("bastard_sword_b",0),("bastard_sword_b_scabbard", ixmesh_carry)], itp_craftable|itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 526 , weight(2.25)|difficulty(9)|spd_rtng(97) | weapon_length(105)|swing_damage(37 , cut) | thrust_damage(27 ,  pierce),imodbits_sword_high ],

["axe_crusader_a","Knight War Axe", [("axe_crusader_a", 0)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_bonus_against_shield, itcf_carry_axe_left_hip|itc_scimitar,550, weight(2)|abundance(100)|difficulty(9)|spd_rtng(95)|weapon_length(80)|thrust_damage(0, pierce)|swing_damage(36, cut), imodbits_none, [], [fac_kingdom_1]],
["axe_crusader_b","Knight War Axe", [("axe_crusader_b", 0)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_bonus_against_shield, itcf_carry_axe_left_hip|itc_scimitar,650, weight(2)|abundance(100)|difficulty(9)|spd_rtng(98)|weapon_length(73)|thrust_damage(0, pierce)|swing_damage(34, cut), imodbits_none, [], [fac_kingdom_1]],
["axe_crusader_c","Knight War Axe", [("axe_crusader_c", 0)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_bonus_against_shield, itcf_carry_axe_left_hip|itc_scimitar,750, weight(2)|abundance(100)|difficulty(9)|spd_rtng(90)|weapon_length(85)|thrust_damage(0, pierce)|swing_damage(38, cut), imodbits_none, [], [fac_kingdom_1]],
["axe_crusader_d","Knight War Axe", [("axe_crusader_d", 0)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_bonus_against_shield|itp_crush_through|itp_can_knock_down, itcf_carry_axe_left_hip|itc_scimitar,850, weight(4.75)|abundance(100)|difficulty(9)|spd_rtng(90)|weapon_length(90)|thrust_damage(0, pierce)|swing_damage(44, cut), imodbits_none, [], [fac_kingdom_1]],
["axe_crusader_1","Knight War Axe", [("axe_crusader_1", 0)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_bonus_against_shield|itp_crush_through|itp_can_knock_down, itcf_carry_axe_left_hip|itc_scimitar,1000, weight(4.25)|abundance(100)|difficulty(9)|spd_rtng(88)|weapon_length(88)|thrust_damage(0, pierce)|swing_damage(48, cut), imodbits_none, [], [fac_kingdom_1]],

["one_handed_war_axe_a", "One Handed Axe", [("one_handed_war_axe_a",0)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 87 , weight(1.5)|difficulty(9)|spd_rtng(98) | weapon_length(71)|swing_damage(32 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["one_handed_battle_axe_a", "One Handed Battle Axe", [("one_handed_battle_axe_a",0)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 142 , weight(1.5)|difficulty(9)|spd_rtng(98) | weapon_length(73)|swing_damage(34 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["one_handed_war_axe_b", "One Handed War Axe", [("one_handed_war_axe_b",0)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 190 , weight(1.5)|difficulty(9)|spd_rtng(98) | weapon_length(76)|swing_damage(34 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["one_handed_battle_axe_b", "One Handed Battle Axe", [("one_handed_battle_axe_b",0)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 230 , weight(1.75)|difficulty(9)|spd_rtng(98) | weapon_length(72)|swing_damage(36 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["one_handed_battle_axe_c", "One Handed Battle Axe", [("one_handed_battle_axe_c",0)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 550 , weight(2.0)|difficulty(9)|spd_rtng(98) | weapon_length(76)|swing_damage(37 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["two_handed_axe",         "Two Handed Axe", [("two_handed_battle_axe_a",0)], itp_craftable|itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 90 , weight(4.5)|difficulty(10)|spd_rtng(96) | weapon_length(90)|swing_damage(38 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["two_handed_battle_axe_2",         "Two Handed War Axe", [("two_handed_battle_axe_b",0)], itp_craftable|itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 152 , weight(4.5)|difficulty(10)|spd_rtng(96) | weapon_length(92)|swing_damage(44 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["shortened_voulge",         "Shortened Voulge", [("two_handed_battle_axe_c",0)], itp_craftable|itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 228 , weight(4.5)|difficulty(10)|spd_rtng(92) | weapon_length(100)|swing_damage(45 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["great_axe",         "Great Axe", [("two_handed_battle_axe_e",0)], itp_craftable|itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 316 , weight(4.5)|difficulty(10)|spd_rtng(94) | weapon_length(96)|swing_damage(47 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["long_axe",         "Long Axe", [("long_axe_a",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_next_item_as_melee|itp_unbalanced|itp_merchandise,itc_staff|itcf_carry_axe_back,
 390 , weight(4.75)|difficulty(10)|spd_rtng(93) | weapon_length(120)|swing_damage(46 , cut) | thrust_damage(19 ,  blunt),imodbits_axe ],
["long_axe_alt",         "Long Axe", [("long_axe_a",0)],itp_craftable|itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 390 , weight(4.75)|difficulty(10)|spd_rtng(88) | weapon_length(120)|swing_damage(46 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["long_axe_b",         "Long War Axe", [("long_axe_b",0)], itp_type_polearm| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_next_item_as_melee|itp_unbalanced|itp_merchandise, itc_staff|itcf_carry_axe_back,
 510 , weight(5.0)|difficulty(10)|spd_rtng(92) | weapon_length(125)|swing_damage(50 , cut) | thrust_damage(18 ,  blunt),imodbits_axe ],
["long_axe_b_alt",         "Long War Axe", [("long_axe_b",0)], itp_craftable|itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 510 , weight(5.0)|difficulty(10)|spd_rtng(87) | weapon_length(125)|swing_damage(50 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["long_axe_c",         "Great Long Axe", [("long_axe_c",0)], itp_type_polearm| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_next_item_as_melee|itp_unbalanced|itp_merchandise, itc_staff|itcf_carry_axe_back,
 660 , weight(5.5)|difficulty(10)|spd_rtng(91) | weapon_length(127)|swing_damage(54 , cut) | thrust_damage(19 ,  blunt),imodbits_axe ],
["long_axe_c_alt",      "Great Long Axe", [("long_axe_c",0)], itp_craftable|itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 660 , weight(5.5)|difficulty(10)|spd_rtng(85) | weapon_length(127)|swing_damage(54 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["bardiche",         "Bardiche", [("two_handed_battle_axe_d",0)], itp_craftable|itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 291 , weight(4.75)|difficulty(10)|spd_rtng(91) | weapon_length(102)|swing_damage(47 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["great_bardiche",         "Great Bardiche", [("two_handed_battle_axe_f",0)], itp_craftable|itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 617 , weight(5.0)|difficulty(10)|spd_rtng(89) | weapon_length(116)|swing_damage(50 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["voulge",         "Voulge", [("two_handed_battle_long_axe_a",0)], itp_type_polearm|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_staff,
 120 , weight(3.0)|difficulty(10)|spd_rtng(88) | weapon_length(175)|swing_damage(40 , cut) | thrust_damage(18 ,  pierce),imodbits_axe ],
["long_bardiche",         "Long Bardiche", [("two_handed_battle_long_axe_b",0)], itp_type_polearm|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_staff,
390 , weight(4.75)|difficulty(11)|spd_rtng(89) | weapon_length(140)|swing_damage(48 , cut) | thrust_damage(17 ,  pierce),imodbits_axe ],
["great_long_bardiche",         "Great Long Bardiche", [("two_handed_battle_long_axe_c",0)], itp_type_polearm|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_staff,
 660 , weight(5.0)|difficulty(12)|spd_rtng(88) | weapon_length(155)|swing_damage(50 , cut) | thrust_damage(17 ,  pierce),imodbits_axe ],

["horseman_poleaxe_a",         "Horseman Poleaxe", [("luc_swiss_poleaxe",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry, itcf_carry_spear|itc_guandao, 381 , weight(3.25)|difficulty(9)|spd_rtng(93) | weapon_length(156)|swing_damage(43 , cut) | thrust_damage(15 ,  pierce),imodbits_polearm ],
["horseman_poleaxe_b",         "Horseman Poleaxe", [("luc_swiss_poleaxe_b",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry, itcf_carry_spear|itc_guandao, 439 , weight(3.5)|difficulty(9)|spd_rtng(93) | weapon_length(160)|swing_damage(43 , cut) | thrust_damage(18 ,  pierce),imodbits_polearm ],

["hafted_blade_a",         "Hafted Blade", [("luc_hafted_blade_1",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry, itcf_carry_spear|itc_guandao, 350 , weight(3.25)|difficulty(0)|spd_rtng(93) | weapon_length(150)|swing_damage(39 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm ],
["hafted_blade_b",         "Hafted Blade", [("luc_hafted_blade_2",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry, itcf_carry_spear|itc_guandao, 348 , weight(3.5)|difficulty(0)|spd_rtng(95) | weapon_length(150)|swing_damage(40 , cut) | thrust_damage(15 ,  pierce),imodbits_polearm ],
["hafted_blade_c",         "Hafted Blade", [("luc_hafted_blade_3",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry, itcf_carry_spear|itc_guandao, 369 , weight(3)|difficulty(0)|spd_rtng(96) | weapon_length(150)|swing_damage(40 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm ],
["hafted_blade_d",         "Hafted Blade", [("luc_hafted_blade_4",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry, itcf_carry_spear|itc_guandao, 359 , weight(3)|difficulty(0)|spd_rtng(96) | weapon_length(150)|swing_damage(37 , cut) | thrust_damage(26 ,  pierce),imodbits_polearm ],
["hafted_blade_e",         "Hafted Blade", [("luc_hafted_blade_3",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry, itcf_carry_spear|itc_guandao, 371 , weight(3)|difficulty(0)|spd_rtng(97) | weapon_length(150)|swing_damage(37 , cut) | thrust_damage(25 ,  pierce),imodbits_polearm ],
["hafted_blade_f",         "Hafted Blade", [("luc_hafted_blade_3",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry, itcf_carry_spear|itc_guandao, 362 , weight(3)|difficulty(0)|spd_rtng(96) | weapon_length(150)|swing_damage(38 , cut) | thrust_damage(25 ,  pierce),imodbits_polearm ],

["shortened_military_scythe",         "Shortened Military Scythe", [("two_handed_battle_scythe_a",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back,
 264 , weight(3.0)|difficulty(10)|spd_rtng(90) | weapon_length(112)|swing_damage(45 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],

["sword_medieval_a", "Sword", [("sword_medieval_a",0),("sword_medieval_a_scabbard", ixmesh_carry)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 163 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(27 , cut) | thrust_damage(22 ,  pierce),imodbits_sword_high ],
["sword_medieval_b", "Sword", [("sword_medieval_b",0),("sword_medieval_b_scabbard", ixmesh_carry),("sword_rusty_a",imodbit_rusty),("sword_rusty_a_scabbard", ixmesh_carry|imodbit_rusty)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 243 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(28 , cut) | thrust_damage(23 ,  pierce),imodbits_sword_high ],
["sword_medieval_b_small", "Short Sword", [("sword_medieval_b_small",0),("sword_medieval_b_small_scabbard", ixmesh_carry)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 152 , weight(1)|difficulty(0)|spd_rtng(102) | weapon_length(85)|swing_damage(26, cut) | thrust_damage(24, pierce),imodbits_sword_high ],
["sword_medieval_c", "Arming Sword", [("sword_medieval_c",0),("sword_medieval_c_scabbard", ixmesh_carry)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 410 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(29 , cut) | thrust_damage(24 ,  pierce),imodbits_sword_high ],
["sword_medieval_c_small", "Short Arming Sword", [("sword_medieval_c_small",0),("sword_medieval_c_small_scabbard", ixmesh_carry)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 243 , weight(1)|difficulty(0)|spd_rtng(103) | weapon_length(86)|swing_damage(26, cut) | thrust_damage(24 ,  pierce),imodbits_sword_high ],
["sword_medieval_c_long", "Arming Sword", [("sword_medieval_c_long",0),("sword_medieval_c_long_scabbard", ixmesh_carry)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 480 , weight(1.7)|difficulty(0)|spd_rtng(99) | weapon_length(100)|swing_damage(29 , cut) | thrust_damage(28 ,  pierce),imodbits_sword_high ],
["sword_medieval_d_long", "Long Arming Sword", [("sword_medieval_d_long",0),("sword_medieval_d_long_scabbard", ixmesh_carry)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 550 , weight(1.8)|difficulty(0)|spd_rtng(96) | weapon_length(105)|swing_damage(33 , cut) | thrust_damage(28 ,  pierce),imodbits_sword ],
 
["sword_viking_1", "Nordic Sword", [("sword_viking_c",0),("sword_viking_c_scabbard ", ixmesh_carry)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 147 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(94)|swing_damage(28 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ] ,
["sword_viking_2", "Nordic Sword", [("sword_viking_b",0),("sword_viking_b_scabbard", ixmesh_carry)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 276 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(29 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high ],
["sword_viking_2_small", "Nordic Short Sword", [("sword_viking_b_small",0),("sword_viking_b_small_scabbard", ixmesh_carry)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 162 , weight(1.25)|difficulty(0)|spd_rtng(103) | weapon_length(85)|swing_damage(28 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high ],
["sword_viking_3", "Nordic War Sword", [("sword_viking_a",0),("sword_viking_a_scabbard", ixmesh_carry)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 394 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(30 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high ],

["sword_viking_3_small", "Nordic Short War Sword", [("sword_viking_a_small",0),("sword_viking_a_small_scabbard", ixmesh_carry)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 280 , weight(1.25)|difficulty(0)|spd_rtng(103) | weapon_length(86)|swing_damage(29 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high ],

["sword_khergit_1", "Nomad Sabre", [("khergit_sword_b",0),("khergit_sword_b_scabbard", ixmesh_carry)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 105 , weight(1.25)|difficulty(0)|spd_rtng(100) | weapon_length(97)|swing_damage(29 , cut),imodbits_sword_high ],
["sword_khergit_2", "Sabre", [("khergit_sword_c",0),("khergit_sword_c_scabbard", ixmesh_carry)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 191 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(97)|swing_damage(30 , cut),imodbits_sword_high ],
["sword_khergit_3", "Sabre", [("khergit_sword_a",0),("khergit_sword_a_scabbard", ixmesh_carry)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 294 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(98)|swing_damage(31 , cut),imodbits_sword_high ],
["sword_khergit_4", "Heavy Sabre", [("khergit_sword_d",0),("khergit_sword_d_scabbard", ixmesh_carry)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 384 , weight(1.75)|difficulty(0)|spd_rtng(98) | weapon_length(96)|swing_damage(33 , cut),imodbits_sword_high ],

["mace_1",         "Spiked Club", [("mace_d",0)], itp_craftable|itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
 45 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(70)|swing_damage(19 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],
["mace_2",         "Knobbed_Mace", [("luc_knobbed_mace_b",0)], itp_craftable|itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
 98 , weight(2.5)|difficulty(0)|spd_rtng(98) | weapon_length(70)|swing_damage(21 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["mace_3",         "Spiked Mace", [("luc_spiked_mace",0)], itp_craftable|itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
 152 , weight(2.75)|difficulty(0)|spd_rtng(98) | weapon_length(70)|swing_damage(23 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["mace_4",         "Winged_Mace", [("mace_b",0)], itp_craftable|itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
 212 , weight(2.75)|difficulty(0)|spd_rtng(98) | weapon_length(70)|swing_damage(24 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],

["m_mace_knight", "Knight Hammer", [("luc_knightly_hammer",0)], itp_craftable|itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 899 , weight(3.0)|difficulty(11)|spd_rtng(98) | weapon_length(75)|swing_damage(32 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["m_mace_knight_pierce", "Knight War Hammer", [("luc_warhammer_s",0)], itp_craftable|itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 1346 , weight(3.0)|difficulty(11)|spd_rtng(98) | weapon_length(80)|swing_damage(32 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],

# Goedendag
 ["club_with_spike_head",  "Spiked Staff", [("mace_e",0)],  itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_wooden_parry, itc_bastardsword|itcf_carry_axe_back,
 200 , weight(2.80)|difficulty(9)|spd_rtng(95) | weapon_length(117)|swing_damage(24 , blunt) | thrust_damage(20 ,  pierce),imodbits_mace ],

["long_spiked_club",         "Long Spiked Club", [("mace_long_c",0)], itp_type_polearm|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_axe_back,
 264 , weight(3)|difficulty(0)|spd_rtng(96) | weapon_length(126)|swing_damage(23 , pierce) | thrust_damage(20 ,  blunt),imodbits_mace ],
["long_hafted_knobbed_mace",         "Long Hafted Knobbed Mace", [("mace_long_a",0)], itp_type_polearm| itp_can_knock_down|itp_primary|itp_wooden_parry, itc_staff|itcf_carry_axe_back,
 324 , weight(3)|difficulty(0)|spd_rtng(95) | weapon_length(133)|swing_damage(26 , blunt) | thrust_damage(23 ,  blunt),imodbits_mace ],
["long_hafted_spiked_mace",         "Long Hafted Spiked Mace", [("mace_long_b",0)], itp_type_polearm|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_axe_back,
 310 , weight(3)|difficulty(0)|spd_rtng(94) | weapon_length(140)|swing_damage(28 , blunt) | thrust_damage(26 ,  blunt),imodbits_mace ],

["scythe",         "Scythe", [("luc_war_scythe",0)], itp_craftable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff|itcf_carry_spear, 43 , weight(2)|difficulty(0)|spd_rtng(97) | weapon_length(182)|swing_damage(30 , cut) | thrust_damage(14 ,  pierce),imodbits_polearm ],
["scythe_b",         "War Scythe", [("luc_war_scythe_2",0)], itp_craftable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff|itcf_carry_spear, 120 , weight(3)|difficulty(0)|spd_rtng(93) | weapon_length(182)|swing_damage(35 , cut) | thrust_damage(15 ,  pierce),imodbits_polearm ],
["pitch_fork",         "Pitch Fork", [("luc_fork_pitch",0)], itp_craftable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry,itc_staff, 19 , weight(1.5)|difficulty(0)|spd_rtng(87) | weapon_length(154)|swing_damage(16 , blunt) | thrust_damage(22 ,  pierce),imodbits_polearm ],
["military_fork", "Military Fork", [("luc_fork_military",0)], itp_craftable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry,itc_staff, 153 , weight(2)|difficulty(0)|spd_rtng(95) | weapon_length(135)|swing_damage(15 , blunt) | thrust_damage(30 ,  pierce),imodbits_polearm ],
["battle_fork",         "Battle Fork", [("luc_fork_battle",0)], itp_craftable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry,itc_staff, 282 , weight(2.2)|difficulty(0)|spd_rtng(90) | weapon_length(144)|swing_damage(15, blunt) | thrust_damage(35 ,  pierce),imodbits_polearm ],
["battle_trident",         "Battle Trident", [("luc_trident",0)], itp_craftable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry,itc_staff|itcf_carry_spear, 282 , weight(2.2)|difficulty(0)|spd_rtng(90) | weapon_length(140)|swing_damage(15, blunt) | thrust_damage(41 ,  pierce),imodbits_polearm ],
["ranseur",         "Ranseur", [("luc_ranseur",0)], itp_craftable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry,itc_staff|itcf_carry_spear, 387 , weight(2.25)|difficulty(0)|spd_rtng(96) | weapon_length(160)|swing_damage(18, pierce) | thrust_damage(35 ,  pierce),imodbits_polearm ],
["boar_spear",         "Boar Spear", [("boar_spear_k2",0)], itp_craftable|itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry,itc_staff|itcf_carry_spear, 
76 , weight(1.5)|difficulty(0)|spd_rtng(90) | weapon_length(157)|swing_damage(26 , cut) | thrust_damage(23 ,  pierce),imodbits_polearm ],
["broad_spear",         "Broad Spear", [("luc_broad_spear",0)], itp_craftable|itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry,itc_staff|itcf_carry_spear, 
76 , weight(1.5)|difficulty(0)|spd_rtng(90) | weapon_length(157)|swing_damage(26 , cut) | thrust_damage(23 ,  pierce),imodbits_polearm ],
["tongue_spear",         "Tongue Spear", [("luc_ox_tongue",0)], itp_craftable|itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry,itc_staff|itcf_carry_spear, 
76 , weight(1.5)|difficulty(0)|spd_rtng(90) | weapon_length(157)|swing_damage(26 , cut) | thrust_damage(23 ,  pierce),imodbits_polearm ],


["jousting_lance", "Jousting Lance", [("joust_of_peace",0)], itp_craftable|itp_couchable|itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_greatlance, 158 , weight(5)|difficulty(0)|spd_rtng(61) | weapon_length(240)|swing_damage(0 , cut) | thrust_damage(17 ,  blunt),imodbits_polearm ],
["double_sided_lance", "Double Sided Lance", [("lance_dblhead",0)], itp_craftable|itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff, 261 , weight(4.0)|difficulty(0)|spd_rtng(95) | weapon_length(128)|swing_damage(25, cut) | thrust_damage(27 ,  pierce),imodbits_polearm ],
["glaive",         "Glaive", [("luc_german_great_glaive",0)], itp_craftable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_staff|itcf_carry_spear,
 352 , weight(4.5)|difficulty(0)|spd_rtng(90) | weapon_length(157)|swing_damage(39 , cut) | thrust_damage(21 ,  pierce),imodbits_polearm ],
 ["m_glaive_a", "Milita Glaive", [("luc_burgundian_glaive",0)], itp_craftable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_staff|itcf_carry_spear,
 352 , weight(4.5)|difficulty(0)|spd_rtng(90) | weapon_length(157)|swing_damage(39 , cut) | thrust_damage(21 ,  pierce),imodbits_polearm ],
 ["m_glaive_b", "Great Glaive", [("luc_german_halbard",0)], itp_craftable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_staff|itcf_carry_spear,
 352 , weight(4.5)|difficulty(0)|spd_rtng(90) | weapon_length(157)|swing_damage(39 , cut) | thrust_damage(21 ,  pierce),imodbits_polearm ],
["poleaxe",         "Poleaxe", [("luc_pole_axe_new",0)], itp_craftable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_staff,
 384 , weight(4.5)|difficulty(13)|spd_rtng(77) | weapon_length(180)|swing_damage(50 , cut) | thrust_damage(15 ,  blunt),imodbits_polearm ],
["polehammer",         "Polehammer", [("pole_hammer",0)], itp_craftable|itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_wooden_parry, itc_staff,
 169 , weight(7)|difficulty(18)|spd_rtng(50) | weapon_length(126)|swing_damage(50 , blunt) | thrust_damage(35 ,  blunt),imodbits_polearm ],
["staff",         "Staff", [("wooden_staff",0)], itp_craftable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_staff|itcf_carry_sword_back,
 36 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(130)|swing_damage(18 , blunt) | thrust_damage(19 ,  blunt),imodbits_polearm ],
["quarter_staff", "Quarter Staff", [("quarter_staff",0)], itp_craftable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_staff|itcf_carry_sword_back,
 60 , weight(2)|difficulty(0)|spd_rtng(104) | weapon_length(140)|swing_damage(20 , blunt) | thrust_damage(20 ,  blunt),imodbits_polearm ],
["iron_staff",         "Iron Staff", [("iron_staff",0)], itp_craftable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary, itc_staff|itcf_carry_sword_back,
 202 , weight(2)|difficulty(0)|spd_rtng(97) | weapon_length(140)|swing_damage(25 , blunt) | thrust_damage(26 ,  blunt),imodbits_polearm ],

["shortened_spear",         "Shortened Spear", [("spear_g_1-9m",0)], itp_craftable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear,
 53 , weight(2.0)|difficulty(0)|spd_rtng(102) | weapon_length(120)|swing_damage(19 , blunt) | thrust_damage(25 ,  pierce),imodbits_polearm ],
["spear",         "Spear", [("spear_h_2-15m",0)], itp_craftable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear,
 85 , weight(2.25)|difficulty(0)|spd_rtng(98) | weapon_length(135)|swing_damage(20 , blunt) | thrust_damage(26 ,  pierce),imodbits_polearm ],

["bamboo_spear",         "Bamboo Spear", [("arabian_spear_a_3m",0)], itp_craftable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff|itcf_carry_spear,
 80 , weight(2.0)|difficulty(0)|spd_rtng(88) | weapon_length(200)|swing_damage(15 , blunt) | thrust_damage(20 ,  pierce),imodbits_polearm ],

["war_spear",         "War Spear", [("luc_long_war_spear",0)], itp_craftable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear,
 140 , weight(2.5)|difficulty(0)|spd_rtng(95) | weapon_length(150)|swing_damage(20 , blunt) | thrust_damage(27 ,  pierce),imodbits_polearm ],

["crusader_spear_a","Infantry Spear", [("crusader_spear_a", 0)], itp_craftable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear,140, weight(2.5)|abundance(100)|spd_rtng(110)|weapon_length(180)|thrust_damage(27, pierce)|swing_damage(20, blunt), imodbits_none, []],
["crusader_spear_b","Infantry Spear", [("crusader_spear_b", 0)], itp_craftable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear,140, weight(2.5)|abundance(100)|spd_rtng(110)|weapon_length(175)|thrust_damage(27, pierce)|swing_damage(20, blunt), imodbits_none, []],
["crusader_spear_c","Infantry Spear", [("crusader_spear_c", 0)], itp_craftable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear,140, weight(2.5)|abundance(100)|spd_rtng(100)|weapon_length(170)|thrust_damage(27, pierce)|swing_damage(20, blunt), imodbits_none, []],
["crusader_spear_inf_a","Infantry Spear", [("crusader_spear_inf_a", 0)], itp_craftable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear,140, weight(2.5)|abundance(100)|spd_rtng(100)|weapon_length(155)|thrust_damage(27, pierce)|swing_damage(20, blunt), imodbits_none, []],
["crusader_spear_inf_b","Infantry Spear", [("crusader_spear_inf_b", 0)], itp_craftable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear,140, weight(2.5)|abundance(100)|spd_rtng(100)|weapon_length(160)|thrust_damage(27, pierce)|swing_damage(20, blunt), imodbits_none, []],
["crusader_spear_inf_c","Infantry Spear", [("crusader_spear_inf_c", 0)], itp_craftable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear,140, weight(2.5)|abundance(100)|spd_rtng(100)|weapon_length(175)|thrust_damage(27, pierce)|swing_damage(20, blunt), imodbits_none, []],

["solarian_spear_a","Infantry Spear", [("saracin_spears_a_v_1", 0)], itp_craftable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear,140, weight(2.0)|abundance(100)|spd_rtng(110)|weapon_length(125)|thrust_damage(25, pierce)|swing_damage(20, blunt), imodbits_none, []],
["solarian_spear_b","Infantry Spear", [("saracin_spears_a", 0)], itp_craftable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear,197, weight(2.0)|abundance(100)|spd_rtng(110)|weapon_length(165)|thrust_damage(27, pierce)|swing_damage(20, blunt), imodbits_none, []],

["solarian_lance_a", "Solarian Lance", [("mameluk_spears_a",0)], itp_couchable|itp_craftable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 334 , weight(3.5)|difficulty(0)|spd_rtng(90) | weapon_length(185)|swing_damage(21 , blunt) | thrust_damage(27 ,  pierce),imodbits_polearm ],
["solarian_lance_b", "Solarian Lance", [("mameluk_spears_b",0)], itp_couchable|itp_craftable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 270 , weight(2.5)|difficulty(0)|spd_rtng(99) | weapon_length(185)|swing_damage(16 , blunt) | thrust_damage(26 ,  pierce),imodbits_polearm ],
["solarian_lance_c", "Solarian Lance", [("mameluk_spears_c",0)], itp_couchable|itp_craftable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 270 , weight(2.5)|difficulty(0)|spd_rtng(99) | weapon_length(180)|swing_damage(16 , blunt) | thrust_damage(26 ,  pierce),imodbits_polearm ],
["solarian_lance_d", "Solarian Lance", [("mameluk_spears_c_v_1",0)], itp_couchable|itp_craftable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 345 , weight(3.5)|difficulty(0)|spd_rtng(99) | weapon_length(200)|swing_damage(20 , blunt) | thrust_damage(28 ,  pierce),imodbits_polearm ],

["military_scythe",         "Military Scythe", [("luc_bohemian_war_scythe",0),("spear_c_2-5m",imodbits_bad)], itp_craftable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff|itcf_carry_spear,
 155 , weight(2.5)|difficulty(0)|spd_rtng(90) | weapon_length(155)|swing_damage(36 , cut) | thrust_damage(25 ,  pierce),imodbits_polearm ],
["light_lance",         "Light Lance", [("spear_b_2-75m",0)], itp_couchable|itp_craftable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,
 180 , weight(2.5)|difficulty(0)|spd_rtng(85) | weapon_length(175)|swing_damage(16 , blunt) | thrust_damage(27 ,  pierce),imodbits_polearm ],
["lance",         "Lance", [("spear_d_2-8m",0)], itp_couchable|itp_craftable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,
 270 , weight(2.5)|difficulty(0)|spd_rtng(80) | weapon_length(180)|swing_damage(16 , blunt) | thrust_damage(26 ,  pierce),imodbits_polearm ],
["heavy_lance",         "Heavy Lance", [("spear_f_2-9m",0)], itp_couchable|itp_craftable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,
 360 , weight(2.75)|difficulty(10)|spd_rtng(75) | weapon_length(190)|swing_damage(16 , blunt) | thrust_damage(26 ,  pierce),imodbits_polearm ],
["great_lance",         "Great Lance", [("heavy_lance",0)], itp_couchable|itp_craftable|itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_greatlance, 
 410 , weight(5)|difficulty(11)|spd_rtng(55) | weapon_length(240)|swing_damage(0 , cut) | thrust_damage(21 ,  pierce),imodbits_polearm ],

["crusader_knight_spear_a","Knight Lance", [("crusader_knight_spear_a", 0)], itp_couchable|itp_craftable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,410, weight(5)|abundance(100)|difficulty(11)|spd_rtng(55)|weapon_length(265)|thrust_damage(21, pierce), imodbits_none, [], [fac_kingdom_1]],
["crusader_knight_spear_a_2","Knight Lance Broken", [("crusader_knight_spear_a_2", 0)], itp_couchable|itp_craftable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,410, weight(4)|abundance(100)|difficulty(11)|spd_rtng(55)|weapon_length(170)|thrust_damage(5, blunt), imodbits_none, []],
["crusader_knight_spear_b","Knight Lance", [("crusader_knight_spear_b", 0)], itp_couchable|itp_craftable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,410, weight(5)|abundance(100)|difficulty(11)|spd_rtng(55)|weapon_length(285)|thrust_damage(21, pierce), imodbits_none, [], [fac_kingdom_1]],
["crusader_knight_spear_b_2","Knight Lance Broken", [("crusader_knight_spear_b_2", 0)], itp_couchable|itp_craftable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,410, weight(4)|abundance(100)|difficulty(11)|spd_rtng(55)|weapon_length(170)|thrust_damage(5, blunt), imodbits_none, []],

["crusader_knight_spear_a_2_tip","Broken Knight Lance Tip", [("crusader_knight_spear_a_1", 0)], itp_type_one_handed_wpn|itp_primary, itcf_carry_sword_left_hip|itc_longsword,31, weight(3)|abundance(100)|spd_rtng(100)|weapon_length(70)|thrust_damage(19, pierce)|swing_damage(12, blunt), imodbits_none, [], [fac_kingdom_1]],

["pike",         "Pike", [("spear_a_3m",0)], itp_craftable|itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed, itc_cutting_spear,
 125 , weight(3.0)|difficulty(0)|spd_rtng(81) | weapon_length(245)|swing_damage(16 , blunt) | thrust_damage(26 ,  pierce),imodbits_polearm ],
["ashwood_pike", "Ashwood Pike", [("pike",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_cutting_spear,
 205 , weight(3.5)|difficulty(9)|spd_rtng(90) | weapon_length(170)|swing_damage(19 , blunt) | thrust_damage(29,  pierce),imodbits_polearm ],
["m_ashwood_pike_a", "Ashwood Pike", [("ashwood_pike",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_cutting_spear,
 205 , weight(3.5)|difficulty(9)|spd_rtng(90) | weapon_length(170)|swing_damage(19 , blunt) | thrust_damage(29,  pierce),imodbits_polearm ],
["awlpike",    "Awlpike", [("awl_pike_b",0)], itp_craftable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear,
 345 , weight(2.25)|difficulty(0)|spd_rtng(92) | weapon_length(165)|swing_damage(20 , blunt) | thrust_damage(33 ,  pierce),imodbits_polearm ],
["awlpike_long",  "Long Awlpike", [("awl_pike_a",0)], itp_craftable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear,
 385 , weight(2.25)|difficulty(0)|spd_rtng(89) | weapon_length(185)|swing_damage(20 , blunt) | thrust_damage(32 ,  pierce),imodbits_polearm ],

# 378 , weight(3.5)|difficulty(12)|spd_rtng(92) | weapon_length(160)|swing_damage(20 ,blunt) | thrust_damage(31 ,  pierce),imodbits_polearm ],
["bec_de_corbin_a",  "War Hammer", [("polehammer_edited",0)], itp_craftable|itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed, itc_cutting_spear|itcf_carry_spear,
 125 , weight(3.0)|difficulty(0)|spd_rtng(81) | weapon_length(120)|swing_damage(38, blunt) | thrust_damage(38 ,  pierce),imodbits_polearm ],
# 378 , weight(3.5)|difficulty(12)|spd_rtng(92) | weapon_length(160)|swing_damage(20 ,blunt) | thrust_damage(31 ,  pierce),imodbits_polearm ],

# SHIELDS

["wooden_shield", "Wooden Shield", [("shield_round_a",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
["nordic_shield", "Nordic Shield", [("shield_round_b",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  95 , weight(2)|hit_points(440)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
["fur_covered_shield",  "Fur Covered Shield", [("shield_kite_m",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  227 , weight(3.5)|hit_points(600)|body_armor(1)|spd_rtng(76)|shield_width(81),imodbits_shield ],
["steel_shield", "Steel Shield", [("shield_dragon",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,  697 , weight(4)|hit_points(700)|body_armor(17)|spd_rtng(61)|shield_width(40),imodbits_shield ],

["plate_covered_round_shield", "Plate Covered Round Shield", [("shield_round_e",0)], itp_type_shield, itcf_carry_round_shield,  140 , weight(4)|hit_points(330)|body_armor(16)|spd_rtng(90)|shield_width(40),imodbits_shield ],
["leather_covered_round_shield", "Leather Covered Round Shield", [("shield_round_d",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  80 , weight(2.5)|hit_points(310)|body_armor(8)|spd_rtng(96)|shield_width(40),imodbits_shield ],
["hide_covered_round_shield", "Hide Covered Round Shield", [("shield_round_f",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  40 , weight(2)|hit_points(260)|body_armor(3)|spd_rtng(100)|shield_width(40),imodbits_shield ],

["shield_heater_c", "Heater Shield", [("shield_heater_c",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  277 , weight(3.5)|hit_points(410)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],

["norman_shield_1",         "Kite Shield", [("norman_shield_1",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
["norman_shield_2",         "Kite Shield", [("norman_shield_2",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
["norman_shield_3",         "Kite Shield", [("norman_shield_3",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
["norman_shield_4",         "Kite Shield", [("norman_shield_4",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
["norman_shield_5",         "Kite Shield", [("norman_shield_5",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
["norman_shield_6",         "Kite Shield", [("norman_shield_6",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
["norman_shield_7",         "Kite Shield", [("norman_shield_7",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
["norman_shield_8",         "Kite Shield", [("norman_shield_8",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],

["m_plain_round_shield_a", "Plain Round Shield", [("luc_wooden_shield_y",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  65 , weight(3)|hit_points(260)|body_armor(8)|spd_rtng(90)|shield_width(50),imodbits_shield, [], []],
["m_plain_round_shield_b", "Plain Round Shield", [("luc_wooden_shield_w",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  129 , weight(3)|hit_points(330)|body_armor(9)|spd_rtng(90)|shield_width(50),imodbits_shield, [], []],
["m_plain_round_shield_c", "Leather Covered Round Shield", [("luc_leather_covered_shield_z",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  349 , weight(4)|hit_points(400)|body_armor(11)|spd_rtng(90)|shield_width(50),imodbits_shield, [], []],
["m_plain_round_shield_d", "Leather Covered Round Shield", [("luc_leather_covered_shield_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  301 , weight(4)|hit_points(370)|body_armor(9)|spd_rtng(90)|shield_width(50),imodbits_shield, [], []],
["m_plain_round_shield_e", "Heavy Plain Round Shield", [("luc_heavy_wooden_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  349 , weight(4)|hit_points(400)|body_armor(11)|spd_rtng(90)|shield_width(50),imodbits_shield, [], []],

["tab_shield_round_a", "Old Round Shield", [("tableau_shield_round_5",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  
26 , weight(2.5)|hit_points(195)|body_armor(4)|spd_rtng(93)|shield_width(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_5", ":agent_no", ":troop_no")])]],
["tab_shield_round_b", "Plain Round Shield", [("tableau_shield_round_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  
65 , weight(3)|hit_points(260)|body_armor(8)|spd_rtng(90)|shield_width(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_3", ":agent_no", ":troop_no")])]],
["tab_shield_round_c", "Round Shield", [("tableau_shield_round_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  
105 , weight(3.5)|hit_points(310)|body_armor(12)|spd_rtng(87)|shield_width(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner","tableau_round_shield_2", ":agent_no", ":troop_no")])]],
["tab_shield_round_d", "Heavy Round Shield", [("tableau_shield_round_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  
210 , weight(4)|hit_points(350)|body_armor(15)|spd_rtng(84)|shield_width(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_round_e", "Huscarl's Round Shield", [("tableau_shield_round_4",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,  
430 , weight(4.5)|hit_points(410)|body_armor(19)|spd_rtng(81)|shield_width(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_4", ":agent_no", ":troop_no")])]],

["tab_shield_kite_a", "Old Kite Shield",   [("tableau_shield_kite_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
33 , weight(2)|hit_points(165)|body_armor(5)|spd_rtng(96)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_kite_b", "Plain Kite Shield",   [("tableau_shield_kite_3" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
70 , weight(2.5)|hit_points(215)|body_armor(10)|spd_rtng(93)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_3", ":agent_no", ":troop_no")])]],
["tab_shield_kite_c", "Kite Shield",   [("tableau_shield_kite_2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
156 , weight(3)|hit_points(265)|body_armor(13)|spd_rtng(90)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_2", ":agent_no", ":troop_no")])]],
["tab_shield_kite_d", "Heavy Kite Shield",   [("tableau_shield_kite_2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
320 , weight(3.5)|hit_points(310)|body_armor(18)|spd_rtng(87)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_2", ":agent_no", ":troop_no")])]],
["tab_shield_kite_cav_a", "Horseman's Kite Shield",   [("tableau_shield_kite_4" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
205 , weight(2)|hit_points(165)|body_armor(14)|spd_rtng(103)|shield_width(30)|shield_height(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_4", ":agent_no", ":troop_no")])]],
["tab_shield_kite_cav_b", "Knightly Kite Shield",   [("tableau_shield_kite_4" ,0)], itp_merchandise|itp_type_shield, itcf_carry_kite_shield,  
360 , weight(2.5)|hit_points(225)|body_armor(23)|spd_rtng(100)|shield_width(30)|shield_height(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_4", ":agent_no", ":troop_no")])]],

["tab_shield_heater_a", "Old Heater Shield",   [("tableau_shield_heater_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
36 , weight(2)|hit_points(160)|body_armor(6)|spd_rtng(96)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_heater_b", "Plain Heater Shield",   [("tableau_shield_heater_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
74 , weight(2.5)|hit_points(210)|body_armor(11)|spd_rtng(93)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_heater_c", "Heater Shield",   [("tableau_shield_heater_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
160 , weight(3)|hit_points(260)|body_armor(14)|spd_rtng(90)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_heater_d", "Heavy Heater Shield",   [("tableau_shield_heater_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
332 , weight(3.5)|hit_points(305)|body_armor(19)|spd_rtng(87)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_heater_cav_a", "Horseman's Heater Shield",   [("tableau_shield_heater_2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
229 , weight(2)|hit_points(160)|body_armor(16)|spd_rtng(103)|shield_width(30)|shield_height(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_2", ":agent_no", ":troop_no")])]],
["tab_shield_heater_cav_b", "Knightly Heater Shield",   [("tableau_shield_heater_2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
390 , weight(2.5)|hit_points(220)|body_armor(23)|spd_rtng(100)|shield_width(30)|shield_height(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_2", ":agent_no", ":troop_no")])]],

["tab_shield_pavise_a", "Old Board Shield",   [("tableau_shield_pavise_2" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,  
60 , weight(3.5)|hit_points(280)|body_armor(4)|spd_rtng(89)|shield_width(43)|shield_height(100),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_2", ":agent_no", ":troop_no")])]],
["tab_shield_pavise_b", "Plain Board Shield",   [("tableau_shield_pavise_2" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,  
114 , weight(4)|hit_points(360)|body_armor(8)|spd_rtng(85)|shield_width(43)|shield_height(100),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_2", ":agent_no", ":troop_no")])]],
["tab_shield_pavise_c", "Board Shield",   [("tableau_shield_pavise_1" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,  
210 , weight(4.5)|hit_points(430)|body_armor(10)|spd_rtng(81)|shield_width(43)|shield_height(100),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_pavise_d", "Heavy Board Shield",   [("tableau_shield_pavise_1" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,  
370 , weight(5)|hit_points(550)|body_armor(14)|spd_rtng(78)|shield_width(43)|shield_height(100),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_1", ":agent_no", ":troop_no")])]],

["shield_heater_c", "Leather Covered Heater Shield", [("shield_heater_c",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 277 , weight(2.75)|hit_points(310)|body_armor(12)|spd_rtng(80)|shield_width(30)|shield_height(51),imodbits_shield,
[(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_shield_heater_c", ":agent_no", ":troop_no")])]],
["shield_heater_d", "Heater Shield", [("shield_heater_d",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 477 , weight(3.25)|hit_points(510)|body_armor(14)|spd_rtng(80)|shield_width(31)|shield_height(52),imodbits_shield,
[(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_shield_heater_d", ":agent_no", ":troop_no")])]],

["shield_kite_g", "Kite Shield", [("shield_kite_g",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(36)|shield_height(72),imodbits_shield,
[(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_shield_kite_g", ":agent_no", ":troop_no")])]],
["shield_kite_h", "Battle Shield", [("shield_kite_h",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(35)|shield_height(75),imodbits_shield,
[(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_shield_kite_h", ":agent_no", ":troop_no")])]],
["shield_kite_i", "Banded Kite Shield", [("shield_kite_i",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(36)|shield_height(70),imodbits_shield,
[(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_shield_kite_i", ":agent_no", ":troop_no")])]],
["shield_kite_k", "Studded Kite Shield", [("shield_kite_k",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(36)|shield_height(70),imodbits_shield,
[(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_shield_kite_k", ":agent_no", ":troop_no")])]],

["norman_shield_1", "Kite Shield", [("norman_shield_a",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(35)|shield_height(70),imodbits_shield,
[(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_shield_norman_1", ":agent_no", ":troop_no")])]],
["norman_shield_2", "Kite Shield", [("norman_shield_b",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(35)|shield_height(70),imodbits_shield,
[(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_shield_norman_2", ":agent_no", ":troop_no")])]],
["norman_shield_3", "Kite Shield", [("norman_shield_c",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(35)|shield_height(70),imodbits_shield,
[(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_shield_norman_3", ":agent_no", ":troop_no")])]],
["norman_shield_4", "Kite Shield", [("norman_shield_d",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(35)|shield_height(70),imodbits_shield,
[(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_shield_norman_4", ":agent_no", ":troop_no")])]],

["practice_board_shield", "Practice Board Shield", [("tableau_shield_pavise" ,0)], itp_type_shield|itp_cant_use_on_horseback, itcf_carry_board_shield,
370 , weight(5)|hit_points(550)|body_armor(10)|spd_rtng(78)|shield_width(45)|shield_height(100),imodbits_shield,
[(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_3", ":agent_no", ":troop_no")])]],

["tab_shield_small_round_a", "Plain Cavalry Shield", [("tableau_shield_small_round_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  
96 , weight(2)|hit_points(160)|body_armor(8)|spd_rtng(105)|shield_width(40),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_3", ":agent_no", ":troop_no")])]],
["tab_shield_small_round_b", "Round Cavalry Shield", [("tableau_shield_small_round_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
195 , weight(2.5)|hit_points(200)|body_armor(14)|spd_rtng(103)|shield_width(40),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_small_round_c", "Elite Cavalry Shield", [("tableau_shield_small_round_2",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,
370 , weight(3)|hit_points(250)|body_armor(22)|spd_rtng(100)|shield_width(40),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_2", ":agent_no", ":troop_no")])]],

###
 ["tab_shield_tauria_a", "Plain Shield",   [("tableau_shield_sarranid_a" ,0)], itp_merchandise|itp_type_shield|itp_craftable|itp_wooden_parry, itcf_carry_kite_shield,
 56 , weight(3)|hit_points(280)|body_armor(4)|spd_rtng(90)|shield_width(40)|shield_height(55),imodbits_shield,
  [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_sarranid_shield_a", ":agent_no", ":troop_no")])]],  
 ["tab_shield_tauria_b", "Infantry Shield",   [("tableau_shield_sarranid_b" ,0)], itp_merchandise|itp_type_shield|itp_craftable|itp_wooden_parry, itcf_carry_board_shield,
 174 , weight(3)|hit_points(360)|body_armor(8)|spd_rtng(90)|shield_width(45)|shield_height(60),imodbits_shield,
  [(ti_on_init_item,[(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_sarranid_shield_b", ":agent_no", ":troop_no")])]],  
 ["tab_shield_tauria_c", "Guard Shield",   [("tableau_shield_sarranid_c" ,0)], itp_merchandise|itp_type_shield|itp_craftable|itp_wooden_parry, itcf_carry_board_shield,
 360 , weight(3)|hit_points(430)|body_armor(10)|spd_rtng(88)|shield_width(40)|shield_height(50),imodbits_shield,
  [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_sarranid_shield_c", ":agent_no", ":troop_no")])]], 

["player_tab_footman_shield","Plain Footman Shield", [("Player_Shield_Veteran_Heraldic", 0)], itp_merchandise|itp_type_shield|itp_craftable|itp_wooden_parry, itcf_carry_kite_shield,120, weight(2)|abundance(100)|body_armor(4)|hit_points(140)|spd_rtng(80)|shield_height(110)|shield_width(38), imodbit_reinforced, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_player_shield_a", ":agent_no", ":troop_no")])]],
["player_tab_footman_shield_reinforced","Reinforced Footman Shield", [("Player_Shield_Veteran_Heraldic_Reinforced", 0)], itp_merchandise|itp_type_shield|itp_craftable|itp_wooden_parry, itcf_carry_kite_shield,120, weight(2)|abundance(100)|body_armor(9)|hit_points(290)|spd_rtng(80)|shield_height(110)|shield_width(38), imodbit_reinforced, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_player_shield_b", ":agent_no", ":troop_no")])]],
###

["player_oval_shield_a","Oval Shield", [("Player_Shield_Oval_A", 0)], itp_type_shield|itp_craftable|itp_wooden_parry, itcf_carry_round_shield,140, weight(2)|abundance(100)|body_armor(1)|hit_points(165)|spd_rtng(100)|shield_width(36), imodbit_reinforced, [], []],
["player_oval_shield_b","Oval Shield", [("Player_Shield_Oval_B", 0)], itp_type_shield|itp_craftable|itp_wooden_parry, itcf_carry_round_shield,140, weight(2)|abundance(100)|body_armor(1)|hit_points(165)|spd_rtng(100)|shield_width(36), imodbit_reinforced, [], []],

["player_footman_shield_a","Footman Shield", [("Player_Shield_Veteran_A", 0)], itp_type_shield|itp_craftable|itp_wooden_parry, itcf_carry_kite_shield,845, weight(2)|abundance(100)|body_armor(25)|hit_points(370)|spd_rtng(80)|shield_height(110)|shield_width(38), imodbit_reinforced, [], []],
["player_footman_shield_b","Footman Shield", [("Player_Shield_Veteran_B", 0)], itp_type_shield|itp_craftable|itp_wooden_parry, itcf_carry_kite_shield,845, weight(2)|abundance(100)|body_armor(25)|hit_points(370)|spd_rtng(80)|shield_height(110)|shield_width(38), imodbit_reinforced, [], []],
["player_footman_shield_c","Footman Shield", [("Player_Shield_Veteran_C", 0)], itp_type_shield|itp_craftable|itp_wooden_parry, itcf_carry_kite_shield,845, weight(2)|abundance(100)|body_armor(25)|hit_points(370)|spd_rtng(80)|shield_height(110)|shield_width(38), imodbit_reinforced, [], []],
["player_footman_shield_d","Footman Shield", [("Player_Shield_Veteran_D", 0)], itp_type_shield|itp_craftable|itp_wooden_parry, itcf_carry_kite_shield,845, weight(2)|abundance(100)|body_armor(25)|hit_points(370)|spd_rtng(80)|shield_height(110)|shield_width(38), imodbit_reinforced, [], []],

["player_footman_shield_kite_a","Footman Shield", [("Player_Shield_Kite_A", 0)], itp_type_shield|itp_craftable|itp_wooden_parry, itcf_carry_kite_shield,875, weight(2)|abundance(100)|body_armor(27)|hit_points(395)|spd_rtng(80)|shield_height(115)|shield_width(38), imodbit_reinforced, [], []],
["player_footman_shield_kite_b","Footman Shield", [("Player_Shield_Kite_B", 0)], itp_type_shield|itp_craftable|itp_wooden_parry, itcf_carry_kite_shield,875, weight(2)|abundance(100)|body_armor(27)|hit_points(395)|spd_rtng(80)|shield_height(115)|shield_width(38), imodbit_reinforced, [], []],
["player_footman_shield_kite_c","Footman Shield", [("Player_Shield_Kite_C", 0)], itp_type_shield|itp_craftable|itp_wooden_parry, itcf_carry_kite_shield,875, weight(2)|abundance(100)|body_armor(27)|hit_points(395)|spd_rtng(80)|shield_height(115)|shield_width(38), imodbit_reinforced, [], []],
["player_footman_shield_kite_d","Footman Shield", [("Player_Shield_Kite_D", 0)], itp_type_shield|itp_craftable|itp_wooden_parry, itcf_carry_kite_shield,875, weight(2)|abundance(100)|body_armor(27)|hit_points(395)|spd_rtng(80)|shield_height(115)|shield_width(38), imodbit_reinforced, [], []],

["player_oval_eastern_shield_a","Eastern Oval Shield", [("Player_Shield_Oval_Eastern_A", 0)], itp_type_shield|itp_craftable|itp_wooden_parry, itcf_carry_round_shield,530, weight(2)|abundance(100)|body_armor(20)|hit_points(165)|spd_rtng(96)|shield_height(70)|shield_width(36), imodbit_reinforced|imodbit_lordly, [], []],
["player_oval_eastern_shield_b","Eastern Oval Shield", [("Player_Shield_Oval_Eastern_B", 0)], itp_type_shield|itp_craftable|itp_wooden_parry, itcf_carry_round_shield,530, weight(2)|abundance(100)|body_armor(20)|hit_points(165)|spd_rtng(96)|shield_height(70)|shield_width(36), imodbit_reinforced|imodbit_lordly, [], []],

["swadia_oval_shield_1","Oval Shield", [("shields_archer_tripoli_b", 0),("shields_archer_tripoli_d", imodbit_reinforced)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,70, weight(2)|abundance(100)|body_armor(1)|hit_points(165)|spd_rtng(100)|shield_width(36), imodbit_reinforced, [], [fac_kingdom_1]],
["swadia_oval_shield_2","Oval Shield", [("shields_archer_tripoli_a", 0),("shields_archer_tripoli_c", imodbit_reinforced)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,70, weight(2)|abundance(100)|body_armor(1)|hit_points(165)|spd_rtng(100)|shield_width(36), imodbit_reinforced, [], [fac_kingdom_1]],
["swadia_kite_shield_1","Kite Shield", [("tripoli_shield_a", 0),("tripoli_shield_b", imodbit_reinforced),("tripoli_shield_e", imodbit_lordly)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield,205, weight(2)|abundance(100)|body_armor(14)|hit_points(180)|spd_rtng(103)|shield_height(50)|shield_width(30), imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_1]],
["swadia_kite_shield_2","Kite Shield", [("tripoli_shield_c", 0),("tripoli_shield_d", imodbit_reinforced),("tripoli_shield_e", imodbit_lordly)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield,205, weight(2)|abundance(100)|body_armor(14)|hit_points(180)|spd_rtng(103)|shield_height(50)|shield_width(30), imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_1]],
["swadia_footman_shield_1","Footman Shield", [("shield_veteran_tripoli_b", 0),("shield_veteran_tripoli_c", imodbit_reinforced),("shield_veteran_tripoli_d", imodbit_lordly)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield,700, weight(2)|abundance(100)|body_armor(25)|hit_points(370)|spd_rtng(80)|shield_height(110)|shield_width(38), imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_1]],
["swadia_footman_shield_2","Footman Shield", [("shield_veteran_tripoli_a", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield,700, weight(2)|abundance(100)|body_armor(25)|hit_points(370)|spd_rtng(80)|shield_height(110)|shield_width(38), imodbit_reinforced, [], [fac_kingdom_1]],
["swadia_footman_shield_3","Footman Shield", [("shield_veteran_tripoli_e", 0),("shield_veteran_tripoli_g", imodbit_reinforced)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield,700, weight(2)|abundance(100)|body_armor(25)|hit_points(370)|spd_rtng(80)|shield_height(110)|shield_width(38), imodbit_reinforced, [], [fac_kingdom_1]],
["swadia_footman_shield_4","Footman Shield", [("shield_veteran_tripoli_f", 0),("shield_veteran_tripoli_h", imodbit_reinforced)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield,700, weight(2)|abundance(100)|body_armor(25)|hit_points(370)|spd_rtng(80)|shield_height(110)|shield_width(38), imodbit_reinforced, [], [fac_kingdom_1]],
["swadia_heater_shield_1","Heater Shield", [("shield_knight_tripoli_a", 0),("shield_knight_tripoli_c", imodbit_reinforced)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield,500, weight(3)|abundance(100)|body_armor(17)|hit_points(300)|spd_rtng(98)|shield_height(50)|shield_width(32), imodbit_reinforced, [], [fac_kingdom_1]],
["swadia_heater_shield_2","Heater Shield", [("shield_knight_tripoli_b", 0),("shield_knight_tripoli_d", imodbit_reinforced)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield,500, weight(3)|abundance(100)|body_armor(17)|hit_points(300)|spd_rtng(98)|shield_height(50)|shield_width(32), imodbit_reinforced, [], [fac_kingdom_1]],

["eastern_round_shield_a","Eastern Round Shield", [("shield_vostoka_a", 0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,138, weight(2)|abundance(100)|body_armor(5)|hit_points(165)|spd_rtng(96)|shield_height(70)|shield_width(36), imodbits_none, []],
["eastern_round_shield_b","Eastern Round Shield", [("shield_vostoka_b", 0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,138, weight(2)|abundance(100)|body_armor(5)|hit_points(165)|spd_rtng(96)|shield_height(70)|shield_width(36), imodbits_none, []],
["eastern_round_shield_c","Eastern Round Shield", [("shield_vostoka_c", 0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,138, weight(2)|abundance(100)|body_armor(5)|hit_points(165)|spd_rtng(96)|shield_height(70)|shield_width(36), imodbits_none, []],

["solarian_oval_shield_a","Solarian Oval Shield", [("saracin_shield_a", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,330, weight(2)|abundance(100)|body_armor(17)|hit_points(165)|spd_rtng(96)|shield_height(70)|shield_width(36), imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_6]],
["solarian_oval_shield_b","Solarian Oval Shield", [("saracin_shield_b", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,330, weight(2)|abundance(100)|body_armor(17)|hit_points(165)|spd_rtng(96)|shield_height(70)|shield_width(36), imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_6]],
["solarian_oval_shield_c","Solarian Oval Shield", [("saracin_shield_f", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,330, weight(2)|abundance(100)|body_armor(17)|hit_points(165)|spd_rtng(96)|shield_height(70)|shield_width(36), imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_6]],
["solarian_oval_shield_d","Solarian Oval Shield", [("saracin_shield_m", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,330, weight(2)|abundance(100)|body_armor(17)|hit_points(165)|spd_rtng(96)|shield_height(70)|shield_width(36), imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_6]],
["solarian_oval_shield_e","Solarian Oval Shield", [("saracin_shield_n", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,330, weight(2)|abundance(100)|body_armor(17)|hit_points(165)|spd_rtng(96)|shield_height(70)|shield_width(36), imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_6]],
["solarian_oval_shield_f","Solarian Oval Shield", [("securiti_caravan_crusader_shield", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,330, weight(2)|abundance(100)|body_armor(17)|hit_points(165)|spd_rtng(96)|shield_height(70)|shield_width(36), imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_6]],

["solarian_round_shield_a","Solarian Round Shield", [("saracin_shield_c", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,295, weight(2)|abundance(100)|body_armor(5)|hit_points(165)|spd_rtng(96)|shield_height(70)|shield_width(36), imodbit_reinforced, [], [fac_kingdom_6]],
["solarian_round_shield_b","Solarian Round Shield", [("saracin_shield_d", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,295, weight(2)|abundance(100)|body_armor(5)|hit_points(165)|spd_rtng(96)|shield_height(70)|shield_width(36), imodbit_reinforced, [], [fac_kingdom_6]],
["solarian_round_shield_c","Solarian Round Shield", [("saracin_shield_e", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,295, weight(2)|abundance(100)|body_armor(5)|hit_points(165)|spd_rtng(96)|shield_height(70)|shield_width(36), imodbit_reinforced, [], [fac_kingdom_6]],
["solarian_round_shield_d","Solarian Round Shield", [("saracin_shield_g", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,295, weight(2)|abundance(100)|body_armor(5)|hit_points(165)|spd_rtng(96)|shield_height(70)|shield_width(36), imodbit_reinforced, [], [fac_kingdom_6]],
["solarian_round_shield_e","Solarian Round Shield", [("saracin_shield_h", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,295, weight(2)|abundance(100)|body_armor(5)|hit_points(165)|spd_rtng(96)|shield_height(70)|shield_width(36), imodbit_reinforced, [], [fac_kingdom_6]],
["solarian_round_shield_f","Solarian Round Shield", [("saracin_shield_k", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,295, weight(2)|abundance(100)|body_armor(5)|hit_points(165)|spd_rtng(96)|shield_height(70)|shield_width(36), imodbit_reinforced, [], [fac_kingdom_6]],
["solarian_round_shield_g","Solarian Round Shield", [("saracin_shield_k", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,295, weight(2)|abundance(100)|body_armor(5)|hit_points(165)|spd_rtng(96)|shield_height(70)|shield_width(36), imodbit_reinforced, [], [fac_kingdom_6]],
 #RANGED


#TODO:
["darts",         "Darts", [("dart_b",0),("dart_b_bag", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_javelin|itcf_carry_quiver_right_vertical|itcf_show_holster_when_drawn,
155 , weight(4)|difficulty(1)|spd_rtng(95) | shoot_speed(28) | thrust_damage(22 ,  pierce)|max_ammo(7)|weapon_length(32),imodbits_thrown ],
["war_darts",         "War Darts", [("dart_a",0),("dart_a_bag", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 
285 , weight(5)|difficulty(1)|spd_rtng(93) | shoot_speed(27) | thrust_damage(25 ,  pierce)|max_ammo(7)|weapon_length(45),imodbits_thrown ],

["javelin",         "Javelins", [("javelin",0),("javelins_quiver_new", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 
300, weight(4)|difficulty(1)|spd_rtng(91) | shoot_speed(25) | thrust_damage(34 ,  pierce)|max_ammo(5)|weapon_length(75),imodbits_thrown ],
["javelin_melee",         "Javelin", [("javelin",0)], itp_type_polearm|itp_primary|itp_wooden_parry , itc_staff, 
300, weight(1)|difficulty(0)|spd_rtng(95) |swing_damage(12, cut)| thrust_damage(14,  pierce)|weapon_length(75),imodbits_polearm ],

["throwing_spears",         "Throwing Spears", [("jarid_new_b",0),("jarid_new_b_bag", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 
525 , weight(3)|difficulty(2)|spd_rtng(87) | shoot_speed(22) | thrust_damage(44 ,  pierce)|max_ammo(4)|weapon_length(65),imodbits_thrown ],
["throwing_spear_melee",         "Throwing Spear", [("jarid_new_b",0),("javelins_quiver", ixmesh_carry)],itp_type_polearm|itp_primary|itp_wooden_parry , itc_staff, 
525 , weight(1)|difficulty(1)|spd_rtng(91) | swing_damage(18, cut) | thrust_damage(23 ,  pierce)|weapon_length(75),imodbits_thrown ],

["jarid",         "Jarids", [("jarid_new",0),("jarid_quiver", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 
560 , weight(2.75)|difficulty(2)|spd_rtng(89) | shoot_speed(24) | thrust_damage(45 ,  pierce)|max_ammo(4)|weapon_length(65),imodbits_thrown ],
["jarid_melee",         "Jarid", [("jarid_new",0),("jarid_quiver", ixmesh_carry)], itp_type_polearm|itp_primary|itp_wooden_parry , itc_staff,
560 , weight(1)|difficulty(2)|spd_rtng(93) | swing_damage(16, cut) | thrust_damage(20 ,  pierce)|weapon_length(65),imodbits_thrown ],


#TODO:
#TODO: Heavy throwing Spear
["stones",         "Stones", [("throwing_stone",0)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_stone, 1 , weight(4)|difficulty(0)|spd_rtng(97) | shoot_speed(30) | thrust_damage(11 ,  blunt)|max_ammo(18)|weapon_length(8),imodbit_large_bag ],

["throwing_knives", "Throwing Knives", [("throwing_knife",0)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_knife, 76 , weight(2.5)|difficulty(0)|spd_rtng(121) | shoot_speed(25) | thrust_damage(19 ,  cut)|max_ammo(14)|weapon_length(0),imodbits_thrown ],
["throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_knife, 193 , weight(2.5)|difficulty(0)|spd_rtng(110) | shoot_speed(24) | thrust_damage(25 ,  cut)|max_ammo(13)|weapon_length(0),imodbits_thrown ],

["throwing_hammers", "Throwing Hammers", [("luc_throwing_hammer",0)], itp_type_thrown |itp_merchandise|itp_primary,itcf_throw_axe,406, weight(5)|difficulty(2)|spd_rtng(99) | shoot_speed(18) | thrust_damage(35,blunt)|max_ammo(5)|weapon_length(53),imodbits_thrown_minus_heavy ],

#TODO: Light Trowing axe, Heavy Throwing Axe
["light_throwing_axes", "Throwing Hatchets", [("luc_hatchet_g",0),("luc_hatchet_g_inv",ixmesh_inventory)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee,itcf_throw_axe,
360, weight(5)|difficulty(2)|spd_rtng(99) | shoot_speed(18) | thrust_damage(35,cut)|max_ammo(4)|weapon_length(53),imodbits_thrown_minus_heavy ],
["light_throwing_axes_melee", "Throwing Hatchets", [("luc_hatchet_g",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar,
360, weight(1)|difficulty(2)|spd_rtng(99)|weapon_length(53)| swing_damage(26,cut),imodbits_thrown_minus_heavy ],
["throwing_axes", "Throwing Axes", [("throwing_axe_a",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee,itcf_throw_axe,
490, weight(5)|difficulty(3)|spd_rtng(98) | shoot_speed(18) | thrust_damage(39,cut)|max_ammo(4)|weapon_length(53),imodbits_thrown_minus_heavy ],
["throwing_axes_melee", "Throwing Axe", [("throwing_axe_a",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar,
490, weight(1)|difficulty(3)|spd_rtng(98) | swing_damage(29,cut)|weapon_length(53),imodbits_thrown_minus_heavy ],
["heavy_throwing_axes", "Heavy Throwing Axes", [("throwing_axe_b",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee,itcf_throw_axe,
620, weight(5)|difficulty(4)|spd_rtng(97) | shoot_speed(18) | thrust_damage(44,cut)|max_ammo(4)|weapon_length(53),imodbits_thrown_minus_heavy ],
["heavy_throwing_axes_melee", "Heavy Throwing Axe", [("throwing_axe_b",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar,
620, weight(1)|difficulty(4)|spd_rtng(97) | swing_damage(32,cut)|weapon_length(53),imodbits_thrown_minus_heavy ],



["hunting_bow",         "Hunting Bow", [("hunting_bow",0),("hunting_bow_carry",ixmesh_carry)],itp_type_bow |itp_merchandise|itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bow_back, 
17 , weight(1)|difficulty(0)|spd_rtng(100) | shoot_speed(52) | thrust_damage(15 ,  pierce),imodbits_bow ],
["short_bow",         "Short Bow", [("short_bow",0),("short_bow_carry",ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 
58 , weight(1)|difficulty(1)|spd_rtng(97) | shoot_speed(55) | thrust_damage(18 ,  pierce  ),imodbits_bow ],
["nomad_bow",         "Nomad Bow", [("nomad_bow",0),("nomad_bow_case", ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 
164 , weight(1.25)|difficulty(2)|spd_rtng(94) | shoot_speed(56) | thrust_damage(20 ,  pierce),imodbits_bow ],
["long_bow",         "Long Bow", [("long_bow",0),("long_bow_carry",ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 
145 , weight(1.75)|difficulty(3)|spd_rtng(79) | shoot_speed(56) | thrust_damage(22 ,  pierce),imodbits_bow ],
["khergit_bow",         "Khergit Bow", [("khergit_bow",0),("khergit_bow_case", ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 
269 , weight(1.25)|difficulty(3)|spd_rtng(90) | shoot_speed(57) | thrust_damage(21 ,pierce),imodbits_bow ],
["strong_bow",         "Strong Bow", [("strong_bow",0),("strong_bow_case", ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 
437 , weight(1.25)|difficulty(3)|spd_rtng(88) | shoot_speed(58) | thrust_damage(23 ,pierce),imodbit_cracked | imodbit_bent | imodbit_masterwork ],
["war_bow",         "War Bow", [("war_bow",0),("war_bow_carry",ixmesh_carry)],itp_type_bow|itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 
728 , weight(1.5)|difficulty(4)|spd_rtng(84) | shoot_speed(59) | thrust_damage(25 ,pierce),imodbits_bow ],
["hunting_crossbow", "Hunting Crossbow", [("crusaders_crossbows_a",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 
22 , weight(2.25)|difficulty(0)|spd_rtng(47) | shoot_speed(50) | thrust_damage(37 ,  pierce)|max_ammo(1),imodbits_crossbow ],
["light_crossbow", "Light Crossbow", [("crusaders_crossbows_b",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 
67 , weight(2.5)|difficulty(8)|spd_rtng(45) | shoot_speed(59) | thrust_damage(44 ,  pierce)|max_ammo(1),imodbits_crossbow ],
["crossbow",         "Crossbow",         [("crusaders_crossbows_a",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 
182 , weight(3)|difficulty(8)|spd_rtng(43) | shoot_speed(66) | thrust_damage(49,pierce)|max_ammo(1),imodbits_crossbow ],
["heavy_crossbow", "Heavy Crossbow", [("crusaders_crossbows_c",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 
349 , weight(3.5)|difficulty(9)|spd_rtng(41) | shoot_speed(68) | thrust_damage(58 ,pierce)|max_ammo(1),imodbits_crossbow ],
["sniper_crossbow", "Siege Crossbow", [("crusaders_crossbows_c",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 
683 , weight(3.75)|difficulty(10)|spd_rtng(37) | shoot_speed(70) | thrust_damage(63 ,pierce)|max_ammo(1),imodbits_crossbow ],

["pistol_a", "Flintlock Pistol", [("Pistol_Pistolier_A_01",0)], itp_type_pistol |itp_merchandise|itp_primary ,itcf_shoot_pistol|itcf_reload_pistol|itcf_carry_pistol_front_left, 1455 , weight(2.5)|difficulty(0)|spd_rtng(38) | shoot_speed(160) | thrust_damage(66 ,pierce)|max_ammo(1)|accuracy(65),imodbits_none,[(ti_on_weapon_attack, [(play_sound,"snd_pistol_shot"),(position_move_x, pos1,27),(position_move_y, pos1,36),(particle_system_burst, "psys_pistol_smoke", pos1, 15)])]],
["pistol_b", "Flintlock Pistol", [("Pistol_Pistolier_B_01",0)], itp_type_pistol |itp_merchandise|itp_primary ,itcf_shoot_pistol|itcf_reload_pistol|itcf_carry_pistol_front_left, 891 , weight(2.5)|difficulty(0)|spd_rtng(38) | shoot_speed(160) | thrust_damage(55 ,pierce)|max_ammo(1)|accuracy(65),imodbits_none,[(ti_on_weapon_attack, [(play_sound,"snd_pistol_shot"),(position_move_x, pos1,27),(position_move_y, pos1,36),(particle_system_burst, "psys_pistol_smoke", pos1, 15)])]],

["light_rifle_a", "Flintlock Rifle", [("Gun_Empire_Light_Muscket_A_P1_01",0)], itp_type_musket |itp_merchandise|itp_primary ,itcf_shoot_musket|itcf_reload_musket|itcf_carry_crossbow_back, 891 , weight(2.5)|difficulty(0)|spd_rtng(38) | shoot_speed(160) | thrust_damage(55 ,pierce)|max_ammo(1)|accuracy(77),imodbits_none,[(ti_on_weapon_attack, [(play_sound,"snd_pistol_shot"),(position_move_x, pos1,27),(position_move_y, pos1,36),(particle_system_burst, "psys_pistol_smoke", pos1, 15)])]],
["light_rifle_b", "Rough Flintlock Rifle", [("Gun_Empire_Light_Muscket_B_P1_01",0)], itp_type_musket |itp_merchandise|itp_primary ,itcf_shoot_musket|itcf_reload_musket|itcf_carry_crossbow_back, 891 , weight(4.5)|difficulty(0)|spd_rtng(55) | shoot_speed(160) | thrust_damage(55 ,pierce)|max_ammo(1)|accuracy(50),imodbits_none,[(ti_on_weapon_attack, [(play_sound,"snd_pistol_shot"),(position_move_x, pos1,27),(position_move_y, pos1,36),(particle_system_burst, "psys_pistol_smoke", pos1, 15)])]],
["light_rifle_c", "Hunting Rifle", [("Gun_Empire_Light_Muscket_C_P1_01",0)], itp_type_musket |itp_merchandise|itp_primary ,itcf_shoot_musket|itcf_reload_musket|itcf_carry_crossbow_back, 891 , weight(2.5)|difficulty(0)|spd_rtng(55) | shoot_speed(160) | thrust_damage(55 ,pierce)|max_ammo(1)|accuracy(70),imodbits_none,[(ti_on_weapon_attack, [(play_sound,"snd_pistol_shot"),(position_move_x, pos1,27),(position_move_y, pos1,36),(particle_system_burst, "psys_pistol_smoke", pos1, 15)])]],
["light_rifle_d", "Short Barrel Rifle", [("Gun_Empire_Light_Muscket_C_P1_01",0)], itp_type_musket |itp_merchandise|itp_primary ,itcf_shoot_musket|itcf_reload_musket|itcf_carry_crossbow_back, 891 , weight(2.5)|difficulty(0)|spd_rtng(55) | shoot_speed(160) | thrust_damage(55 ,pierce)|max_ammo(1)|accuracy(71),imodbits_none,[(ti_on_weapon_attack, [(play_sound,"snd_pistol_shot"),(position_move_x, pos1,27),(position_move_y, pos1,36),(particle_system_burst, "psys_pistol_smoke", pos1, 15)])]],

["medium_rifle_a", "Military Rifle", [("Gun_Empire_Medium_Muscket_A_P1_01",0)], itp_type_musket |itp_merchandise|itp_primary ,itcf_shoot_musket|itcf_reload_musket|itcf_carry_crossbow_back, 2319 , weight(4.5)|difficulty(0)|spd_rtng(55) | shoot_speed(160) | thrust_damage(67 ,pierce)|max_ammo(1)|accuracy(60),imodbits_none,[(ti_on_weapon_attack, [(play_sound,"snd_pistol_shot"),(position_move_x, pos1,27),(position_move_y, pos1,36),(particle_system_burst, "psys_pistol_smoke", pos1, 15)])]],
["medium_rifle_b", "Great Barrel Rifle", [("Gun_Empire_Medium_Muscket_B_P1_01",0)], itp_type_musket |itp_merchandise|itp_primary ,itcf_shoot_musket|itcf_reload_musket|itcf_carry_crossbow_back, 891 , weight(4.5)|difficulty(0)|spd_rtng(55) | shoot_speed(160) | thrust_damage(73 ,pierce)|max_ammo(1)|accuracy(80),imodbits_none,[(ti_on_weapon_attack, [(play_sound,"snd_pistol_shot"),(position_move_x, pos1,27),(position_move_y, pos1,36),(particle_system_burst, "psys_pistol_smoke", pos1, 15)])]],
["medium_rifle_c", "Rifle", [("Gun_Empire_Medium_Muscket_C_P1_01",0)], itp_type_musket |itp_merchandise|itp_primary ,itcf_shoot_musket|itcf_reload_musket|itcf_carry_crossbow_back, 891 , weight(4.5)|difficulty(0)|spd_rtng(55) | shoot_speed(160) | thrust_damage(55 ,pierce)|max_ammo(1)|accuracy(50),imodbits_none,[(ti_on_weapon_attack, [(play_sound,"snd_pistol_shot"),(position_move_x, pos1,27),(position_move_y, pos1,36),(particle_system_burst, "psys_pistol_smoke", pos1, 15)])]],
["medium_rifle_d", "Rifle", [("Gun_Empire_Medium_Muscket_D_P1_01",0)], itp_type_musket |itp_merchandise|itp_primary ,itcf_shoot_musket|itcf_reload_musket|itcf_carry_crossbow_back, 891 , weight(4.5)|difficulty(0)|spd_rtng(55) | shoot_speed(160) | thrust_damage(55 ,pierce)|max_ammo(1)|accuracy(50),imodbits_none,[(ti_on_weapon_attack, [(play_sound,"snd_pistol_shot"),(position_move_x, pos1,27),(position_move_y, pos1,36),(particle_system_burst, "psys_pistol_smoke", pos1, 15)])]],
["medium_rifle_e", "Two Barrel Rifle", [("Gun_Empire_Medium_Muscket_E_P1_01",0)], itp_type_musket |itp_merchandise|itp_primary ,itcf_shoot_musket|itcf_reload_musket|itcf_carry_crossbow_back, 891 , weight(4.5)|difficulty(0)|spd_rtng(55) | shoot_speed(160) | thrust_damage(55 ,pierce)|max_ammo(2)|accuracy(50),imodbits_none,[(ti_on_weapon_attack, [(play_sound,"snd_pistol_shot"),(position_move_x, pos1,27),(position_move_y, pos1,36),(particle_system_burst, "psys_pistol_smoke", pos1, 15)])]],
["medium_rifle_f", "Rifle", [("Gun_Empire_Medium_Muscket_F_P1_01",0)], itp_type_musket |itp_merchandise|itp_primary ,itcf_shoot_musket|itcf_reload_musket|itcf_carry_crossbow_back, 891 , weight(4.5)|difficulty(0)|spd_rtng(55) | shoot_speed(160) | thrust_damage(55 ,pierce)|max_ammo(1)|accuracy(50),imodbits_none,[(ti_on_weapon_attack, [(play_sound,"snd_pistol_shot"),(position_move_x, pos1,27),(position_move_y, pos1,36),(particle_system_burst, "psys_pistol_smoke", pos1, 15)])]],

["heavy_rifle_a", "Rifle", [("Gun_Empire_Heavy_Muscket_A_P1_01",0)], itp_type_musket |itp_merchandise|itp_primary ,itcf_shoot_musket|itcf_reload_musket|itcf_carry_crossbow_back, 891 , weight(4.5)|difficulty(0)|spd_rtng(55) | shoot_speed(160) | thrust_damage(55 ,pierce)|max_ammo(1)|accuracy(50),imodbits_none,[(ti_on_weapon_attack, [(play_sound,"snd_pistol_shot"),(position_move_x, pos1,27),(position_move_y, pos1,36),(particle_system_burst, "psys_pistol_smoke", pos1, 15)])]],
["heavy_rifle_b", "Rifle", [("Gun_Empire_Heavy_Muscket_B_P1_01",0)], itp_type_musket |itp_merchandise|itp_primary ,itcf_shoot_musket|itcf_reload_musket|itcf_carry_crossbow_back, 891 , weight(4.5)|difficulty(0)|spd_rtng(55) | shoot_speed(160) | thrust_damage(55 ,pierce)|max_ammo(2)|accuracy(50),imodbits_none,[(ti_on_weapon_attack, [(play_sound,"snd_pistol_shot"),(position_move_x, pos1,27),(position_move_y, pos1,36),(particle_system_burst, "psys_pistol_smoke", pos1, 15)])]],
["heavy_rifle_c", "Rifle", [("Gun_Empire_Heavy_Muscket_C_P1_01",0)], itp_type_musket |itp_merchandise|itp_primary ,itcf_shoot_musket|itcf_reload_musket|itcf_carry_crossbow_back, 891 , weight(4.5)|difficulty(0)|spd_rtng(55) | shoot_speed(160) | thrust_damage(55 ,pierce)|max_ammo(1)|accuracy(50),imodbits_none,[(ti_on_weapon_attack, [(play_sound,"snd_pistol_shot"),(position_move_x, pos1,27),(position_move_y, pos1,36),(particle_system_burst, "psys_pistol_smoke", pos1, 15)])]],
["heavy_rifle_d", "Rifle", [("Gun_Empire_Heavy_Muscket_D_P1_01",0)], itp_type_musket |itp_merchandise|itp_primary ,itcf_shoot_musket|itcf_reload_musket|itcf_carry_crossbow_back, 891 , weight(4.5)|difficulty(0)|spd_rtng(55) | shoot_speed(160) | thrust_damage(55 ,pierce)|max_ammo(1)|accuracy(50),imodbits_none,[(ti_on_weapon_attack, [(play_sound,"snd_pistol_shot"),(position_move_x, pos1,27),(position_move_y, pos1,36),(particle_system_burst, "psys_pistol_smoke", pos1, 15)])]],
["heavy_rifle_e", "Rifle", [("Gun_Empire_Heavy_Muscket_E_P1_01",0)], itp_type_musket |itp_merchandise|itp_primary ,itcf_shoot_musket|itcf_reload_musket|itcf_carry_crossbow_back, 891 , weight(4.5)|difficulty(0)|spd_rtng(55) | shoot_speed(160) | thrust_damage(55 ,pierce)|max_ammo(1)|accuracy(50),imodbits_none,[(ti_on_weapon_attack, [(play_sound,"snd_pistol_shot"),(position_move_x, pos1,27),(position_move_y, pos1,36),(particle_system_burst, "psys_pistol_smoke", pos1, 15)])]],
["heavy_rifle_f", "Rifle", [("Gun_Empire_Heavy_Muscket_F_P1_01",0)], itp_type_musket |itp_merchandise|itp_primary ,itcf_shoot_musket|itcf_reload_musket|itcf_carry_crossbow_back, 891 , weight(4.5)|difficulty(0)|spd_rtng(55) | shoot_speed(160) | thrust_damage(55 ,pierce)|max_ammo(2)|accuracy(50),imodbits_none,[(ti_on_weapon_attack, [(play_sound,"snd_pistol_shot"),(position_move_x, pos1,27),(position_move_y, pos1,36),(particle_system_burst, "psys_pistol_smoke", pos1, 15)])]],


["torch",         "Torch", [("club",0)], itp_type_one_handed_wpn|itp_primary, itc_scimitar, 11 , weight(2.5)|difficulty(0)|spd_rtng(95) | weapon_length(95)|swing_damage(11 , blunt) | thrust_damage(0 ,  pierce),imodbits_none,
 [(ti_on_init_item, [(set_position_delta,0,60,0),(particle_system_add_new, "psys_torch_fire"),(particle_system_add_new, "psys_torch_smoke"),(set_current_color,150, 130, 70),(add_point_light, 10, 30),
])]],

["lyre",         "Lyre", [("lyre",0)], itp_type_shield|itp_wooden_parry|itp_civilian, itcf_carry_bow_back,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(90),0 ],
["lute",         "Lute", [("lute",0)], itp_type_shield|itp_wooden_parry|itp_civilian, itcf_carry_bow_back,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(90),0 ],

##["short_sword", "Short Sword",
## [("sword_norman",0),("sword_norman_scabbard", ixmesh_carry),("sword_norman_rusty",imodbit_rusty),("sword_norman_rusty_scabbard", ixmesh_carry|imodbit_rusty)],
## itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 183 , weight(1.25)|difficulty(0)|spd_rtng(103) | weapon_length(75)|swing_damage(25 , cut) | thrust_damage(19 ,  pierce),imodbits_sword ],

["strange_armor",  "Strange Armor", [("samurai_armor",0)], itp_type_body_armor  |itp_covers_legs ,0, 1259 , weight(18)|abundance(100)|head_armor(0)|body_armor(38)|leg_armor(19)|difficulty(7) ,imodbits_armor ],
["strange_boots",  "Strange Boots", [("samurai_boots",0)], itp_type_foot_armor | itp_attach_armature,0, 465 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(21)|difficulty(0) ,imodbits_cloth ],
["strange_helmet", "Strange Helmet", [("samurai_helmet",0)], itp_type_head_armor   ,0, 824 , weight(2)|abundance(100)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["strange_sword", "Strange Sword", [("katana",0),("katana_scabbard",ixmesh_carry)], itp_type_two_handed_wpn| itp_primary, itc_bastardsword|itcf_carry_katana|itcf_show_holster_when_drawn, 679 , weight(2.0)|difficulty(9)|spd_rtng(108) | weapon_length(95)|swing_damage(32 , cut) | thrust_damage(18 ,  pierce),imodbits_sword ],
["strange_great_sword",  "Strange Great Sword", [("no_dachi",0),("no_dachi_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back|itcf_show_holster_when_drawn, 920 , weight(3.5)|difficulty(11)|spd_rtng(92) | weapon_length(125)|swing_damage(38 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["strange_short_sword", "Strange Short Sword", [("wakizashi",0),("wakizashi_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_wakizashi|itcf_show_holster_when_drawn, 321 , weight(1.25)|difficulty(0)|spd_rtng(108) | weapon_length(65)|swing_damage(25 , cut) | thrust_damage(19 ,  pierce),imodbits_sword ],
["court_dress", "Court Dress", [("court_dress",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
["khergit_guard_armor", "Khergit Guard Armor", [("lamellar_armor_a",0)], itp_type_body_armor|itp_covers_legs   ,0, 
3048 , weight(25)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(18)|difficulty(0) ,imodbits_armor ],
#["leather_steppe_cap_c", "Leather Steppe Cap", [("leather_steppe_cap_c",0)], itp_type_head_armor   ,0, 51 , weight(2)|abundance(100)|head_armor(18)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["felt_steppe_cap", "Felt Steppe Cap", [("felt_steppe_cap",0)], itp_type_head_armor   ,0, 237 , weight(2)|abundance(100)|head_armor(16)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["khergit_war_helmet", "Khergit War Helmet", [("tattered_steppe_cap_a_new",0)], itp_type_head_armor | itp_merchandise   ,0, 200 , weight(2)|abundance(100)|head_armor(31)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["khergit_helmet", "Khergit Helmet", [("khergit_guard_helmet",0)], itp_type_head_armor   ,0, 361 , weight(2)|abundance(100)|head_armor(33)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
#["khergit_sword", "Khergit Sword", [("khergit_sword",0),("khergit_sword_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 183 , weight(1.25)|difficulty(0)|spd_rtng(100) | weapon_length(97)|swing_damage(23 , cut) | thrust_damage(14 ,  pierce),imodbits_sword ],
["khergit_guard_helmet", "Khergit Guard Helmet", [("lamellar_helmet_a",0)], itp_type_head_armor |itp_merchandise   ,0, 433 , weight(2)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["khergit_cavalry_helmet", "Khergit Cavalry Helmet", [("lamellar_helmet_b",0)], itp_type_head_armor | itp_merchandise   ,0, 333 , weight(2)|abundance(100)|head_armor(36)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],

["black_hood", "Black Hood", [("hood_black",0)], itp_type_head_armor|itp_merchandise   ,0, 193 , weight(2)|abundance(100)|head_armor(18)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["light_leather", "Light Leather", [("light_leather",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 352 , weight(5)|abundance(100)|head_armor(0)|body_armor(26)|leg_armor(7)|difficulty(0) ,imodbits_armor ],
["mail_and_plate", "Mail and Plate", [("mail_and_plate",0)], itp_type_body_armor|itp_covers_legs   ,0, 593 , weight(16)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(12)|difficulty(0) ,imodbits_armor ],
["light_mail_and_plate", "Light Mail and Plate", [("light_mail_and_plate",0)], itp_type_body_armor|itp_covers_legs   ,0, 532 , weight(10)|abundance(100)|head_armor(0)|body_armor(32)|leg_armor(12)|difficulty(0) ,imodbits_armor ],

["byzantion_helmet_a", "Byzantion Helmet", [("byzantion_helmet_a",0)], itp_type_head_armor   ,0, 278 , weight(2)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["magyar_helmet_a", "Magyar Helmet", [("magyar_helmet_a",0)], itp_type_head_armor   ,0, 278 , weight(2)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["rus_helmet_a", "Rus Helmet", [("rus_helmet_a",0)], itp_type_head_armor   ,0, 278 , weight(2)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["sipahi_helmet_a", "Sipahi Helmet", [("securiti_crysader_helm_a",0),("securiti_crysader_helm_a.1",0),("securiti_crysader_helm_a_marcet",ixmesh_inventory),("securiti_crysader_helm_a_marcet.1",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature   ,0, 278 , weight(2)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["shahi", "Shahi", [("shahi",0)], itp_type_head_armor   ,0, 278 , weight(2)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["rabati", "Rabati", [("securiti_crysader_helm_b",0),("securiti_crysader_helm_b_marcet",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature   ,0, 278 , weight(2)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],

["keys", "Ring of Keys", [("throwing_axe_a",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar,
240, weight(5)|spd_rtng(98) | swing_damage(29,cut)|max_ammo(5)|weapon_length(53),imodbits_thrown ], 
["bride_dress", "Bride Dress", [("bride_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["bride_crown", "Crown of Flowers", [("bride_crown",0)],  itp_type_head_armor | itp_doesnt_cover_hair |itp_civilian |itp_attach_armature,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["bride_shoes", "Bride Shoes", [("bride_shoes",0)], itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 30 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],

["practice_bow_2","Practice Bow", [("hunting_bow",0), ("hunting_bow_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bow_back, 0, weight(1.5)|spd_rtng(90) | shoot_speed(40) | thrust_damage(21, blunt),imodbits_bow ],
["practice_arrows_2","Practice Arrows", [("arena_arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(80),imodbits_missile],

["heraldic_mail_with_surcoat_for_tableau", "{!}Heraldic Mail with Surcoat", [("heraldic_armor_new_a",0)], itp_type_body_armor |itp_covers_legs ,0,
 1, weight(22)|abundance(100)|head_armor(0)|body_armor(1)|leg_armor(1),imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_a", ":agent_no", ":troop_no")])]],
["mail_boots_for_tableau", "Mail Boots", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1, weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["warhorse_sarranid","Sarranian War Horse", [("warhorse_sarranid",0)], itp_merchandise|itp_type_horse, 0, 1811,abundance(40)|hit_points(165)|body_armor(58)|difficulty(4)|horse_speed(40)|horse_maneuver(44)|horse_charge(32)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_6]],
["warhorse_steppe","Steppe Charger", [("warhorse_steppe",0)], itp_merchandise|itp_type_horse, 0, 1400,abundance(45)|hit_points(150)|body_armor(40)|difficulty(4)|horse_speed(40)|horse_maneuver(50)|horse_charge(28)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_3,fac_kingdom_2]],

["saracin_hard_horses_a","Heavy Eastern Horse", [("saracin_hard_horses_a", 0),("saracin_hard_horses_a", imodbit_heavy|imodbit_spirited)], itp_type_horse|itp_merchandise, 0,5000, weight(0)|abundance(10)|body_armor(40)|difficulty(3)|hit_points(200)|horse_maneuver(37)|horse_speed(45)|weapon_length(110)|horse_charge(50), imodbit_champion, [], [fac_kingdom_6]],
["saracin_hard_horses_b","Heavy Eastern Horse", [("saracin_hard_horses_b", 0),("saracin_hard_horses_b", imodbit_heavy|imodbit_spirited)], itp_type_horse|itp_merchandise, 0,5000, weight(0)|abundance(10)|body_armor(40)|difficulty(3)|hit_points(200)|horse_maneuver(37)|horse_speed(45)|weapon_length(110)|horse_charge(50), imodbit_champion, [], [fac_kingdom_6]],
["saracin_hard_horses_c","Heavy Eastern Horse", [("saracin_hard_horses_c", 0),("saracin_hard_horses_a", imodbit_heavy|imodbit_spirited)], itp_type_horse|itp_merchandise, 0,5000, weight(0)|abundance(10)|body_armor(40)|difficulty(3)|hit_points(200)|horse_maneuver(37)|horse_speed(45)|weapon_length(110)|horse_charge(50), imodbit_champion, [], [fac_kingdom_6]],
["saracin_hard_horses_d","Heavy Eastern Horse", [("saracin_hard_horses_d", 0),("saracin_hard_horses_d", imodbit_heavy|imodbit_spirited)], itp_type_horse|itp_merchandise, 0,5000, weight(0)|abundance(10)|body_armor(40)|difficulty(3)|hit_points(200)|horse_maneuver(37)|horse_speed(45)|weapon_length(110)|horse_charge(50), imodbit_champion, [], [fac_kingdom_6]],
["saracin_hard_horses_a_v1","Heavy Eastern Horse", [("saracin_hard_horses_a_v1", 0),("saracin_hard_horses_a_v1", imodbit_heavy|imodbit_spirited)], itp_type_horse|itp_merchandise, 0,5000, weight(0)|abundance(10)|body_armor(40)|difficulty(3)|hit_points(200)|horse_maneuver(37)|horse_speed(45)|weapon_length(110)|horse_charge(50), imodbit_champion, [], [fac_kingdom_6]],
["saracin_hard_horses_b_v1","Heavy Eastern Horse", [("saracin_hard_horses_b_v1", 0),("saracin_hard_horses_b_v1", imodbit_heavy|imodbit_spirited)], itp_type_horse|itp_merchandise, 0,5000, weight(0)|abundance(10)|body_armor(40)|difficulty(3)|hit_points(200)|horse_maneuver(37)|horse_speed(45)|weapon_length(110)|horse_charge(50), imodbit_champion, [], [fac_kingdom_6]],
["saracin_hard_horses_c_v1","Heavy Eastern Horse", [("saracin_hard_horses_c_v1", 0),("saracin_hard_horses_a_v1", imodbit_heavy|imodbit_spirited)], itp_type_horse|itp_merchandise, 0,5000, weight(0)|abundance(10)|body_armor(40)|difficulty(3)|hit_points(200)|horse_maneuver(37)|horse_speed(45)|weapon_length(110)|horse_charge(50), imodbit_champion, [], [fac_kingdom_6]],
["saracin_hard_horses_d_v1","Heavy Eastern Horse", [("saracin_hard_horses_d_v1", 0),("saracin_hard_horses_d_v1", imodbit_heavy|imodbit_spirited)], itp_type_horse|itp_merchandise, 0,5000, weight(0)|abundance(10)|body_armor(40)|difficulty(3)|hit_points(200)|horse_maneuver(37)|horse_speed(45)|weapon_length(110)|horse_charge(50), imodbit_champion, [], [fac_kingdom_6]],
["saracen_horse_sultan","Sultan's Horse", [("saracen_horse_Sultan", 0)], itp_type_horse|itp_merchandise, 0,5000, weight(0)|abundance(10)|body_armor(40)|difficulty(3)|hit_points(200)|horse_maneuver(37)|horse_speed(45)|weapon_length(110)|horse_charge(50), imodbit_champion, [], [fac_kingdom_6]],

# Sonyer OSP Items

["maa_camel_rider_shield_a", "Camel Rider Shield", [("camel_rider_shield_a",0)], itp_type_shield, itcf_carry_round_shield, 339, weight(1.5)|hit_points(540)|body_armor(6)|spd_rtng(90)|shield_width(52),imodbits_shield, [], [fac_kingdom_11, fac_kingdom_6] ],
["maa_camel_rider_shield_b", "Camel Rider Shield", [("camel_rider_shield_b",0)], itp_type_shield, itcf_carry_round_shield, 339, weight(1.5)|hit_points(540)|body_armor(6)|spd_rtng(90)|shield_width(52),imodbits_shield, [], [fac_kingdom_11, fac_kingdom_6] ],
["maa_camel_rider_shield_c", "Camel Rider Shield", [("camel_rider_shield_c",0)], itp_type_shield, itcf_carry_round_shield, 339, weight(1.5)|hit_points(540)|body_armor(6)|spd_rtng(90)|shield_width(52),imodbits_shield, [], [fac_kingdom_11, fac_kingdom_6] ],
["maa_camel_rider_shield_d", "Camel Rider Shield", [("camel_rider_shield_d",0)], itp_type_shield, itcf_carry_round_shield, 339, weight(1.5)|hit_points(540)|body_armor(6)|spd_rtng(90)|shield_width(52),imodbits_shield, [], [fac_kingdom_11, fac_kingdom_6] ],
["maa_camel_rider_shield_e", "Camel Rider Shield", [("camel_rider_shield_e",0)], itp_type_shield, itcf_carry_round_shield, 339, weight(1.5)|hit_points(540)|body_armor(6)|spd_rtng(90)|shield_width(52),imodbits_shield, [], [fac_kingdom_11, fac_kingdom_6] ],
["maa_camel_rider_shield_f", "Camel Rider Shield", [("camel_rider_shield_f",0)], itp_type_shield, itcf_carry_round_shield, 339, weight(1.5)|hit_points(540)|body_armor(6)|spd_rtng(90)|shield_width(52),imodbits_shield, [], [fac_kingdom_11, fac_kingdom_6] ],

["maa_camel_light_c", "Rider's Camel", [("bedyin_camel_a",0),("bedyin_camel_a.1",0)], itp_merchandise|itp_type_horse,0 ,1999, weight(0)|abundance(100)|hit_points(250)|body_armor(25)|difficulty(0)|horse_speed(40)|horse_maneuver(40)|horse_charge(30)|horse_scale(90),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_11, fac_kingdom_6]],
["maa_camel_light_d", "Rider's Camel", [("bedyin_camel_b",0),("bedyin_camel_b.1",0)], itp_merchandise|itp_type_horse,0 ,1999, weight(0)|abundance(100)|hit_points(250)|body_armor(25)|difficulty(0)|horse_speed(40)|horse_maneuver(40)|horse_charge(30)|horse_scale(90),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_11, fac_kingdom_6]],

["maa_camel_war_a", "War Camel", [("bedyin_camel_c",0),("bedyin_camel_c.1",0),("bedyin_camel_c.2",0)], itp_merchandise|itp_type_horse,0 ,2599, weight(0)|abundance(100)|hit_points(300)|body_armor(45)|difficulty(3)|horse_speed(45)|horse_maneuver(45)|horse_charge(45)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_11, fac_kingdom_6]],
["maa_camel_war_b", "War Camel", [("bedyin_camel_d",0),("bedyin_camel_d.1",0),("bedyin_camel_d.2",0)], itp_merchandise|itp_type_horse,0 ,2599, weight(0)|abundance(100)|hit_points(300)|body_armor(45)|difficulty(3)|horse_speed(45)|horse_maneuver(45)|horse_charge(45)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_11, fac_kingdom_6]],
["maa_camel_war_c", "War Camel", [("bedyin_camel_e",0),("bedyin_camel_e.1",0),("bedyin_camel_e.2",0)], itp_merchandise|itp_type_horse,0 ,2599, weight(0)|abundance(100)|hit_points(300)|body_armor(45)|difficulty(3)|horse_speed(45)|horse_maneuver(45)|horse_charge(45)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_11, fac_kingdom_6]],
["maa_camel_war_d", "War Camel", [("bedyin_camel_f",0),("bedyin_camel_f.1",0)], itp_merchandise|itp_type_horse,0 ,2599, weight(0)|abundance(100)|hit_points(300)|body_armor(45)|difficulty(3)|horse_speed(45)|horse_maneuver(45)|horse_charge(45)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_11, fac_kingdom_6]],

["helper_staff","Helper Staff", [("Helper_Staff_A",0)], itp_craftable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_staff|itcf_carry_sword_back,
 2945 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(130)|swing_damage(18 , blunt) | thrust_damage(19 ,  blunt),imodbits_polearm ],

##diplomacy begin
["dplmc_coat_of_plates_red_constable", "Constable Coat of Plates", [("coat_of_plates_red",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(0) ,imodbits_armor, [], []],
##diplomacy end

["items_end", "Items End", [("shield_round_a",0)], 0, 0, 1, 0, 0],

##INVASION MODE START
["javelin_bow",         "Javelin Bow", [("war_bow",0),("war_bow_carry",ixmesh_carry)],itp_type_bow|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 
0 , weight(1.5)|difficulty(0)|spd_rtng(84) | shoot_speed(59) | thrust_damage(25 ,pierce), 0, [(ti_on_weapon_attack, [(play_sound,"snd_throw_javelin")])] ],
["knockdown_mace",         "Knockdown Mace", [("flanged_mace",0)], itp_type_one_handed_wpn|itp_can_knock_down| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
0 , weight(3.5)|difficulty(0)|spd_rtng(103) | weapon_length(70)|swing_damage(24 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["blood_drain_throwing_knives", "Blood Drain Throwing Knives", [("throwing_knife",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(2.5)|difficulty(0)|spd_rtng(121) | shoot_speed(25) | thrust_damage(25 ,  pierce)|max_ammo(5)|weapon_length(0),imodbits_thrown ],
["doom_javelins",         "Doom Javelins", [("jarid_new_b",0),("jarid_new_b_bag", ixmesh_carry)], itp_type_thrown |itp_primary ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 
0 , weight(3)|difficulty(0)|spd_rtng(87) | shoot_speed(22) | thrust_damage(44 ,  pierce)|max_ammo(2)|weapon_length(65),imodbits_thrown ],
#["unblockable_morningstar",         "Unblockable Morningstar", [("mace_morningstar_new",0)], itp_crush_through|itp_type_two_handed_wpn|itp_primary|itp_wooden_parry|itp_unbalanced, itc_morningstar|itcf_carry_mace_left_hip, 
#305 , weight(20)|difficulty(13)|spd_rtng(95) | weapon_length(85)|swing_damage(38 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],
["disarming_throwing_axe", "Disarming Throwing Axe", [("throwing_axe_a",0)], itp_type_thrown |itp_primary,itcf_throw_axe,
0, weight(1)|difficulty(0)|spd_rtng(98) | shoot_speed(18) | thrust_damage(10,cut)|max_ammo(1)|weapon_length(53),imodbits_thrown_minus_heavy ],
["instakill_knife",         "Instakill Knife", [("peasant_knife_new",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry|itp_two_handed, itc_dagger|itcf_carry_dagger_front_left, 
0 , weight(0.5)|difficulty(0)|spd_rtng(101) | weapon_length(40)|swing_damage(21 , cut) | thrust_damage(13 ,  pierce),imodbits_sword ],
["backstabber", "Backstabber", [("sword_viking_a_small",0),("sword_viking_a_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
0 , weight(1.25)|difficulty(0)|spd_rtng(103) | weapon_length(86)|swing_damage(20 , cut) | thrust_damage(13 ,  pierce),imodbits_sword_high ],
["weak_beserker_dart",         "Weak Beserker Dart", [("dart_b",0),("dart_b_bag", ixmesh_carry)], itp_type_thrown |itp_primary ,itcf_throw_javelin|itcf_carry_quiver_right_vertical|itcf_show_holster_when_drawn, 
0 , weight(4)|difficulty(0)|spd_rtng(95) | shoot_speed(28) | thrust_damage(5 ,  pierce)|max_ammo(1)|weapon_length(32),imodbits_thrown ],
["team_change_dart",         "Team Change Dart", [("dart_a",0),("dart_a_bag", ixmesh_carry)], itp_type_thrown |itp_primary ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 
0 , weight(5)|difficulty(0)|spd_rtng(93) | shoot_speed(27) | thrust_damage(5 ,  pierce)|max_ammo(1)|weapon_length(45),imodbits_thrown ],
["awesome_spear",         "Awesome Spear", [("spear",0)], itp_type_polearm| itp_primary|itp_penalty_with_shield|itp_wooden_parry,itc_staff|itcf_carry_spear, 
0 , weight(1.5)|difficulty(0)|spd_rtng(110) | weapon_length(157)|swing_damage(41 , cut) | thrust_damage(33 ,  pierce),imodbits_polearm ],


["running_boots",  "Running Boots", [("samurai_boots",0)], itp_type_foot_armor | itp_attach_armature,0, 0 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(21)|difficulty(0) ,imodbits_cloth ],
["power_gloves","Power Gloves", [("scale_gauntlets_a_L",0)], itp_type_hand_armor,0, 0, weight(0.9)|abundance(100)|body_armor(6)|difficulty(0),imodbits_armor],
#["wielding_gloves","Wielding Gloves", [("scale_gauntlets_b_L",0)], itp_type_hand_armor,0, 0, weight(0.75)|abundance(100)|body_armor(5)|difficulty(0),imodbits_armor],
["invulnerable_helmet", "Invulnerable Helmet", [("maciejowski_helmet_new",0)], itp_type_head_armor|itp_covers_head,0, 1240 , weight(2.75)|abundance(100)|head_armor(63)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ],
["kicking_boots", "Kicking Boots", [("sarranid_camel_boots",0)],  itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 0 , weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_plate ],
["restore_health_armour",  "Restore Health Armour", [("samurai_armor",0)], itp_type_body_armor  |itp_covers_legs ,0, 0 , weight(12)|abundance(100)|head_armor(0)|body_armor(27)|leg_armor(11)|difficulty(0) ,imodbits_armor ],
#["extra_life_helmet", "Extra Life Helmet", [("byzantion_helmet_a",0)], itp_type_head_armor   ,0, 0 , weight(2)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
#["scatter_crossbow", "Scatter Crossbow", [("crossbow_c",0)], itp_type_crossbow |itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 
#0 , weight(3.75)|spd_rtng(20) | shoot_speed(90) | thrust_damage(90 ,pierce)|max_ammo(1),imodbits_crossbow ],

#additional items for coop
["javelin_bow_ammo",         "Shooting Javelins", [("javelin_bow_ammo",0),("javelins_quiver_new", ixmesh_carry)], itp_type_arrows|itp_default_ammo ,itcf_carry_quiver_back, 
0, weight(4) | thrust_damage(34 ,  pierce)|max_ammo(15)|weapon_length(75),0 ],
#["scatter_bolts","Scatter Bolts", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts|itp_merchandise|itp_default_ammo|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical, 
#0,weight(2.25)|abundance(90)|weapon_length(63)|thrust_damage(1,pierce)|max_ammo(4),imodbits_missile],
["ccoop_new_items_end", "Items End", [("shield_round_a",0)], 0, 0, 1, 0, 0],
#INVASION MODE END

]
# modmerger_start version=201 type=2
try:
    component_name = "items"
    var_set = { "items" : items }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end
