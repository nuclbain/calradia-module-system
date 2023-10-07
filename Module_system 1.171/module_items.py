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
 ["tutorial_club", "Club", [("club",0)], itp_type_one_handed_wpn| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar, 0 , weight(2.5)|difficulty(0)|spd_rtng(95) | weapon_length(95)|swing_damage(11 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
 ["tutorial_battle_axe", "Battle Axe", [("battle_ax",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(5)|difficulty(0)|spd_rtng(88) | weapon_length(108)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["tutorial_arrows","Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(3)|abundance(160)|weapon_length(95)|thrust_damage(0,pierce)|max_ammo(20),imodbits_missile],
 ["tutorial_bolts","Bolts", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|abundance(90)|weapon_length(55)|thrust_damage(0,pierce)|max_ammo(18),imodbits_missile],
 ["tutorial_short_bow", "Short Bow", [("short_bow",0),("short_bow_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 0 , weight(1)|difficulty(0)|spd_rtng(98) | shoot_speed(49) | thrust_damage(12 ,  pierce  ),imodbits_bow ],
 ["tutorial_crossbow", "Crossbow", [("crossbow",0)], itp_type_crossbow |itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 0 , weight(3)|difficulty(0)|spd_rtng(42)|  shoot_speed(68) | thrust_damage(32,pierce)|max_ammo(1),imodbits_crossbow ],
 ["tutorial_throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|difficulty(0)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16 ,  cut)|max_ammo(14)|weapon_length(0),imodbits_missile ],
 ["tutorial_saddle_horse", "Saddle Horse", [("saddle_horse",0)], itp_type_horse, 0, 0,abundance(90)|body_armor(3)|difficulty(0)|horse_speed(40)|horse_maneuver(38)|horse_charge(8),imodbits_horse_basic],
 ["tutorial_shield", "Kite Shield", [("shield_kite_a",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(150),imodbits_shield ],
 ["tutorial_staff_no_attack","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_parry_polearm|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(0,blunt) | thrust_damage(0,blunt),imodbits_none],
 ["tutorial_staff","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(16,blunt) | thrust_damage(16,blunt),imodbits_none],
 ["tutorial_sword", "Sword", [("long_sword",0),("scab_longsw_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 0 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(102)|swing_damage(18 , cut) | thrust_damage(15 ,  pierce),imodbits_sword ],
 ["tutorial_axe", "Axe", [("iron_ax",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(4)|difficulty(0)|spd_rtng(91) | weapon_length(108)|swing_damage(19 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

 ["tutorial_dagger","Dagger", [("practice_dagger",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(40)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],


 ["horse_meat","Horse Meat", [("raw_meat",0)], itp_type_goods|itp_consumable|itp_food, 0, 12,weight(40)|food_quality(30)|max_ammo(40),imodbits_none],
# Items before this point are hardwired and their order should not be changed!
 ["practice_sword","Practice Sword", [("practice_sword",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_wooden_parry|itp_wooden_attack, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(22,blunt)|thrust_damage(20,blunt),imodbits_none],
 ["heavy_practice_sword","Heavy Practice Sword", [("heavy_practicesword",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_wooden_parry|itp_wooden_attack, itc_greatsword,
    21, weight(6.25)|spd_rtng(94)|weapon_length(128)|swing_damage(30,blunt)|thrust_damage(24,blunt),imodbits_none],
 ["practice_dagger","Practice Dagger", [("practice_dagger",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry|itp_wooden_attack, itc_dagger|itcf_carry_dagger_front_left, 2,weight(0.5)|spd_rtng(110)|weapon_length(47)|swing_damage(16,blunt)|thrust_damage(14,blunt),imodbits_none],
 ["practice_axe", "Practice Axe", [("hatchet",0)], itp_type_one_handed_wpn| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 24 , weight(2) | spd_rtng(95) | weapon_length(75) | swing_damage(24, blunt) | thrust_damage(0, pierce), imodbits_axe],
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
 ["practice_crossbow", "Practice Crossbow", [("crossbow_a",0)], itp_type_crossbow |itp_primary|itp_two_handed ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 0, weight(3)|spd_rtng(42)| shoot_speed(68) | thrust_damage(32,blunt)|max_ammo(1),imodbits_crossbow],
 ["practice_javelin", "Practice Javelins", [("javelin",0),("javelins_quiver_new", ixmesh_carry)], itp_type_thrown |itp_primary|itp_next_item_as_melee,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 0, weight(5) | spd_rtng(91) | shoot_speed(28) | thrust_damage(27, blunt) | max_ammo(50) | weapon_length(75), imodbits_thrown],
 ["practice_javelin_melee", "practice_javelin_melee", [("javelin",0)], itp_type_polearm|itp_primary|itp_penalty_with_shield|itp_wooden_parry , itc_staff, 0, weight(1)|difficulty(0)|spd_rtng(91) |swing_damage(12, blunt)| thrust_damage(14,  blunt)|weapon_length(75),imodbits_polearm ],
 ["practice_throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16, blunt)|max_ammo(10)|weapon_length(0),imodbits_thrown ],
 ["practice_throwing_daggers_100_amount", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16, blunt)|max_ammo(100)|weapon_length(0),imodbits_thrown ],
# ["cheap_shirt","Cheap Shirt", [("shirt",0)], itp_type_body_armor|itp_covers_legs, 0, 4,weight(1.25)|body_armor(3),imodbits_none],
 ["practice_horse","Practice Horse", [("saddle_horse",0)], itp_type_horse, 0, 37,body_armor(10)|horse_speed(40)|horse_maneuver(37)|horse_charge(14),imodbits_none],
 ["practice_arrows","Practice Arrows", [("arena_arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(80),imodbits_missile],
## ["practice_arrows","Practice Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo)], itp_type_arrows, 0, 31,weight(1.5)|weapon_length(95)|max_ammo(80),imodbits_none],
 ["practice_bolts","Practice Bolts", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|weapon_length(55)|max_ammo(49),imodbits_missile],
 ["practice_arrows_10_amount","Practice Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(10),imodbits_missile],
 ["practice_arrows_100_amount","Practice Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(100),imodbits_missile],
 ["practice_bolts_9_amount","Practice Bolts", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|weapon_length(55)|max_ammo(9),imodbits_missile],
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

["arena_armor_white", "Arena Armor White", [("arena_armorW_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
["arena_armor_red", "Arena Armor Red", [("arena_armorR_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
["arena_armor_blue", "Arena Armor Blue", [("arena_armorB_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
["arena_armor_green", "Arena Armor Green", [("arena_armorG_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
["arena_armor_yellow", "Arena Armor Yellow", [("arena_armorY_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
["arena_tunic_white", "Arena Tunic White ", [("arena_tunicW_new",0)], itp_type_body_armor |itp_covers_legs ,0, 47 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth ],
["arena_tunic_red", "Arena Tunic Red", [("arena_tunicR_new",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth ], 
["arena_tunic_blue", "Arena Tunic Blue", [("arena_tunicB_new",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth ], 
["arena_tunic_green", "Arena Tunic Green", [("arena_tunicG_new",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth ],
["arena_tunic_yellow", "Arena Tunic Yellow", [("arena_tunicY_new",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth ],
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

 ["iron","Iron", [("iron",0)], itp_merchandise|itp_type_goods, 0,264,weight(60)|abundance(60),imodbits_none],
 ["tools","Tools", [("iron_hammer",0)], itp_merchandise|itp_type_goods, 0, 410,weight(50)|abundance(90),imodbits_none],

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
 ["tutorial_axe", "Axe", [("iron_ax",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(4)|difficulty(0)|spd_rtng(91) | weapon_length(108)|swing_damage(19 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["tutorial_spear", "Spear", [("spear",0)], itp_type_polearm| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear, 0 , weight(4.5)|difficulty(0)|spd_rtng(80) | weapon_length(158)|swing_damage(0 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm ],
 ["tutorial_club", "Club", [("club",0)], itp_type_one_handed_wpn| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar, 0 , weight(2.5)|difficulty(0)|spd_rtng(95) | weapon_length(95)|swing_damage(11 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
 ["tutorial_battle_axe", "Battle Axe", [("battle_ax",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(5)|difficulty(0)|spd_rtng(88) | weapon_length(108)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["tutorial_arrows","Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(3)|abundance(160)|weapon_length(95)|thrust_damage(0,pierce)|max_ammo(20),imodbits_missile],
 ["tutorial_bolts","Bolts", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|abundance(90)|weapon_length(63)|thrust_damage(0,pierce)|max_ammo(18),imodbits_missile],
 ["tutorial_short_bow", "Short Bow", [("short_bow",0),("short_bow_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 0 , weight(1)|difficulty(0)|spd_rtng(98) | shoot_speed(49) | thrust_damage(12 ,  pierce  ),imodbits_bow ],
 ["tutorial_crossbow", "Crossbow", [("crossbow_a",0)], itp_type_crossbow |itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 0 , weight(3)|difficulty(0)|spd_rtng(42)|  shoot_speed(68) | thrust_damage(32,pierce)|max_ammo(1),imodbits_crossbow ],
 ["tutorial_throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|difficulty(0)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16 ,  cut)|max_ammo(14)|weapon_length(0),imodbits_missile ],
 ["tutorial_saddle_horse", "Saddle Horse", [("saddle_horse",0)], itp_type_horse, 0, 0,abundance(90)|body_armor(3)|difficulty(0)|horse_speed(40)|horse_maneuver(38)|horse_charge(8),imodbits_horse_basic],
 ["tutorial_shield", "Kite Shield", [("shield_kite_a",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(150),imodbits_shield ],
 ["tutorial_staff_no_attack","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_parry_polearm|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(0,blunt) | thrust_damage(0,blunt),imodbits_none],
 ["tutorial_staff","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(16,blunt) | thrust_damage(16,blunt),imodbits_none],

# Horses: sumpter horse/ pack horse, saddle horse, steppe horse, warm blood, geldling, stallion,   war mount, charger, 
# Carthorse, hunter, heavy hunter, hackney, palfrey, courser, destrier.
 ["sumpter_horse","Sumpter Horse", [("sumpter_horse",0)], itp_merchandise|itp_type_horse, 0, 134,abundance(90)|hit_points(100)|body_armor(14)|difficulty(1)|horse_speed(37)|horse_maneuver(39)|horse_charge(9)|horse_scale(100),imodbits_horse_basic],
 ["saddle_horse","Saddle Horse", [("saddle_horse",0),("horse_c",imodbits_horse_good)], itp_merchandise|itp_type_horse, 0, 240,abundance(90)|hit_points(100)|body_armor(8)|difficulty(1)|horse_speed(45)|horse_maneuver(44)|horse_charge(10)|horse_scale(104),imodbits_horse_basic],
 ["steppe_horse","Steppe Horse", [("steppe_horse",0)], itp_merchandise|itp_type_horse, 0, 192,abundance(80)|hit_points(120)|body_armor(10)|difficulty(2)|horse_speed(40)|horse_maneuver(51)|horse_charge(8)|horse_scale(98),imodbits_horse_basic, [], [fac_kingdom_2, fac_kingdom_3]],
 ["arabian_horse_a","Desert Horse", [("arabian_horse_a",0)], itp_merchandise|itp_type_horse, 0, 550,abundance(80)|hit_points(110)|body_armor(10)|difficulty(2)|horse_speed(42)|horse_maneuver(50)|horse_charge(12)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_3, fac_kingdom_6]],
 ["courser","Courser", [("courser",0)], itp_merchandise|itp_type_horse, 0, 600,abundance(70)|body_armor(12)|hit_points(110)|difficulty(2)|horse_speed(50)|horse_maneuver(44)|horse_charge(12)|horse_scale(106),imodbits_horse_basic|imodbit_champion],
 ["arabian_horse_b","Sarranid Horse", [("arabian_horse_b",0)], itp_merchandise|itp_type_horse, 0, 700,abundance(80)|hit_points(120)|body_armor(10)|difficulty(3)|horse_speed(43)|horse_maneuver(54)|horse_charge(16)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_6]],
 ["hunter","Hunter", [("hunting_horse",0),("hunting_horse",imodbits_horse_good)], itp_merchandise|itp_type_horse, 0, 810,abundance(60)|hit_points(160)|body_armor(18)|difficulty(3)|horse_speed(43)|horse_maneuver(44)|horse_charge(24)|horse_scale(108),imodbits_horse_basic|imodbit_champion],
 ["warhorse","War Horse", [("warhorse_chain",0)], itp_merchandise|itp_type_horse, 0, 1224,abundance(50)|hit_points(165)|body_armor(40)|difficulty(4)|horse_speed(40)|horse_maneuver(41)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_12, fac_kingdom_5, fac_kingdom_9]],
 ["charger","Charger", [("charger_new",0)], itp_merchandise|itp_type_horse, 0, 1811,abundance(40)|hit_points(165)|body_armor(58)|difficulty(4)|horse_speed(40)|horse_maneuver(44)|horse_charge(32)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1, fac_kingdom_5]],



#whalebone crossbow, yew bow, war bow, arming sword 
 ["arrows","Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows|itp_merchandise|itp_default_ammo, itcf_carry_quiver_back, 
 72,weight(3)|abundance(160)|weapon_length(95)|thrust_damage(1,pierce)|max_ammo(30),imodbits_missile],
 ["khergit_arrows","Khergit Arrows", [("arrow_b",0),("flying_missile",ixmesh_flying_ammo),("quiver_b", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 
 410,weight(3.5)|abundance(30)|weapon_length(95)|thrust_damage(3,pierce)|max_ammo(30),imodbits_missile],
 ["barbed_arrows","Barbed Arrows", [("barbed_arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver_d", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 
 124,weight(3)|abundance(70)|weapon_length(95)|thrust_damage(2,pierce)|max_ammo(30),imodbits_missile],
 ["bodkin_arrows","Bodkin Arrows", [("piercing_arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver_c", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 
 350,weight(3)|abundance(50)|weapon_length(91)|thrust_damage(3,pierce)|max_ammo(28),imodbits_missile],
 ["bolts","Bolts", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts|itp_merchandise|itp_default_ammo|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical, 
 64,weight(2.25)|abundance(90)|weapon_length(63)|thrust_damage(1,pierce)|max_ammo(29),imodbits_missile],
 ["steel_bolts","Steel Bolts", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag_c", ixmesh_carry)], itp_type_bolts|itp_merchandise|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical, 
 210,weight(2.5)|abundance(20)|weapon_length(63)|thrust_damage(2,pierce)|max_ammo(29),imodbits_missile],
 ["cartridges","Cartridges", [("cartridge_a",0)], itp_type_bullets|itp_merchandise|itp_can_penetrate_shield|itp_default_ammo, 0, 
 41,weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(1,pierce)|max_ammo(50),imodbits_missile],

["pilgrim_disguise", "Pilgrim Disguise", [("pilgrim_outfit",0)], 0| itp_type_body_armor |itp_covers_legs |itp_civilian ,0, 25 , weight(2)|abundance(100)|head_armor(0)|body_armor(19)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["pilgrim_hood", "Pilgrim Hood", [("pilgrim_hood",0)], 0| itp_type_head_armor |itp_civilian  ,0, 35 , weight(1.25)|abundance(100)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

# ARMOR
#handwear
["leather_gloves","Leather Gloves", [("leather_gloves_L",0)], itp_merchandise|itp_type_hand_armor,0, 90, weight(0.25)|abundance(120)|body_armor(2)|difficulty(0),imodbits_cloth],
["mail_mittens","Mail Mittens", [("mail_mittens_L",0)], itp_merchandise|itp_type_hand_armor,0, 350, weight(0.5)|abundance(100)|body_armor(4)|difficulty(0),imodbits_armor],
["scale_gauntlets","Scale Gauntlets", [("scale_gauntlets_b_L",0)], itp_merchandise|itp_type_hand_armor,0, 710, weight(0.75)|abundance(100)|body_armor(5)|difficulty(0),imodbits_armor],
["lamellar_gauntlets","Lamellar Gauntlets", [("scale_gauntlets_a_L",0)], itp_merchandise|itp_type_hand_armor,0, 910, weight(0.9)|abundance(100)|body_armor(6)|difficulty(0),imodbits_armor],
["gauntlets","Gauntlets", [("gauntlets_L",0),("gauntlets_L",imodbit_reinforced)], itp_merchandise|itp_type_hand_armor,0, 1040, weight(1.0)|abundance(100)|body_armor(7)|difficulty(0),imodbits_armor],

#footwear
["wrapping_boots", "Wrapping Boots", [("wrapping_boots_a",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 3 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(3)|difficulty(0) ,imodbits_cloth ],
["woolen_hose", "Woolen Hose", [("woolen_hose_a",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
["blue_hose", "Blue Hose", [("blue_hose_a",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 11 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
["hunter_boots", "Hunter Boots", [("hunter_boots_a",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature,0,
 19 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
["hide_boots", "Hide Boots", [("hide_boots_a",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 34 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["ankle_boots", "Ankle Boots", [("ankle_boots_a_new",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 75 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["nomad_boots", "Nomad Boots", [("nomad_boots_a",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 90 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(14)|difficulty(0) ,imodbits_cloth ],
["leather_boots", "Leather Boots", [("leather_boots_a",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 174 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth ],
["splinted_leather_greaves", "Splinted Leather Greaves", [("leather_greaves_a",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
 310 , weight(2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(21)|difficulty(0) ,imodbits_armor ],
["mail_chausses", "Mail Chausses", [("mail_chausses_a",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature  ,0,
 530 , weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(24)|difficulty(0) ,imodbits_armor ],
["splinted_greaves", "Splinted Greaves", [("splinted_greaves_a",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
 853 , weight(2.75)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(28)|difficulty(7) ,imodbits_armor ],
["mail_boots", "Mail Boots", [("mail_boots_a",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature  ,0,
 1250 , weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(31)|difficulty(8) ,imodbits_armor ],
["iron_greaves", "Iron Greaves", [("iron_greaves_a",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
 1770 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_armor ],
["black_greaves", "Black Greaves", [("black_greaves",0)], itp_type_foot_armor  | itp_attach_armature,0,
 2361 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(35)|difficulty(0) ,imodbits_armor ],
["khergit_leather_boots", "Khergit Leather Boots", [("khergit_leather_boots",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 120 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(18)|difficulty(0) ,imodbits_cloth ],
["sarranid_boots_a", "Sarranid Shoes", [("sarranid_shoes",0)], itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 30 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["sarranid_boots_b", "Sarranid Leather Boots", [("sarranid_boots",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 120 , weight(2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth ],
["sarranid_boots_c", "Plated Boots", [("sarranid_camel_boots",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 280 , weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_plate ],
["sarranid_boots_d", "Sarranid Mail Boots", [("sarranid_mail_chausses",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 920 , weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_armor ],

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
["sarranid_lady_dress", "Sarranid Lady Dress", [("sarranid_lady_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["sarranid_lady_dress_b", "Sarranid Lady Dress", [("sarranid_lady_dress_b",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["sarranid_common_dress", "Sarranid Dress", [("sarranid_common_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["sarranid_common_dress_b", "Sarranid Dress", [("sarranid_common_dress_b",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["courtly_outfit", "Courtly Outfit", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["nobleman_outfit", "Nobleman Outfit", [("nobleman_outfit_b_new",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(12)|difficulty(0) ,imodbits_cloth ], 
["nomad_armor", "Nomad Armor", [("nomad_armor_new",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs   ,0, 25 , weight(2)|abundance(100)|head_armor(0)|body_armor(24)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["khergit_armor", "Khergit Armor", [("khergit_armor_new",0)], itp_merchandise| itp_type_body_armor | itp_covers_legs ,0, 38 , weight(2)|abundance(100)|head_armor(0)|body_armor(24)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["leather_jacket", "Leather Jacket", [("leather_jacket_new",0)], itp_merchandise| itp_type_body_armor | itp_covers_legs  |itp_civilian ,0, 50 , weight(3)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

#NEW:
["rawhide_coat", "Rawhide Coat", [("coat_of_plates_b",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 12 , weight(5)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
#NEW: was lthr_armor_a
["leather_armor", "Leather Armor", [("tattered_leather_armor_a",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs  ,0, 65 , weight(7)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["fur_coat", "Fur Coat", [("fur_coat",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 117 , weight(6)|abundance(100)|head_armor(0)|body_armor(13)|leg_armor(6)|difficulty(0) ,imodbits_armor ],



#for future:
["coat", "Coat", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["leather_coat", "Leather Coat", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["mail_coat", "Coat of Mail", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["long_mail_coat", "Long Coat of Mail", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["mail_with_tunic_red", "Mail with Tunic", [("arena_armorR_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(8), imodbits_armor ],
["mail_with_tunic_green", "Mail with Tunic", [("arena_armorG_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(8), imodbits_armor ],
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
["blue_dress", "Blue Dress", [("blue_dress_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["peasant_dress", "Peasant Dress", [("peasant_dress_b_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ], 
["woolen_dress", "Woolen Dress", [("woolen_dress",0)], itp_merchandise| itp_type_body_armor|itp_civilian  |itp_covers_legs ,0,
 10 , weight(1.75)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["shirt", "Shirt", [("shirt",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 3 , weight(1)|abundance(100)|head_armor(0)|body_armor(5)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
 #NEW: was "linen_tunic"
["linen_tunic", "Linen Tunic", [("shirt_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
 #NEW was cvl_costume_a
["short_tunic", "Red Tunic", [("rich_tunic_a",0)], itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
#TODO:
 ["red_shirt", "Red Shirt", [("rich_tunic_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
 ["red_tunic", "Red Tunic", [("arena_tunicR_new",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],

 ["green_tunic", "Green Tunic", [("arena_tunicG_new",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
 ["blue_tunic", "Blue Tunic", [("arena_tunicB_new",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
["robe", "Robe", [("robe",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 31 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
#NEW: was coarse_tunic
["coarse_tunic", "Tunic with vest", [("coarse_tunic_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 47 , weight(2)|abundance(100)|head_armor(0)|body_armor(11)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["leather_apron", "Leather Apron", [("leather_apron",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 61 , weight(3)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(7)|difficulty(0) ,imodbits_cloth ],
#NEW: was tabard_a
["tabard", "Tabard", [("tabard_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 107 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
#NEW: was leather_vest
["leather_vest", "Leather Vest", [("leather_vest_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 146 , weight(4)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(7)|difficulty(0) ,imodbits_cloth ],
["steppe_armor", "Steppe Armor", [("lamellar_leather",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 195 , weight(5)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["gambeson", "Gambeson", [("white_gambeson",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 260 , weight(5)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
["blue_gambeson", "Blue Gambeson", [("blue_gambeson",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 270 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
#NEW: was red_gambeson
["red_gambeson", "Red Gambeson", [("red_gambeson_a",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
#NEW: was aketon_a
["padded_cloth", "Aketon", [("padded_cloth_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 297 , weight(11)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
#NEW:
 ["aketon_green", "Padded Cloth", [("padded_cloth_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 297 , weight(11)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
 #NEW: was "leather_jerkin"
["leather_jerkin", "Leather Jerkin", [("ragged_leather_jerkin",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 321 , weight(6)|abundance(100)|head_armor(0)|body_armor(23)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["nomad_vest", "Nomad Vest", [("nomad_vest_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 360 , weight(7)|abundance(50)|head_armor(0)|body_armor(22)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["ragged_outfit", "Ragged Outfit", [("ragged_outfit_a_new",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 390 , weight(7)|abundance(100)|head_armor(0)|body_armor(23)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
 #NEW: was padded_leather
["padded_leather", "Padded Leather", [("leather_armor_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian,0,
 454 , weight(12)|abundance(100)|head_armor(0)|body_armor(27)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["tribal_warrior_outfit", "Tribal Warrior Outfit", [("tribal_warrior_outfit_a_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 520 , weight(14)|abundance(100)|head_armor(0)|body_armor(30)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["nomad_robe", "Nomad Robe", [("nomad_robe_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0,
 610 , weight(15)|abundance(100)|head_armor(0)|body_armor(32)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
#["heraldric_armor", "Heraldric Armor", [("tourn_armor_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 442 , weight(17)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(8)|difficulty(7) ,imodbits_armor ],
#NEW: was "std_lthr_coat"
["studded_leather_coat", "Studded Leather Coat", [("leather_armor_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 690 , weight(14)|abundance(100)|head_armor(0)|body_armor(36)|leg_armor(10)|difficulty(7) ,imodbits_armor ],

["byrnie", "Byrnie", [("byrnie_a_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 795 , weight(17)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(6)|difficulty(7) ,imodbits_armor ],
#["blackwhite_surcoat", "Black and White Surcoat", [("surcoat_blackwhite",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 348 , weight(16)|abundance(100)|head_armor(0)|body_armor(33)|leg_armor(8)|difficulty(7) ,imodbits_armor ],
#["green_surcoat", "Green Surcoat", [("surcoat_green",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 348 , weight(16)|abundance(100)|head_armor(0)|body_armor(33)|leg_armor(8)|difficulty(7) ,imodbits_armor ],
#["blue_surcoat", "Blue Surcoat", [("surcoat_blue",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 350 , weight(16)|abundance(100)|head_armor(0)|body_armor(33)|leg_armor(8)|difficulty(7) ,imodbits_armor ],
#["red_surcoat", "Red Surcoat", [("surcoat_red",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 350 , weight(16)|abundance(100)|head_armor(0)|body_armor(33)|leg_armor(8)|difficulty(7) ,imodbits_armor ],
#NEW: was "haubergeon_a"
["haubergeon", "Haubergeon", [("haubergeon_c",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 863 , weight(18)|abundance(100)|head_armor(0)|body_armor(41)|leg_armor(6)|difficulty(6) ,imodbits_armor ],

["lamellar_vest", "Lamellar Vest", [("lamellar_vest_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 970 , weight(18)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_cloth ],

["lamellar_vest_khergit", "Khergit Lamellar Vest", [("lamellar_vest_b",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 970 , weight(18)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_cloth ],

 #NEW: was mail_shirt
["mail_shirt", "Mail Shirt", [("mail_shirt_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 1040 , weight(19)|abundance(100)|head_armor(0)|body_armor(37)|leg_armor(12)|difficulty(7) ,imodbits_armor ],

["mail_hauberk", "Mail Hauberk", [("hauberk_a_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(12)|difficulty(7) ,imodbits_armor ],

["mail_with_surcoat", "Mail with Surcoat", [("mail_long_surcoat_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 1544 , weight(22)|abundance(100)|head_armor(0)|body_armor(42)|leg_armor(14)|difficulty(7) ,imodbits_armor ],
["surcoat_over_mail", "Surcoat over Mail", [("surcoat_over_mail_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 1720 , weight(22)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(14)|difficulty(7) ,imodbits_armor ],
#["lamellar_cuirass", "Lamellar Cuirass", [("lamellar_armor",0)], itp_type_body_armor  |itp_covers_legs,0, 1020 , weight(25)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(15)|difficulty(9) ,imodbits_armor ],
#NEW: was "brigandine_a"
["brigandine_red", "Brigandine", [("brigandine_b",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
 1830 , weight(19)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(12)|difficulty(0) ,imodbits_armor ],
["lamellar_armor", "Lamellar Armor", [("lamellar_armor_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2410 , weight(25)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(13)|difficulty(0) ,imodbits_armor ],
["scale_armor", "Scale Armor", [("lamellar_armor_e",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2558 , weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(13)|difficulty(8) ,imodbits_armor ],
 #NEW: was "reinf_jerkin"
["banded_armor", "Banded Armor", [("banded_armor_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2710 , weight(23)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(14)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_4] ],
#NEW: was hard_lthr_a
["cuir_bouilli", "Cuir Bouilli", [("cuir_bouilli_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3100 , weight(24)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(15)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_4] ],
["coat_of_plates", "Coat of Plates", [("coat_of_plates_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
["coat_of_plates_red", "Coat of Plates", [("coat_of_plates_red",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
["plate_armor", "Plate Armor", [("full_plate_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 6553 , weight(27)|abundance(100)|head_armor(0)|body_armor(55)|leg_armor(17)|difficulty(9) ,imodbits_plate ],
["black_armor", "Black Armor", [("black_armor",0)], itp_type_body_armor  |itp_covers_legs ,0,
 9496 , weight(28)|abundance(100)|head_armor(0)|body_armor(57)|leg_armor(18)|difficulty(10) ,imodbits_plate ],

##armors_d
["pelt_coat", "Pelt Coat", [("thick_coat_a",0)],  itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
 14, weight(2)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
##armors_e
["khergit_elite_armor", "Khergit Elite Armor", [("lamellar_armor_d",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
["vaegir_elite_armor", "Vaegir Elite Armor", [("lamellar_armor_c",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_2] ],
["sarranid_elite_armor", "Sarranid Elite Armor", [("tunic_armor_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian ,0,
 3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(8) ,imodbits_armor ],


 ["sarranid_dress_a", "Dress", [("woolen_dress",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 33 , weight(1)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
 ["sarranid_dress_b", "Dress", [("woolen_dress",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 33 , weight(1)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
 ["sarranid_cloth_robe", "Worn Robe", [("sar_robe",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 33 , weight(1)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
 ["sarranid_cloth_robe_b", "Worn Robe", [("sar_robe_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 33 , weight(1)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
["skirmisher_armor", "Skirmisher Armor", [("skirmisher_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 74 , weight(3)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
["archers_vest", "Archer's Padded Vest", [("archers_vest",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 260 , weight(6)|abundance(100)|head_armor(0)|body_armor(23)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["sarranid_leather_armor", "Sarranid Leather Armor", [("sarranid_leather_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 650 , weight(9)|abundance(100)|head_armor(0)|body_armor(32)|leg_armor(12)|difficulty(0) ,imodbits_armor ],
["sarranid_cavalry_robe", "Cavalry Robe", [("arabian_armor_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 990 , weight(15)|abundance(100)|head_armor(0)|body_armor(36)|leg_armor(8)|difficulty(0) ,imodbits_armor ],
["arabian_armor_b", "Sarranid Guard Armor", [("arabian_armor_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 1200 , weight(19)|abundance(100)|head_armor(0)|body_armor(38)|leg_armor(8)|difficulty(0) ,imodbits_armor],
 ["sarranid_mail_shirt", "Sarranid Mail Shirt", [("sarranian_mail_shirt",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 1400 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(14)|difficulty(7) ,imodbits_armor ],
["mamluke_mail", "Mamluke Mail", [("sarranid_elite_cavalary",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
2900 , weight(24)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(16)|difficulty(8) ,imodbits_armor ],

#Quest-specific - perhaps can be used for prisoners, 
["burlap_tunic", "Burlap Tunic", [("shirt",0)], itp_type_body_armor  |itp_covers_legs ,0,
 5 , weight(1)|abundance(100)|head_armor(0)|body_armor(3)|leg_armor(1)|difficulty(0) ,imodbits_armor ],


["heraldic_mail_with_surcoat", "Heraldic Mail with Surcoat", [("heraldic_armor_new_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3454 , weight(22)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(17)|difficulty(7) ,imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_a", ":agent_no", ":troop_no")])]],
["heraldic_mail_with_tunic", "Heraldic Mail", [("heraldic_armor_new_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3520 , weight(22)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(16)|difficulty(7) ,imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_b", ":agent_no", ":troop_no")])]],
["heraldic_mail_with_tunic_b", "Heraldic Mail", [("heraldic_armor_new_c",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3610 , weight(22)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(16)|difficulty(7) ,imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_c", ":agent_no", ":troop_no")])]],
["heraldic_mail_with_tabard", "Heraldic Mail with Tabard", [("heraldic_armor_new_d",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3654 , weight(21)|abundance(100)|head_armor(0)|body_armor(51)|leg_armor(15)|difficulty(7) ,imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_d", ":agent_no", ":troop_no")])]],
["turret_hat_ruby", "Turret Hat", [("turret_hat_r",0)], itp_type_head_armor  |itp_civilian|itp_fit_to_head ,0, 70 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ], 
["turret_hat_blue", "Turret Hat", [("turret_hat_b",0)], itp_type_head_armor  |itp_civilian|itp_fit_to_head ,0, 80 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ], 
["turret_hat_green", "Barbette", [("barbette_new",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_fit_to_head,0,70, weight(0.5)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["head_wrappings","Head Wrapping",[("head_wrapping",0)],itp_type_head_armor|itp_fit_to_head,0,16, weight(0.25)|head_armor(3),imodbit_tattered | imodbit_ragged | imodbit_sturdy | imodbit_thick],
["court_hat", "Turret Hat", [("court_hat",0)], itp_type_head_armor  |itp_civilian|itp_fit_to_head ,0, 80 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ], 
["wimple_a", "Wimple", [("wimple_a_new",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_fit_to_head,0,10, weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["wimple_with_veil", "Wimple with Veil", [("wimple_b_new",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_fit_to_head,0,10, weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["straw_hat", "Straw Hat", [("straw_hat_new",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["common_hood", "Hood", [("hood_new",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["hood_b", "Hood", [("hood_b",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["hood_c", "Hood", [("hood_c",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["hood_d", "Hood", [("hood_d",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["headcloth", "Headcloth", [("headcloth_a_new",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["woolen_hood", "Woolen Hood", [("woolen_hood",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["arming_cap", "Arming Cap", [("arming_cap_a_new",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 5 , weight(1)|abundance(100)|head_armor(7)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["m_arming_cap_a", "Brown Padded Arming Cap", [("Arming_Cap_A",0),("Arming_Cap_A.1",0)], itp_merchandise| itp_type_head_armor  |itp_civilian|itp_attach_armature ,0, 49 , weight(2)|abundance(100)|head_armor(12)|body_armor(3)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["m_arming_cap_b", "Red Padded Arming Cap", [("Arming_Cap_B",0),("Arming_Cap_B.1",0)], itp_merchandise| itp_type_head_armor  |itp_civilian|itp_attach_armature ,0, 49 , weight(2)|abundance(100)|head_armor(12)|body_armor(3)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["m_arming_cap_c", "Black Padded Arming Cap", [("Arming_Cap_C",0),("Arming_Cap_C.1",0)], itp_merchandise| itp_type_head_armor  |itp_civilian|itp_attach_armature ,0, 49 , weight(2)|abundance(100)|head_armor(12)|body_armor(3)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["fur_hat", "Fur Hat", [("fur_hat_a_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["nomad_cap", "Nomad Cap", [("nomad_cap_a_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["nomad_cap_b", "Nomad Cap", [("nomad_cap_b_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(13)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["steppe_cap", "Steppe Cap", [("steppe_cap_a_new",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 14 , weight(1)|abundance(100)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["padded_coif", "Padded Coif", [("padded_coif_a_new",0)], itp_merchandise| itp_type_head_armor   ,0, 6 , weight(1)|abundance(100)|head_armor(11)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["m_padded_coif_a", "Padded Coif", [("Padded_Coif_A",0),("Padded_Coif_A.1",0)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 61 , weight(2)|abundance(100)|head_armor(15)|body_armor(3)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["m_padded_coif_b", "Black Padded Coif", [("Padded_Coif_B",0),("Padded_Coif_B.1",0)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 61 , weight(2)|abundance(100)|head_armor(15)|body_armor(3)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["woolen_cap", "Woolen Cap", [("woolen_cap_new",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 2 , weight(1)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["felt_hat", "Felt Hat", [("felt_hat_a_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["felt_hat_b", "Felt Hat", [("felt_hat_b_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["itm_felt_hat_a", "Forester Felt Hat", [("Felt_A",0),("Felt_A.1",0),("Felt_A.2",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_attach_armature,0, 45 , weight(2)|abundance(100)|head_armor(12)|body_armor(3)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["itm_felt_hat_b", "Forester Felt Hat", [("Felt_B",0),("Felt_B.1",0),("Felt_B.2",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_attach_armature,0, 45 , weight(2)|abundance(100)|head_armor(12)|body_armor(3)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["itm_felt_hat_c", "Forester Felt Hat", [("Felt_C",0),("Felt_C.1",0),("Felt_C.2",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_attach_armature,0, 36 , weight(2)|abundance(100)|head_armor(10)|body_armor(2)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["itm_felt_hat_d", "Forester Felt Hat", [("Felt_D",0),("Felt_D.1",0),("Felt_D.2",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_attach_armature,0, 36 , weight(2)|abundance(100)|head_armor(10)|body_armor(2)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["leather_cap", "Leather Cap", [("leather_cap_a_new",0)], itp_merchandise| itp_type_head_armor|itp_civilian ,0, 8, weight(1)|abundance(100)|head_armor(18)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["female_hood", "Lady's Hood", [("ladys_hood_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 9 , weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["leather_steppe_cap_a", "Steppe Cap", [("leather_steppe_cap_a_new",0)], itp_merchandise|itp_type_head_armor   ,0, 
24 , weight(1)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["leather_steppe_cap_b", "Steppe Cap ", [("tattered_steppe_cap_b_new",0)], itp_merchandise|itp_type_head_armor   ,0, 
36 , weight(1)|abundance(100)|head_armor(16)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["leather_steppe_cap_c", "Steppe Cap", [("steppe_cap_a_new",0)], itp_merchandise|itp_type_head_armor   ,0, 51 , weight(1)|abundance(100)|head_armor(16)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["leather_warrior_cap", "Leather Warrior Cap", [("skull_cap_new_b",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 14 , weight(1)|abundance(100)|head_armor(18)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["skullcap", "Skullcap", [("skull_cap_new_a",0)], itp_merchandise| itp_type_head_armor   ,0, 60 , weight(1.0)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ],
["mail_coif", "Mail Coif", [("mail_coif_new",0)], itp_merchandise| itp_type_head_armor   ,0, 71 , weight(1.25)|abundance(100)|head_armor(22)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_armor ],
["footman_helmet", "Footman's Helmet", [("skull_cap_new",0)], itp_merchandise| itp_type_head_armor   ,0, 95 , weight(1.5)|abundance(100)|head_armor(24)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ],
#missing...
["nasal_helmet", "Nasal Helmet", [("nasal_helmet_b",0)], itp_merchandise| itp_type_head_armor   ,0, 121 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["norman_helmet", "Helmet with Cap", [("norman_helmet_a",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head ,0, 147 , weight(1.25)|abundance(100)|head_armor(28)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["segmented_helmet", "Segmented Helmet", [("segmented_helm_new",0)], itp_merchandise| itp_type_head_armor   ,0, 174 , weight(1.25)|abundance(100)|head_armor(31)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["helmet_with_neckguard", "Helmet with Neckguard", [("neckguard_helm_new",0)], itp_merchandise| itp_type_head_armor   ,0, 
190 , weight(1.5)|abundance(100)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["flat_topped_helmet", "Flat Topped Helmet", [("flattop_helmet_new",0)], itp_merchandise| itp_type_head_armor   ,0, 
203 , weight(1.75)|abundance(100)|head_armor(33)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["kettle_hat", "Kettle Hat", [("kettle_hat_new",0)], itp_merchandise| itp_type_head_armor,0, 
240 , weight(1.75)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["spiked_helmet", "Spiked Helmet", [("spiked_helmet_new",0)], itp_merchandise| itp_type_head_armor   ,0, 278 , weight(2)|abundance(100)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["nordic_helmet", "Nordic Helmet", [("helmet_w_eyeguard_new",0)], itp_merchandise| itp_type_head_armor   ,0, 340 , weight(2)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["khergit_lady_hat", "Khergit Lady Hat", [("khergit_lady_hat",0)],  itp_type_head_armor   |itp_civilian |itp_doesnt_cover_hair | itp_fit_to_head,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["khergit_lady_hat_b", "Khergit Lady Leather Hat", [("khergit_lady_hat_b",0)], itp_type_head_armor  | itp_doesnt_cover_hair | itp_fit_to_head  |itp_civilian ,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["sarranid_felt_hat", "Sarranid Felt Hat", [("sar_helmet3",0)], itp_merchandise| itp_type_head_armor   ,0, 16 , weight(2)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_cloth ],
["turban", "Turban", [("tuareg_open",0)], itp_merchandise| itp_type_head_armor   ,0, 28 , weight(1)|abundance(100)|head_armor(11)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_cloth ],
["desert_turban", "Desert Turban", [("tuareg",0)], itp_merchandise| itp_type_head_armor | itp_covers_beard ,0, 38 , weight(1.50)|abundance(100)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_cloth ],
["sarranid_warrior_cap", "Sarranid Warrior Cap", [("tuareg_helmet",0)], itp_merchandise| itp_type_head_armor | itp_covers_beard  ,0, 90 , weight(2)|abundance(100)|head_armor(19)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["sarranid_horseman_helmet", "Horseman Helmet", [("sar_helmet2",0)], itp_merchandise| itp_type_head_armor   ,0, 180 , weight(2.75)|abundance(100)|head_armor(25)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["sarranid_helmet1", "Sarranid Keffiyeh Helmet", [("sar_helmet1",0)], itp_merchandise| itp_type_head_armor   ,0, 290 , weight(2.50)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["sarranid_mail_coif", "Sarranid Mail Coif", [("tuareg_helmet2",0)], itp_merchandise| itp_type_head_armor ,0, 430 , weight(3)|abundance(100)|head_armor(41)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["sarranid_veiled_helmet", "Sarranid Veiled Helmet", [("sar_helmet4",0)], itp_merchandise| itp_type_head_armor | itp_covers_beard  ,0, 810 , weight(3.50)|abundance(100)|head_armor(47)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["nordic_archer_helmet", "Nordic Leather Helmet", [("Helmet_A_vs2",0)], itp_merchandise| itp_type_head_armor    ,0, 40 , weight(1.25)|abundance(100)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["nordic_veteran_archer_helmet", "Nordic Leather Helmet", [("Helmet_A",0)], itp_merchandise| itp_type_head_armor,0, 70 , weight(1.5)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["nordic_footman_helmet", "Nordic Footman Helmet", [("Helmet_B_vs2",0)], itp_merchandise| itp_type_head_armor |itp_fit_to_head ,0, 150 , weight(1.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["nordic_fighter_helmet", "Nordic Fighter Helmet", [("Helmet_B",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head ,0, 240 , weight(2)|abundance(100)|head_armor(34)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["nordic_huscarl_helmet", "Nordic Huscarl's Helmet", [("Helmet_C_vs2",0)], itp_merchandise| itp_type_head_armor   ,0, 390 , weight(2)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["nordic_warlord_helmet", "Nordic Warlord Helmet", [("Helmet_C",0)], itp_merchandise| itp_type_head_armor ,0, 880 , weight(2.25)|abundance(100)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],

["vaegir_fur_cap", "Cap with Fur", [("vaeg_helmet3",0)], itp_merchandise| itp_type_head_armor   ,0, 50 , weight(1)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["vaegir_fur_helmet", "Vaegir Helmet", [("vaeg_helmet2",0)], itp_merchandise| itp_type_head_armor   ,0, 110 , weight(2)|abundance(100)|head_armor(21)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["vaegir_spiked_helmet", "Spiked Cap", [("vaeg_helmet1",0)], itp_merchandise| itp_type_head_armor   ,0, 230 , weight(2.50)|abundance(100)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["vaegir_lamellar_helmet", "Helmet with Lamellar Guard", [("vaeg_helmet4",0)], itp_merchandise| itp_type_head_armor   ,0, 360 , weight(2.75)|abundance(100)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["vaegir_noble_helmet", "Vaegir Nobleman Helmet", [("vaeg_helmet7",0)], itp_merchandise| itp_type_head_armor   ,0, 710, weight(2.75)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["vaegir_war_helmet", "Vaegir War Helmet", [("vaeg_helmet6",0)], itp_merchandise| itp_type_head_armor   ,0, 820 , weight(3)|abundance(100)|head_armor(47)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["vaegir_mask", "Vaegir War Mask", [("vaeg_helmet9",0)], itp_merchandise| itp_type_head_armor |itp_covers_beard ,0, 950 , weight(3.50)|abundance(100)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],

#TODO:
#["skullcap_b", "Skullcap_b", [("skull_cap_new_b",0)], itp_merchandise| itp_type_head_armor   ,0, 71 , weight(1.5)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ],
 
["bascinet", "Bascinet", [("bascinet_avt_new",0)], itp_merchandise|itp_type_head_armor   ,0, 479 , weight(2.25)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["bascinet_2", "Bascinet with Aventail", [("bascinet_new_a",0)], itp_merchandise|itp_type_head_armor   ,0, 479 , weight(2.25)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["bascinet_3", "Bascinet with Nose Guard", [("bascinet_new_b",0)], itp_merchandise|itp_type_head_armor   ,0, 479 , weight(2.25)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["guard_helmet", "Guard Helmet", [("reinf_helmet_new",0)], itp_merchandise| itp_type_head_armor   ,0, 555 , weight(2.5)|abundance(100)|head_armor(47)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["black_helmet", "Black Helmet", [("black_helm",0)], itp_type_head_armor,0, 638 , weight(2.75)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["full_helm", "Full Helm", [("great_helmet_new_b",0)], itp_merchandise| itp_type_head_armor |itp_covers_head ,0, 811 , weight(2.5)|abundance(100)|head_armor(51)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["great_helmet", "Great Helmet", [("great_helmet_new",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0, 980 , weight(2.75)|abundance(100)|head_armor(53)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["winged_great_helmet", "Winged Great Helmet", [("maciejowski_helmet_new",0)], itp_merchandise|itp_type_head_armor|itp_covers_head,0, 1240 , weight(2.75)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],


#WEAPONS
["wooden_stick",         "Wooden Stick", [("wooden_stick",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar, 
4 , weight(2.5)|difficulty(0)|spd_rtng(99) | weapon_length(63)|swing_damage(13 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
["cudgel",         "Cudgel", [("club",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar, 
4 , weight(2.5)|difficulty(0)|spd_rtng(99) | weapon_length(70)|swing_damage(13 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
["hammer",         "Hammer", [("iron_hammer_new",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar, 
7 , weight(2)|difficulty(0)|spd_rtng(100) | weapon_length(55)|swing_damage(24 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["club",         "Club", [("club",0)], itp_type_one_handed_wpn|itp_merchandise| itp_can_knock_down|itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar, 
11 , weight(2.5)|difficulty(0)|spd_rtng(98) | weapon_length(70)|swing_damage(20 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
["winged_mace",         "Flanged Mace", [("flanged_mace",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
122 , weight(3.5)|difficulty(0)|spd_rtng(103) | weapon_length(70)|swing_damage(24 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["spiked_mace",         "Spiked Mace", [("spiked_mace_new",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
180 , weight(3.5)|difficulty(0)|spd_rtng(98) | weapon_length(70)|swing_damage(28 , blunt) | thrust_damage(0 ,  pierce),imodbits_pick ],
["military_hammer", "Military Hammer", [("military_hammer",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
317 , weight(2)|difficulty(0)|spd_rtng(95) | weapon_length(70)|swing_damage(31 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["maul",         "Maul", [("maul_b",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down |itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear, 
97 , weight(6)|difficulty(11)|spd_rtng(83) | weapon_length(79)|swing_damage(36 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["sledgehammer", "Sledgehammer", [("maul_c",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear, 
101 , weight(7)|difficulty(12)|spd_rtng(81) | weapon_length(82)|swing_damage(39, blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["warhammer",         "Great Hammer", [("maul_d",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear, 
290 , weight(9)|difficulty(14)|spd_rtng(79) | weapon_length(75)|swing_damage(45 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["pickaxe",         "Pickaxe", [("fighting_pick_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
27 , weight(3)|difficulty(0)|spd_rtng(99) | weapon_length(70)|swing_damage(19 , pierce) | thrust_damage(0 ,  pierce),imodbits_pick ],
["spiked_club",         "Spiked Club", [("spiked_club",0)], itp_type_one_handed_wpn|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
83 , weight(3)|difficulty(0)|spd_rtng(97) | weapon_length(70)|swing_damage(21 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],
["fighting_pick", "Fighting Pick", [("fighting_pick_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
108 , weight(1.0)|difficulty(0)|spd_rtng(98) | weapon_length(70)|swing_damage(22 , pierce) | thrust_damage(0 ,  pierce),imodbits_pick ],
["military_pick", "Military Pick", [("steel_pick_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
280 , weight(1.5)|difficulty(0)|spd_rtng(97) | weapon_length(70)|swing_damage(31 , pierce) | thrust_damage(0 ,  pierce),imodbits_pick ],
["morningstar",         "Morningstar", [("mace_morningstar_new",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry|itp_unbalanced, itc_morningstar|itcf_carry_mace_left_hip, 
305 , weight(4.5)|difficulty(13)|spd_rtng(95) | weapon_length(85)|swing_damage(38 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],


["sickle",         "Sickle", [("sickle",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry|itp_wooden_parry, itc_cleaver, 
9 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(40)|swing_damage(20 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["cleaver",         "Cleaver", [("cleaver_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry|itp_wooden_parry, itc_cleaver, 
14 , weight(1.5)|difficulty(0)|spd_rtng(103) | weapon_length(35)|swing_damage(24 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["knife",         "Knife", [("peasant_knife_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left, 
18 , weight(0.5)|difficulty(0)|spd_rtng(110) | weapon_length(40)|swing_damage(21 , cut) | thrust_damage(13 ,  pierce),imodbits_sword ],
["butchering_knife", "Butchering Knife", [("khyber_knife_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_right, 
23 , weight(0.75)|difficulty(0)|spd_rtng(108) | weapon_length(60)|swing_damage(24 , cut) | thrust_damage(17 ,  pierce),imodbits_sword ],
["dagger",         "Dagger", [("dagger_b",0),("dagger_b_scabbard",ixmesh_carry),("dagger_b",imodbits_good),("dagger_b_scabbard",ixmesh_carry|imodbits_good)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn, 
37 , weight(0.75)|difficulty(0)|spd_rtng(109) | weapon_length(47)|swing_damage(22 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high ],
#["nordic_sword", "Nordic Sword", [("viking_sword",0),("scab_vikingsw", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 142 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(98)|swing_damage(27 , cut) | thrust_damage(19 ,  pierce),imodbits_sword ],
#["arming_sword", "Arming Sword", [("b_long_sword",0),("scab_longsw_b", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 156 , weight(1.5)|difficulty(0)|spd_rtng(101) | weapon_length(100)|swing_damage(25 , cut) | thrust_damage(22 ,  pierce),imodbits_sword ],
#["sword",         "Sword", [("long_sword",0),("scab_longsw_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 148 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(102)|swing_damage(26 , cut) | thrust_damage(23 ,  pierce),imodbits_sword ],
["falchion",         "Falchion", [("falchion_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 
105 , weight(2.5)|difficulty(8)|spd_rtng(98) | weapon_length(73)|swing_damage(30 , cut) | thrust_damage(0 ,  pierce),imodbits_sword ],
#["broadsword",         "Broadsword", [("broadsword",0),("scab_broadsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 122 , weight(2.5)|difficulty(8)|spd_rtng(91) | weapon_length(101)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_sword ],
#["scimitar",         "Scimitar", [("scimeter",0),("scab_scimeter", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
#108 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(97)|swing_damage(29 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],

["scimitar",         "Scimitar", [("scimitar_a",0),("scab_scimeter_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(1.5)|difficulty(0)|spd_rtng(101) | weapon_length(97)|swing_damage(30 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],
["scimitar_b",         "Elite Scimitar", [("scimitar_b",0),("scab_scimeter_b", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
290 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(103)|swing_damage(32 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],

["arabian_sword_a",         "Sarranid Sword", [("arabian_sword_a",0),("scab_arabian_sword_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
108 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(97)|swing_damage(26 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high ],
["arabian_sword_b",         "Sarranid Arming Sword", [("arabian_sword_b",0),("scab_arabian_sword_b", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
218 , weight(1.7)|difficulty(0)|spd_rtng(99) | weapon_length(97)|swing_damage(28 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high ],
["sarranid_cavalry_sword",         "Sarranid Cavalry Sword", [("arabian_sword_c",0),("scab_arabian_sword_c", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
310 , weight(1.5)|difficulty(0)|spd_rtng(98) | weapon_length(105)|swing_damage(28 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high ],
["arabian_sword_d",         "Sarranid Guard Sword", [("arabian_sword_d",0),("scab_arabian_sword_d", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
420 , weight(1.7)|difficulty(0)|spd_rtng(99) | weapon_length(97)|swing_damage(30 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ],


#["nomad_sabre",         "Nomad Sabre", [("shashqa",0),("scab_shashqa", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 115 , weight(1.75)|difficulty(0)|spd_rtng(101) | weapon_length(100)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_sword ],
#["bastard_sword", "Bastard Sword", [("bastard_sword",0),("scab_bastardsw", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 279 , weight(2.25)|difficulty(9)|spd_rtng(102) | weapon_length(120)|swing_damage(33 , cut) | thrust_damage(27 ,  pierce),imodbits_sword ],
["great_sword",         "Great Sword", [("b_bastard_sword",0),("scab_bastardsw_b", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back|itcf_show_holster_when_drawn,
 423 , weight(2.75)|difficulty(10)|spd_rtng(95) | weapon_length(125)|swing_damage(39 , cut) | thrust_damage(31 ,  pierce),imodbits_sword_high ],
["sword_of_war", "Sword of War", [("b_bastard_sword",0),("scab_bastardsw_b", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back|itcf_show_holster_when_drawn,
 524 , weight(3)|difficulty(11)|spd_rtng(94) | weapon_length(130)|swing_damage(40 , cut) | thrust_damage(31 ,  pierce),imodbits_sword_high ],
["hatchet",         "Hatchet", [("hatchet_k2",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
13 , weight(2)|difficulty(0)|spd_rtng(97) | weapon_length(60)|swing_damage(23 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["hand_axe",         "Hand Axe", [("hatchet_k2",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
24 , weight(2)|difficulty(7)|spd_rtng(95) | weapon_length(75)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["fighting_axe", "Fighting Axe", [("fighting_ax",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
77 , weight(2.5)|difficulty(9)|spd_rtng(92) | weapon_length(90)|swing_damage(31 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["axe",                 "Axe", [("iron_ax",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 
65 , weight(4)|difficulty(8)|spd_rtng(91) | weapon_length(108)|swing_damage(32 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["voulge_short",         "Voulge", [("voulge",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 
129 , weight(4.5)|difficulty(8)|spd_rtng(87) | weapon_length(119)|swing_damage(35 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["battle_axe",         "Battle Axe", [("battle_ax",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 
240 , weight(5)|difficulty(9)|spd_rtng(88) | weapon_length(108)|swing_damage(41 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["war_axe",         "War Axe", [("war_ax",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 
264 , weight(5)|difficulty(10)|spd_rtng(86) | weapon_length(110)|swing_damage(43 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
#["double_axe",         "Double Axe", [("dblhead_ax",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 359 , weight(6.5)|difficulty(12)|spd_rtng(85) | weapon_length(95)|swing_damage(43 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
#["great_axe",         "Great Axe", [("great_ax",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 415 , weight(7)|difficulty(13)|spd_rtng(82) | weapon_length(120)|swing_damage(45 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["sword_two_handed_b",         "Two Handed Sword", [("sword_two_handed_b",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back,
 670 , weight(2.75)|difficulty(10)|spd_rtng(97) | weapon_length(110)|swing_damage(40 , cut) | thrust_damage(28 ,  pierce),imodbits_sword_high ],
["sword_two_handed_a",         "Great Sword", [("sword_two_handed_a",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back,
 1123 , weight(2.75)|difficulty(10)|spd_rtng(96) | weapon_length(120)|swing_damage(42 , cut) | thrust_damage(29 ,  pierce),imodbits_sword_high ],


["khergit_sword_two_handed_a",         "Two Handed Sabre", [("khergit_sword_two_handed_a",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back,
 523 , weight(2.75)|difficulty(10)|spd_rtng(96) | weapon_length(120)|swing_damage(40 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],
["khergit_sword_two_handed_b",         "Two Handed Sabre", [("khergit_sword_two_handed_b",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back,
 920 , weight(2.75)|difficulty(10)|spd_rtng(96) | weapon_length(120)|swing_damage(44 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],

["two_handed_cleaver", "War Cleaver", [("military_cleaver_a",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back,
 640 , weight(2.75)|difficulty(10)|spd_rtng(93) | weapon_length(120)|swing_damage(45 , cut) | thrust_damage(0 ,  cut),imodbits_sword_high ],
["military_cleaver_b", "Soldier's Cleaver", [("military_cleaver_b",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip,
 193 , weight(1.5)|difficulty(0)|spd_rtng(96) | weapon_length(95)|swing_damage(31 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],
["military_cleaver_c", "Military Cleaver", [("military_cleaver_c",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip,
 263 , weight(1.5)|difficulty(0)|spd_rtng(96) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],

["military_sickle_a", "Military Sickle", [("military_sickle_a",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 220 , weight(1.0)|difficulty(9)|spd_rtng(100) | weapon_length(75)|swing_damage(26 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe ],


["bastard_sword_a", "Bastard Sword", [("bastard_sword_a",0),("bastard_sword_a_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 294 , weight(2.0)|difficulty(9)|spd_rtng(98) | weapon_length(101)|swing_damage(35 , cut) | thrust_damage(26 ,  pierce),imodbits_sword_high ],
["bastard_sword_b", "Heavy Bastard Sword", [("bastard_sword_b",0),("bastard_sword_b_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 526 , weight(2.25)|difficulty(9)|spd_rtng(97) | weapon_length(105)|swing_damage(37 , cut) | thrust_damage(27 ,  pierce),imodbits_sword_high ],

["one_handed_war_axe_a", "One Handed Axe", [("one_handed_war_axe_a",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 87 , weight(1.5)|difficulty(9)|spd_rtng(98) | weapon_length(71)|swing_damage(32 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["one_handed_battle_axe_a", "One Handed Battle Axe", [("one_handed_battle_axe_a",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 142 , weight(1.5)|difficulty(9)|spd_rtng(98) | weapon_length(73)|swing_damage(34 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["one_handed_war_axe_b", "One Handed War Axe", [("one_handed_war_axe_b",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 190 , weight(1.5)|difficulty(9)|spd_rtng(98) | weapon_length(76)|swing_damage(34 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["one_handed_battle_axe_b", "One Handed Battle Axe", [("one_handed_battle_axe_b",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 230 , weight(1.75)|difficulty(9)|spd_rtng(98) | weapon_length(72)|swing_damage(36 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["one_handed_battle_axe_c", "One Handed Battle Axe", [("one_handed_battle_axe_c",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 550 , weight(2.0)|difficulty(9)|spd_rtng(98) | weapon_length(76)|swing_damage(37 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],


["two_handed_axe",         "Two Handed Axe", [("two_handed_battle_axe_a",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 90 , weight(4.5)|difficulty(10)|spd_rtng(96) | weapon_length(90)|swing_damage(38 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["two_handed_battle_axe_2",         "Two Handed War Axe", [("two_handed_battle_axe_b",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 152 , weight(4.5)|difficulty(10)|spd_rtng(96) | weapon_length(92)|swing_damage(44 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["shortened_voulge",         "Shortened Voulge", [("two_handed_battle_axe_c",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 228 , weight(4.5)|difficulty(10)|spd_rtng(92) | weapon_length(100)|swing_damage(45 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["great_axe",         "Great Axe", [("two_handed_battle_axe_e",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 316 , weight(4.5)|difficulty(10)|spd_rtng(94) | weapon_length(96)|swing_damage(47 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["long_axe",         "Long Axe", [("long_axe_a",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_next_item_as_melee|itp_unbalanced|itp_merchandise,itc_staff|itcf_carry_axe_back,
 390 , weight(4.75)|difficulty(10)|spd_rtng(93) | weapon_length(120)|swing_damage(46 , cut) | thrust_damage(19 ,  blunt),imodbits_axe ],
["long_axe_alt",         "Long Axe", [("long_axe_a",0)],itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 390 , weight(4.75)|difficulty(10)|spd_rtng(88) | weapon_length(120)|swing_damage(46 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["long_axe_b",         "Long War Axe", [("long_axe_b",0)], itp_type_polearm| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_next_item_as_melee|itp_unbalanced|itp_merchandise, itc_staff|itcf_carry_axe_back,
 510 , weight(5.0)|difficulty(10)|spd_rtng(92) | weapon_length(125)|swing_damage(50 , cut) | thrust_damage(18 ,  blunt),imodbits_axe ],
["long_axe_b_alt",         "Long War Axe", [("long_axe_b",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 510 , weight(5.0)|difficulty(10)|spd_rtng(87) | weapon_length(125)|swing_damage(50 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["long_axe_c",         "Great Long Axe", [("long_axe_c",0)], itp_type_polearm| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_next_item_as_melee|itp_unbalanced|itp_merchandise, itc_staff|itcf_carry_axe_back,
 660 , weight(5.5)|difficulty(10)|spd_rtng(91) | weapon_length(127)|swing_damage(54 , cut) | thrust_damage(19 ,  blunt),imodbits_axe ],
["long_axe_c_alt",      "Great Long Axe", [("long_axe_c",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 660 , weight(5.5)|difficulty(10)|spd_rtng(85) | weapon_length(127)|swing_damage(54 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

 ["bardiche",         "Bardiche", [("two_handed_battle_axe_d",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 291 , weight(4.75)|difficulty(10)|spd_rtng(91) | weapon_length(102)|swing_damage(47 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["great_bardiche",         "Great Bardiche", [("two_handed_battle_axe_f",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 617 , weight(5.0)|difficulty(10)|spd_rtng(89) | weapon_length(116)|swing_damage(50 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],




["voulge",         "Voulge", [("two_handed_battle_long_axe_a",0)], itp_type_polearm|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_staff,
 120 , weight(3.0)|difficulty(10)|spd_rtng(88) | weapon_length(175)|swing_damage(40 , cut) | thrust_damage(18 ,  pierce),imodbits_axe ],
["long_bardiche",         "Long Bardiche", [("two_handed_battle_long_axe_b",0)], itp_type_polearm|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_staff,
390 , weight(4.75)|difficulty(11)|spd_rtng(89) | weapon_length(140)|swing_damage(48 , cut) | thrust_damage(17 ,  pierce),imodbits_axe ],
["great_long_bardiche",         "Great Long Bardiche", [("two_handed_battle_long_axe_c",0)], itp_type_polearm|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_staff,
 660 , weight(5.0)|difficulty(12)|spd_rtng(88) | weapon_length(155)|swing_damage(50 , cut) | thrust_damage(17 ,  pierce),imodbits_axe ],

 ["hafted_blade_b",         "Hafted Blade", [("khergit_pike_b",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry, itcf_carry_spear|itc_guandao,
 185 , weight(2.75)|difficulty(0)|spd_rtng(95) | weapon_length(135)|swing_damage(37 , cut) | thrust_damage(20 ,  pierce),imodbits_polearm ],
 ["hafted_blade_a",         "Hafted Blade", [("khergit_pike_a",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry, itcf_carry_spear|itc_guandao,
 350 , weight(3.25)|difficulty(0)|spd_rtng(93) | weapon_length(153)|swing_damage(39 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm ],

["shortened_military_scythe",         "Shortened Military Scythe", [("two_handed_battle_scythe_a",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back,
 264 , weight(3.0)|difficulty(10)|spd_rtng(90) | weapon_length(112)|swing_damage(45 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],

["sword_medieval_a", "Sword", [("sword_medieval_a",0),("sword_medieval_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 163 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(27 , cut) | thrust_damage(22 ,  pierce),imodbits_sword_high ],
#["sword_medieval_a_long", "Sword", [("sword_medieval_a_long",0),("sword_medieval_a_long_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 156 , weight(1.5)|difficulty(0)|spd_rtng(97) | weapon_length(105)|swing_damage(25 , cut) | thrust_damage(22 ,  pierce),imodbits_sword ],
["sword_medieval_b", "Sword", [("sword_medieval_b",0),("sword_medieval_b_scabbard", ixmesh_carry),("sword_rusty_a",imodbit_rusty),("sword_rusty_a_scabbard", ixmesh_carry|imodbit_rusty)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 243 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(28 , cut) | thrust_damage(23 ,  pierce),imodbits_sword_high ],
["sword_medieval_b_small", "Short Sword", [("sword_medieval_b_small",0),("sword_medieval_b_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 152 , weight(1)|difficulty(0)|spd_rtng(102) | weapon_length(85)|swing_damage(26, cut) | thrust_damage(24, pierce),imodbits_sword_high ],
["sword_medieval_c", "Arming Sword", [("sword_medieval_c",0),("sword_medieval_c_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 410 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(29 , cut) | thrust_damage(24 ,  pierce),imodbits_sword_high ],
["sword_medieval_c_small", "Short Arming Sword", [("sword_medieval_c_small",0),("sword_medieval_c_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 243 , weight(1)|difficulty(0)|spd_rtng(103) | weapon_length(86)|swing_damage(26, cut) | thrust_damage(24 ,  pierce),imodbits_sword_high ],
["sword_medieval_c_long", "Arming Sword", [("sword_medieval_c_long",0),("sword_medieval_c_long_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 480 , weight(1.7)|difficulty(0)|spd_rtng(99) | weapon_length(100)|swing_damage(29 , cut) | thrust_damage(28 ,  pierce),imodbits_sword_high ],
["sword_medieval_d_long", "Long Arming Sword", [("sword_medieval_d_long",0),("sword_medieval_d_long_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 550 , weight(1.8)|difficulty(0)|spd_rtng(96) | weapon_length(105)|swing_damage(33 , cut) | thrust_damage(28 ,  pierce),imodbits_sword ],
 
#["sword_medieval_d", "sword_medieval_d", [("sword_medieval_d",0),("sword_medieval_d_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
# 131 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(24 , cut) | thrust_damage(21 ,  pierce),imodbits_sword ],
#["sword_medieval_e", "sword_medieval_e", [("sword_medieval_e",0),("sword_medieval_e_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
# 131 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(24 , cut) | thrust_damage(21 ,  pierce),imodbits_sword ],

["sword_viking_1", "Nordic Sword", [("sword_viking_c",0),("sword_viking_c_scabbard ", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 147 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(94)|swing_damage(28 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ] ,
["sword_viking_2", "Nordic Sword", [("sword_viking_b",0),("sword_viking_b_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 276 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(29 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high ],
["sword_viking_2_small", "Nordic Short Sword", [("sword_viking_b_small",0),("sword_viking_b_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 162 , weight(1.25)|difficulty(0)|spd_rtng(103) | weapon_length(85)|swing_damage(28 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high ],
["sword_viking_3", "Nordic War Sword", [("sword_viking_a",0),("sword_viking_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 394 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(30 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high ],
#["sword_viking_a_long", "sword_viking_a_long", [("sword_viking_a_long",0),("sword_viking_a_long_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
# 142 , weight(1.5)|difficulty(0)|spd_rtng(97) | weapon_length(105)|swing_damage(27 , cut) | thrust_damage(19 ,  pierce),imodbits_sword ],
["sword_viking_3_small", "Nordic Short War Sword", [("sword_viking_a_small",0),("sword_viking_a_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 280 , weight(1.25)|difficulty(0)|spd_rtng(103) | weapon_length(86)|swing_damage(29 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high ],
#["sword_viking_c_long", "sword_viking_c_long", [("sword_viking_c_long",0),("sword_viking_c_long_scabbard ", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
# 142 , weight(1.5)|difficulty(0)|spd_rtng(95) | weapon_length(105)|swing_damage(27 , cut) | thrust_damage(19 ,  pierce),imodbits_sword ] ,

["sword_khergit_1", "Nomad Sabre", [("khergit_sword_b",0),("khergit_sword_b_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 105 , weight(1.25)|difficulty(0)|spd_rtng(100) | weapon_length(97)|swing_damage(29 , cut),imodbits_sword_high ],
["sword_khergit_2", "Sabre", [("khergit_sword_c",0),("khergit_sword_c_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 191 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(97)|swing_damage(30 , cut),imodbits_sword_high ],
["sword_khergit_3", "Sabre", [("khergit_sword_a",0),("khergit_sword_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 294 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(98)|swing_damage(31 , cut),imodbits_sword_high ],
["sword_khergit_4", "Heavy Sabre", [("khergit_sword_d",0),("khergit_sword_d_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 384 , weight(1.75)|difficulty(0)|spd_rtng(98) | weapon_length(96)|swing_damage(33 , cut),imodbits_sword_high ],



["mace_1",         "Spiked Club", [("mace_d",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
 45 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(70)|swing_damage(19 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],
["mace_2",         "Knobbed_Mace", [("mace_a",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
 98 , weight(2.5)|difficulty(0)|spd_rtng(98) | weapon_length(70)|swing_damage(21 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["mace_3",         "Spiked Mace", [("mace_c",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
 152 , weight(2.75)|difficulty(0)|spd_rtng(98) | weapon_length(70)|swing_damage(23 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["mace_4",         "Winged_Mace", [("mace_b",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
 212 , weight(2.75)|difficulty(0)|spd_rtng(98) | weapon_length(70)|swing_damage(24 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
# Goedendag
 ["club_with_spike_head",  "Spiked Staff", [("mace_e",0)],  itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_wooden_parry, itc_bastardsword|itcf_carry_axe_back,
 200 , weight(2.80)|difficulty(9)|spd_rtng(95) | weapon_length(117)|swing_damage(24 , blunt) | thrust_damage(20 ,  pierce),imodbits_mace ],

["long_spiked_club",         "Long Spiked Club", [("mace_long_c",0)], itp_type_polearm|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_axe_back,
 264 , weight(3)|difficulty(0)|spd_rtng(96) | weapon_length(126)|swing_damage(23 , pierce) | thrust_damage(20 ,  blunt),imodbits_mace ],
["long_hafted_knobbed_mace",         "Long Hafted Knobbed Mace", [("mace_long_a",0)], itp_type_polearm| itp_can_knock_down|itp_primary|itp_wooden_parry, itc_staff|itcf_carry_axe_back,
 324 , weight(3)|difficulty(0)|spd_rtng(95) | weapon_length(133)|swing_damage(26 , blunt) | thrust_damage(23 ,  blunt),imodbits_mace ],
["long_hafted_spiked_mace",         "Long Hafted Spiked Mace", [("mace_long_b",0)], itp_type_polearm|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_axe_back,
 310 , weight(3)|difficulty(0)|spd_rtng(94) | weapon_length(140)|swing_damage(28 , blunt) | thrust_damage(26 ,  blunt),imodbits_mace ],

["sarranid_two_handed_mace_1",         "Iron Mace", [("mace_long_d",0)], itp_type_two_handed_wpn|itp_can_knock_down|itp_two_handed|itp_merchandise| itp_primary|itp_crush_through|itp_unbalanced, itc_greatsword|itcf_carry_axe_back,
470 , weight(4.5)|difficulty(0)|spd_rtng(90) | weapon_length(95)|swing_damage(35 , blunt) | thrust_damage(22 ,  blunt),imodbits_mace ],


["sarranid_mace_1",         "Iron Mace", [("mace_small_d",0)], itp_type_one_handed_wpn|itp_merchandise|itp_can_knock_down |itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
 45 , weight(2.0)|difficulty(0)|spd_rtng(99) | weapon_length(73)|swing_damage(22 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["sarranid_axe_a", "Iron Battle Axe", [("one_handed_battle_axe_g",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 250 , weight(1.65)|difficulty(9)|spd_rtng(97) | weapon_length(71)|swing_damage(35 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["sarranid_axe_b", "Iron War Axe", [("one_handed_battle_axe_h",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 360 , weight(1.75)|difficulty(9)|spd_rtng(97) | weapon_length(71)|swing_damage(38 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["sarranid_two_handed_axe_a",         "Sarranid Battle Axe", [("two_handed_battle_axe_g",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 350 , weight(3.0)|difficulty(10)|spd_rtng(89) | weapon_length(95)|swing_damage(49 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["sarranid_two_handed_axe_b",         "Sarranid War Axe", [("two_handed_battle_axe_h",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 280 , weight(2.50)|difficulty(10)|spd_rtng(90) | weapon_length(90)|swing_damage(46 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],




["scythe",         "Scythe", [("scythe",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff|itcf_carry_spear, 43 , weight(2)|difficulty(0)|spd_rtng(97) | weapon_length(182)|swing_damage(30 , cut) | thrust_damage(14 ,  pierce),imodbits_polearm ],
["pitch_fork",         "Pitch Fork", [("pitch_fork",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry,itc_staff, 19 , weight(1.5)|difficulty(0)|spd_rtng(87) | weapon_length(154)|swing_damage(16 , blunt) | thrust_damage(22 ,  pierce),imodbits_polearm ],
["military_fork", "Military Fork", [("military_fork",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry,itc_staff, 153 , weight(2)|difficulty(0)|spd_rtng(95) | weapon_length(135)|swing_damage(15 , blunt) | thrust_damage(30 ,  pierce),imodbits_polearm ],
["battle_fork",         "Battle Fork", [("battle_fork",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry,itc_staff, 282 , weight(2.2)|difficulty(0)|spd_rtng(90) | weapon_length(144)|swing_damage(15, blunt) | thrust_damage(35 ,  pierce),imodbits_polearm ],
["boar_spear",         "Boar Spear", [("spear",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry,itc_staff|itcf_carry_spear, 
76 , weight(1.5)|difficulty(0)|spd_rtng(90) | weapon_length(157)|swing_damage(26 , cut) | thrust_damage(23 ,  pierce),imodbits_polearm ],
#["spear",         "Spear", [("spear",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear, 173 , weight(4.5)|difficulty(0)|spd_rtng(80) | weapon_length(158)|swing_damage(17 , blunt) | thrust_damage(23 ,  pierce),imodbits_polearm ],


["jousting_lance", "Jousting Lance", [("joust_of_peace",0)], itp_couchable|itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_greatlance, 158 , weight(5)|difficulty(0)|spd_rtng(61) | weapon_length(240)|swing_damage(0 , cut) | thrust_damage(17 ,  blunt),imodbits_polearm ],
#["lance",         "Lance", [("pike",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear, 196 , weight(5)|difficulty(0)|spd_rtng(72) | weapon_length(170)|swing_damage(0 , cut) | thrust_damage(20 ,  pierce),imodbits_polearm ],
["double_sided_lance", "Double Sided Lance", [("lance_dblhead",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff, 261 , weight(4.0)|difficulty(0)|spd_rtng(95) | weapon_length(128)|swing_damage(25, cut) | thrust_damage(27 ,  pierce),imodbits_polearm ],
#["pike",         "Pike", [("pike",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_spear,
# 212 , weight(6)|difficulty(0)|spd_rtng(77) | weapon_length(167)|swing_damage(0 , blunt) | thrust_damage(23 ,  pierce),imodbits_polearm ],
["glaive",         "Glaive", [("glaive_b",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_staff|itcf_carry_spear,
 352 , weight(4.5)|difficulty(0)|spd_rtng(90) | weapon_length(157)|swing_damage(39 , cut) | thrust_damage(21 ,  pierce),imodbits_polearm ],
["poleaxe",         "Poleaxe", [("pole_ax",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_staff,
 384 , weight(4.5)|difficulty(13)|spd_rtng(77) | weapon_length(180)|swing_damage(50 , cut) | thrust_damage(15 ,  blunt),imodbits_polearm ],
["polehammer",         "Polehammer", [("pole_hammer",0)], itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_wooden_parry, itc_staff,
 169 , weight(7)|difficulty(18)|spd_rtng(50) | weapon_length(126)|swing_damage(50 , blunt) | thrust_damage(35 ,  blunt),imodbits_polearm ],
["staff",         "Staff", [("wooden_staff",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_staff|itcf_carry_sword_back,
 36 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(130)|swing_damage(18 , blunt) | thrust_damage(19 ,  blunt),imodbits_polearm ],
["quarter_staff", "Quarter Staff", [("quarter_staff",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_staff|itcf_carry_sword_back,
 60 , weight(2)|difficulty(0)|spd_rtng(104) | weapon_length(140)|swing_damage(20 , blunt) | thrust_damage(20 ,  blunt),imodbits_polearm ],
["iron_staff",         "Iron Staff", [("iron_staff",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary, itc_staff|itcf_carry_sword_back,
 202 , weight(2)|difficulty(0)|spd_rtng(97) | weapon_length(140)|swing_damage(25 , blunt) | thrust_damage(26 ,  blunt),imodbits_polearm ],

#["glaive_b",         "Glaive_b", [("glaive_b",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_staff|itcf_carry_spear,
# 352 , weight(4.5)|difficulty(0)|spd_rtng(83) | weapon_length(157)|swing_damage(38 , cut) | thrust_damage(21 ,  pierce),imodbits_polearm ],


["shortened_spear",         "Shortened Spear", [("spear_g_1-9m",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear,
 53 , weight(2.0)|difficulty(0)|spd_rtng(102) | weapon_length(120)|swing_damage(19 , blunt) | thrust_damage(25 ,  pierce),imodbits_polearm ],
["spear",         "Spear", [("spear_h_2-15m",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear,
 85 , weight(2.25)|difficulty(0)|spd_rtng(98) | weapon_length(135)|swing_damage(20 , blunt) | thrust_damage(26 ,  pierce),imodbits_polearm ],

["bamboo_spear",         "Bamboo Spear", [("arabian_spear_a_3m",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff|itcf_carry_spear,
 80 , weight(2.0)|difficulty(0)|spd_rtng(88) | weapon_length(200)|swing_damage(15 , blunt) | thrust_damage(20 ,  pierce),imodbits_polearm ],




["war_spear",         "War Spear", [("spear_i_2-3m",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear,
 140 , weight(2.5)|difficulty(0)|spd_rtng(95) | weapon_length(150)|swing_damage(20 , blunt) | thrust_damage(27 ,  pierce),imodbits_polearm ],
#TODO:["shortened_spear",         "shortened_spear", [("spear_e_2-1m",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear,
# 65 , weight(2.0)|difficulty(0)|spd_rtng(98) | weapon_length(110)|swing_damage(17 , blunt) | thrust_damage(23 ,  pierce),imodbits_polearm ],
#TODO:["spear_2-4m",         "spear", [("spear_e_2-25m",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff|itcf_carry_spear,
# 67 , weight(2.0)|difficulty(0)|spd_rtng(95) | weapon_length(125)|swing_damage(17 , blunt) | thrust_damage(23 ,  pierce),imodbits_polearm ],
["military_scythe",         "Military Scythe", [("spear_e_2-5m",0),("spear_c_2-5m",imodbits_bad)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff|itcf_carry_spear,
 155 , weight(2.5)|difficulty(0)|spd_rtng(90) | weapon_length(155)|swing_damage(36 , cut) | thrust_damage(25 ,  pierce),imodbits_polearm ],
["light_lance",         "Light Lance", [("spear_b_2-75m",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,
 180 , weight(2.5)|difficulty(0)|spd_rtng(85) | weapon_length(175)|swing_damage(16 , blunt) | thrust_damage(27 ,  pierce),imodbits_polearm ],
["lance",         "Lance", [("spear_d_2-8m",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,
 270 , weight(2.5)|difficulty(0)|spd_rtng(80) | weapon_length(180)|swing_damage(16 , blunt) | thrust_damage(26 ,  pierce),imodbits_polearm ],
["heavy_lance",         "Heavy Lance", [("spear_f_2-9m",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,
 360 , weight(2.75)|difficulty(10)|spd_rtng(75) | weapon_length(190)|swing_damage(16 , blunt) | thrust_damage(26 ,  pierce),imodbits_polearm ],
["great_lance",         "Great Lance", [("heavy_lance",0)], itp_couchable|itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_greatlance, 
 410 , weight(5)|difficulty(11)|spd_rtng(55) | weapon_length(240)|swing_damage(0 , cut) | thrust_damage(21 ,  pierce),imodbits_polearm ],
["pike",         "Pike", [("spear_a_3m",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed, itc_cutting_spear,
 125 , weight(3.0)|difficulty(0)|spd_rtng(81) | weapon_length(245)|swing_damage(16 , blunt) | thrust_damage(26 ,  pierce),imodbits_polearm ],
##["spear_e_3-25m",         "Spear_3-25m", [("spear_e_3-25m",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear,
## 150 , weight(4.5)|difficulty(0)|spd_rtng(81) | weapon_length(225)|swing_damage(19 , blunt) | thrust_damage(23 ,  pierce),imodbits_polearm ],
["ashwood_pike", "Ashwood Pike", [("pike",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_cutting_spear,
 205 , weight(3.5)|difficulty(9)|spd_rtng(90) | weapon_length(170)|swing_damage(19 , blunt) | thrust_damage(29,  pierce),imodbits_polearm ],
["awlpike",    "Awlpike", [("awl_pike_b",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear,
 345 , weight(2.25)|difficulty(0)|spd_rtng(92) | weapon_length(165)|swing_damage(20 , blunt) | thrust_damage(33 ,  pierce),imodbits_polearm ],
["awlpike_long",  "Long Awlpike", [("awl_pike_a",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear,
 385 , weight(2.25)|difficulty(0)|spd_rtng(89) | weapon_length(185)|swing_damage(20 , blunt) | thrust_damage(32 ,  pierce),imodbits_polearm ],
#["awlpike",         "Awlpike", [("pike",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear,
# 378 , weight(3.5)|difficulty(12)|spd_rtng(92) | weapon_length(160)|swing_damage(20 ,blunt) | thrust_damage(31 ,  pierce),imodbits_polearm ],

["bec_de_corbin_a",  "War Hammer", [("bec_de_corbin_a",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed, itc_cutting_spear|itcf_carry_spear,
 125 , weight(3.0)|difficulty(0)|spd_rtng(81) | weapon_length(120)|swing_damage(38, blunt) | thrust_damage(38 ,  pierce),imodbits_polearm ],



# SHIELDS

["wooden_shield", "Wooden Shield", [("shield_round_a",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
##["wooden_shield", "Wooden Shield", [("shield_round_a",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield,




#["round_shield", "Round Shield", [("shield_round_c",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  64 , weight(2)|hit_points(400)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
["nordic_shield", "Nordic Shield", [("shield_round_b",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  95 , weight(2)|hit_points(440)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
#["kite_shield",         "Kite Shield", [("shield_kite_a",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
#["kite_shield_", "Kite Shield", [("shield_kite_b",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
#["large_shield", "Large Shield", [("shield_kite_c",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  165 , weight(2.5)|hit_points(520)|body_armor(1)|spd_rtng(80)|shield_width(92),imodbits_shield ],
#["battle_shield", "Battle Shield", [("shield_kite_d",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  196 , weight(3)|hit_points(560)|body_armor(1)|spd_rtng(78)|shield_width(94),imodbits_shield ],
["fur_covered_shield",  "Fur Covered Shield", [("shield_kite_m",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  227 , weight(3.5)|hit_points(600)|body_armor(1)|spd_rtng(76)|shield_width(81),imodbits_shield ],
#["heraldric_shield", "Heraldric Shield", [("shield_heraldic",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  301 , weight(3.5)|hit_points(640)|body_armor(1)|spd_rtng(83)|shield_width(65),imodbits_shield ],
#["heater_shield", "Heater Shield", [("shield_heater_a",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  477 , weight(3.5)|hit_points(710)|body_armor(4)|spd_rtng(80)|shield_width(60),imodbits_shield ],
["steel_shield", "Steel Shield", [("shield_dragon",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,  697 , weight(4)|hit_points(700)|body_armor(17)|spd_rtng(61)|shield_width(40),imodbits_shield ],
#["nomad_shield", "Nomad Shield", [("shield_wood_b",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  12 , weight(2)|hit_points(260)|body_armor(6)|spd_rtng(110)|shield_width(30),imodbits_shield ],

["plate_covered_round_shield", "Plate Covered Round Shield", [("shield_round_e",0)], itp_type_shield, itcf_carry_round_shield,  140 , weight(4)|hit_points(330)|body_armor(16)|spd_rtng(90)|shield_width(40),imodbits_shield ],
["leather_covered_round_shield", "Leather Covered Round Shield", [("shield_round_d",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  80 , weight(2.5)|hit_points(310)|body_armor(8)|spd_rtng(96)|shield_width(40),imodbits_shield ],
["hide_covered_round_shield", "Hide Covered Round Shield", [("shield_round_f",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  40 , weight(2)|hit_points(260)|body_armor(3)|spd_rtng(100)|shield_width(40),imodbits_shield ],

["shield_heater_c", "Heater Shield", [("shield_heater_c",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  277 , weight(3.5)|hit_points(410)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
#["shield_heater_d", "Heater Shield", [("shield_heater_d",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  477 , weight(3.5)|hit_points(710)|body_armor(4)|spd_rtng(80)|shield_width(60),imodbits_shield ],

#["shield_kite_g",         "Kite Shield g", [("shield_kite_g",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
#["shield_kite_h",         "Kite Shield h", [("shield_kite_h",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
#["shield_kite_i",         "Kite Shield i ", [("shield_kite_i",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
#["shield_kite_k",         "Kite Shield k", [("shield_kite_k",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],

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

["tab_shield_small_round_a", "Plain Cavalry Shield", [("tableau_shield_small_round_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  
96 , weight(2)|hit_points(160)|body_armor(8)|spd_rtng(105)|shield_width(40),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_3", ":agent_no", ":troop_no")])]],
["tab_shield_small_round_b", "Round Cavalry Shield", [("tableau_shield_small_round_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  
195 , weight(2.5)|hit_points(200)|body_armor(14)|spd_rtng(103)|shield_width(40),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_small_round_c", "Elite Cavalry Shield", [("tableau_shield_small_round_2",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,  
370 , weight(3)|hit_points(250)|body_armor(22)|spd_rtng(100)|shield_width(40),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_2", ":agent_no", ":troop_no")])]],


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
#TODO: Light Trowing axe, Heavy Throwing Axe
["light_throwing_axes", "Light Throwing Axes", [("francisca",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee,itcf_throw_axe,
360, weight(5)|difficulty(2)|spd_rtng(99) | shoot_speed(18) | thrust_damage(35,cut)|max_ammo(4)|weapon_length(53),imodbits_thrown_minus_heavy ],
["light_throwing_axes_melee", "Light Throwing Axe", [("francisca",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar,
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
["hunting_crossbow", "Hunting Crossbow", [("crossbow_a",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 
22 , weight(2.25)|difficulty(0)|spd_rtng(47) | shoot_speed(50) | thrust_damage(37 ,  pierce)|max_ammo(1),imodbits_crossbow ],
["light_crossbow", "Light Crossbow", [("crossbow_b",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 
67 , weight(2.5)|difficulty(8)|spd_rtng(45) | shoot_speed(59) | thrust_damage(44 ,  pierce)|max_ammo(1),imodbits_crossbow ],
["crossbow",         "Crossbow",         [("crossbow_a",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 
182 , weight(3)|difficulty(8)|spd_rtng(43) | shoot_speed(66) | thrust_damage(49,pierce)|max_ammo(1),imodbits_crossbow ],
["heavy_crossbow", "Heavy Crossbow", [("crossbow_c",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 
349 , weight(3.5)|difficulty(9)|spd_rtng(41) | shoot_speed(68) | thrust_damage(58 ,pierce)|max_ammo(1),imodbits_crossbow ],
["sniper_crossbow", "Siege Crossbow", [("crossbow_c",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 
683 , weight(3.75)|difficulty(10)|spd_rtng(37) | shoot_speed(70) | thrust_damage(63 ,pierce)|max_ammo(1),imodbits_crossbow ],
["flintlock_pistol", "Flintlock Pistol", [("flintlock_pistol",0)], itp_type_pistol |itp_merchandise|itp_primary ,itcf_shoot_pistol|itcf_reload_pistol, 230 , weight(1.5)|difficulty(0)|spd_rtng(38) | shoot_speed(160) | thrust_damage(45 ,pierce)|max_ammo(1)|accuracy(65),imodbits_none,
 [(ti_on_weapon_attack, [(play_sound,"snd_pistol_shot"),(position_move_x, pos1,27),(position_move_y, pos1,36),(particle_system_burst, "psys_pistol_smoke", pos1, 15)])]],
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
["rich_outfit", "Rich Outfit", [("merchant_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
["khergit_guard_armor", "Khergit Guard Armor", [("lamellar_armor_a",0)], itp_type_body_armor|itp_covers_legs   ,0, 
3048 , weight(25)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(18)|difficulty(0) ,imodbits_armor ],
#["leather_steppe_cap_c", "Leather Steppe Cap", [("leather_steppe_cap_c",0)], itp_type_head_armor   ,0, 51 , weight(2)|abundance(100)|head_armor(18)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["felt_steppe_cap", "Felt Steppe Cap", [("felt_steppe_cap",0)], itp_type_head_armor   ,0, 237 , weight(2)|abundance(100)|head_armor(16)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["khergit_war_helmet", "Khergit War Helmet", [("tattered_steppe_cap_a_new",0)], itp_type_head_armor | itp_merchandise   ,0, 200 , weight(2)|abundance(100)|head_armor(31)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["khergit_helmet", "Khergit Helmet", [("khergit_guard_helmet",0)], itp_type_head_armor   ,0, 361 , weight(2)|abundance(100)|head_armor(33)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
#["khergit_sword", "Khergit Sword", [("khergit_sword",0),("khergit_sword_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 183 , weight(1.25)|difficulty(0)|spd_rtng(100) | weapon_length(97)|swing_damage(23 , cut) | thrust_damage(14 ,  pierce),imodbits_sword ],
["khergit_guard_boots",  "Khergit Guard Boots", [("lamellar_boots_a",0)], itp_type_foot_armor | itp_attach_armature,0, 254 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_cloth ],
["khergit_guard_helmet", "Khergit Guard Helmet", [("lamellar_helmet_a",0)], itp_type_head_armor |itp_merchandise   ,0, 433 , weight(2)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["khergit_cavalry_helmet", "Khergit Cavalry Helmet", [("lamellar_helmet_b",0)], itp_type_head_armor | itp_merchandise   ,0, 333 , weight(2)|abundance(100)|head_armor(36)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],

["black_hood", "Black Hood", [("hood_black",0)], itp_type_head_armor|itp_merchandise   ,0, 193 , weight(2)|abundance(100)|head_armor(18)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["light_leather", "Light Leather", [("light_leather",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 352 , weight(5)|abundance(100)|head_armor(0)|body_armor(26)|leg_armor(7)|difficulty(0) ,imodbits_armor ],
["light_leather_boots",  "Light Leather Boots", [("light_leather_boots",0)], itp_type_foot_armor |itp_merchandise| itp_attach_armature,0, 91 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(15)|difficulty(0) ,imodbits_cloth ],
["mail_and_plate", "Mail and Plate", [("mail_and_plate",0)], itp_type_body_armor|itp_covers_legs   ,0, 593 , weight(16)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(12)|difficulty(0) ,imodbits_armor ],
["light_mail_and_plate", "Light Mail and Plate", [("light_mail_and_plate",0)], itp_type_body_armor|itp_covers_legs   ,0, 532 , weight(10)|abundance(100)|head_armor(0)|body_armor(32)|leg_armor(12)|difficulty(0) ,imodbits_armor ],

["byzantion_helmet_a", "Byzantion Helmet", [("byzantion_helmet_a",0)], itp_type_head_armor   ,0, 278 , weight(2)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["magyar_helmet_a", "Magyar Helmet", [("magyar_helmet_a",0)], itp_type_head_armor   ,0, 278 , weight(2)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["rus_helmet_a", "Rus Helmet", [("rus_helmet_a",0)], itp_type_head_armor   ,0, 278 , weight(2)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["sipahi_helmet_a", "Sipahi Helmet", [("sipahi_helmet_a",0)], itp_type_head_armor   ,0, 278 , weight(2)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["shahi", "Shahi", [("shahi",0)], itp_type_head_armor   ,0, 278 , weight(2)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["rabati", "Rabati", [("rabati",0)], itp_type_head_armor   ,0, 278 , weight(2)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],

["tunic_with_green_cape", "Tunic with Green Cape", [("peasant_man_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ], 
["keys", "Ring of Keys", [("throwing_axe_a",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar,
240, weight(5)|spd_rtng(98) | swing_damage(29,cut)|max_ammo(5)|weapon_length(53),imodbits_thrown ], 
["bride_dress", "Bride Dress", [("bride_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["bride_crown", "Crown of Flowers", [("bride_crown",0)],  itp_type_head_armor | itp_doesnt_cover_hair |itp_civilian |itp_attach_armature,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["bride_shoes", "Bride Shoes", [("bride_shoes",0)], itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 30 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],

["practice_bow_2","Practice Bow", [("hunting_bow",0), ("hunting_bow_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bow_back, 0, weight(1.5)|spd_rtng(90) | shoot_speed(40) | thrust_damage(21, blunt),imodbits_bow ],
["practice_arrows_2","Practice Arrows", [("arena_arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(80),imodbits_missile],


["plate_boots", "Plate Boots", [("plate_boots",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
 1770 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_plate ], 

["heraldic_mail_with_surcoat_for_tableau", "{!}Heraldic Mail with Surcoat", [("heraldic_armor_new_a",0)], itp_type_body_armor |itp_covers_legs ,0,
 1, weight(22)|abundance(100)|head_armor(0)|body_armor(1)|leg_armor(1),imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_a", ":agent_no", ":troop_no")])]],
["mail_boots_for_tableau", "Mail Boots", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1, weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["warhorse_sarranid","Sarranian War Horse", [("warhorse_sarranid",0)], itp_merchandise|itp_type_horse, 0, 1811,abundance(40)|hit_points(165)|body_armor(58)|difficulty(4)|horse_speed(40)|horse_maneuver(44)|horse_charge(32)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_6]],
["warhorse_steppe","Steppe Charger", [("warhorse_steppe",0)], itp_merchandise|itp_type_horse, 0, 1400,abundance(45)|hit_points(150)|body_armor(40)|difficulty(4)|horse_speed(40)|horse_maneuver(50)|horse_charge(28)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_3,fac_kingdom_2]],

# 15TH CENTURY WEAPONS PACK
###Weapons
##Polearms
["poleaxe_a", "Poleaxe", [("poleaxe_a",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_two_handed, itc_staff|itcf_carry_spear,
280 , weight(3.5)|difficulty(10)|spd_rtng(79) | weapon_length(144)|swing_damage(38, cut) | thrust_damage(36 , pierce),imodbits_polearm ],
["elegant_poleaxe", "Poleaxe", [("elegant_poleaxe",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_two_handed, itc_staff|itcf_carry_spear,
365 , weight(3.25)|difficulty(9)|spd_rtng(81) | weapon_length(139)|swing_damage(41, cut) | thrust_damage(38 , pierce),imodbits_polearm ],
["german_poleaxe", "German Poleaxe", [("german_poleaxe",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_two_handed, itc_staff|itcf_carry_spear,
255 , weight(3)|difficulty(8)|spd_rtng(82) | weapon_length(128)|swing_damage(37, cut) | thrust_damage(37 , pierce),imodbits_polearm ],
["simple_poleaxe", "Burgundian Poleaxe", [("simple_poleaxe",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_two_handed, itc_staff|itcf_carry_spear,
205 , weight(3.25)|difficulty(8)|spd_rtng(80) | weapon_length(135)|swing_damage(34, cut) | thrust_damage(39 , pierce),imodbits_polearm ],
["bec_de_corbin", "Bec de Corbin", [("bec_de_corbin",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_two_handed, itc_staff|itcf_carry_spear,
200 , weight(2.25)|difficulty(8)|spd_rtng(85) | weapon_length(120)|swing_damage(32, pierce) | thrust_damage(33 , pierce),imodbits_polearm ],
["english_bill", "English Bill", [("english_bill",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_two_handed, itc_staff|itcf_carry_spear,
170 , weight(3.25)|difficulty(12)|spd_rtng(75) | weapon_length(167)|swing_damage(44, cut) | thrust_damage(32 , pierce),imodbits_polearm ],
["swiss_halberd", "Swiss Halberd", [("swiss_halberd",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_two_handed, itc_cutting_spear|itcf_carry_spear,
230 , weight(3)|difficulty(11)|spd_rtng(76) | weapon_length(161)|swing_damage(46, cut) | thrust_damage(34 , pierce),imodbits_polearm ],
["guisarme", "Guisarme", [("guisarme_a",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_two_handed, itc_staff|itcf_carry_spear,
145 , weight(3)|difficulty(11)|spd_rtng(74) | weapon_length(164)|swing_damage(30, pierce) | thrust_damage(32 , pierce),imodbits_polearm ],
["german_hunting_spear", "German Hunting Spear", [("german_hunting_spear",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_two_handed, itc_staff|itcf_carry_spear,
120 , weight(1.75)|difficulty(0)|spd_rtng(92) | weapon_length(178)|swing_damage(19, blunt) | thrust_damage(34 , pierce),imodbits_polearm ],
["glaive_a", "Glaive", [("glaive1",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_two_handed, itc_staff|itcf_carry_spear,
245 , weight(2.5)|difficulty(9)|spd_rtng(82) | weapon_length(163)|swing_damage(31, cut) | thrust_damage(28 , pierce),imodbits_polearm ],
["glaive_b", "Glaive", [("glaive2",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_two_handed, itc_staff|itcf_carry_spear,
270 , weight(2.25)|difficulty(10)|spd_rtng(80) | weapon_length(170)|swing_damage(34, cut) | thrust_damage(29 , pierce),imodbits_polearm ],
["partisan", "Partisan", [("partisan",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_two_handed, itc_staff|itcf_carry_spear,
305 , weight(2)|difficulty(10)|spd_rtng(84) | weapon_length(158)|swing_damage(34, cut) | thrust_damage(34 , pierce),imodbits_polearm ],
##Swords
["longsword", "Longsword", [("longsword_b",0)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip,
345 , weight(2.0)|difficulty(9)|spd_rtng(97) | weapon_length(100)|swing_damage(36 , cut) | thrust_damage(29 , pierce),imodbits_sword_high ],
["danish_greatsword", "Danish Greatsword", [("danish_greatsword",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back,
458 , weight(3.0)|difficulty(10)|spd_rtng(96) | weapon_length(114)|swing_damage(42 , cut) | thrust_damage(33 , pierce),imodbits_sword_high ],
["espada_eslavona_a", "Espada Eslavona", [("espada_eslavona_a",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip,
203 , weight(1.75)|difficulty(0)|spd_rtng(99) | weapon_length(90)|swing_damage(29 , cut) | thrust_damage(23 , pierce),imodbits_sword_high ],
["espada_eslavona_b", "Espada Eslavona", [("espada_eslavona_b",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip,
245 , weight(2.0)|difficulty(0)|spd_rtng(97) | weapon_length(101)|swing_damage(31 , cut) | thrust_damage(24 , pierce),imodbits_sword_high ],
["english_longsword", "English Longsword", [("english_longsword",0),("english_longsword_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
370 , weight(2.0)|difficulty(9)|spd_rtng(97) | weapon_length(103)|swing_damage(37 , cut) | thrust_damage(32 , pierce),imodbits_sword_high ],
["german_bastard_sword", "German Bastard Sword", [("german_bastard_sword",0),("german_bastard_sword_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
355 , weight(2.0)|difficulty(9)|spd_rtng(97) | weapon_length(107)|swing_damage(36 , cut) | thrust_damage(33 , pierce),imodbits_sword_high ],
["italian_sword", "Italian Sword", [("italian_sword",0),("italian_sword_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
234 , weight(2.0)|difficulty(8)|spd_rtng(96) | weapon_length(98)|swing_damage(32 , cut) | thrust_damage(24 , pierce),imodbits_sword_high ],
["side_sword", "Side-sword", [("side_sword",0),("side_sword_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
280 , weight(2.0)|difficulty(0)|spd_rtng(98) | weapon_length(94)|swing_damage(30 , cut) | thrust_damage(28 , pierce),imodbits_sword_high ],
["milanese_sword", "Milanese Shortsword", [("milanese_sword",0),("milanese_sword_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
190 , weight(1.5)|difficulty(0)|spd_rtng(102) | weapon_length(76)|swing_damage(27 , cut) | thrust_damage(26 , pierce),imodbits_sword_high ],
["longbowman_sword", "Archer's Sword", [("longbowman_sword",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip,
165 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(83)|swing_damage(28 , cut) | thrust_damage(21 , pierce),imodbits_sword_high ],
["italian_falchion", "Italian Falchion", [("italian_falchion",0),("italian_falchion_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
215 , weight(1.5)|difficulty(0)|spd_rtng(104) | weapon_length(73)|swing_damage(32 , cut) | thrust_damage(20 , pierce),imodbits_sword_high ],
["scottish_sword", "Scottish Sword", [("scottish_sword",0),("scottish_sword_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
170 , weight(1.75)|difficulty(0)|spd_rtng(98) | weapon_length(81)|swing_damage(28 , cut) | thrust_damage(25 , pierce),imodbits_sword_high ],
["crusader_sword", "Crusader's Longsword", [("crusader_sword",0),("crusader_sword_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
310 , weight(2.0)|difficulty(9)|spd_rtng(97) | weapon_length(98)|swing_damage(33 , cut) | thrust_damage(31 , pierce),imodbits_sword_high ],
["grosse_messer", "Grosse Messer", [("grosse_messer",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip,
140 , weight(1.75)|difficulty(0)|spd_rtng(98) | weapon_length(86)|swing_damage(29 , cut) | thrust_damage(20 , pierce),imodbits_sword_high ],
["grosse_messer_b", "Grosse Messer", [("grosse_messer_b",0),("grosse_messer_b_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
185 , weight(2.0)|difficulty(9)|spd_rtng(98) | weapon_length(92)|swing_damage(35 , cut) | thrust_damage(24 , pierce),imodbits_sword_high ],
["irish_sword", "Irish Sword", [("irish_sword",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip,
200 , weight(2.0)|difficulty(0)|spd_rtng(96) | weapon_length(106)|swing_damage(27 , cut) | thrust_damage(25 , pierce),imodbits_sword_high ],
##Daggers/Knives
["bollock_dagger", "Bollock Dagger", [("bollock_dagger",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left,
75 , weight(1)|difficulty(0)|spd_rtng(109) | weapon_length(46)|swing_damage(21 , cut) | thrust_damage(22 , pierce),imodbits_sword_high ],
["pikeman_dagger", "Pikeman's Dagger", [("pikeman_dagger",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left,
64 , weight(1)|difficulty(0)|spd_rtng(108) | weapon_length(41)|swing_damage(23 , cut) | thrust_damage(19 , pierce),imodbits_sword_high ],
["rondel_dagger", "Rondel Dagger", [("rondel_dagger",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left,
91 , weight(1.5)|difficulty(0)|spd_rtng(106) | weapon_length(47)|swing_damage(24 , cut) | thrust_damage(22 , pierce),imodbits_sword_high ],

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

# New heraldic armors
["mail_long_surcoat_new_heraldic", "Heraldic Mail with Tabard", [("mail_long_surcoat_new_heraldic",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3412 , weight(21)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(16)|difficulty(7) ,imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_mail_long_surcoat_new", ":agent_no", ":troop_no")])]],

["mail_short_surcoat_new_heraldic", "Heraldic Mail with Tabard", [("heraldic_surcoat_over_mail_short",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3999 , weight(25)|abundance(100)|head_armor(0)|body_armor(53)|leg_armor(19)|difficulty(9) ,imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_surcoat_over_mail_short", ":agent_no", ":troop_no")])]],

["mail_tabard_heraldic", "Heraldic Mail with Tabard", [("tabard_b_heraldic",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3187 , weight(20)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(19)|difficulty(7) ,imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_tabard_b_heraldic", ":agent_no", ":troop_no")])]],

["brigandine_b_heraldic", "Heraldic Brigandine", [("brigandine_b_heraldic",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
 2230 , weight(20)|abundance(100)|head_armor(0)|body_armor(47)|leg_armor(16)|difficulty(10) ,imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_brigandine_b_heraldic_new", ":agent_no", ":troop_no")])]],
 
["heraldic_tunic_new", "Heraldic Tunic", [("heraldic_tunic_new",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
 2230 , weight(20)|abundance(100)|head_armor(0)|body_armor(47)|leg_armor(16)|difficulty(10) ,imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_short_tunic_new", ":agent_no", ":troop_no")])]],

# CWA Stuff
  ["axe_crusader_a","Knight War Axe", [("axe_crusader_a", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_bonus_against_shield, itcf_carry_axe_left_hip|itc_scimitar,550, weight(2)|abundance(100)|difficulty(9)|spd_rtng(95)|weapon_length(80)|thrust_damage(0, pierce)|swing_damage(36, cut), imodbits_none, [], [fac_kingdom_1]],
  ["axe_crusader_b","Knight War Axe", [("axe_crusader_b", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_bonus_against_shield, itcf_carry_axe_left_hip|itc_scimitar,650, weight(2)|abundance(100)|difficulty(9)|spd_rtng(98)|weapon_length(73)|thrust_damage(0, pierce)|swing_damage(34, cut), imodbits_none, [], [fac_kingdom_1]],
  ["axe_crusader_c","Knight War Axe", [("axe_crusader_c", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_bonus_against_shield, itcf_carry_axe_left_hip|itc_scimitar,750, weight(2)|abundance(100)|difficulty(9)|spd_rtng(90)|weapon_length(85)|thrust_damage(0, pierce)|swing_damage(38, cut), imodbits_none, [], [fac_kingdom_1]],
  ["axe_crusader_d","Knight War Axe", [("axe_crusader_d", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_bonus_against_shield|itp_crush_through|itp_can_knock_down, itcf_carry_axe_left_hip|itc_scimitar,850, weight(4.75)|abundance(100)|difficulty(9)|spd_rtng(90)|weapon_length(90)|thrust_damage(0, pierce)|swing_damage(44, cut), imodbits_none, [], [fac_kingdom_1]],
  ["axe_crusader_1","Knight War Axe", [("axe_crusader_1", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_bonus_against_shield|itp_crush_through|itp_can_knock_down, itcf_carry_axe_left_hip|itc_scimitar,1000, weight(4.25)|abundance(100)|difficulty(9)|spd_rtng(88)|weapon_length(88)|thrust_damage(0, pierce)|swing_damage(48, cut), imodbits_none, [], [fac_kingdom_1]],

  ["crusader_knight_spear_a","Knight Lance", [("crusader_knight_spear_a", 0),("invalid_item", ixmesh_carry),("crusader_knight_spear_a", ixmesh_carry|imodbit_cheap)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_covers_head, itcf_carry_revolver_right,410, weight(5)|abundance(100)|difficulty(11)|spd_rtng(55)|weapon_length(265)|thrust_damage(21, pierce), imodbits_none, [], [fac_kingdom_1]],
  ["crusader_knight_spear_a_2","Knight Lance Broken", [("crusader_knight_spear_a_2", 0),("invalid_item", ixmesh_carry),("crusader_knight_spear_a_2", ixmesh_carry|imodbit_cheap)], itp_type_polearm|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_no_pick_up_from_ground, itcf_carry_revolver_right,410, weight(4)|abundance(100)|difficulty(11)|spd_rtng(55)|weapon_length(170)|thrust_damage(5, blunt), imodbits_none, []],
  ["crusader_knight_spear_b","Knight Lance", [("crusader_knight_spear_b", 0),("invalid_item", ixmesh_carry),("crusader_knight_spear_b", ixmesh_carry|imodbit_cheap)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_covers_head, itcf_carry_revolver_right,410, weight(5)|abundance(100)|difficulty(11)|spd_rtng(55)|weapon_length(285)|thrust_damage(21, pierce), imodbits_none, [], [fac_kingdom_1]],
  ["crusader_knight_spear_b_2","Knight Lance Broken", [("crusader_knight_spear_b_2", 0),("invalid_item", ixmesh_carry),("crusader_knight_spear_b_2", ixmesh_carry|imodbit_cheap)], itp_type_polearm|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_no_pick_up_from_ground, itcf_carry_revolver_right,410, weight(4)|abundance(100)|difficulty(11)|spd_rtng(55)|weapon_length(170)|thrust_damage(5, blunt), imodbits_none, []],

  ["crusader_knight_spear_a_2_tip","Broken Knight Lance Tip", [("crusader_knight_spear_a_1", 0)], itp_type_one_handed_wpn|itp_primary, itcf_carry_sword_left_hip|itc_longsword,31, weight(3)|abundance(100)|spd_rtng(100)|weapon_length(70)|thrust_damage(19, pierce)|swing_damage(12, blunt), imodbits_none, [], [fac_kingdom_1]],

  ["crusader_long_sword_a","Long Sword", [("crusader_long_sword_a", 0),("crusader_long_sword_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itc_nodachi|itcf_overswing_onehanded|itcf_slashright_onehanded|itcf_slashleft_onehanded|itcf_show_holster_when_drawn,526, weight(4)|abundance(100)|spd_rtng(100)|weapon_length(100)|swing_damage(30, cut), imodbits_none, [], [fac_kingdom_1]],
  ["crusader_long_sword_b","Long Sword", [("crusader_long_sword_b", 0),("crusader_long_sword_b_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itc_nodachi|itcf_overswing_onehanded|itcf_slashright_onehanded|itcf_slashleft_onehanded|itcf_show_holster_when_drawn,526, weight(4)|abundance(100)|spd_rtng(100)|weapon_length(100)|swing_damage(30, cut), imodbits_none, [], [fac_kingdom_1]],
  ["crusader_long_sword_c","Long Sword", [("crusader_long_sword_c", 0),("crusader_long_sword_c_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itc_nodachi|itcf_overswing_onehanded|itcf_slashright_onehanded|itcf_slashleft_onehanded|itcf_show_holster_when_drawn,526, weight(4)|abundance(100)|spd_rtng(100)|weapon_length(100)|swing_damage(30, cut), imodbits_none, [], [fac_kingdom_1]],

  ["crusader_spear_a","Infantry Spear", [("crusader_spear_a", 0),("invalid_item", ixmesh_carry),("crusader_spear_c", ixmesh_carry|imodbit_cheap)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance, itcf_carry_revolver_right|itc_poleaxe|itcf_thrust_onehanded_lance|itcf_thrust_onehanded_lance_horseback,140, weight(2.5)|abundance(100)|spd_rtng(110)|weapon_length(180)|thrust_damage(27, pierce)|swing_damage(20, blunt), imodbits_none, []],
  ["crusader_spear_b","Infantry Spear", [("crusader_spear_b", 0),("invalid_item", ixmesh_carry),("crusader_spear_c", ixmesh_carry|imodbit_cheap)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance, itcf_carry_revolver_right|itc_poleaxe|itcf_thrust_onehanded_lance|itcf_thrust_onehanded_lance_horseback,140, weight(2.5)|abundance(100)|spd_rtng(110)|weapon_length(175)|thrust_damage(27, pierce)|swing_damage(20, blunt), imodbits_none, []],
  ["crusader_spear_c","Infantry Spear", [("crusader_spear_c", 0),("invalid_item", ixmesh_carry),("crusader_spear_c", ixmesh_carry|imodbit_cheap)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance, itcf_carry_revolver_right|itc_poleaxe|itcf_thrust_onehanded_lance|itcf_thrust_onehanded_lance_horseback,140, weight(2.5)|abundance(100)|spd_rtng(100)|weapon_length(170)|thrust_damage(27, pierce)|swing_damage(20, blunt), imodbits_none, []],
  ["crusader_spear_inf_a","Infantry Spear", [("crusader_spear_inf_a", 0),("invalid_item", ixmesh_carry),("crusader_spear_inf_a", ixmesh_carry|imodbit_cheap)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance, itc_poleaxe|itcf_thrust_onehanded_lance|itcf_thrust_onehanded_lance_horseback,140, weight(2.5)|abundance(100)|spd_rtng(100)|weapon_length(155)|thrust_damage(27, pierce)|swing_damage(20, blunt), imodbits_none, []],
  ["crusader_spear_inf_b","Infantry Spear", [("crusader_spear_inf_b", 0),("invalid_item", ixmesh_carry),("crusader_spear_inf_b", ixmesh_carry|imodbit_cheap)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance, itc_poleaxe|itcf_thrust_onehanded_lance|itcf_thrust_onehanded_lance_horseback,140, weight(2.5)|abundance(100)|spd_rtng(100)|weapon_length(160)|thrust_damage(27, pierce)|swing_damage(20, blunt), imodbits_none, []],
  ["crusader_spear_inf_c","Infantry Spear", [("crusader_spear_inf_c", 0),("invalid_item", ixmesh_carry),("crusader_spear_inf_c", ixmesh_carry|imodbit_cheap)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance, itc_poleaxe|itcf_thrust_onehanded_lance|itcf_thrust_onehanded_lance_horseback,140, weight(2.5)|abundance(100)|spd_rtng(100)|weapon_length(175)|thrust_damage(27, pierce)|swing_damage(20, blunt), imodbits_none, []],

  ["crusader_sword_a","Swort Sword", [("crusaders_swords_a", 0),("crusader_sword_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itcf_carry_sword_left_hip|itc_longsword|itcf_show_holster_when_drawn,0, weight(1.5)|abundance(100)|spd_rtng(105)|weapon_length(75)|thrust_damage(20, pierce)|swing_damage(28, cut), imodbits_none, []],
  ["crusader_sword_b","Sword", [("crusader_sword_b", 0),("crusader_sword_b_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itcf_carry_sword_left_hip|itc_longsword|itcf_show_holster_when_drawn,0, weight(1.5)|abundance(100)|spd_rtng(102)|weapon_length(86)|thrust_damage(20, pierce)|swing_damage(28, cut), imodbits_none, []],
  ["crusader_sword_c","Sword", [("crusader_sword_c", 0),("crusader_sword_c_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itcf_carry_sword_left_hip|itc_longsword|itcf_show_holster_when_drawn,0, weight(1.5)|abundance(100)|spd_rtng(102)|weapon_length(86)|thrust_damage(20, pierce)|swing_damage(28, cut), imodbits_none, []],

  ["falshion_1","Falshion", [("falshion_1", 0),("falshion_1_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itc_scimitar,200, weight(2)|abundance(100)|difficulty(8)|spd_rtng(100)|weapon_length(63)|thrust_damage(0, pierce)|swing_damage(28, cut), imodbits_none, [], [fac_kingdom_1]],
  ["falshion_2","Falshion", [("falshion_2", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itc_scimitar,105, weight(2.5)|abundance(100)|difficulty(8)|spd_rtng(96)|weapon_length(73)|thrust_damage(0, pierce)|swing_damage(28, cut), imodbits_none, [], [fac_kingdom_6]],

  ["k_long_sword_a","Knight Lognsword", [("k_long_sword_a", 0),("k_long_sword_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itc_nodachi|itcf_overswing_onehanded|itcf_slashright_onehanded|itcf_slashleft_onehanded|itcf_show_holster_when_drawn,526, weight(4)|abundance(100)|spd_rtng(100)|weapon_length(100)|swing_damage(30, cut), imodbits_none, [], [fac_kingdom_1]],
  ["k_long_sword_b","Knight Lognsword", [("k_long_sword_b", 0),("k_long_sword_b_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itc_nodachi|itcf_overswing_onehanded|itcf_slashright_onehanded|itcf_slashleft_onehanded|itcf_show_holster_when_drawn,526, weight(4)|abundance(100)|spd_rtng(100)|weapon_length(100)|swing_damage(30, cut), imodbits_none, [], [fac_kingdom_1]],
  ["k_long_sword_c","Knight Lognsword", [("k_long_sword_c", 0),("k_long_sword_c_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itc_nodachi|itcf_overswing_onehanded|itcf_slashright_onehanded|itcf_slashleft_onehanded|itcf_show_holster_when_drawn,526, weight(4)|abundance(100)|spd_rtng(100)|weapon_length(100)|swing_damage(30, cut), imodbits_none, [], [fac_kingdom_1]],

  ["mameluk_spears_a","Mameluk Spear", [("mameluk_spears_a", 0),("invalid_item", ixmesh_carry),("mameluk_spears_a", ixmesh_carry|imodbit_cheap)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance, itcf_carry_revolver_right|itc_poleaxe|itcf_thrust_onehanded_lance|itcf_thrust_onehanded_lance_horseback,140, weight(3.5)|abundance(100)|spd_rtng(90)|weapon_length(185)|thrust_damage(27, pierce)|swing_damage(20, blunt), imodbits_none, [], [fac_kingdom_6]],
  ["mameluk_spears_b","Mameluk Spear", [("mameluk_spears_b", 0),("invalid_item", ixmesh_carry),("mameluk_spears_b", ixmesh_carry|imodbit_cheap)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance, itcf_carry_revolver_right|itc_poleaxe|itcf_thrust_onehanded_lance|itcf_thrust_onehanded_lance_horseback,140, weight(2.5)|abundance(100)|spd_rtng(90)|weapon_length(185)|thrust_damage(27, pierce)|swing_damage(20, blunt), imodbits_none, [], [fac_kingdom_6]],
  ["mameluk_spears_c_v_1","Mameluk Spear", [("mameluk_spears_c_v_1", 0),("invalid_item", ixmesh_carry),("mameluk_spears_c_v_1", ixmesh_carry|imodbit_cheap)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance, itcf_carry_revolver_right|itc_cutting_spear,140, weight(4)|abundance(100)|spd_rtng(80)|weapon_length(200)|thrust_damage(32, pierce), imodbits_none, [], [fac_kingdom_6]],
  ["mameluk_spears_c","Mameluk Spear", [("mameluk_spears_c", 0),("invalid_item", ixmesh_carry),("mameluk_spears_c", ixmesh_carry|imodbit_cheap)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance, itcf_carry_revolver_right|itc_cutting_spear,140, weight(3.5)|abundance(100)|spd_rtng(80)|weapon_length(185)|thrust_damage(32, pierce), imodbits_none, [], [fac_kingdom_6]],

  ["saracin_spears_a","Footman Spear", [("saracin_spears_a", 0),("invalid_item", ixmesh_carry),("saracin_spears_a", ixmesh_carry|imodbit_cheap)], 0, itcf_carry_spear|itc_poleaxe|itcf_thrust_onehanded_lance|itcf_thrust_onehanded_lance_horseback,140, weight(3)|abundance(100)|spd_rtng(85)|weapon_length(165)|thrust_damage(27, pierce)|swing_damage(19, blunt), imodbits_none, [], [fac_kingdom_6]],
  ["saracin_spears_a_v_1","Shortened Footman Spear", [("saracin_spears_a_v_1", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance, itcf_carry_spear|itc_poleaxe|itcf_thrust_onehanded_lance|itcf_thrust_onehanded_lance_horseback,53, weight(2)|abundance(100)|spd_rtng(102)|weapon_length(125)|thrust_damage(25, pierce)|swing_damage(19, blunt), imodbits_none, [], [fac_kingdom_6]],

  ["saracin_sword_a","Sarranid Sword", [("saracin_sword_a", 0),("scab_saracin_sword_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itc_scimitar|itcf_show_holster_when_drawn,110, weight(1.25)|abundance(100)|spd_rtng(100)|weapon_length(100)|swing_damage(30, cut), imodbits_none, [], [fac_kingdom_6]],
  ["saracin_sword_b","Sarranid Sword", [("saracin_sword_b", 0),("scab_saracin_sword_b", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itc_scimitar|itcf_show_holster_when_drawn,110, weight(1.25)|abundance(100)|spd_rtng(100)|weapon_length(90)|swing_damage(30, cut), imodbits_none, [], [fac_kingdom_6]],
  ["saracin_sword_d","Sarranid Sword", [("saracin_sword_d", 0),("scab_saracin_sword_d", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itc_scimitar|itcf_show_holster_when_drawn,105, weight(1.25)|abundance(100)|spd_rtng(100)|weapon_length(103)|swing_damage(30, cut), imodbits_none, [], [fac_kingdom_6]],
  ["saracin_sword_c","Sarranid Sword", [("saracin_sword_c", 0),("scab_saracin_sword_c", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itc_scimitar|itcf_show_holster_when_drawn,110, weight(1.25)|abundance(100)|spd_rtng(100)|weapon_length(103)|swing_damage(30, cut), imodbits_none, [], [fac_kingdom_6]],
  ["saracin_sword_e","Sarranid Sword", [("saracin_sword_e", 0),("scab_saracin_sword_e", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itc_scimitar|itcf_show_holster_when_drawn,110, weight(1.25)|abundance(100)|spd_rtng(100)|weapon_length(103)|swing_damage(30, cut), imodbits_none, [], [fac_kingdom_6]],

  ["swadia_oval_shield_1","Oval Swadian Shield", [("shields_archer_tripoli_b", 0),("shields_archer_tripoli_d", imodbit_reinforced)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,70, weight(2)|abundance(100)|body_armor(1)|hit_points(165)|spd_rtng(100)|shield_width(36), imodbit_reinforced, [], [fac_kingdom_1]],
  ["swadia_oval_shield_2","Oval Swadian Shield", [("shields_archer_tripoli_a", 0),("shields_archer_tripoli_c", imodbit_reinforced)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_round_shield,70, weight(2)|abundance(100)|body_armor(1)|hit_points(165)|spd_rtng(100)|shield_width(36), imodbit_reinforced, [], [fac_kingdom_1]],
  ["swadia_kite_shield_1","Kite Swadian Shield", [("tripoli_shield_a", 0),("tripoli_shield_b", imodbit_reinforced),("tripoli_shield_e", imodbit_lordly)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield,205, weight(2)|abundance(100)|body_armor(14)|hit_points(180)|spd_rtng(103)|shield_height(50)|shield_width(30), imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_1]],
  ["swadia_kite_shield_2","Kite Swadian Shield", [("tripoli_shield_c", 0),("tripoli_shield_d", imodbit_reinforced),("tripoli_shield_e", imodbit_lordly)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield,205, weight(2)|abundance(100)|body_armor(14)|hit_points(180)|spd_rtng(103)|shield_height(50)|shield_width(30), imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_1]],
  ["swadia_footman_shield_1","Swadia Footman Shield", [("shield_veteran_tripoli_b", 0),("shield_veteran_tripoli_c", imodbit_reinforced),("shield_veteran_tripoli_d", imodbit_lordly)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield,700, weight(2)|abundance(100)|body_armor(25)|hit_points(370)|spd_rtng(80)|shield_height(110)|shield_width(38), imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_1]],
  ["swadia_footman_shield_2","Swadia Footman Shield", [("shield_veteran_tripoli_a", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield,700, weight(2)|abundance(100)|body_armor(25)|hit_points(370)|spd_rtng(80)|shield_height(110)|shield_width(38), imodbit_reinforced, [], [fac_kingdom_1]],
  ["swadia_footman_shield_3","Swadia Footman Shield", [("shield_veteran_tripoli_e", 0),("shield_veteran_tripoli_g", imodbit_reinforced)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield,700, weight(2)|abundance(100)|body_armor(25)|hit_points(370)|spd_rtng(80)|shield_height(110)|shield_width(38), imodbit_reinforced, [], [fac_kingdom_1]],
  ["swadia_footman_shield_4","Swadia Footman Shield", [("shield_veteran_tripoli_f", 0),("shield_veteran_tripoli_h", imodbit_reinforced)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield,700, weight(2)|abundance(100)|body_armor(25)|hit_points(370)|spd_rtng(80)|shield_height(110)|shield_width(38), imodbit_reinforced, [], [fac_kingdom_1]],
  ["swadia_heater_shield_1","Swadia Heater Shield", [("shield_knight_tripoli_a", 0),("shield_knight_tripoli_c", imodbit_reinforced)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield,500, weight(3)|abundance(100)|body_armor(17)|hit_points(300)|spd_rtng(98)|shield_height(50)|shield_width(32), imodbit_reinforced, [], [fac_kingdom_1]],
  ["swadia_heater_shield_2","Swadia Heater Shield", [("shield_knight_tripoli_b", 0),("shield_knight_tripoli_d", imodbit_reinforced)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_kite_shield,500, weight(3)|abundance(100)|body_armor(17)|hit_points(300)|spd_rtng(98)|shield_height(50)|shield_width(32), imodbit_reinforced, [], [fac_kingdom_1]],

["m_swadia_light_horse_a","Swadia Light Horse", [("European_horse_a",0), ("European_horse_a.1",0)], itp_merchandise|itp_type_horse, 0, 1299,abundance(50)|hit_points(165)|body_armor(30)|difficulty(3)|horse_speed(52)|horse_maneuver(50)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1]],
["m_swadia_light_horse_b","Swadia Light Horse", [("European_horse_b",0), ("European_horse_b.1",0)], itp_merchandise|itp_type_horse, 0, 1299,abundance(50)|hit_points(165)|body_armor(30)|difficulty(3)|horse_speed(52)|horse_maneuver(50)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1]],
["m_swadia_light_horse_c","Swadia Light Horse", [("European_horse_c",0), ("European_horse_c.1",0)], itp_merchandise|itp_type_horse, 0, 1299,abundance(50)|hit_points(165)|body_armor(30)|difficulty(3)|horse_speed(52)|horse_maneuver(50)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1]],
["m_swadia_light_horse_d","Swadia Light Horse", [("European_horse_d",0), ("European_horse_d.1",0)], itp_merchandise|itp_type_horse, 0, 1299,abundance(50)|hit_points(165)|body_armor(30)|difficulty(3)|horse_speed(52)|horse_maneuver(50)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1]],
["m_swadia_light_horse_e","Swadia Light Horse", [("European_horse_e",0), ("European_horse_e.1",0)], itp_merchandise|itp_type_horse, 0, 1299,abundance(50)|hit_points(165)|body_armor(30)|difficulty(3)|horse_speed(52)|horse_maneuver(50)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1]],
["m_swadia_light_horse_f","Swadia Light Horse", [("European_horse_f",0), ("European_horse_f.1",0)], itp_merchandise|itp_type_horse, 0, 1299,abundance(50)|hit_points(165)|body_armor(30)|difficulty(3)|horse_speed(52)|horse_maneuver(50)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1]],

["m_swadia_heavy_horse_a","Swadia Heavy Horse", [("tripoli_knight_horse_a",0), ("tripoli_knight_horse_a.1",0)], itp_merchandise|itp_type_horse, 0, 1499,abundance(50)|hit_points(165)|body_armor(50)|difficulty(4)|horse_speed(50)|horse_maneuver(45)|horse_charge(35)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1]],
["m_swadia_heavy_horse_b","Swadia Heavy Horse", [("tripoli_knight_horse_b",0), ("tripoli_knight_horse_b.1",0)], itp_merchandise|itp_type_horse, 0, 1499,abundance(50)|hit_points(165)|body_armor(50)|difficulty(4)|horse_speed(50)|horse_maneuver(45)|horse_charge(35)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1]],
["m_swadia_heavy_horse_c","Swadia Heavy Horse", [("tripoli_knight_horse_c",0), ("tripoli_knight_horse_c.1",0)], itp_merchandise|itp_type_horse, 0, 1499,abundance(50)|hit_points(165)|body_armor(50)|difficulty(4)|horse_speed(50)|horse_maneuver(45)|horse_charge(35)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1]],

["m_swadia_elite_horse_a","Swadia Elite Horse", [("Jerusalem_knight_horse_a",0), ("Jerusalem_knight_horse_a.1",0)], itp_merchandise|itp_type_horse, 0, 1699,abundance(50)|hit_points(175)|body_armor(60)|difficulty(5)|horse_speed(50)|horse_maneuver(45)|horse_charge(35)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1]],
["m_swadia_elite_horse_b","Swadia Elite Horse", [("Jerusalem_knight_horse_b",0), ("Jerusalem_knight_horse_b.1",0)], itp_merchandise|itp_type_horse, 0, 1699,abundance(50)|hit_points(175)|body_armor(60)|difficulty(5)|horse_speed(50)|horse_maneuver(45)|horse_charge(35)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1]],
["m_swadia_elite_horse_c","Swadia Elite Horse", [("Jerusalem_knight_horse_c",0), ("Jerusalem_knight_horse_c.1",0)], itp_merchandise|itp_type_horse, 0, 1699,abundance(50)|hit_points(175)|body_armor(60)|difficulty(5)|horse_speed(50)|horse_maneuver(45)|horse_charge(35)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1]],

["m_swadia_lord_horse_a","Swadia Elite Horse", [("Jerusalem_king_horse",0), ("Jerusalem_king_horse.1",0), ("Jerusalem_king_horse.2",0)], itp_merchandise|itp_type_horse, 0, 1899,abundance(50)|hit_points(185)|body_armor(70)|difficulty(6)|horse_speed(50)|horse_maneuver(45)|horse_charge(35)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1]],

["m_swadia_common_a", "Rusty Padded Armor", [("dethertir_armor_h",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 299 , weight(10)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(8)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_common_b", "Rusty Padded Armor", [("dethertir_armor_f",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 299 , weight(10)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(8)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],

["m_swadia_common_plated_a", "Rusty Padded Armor with Plates", [("swadia_padded_a",0), ("swadia_padded_a.1",0),("swadia_padded_a.2",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 799 , weight(16)|abundance(100)|head_armor(0)|body_armor(31)|leg_armor(8)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_common_plated_b", "Rusty Padded Armor with Plates", [("swadia_padded_b",0), ("swadia_padded_b.1",0),("swadia_padded_b.2",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 1455 , weight(18)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(15)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_common_plated_c", "Rusty Padded Armor with Plates", [("swadia_padded_c",0), ("swadia_padded_c.1",0),("swadia_padded_c.2",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 1455 , weight(18)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(15)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],

["m_swadia_common_mail_a", "Rusty Mail Armor", [("dethertir_armor_g",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 499 , weight(16)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(8)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_common_mail_b", "Rusty Mail Armor", [("dethertir_armor_c",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 499 , weight(16)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(8)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],

["m_swadia_common_knight_armor_a", "Old Knight Armor", [("dethertir_armor_a",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 1199 , weight(19)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(18)|difficulty(11) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_common_knight_armor_b", "Old Knight Armor", [("dethertir_armor_b",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 1199 , weight(19)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(18)|difficulty(11) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_common_knight_armor_c", "Old Knight Armor", [("dethertir_armor_d",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 1199 , weight(19)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(18)|difficulty(11) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_common_knight_armor_d", "Old Knight Armor", [("dethertir_armor_e",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 1199 , weight(19)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(18)|difficulty(11) ,imodbits_armor, [], [fac_kingdom_1] ],

["m_swadia_knight_plated_old_a", "Old Plated Knight Armor", [("swadia_coat_a",0),("swadia_coat_a.1",0),("swadia_coat_a.2",0),("swadia_coat_a.3",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 5899 , weight(25)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(23)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_knight_plated_old_b", "Old Plated Knight Armor", [("swadia_coat_b",0),("swadia_coat_b.1",0),("swadia_coat_b.2",0),("swadia_coat_b.3",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 5899 , weight(25)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(23)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_1] ],

["m_coif_cloth_a", "Black Coif", [("koif_monie_a",0)], itp_type_head_armor|itp_merchandise   ,0, 89 , weight(0.5)|abundance(100)|head_armor(12)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["m_coif_cloth_b", "Light Coif", [("koif_monie_b",0)], itp_type_head_armor|itp_merchandise   ,0, 89 , weight(0.5)|abundance(100)|head_armor(12)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],

["m_swadia_common_helmet_a", "Old Helmet", [("dethertir_helm_a",0),("dethertir_helm_a.1",0)], itp_type_head_armor|itp_merchandise   ,0, 864 , weight(1)|abundance(100)|head_armor(39)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_common_helmet_b", "Old Helmet", [("dethertir_helm_b",0),("dethertir_helm_b.1",0)], itp_type_head_armor|itp_merchandise   ,0, 599 , weight(1)|abundance(100)|head_armor(30)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_common_helmet_c", "Old Helmet", [("dethertir_helm_c",0),("dethertir_helm_c.1",0)], itp_type_head_armor|itp_merchandise   ,0, 599 , weight(1)|abundance(100)|head_armor(30)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],

["m_swadia_gloves_a","Old Gloves", [("dethertir_gloves_L",0)], itp_merchandise|itp_type_hand_armor,0, 399, weight(0.25)|abundance(100)|body_armor(3)|difficulty(0),imodbits_cloth, [], [fac_kingdom_1]],
["m_swadia_mail_gloves_a","Old Mail Gloves", [("dethertir_gauntlets_L",0)], itp_merchandise|itp_type_hand_armor,0, 399, weight(0.75)|abundance(100)|body_armor(5)|difficulty(0),imodbits_armor, [], [fac_kingdom_1]],

["m_swadia_elite_recruit_a", "Padded Vest", [("novici_Jerusalem",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 325 , weight(10)|abundance(100)|head_armor(0)|body_armor(24)|leg_armor(8)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_elite_recruit_b", "Padded Vest", [("armor_infantry_Jerusalem_a",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 409 , weight(10)|abundance(100)|head_armor(0)|body_armor(28)|leg_armor(13)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_elite_recruit_c", "Padded Vest", [("armor_infantry_Jerusalem_b",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 409 , weight(10)|abundance(100)|head_armor(0)|body_armor(28)|leg_armor(13)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_elite_recruit_d", "Padded Vest", [("archer_jerusalem_armor_a",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 399 , weight(10)|abundance(100)|head_armor(0)|body_armor(27)|leg_armor(13)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_elite_recruit_e", "Padded Vest", [("archer_jerusalem_armor_b",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 399 , weight(10)|abundance(100)|head_armor(0)|body_armor(27)|leg_armor(13)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],

["m_swadia_elite_recruit_plated_a", "Padded Vest", [("swadia_army_elite_a",0),("swadia_army_elite_a.1",0),("swadia_army_elite_a.2",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 1459 , weight(15)|abundance(100)|head_armor(0)|body_armor(31)|leg_armor(17)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_elite_recruit_plated_b", "Padded Vest", [("swadia_army_elite_b",0),("swadia_army_elite_b.1",0),("swadia_army_elite_b.2",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 1459 , weight(15)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(17)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_elite_recruit_plated_c", "Infantry Padded Vest", [("swadia_infantry_elite_a",0),("swadia_infantry_elite_a.1",0),("swadia_infantry_elite_a.2",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 1679 , weight(17)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(17)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_elite_recruit_plated_d", "Infantry Padded Vest", [("swadia_infantry_elite_b",0),("swadia_infantry_elite_b.1",0),("swadia_infantry_elite_b.2",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 1679 , weight(17)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(17)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],

["m_swadia_elite_sergant_armor_a", "Mail Armor", [("sergeant_Jerusalem_armor",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 592 , weight(16)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(18)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],

["m_swadia_elite_sergant_plated_a", "Infantry Plated Mail", [("swadia_army_elite_padded_a",0),("swadia_army_elite_padded_a.1",0),("swadia_army_elite_padded_a.2",0),("swadia_army_elite_padded_a.3",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 4099 , weight(18)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(17)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_elite_sergant_plated_b", "Infantry Plated Mail", [("swadia_army_elite_padded_b",0),("swadia_army_elite_padded_b.1",0),("swadia_army_elite_padded_b.2",0),("swadia_army_elite_padded_b.3",0),("swadia_army_elite_padded_b.4",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 5129 , weight(19)|abundance(100)|head_armor(4)|body_armor(47)|leg_armor(17)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_elite_sergant_plated_c", "Infantry Plated Mail", [("swadia_army_elite_padded_c",0),("swadia_army_elite_padded_c.1",0),("swadia_army_elite_padded_c.2",0),("swadia_army_elite_padded_c.3",0),("swadia_army_elite_padded_c.4",0),("swadia_army_elite_padded_c.5",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 6981 , weight(20)|abundance(100)|head_armor(4)|body_armor(51)|leg_armor(20)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_elite_sergant_plated_d", "Infantry Plated Mail", [("swadia_army_elite_padded_d",0),("swadia_army_elite_padded_d.1",0),("swadia_army_elite_padded_d.2",0),("swadia_army_elite_padded_d.3",0),("swadia_army_elite_padded_d.4",0),("swadia_army_elite_padded_d.5",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 6981 , weight(20)|abundance(100)|head_armor(4)|body_armor(51)|leg_armor(20)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_1] ],

["m_swadia_elite_knight_armor_a", "Mail with Surcoat", [("knight_armor_jerusalem_a",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 1397 , weight(19)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(23)|difficulty(11) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_elite_knight_armor_b", "Mail with Surcoat", [("knight_armor_jerusalem_b",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 1397 , weight(19)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(23)|difficulty(11) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_elite_knight_armor_c", "Mail with Surcoat", [("knight_armor_jerusalem_c",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 1397 , weight(19)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(23)|difficulty(11) ,imodbits_armor, [], [fac_kingdom_1] ],

["m_swadia_elite_knight_armor_a_cloaked", "Mail with Surcoat and Cloak", [("knight_armor_jerusalem_a_cloak",0),("knight_armor_jerusalem_a_cloak.1",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 1497 , weight(21)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(25)|difficulty(11) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_elite_knight_armor_b_cloaked", "Mail with Surcoat and Cloak", [("knight_armor_jerusalem_b_cloak",0),("knight_armor_jerusalem_b_cloak.1",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 1497 , weight(21)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(25)|difficulty(11) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_elite_knight_armor_c_cloaked", "Mail with Surcoat and Cloak", [("knight_armor_jerusalem_c_cloak",0),("knight_armor_jerusalem_c_cloak.1",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 1497 , weight(21)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(25)|difficulty(11) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_elite_knight_armor_d_cloaked", "Mail with Surcoat and Cloak", [("knight_armor_jerusalem_d_cloak",0),("knight_armor_jerusalem_d_cloak.1",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 1497 , weight(21)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(25)|difficulty(11) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_elite_knight_armor_e_cloaked", "Mail with Surcoat and Cloak", [("knight_armor_jerusalem_e_cloak",0),("knight_armor_jerusalem_e_cloak.1",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 1497 , weight(21)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(25)|difficulty(11) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_elite_knight_armor_f_cloaked", "Mail with Surcoat and Cloak", [("knight_armor_jerusalem_f_cloak",0),("knight_armor_jerusalem_f_cloak.1",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 1497 , weight(21)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(25)|difficulty(11) ,imodbits_armor, [], [fac_kingdom_1] ],

# ["m_swadia_lord_armor_a", "Swadian High Knight Armor", [("armor_king_Jerusalem",0),("armor_king_Jerusalem.1",0),("armor_king_Jerusalem.2",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 1871 , weight(21)|abundance(100)|head_armor(0)|body_armor(56)|leg_armor(27)|difficulty(15) ,imodbits_armor ],

["m_swadia_recruit_a", "Swadian Recruit Armor", [("novici_tripoli_armor",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 299 , weight(10)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(7)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],

["m_swadia_recruit_plated_a", "Swadian Plated Recruit Armor", [("swadia_army_a",0),("swadia_army_a.1",0),("swadia_army_a.2",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 1399 , weight(15)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(7)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_recruit_plated_b", "Swadian Plated Recruit Armor", [("swadia_army_b",0),("swadia_army_b.1",0),("swadia_army_b.2",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 1699 , weight(15)|abundance(100)|head_armor(0)|body_armor(33)|leg_armor(16)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_recruit_plated_c", "Swadian Plated Recruit Armor", [("swadia_army_c",0),("swadia_army_c.1",0),("swadia_army_c.2",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 1499 , weight(15)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(16)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],

["m_swadia_armor_light_a", "Swadian Light Armor", [("archer_tripoli_armor_a",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 352 , weight(12)|abundance(100)|head_armor(0)|body_armor(26)|leg_armor(7)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_armor_light_b", "Swadian Light Armor", [("archer_tripoli_armor_b",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 352 , weight(12)|abundance(100)|head_armor(0)|body_armor(26)|leg_armor(7)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],

["m_swadia_infantry_a", "Swadian Infantry Armor", [("armor_infantry_tripoli_a",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 442 , weight(12)|abundance(100)|head_armor(0)|body_armor(32)|leg_armor(11)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_infantry_b", "Swadian Infantry Armor", [("armor_infantry_tripoli_b",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 442 , weight(12)|abundance(100)|head_armor(0)|body_armor(32)|leg_armor(11)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],

["m_swadia_infantry_plated_a", "Plated Swadian Infantry Armor", [("swadia_infantry_a",0),("swadia_infantry_a.1",0),("swadia_infantry_a.2",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 1349 , weight(16)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(11)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_infantry_plated_b", "Plated Swadian Infantry Armor", [("swadia_infantry_b",0),("swadia_infantry_b.1",0),("swadia_infantry_b.2",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 1349 , weight(16)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(11)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_infantry_plated_kneekops_a", "Plated Swadian Infantry Armor with Kneekops", [("swadia_infantry_c",0),("swadia_infantry_c.1",0),("swadia_infantry_c.2",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 1999 , weight(19)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(19)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_infantry_plated_kneekops_b", "Plated Swadian Infantry Armor with Kneekops", [("swadia_infantry_d",0),("swadia_infantry_d.1",0),("swadia_infantry_d.2",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 1999 , weight(19)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(19)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],

["m_swadia_infantry_heavy_a", "Heavy Plated Swadian Armor", [("swadia_heavy_infantry_a",0),("swadia_heavy_infantry_a.1",0),("swadia_heavy_infantry_a.2",0),("swadia_heavy_infantry_a.3",0),("swadia_heavy_infantry_a.4",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 5699 , weight(24)|abundance(100)|head_armor(0)|body_armor(47)|leg_armor(21)|difficulty(10) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_infantry_heavy_b", "Heavy Plated Swadian Armor", [("swadia_heavy_infantry_b",0),("swadia_heavy_infantry_b.1",0),("swadia_heavy_infantry_b.2",0),("swadia_heavy_infantry_b.3",0),("swadia_heavy_infantry_b.4",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 5699 , weight(24)|abundance(100)|head_armor(0)|body_armor(47)|leg_armor(21)|difficulty(10) ,imodbits_armor, [], [fac_kingdom_1] ],

["m_swadia_sergant_armor_a", "Swadian Sergant Armor", [("sergeant_armor_tripoli_a",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 532 , weight(16)|abundance(100)|head_armor(0)|body_armor(38)|leg_armor(15)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_sergant_armor_b", "Swadian Sergant Armor", [("sergeant_armor_tripoli_b",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 532 , weight(16)|abundance(100)|head_armor(0)|body_armor(38)|leg_armor(15)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],

["m_swadia_guardian_armor_a", "Swadian Guard Armor", [("swadia_army_padded_a",0),("swadia_army_padded_a.1",0),("swadia_army_padded_a.2",0),("swadia_army_padded_a.3",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 2679 , weight(23)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(20)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_guardian_armor_b", "Swadian Guard Armor", [("swadia_army_padded_b",0),("swadia_army_padded_b.1",0),("swadia_army_padded_b.2",0),("swadia_army_padded_b.3",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 2679 , weight(23)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(20)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_guardian_armor_c", "Swadian Guard Armor", [("swadia_army_padded_c",0),("swadia_army_padded_c.1",0),("swadia_army_padded_c.2",0),("swadia_army_padded_c.3",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 2679 , weight(23)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(20)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_1] ],

["m_swadia_knight_armor_a", "Swadian Knight Armor", [("knight_armor_tripolli_a",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 1232 , weight(19)|abundance(100)|head_armor(0)|body_armor(47)|leg_armor(21)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_knight_armor_b", "Swadian Knight Armor", [("knight_armor_tripolli_b",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 1232 , weight(19)|abundance(100)|head_armor(0)|body_armor(47)|leg_armor(21)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_knight_armor_c", "Swadian Knight Armor", [("knight_armor_tripolli_c",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 1232 , weight(19)|abundance(100)|head_armor(0)|body_armor(47)|leg_armor(21)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],

["m_swadia_knight_armor_a_cloaked", "Swadian Knight Armor", [("knight_armor_tripolli_a_cloak",0),("knight_armor_tripolli_a_cloak.1",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 1332 , weight(21)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(23)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_knight_armor_b_cloaked", "Swadian Knight Armor", [("knight_armor_tripolli_b_cloak",0),("knight_armor_tripolli_b_cloak.1",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 1332 , weight(21)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(23)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_knight_armor_c_cloaked", "Swadian Knight Armor", [("knight_armor_tripolli_c_cloak",0),("knight_armor_tripolli_c_cloak.1",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 1332 , weight(21)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(23)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],

["m_swadia_knight_plated_a", "Swadian Plated Knight Armor", [("swadia_army_coat_a",0),("swadia_army_coat_a.1",0),("swadia_army_coat_a.2",0),("swadia_army_coat_a.3",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 6715 , weight(25)|abundance(100)|head_armor(0)|body_armor(53)|leg_armor(23)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_knight_plated_b", "Swadian Plated Knight Armor", [("swadia_army_coat_b",0),("swadia_army_coat_b.1",0),("swadia_army_coat_b.2",0),("swadia_army_coat_b.3",0),("swadia_army_coat_b.4",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 6715 , weight(25)|abundance(100)|head_armor(0)|body_armor(53)|leg_armor(23)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],

["m_capelina_a", "Capelina", [("capelina_crusader_a",0)], itp_type_head_armor|itp_merchandise   ,0, 659 , weight(2)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_capelina_b", "Capelina", [("capelina_crusader_b",0)], itp_type_head_armor|itp_merchandise   ,0, 659 , weight(2)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],

["m_crusader_helm_a", "Crusader Helm", [("crusader_hard_helm_a",0)], itp_type_head_armor|itp_merchandise   ,0, 1233 , weight(2.5)|abundance(100)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_crusader_helm_b", "Crusader Helm", [("crusader_hard_helm_b",0)], itp_type_head_armor|itp_merchandise   ,0, 1233 , weight(2.5)|abundance(100)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_crusader_helm_c", "Crusader Helm", [("crusader_hard_helm_c",0)], itp_type_head_armor|itp_merchandise   ,0, 1233 , weight(2.5)|abundance(100)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_crusader_helm_d", "Crusader Helm", [("crusader_hard_helm_d",0)], itp_type_head_armor|itp_merchandise   ,0, 1233 , weight(2.5)|abundance(100)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_crusader_helm_e", "Crusader Helm", [("crusader_hard_helm_f",0)], itp_type_head_armor|itp_merchandise   ,0, 1233 , weight(2.5)|abundance(100)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_crusader_helm_f", "Crusader Helm", [("crusader_hard_helm_ord",0)], itp_type_head_armor|itp_merchandise   ,0, 1233 , weight(2.5)|abundance(100)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_1] ],

["m_cavalry_helmet_a", "Cavalry Helmet", [("crusader_helm_1",0)], itp_type_head_armor|itp_merchandise   ,0, 1021 , weight(2.5)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_cavalry_helmet_b", "Cavalry Helmet", [("crusader_helm_2",0)], itp_type_head_armor|itp_merchandise   ,0, 1021 , weight(2.5)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_cavalry_helmet_c", "Cavalry Helmet", [("crusader_helm_3",0)], itp_type_head_armor|itp_merchandise   ,0, 1021 , weight(2.5)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_cavalry_helmet_d", "Cavalry Helmet", [("crusader_helm_4",0)], itp_type_head_armor|itp_merchandise   ,0, 1021 , weight(2.5)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_cavalry_helmet_e", "Cavalry Helmet", [("crusader_helm_5",0)], itp_type_head_armor|itp_merchandise   ,0, 1021 , weight(2.5)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_1, fac_kingdom_12] ],
["m_cavalry_helmet_f", "Cavalry Helmet", [("crusader_helm_6",0)], itp_type_head_armor|itp_merchandise   ,0, 1021 , weight(2.5)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_1, fac_kingdom_12] ],
["m_cavalry_helmet_g", "Cavalry Helmet", [("crusader_helm_7",0)], itp_type_head_armor|itp_merchandise   ,0, 1021 , weight(2.5)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_1] ],

["m_infantry_helmet_a", "Infantry Helmet", [("crusader_helm_medium_a",0)], itp_type_head_armor|itp_merchandise   ,0, 999 , weight(2.25)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_infantry_helmet_b", "Infantry Helmet", [("crusader_helm_medium_b",0)], itp_type_head_armor|itp_merchandise   ,0, 999 , weight(2.25)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_infantry_helmet_c", "Infantry Helmet", [("crusader_helm_medium_c",0)], itp_type_head_armor|itp_merchandise   ,0, 999 , weight(2.25)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_infantry_helmet_d", "Infantry Helmet", [("crusader_helm_medium_d",0)], itp_type_head_armor|itp_merchandise   ,0, 999 , weight(2.25)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_infantry_helmet_e", "Infantry Helmet", [("crusader_helm_medium_e",0)], itp_type_head_armor|itp_merchandise   ,0, 999 , weight(2.25)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_1] ],

["m_infantry_coif_a", "Infantry Coif", [("crusader_koif_a",0)], itp_type_head_armor|itp_merchandise   ,0, 579 , weight(1.75)|abundance(100)|head_armor(31)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_armor, [], [fac_kingdom_1] ],

["m_knigh_helm_a", "Knight Helmet", [("crusader_knight_helm_a",0)], itp_type_head_armor|itp_merchandise   ,0, 1699 , weight(2.75)|abundance(100)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_knigh_helm_b", "Knight Helmet", [("crusader_knight_helm_b",0)], itp_type_head_armor|itp_merchandise   ,0, 1699 , weight(2.75)|abundance(100)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_knigh_helm_c", "Knight Helmet", [("crusader_knight_helm_c",0)], itp_type_head_armor|itp_merchandise   ,0, 1699 , weight(2.75)|abundance(100)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_knigh_helm_d", "Knight Helmet", [("crusader_knight_helm_d",0)], itp_type_head_armor|itp_merchandise   ,0, 1699 , weight(2.75)|abundance(100)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_knigh_helm_e", "Knight Helmet", [("crusader_knight_helm_e",0)], itp_type_head_armor|itp_merchandise   ,0, 1699 , weight(2.75)|abundance(100)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_knigh_helm_f", "Knight Helmet", [("crusader_knight_helm_f",0)], itp_type_head_armor|itp_merchandise   ,0, 1699 , weight(2.75)|abundance(100)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_armor, [], [fac_kingdom_1] ],

["m_light_capelina_a", "Light Capelina", [("light_capelina_crusader_a",0)], itp_type_head_armor|itp_merchandise   ,0, 519 , weight(1.5)|abundance(100)|head_armor(29)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1, fac_kingdom_12] ],
["m_light_capelina_b", "Light Capelina", [("light_capelina_crusader_b",0)], itp_type_head_armor|itp_merchandise   ,0, 519 , weight(1.5)|abundance(100)|head_armor(29)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1, fac_kingdom_12] ],

["m_light_infantry_helmet_a", "Light Infantry Helmet", [("light_crusader_helm_a",0)], itp_type_head_armor|itp_merchandise   ,0, 872 , weight(2)|abundance(100)|head_armor(34)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_1, fac_kingdom_12] ],
["m_light_infantry_helmet_b", "Light Infantry Helmet", [("light_crusader_helm_b",0)], itp_type_head_armor|itp_merchandise   ,0, 872 , weight(2)|abundance(100)|head_armor(34)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_1, fac_kingdom_12] ],
["m_light_infantry_helmet_c", "Light Infantry Helmet", [("light_crusader_helm_c",0)], itp_type_head_armor|itp_merchandise   ,0, 872 , weight(2)|abundance(100)|head_armor(34)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_1, fac_kingdom_12] ],
["m_light_infantry_helmet_d", "Light Infantry Helmet", [("light_crusader_helm_d",0)], itp_type_head_armor|itp_merchandise   ,0, 872 , weight(2)|abundance(100)|head_armor(34)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_1, fac_kingdom_12] ],
["m_light_infantry_helmet_e", "Light Infantry Helmet", [("light_crusader_helm_e",0)], itp_type_head_armor|itp_merchandise   ,0, 872 , weight(2)|abundance(100)|head_armor(34)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_1, fac_kingdom_12] ],

["m_sergant_helmet_a", "Sergant Helmet", [("marching_helmet_crusader_a",0)], itp_type_head_armor|itp_merchandise   ,0, 1122 , weight(2.25)|abundance(100)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_1, fac_kingdom_12] ],

["m_swadia_elite_helmet_a", "Swadian Elite Helmet", [("fracia_helmet_1",0)], itp_type_head_armor|itp_merchandise   ,0, 1522 , weight(2.5)|abundance(100)|head_armor(49)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_elite_helmet_b", "Swadian Elite Helmet", [("fracia_helmet_2",0)], itp_type_head_armor|itp_merchandise   ,0, 1522 , weight(2.5)|abundance(100)|head_armor(49)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_elite_helmet_c", "Swadian Elite Helmet", [("fracia_knight_helm_a",0)], itp_type_head_armor|itp_merchandise   ,0, 1522 , weight(2.5)|abundance(100)|head_armor(49)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_armor, [], [fac_kingdom_1] ],

["m_swadia_lord_helmet_a", "Swadian High Knight Helmet", [("helm_king_Jerusalem",0)], itp_type_head_armor|itp_merchandise|itp_attach_armature   ,0, 1995 , weight(2.5)|abundance(100)|head_armor(53)|body_armor(0)|leg_armor(0)|difficulty(13) ,imodbits_armor, [], [fac_kingdom_1] ],

["m_swadia_light_boots_a", "Ankle Boots", [("boot_light_crusader_a",0)], itp_type_foot_armor|itp_merchandise   ,0, 100 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(4)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_light_boots_b", "Ankle Boots", [("boot_light_crusader_b",0)], itp_type_foot_armor|itp_merchandise   ,0, 100 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(4)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],

["m_swadia_milita_boots_a", "Milita Boots", [("boot_light_crusader_c",0)], itp_type_foot_armor|itp_merchandise   ,0, 150 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(7)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_4, fac_kingdom_12] ],
["m_swadia_milita_boots_b", "Milita Boots", [("boot_light_crusader_d",0)], itp_type_foot_armor|itp_merchandise   ,0, 150 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(7)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_4, fac_kingdom_12] ],

["m_swadia_infantry_boots_a", "Infantry Boots", [("boot_average_crusader_a",0)], itp_type_foot_armor|itp_merchandise   ,0, 200 , weight(2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_1] ],
["m_swadia_infantry_boots_b", "Infantry Boots", [("boot_average_crusader_b",0)], itp_type_foot_armor|itp_merchandise   ,0, 200 , weight(2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_1] ],

["m_swadia_leather_boots_a", "Leather Boots", [("boot_average_crusader_c",0)], itp_type_foot_armor|itp_merchandise   ,0, 250 , weight(2.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth,[], [fac_kingdom_1, fac_kingdom_4, fac_kingdom_12, fac_kingdom_5] ],
["m_swadia_leather_boots_b", "Leather Boots", [("boot_average_crusader_d",0)], itp_type_foot_armor|itp_merchandise   ,0, 250 , weight(2.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth,[], [fac_kingdom_1, fac_kingdom_4, fac_kingdom_12, fac_kingdom_5] ],

["m_swadia_mail_boots_a", "Swadian Mail Boots", [("shoes_crusader",0)], itp_type_foot_armor|itp_merchandise   ,0, 488 , weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_mail_boots_b", "Swadian Mail Boots", [("shoes_crusader_knight",0)], itp_type_foot_armor|itp_merchandise   ,0, 501 , weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],

# Misc helmets
["m_coif_alternate_a", "Mail Coif", [("coif",0)], itp_merchandise|itp_type_head_armor|itp_covers_beard  ,0, 599 , weight(1.5)|abundance(100)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_5] ],
["m_coif_alternate_b", "Balaclava Coif", [("balaclavacoif",0)], itp_merchandise|itp_type_head_armor|itp_covers_beard  ,0, 599 , weight(1.5)|abundance(100)|head_armor(34)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_5] ],
["m_coif_alternate_c", "Full Face Coif", [("fullfacecoif",0)], itp_merchandise|itp_type_head_armor|itp_covers_beard  ,0, 599 , weight(1.5)|abundance(100)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_5] ],

["m_pepperpot_a", "Pepperpot Helmet", [("frenchpepperpot2",0)], itp_merchandise|itp_type_head_armor  ,0, 799 , weight(2)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_5] ],
["m_pepperpot_b", "Pepperpot Helmet", [("frenchpepperpot3",0)], itp_merchandise|itp_type_head_armor  ,0, 799 , weight(2)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_5] ],
["m_pepperpot_c", "Pepperpot Helmet", [("pepperpothelm1",0)], itp_merchandise|itp_type_head_armor  ,0, 799 , weight(2)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_5] ],
["m_pepperpot_d", "Pepperpot Helmet", [("frenchpepperpot",0)], itp_merchandise|itp_type_head_armor  ,0, 799 , weight(2)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_5] ],

["m_munitions_helm_a", "Munitions Helmet", [("munitionshelm2",0)], itp_merchandise|itp_type_head_armor  ,0, 799 , weight(2)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_5] ],
["m_munitions_helm_b", "Munitions Helmet", [("munitionshelm1",0)], itp_merchandise|itp_type_head_armor  ,0, 799 , weight(2)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_5] ],

["m_conical_helmet_a", "Conical Helmet", [("conichelm",0)], itp_merchandise|itp_type_head_armor  ,0, 701 , weight(2)|abundance(100)|head_armor(39)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_5] ],

["m_flat_top_a", "Flat Top Helmet", [("flattophelmet",0)], itp_merchandise|itp_type_head_armor  ,0, 701 , weight(2)|abundance(100)|head_armor(39)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_5] ],

["m_tower_helm_a", "Tower Helmet", [("byzantion",0)], itp_merchandise|itp_type_head_armor  ,0, 799 , weight(2)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_5] ],
["m_tower_helm_b", "Ornate Tower Helmet", [("col1_byzantion",0)], itp_merchandise|itp_type_head_armor  ,0, 799 , weight(2)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_5] ],

# Narf's Kievian Rus related stuff
["m_vaegir_nikolskoe_helm", "Vaegir Helmet", [("nikolskoe_helm",0), ("inv_nikolskoe_helm",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature  ,0, 820 , weight(2)|abundance(100)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_2] ],
["m_vaegir_novogrod_helm", "Vaegir Helmet", [("novogrod_helm",0), ("inv_novogrod_helm",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0, 740 , weight(2)|abundance(100)|head_armor(47)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_2] ],
["m_vaegir_gnezdovo_helm_a", "Vaegir Helmet", [("gnezdovo_helm_a",0), ("inv_gnezdovo_helm_a",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0, 640 , weight(2)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_2] ],
["m_vaegir_gnezdovo_helm_b", "Vaegir Helmet", [("gnezdovo_helm_b",0), ("inv_gnezdovo_helm_b",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0, 640 , weight(2)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_2] ],
["m_vaegir_tagancha_helm_a", "Vaegir Helmet", [("tagancha_helm_a",0), ("inv_tagancha_helm_a",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0, 580 , weight(2)|abundance(100)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_2] ],
["m_vaegir_tagancha_helm_b", "Vaegir Helmet", [("tagancha_helm_b",0), ("inv_tagancha_helm_b",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0, 820 , weight(2)|abundance(100)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_2] ],
["m_vaegir_rus_helm", "Vaegir Helmet", [("rus_helm",0), ("inv_rus_helm",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0, 230 , weight(2)|abundance(100)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_2] ],
["m_vaegir_litchina_helm", "Vaegir Facemask", [("litchina_helm",0), ("inv_litchina_helm",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0, 820 , weight(2)|abundance(100)|head_armor(54)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_2] ],

["m_vaegir_rus_shoes", "Eastern Shoes", [("rus_shoes",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 75 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_2] ],
["m_vaegir_rus_cav_boots", "Vaegir Cavalry Boots", [("rus_cav_boots",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 459 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(18)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_2] ],
["m_vaegir_rus_splint_greaves", "Vaegir Splinted Greaves", [("rus_splint_greaves",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
 960 , weight(2.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_2] ],

["m_vaegir_padded_a", "Padded Vaegir Armor", [("mailruss",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 395 , weight(16)|abundance(100)|head_armor(0)|body_armor(31)|leg_armor(5)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_2] ],
["m_vaegir_padded_b", "Padded Vaegir Armor with Mail", [("mailrusss",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 605 , weight(16)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(12)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_2] ],

["m_vaegir_mail_a", "Vaegir Mail Armor", [("mailrus",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 795 , weight(16)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(12)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_2] ],
["m_vaegir_mail_long_a", "Long Mail Armor", [("maill",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 815 , weight(21)|abundance(100)|head_armor(0)|body_armor(42)|leg_armor(12)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_2, fac_kingdom_4] ],
["m_mail_long_a", "Long Mail Armor", [("norman_maill",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 815 , weight(21)|abundance(100)|head_armor(0)|body_armor(42)|leg_armor(12)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_2, fac_kingdom_4] ],
["m_mail_long_b", "Long Mail Armor", [("mailnormans",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 815 , weight(21)|abundance(100)|head_armor(0)|body_armor(42)|leg_armor(12)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_2, fac_kingdom_4] ],

["m_vaegir_rus_lamellar_a", "Vaegir Lamellar Armor", [("rus_lamellar_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 1095 , weight(18)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(12)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_2] ],
["m_vaegir_rus_lamellar_b", "Vaegir Lamellar Armor", [("rus_lamellar_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 1095 , weight(18)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(12)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_2] ],
["m_vaegir_kuyak_a", "Kuyak", [("kuyak_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 795 , weight(16)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(12)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_2] ],
["m_vaegir_kuyak_b", "Kuyak", [("kuyak_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 795 , weight(16)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(12)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_2] ],
["m_vaegir_kuyak_c", "Kuyak", [("kuwra",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 795 , weight(16)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(12)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_2] ],
["m_vaegir_kuyak_d", "Kuyak", [("kuwras",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 795 , weight(16)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(12)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_2] ],
["m_vaegir_rus_scale", "Vaegir Scale", [("rus_scale",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 1295 , weight(19)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(18)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_2] ],

["northerner_horse","Northerner Horse", [("northerner_horse",0),("horse_c",imodbits_horse_good)], itp_merchandise|itp_type_horse, 0, 350,abundance(90)|hit_points(100)|body_armor(15)|difficulty(1)|horse_speed(35)|horse_maneuver(44)|horse_charge(16)|horse_scale(104),imodbits_horse_basic, [], [fac_kingdom_2]],
["northerner_horse_black","Northerner Horse Black", [("northerner_horse_black",0),("horse_c",imodbits_horse_good)], itp_merchandise|itp_type_horse, 0, 480,abundance(90)|hit_points(100)|body_armor(15)|difficulty(1)|horse_speed(39)|horse_maneuver(44)|horse_charge(16)|horse_scale(104),imodbits_horse_basic, [], [fac_kingdom_2]],
["northerner_horse_white","Northerner Horse White", [("northerner_horse_white",0)], itp_merchandise|itp_type_horse, 0, 660,abundance(80)|hit_points(120)|body_armor(20)|difficulty(3)|horse_speed(42)|horse_maneuver(51)|horse_charge(18)|horse_scale(98),imodbits_horse_basic, [], [fac_kingdom_2]],
["northerner_horse_hunter","Northerner Horse Hunt", [("northerner_horse_hunter",0)], itp_merchandise|itp_type_horse, 0, 850,abundance(80)|hit_points(120)|body_armor(18)|difficulty(3)|horse_speed(45)|horse_maneuver(51)|horse_charge(18)|horse_scale(98),imodbits_horse_basic, [], [fac_kingdom_2]],

["m_rider_bow_a", "Rider Bow", [("akhergit_bow",0),("akhergit_bow_case", ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 999 , weight(1.25)|difficulty(4)|spd_rtng(100)|shoot_speed(88) | thrust_damage(26 ,pierce),imodbit_cracked | imodbit_bent | imodbit_masterwork, [], [fac_kingdom_3] ],
["m_rider_arrows","Rider Arrows", [("arrow_b",0),("flying_missile",ixmesh_flying_ammo),("copy_arrows_a_kolchan_I", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 1239,weight(5.0)|abundance(10)|weapon_length(95)|thrust_damage(4,pierce)|max_ammo(45),imodbits_missile, [], [fac_kingdom_3]],


["m_impaler_a", "Impaler", [("mgqq",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry,itc_staff|itcf_carry_spear,429 , weight(2.25)|difficulty(0)|spd_rtng(90) | weapon_length(192)|swing_damage(23 , cut) | thrust_damage(29 ,  pierce),imodbits_polearm, [], [fac_kingdom_3] ],
["m_impaler_b", "Elite Impaler", [("mgqqj",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry,itc_staff|itcf_carry_spear, 899 , weight(2.25)|difficulty(0)|spd_rtng(100) | weapon_length(192)|swing_damage(25 , cut) | thrust_damage(31 ,  pierce),imodbits_polearm, [], [fac_kingdom_3] ],
 
["m_rider_sword_a", "Rider Sword", [("tihewandao1",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_katana, 399, weight(1.25)|difficulty(0)|spd_rtng(100) | weapon_length(90)|swing_damage(34 , cut),imodbits_sword_high, [], [fac_kingdom_3] ],
["m_rider_sword_b", "Elite Rider Sword", [("tihewandao",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_katana, 899, weight(1.25)|difficulty(0)|spd_rtng(111) | weapon_length(90)|swing_damage(36 , cut),imodbits_sword_high, [], [fac_kingdom_3] ],

["m_dao_a", "Dao", [("HX_HSDJ344c",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_katana, 499, weight(1.25)|difficulty(0)|spd_rtng(95) | weapon_length(90)|swing_damage(36 , cut),imodbits_sword_high, [], [fac_kingdom_3] ],
["m_dao_b", "Dao", [("HX_HSDJ344c1",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_katana, 499, weight(1.25)|difficulty(0)|spd_rtng(95) | weapon_length(90)|swing_damage(36 , cut),imodbits_sword_high, [], [fac_kingdom_3] ],

["m_buckler_a", "Steel Buckler", [("steel_buckler1",0)], itp_merchandise|itp_type_shield, itcf_carry_buckler_left,  699 , weight(2)|hit_points(700)|body_armor(12)|spd_rtng(125)|shield_width(30),imodbits_shield ],
["m_buckler_b", "Steel Buckler", [("steel_buckler2",0)], itp_merchandise|itp_type_shield, itcf_carry_buckler_left,  699 , weight(2)|hit_points(700)|body_armor(12)|spd_rtng(125)|shield_width(30),imodbits_shield ],

["m_lamellar_leather_a", "Leather Lamellar Armor", [("kstjbdbs",0)], itp_merchandise|itp_type_body_armor, 0, 429,abundance(100)|head_armor(0)|body_armor(25)|leg_armor(10)|difficulty(0),imodbits_cloth, [], [fac_kingdom_4]],
["m_lamellar_leather_b", "Leather Lamellar Armor", [("kstjbdbss",0)], itp_merchandise|itp_type_body_armor, 0, 479,abundance(100)|head_armor(0)|body_armor(30)|leg_armor(10)|difficulty(0),imodbits_cloth, [], [fac_kingdom_4]],

["m_lamellar_armor_west_a", "Lamellar Armor on Vest", [("cloth_b_alt3bdaybcdbvbzt",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 579,abundance(100)|head_armor(0)|body_armor(36)|leg_armor(11)|difficulty(0),imodbits_armor, [], [fac_kingdom_3]],
["m_lamellar_armor_west_b", "Battle Lamellar Armor on Vest", [("cloth_b_alt3bdaybcdbvbzta",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 699,abundance(100)|head_armor(0)|body_armor(39)|leg_armor(11)|difficulty(0),imodbits_armor, [], [fac_kingdom_3]],

["m_lamellar_armor_a", "Lamellar Armor", [("cloth_b_alt3bdaybcdbvbztt",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 579,abundance(100)|head_armor(0)|body_armor(36)|leg_armor(16)|difficulty(0),imodbits_armor, [], [fac_kingdom_3]],
["m_lamellar_armor_b", "Battle Lamellar Armor", [("cloth_b_alt3bdaybcdbvbztt_combined",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 699,abundance(100)|head_armor(0)|body_armor(39)|leg_armor(16)|difficulty(0),imodbits_armor, [], [fac_kingdom_3]],

["m_lamellar_champion_a", "Champion Lamellar Armor", [("cloth_b_alt3ab",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 779,abundance(100)|head_armor(0)|body_armor(43)|leg_armor(22)|difficulty(0),imodbits_armor, [], [fac_kingdom_3]],

["m_lancer_armor_a", "Lancer Armor", [("mughal_xlamellarvax",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 1089,abundance(100)|head_armor(0)|body_armor(43)|leg_armor(22)|difficulty(7),imodbits_armor, [], [fac_kingdom_3]],
["m_lancer_armor_b", "Lancer Armor", [("mughal_xlamellarvaxh",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 1089,abundance(100)|head_armor(0)|body_armor(43)|leg_armor(22)|difficulty(7),imodbits_armor, [], [fac_kingdom_3]],
["m_lancer_armor_c", "Lancer Armor", [("mughal_xlamellarvaxhv",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 1089,abundance(100)|head_armor(0)|body_armor(43)|leg_armor(22)|difficulty(7),imodbits_armor, [], [fac_kingdom_3]],
["m_lancer_armor_d", "Lancer Armor", [("mughal_xlamellarvax",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 1089,abundance(100)|head_armor(0)|body_armor(43)|leg_armor(22)|difficulty(7),imodbits_armor, [], [fac_kingdom_3]],
["m_lancer_armor_e", "Lancer Armor", [("mughal_xlamellarvacdf",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 1089,abundance(100)|head_armor(0)|body_armor(43)|leg_armor(22)|difficulty(7),imodbits_armor, [], [fac_kingdom_3]],
["m_lancer_armor_f", "Lancer Armor", [("mughal_xlamellarvacd",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 1089,abundance(100)|head_armor(0)|body_armor(43)|leg_armor(22)|difficulty(7),imodbits_armor, [], [fac_kingdom_3]],
["m_lancer_armor_g", "Lancer Armor", [("mughal_xlamellarvac",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 1089,abundance(100)|head_armor(0)|body_armor(43)|leg_armor(22)|difficulty(7),imodbits_armor, [], [fac_kingdom_3]],

["m_lancer_armor_a_long", "Long Lancer Armor", [("mughal_xlamellarvaxc",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 1289,abundance(100)|head_armor(0)|body_armor(43)|leg_armor(29)|difficulty(7),imodbits_armor, [], [fac_kingdom_3]],
["m_lancer_armor_b_long", "Long Lancer Armor", [("mughal_xlamellarvacdfv",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 1289,abundance(100)|head_armor(0)|body_armor(43)|leg_armor(29)|difficulty(7),imodbits_armor, [], [fac_kingdom_3]],

["m_lancer_armor_elite_a", "Elite Lancer Armor", [("mughal_lamellarvax",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 1189,abundance(100)|head_armor(0)|body_armor(48)|leg_armor(26)|difficulty(9),imodbits_armor, [], [fac_kingdom_3]],
["m_lancer_armor_elite_b", "Elite Lancer Armor", [("mughal_lamellarvacdf",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 1189,abundance(100)|head_armor(0)|body_armor(48)|leg_armor(26)|difficulty(9),imodbits_armor, [], [fac_kingdom_3]],
["m_lancer_armor_elite_c", "Elite Lancer Armor", [("mughal_lamellarvacd",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 1189,abundance(100)|head_armor(0)|body_armor(48)|leg_armor(26)|difficulty(9),imodbits_armor, [], [fac_kingdom_3]],
["m_lancer_armor_elite_d", "Elite Lancer Armor", [("mughal_lamellarvac",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 1189,abundance(100)|head_armor(0)|body_armor(48)|leg_armor(26)|difficulty(9),imodbits_armor, [], [fac_kingdom_3]],
["m_lancer_armor_elite_e", "Elite Lancer Armor", [("mughal_lamellarvax",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 1189,abundance(100)|head_armor(0)|body_armor(48)|leg_armor(26)|difficulty(9),imodbits_armor, [], [fac_kingdom_3]],
["m_lancer_armor_elite_f", "Elite Lancer Armor", [("mughal_lamellarvaxh",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 1189,abundance(100)|head_armor(0)|body_armor(48)|leg_armor(26)|difficulty(9),imodbits_armor, [], [fac_kingdom_3]],
["m_lancer_armor_elite_g", "Elite Lancer Armor", [("mughal_lamellarvaxhv",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 1189,abundance(100)|head_armor(0)|body_armor(48)|leg_armor(26)|difficulty(9),imodbits_armor, [], [fac_kingdom_3]],

["m_lancer_armor_elite_a_long", "Elite Long Lancer Armor", [("mughal_lamellarvacdfv",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 1389,abundance(100)|head_armor(0)|body_armor(48)|leg_armor(32)|difficulty(9),imodbits_armor, [], [fac_kingdom_3]],
["m_lancer_armor_elite_b_long", "Elite Long Lancer Armor", [("mughal_lamellarvaxc",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 1389,abundance(100)|head_armor(0)|body_armor(48)|leg_armor(32)|difficulty(9),imodbits_armor, [], [fac_kingdom_3]],

["m_lancer_heavy_elite_a", "Heavy Elite Lancer Armor", [("mughal_lamellarvacdff",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 1589,abundance(100)|head_armor(0)|body_armor(52)|leg_armor(28)|difficulty(11),imodbits_armor, [], [fac_kingdom_3]],

["m_lancer_helmet_light_a", "Light Lancer Helmet", [("mughal_xlamellarvaxttc",0)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0, 459 , weight(1.5)|abundance(100)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_3] ],
["m_lancer_helmet_light_b", "Light Lancer Helmet", [("mughal_xlamellarvaxtt",0)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0, 459 , weight(1.5)|abundance(100)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_3] ],

["m_lancer_helmet_midi_a", "Medium Lancer Helmet", [("copy_mughal_lamellar_wx_agawt",0)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0, 589 , weight(2.0)|abundance(100)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_3] ],
["m_lancer_helmet_midi_b", "Medium Lancer Helmet", [("mughal_lamellarvatky",0)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0, 589 , weight(2.0)|abundance(100)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_3] ],
["m_lancer_helmet_midi_c", "Medium Lancer Helmet", [("mughal_xlamellarvatky",0)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0, 589 , weight(2.0)|abundance(100)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_3] ],
["m_lancer_helmet_midi_d", "Medium Lancer Helmet", [("mughal_lamellar_wx_agawb_h",0)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0, 589 , weight(2.0)|abundance(100)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_3] ],
["m_lancer_helmet_midi_e", "Medium Lancer Helmet", [("mughal_lamellar_wx_agaw_h",0)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0, 589 , weight(2.0)|abundance(100)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_3] ],
["m_lancer_helmet_midi_f", "Medium Lancer Helmet", [("mughal_lamellar_wx_avc_h",0)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0, 589 , weight(2.0)|abundance(100)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_3] ],

["m_lancer_helmet_heavy_a", "Heavy Lancer Helmet", [("donyasbkab",0)], itp_merchandise| itp_type_head_armor | itp_attach_armature|itp_covers_beard,0, 689 , weight(2.5)|abundance(100)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_3] ],

# Highlander Pack
 ["a_h1",  "Highlander Costume", [("a_h1",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0, 259 , weight(3)|abundance(5)|head_armor(0)|body_armor(20)|leg_armor(8)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_4] ],
 ["a_h1_1",  "Highlander Costume", [("a_h1_1",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0, 259 , weight(3)|abundance(5)|head_armor(0)|body_armor(20)|leg_armor(8)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_4] ],
 ["a_h2",  "Highlander Armor", [("a_h2",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0, 1000 , weight(15)|abundance(5)|head_armor(0)|body_armor(34)|leg_armor(14)|difficulty(7) ,imodbits_armor, [], [fac_kingdom_4] ],
 ["a_h2_1",  "Highlander Armor", [("a_h2_1",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0, 1000 , weight(15)|abundance(5)|head_armor(0)|body_armor(34)|leg_armor(14)|difficulty(7) ,imodbits_armor, [], [fac_kingdom_4] ],
 ["a_h3",  "Elite Highlander Armor", [("a_h3",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0, 3000 , weight(3)|abundance(5)|head_armor(0)|body_armor(46)|leg_armor(18)|difficulty(7) ,imodbits_armor, [], [fac_kingdom_4] ],
 ["a_h3_1",  "Elite Highlander Armor", [("a_h3_1",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0, 3000 , weight(3)|abundance(5)|head_armor(0)|body_armor(46)|leg_armor(18)|difficulty(7) ,imodbits_armor, [], [fac_kingdom_4] ],
 ["a_h4",  "Highlander Costume", [("a_h4",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0, 300 , weight(3)|abundance(5)|head_armor(0)|body_armor(24)|leg_armor(10)|difficulty(7) ,imodbits_armor, [], [fac_kingdom_4] ],
 ["a_h4_1",  "Highlander Costume", [("a_h4_1",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0, 300 , weight(3)|abundance(5)|head_armor(0)|body_armor(24)|leg_armor(10)|difficulty(7) ,imodbits_armor, [], [fac_kingdom_4] ],

["h_h1", "Highlander Beret", [("h_h1",0)], itp_type_head_armor| itp_attach_armature|itp_fit_to_head   ,0, 278 , weight(2)|abundance(5)|head_armor(20)|body_armor(0)|leg_armor(0) ,imodbits_cloth, [], [fac_kingdom_4] ],
["h_h1_1", "Highlander Beret", [("h_h1_1",0)], itp_type_head_armor | itp_attach_armature|itp_fit_to_head   ,0, 278 , weight(2)|abundance(5)|head_armor(20)|body_armor(0)|leg_armor(0) ,imodbits_cloth, [], [fac_kingdom_4] ],
["h_h2", "Highlander Beret", [("h_h2",0)], itp_type_head_armor | itp_attach_armature|itp_fit_to_head   ,0, 350 , weight(2)|abundance(5)|head_armor(25)|body_armor(0)|leg_armor(0) ,imodbits_cloth, [], [fac_kingdom_4] ],
["h_h2_1", "Highlander Beret", [("h_h2_1",0)], itp_type_head_armor | itp_attach_armature|itp_fit_to_head   ,0, 350 , weight(2)|abundance(5)|head_armor(25)|body_armor(0)|leg_armor(0) ,imodbits_cloth, [], [fac_kingdom_4] ],
 
["b_h1", "Highlander Boots", [("b_h1",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 1500 , weight(2.5)|abundance(5)|head_armor(0)|body_armor(0)|leg_armor(23)|difficulty(7) ,imodbits_armor, [], [fac_kingdom_4] ],
["b_h1_1", "Highlander Boots", [("b_h1_1",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 1500 , weight(2.5)|abundance(5)|head_armor(0)|body_armor(0)|leg_armor(23)|difficulty(7) ,imodbits_armor, [], [fac_kingdom_4] ],
["b_h2", "Highlander Boots", [("b_h2",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 1770 , weight(2.5)|abundance(5)|head_armor(0)|body_armor(0)|leg_armor(28)|difficulty(7) ,imodbits_armor, [], [fac_kingdom_4] ],
["b_h2_1", "Highlander Boots", [("b_h2_1",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 1770 , weight(2.5)|abundance(5)|head_armor(0)|body_armor(0)|leg_armor(28)|difficulty(7) ,imodbits_armor, [], [fac_kingdom_4] ],

["s_h1", "Improved Highlander Shield", [("s_h1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield ,  2000 , weight(3.5)|hit_points(350)|body_armor(2)|spd_rtng(100)|shield_width(60),imodbits_shield, [], [fac_kingdom_4] ],
["s_h1_1", "Improved Highlander Shield", [("s_h1_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield ,  2500 , weight(3.5)|hit_points(360)|body_armor(2)|spd_rtng(100)|shield_width(60),imodbits_shield, [], [fac_kingdom_4] ],
["s_h1_2", "Improved Highlander Shield", [("s_h1_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield ,  3000 , weight(3.5)|hit_points(370)|body_armor(2)|spd_rtng(100)|shield_width(60),imodbits_shield, [], [fac_kingdom_4] ],
["s_h2", "Highlander Shield", [("s_h2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield ,  1000 , weight(3.5)|hit_points(300)|body_armor(2)|spd_rtng(100)|shield_width(60),imodbits_shield, [], [fac_kingdom_4] ],
["s_h2_1", "Highlander Shield", [("s_h2_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield ,  1500 , weight(3.5)|hit_points(315)|body_armor(2)|spd_rtng(100)|shield_width(60),imodbits_shield, [], [fac_kingdom_4] ],
["s_h2_2", "Highlander Shield", [("s_h2_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield ,  1800 , weight(3.5)|hit_points(330)|body_armor(2)|spd_rtng(100)|shield_width(60),imodbits_shield, [], [fac_kingdom_4] ],

["dirk", "Dirk",[("dirk",0),("dirk_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_dagger|itcf_carry_dagger_front_right|itcf_show_holster_when_drawn, 183 , weight(1.25)|difficulty(0)|spd_rtng(103) | weapon_length(75)|swing_damage(25 , cut) | thrust_damage(19 ,  pierce),imodbits_sword, [], [fac_kingdom_4] ],

["2h_claymore", "Claymore", [("2h_claymore",0)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_back, 294 , weight(2.0)|difficulty(9)|spd_rtng(98) | weapon_length(101)|swing_damage(35 , cut) | thrust_damage(26 ,  pierce),imodbits_sword_high, [], [fac_kingdom_4] ],

["highlad_broadsword", "Highlad Broadsword", [("highlad_broadsword",0),("highlad_broadsword_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 163 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(27 , cut) | thrust_damage(22 ,  pierce),imodbits_sword_high, [], [fac_kingdom_4] ],
# Higlander Pack end

["sar_helmet5", "Sar Helmet 5", [("sar_helmet5",0)], itp_type_head_armor   ,0, 578 , weight(3)|abundance(0)|head_armor(20)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],

["woolen_cap_new_b", "Woolen Cap", [("woolen_cap_new_b",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 2 , weight(1)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["woolen_cap_new_c", "Woolen Cap", [("woolen_cap_new_c",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 2 , weight(1)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["woolen_cap_new_d", "Woolen Cap", [("woolen_cap_new_d",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 2 , weight(1)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["woolen_cap_new_e", "Woolen Cap", [("woolen_cap_new_e",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 2 , weight(1)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["woolen_cap_new_f", "Woolen Cap", [("woolen_cap_new_f",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 2 , weight(1)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["cervelliere", "Cervelliere", [("cervelliere",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 4 , weight(0.6)|abundance(0)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

# ["chionite_hat", "Chionite Hat", [("chionite_hat",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 4 , weight(0.5)|abundance(0)|head_armor(9)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

# ["chionite_hat_b", "Chionite b", [("chionite_hat_b",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 4 , weight(0.5)|abundance(0)|head_armor(9)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
# ["chionite_hat_c", "Chionite c", [("chionite_hat_c",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 4 , weight(0.5)|abundance(0)|head_armor(9)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
# ["chionite_hat_d", "Chionite d", [("chionite_hat_d",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 4 , weight(0.5)|abundance(0)|head_armor(9)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
# ["chionite_hat_e", "Chionite e", [("chionite_hat_e",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 4 , weight(0.5)|abundance(0)|head_armor(9)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
# ["chionite_hat_f", "Chionite f", [("chionite_hat_f",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 4 , weight(0.5)|abundance(0)|head_armor(9)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

# Combined armors
# shirt_a_new
["shirt_a_new", "Shirt", [("shirt_a_new",0)], itp_type_body_armor, 0, 39,abundance(100)|head_armor(0)|body_armor(6)|leg_armor(4)|difficulty(0),imodbits_cloth],
# shirt_a_vest, shirt_a_vest.1
["shirt_a_vest", "Shirt with Vest", [("shirt_a_vest",0),("shirt_a_vest.1",0)], itp_type_body_armor, 0, 49,abundance(100)|head_armor(0)|body_armor(8)|leg_armor(4)|difficulty(0),imodbits_cloth],
# shirt_a_cloak, shirt_a_cloak.1
["shirt_a_cloak", "Shirt with Cloak", [("shirt_a_cloak",0),("shirt_a_cloak.1",0)], itp_type_body_armor, 0, 43,abundance(100)|head_armor(0)|body_armor(8)|leg_armor(4)|difficulty(0),imodbits_cloth],
# shirt_a_tattered_vest, shirt_a_tattered_vest.1
["shirt_a_tattered_vest", "Tattered Shirt with Vest", [("shirt_a_tattered_vest",0),("shirt_a_tattered_vest.1",0)], itp_type_body_armor, 0, 189,abundance(100)|head_armor(0)|body_armor(15)|leg_armor(4)|difficulty(0),imodbits_cloth],
# shirt_a_leather_jerkin, shirt_a_leather_jerkin.1
["shirt_a_leather_jerkin", "Leather Jerkin", [("shirt_a_leather_jerkin",0),("shirt_a_leather_jerkin.1",0)], itp_type_body_armor, 0, 275,abundance(100)|head_armor(0)|body_armor(25)|leg_armor(13)|difficulty(0),imodbits_cloth],
# shirt_a_padded_new, shirt_a_padded_new.1
["shirt_a_padded_new", "Padded Shirt", [("shirt_a_padded_new",0),("shirt_a_padded_new.1",0)], itp_type_body_armor, 0, 201,abundance(100)|head_armor(0)|body_armor(26)|leg_armor(14)|difficulty(0),imodbits_cloth],
# shirt_a_byrnie, shirt_a_byrnie.1, shirt_a_byrnie.2
["shirt_a_byrnie", "Byrnie", [("shirt_a_byrnie",0),("shirt_a_byrnie.1",0),("shirt_a_byrnie.2",0)], itp_type_body_armor, 0, 399,abundance(100)|head_armor(0)|body_armor(37)|leg_armor(13)|difficulty(0),imodbits_armor],
# shirt_a_lamellar_new, shirt_a_lamellar_new.1
["shirt_a_lamellar_new", "Lamellar Shirt", [("shirt_a_lamellar_new",0),("shirt_a_lamellar_new.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(0)|body_armor(16)|leg_armor(0)|difficulty(0),imodbits_cloth],
# shirt_a_coat_of_plates_light, shirt_a_coat_of_plates_light.1
["shirt_a_coat_of_plates_light", "Light Coat of Plates", [("shirt_a_coat_of_plates_light",0),("shirt_a_coat_of_plates_light.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(0)|body_armor(18)|leg_armor(0)|difficulty(0),imodbits_armor],
# shirt_a_mail_new, shirt_a_mail_new.1
["shirt_a_mail_new", "Mail Shirt", [("shirt_a_mail_new",0),("shirt_a_mail_new.1",0)], itp_type_body_armor, 0, 456,abundance(100)|head_armor(0)|body_armor(29)|leg_armor(17)|difficulty(0),imodbits_armor],
# shirt_a_lamellar_mail, shirt_a_lamellar_mail.1, shirt_a_lamellar_mail.2
["shirt_a_lamellar_mail", "Lamellar Mail Shirt", [("shirt_a_lamellar_mail",0),("shirt_a_lamellar_mail.1",0),("shirt_a_lamellar_mail.2",0)], itp_type_body_armor, 0, 781,abundance(100)|head_armor(0)|body_armor(35)|leg_armor(17)|difficulty(0),imodbits_armor],
# shirt_a_coat_of_plates_new, shirt_a_coat_of_plates_new.1
["shirt_a_coat_of_plates_new", "Coat of Plates", [("shirt_a_coat_of_plates_new",0),("shirt_a_coat_of_plates_new.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(1)|body_armor(24)|leg_armor(0)|difficulty(0),imodbits_armor],
# rich_tunic_a_new
["rich_tunic_a_new", "Rich Tunic", [("rich_tunic_a_new",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(0)|body_armor(8)|leg_armor(4)|difficulty(0),imodbits_cloth],
# rich_tunic_a_shirt, rich_tunic_a_shirt.1
["rich_tunic_a_shirt", "Rich Tunic with Shirt", [("rich_tunic_a_shirt",0),("rich_tunic_a_shirt.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(0)|body_armor(8)|leg_armor(4)|difficulty(0),imodbits_cloth],
# rich_tunic_a_cloak, rich_tunic_a_cloak.1
["rich_tunic_a_cloak", "Rich Tunic with Cloak", [("rich_tunic_a_cloak",0),("rich_tunic_a_cloak.1",0)], itp_type_body_armor, 0, 109,abundance(100)|head_armor(0)|body_armor(9)|leg_armor(4)|difficulty(0),imodbits_cloth],
# rich_tunic_a_vest, rich_tunic_a_vest.1, rich_tunic_a_vest.2
["rich_tunic_a_vest", "Rich Tunic with Vest", [("rich_tunic_a_vest",0),("rich_tunic_a_vest.1",0),("rich_tunic_a_vest.2",0)], itp_type_body_armor, 0, 199,abundance(100)|head_armor(0)|body_armor(18)|leg_armor(4)|difficulty(0),imodbits_cloth],
# rich_tunic_a_padded, rich_tunic_a_padded.1, rich_tunic_a_padded.2
["rich_tunic_a_padded", "Rich Tunic with Padded Cloth", [("rich_tunic_a_padded",0),("rich_tunic_a_padded.1",0),("rich_tunic_a_padded.2",0)], itp_type_body_armor, 0, 209,abundance(100)|head_armor(0)|body_armor(19)|leg_armor(4)|difficulty(0),imodbits_cloth],
# rich_tunic_a_lamellar_leather, rich_tunic_a_lamellar_leather.1
["rich_tunic_a_lamellar_leather", "Rich Tunic with Lamellar Leather", [("rich_tunic_a_lamellar_leather",0),("rich_tunic_a_lamellar_leather.1",0)], itp_type_body_armor, 0, 189,abundance(100)|head_armor(0)|body_armor(17)|leg_armor(4)|difficulty(0),imodbits_cloth],
# rich_tunic_a_haubergeon, rich_tunic_a_haubergeon.1
["rich_tunic_a_haubergeon", "Rich Tunic with Haubergeon", [("rich_tunic_a_haubergeon",0),("rich_tunic_a_haubergeon.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(1)|body_armor(12)|leg_armor(0)|difficulty(0),imodbits_cloth],
# rich_tunic_a_lamellar, rich_tunic_a_lamellar.1
["rich_tunic_a_lamellar", "Rich Tunic with Lamellar", [("rich_tunic_a_lamellar",0),("rich_tunic_a_lamellar.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(1)|body_armor(12)|leg_armor(0)|difficulty(0),imodbits_cloth],
# rich_tunic_a_lamellar_variant, rich_tunic_a_lamellar_variant.1
["rich_tunic_a_lamellar_variant", "Rich Tunic with Lamellar Variant", [("rich_tunic_a_lamellar_variant",0),("rich_tunic_a_lamellar_variant.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(1)|body_armor(12)|leg_armor(0)|difficulty(0),imodbits_cloth],
# rich_tunic_a_byrnie, rich_tunic_a_byrnie.1, rich_tunic_a_byrnie.2
["rich_tunic_a_byrnie", "Rich Tunic with Byrnie", [("rich_tunic_a_byrnie",0),("rich_tunic_a_byrnie.1",0),("rich_tunic_a_byrnie.2",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(1)|body_armor(12)|leg_armor(0)|difficulty(0),imodbits_cloth],
# rich_tunic_a_lamellar_armour, rich_tunic_a_lamellar_armour.1
["rich_tunic_a_lamellar_armour", "Rich Tunic with Lamellar Armour", [("rich_tunic_a_lamellar_armour",0),("rich_tunic_a_lamellar_armour.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(2)|body_armor(15)|leg_armor(0)|difficulty(0),imodbits_cloth],
# rich_tunic_a_lamellar_armour_variant, rich_tunic_a_lamellar_armour_variant.1
["rich_tunic_a_lamellar_armour_variant", "Rich Tunic with Lamellar Armour Variant", [("rich_tunic_a_lamellar_armour_variant",0),("rich_tunic_a_lamellar_armour_variant.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(2)|body_armor(15)|leg_armor(0)|difficulty(0),imodbits_cloth],
# rich_tunic_a_scale, rich_tunic_a_scale.1
["rich_tunic_a_scale", "Rich Tunic with Scale", [("rich_tunic_a_scale",0),("rich_tunic_a_scale.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(2)|body_armor(15)|leg_armor(0)|difficulty(0),imodbits_cloth],
# rich_tunic_a_mail, rich_tunic_a_mail.1
["rich_tunic_a_mail", "Rich Tunic with Mail", [("rich_tunic_a_mail",0),("rich_tunic_a_mail.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(2)|body_armor(15)|leg_armor(0)|difficulty(0),imodbits_cloth],
# nomad_vest_new_a
["nomad_vest_new_a", "Nomad Vest", [("nomad_vest_new_a",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(0)|body_armor(15)|leg_armor(8)|difficulty(0),imodbits_cloth],
# nomad_vest_padded, nomad_vest_padded.1, nomad_vest_padded.2
["nomad_vest_padded", "Nomad Vest with Padded", [("nomad_vest_padded",0),("nomad_vest_padded.1",0),("nomad_vest_padded.2",0)], itp_type_body_armor, 0, 299,abundance(100)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0),imodbits_cloth],
# nomad_vest_mail, nomad_vest_mail.1
["nomad_vest_mail", "Nomad Vest with Mail", [("nomad_vest_mail",0),("nomad_vest_mail.1",0)], itp_type_body_armor, 0, 499,abundance(100)|head_armor(0)|body_armor(35)|leg_armor(16)|difficulty(0),imodbits_armor],
# nomad_vest_lamellar, nomad_vest_lamellar.1, nomad_vest_lamellar.2
["nomad_vest_lamellar", "Nomad Vest with Lamellar", [("nomad_vest_lamellar",0),("nomad_vest_lamellar.1",0),("nomad_vest_lamellar.2",0)], itp_type_body_armor, 0, 899,abundance(100)|head_armor(0)|body_armor(42)|leg_armor(24)|difficulty(0),imodbits_armor],
# arabian_robe_a, arabian_robe_a_padded, arabian_robe_a_padded.1
["arabian_robe_a", "Arabian Robe", [("arabian_robe_a",0),("arabian_robe_a_padded",0),("arabian_robe_a_padded.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(1)|body_armor(12)|leg_armor(0)|difficulty(0),imodbits_cloth],
# arabian_robe_a_byrnie, arabian_robe_a_byrnie.1, arabian_robe_a_byrnie.2 
["arabian_robe_a_byrnie", "Arabian Robe with Byrnie", [("arabian_robe_a_byrnie",0),("arabian_robe_a_byrnie.1",0),("arabian_robe_a_byrnie.2",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(1)|body_armor(12)|leg_armor(0)|difficulty(0),imodbits_cloth],
# arabian_robe_a_mail, arabian_robe_a_mail.1
["arabian_robe_a_mail", "Arabian Robe with Mail", [("arabian_robe_a_mail",0),("arabian_robe_a_mail.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(1)|body_armor(12)|leg_armor(0)|difficulty(0),imodbits_cloth],
# arabian_shirt_new, arabian_shirt_new.1
["arabian_shirt_new", "Arabian Shirt", [("arabian_shirt_new",0),("arabian_shirt_new.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(1)|body_armor(12)|leg_armor(0)|difficulty(0),imodbits_cloth],
# arabian_shirt_padded, arabian_shirt_padded.1, arabian_shirt_padded.2
["arabian_shirt_padded", "Arabian Shirt with Padded", [("arabian_shirt_padded",0),("arabian_shirt_padded.1",0),("arabian_shirt_padded.2",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(1)|body_armor(12)|leg_armor(0)|difficulty(0),imodbits_cloth],
# arabian_shirt_cuirass, arabian_shirt_cuirass.1
["arabian_shirt_cuirass", "Arabian Shirt with Cuirass", [("arabian_shirt_cuirass",0),("arabian_shirt_cuirass.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(1)|body_armor(12)|leg_armor(0)|difficulty(0),imodbits_cloth],
# arabian_shirt_lamellar_armor
["arabian_shirt_lamellar_armor", "Arabian Shirt with Lamellar", [("arabian_shirt_lamellar_armor",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(1)|body_armor(12)|leg_armor(0)|difficulty(0),imodbits_cloth],
# arabian_shirt_b_new, arabian_shirt_b_new.1
["arabian_shirt_b_new", "Arabian Shirt", [("arabian_shirt_b_new",0),("arabian_shirt_b_new.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(2)|body_armor(15)|leg_armor(0)|difficulty(0),imodbits_cloth],
# arabian_shirt_b_padded, arabian_shirt_b_padded.1, arabian_shirt_b_padded.2
["arabian_shirt_b_padded", "Arabian Shirt with Padded", [("arabian_shirt_b_padded",0),("arabian_shirt_b_padded.1",0),("arabian_shirt_b_padded.2",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(2)|body_armor(15)|leg_armor(0)|difficulty(0),imodbits_cloth],
# arabian_shirt_b_cuirass, arabian_shirt_b_cuirass.1, arabian_shirt_b_cuirass.2
["arabian_shirt_b_cuirass", "Arabian Shirt with Cuirass", [("arabian_shirt_b_cuirass",0),("arabian_shirt_b_cuirass.1",0),("arabian_shirt_b_cuirass.2",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(2)|body_armor(15)|leg_armor(0)|difficulty(0),imodbits_cloth],
# arabian_shirt_b_lamellar_armor, arabian_shirt_b_lamellar_armor.1
["arabian_shirt_b_lamellar_armor", "Arabian Shirt with Lamellar", [("arabian_shirt_b_lamellar_armor",0),("arabian_shirt_b_lamellar_armor.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(2)|body_armor(15)|leg_armor(0)|difficulty(0),imodbits_cloth],
# sar_robe_new
["sar_robe_new", "Saracen Robe", [("sar_robe_new",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(1)|body_armor(12)|leg_armor(0)|difficulty(0),imodbits_cloth],
# sar_robe_vest, sar_robe_vest.1
["sar_robe_vest", "Saracen Robe with Vest", [("sar_robe_vest",0),("sar_robe_vest.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(1)|body_armor(12)|leg_armor(0)|difficulty(0),imodbits_cloth],
# sar_robe_nomad, sar_robe_nomad.1
["sar_robe_nomad", "Saracen Robe with Nomad", [("sar_robe_nomad",0),("sar_robe_nomad.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(1)|body_armor(12)|leg_armor(0)|difficulty(0),imodbits_cloth],
# sar_robe_aketon, sar_robe_aketon.1
["sar_robe_aketon", "Saracen Robe with Aketon", [("sar_robe_aketon",0),("sar_robe_aketon.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(1)|body_armor(12)|leg_armor(0)|difficulty(0),imodbits_cloth],
# sar_robe_padded, sar_robe_padded.1
["sar_robe_padded", "Saracen Robe with Padded", [("sar_robe_padded",0),("sar_robe_padded.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(1)|body_armor(12)|leg_armor(0)|difficulty(0),imodbits_cloth],
# sar_robe_quilted, sar_robe_quilted.1
["sar_robe_quilted", "Saracen Robe with Quilted", [("sar_robe_quilted",0),("sar_robe_quilted.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(1)|body_armor(12)|leg_armor(0)|difficulty(0),imodbits_cloth],
# sar_robe_mail, sar_robe_mail.1, sar_robe_mail.2
["sar_robe_mail", "Saracen Robe with Mail", [("sar_robe_mail",0),("sar_robe_mail.1",0),("sar_robe_mail.2",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(1)|body_armor(12)|leg_armor(0)|difficulty(0),imodbits_cloth],
# sar_robe_lamellar, sar_robe_lamellar.1, sar_robe_lamellar.2
["sar_robe_lamellar", "Saracen Robe with Lamellar", [("sar_robe_lamellar",0),("sar_robe_lamellar.1",0),("sar_robe_lamellar.2",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(1)|body_armor(12)|leg_armor(0)|difficulty(0),imodbits_cloth],
# sar_robe_cuirass, sar_robe_cuirass.1
["sar_robe_cuirass", "Saracen Robe with Cuirass", [("sar_robe_cuirass",0),("sar_robe_cuirass.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(1)|body_armor(12)|leg_armor(0)|difficulty(0),imodbits_cloth],
# sar_robe_b_new
["sar_robe_b_new", "Saracen Robe", [("sar_robe_b_new",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(2)|body_armor(15)|leg_armor(0)|difficulty(0),imodbits_cloth],
# sar_robe_b_vest, sar_robe_b_vest.1
["sar_robe_b_vest", "Saracen Robe with Vest", [("sar_robe_b_vest",0),("sar_robe_b_vest.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(2)|body_armor(15)|leg_armor(0)|difficulty(0),imodbits_cloth],
# sar_robe_b_nomad, sar_robe_b_nomad.1
["sar_robe_b_nomad", "Saracen Robe with Nomad", [("sar_robe_b_nomad",0),("sar_robe_b_nomad.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(2)|body_armor(15)|leg_armor(0)|difficulty(0),imodbits_cloth],
# sar_robe_b_aketon, sar_robe_b_aketon.1
["sar_robe_b_aketon", "Saracen Robe with Aketon", [("sar_robe_b_aketon",0),("sar_robe_b_aketon.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(2)|body_armor(15)|leg_armor(0)|difficulty(0),imodbits_cloth],
# sar_robe_b_padded, sar_robe_b_padded.1
["sar_robe_b_padded", "Saracen Robe with Padded", [("sar_robe_b_padded",0),("sar_robe_b_padded.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(2)|body_armor(15)|leg_armor(0)|difficulty(0),imodbits_cloth],
# sar_robe_b_quilted, sar_robe_b_quilted.1
["sar_robe_b_quilted", "Saracen Robe with Quilted", [("sar_robe_b_quilted",0),("sar_robe_b_quilted.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(2)|body_armor(15)|leg_armor(0)|difficulty(0),imodbits_cloth],
# sar_robe_b_mail, sar_robe_b_mail.1, sar_robe_b_mail.2
["sar_robe_b_mail", "Saracen Robe with Mail", [("sar_robe_b_mail",0),("sar_robe_b_mail.1",0),("sar_robe_b_mail.2",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(2)|body_armor(15)|leg_armor(0)|difficulty(0),imodbits_cloth],
# sar_robe_b_lamellar, sar_robe_b_lamellar.1, sar_robe_b_lamellar.2
["sar_robe_b_lamellar", "Saracen Robe with Lamellar", [("sar_robe_b_lamellar",0),("sar_robe_b_lamellar.1",0),("sar_robe_b_lamellar.2",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(2)|body_armor(15)|leg_armor(0)|difficulty(0),imodbits_cloth],
# sar_robe_b_cuirass, sar_robe_b_cuirass.1
["sar_robe_b_cuirass", "Saracen Robe with Cuirass", [("sar_robe_b_cuirass",0),("sar_robe_b_cuirass.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(2)|body_armor(15)|leg_armor(0)|difficulty(0),imodbits_cloth],
# arena_tunic_a
["arena_tunic_a", "Arena Tunic", [("arena_tunic_a",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(0)|body_armor(10)|leg_armor(0)|difficulty(0),imodbits_cloth],
# arena_tunic_a_vest, arena_tunic_a_vest.1
["arena_tunic_a_vest", "Arena Tunic with Vest", [("arena_tunic_a_vest",0),("arena_tunic_a_vest.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(0)|body_armor(10)|leg_armor(0)|difficulty(0),imodbits_cloth],
# arena_tunic_a_nomad, arena_tunic_a_nomad.1
["arena_tunic_a_nomad", "Arena Tunic with Nomad", [("arena_tunic_a_nomad",0),("arena_tunic_a_nomad.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(0)|body_armor(10)|leg_armor(0)|difficulty(0),imodbits_cloth],
# arena_tunic_a_leather, arena_tunic_a_leather.1
["arena_tunic_a_leather", "Arena Tunic with Leather", [("arena_tunic_a_leather",0),("arena_tunic_a_leather.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(0)|body_armor(10)|leg_armor(0)|difficulty(0),imodbits_cloth],
# arena_tunic_a_padded, arena_tunic_a_padded.1
["arena_tunic_a_padded", "Arena Tunic with Padded", [("arena_tunic_a_padded",0),("arena_tunic_a_padded.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(0)|body_armor(10)|leg_armor(0)|difficulty(0),imodbits_cloth],
# arena_tunic_a_cuirass, arena_tunic_a_cuirass.1
["arena_tunic_a_cuirass", "Arena Tunic with Cuirass", [("arena_tunic_a_cuirass",0),("arena_tunic_a_cuirass.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(0)|body_armor(10)|leg_armor(0)|difficulty(0),imodbits_cloth],
# arena_tunic_a_haubergeon, arena_tunic_a_haubergeon.1
["arena_tunic_a_haubergeon", "Arena Tunic with Haubergeon", [("arena_tunic_a_haubergeon",0),("arena_tunic_a_haubergeon.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(0)|body_armor(10)|leg_armor(0)|difficulty(0),imodbits_cloth],
# arena_tunic_a_lamellar, arena_tunic_a_lamellar.1
["arena_tunic_a_lamellar", "Arena Tunic with Lamellar", [("arena_tunic_a_lamellar",0),("arena_tunic_a_lamellar.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(0)|body_armor(10)|leg_armor(0)|difficulty(0),imodbits_cloth],
# arena_tunic_a_lamellar_variant, arena_tunic_a_lamellar_variant.1
["arena_tunic_a_lamellar_variant", "Arena Tunic with Lamellar Variant", [("arena_tunic_a_lamellar_variant",0),("arena_tunic_a_lamellar_variant.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(0)|body_armor(10)|leg_armor(0)|difficulty(0),imodbits_cloth],
# arena_tunic_a_mail, arena_tunic_a_mail.1
["arena_tunic_a_mail", "Arena Tunic with Mail", [("arena_tunic_a_mail",0),("arena_tunic_a_mail.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(0)|body_armor(10)|leg_armor(0)|difficulty(0),imodbits_cloth],
# arena_tunic_b
["arena_tunic_b", "Arena Tunic", [("arena_tunic_b",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(1)|body_armor(15)|leg_armor(1)|difficulty(0),imodbits_cloth],
# arena_tunic_b_vest, arena_tunic_b_vest
["arena_tunic_b_vest", "Arena Tunic with Vest", [("arena_tunic_b_vest",0),("arena_tunic_b_vest.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(1)|body_armor(15)|leg_armor(1)|difficulty(0),imodbits_cloth],
# arena_tunic_b_nomad, arena_tunic_b_nomad.1
["arena_tunic_b_nomad", "Arena Tunic with Nomad", [("arena_tunic_b_nomad",0),("arena_tunic_b_nomad.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(1)|body_armor(15)|leg_armor(1)|difficulty(0),imodbits_cloth],
# arena_tunic_b_leather, arena_tunic_b_leather.1
["arena_tunic_b_leather", "Arena Tunic with Leather", [("arena_tunic_b_leather",0),("arena_tunic_b_leather.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(1)|body_armor(15)|leg_armor(1)|difficulty(0),imodbits_cloth],
# arena_tunic_b_padded, arena_tunic_b_padded.1
["arena_tunic_b_padded", "Arena Tunic with Padded", [("arena_tunic_b_padded",0),("arena_tunic_b_padded.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(1)|body_armor(15)|leg_armor(1)|difficulty(0),imodbits_cloth],
# arena_tunic_b_cuirass, arena_tunic_b_cuirass.1
["arena_tunic_b_cuirass", "Arena Tunic with Cuirass", [("arena_tunic_b_cuirass",0),("arena_tunic_b_cuirass.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(1)|body_armor(15)|leg_armor(1)|difficulty(0),imodbits_cloth],
# arena_tunic_b_haubergeon, arena_tunic_b_haubergeon.1
["arena_tunic_b_haubergeon", "Arena Tunic with Haubergeon", [("arena_tunic_b_haubergeon",0),("arena_tunic_b_haubergeon.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(1)|body_armor(15)|leg_armor(1)|difficulty(0),imodbits_cloth],
# arena_tunic_b_lamellar, arena_tunic_b_lamellar.1
["arena_tunic_b_lamellar", "Arena Tunic with Lamellar", [("arena_tunic_b_lamellar",0),("arena_tunic_b_lamellar.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(1)|body_armor(15)|leg_armor(1)|difficulty(0),imodbits_cloth],
# arena_tunic_b_lamellar_variant, arena_tunic_b_lamellar_variant.1
["arena_tunic_b_lamellar_variant", "Arena Tunic with Lamellar Variant", [("arena_tunic_b_lamellar_variant",0),("arena_tunic_b_lamellar_variant.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(1)|body_armor(15)|leg_armor(1)|difficulty(0),imodbits_cloth],
# arena_tunic_b_mail, arena_tunic_b_mail.1
["arena_tunic_b_mail", "Arena Tunic with Mail", [("arena_tunic_b_mail",0),("arena_tunic_b_mail.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(0)|body_armor(15)|leg_armor(0)|difficulty(0),imodbits_cloth],
# arena_tunic_c
["arena_tunic_c", "Arena Tunic", [("arena_tunic_c",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(1)|body_armor(20)|leg_armor(1)|difficulty(0),imodbits_cloth],
# arena_tunic_c_vest, arena_tunic_c_vest.1
["arena_tunic_c_vest", "Arena Tunic with Vest", [("arena_tunic_c_vest",0),("arena_tunic_c_vest.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(0)|body_armor(20)|leg_armor(0)|difficulty(0),imodbits_cloth],
# arena_tunic_c_nomad, arena_tunic_c_nomad.1
["arena_tunic_c_nomad", "Arena Tunic with Nomad", [("arena_tunic_c_nomad",0),("arena_tunic_c_nomad.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(0)|body_armor(20)|leg_armor(0)|difficulty(0),imodbits_cloth],
# arena_tunic_c_leather, arena_tunic_c_leather.1
["arena_tunic_c_leather", "Arena Tunic with Leather", [("arena_tunic_c_leather",0),("arena_tunic_c_leather.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(0)|body_armor(20)|leg_armor(0)|difficulty(0),imodbits_cloth],
# arena_tunic_c_padded, arena_tunic_c_padded.1
["arena_tunic_c_padded", "Arena Tunic with Padded", [("arena_tunic_c_padded",0),("arena_tunic_c_padded.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(0)|body_armor(20)|leg_armor(0)|difficulty(0),imodbits_cloth],
# arena_tunic_c_cuirass, arena_tunic_c_cuirass.1
["arena_tunic_c_cuirass", "Arena Tunic with Cuirass", [("arena_tunic_c_cuirass",0),("arena_tunic_c_cuirass.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(1)|body_armor(20)|leg_armor(1)|difficulty(0),imodbits_cloth],
# arena_tunic_c_haubergeon, arena_tunic_c_haubergeon.1
["arena_tunic_c_haubergeon", "Arena Tunic with Haubergeon", [("arena_tunic_c_haubergeon",0),("arena_tunic_c_haubergeon.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(1)|body_armor(20)|leg_armor(1)|difficulty(0),imodbits_cloth],
# arena_tunic_c_lamellar, arena_tunic_c_lamellar.1
["arena_tunic_c_lamellar", "Arena Tunic with Lamellar", [("arena_tunic_c_lamellar",0),("arena_tunic_c_lamellar.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(1)|body_armor(20)|leg_armor(1)|difficulty(0),imodbits_cloth],
# arena_tunic_c_lamellar_variant, arena_tunic_c_lamellar_variant.1
["arena_tunic_c_lamellar_variant", "Arena Tunic with Lamellar Variant", [("arena_tunic_c_lamellar_variant",0),("arena_tunic_c_lamellar_variant.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(1)|body_armor(20)|leg_armor(1)|difficulty(0),imodbits_cloth],
# arena_tunic_c_mail, arena_tunic_c_mail.1
["arena_tunic_c_mail", "Arena Tunic with Mail", [("arena_tunic_c_mail",0),("arena_tunic_c_mail.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(1)|body_armor(20)|leg_armor(1)|difficulty(0),imodbits_cloth],
# arena_tunic_d
["arena_tunic_d", "Arena Tunic", [("arena_tunic_d",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(1)|body_armor(20)|leg_armor(1)|difficulty(0),imodbits_cloth],
# arena_tunic_d_vest, arena_tunic_d_vest.1
["arena_tunic_d_vest", "Arena Tunic with Vest", [("arena_tunic_d_vest",0),("arena_tunic_d_vest.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(1)|body_armor(20)|leg_armor(1)|difficulty(0),imodbits_cloth],
# arena_tunic_d_nomad, arena_tunic_d_nomad.1
["arena_tunic_d_nomad", "Arena Tunic with Nomad", [("arena_tunic_d_nomad",0),("arena_tunic_d_nomad.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(1)|body_armor(20)|leg_armor(1)|difficulty(0),imodbits_cloth],
# arena_tunic_d_leather, arena_tunic_d_leather.1
["arena_tunic_d_leather", "Arena Tunic with Leather", [("arena_tunic_d_leather",0),("arena_tunic_d_leather.1",0)], itp_type_body_armor, 0, 399,abundance(100)|head_armor(0)|body_armor(24)|leg_armor(6)|difficulty(0),imodbits_cloth],
# arena_tunic_d_padded, arena_tunic_d_padded.1
["arena_tunic_d_padded", "Arena Tunic with Padded", [("arena_tunic_d_padded",0),("arena_tunic_d_padded.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(0)|body_armor(20)|leg_armor(0)|difficulty(0),imodbits_cloth],
# arena_tunic_d_cuirass, arena_tunic_d_cuirass.1
["arena_tunic_d_cuirass", "Arena Tunic with Cuirass", [("arena_tunic_d_cuirass",0),("arena_tunic_d_cuirass.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(0)|body_armor(20)|leg_armor(0)|difficulty(0),imodbits_cloth],
# arena_tunic_d_haubergeon, arena_tunic_d_haubergeon.1
["arena_tunic_d_haubergeon", "Arena Tunic with Haubergeon", [("arena_tunic_d_haubergeon",0),("arena_tunic_d_haubergeon.1",0)], itp_type_body_armor, 0, 599,abundance(100)|head_armor(0)|body_armor(35)|leg_armor(15)|difficulty(0),imodbits_armor],
# arena_tunic_d_lamellar, arena_tunic_d_lamellar.1
["arena_tunic_d_lamellar", "Arena Tunic with Lamellar", [("arena_tunic_d_lamellar",0),("arena_tunic_d_lamellar.1",0)], itp_type_body_armor, 0, 499,abundance(100)|head_armor(0)|body_armor(37)|leg_armor(15)|difficulty(0),imodbits_armor],
# arena_tunic_d_lamellar_variant, arena_tunic_d_lamellar_variant.1
["arena_tunic_d_lamellar_variant", "Arena Tunic with Lamellar Variant", [("arena_tunic_d_lamellar_variant",0),("arena_tunic_d_lamellar_variant.1",0)], itp_type_body_armor, 0, 459,abundance(100)|head_armor(0)|body_armor(34)|leg_armor(15)|difficulty(0),imodbits_armor],
# arena_tunic_d_mail, arena_tunic_d_mail.1
["arena_tunic_d_mail", "Arena Tunic with Mail", [("arena_tunic_d_mail",0),("arena_tunic_d_mail.1",0)], itp_type_body_armor, 0, 699,abundance(100)|head_armor(0)|body_armor(39)|leg_armor(16)|difficulty(0),imodbits_armor],
# peasant_tunic_new
["peasant_tunic_new", "Peasant Tunic", [("peasant_tunic_new",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(0)|body_armor(6)|leg_armor(3)|difficulty(0),imodbits_cloth],
# peasant_tunic_padded, peasant_tunic_padded.1
["peasant_tunic_padded", "Peasant Tunic with Padded", [("peasant_tunic_padded",0),("peasant_tunic_padded.1",0)], itp_type_body_armor, 0, 439,abundance(100)|head_armor(0)|body_armor(25)|leg_armor(6)|difficulty(0),imodbits_cloth],
# peasant_tunic_cuirass, peasant_tunic_cuirass.1, peasant_tunic_cuirass.2
["peasant_tunic_cuirass", "Peasant Tunic with Cuirass", [("peasant_tunic_cuirass",0),("peasant_tunic_cuirass.1",0),("peasant_tunic_cuirass.2",0)], itp_type_body_armor, 0, 499,abundance(100)|head_armor(0)|body_armor(29)|leg_armor(6)|difficulty(0),imodbits_armor],
# peasant_tunic_lamellar, peasant_tunic_lamellar.1, peasant_tunic_lamellar.2, peasant_tunic_lamellar.3
["peasant_tunic_lamellar", "Peasant Tunic with Lamellar", [("peasant_tunic_lamellar",0),("peasant_tunic_lamellar.1",0),("peasant_tunic_lamellar.2",0),("peasant_tunic_lamellar.3",0)], itp_type_body_armor, 0, 699,abundance(100)|head_armor(0)|body_armor(35)|leg_armor(9)|difficulty(0),imodbits_armor],
# rawhide_coat_new_a
["rawhide_coat_new_a", "Rawhide Coat", [("rawhide_coat_new_a",0)], itp_type_body_armor, 0, 199,abundance(100)|head_armor(0)|body_armor(15)|leg_armor(8)|difficulty(0),imodbits_cloth],
# rawhide_coat_new
["rawhide_coat_new", "Rawhide Coat", [("rawhide_coat_new",0)], itp_type_body_armor, 0, 249,abundance(100)|head_armor(0)|body_armor(15)|leg_armor(12)|difficulty(0),imodbits_cloth],
# rawhide_coat_leather, rawhide_coat_leather.1
["rawhide_coat_leather", "Rawhide Coat with Leather", [("rawhide_coat_leather",0),("rawhide_coat_leather.1",0)], itp_type_body_armor, 0, 399,abundance(100)|head_armor(0)|body_armor(21)|leg_armor(11)|difficulty(0),imodbits_cloth],
# rawhide_coat_leather_lamellar, rawhide_coat_leather_lamellar.1
["rawhide_coat_leather_lamellar", "Rawhide Coat with Leather Lamellar", [("rawhide_coat_leather_lamellar",0),("rawhide_coat_leather_lamellar.1",0)], itp_type_body_armor, 0, 499,abundance(100)|head_armor(0)|body_armor(32)|leg_armor(15)|difficulty(0),imodbits_cloth],
# rawhide_coat_mail, rawhide_coat_mail.1, rawhide_coat_mail.2
["rawhide_coat_mail", "Rawhide Coat with Mail", [("rawhide_coat_mail",0),("rawhide_coat_mail.1",0),("rawhide_coat_mail.2",0)], itp_type_body_armor, 0, 599,abundance(100)|head_armor(0)|body_armor(40)|leg_armor(19)|difficulty(0),imodbits_cloth],
# rawhide_coat_lamellar, rawhide_coat_lamellar.1
["rawhide_coat_lamellar", "Rawhide Coat with Lamellar", [("rawhide_coat_lamellar",0),("rawhide_coat_lamellar.1",0)], itp_type_body_armor, 0, 599,abundance(100)|head_armor(0)|body_armor(36)|leg_armor(15)|difficulty(0),imodbits_cloth],
# khergit_vest_a_new, khergit_vest_a_new.1
["khergit_vest_a_new", "Khergit Vest", [("khergit_vest_a_new",0),("khergit_vest_a_new.1",0)], itp_type_body_armor, 0, 269,abundance(100)|head_armor(0)|body_armor(18)|leg_armor(8)|difficulty(0),imodbits_cloth],
# khergit_vest_a_lamellar
["khergit_vest_a_lamellar", "Khergit Vest with Lamellar", [("khergit_vest_a_lamellar",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(3)|body_armor(20)|leg_armor(3)|difficulty(0),imodbits_cloth],
# khergit_vest_a_mail, khergit_vest_a_mail.1
["khergit_vest_a_mail", "Khergit Vest with Mail", [("khergit_vest_a_mail",0),("khergit_vest_a_mail.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(3)|body_armor(20)|leg_armor(3)|difficulty(0),imodbits_cloth],
# khergit_vest_b_new, khergit_vest_b_new.1
["khergit_vest_b_new", "Khergit Vest", [("khergit_vest_b_new",0),("khergit_vest_b_new.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(3)|body_armor(20)|leg_armor(3)|difficulty(0),imodbits_cloth],
# khergit_vest_b_lamellar
["khergit_vest_b_lamellar", "Khergit Vest with Lamellar", [("khergit_vest_b_lamellar",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(3)|body_armor(20)|leg_armor(3)|difficulty(0),imodbits_cloth],
# khergit_vest_b_mail, khergit_vest_b_mail.1
["khergit_vest_b_mail", "Khergit Vest with Mail", [("khergit_vest_b_mail",0),("khergit_vest_b_mail.1",0)], itp_type_body_armor, 0, 99,abundance(100)|head_armor(3)|body_armor(20)|leg_armor(3)|difficulty(0),imodbits_cloth],

["cuir_bouilli_with_pelt", "Cuir Bouilli with Pelt", [("cuir_bouilli_b",0),("cuir_bouilli_b.1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 3400 , weight(24)|abundance(10)|head_armor(2)|body_armor(51)|leg_armor(15)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_4] ],
["banded_armor_b", "Banded Armor with Pelt", [("banded_armor_b",0),("banded_armor_b.1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 3250 , weight(24)|abundance(10)|head_armor(2)|body_armor(49)|leg_armor(15)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_4] ],
["banded_armor_c", "Nordic Banded Armor", [("banded_armor_c",0),("banded_armor_c.1",0),("banded_armor_c.2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 3250 , weight(24)|abundance(10)|head_armor(2)|body_armor(49)|leg_armor(15)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_4] ],
["banded_armor_d", "Nordic Banded Armor", [("banded_armor_d",0),("banded_armor_d.1",0),("banded_armor_d.2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 3250 , weight(24)|abundance(10)|head_armor(2)|body_armor(49)|leg_armor(15)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_4] ],

# Custom mod armors
# Used once - should be removed?
["m_coif_a", "Mail Coif", [("elite_cavalary_coif",0), ("elite_cavalary_coif_ixmesh_inv",ixmesh_inventory)], itp_type_head_armor|itp_attach_armature, 0, 459, weight(2)|abundance(100)|head_armor(43)|body_armor(2)|leg_armor(0)|difficulty(8) ,imodbits_plate ],

["m_barbuta_open_a", "Barbute", [("Barbuta_E",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 959, weight(1.25)|abundance(100)|head_armor(39)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_7, fac_kingdom_9] ],
["m_barbuta_open_b", "Barbute", [("Barbuta_G",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 999, weight(1.25)|abundance(100)|head_armor(39)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_7, fac_kingdom_9] ],

["m_barbuta_open_red", "Decorated Barbute", [("Barbuta_B",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 959, weight(1.25)|abundance(100)|head_armor(39)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_7, fac_kingdom_9] ],
["m_barbuta_open_nasal", "Barbute with Nasal", [("Barbuta_B_Hinged_Nasal",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 1099, weight(1.25)|abundance(100)|head_armor(41)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_7, fac_kingdom_9] ],

["m_barbuta_a", "Barbute", [("Barbuta_A",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 1139, weight(1.5)|abundance(100)|head_armor(43)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_7, fac_kingdom_9] ],
["m_barbuta_b", "Barbute", [("Barbuta_C",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 1139, weight(1.5)|abundance(100)|head_armor(43)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_7, fac_kingdom_9] ],
["m_barbuta_c", "Barbute", [("Barbuta_F",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 1139, weight(1.5)|abundance(100)|head_armor(43)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_7, fac_kingdom_9] ],

["m_onion_chapel_light_a", "Onion Topped Chapel-De-Fer on Cloth", [("Onion_Cloth_A",0), ("Onion_Cloth_A.1",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 459, weight(2)|abundance(100)|head_armor(43)|body_armor(2)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_7] ],
["m_onion_chapel_light_b", "Onion Topped Chapel-De-Fer on Cloth", [("Onion_Cloth_B",0), ("Onion_Cloth_B.1",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 459, weight(2)|abundance(100)|head_armor(43)|body_armor(2)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_7] ],

["m_german_chapel_padded_a", "Chapel-De-Fer on Padded Cloth", [("German_Padded_A",0), ("German_Padded_A.1",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 459, weight(2)|abundance(100)|head_armor(43)|body_armor(4)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_7] ],
["m_german_chapel_mail_a", "Chapel-De-Fer on Mail", [("German_Mail_A",0), ("German_Mail_A.1",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 669, weight(2)|abundance(100)|head_armor(46)|body_armor(8)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_7] ],

["m_german_chapel_heavy_a", "Great Chapel-De-Fer With Bevor", [("German_Mail_Bevor_A",0), ("German_Mail_Bevor_A.1",0), ("German_Mail_Bevor_A.2",0), ("German_Mail_Bevor_A.3",0), ("German_Mail_Bevor_A.4",0), ("German_Mail_Bevor_A.5",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 2319, weight(4)|abundance(100)|head_armor(52)|body_armor(12)|leg_armor(0)|difficulty(12) ,imodbits_plate, [], [fac_kingdom_7] ],
["m_german_chapel_heavy_a", "Great Chapel-De-Fer With Bevor", [("German_Mail_Bevor_B",0), ("German_Mail_Bevor_B.1",0), ("German_Mail_Bevor_B.2",0), ("German_Mail_Bevor_B.3",0), ("German_Mail_Bevor_B.4",0), ("German_Mail_Bevor_B.5",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 2319, weight(4)|abundance(100)|head_armor(52)|body_armor(12)|leg_armor(0)|difficulty(12) ,imodbits_plate, [], [fac_kingdom_7] ],

["m_chapel_light_a", "Chapel-De-Fer on Cloth", [("chapel_de_fer_cloth1",0), ("chapel_de_fer_cloth1.1",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 459, weight(2)|abundance(100)|head_armor(43)|body_armor(2)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_7] ],
["m_chapel_light_b", "Chapel-De-Fer on Padded", [("chapel_de_fer_cloth2",0), ("chapel_de_fer_cloth2.1",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 499, weight(2)|abundance(100)|head_armor(43)|body_armor(4)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_7] ],
["m_chapel_light_c", "Chapel-De-Fer on Cloth", [("chapel_de_fer_cloth3",0), ("chapel_de_fer_cloth3.1",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 499, weight(2)|abundance(100)|head_armor(43)|body_armor(4)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_7] ],

["m_kattle_a", "Eyeslot Kattlehat", [("eyeslot_kettlehat",0), ("eyeslot_kettlehat.1",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 499, weight(2)|abundance(100)|head_armor(43)|body_armor(2)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_7] ],

["m_chapel_heavy_a", "Chapel-De-Fer on Mail", [("chapel_de_fer_mail1",0), ("chapel_de_fer_mail1.1",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 659, weight(2.5)|abundance(100)|head_armor(46)|body_armor(8)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_7] ],
["m_chapel_heavy_b", "Chapel-De-Fer on Mail", [("chapel_de_fer_mail2",0), ("chapel_de_fer_mail2.1",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 659, weight(2.5)|abundance(100)|head_armor(46)|body_armor(8)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_7] ],
["m_chapel_heavy_c", "Chapel-De-Fer on Mail", [("chapel_de_fer_mail3",0), ("chapel_de_fer_mail3.1",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 659, weight(2.5)|abundance(100)|head_armor(46)|body_armor(8)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_7] ],

["m_houndskull_a", "Houndskull Bascinet", [("hounskull",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 799, weight(2.5)|abundance(100)|head_armor(49)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_7, fac_kingdom_5] ],

["m_bascinet_a", "Bascinet", [("zitta_bascinet_novisor",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 559, weight(2)|abundance(100)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_7, fac_kingdom_5] ],
["m_bascinet_b", "Visored Bascinet", [("zitta_bascinet",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 659, weight(2.5)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_7, fac_kingdom_5] ],

["m_sallet_light_a", "Sallet", [("sallet_c",0), ("sallet_c.1",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 399, weight(1.75)|abundance(100)|head_armor(39)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_7] ],
["m_sallet_light_b", "Sallet with Bevor", [("sallet_c_bevor",0), ("sallet_c_bevor.1",0), ("sallet_c_bevor.2",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 499, weight(2)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_7] ],
["m_sallet_light_c", "Sallet on Cloth", [("sallet_d",0), ("sallet_d.1",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 399, weight(2)|abundance(100)|head_armor(39)|body_armor(2)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_7] ],

["m_sallet_heavy_a", "Closed Sallet", [("sallet_a_closed1",0), ("sallet_a_closed1.1",0), ("sallet_a_closed1.2", 0)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 599, weight(2.5)|abundance(100)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_7] ],
["m_sallet_heavy_b", "Closed Sallet", [("sallet_a_closed2",0), ("sallet_a_closed2.1",0), ("sallet_a_closed2.2", 0)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 599, weight(2.5)|abundance(100)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_7] ],
["m_sallet_heavy_c", "Open Sallet", [("sallet_a_open1",0), ("sallet_a_open1.1",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 499, weight(2.5)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_7] ],
["m_sallet_heavy_d", "Open Sallet", [("sallet_a_open2",0), ("sallet_a_open2.1",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 499, weight(2.5)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_7] ],

["m_sallet_black_a", "Closed Sallet Black", [("sallet_b_closed1",0), ("sallet_b_closed1.1",0), ("sallet_b_closed1.2", 0)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 599, weight(2.5)|abundance(100)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_7] ],
["m_sallet_black_b", "Closed Sallet Black", [("sallet_b_closed2",0), ("sallet_b_closed2.1",0), ("sallet_b_closed2.2", 0)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 599, weight(2.5)|abundance(100)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_7] ],
["m_sallet_black_c", "Open Sallet Black", [("sallet_b_open1",0), ("sallet_b_open1.1",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 499, weight(2.5)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_7] ],
["m_sallet_black_d", "Open Sallet Black", [("sallet_b_open2",0), ("sallet_a_open2.1",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 499, weight(2.5)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_7] ],

["m_onion_chapel", "Onion Top Chapel-de-Fer", [("prato_chapel-de-fer",0)], itp_merchandise|itp_type_head_armor, 0, 459, weight(2.5)|abundance(100)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_7, fac_kingdom_5] ],

["m_onion_bascinet_a", "Onion Top Bascinet", [("onion-top_bascinet",0)], itp_merchandise|itp_type_head_armor, 0, 459, weight(2.5)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_7, fac_kingdom_5] ],
["m_onion_bascinet_b", "Onion Top Bascinet with Visor", [("pigface_klappvisor",0)], itp_merchandise|itp_type_head_armor, 0, 499, weight(2.5)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_7, fac_kingdom_5] ],
["m_onion_bascinet_c", "Onion Top Bascinet with Visor (Opened)", [("pigface_klappvisor_open",0)], itp_merchandise|itp_type_head_armor, 0, 499, weight(2.5)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_7, fac_kingdom_5] ],

["m_padded_dark_a", "Black Padded Vest", [("padded_black",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 299 , weight(10)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(7)|difficulty(0) ,imodbits_armor, [], [] ],
["m_padded_dark_b", "Gray Padded Vest", [("padded_gray",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 299 , weight(10)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(7)|difficulty(0) ,imodbits_armor, [], [] ],
["m_padded_dark_c", "Light Gray Padded Vest", [("padded_light_gray",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 299 , weight(10)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(7)|difficulty(0) ,imodbits_armor, [], [] ],

["m_aketon_forest_a", "Green Forester Aketon", [("aketon_two_tones_a",0), ("aketon_two_tones_a.1",0), ("aketon_two_tones_a.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,251 , weight(12)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], [] ], 
["m_aketon_forest_b", "Green Forester Aketon", [("aketon_two_tones_b",0), ("aketon_two_tones_b.1",0), ("aketon_two_tones_b.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,329 , weight(14)|abundance(100)|head_armor(0)|body_armor(27)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], [] ], 
["m_aketon_forest_c", "Green Forester Aketon with Mail", [("aketon_two_tones_c",0), ("aketon_two_tones_c.1",0), ("aketon_two_tones_c.2",0), ("aketon_two_tones_c.3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,329 , weight(18)|abundance(100)|head_armor(0)|body_armor(37)|leg_armor(6)|difficulty(0) ,imodbits_armor, [], [] ], 

["m_aketon_old_a", "Old Aketon", [("aketon_old_a",0), ("aketon_old_a.1",0), ("aketon_old_a.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,251 , weight(12)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], [] ], 
["m_aketon_old_b", "Old Aketon", [("aketon_old_b",0), ("aketon_old_b.1",0), ("aketon_old_b.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,251 , weight(12)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], [] ], 
["m_aketon_old_c", "Old Aketon with Kneekops", [("aketon_kneecops_old",0), ("aketon_kneecops_old.1",0), ("aketon_kneecops_old.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,459 , weight(19)|abundance(100)|head_armor(0)|body_armor(27)|leg_armor(17)|difficulty(0) ,imodbits_cloth, [], [] ], 

["m_hauberk_old_a", "Hauberk on Old Aketon", [("hauberk_old",0), ("hauberk_old.1",0), ("hauberk_old.2",0), ("hauberk_old.3",0), ("hauberk_old.4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,899 , weight(24)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(9)|difficulty(0) ,imodbits_armor, [], [] ], 

["m_aketon_black_a", "Black Aketon", [("aketon_black",0), ("aketon_black.1",0), ("aketon_black.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,399 , weight(13)|abundance(100)|head_armor(0)|body_armor(24)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], [] ], 
["m_aketon_black_b", "Black Aketon with Kneekops", [("aketon_kneecops_black",0), ("aketon_kneecops_black.1",0), ("aketon_kneecops_black.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,459 , weight(19)|abundance(100)|head_armor(0)|body_armor(27)|leg_armor(17)|difficulty(0) ,imodbits_cloth, [], [] ], 

["m_hauberk_black_a", "Black Hauberk", [("hauberk_black",0), ("hauberk_black.1",0), ("hauberk_black.2",0), ("hauberk_black.3",0), ("hauberk_black.4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,899 , weight(24)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(9)|difficulty(0) ,imodbits_armor, [], [] ], 

["m_aketon_a", "Aketon", [("aketon",0), ("aketon.1",0), ("aketon.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,297 , weight(11)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_7] ], 
["m_aketon_b", "Aketon with Kneekops", [("aketon_kneecops",0), ("aketon_kneecops.1",0), ("aketon_kneecops.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,389 , weight(17)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(17)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_7] ], 

["m_hauberk_a", "Hauberk", [("hauberk",0), ("hauberk.1",0), ("hauberk.2",0), ("hauberk.3",0), ("hauberk.4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,899 , weight(22)|abundance(100)|head_armor(0)|body_armor(41)|leg_armor(9)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_7] ], 
["m_hauberk_b", "Hauberk with Plates", [("hauberk2",0), ("hauberk2.1",0), ("hauberk2.2",0), ("hauberk2.3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1199 , weight(25)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(19)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_7] ], 
["m_hauberk_c", "Hauberk with Kneekops", [("hauberk3",0), ("hauberk3.1",0), ("hauberk3.2",0), ("hauberk3.3",0), ("hauberk3.4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1059 , weight(22)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(16)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_7] ], 

["m_brigandine_a", "Heavy Brigandine with Mail", [("brigandine_black_mail",0), ("brigandine_black_mail.1",0), ("brigandine_black_mail.2",0), ("brigandine_black_mail.3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1299 , weight(25)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(19)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_7] ], 
["m_brigandine_b", "Heavy Brigandine", [("brigandine_blue",0), ("brigandine_blue.1",0), ("brigandine_blue.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,999 , weight(21)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(19)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_7] ], 
["m_brigandine_c", "Brigandine with Mail", [("brigandine_brown_mail",0), ("brigandine_brown_mail.1",0), ("brigandine_brown_mail.2",0), ("brigandine_brown_mail.3",0), ("brigandine_brown_mail.4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,999 , weight(23)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(10)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_7] ], 
["m_brigandine_d", "Brigandine", [("brigandine_green",0), ("brigandine_green.1",0), ("brigandine_green.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,799 , weight(20)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(10)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_7] ], 
["m_brigandine_e", "Brigandine with Mail", [("brigandine_green_mail",0), ("brigandine_green_mail.1",0), ("brigandine_green_mail.2",0), ("brigandine_green_mail.3",0), ("brigandine_green_mail.4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1159 , weight(25)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(19)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_7] ], 
["m_brigandine_f", "Heavy Brigandine", [("brigandine_red",0), ("brigandine_red.1",0), ("brigandine_red.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1199 , weight(24)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(20)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_7] ], 
["m_brigandine_g", "Heavy Brigandine with Mail", [("brigandine_red_mail",0), ("brigandine_red_mail.1",0), ("brigandine_red_mail.2",0), ("brigandine_red_mail.3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1359 , weight(26)|abundance(100)|head_armor(0)|body_armor(51)|leg_armor(19)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_7] ], 

["m_yeomen_a", "Aketon with Hood", [("yeomen_a",0), ("yeomen_a.1",0), ("yeomen_a.2",0), ("yeomen_a.3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,299 , weight(11)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_7] ], 
["m_yeomen_b", "Aketon with Hood", [("yeomen_b",0), ("yeomen_b.1",0), ("yeomen_b.2",0), ("yeomen_b.3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,399 , weight(17)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(17)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_7] ], 

["m_trickshot_a", "Heavy Brigandine with Hood", [("trickshot_a",0), ("trickshot_a.1",0), ("trickshot_a.2",0), ("trickshot_a.3",0),("trickshot_a.4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,399 , weight(26)|abundance(100)|head_armor(0)|body_armor(51)|leg_armor(19)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_7] ], 

["m_corrazina_a", "Corrazina", [("corrazina_red",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1599 , weight(24)|abundance(100)|head_armor(0)|body_armor(51)|leg_armor(19)|difficulty(10) ,imodbits_armor, [], [fac_kingdom_5, fac_kingdom_9] ], 
["m_corrazina_b", "Corrazina", [("corrazina_grey",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1599 , weight(24)|abundance(100)|head_armor(0)|body_armor(51)|leg_armor(19)|difficulty(10) ,imodbits_armor, [], [fac_kingdom_5, fac_kingdom_9] ], 
["m_corrazina_c", "Corrazina", [("corrazina_green",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1599 , weight(24)|abundance(100)|head_armor(0)|body_armor(51)|leg_armor(19)|difficulty(10) ,imodbits_armor, [], [fac_kingdom_5, fac_kingdom_9] ], 

["m_corrazina_a_cloak", "Corrazina with Cloak", [("corrazina_red_cloak",0),("corrazina_red_cloak.1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1899 , weight(24)|abundance(100)|head_armor(0)|body_armor(51)|leg_armor(19)|difficulty(10) ,imodbits_armor, [], [fac_kingdom_7, fac_kingdom_9] ], 

["m_full_plate_a", "Full Plate with Pelt", [("full_plate_armor_b",0),("full_plate_armor_b.1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,2999 , weight(24)|abundance(100)|head_armor(0)|body_armor(56)|leg_armor(19)|difficulty(15) ,imodbits_armor, [], [fac_kingdom_7] ], 
["m_full_plate_b", "Full Plate with Cloack & Pelt", [("full_plate_armor_c",0),("full_plate_armor_c.1",0),("full_plate_armor_c.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,2999 , weight(24)|abundance(100)|head_armor(0)|body_armor(56)|leg_armor(19)|difficulty(15) ,imodbits_armor, [], [fac_kingdom_7] ], 

["m_churburg_a", "Churburg Plate", [("churburg_13",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1799 , weight(24)|abundance(100)|head_armor(0)|body_armor(55)|leg_armor(21)|difficulty(10) ,imodbits_armor, [], [fac_kingdom_7, fac_kingdom_9] ], 
["m_churburg_b", "Churburg Plate", [("churburg_13_brass",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1799 , weight(24)|abundance(100)|head_armor(0)|body_armor(55)|leg_armor(21)|difficulty(10) ,imodbits_armor, [], [fac_kingdom_7, fac_kingdom_9] ], 
["m_churburg_c", "Churburg Plate on Mail", [("churburg_13_mail",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,2059 , weight(27)|abundance(100)|head_armor(0)|body_armor(59)|leg_armor(21)|difficulty(12) ,imodbits_armor, [], [fac_kingdom_7, fac_kingdom_9] ], 
["m_churburg_d", "Churburg Plate on Mail with Decorations", [("churburg_13_lord",0), ("churburg_13_lord.1",0), ("churburg_13_lord.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,2399 , weight(27)|abundance(100)|head_armor(3)|body_armor(60)|leg_armor(21)|difficulty(12) ,imodbits_armor, [], [fac_kingdom_7, fac_kingdom_9] ], 
["m_churburg_e", "Churburg Plate on Mail with Cloak", [("churburg_13_cloak",0), ("churburg_13_cloak.1",0), ("churburg_13_cloak.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,2399 , weight(27)|abundance(100)|head_armor(3)|body_armor(60)|leg_armor(21)|difficulty(12) ,imodbits_armor, [], [fac_kingdom_7, fac_kingdom_9] ],
["m_churburg_f", "Churburg Plate on Mail with Vest", [("churburg_13_vest",0), ("churburg_13_vest.1",0), ("churburg_13_vest.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,2399 , weight(27)|abundance(100)|head_armor(3)|body_armor(60)|leg_armor(21)|difficulty(12) ,imodbits_armor, [], [fac_kingdom_7, fac_kingdom_9] ],

["m_hose_a", "Woolen Hose", [("hosen_blue",0), ("hosen_blue.1",0)], itp_merchandise|itp_type_foot_armor|itp_civilian|itp_attach_armature, 0, 12, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(4)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_7, fac_kingdom_5, fac_kingdom_9, fac_kingdom_10] ],
["m_hose_b", "Woolen Hose", [("hosen_brown",0), ("hosen_brown.1",0)], itp_merchandise|itp_type_foot_armor|itp_civilian|itp_attach_armature, 0, 12, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(4)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_7, fac_kingdom_5, fac_kingdom_9, fac_kingdom_10] ],
["m_hose_c", "Woolen Hose", [("hosen_green",0), ("hosen_green.1",0)], itp_merchandise|itp_type_foot_armor|itp_civilian|itp_attach_armature, 0, 12, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(4)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_7, fac_kingdom_5, fac_kingdom_9, fac_kingdom_10] ],
["m_hose_d", "Woolen Hose", [("hosen_red",0), ("hosen_red.1",0)], itp_merchandise|itp_type_foot_armor|itp_civilian|itp_attach_armature, 0, 12, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(4)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_7, fac_kingdom_5, fac_kingdom_9, fac_kingdom_10] ],
["m_hose_e", "Woolen Hose", [("hosen_yellow",0), ("hosen_yellow.1",0)], itp_merchandise|itp_type_foot_armor|itp_civilian|itp_attach_armature, 0, 12, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(4)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_7, fac_kingdom_5, fac_kingdom_9, fac_kingdom_10] ],

["m_leather_boots_a", "Leather Boots", [("leather_boots",0), ("leather_boots.1",0)], itp_merchandise|itp_type_foot_armor|itp_civilian|itp_attach_armature,0, 179 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth],

["m_greaves_a", "Steel Greaves", [("steel_greaves",0), ("steel_greaves.1",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature,0, 1099 , weight(2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(36)|difficulty(0) ,imodbits_armor ],
["m_greaves_b", "Light Steel Greaves", [("steel_greaves2",0), ("steel_greaves2.1",0), ("steel_greaves2.2",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature,0, 1099 , weight(2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(36)|difficulty(0) ,imodbits_armor ],

["m_gloves_a","Leather Gauntlets", [("leather_gauntlet_L",0)], itp_merchandise|itp_type_hand_armor,0, 499, weight(0.5)|abundance(100)|body_armor(4)|difficulty(0),imodbits_cloth],

["m_gauntlets_a","Plate Gauntlets", [("demi_gauntlets_L",0)], itp_merchandise|itp_type_hand_armor,0, 799, weight(0.75)|abundance(100)|body_armor(6)|difficulty(0),imodbits_armor],
["m_gauntlets_b","Plate Gauntlets", [("finger_gauntlets_L",0)], itp_merchandise|itp_type_hand_armor,0, 849, weight(0.85)|abundance(100)|body_armor(7)|difficulty(0),imodbits_armor],

# tauria items
["mt_hood_a", "Hood", [("helm10",0)], itp_merchandise|itp_type_head_armor, 0, 99, weight(0.5)|abundance(100)|head_armor(9)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_10] ],
["mt_hood_a2", "Hood", [("helm10_g",0)], itp_merchandise|itp_type_head_armor, 0, 99, weight(0.5)|abundance(100)|head_armor(9)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_10] ],
["mt_hood_a3", "Hood", [("helm10_l",0)], itp_merchandise|itp_type_head_armor, 0, 99, weight(0.5)|abundance(100)|head_armor(9)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_10] ],
["mt_hood_a4", "Hood", [("helm10_w",0)], itp_merchandise|itp_type_head_armor, 0, 99, weight(0.5)|abundance(100)|head_armor(9)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_10] ],

["mt_sallet_a", "Sallet", [("helm11",0)], itp_merchandise|itp_type_head_armor, 0, 599, weight(2.5)|abundance(100)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_7, fac_kingdom_5, fac_kingdom_9, fac_kingdom_10] ],
["mt_sallet_a2", "Sallet", [("helm12",0)], itp_merchandise|itp_type_head_armor, 0, 599, weight(2.5)|abundance(100)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_7, fac_kingdom_5, fac_kingdom_9, fac_kingdom_10] ],

["mt_full_helm_a", "Full Helmet", [("helm16",0)], itp_merchandise|itp_type_head_armor|itp_covers_head, 0, 999, weight(2.5)|abundance(1)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_9, fac_kingdom_10] ],
["mt_full_helm_b", "Full Helmet", [("helm21",0)], itp_merchandise|itp_type_head_armor|itp_covers_head, 0, 999, weight(2.5)|abundance(1)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_9, fac_kingdom_10] ],
["mt_full_helm_b2", "Full Helmet", [("helm22",0)], itp_merchandise|itp_type_head_armor|itp_covers_head, 0, 999, weight(2.5)|abundance(1)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_9, fac_kingdom_10] ],
["mt_full_helm_c", "Full Helmet", [("helm26",0)], itp_merchandise|itp_type_head_armor|itp_covers_head, 0, 999, weight(2.5)|abundance(1)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_9, fac_kingdom_10] ],
["mt_full_helm_d", "Full Helmet", [("helm27",0)], itp_merchandise|itp_type_head_armor|itp_covers_head, 0, 999, weight(2.5)|abundance(1)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_9, fac_kingdom_10] ],
["mt_full_helm_d2", "Full Helmet", [("helm27_r",0)], itp_merchandise|itp_type_head_armor|itp_covers_head, 0, 999, weight(2.5)|abundance(1)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_9, fac_kingdom_10] ],
["mt_full_helm_e", "Full Helmet", [("helm6",0)], itp_merchandise|itp_type_head_armor|itp_covers_head, 0, 999, weight(2.5)|abundance(1)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_9, fac_kingdom_10] ],
["mt_full_helm_f", "Full Helmet", [("helm8",0)], itp_merchandise|itp_type_head_armor|itp_covers_head, 0, 999, weight(2.5)|abundance(1)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_9, fac_kingdom_10] ],

["mt_bascinet_a", "Bascinet with Visor", [("helm17",0)], itp_merchandise|itp_type_head_armor, 0, 999, weight(2.5)|abundance(100)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_9, fac_kingdom_10] ],
["mt_bascinet_b", "Bascinet with Aventail", [("helm28",0)], itp_merchandise|itp_type_head_armor, 0, 799, weight(2)|abundance(100)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_9, fac_kingdom_10] ],
["mt_bascinet_b2", "Bascinet", [("helm29",0)], itp_merchandise|itp_type_head_armor, 0, 799, weight(2)|abundance(100)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_9, fac_kingdom_10] ],
["mt_bascinet_c", "Bascinet with Houndskull Visor", [("helm3",0)], itp_merchandise|itp_type_head_armor, 0, 999, weight(2.5)|abundance(100)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_9, fac_kingdom_10] ],
["mt_bascinet_c2", "Bascinet", [("helm4",0)], itp_merchandise|itp_type_head_armor, 0, 699, weight(1.75)|abundance(100)|head_armor(43)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_9, fac_kingdom_10] ],
["mt_bascinet_d", "Bascinet", [("helm30",0)], itp_merchandise|itp_type_head_armor, 0, 799, weight(2)|abundance(100)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_9, fac_kingdom_10] ],

["mt_armet_a", "Armet", [("helm19",0)], itp_merchandise|itp_type_head_armor|itp_covers_head, 0, 1199, weight(2.5)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, [], [fac_kingdom_10] ],
["mt_armet_a2", "Armet with Decorations", [("helm20",0), ("helm20.1",0)], itp_merchandise|itp_type_head_armor|itp_covers_head, 0, 1199, weight(2.5)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, [], [fac_kingdom_10] ],
["mt_armet_b", "Heavy Armet", [("helm5",0)], itp_merchandise|itp_type_head_armor, 0, 1199, weight(2.5)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, [], [fac_kingdom_10] ],

["mt_siege_helm_a", "Siege Crossbowman Helmet", [("helm13",0)], itp_merchandise|itp_type_head_armor, 0, 409, weight(2.5)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate, [], [fac_kingdom_9] ],
["mt_siege_helm_b", "Siege Crossbowman Helmet", [("helm14",0)], itp_merchandise|itp_type_head_armor, 0, 409, weight(2.5)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate, [], [fac_kingdom_9] ],
["mt_siege_helm_c", "Siege Crossbowman Helmet", [("helm31",0)], itp_merchandise|itp_type_head_armor, 0, 409, weight(2.5)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate, [], [fac_kingdom_9] ],
["mt_siege_helm_d", "Siege Crossbowman Helmet", [("helm32",0)], itp_merchandise|itp_type_head_armor, 0, 409, weight(2.5)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate, [], [fac_kingdom_9] ],

["mt_knight_helm_a", "Knighty Helmet of Tauria", [("helm15",0), ("helm15.1",0)], itp_merchandise|itp_type_head_armor, 0, 999, weight(2.5)|abundance(100)|head_armor(59)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate, [], [fac_kingdom_9] ],
["mt_knight_helm_b", "Knighty Helmet of Tauria", [("helm23",0), ("helm23.1",0)], itp_merchandise|itp_type_head_armor, 0, 999, weight(2.5)|abundance(100)|head_armor(59)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate, [], [fac_kingdom_9] ],
["mt_knight_helm_c", "Knighty Helmet of Tauria", [("helm7",0), ("helm7.1",0)], itp_merchandise|itp_type_head_armor, 0, 999, weight(2.5)|abundance(100)|head_armor(59)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate, [], [fac_kingdom_9] ],

["mt_coat_a", "Coat", [("armor9",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,159 , weight(5)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(9)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_10] ], 

["mt_leather_armor_a", "Light Leather Armor", [("armor15",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0 ,299 , weight(11)|abundance(100)|head_armor(0)|body_armor(13)|leg_armor(9)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_9, fac_kingdom_10] ], 
["mt_leather_armor_b", "Light Leather Armor", [("armor31",0),("armor31.1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,299 , weight(11)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(9)|difficulty(0) ,imodbits_cloth, [], [ fac_kingdom_10] ], 
["mt_leather_armor_c", "Ranger Leather Armor", [("armor8",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,599 , weight(9)|abundance(100)|head_armor(0)|body_armor(32)|leg_armor(12)|difficulty(0) ,imodbits_cloth, [], [ fac_kingdom_10] ], 
["mt_leather_armor_c2", "Ranger Leather Armor", [("armor8_g",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,599 , weight(9)|abundance(100)|head_armor(0)|body_armor(32)|leg_armor(12)|difficulty(0) ,imodbits_cloth, [], [ fac_kingdom_10] ], 
["mt_leather_armor_c3", "Ranger Leather Armor", [("armor8_w",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,599 , weight(9)|abundance(100)|head_armor(0)|body_armor(32)|leg_armor(12)|difficulty(0) ,imodbits_cloth, [], [ fac_kingdom_10] ], 

["mt_special_a", "Leather Armor of Elen", [("armor22",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,299 , weight(9)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(11)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_10] ], 
["mt_special_b", "Mail with Plates of Elen", [("armor21",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1359 , weight(17)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(17)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_10] ], 
["mt_special_c", "Heavy Plates of Elen", [("armor23",0), ("armor23.1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,2399 , weight(21)|abundance(100)|head_armor(0)|body_armor(55)|leg_armor(21)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_10] ], 

["mt_hearldic_a", "Heraldic Mail with Plates", [("armor1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1359 , weight(22)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(17)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_9] ], 
["mt_hearldic_a2", "Heraldic Mail with Plates", [("armor1_b",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1359 , weight(22)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(17)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_9] ], 
["mt_hearldic_b", "Heraldic Mail with Plates", [("armor13",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1359 , weight(22)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(17)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_9] ], 
["mt_hearldic_b2", "Heraldic Mail with Plates", [("armor14",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1359 , weight(22)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(17)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_9] ], 
["mt_hearldic_c", "Heraldic Mail with Plates", [("armor16",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1359 , weight(22)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(17)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_9] ], 
["mt_hearldic_c2", "Heraldic Mail with Plates", [("armor17",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1359 , weight(22)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(17)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_9] ], 
["mt_hearldic_c3", "Heraldic Mail with Plates", [("armor18",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1359 , weight(22)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(17)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_9] ], 
["mt_hearldic_c4", "Padded Mail with Plates", [("armor19",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1359 , weight(22)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(17)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_9] ], 
["mt_hearldic_d", "Heraldic Mail with Plates", [("armor2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1359 , weight(22)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(17)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_9] ], 
["mt_hearldic_d2", "Heraldic Mail with Plates", [("armor3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1359 , weight(22)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(17)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_9] ], 
["mt_hearldic_e", "Heraldic Mail with Plates", [("armor24",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1359 , weight(22)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(17)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_9] ], 
["mt_hearldic_e2", "Heraldic Mail with Plates", [("armor32",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1359 , weight(22)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(17)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_9] ], 
["mt_hearldic_f", "Heraldic Mail with Plates", [("armor33",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1359 , weight(22)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(17)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_9] ], 
["mt_hearldic_g", "Heraldic Mail with Plates", [("armor7",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1359 , weight(22)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(17)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_9] ], 

["mt_mail_tunic_a", "Robe over Mail", [("armor10",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,999 , weight(22)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(15)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_9] ], 
["mt_mail_tunic_a2", "Black Robe over Mail", [("armor10_b",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,999 , weight(22)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(15)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_9] ], 

["mt_heavy_plate_a", "Heavy Plate Armor", [("armor11",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,2599 , weight(27)|abundance(100)|head_armor(0)|body_armor(62)|leg_armor(21)|difficulty(13) ,imodbits_armor, [], [fac_kingdom_7, fac_kingdom_5, fac_kingdom_9] ], 
["mt_heavy_plate_a2", "Ornate Heavy Plate Armor", [("armor12",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,2599 , weight(27)|abundance(100)|head_armor(0)|body_armor(62)|leg_armor(21)|difficulty(13) ,imodbits_armor, [], [fac_kingdom_7, fac_kingdom_5, fac_kingdom_9] ], 
["mt_heavy_plate_b", "Shell Plate", [("armor20",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,3599 , weight(29)|abundance(100)|head_armor(0)|body_armor(66)|leg_armor(23)|difficulty(15) ,imodbits_armor, [], [fac_kingdom_7, fac_kingdom_5, fac_kingdom_9] ], 
["mt_heavy_plate_c", "Footman's Plate Armor", [("armor4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,2599 , weight(27)|abundance(100)|head_armor(0)|body_armor(60)|leg_armor(21)|difficulty(13) ,imodbits_armor, [], [fac_kingdom_7, fac_kingdom_5, fac_kingdom_9] ], 

# ["mt_hose_a", "Woolen Hose", [("boot14",0)], itp_merchandise|itp_type_foot_armor|itp_civilian|itp_attach_armature, 0, 12, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
# ["mt_hose_a2", "Woolen Hose", [("boot14_r",0)], itp_merchandise|itp_type_foot_armor|itp_civilian|itp_attach_armature, 0, 12, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],

["mt_wrapping_a", "Wrapping Boots", [("boot17",0)], itp_merchandise|itp_type_foot_armor|itp_civilian|itp_attach_armature, 0, 99, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(9)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_10] ],
["mt_wrapping_a2", "Wrapping Boots", [("boot18",0)], itp_merchandise|itp_type_foot_armor|itp_civilian|itp_attach_armature, 0, 99, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(9)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_10] ],

["mt_leather_boots_a", "Leather Boots", [("boot13",0)], itp_merchandise|itp_type_foot_armor|itp_civilian|itp_attach_armature,0, 179 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_9, fac_kingdom_10] ],
["mt_leather_boots_b", "Leather Boots", [("boot4",0)], itp_merchandise|itp_type_foot_armor|itp_civilian|itp_attach_armature,0, 179 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_9, fac_kingdom_10] ],
["mt_leather_boots_c", "Leather Boots", [("boot6",0)], itp_merchandise|itp_type_foot_armor|itp_civilian|itp_attach_armature,0, 179 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_9, fac_kingdom_10] ],
["mt_leather_boots_d", "Leather Boots", [("boot7",0)], itp_merchandise|itp_type_foot_armor|itp_civilian|itp_attach_armature,0, 179 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_9, fac_kingdom_10] ],
["mt_leather_boots_e", "Leather Boots", [("boot8",0)], itp_merchandise|itp_type_foot_armor|itp_civilian|itp_attach_armature,0, 179 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_9, fac_kingdom_10] ],

["mt_greaves_light_a", "Splinted Greaves", [("boot11",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature,0, 699 , weight(2)|abundance(15)|head_armor(0)|body_armor(0)|leg_armor(28)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_10] ],
["mt_greaves_light_b", "Splinted Greaves", [("boot9",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature,0, 699 , weight(2)|abundance(15)|head_armor(0)|body_armor(0)|leg_armor(28)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_10] ],

["mt_mail_boots_a", "Mail Chausses", [("boot16",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature,0, 699 , weight(2)|abundance(5)|head_armor(0)|body_armor(0)|leg_armor(28)|difficulty(0) ,imodbits_armor ],

["mt_greaves_a", "Steel Greaves", [("boot1",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature,0, 1099 , weight(2)|abundance(5)|head_armor(0)|body_armor(0)|leg_armor(36)|difficulty(0) ,imodbits_armor ],
["mt_greaves_b", "Steel Greaves", [("boot10",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature,0, 1099 , weight(2)|abundance(5)|head_armor(0)|body_armor(0)|leg_armor(36)|difficulty(0) ,imodbits_armor ],
["mt_greaves_c", "Steel Greaves with Scale", [("boot12",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature,0, 1099 , weight(2)|abundance(5)|head_armor(0)|body_armor(0)|leg_armor(36)|difficulty(0) ,imodbits_armor ],
["mt_greaves_d", "Steel Greaves on Hose", [("boot15",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature,0, 699 , weight(1)|abundance(5)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(0) ,imodbits_armor ],
["mt_greaves_e", "Steel Greaves on Mail", [("boot2",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature,0, 999 , weight(2)|abundance(5)|head_armor(0)|body_armor(0)|leg_armor(32)|difficulty(0) ,imodbits_armor ],
["mt_greaves_f", "Steel Greaves", [("boot3",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature,0, 999 , weight(2)|abundance(5)|head_armor(0)|body_armor(0)|leg_armor(32)|difficulty(0) ,imodbits_armor ],
["mt_greaves_g", "Steel Greaves", [("boot5",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature,0, 999 , weight(2)|abundance(5)|head_armor(0)|body_armor(0)|leg_armor(32)|difficulty(0) ,imodbits_armor ],

["mt_leather_gloves_a","Leather_gloves", [("glove4_L",0)], itp_merchandise|itp_type_hand_armor,0, 299, weight(0.75)|abundance(100)|body_armor(2)|difficulty(0),imodbits_cloth, [], [fac_kingdom_5, fac_kingdom_9, fac_kingdom_10]],

["mt_scale_gloves_a","Scale Gloves", [("glove5_L",0)], itp_merchandise|itp_type_hand_armor,0, 559, weight(0.75)|abundance(100)|body_armor(5)|difficulty(0),imodbits_armor, [], [fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_10]],
["mt_scale_gloves_b","Scale Gloves", [("glove6_L",0)], itp_merchandise|itp_type_hand_armor,0, 559, weight(0.75)|abundance(100)|body_armor(5)|difficulty(0),imodbits_armor, [], [fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_10]],

["mt_gauntlets_a","Plate Gauntlets Gothic", [("glove1_L",0)], itp_merchandise|itp_type_hand_armor,0, 799, weight(0.75)|abundance(100)|body_armor(6)|difficulty(0),imodbits_armor, [], [fac_kingdom_10, fac_kingdom_9]],
["mt_gauntlets_a2","Plate Gauntlets Gothic", [("glove2_L",0)], itp_merchandise|itp_type_hand_armor,0, 799, weight(0.75)|abundance(100)|body_armor(6)|difficulty(0),imodbits_armor, [], [fac_kingdom_10, fac_kingdom_9]],
["mt_gauntlets_b","Mail Gloves", [("glove3_L",0)], itp_merchandise|itp_type_hand_armor,0, 599, weight(0.75)|abundance(100)|body_armor(5)|difficulty(0),imodbits_armor, [], [fac_kingdom_10, fac_kingdom_9]],

["mt_horse_a","Horse with Lamellar", [("horse1",0)], itp_merchandise|itp_type_horse, 0, 1699,abundance(50)|hit_points(165)|body_armor(40)|difficulty(4)|horse_speed(52)|horse_maneuver(50)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_10, fac_kingdom_9]],
["mt_horse_a2","Horse with Scale", [("horse2",0)], itp_merchandise|itp_type_horse, 0, 1699,abundance(50)|hit_points(165)|body_armor(40)|difficulty(4)|horse_speed(52)|horse_maneuver(50)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_10, fac_kingdom_9]],

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

# The Stormguard items

# REMOVE THESE ITEMS FROM THE GAME
["ms_helmet_light", "Mountaineer Helmet", [("helm37",0)], itp_merchandise|itp_type_head_armor, 0, 299, weight(1)|abundance(100)|head_armor(24)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate ],
["ms_helmet_a", "Thunderguard Helmet", [("helm34",0)], itp_merchandise|itp_type_head_armor, 0, 499, weight(2)|abundance(100)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate ],
["ms_helmet_a2", "Thunderguard Helmet", [("helm33",0)], itp_merchandise|itp_type_head_armor, 0, 499, weight(2)|abundance(100)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate ],
["ms_helmet_b", "Stormbringers Helmet", [("helm35",0)], itp_merchandise|itp_type_head_armor, 0, 599, weight(2)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate ],
["ms_helmet_c", "Stormbringers Helmet", [("helm36",0)], itp_merchandise|itp_type_head_armor, 0, 699, weight(2)|abundance(100)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate ],
["ms_helmet_d", "Avalanche Warriors Helmet", [("helm9",0)], itp_merchandise|itp_type_head_armor, 0, 799, weight(2)|abundance(100)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate ],
["ms_helmet_e", "Lightning Riders Helmet", [("helm24",0)], itp_merchandise|itp_type_head_armor, 0, 1299, weight(2)|abundance(100)|head_armor(56)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],

["ms_facemask_a", "Tempest Sentinels Facemask", [("mask_1",0)], itp_merchandise|itp_type_head_armor, 0, 1099, weight(2)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["ms_facemask_b", "Tempest Sentinels Facemask", [("mask_2",0)], itp_merchandise|itp_type_head_armor, 0, 1099, weight(2)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],

["ms_facemask_elite", "Elite Tempest Sentinels Facemask", [("nord_ornate_visored_helmet",0),("nord_ornate_visored_helmet.1",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 2299, weight(2)|abundance(100)|head_armor(60)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate ],

#  Nordic Helmets - Some of them have broken mesh and should be either fixed or removed
["ms_hat_a", "Birka", [("birka_cap",0)], itp_merchandise|itp_type_head_armor, 0, 59, weight(0.2)|abundance(100)|head_armor(3)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_4, fac_kingdom_2] ],

["ms_ridge_helmet_c", "Ridge Helmet With Mail", [("ridge_helmet_mail",0),("ridge_helmet_mail.1",0),("ridge_helmet_mail.2",0),("ridge_helmet_mail.3",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 599, weight(1.5)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], [fac_kingdom_4] ],

["ms_conical_helmet_padded_a", "Conical Helmet with Padded Neckguard", [("english_conical_helmet_padded",0),("english_conical_helmet_padded.1",0),("english_conical_helmet_padded.2",0),("english_conical_helmet_padded.3",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 399, weight(1)|abundance(100)|head_armor(31)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], [fac_kingdom_4] ],

["ms_conical_helmet_mail_a", "Conical Helmet with Mail Neckguard", [("english_conical_helmet_mail",0),("english_conical_helmet_mail.1",0),("english_conical_helmet_mail.2",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 599, weight(2)|abundance(100)|head_armor(37)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], [fac_kingdom_4] ],
["ms_conical_helmet_mail_b", "Conical Helmet with Mail Neckguard", [("english_conical_helmet_veiled",0),("english_conical_helmet_veiled.1",0),("english_conical_helmet_veiled.2",0),("english_conical_helmet_veiled.3",0),("english_conical_helmet_veiled.4",0),("english_conical_helmet_veiled.5",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 659, weight(2)|abundance(100)|head_armor(39)|body_armor(0)|leg_armor(0)|difficulty(5),imodbits_plate, [], [fac_kingdom_4] ],

["ms_gjermundbu_helm_a", "Gjermundbu Helmet", [("gjermundbu_helmet",0),("gjermundbu_helmet.1",0),("gjermundbu_helmet.2",0),("gjermundbu_helmet.3",0),("gjermundbu_helmet.4",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 589, weight(1)|abundance(100)|head_armor(36)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], [fac_kingdom_4] ],
["ms_gjermundbu_helm_b", "Gjermundbu Helmet", [("gjermundbu_helmet_b",0),("gjermundbu_helmet_b.1",0),("gjermundbu_helmet_b.2",0),("gjermundbu_helmet_b.3",0),("gjermundbu_helmet_b.4",0),("gjermundbu_helmet_b.5",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 419, weight(1)|abundance(100)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], [fac_kingdom_4] ],
["ms_gjermundbu_helm_c", "Gjermundbu Helmet", [("gjermundbu_helmet_c",0),("gjermundbu_helmet_c.1",0),("gjermundbu_helmet_c.2",0),("gjermundbu_helmet_c.3",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 699, weight(1)|abundance(100)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], [fac_kingdom_4] ],

["ms_pointed_helmet_a", "Pointed Helmet", [("viking_pointed_helmet",0),("viking_pointed_helmet.1",0),("viking_pointed_helmet.2",0),("viking_pointed_helmet.3",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 499, weight(2)|abundance(100)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], [fac_kingdom_4] ],

["ms_spangen_helmet_a", "Decorated Spangen Helmet with Mail", [("vikingr_spangen_helmet_decorated_mail",0),("vikingr_spangen_helmet_decorated_mail.1",0),("vikingr_spangen_helmet_decorated_mail.2",0),("vikingr_spangen_helmet_decorated_mail.3",0),("vikingr_spangen_helmet_decorated_mail.4",0),("vikingr_spangen_helmet_decorated_mail.5",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 559, weight(2.3)|abundance(100)|head_armor(39)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], [fac_kingdom_4] ],
["ms_spangen_helmet_b", "Spangen Helmet with Mail", [("vikingr_spangen_helmet_mail",0),("vikingr_spangen_helmet_mail.1",0),("vikingr_spangen_helmet_mail.2",0),("vikingr_spangen_helmet_mail.3",0),("vikingr_spangen_helmet_mail.4",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 519, weight(2.3)|abundance(100)|head_armor(39)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], [fac_kingdom_4] ],
["ms_spangen_helmet_c", "Padded Spangen Helmet", [("vikingr_spangen_helmet_padded",0),("vikingr_spangen_helmet_padded.1",0),("vikingr_spangen_helmet_padded.2",0),("vikingr_spangen_helmet_padded.3",0),("vikingr_spangen_helmet_padded.4",0),("vikingr_spangen_helmet_padded.5",0)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 499, weight(1.3)|abundance(100)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], [fac_kingdom_4] ],

["ms_gambeson_a", "Light Gambeson", [("light_gambeson_a",0)], itp_merchandise|itp_type_body_armor, 0, 499, weight(15)|abundance(100)|head_armor(0)|body_armor(24)|leg_armor(8)|difficulty(5) ,imodbits_cloth, [], [fac_kingdom_12] ],
["ms_gambeson_b", "Light Gambeson", [("light_gambeson_b",0)], itp_merchandise|itp_type_body_armor, 0, 499, weight(15)|abundance(100)|head_armor(0)|body_armor(24)|leg_armor(8)|difficulty(5) ,imodbits_cloth, [], [fac_kingdom_12] ],
["ms_gambeson_c", "Light Gambeson", [("light_gambeson_c",0)], itp_merchandise|itp_type_body_armor, 0, 499, weight(15)|abundance(100)|head_armor(0)|body_armor(24)|leg_armor(8)|difficulty(5) ,imodbits_cloth, [], [fac_kingdom_12] ],

["ms_byrnie_a", "Stormguard Byrnie", [("english_byrne",0)], itp_merchandise|itp_type_body_armor, 0, 899, weight(20)|abundance(100)|head_armor(0)|body_armor(36)|leg_armor(13)|difficulty(5) ,imodbits_plate, [], [fac_kingdom_12] ],
["ms_byrnie_a_light", "Stormguard Battle Byrnie", [("english_byrne_light_a",0),("english_byrne_light_a.1",0),("english_byrne_light_a.2",0),("english_byrne_light_a.3",0)], itp_merchandise|itp_type_body_armor, 0, 2399, weight(22)|abundance(100)|head_armor(0)|body_armor(41)|leg_armor(18)|difficulty(10) ,imodbits_plate, [], [fac_kingdom_12] ],
["ms_byrnie_a_plated", "Stormguard Plated Byrnie", [("english_byrne_knee_a",0),("english_byrne_knee_a.1",0),("english_byrne_knee_a.2",0)], itp_merchandise|itp_type_body_armor, 0, 2399, weight(24)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(18)|difficulty(10) ,imodbits_plate, [], [fac_kingdom_12] ],
["ms_byrnie_a_plated_mail", "Stormguard Plated Byrnie with Mail", [("english_byrne_knee_b",0),("english_byrne_knee_b.1",0),("english_byrne_knee_b.2",0)], itp_merchandise|itp_type_body_armor, 0, 2469, weight(24)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(18)|difficulty(11) ,imodbits_plate, [], [fac_kingdom_12] ],
["ms_byrnie_a_plated_mail_pelt", "Stormguard Plated Byrnie with Pelt", [("english_byrne_knee_c",0),("english_byrne_knee_c.1",0),("english_byrne_knee_c.2",0),("english_byrne_knee_c.3",0)], itp_merchandise|itp_type_body_armor, 0, 2469, weight(24)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(18)|difficulty(11) ,imodbits_plate, [], [fac_kingdom_12] ],
["ms_byrnie_a_plated_mail_fur", "Stormguard Plated Byrnie with Fur", [("english_byrne_knee_d",0),("english_byrne_knee_d.1",0),("english_byrne_knee_d.2",0),("english_byrne_knee_d.3",0)], itp_merchandise|itp_type_body_armor, 0, 2469, weight(24)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(18)|difficulty(11) ,imodbits_plate, [], [fac_kingdom_12] ],

["ms_byrnie_b", "Byrnie", [("viking_byrnie_b",0), ("viking_byrnie_b.1",0)], itp_merchandise|itp_type_body_armor, 0, 899, weight(20)|abundance(100)|head_armor(0)|body_armor(36)|leg_armor(13)|difficulty(5) ,imodbits_plate, [], [fac_kingdom_12] ],
["ms_byrnie_c", "Byrnie", [("viking_byrnie_c",0)], itp_merchandise|itp_type_body_armor, 0, 899, weight(20)|abundance(100)|head_armor(0)|body_armor(36)|leg_armor(13)|difficulty(5) ,imodbits_plate, [], [fac_kingdom_12] ],
["ms_byrnie_d", "Byrnie", [("viking_byrnie_new",0)], itp_merchandise|itp_type_body_armor, 0, 899, weight(20)|abundance(100)|head_armor(0)|body_armor(36)|leg_armor(13)|difficulty(5) ,imodbits_plate, [], [fac_kingdom_12] ],

["ms_byrnie_d_plated", "Stormguard Plated Byrnie", [("viking_byrnie_knee_a",0),("viking_byrnie_knee_a.1",0),("viking_byrnie_knee_a.2",0)], itp_merchandise|itp_type_body_armor, 0, 2181, weight(23)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(18)|difficulty(5) ,imodbits_plate, [], [fac_kingdom_12] ],
["ms_byrnie_d_plated_cloak", "Stormguard Plated Byrnie with Cloak", [("viking_byrnie_knee_b",0),("viking_byrnie_knee_b.1",0),("viking_byrnie_knee_b.2",0),("viking_byrnie_knee_b.3",0)], itp_merchandise|itp_type_body_armor, 0, 2181, weight(23)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(18)|difficulty(5) ,imodbits_plate, [], [fac_kingdom_12] ],
["ms_byrnie_d_plated_bevor", "Stormguard Plated Byrnie with Bevor", [("viking_byrnie_knee_c",0),("viking_byrnie_knee_c.1",0),("viking_byrnie_knee_c.2",0),("viking_byrnie_knee_c.3",0)], itp_merchandise|itp_type_body_armor, 0, 2399, weight(23)|abundance(100)|head_armor(3)|body_armor(45)|leg_armor(18)|difficulty(5) ,imodbits_plate, [], [fac_kingdom_12] ],
["ms_byrnie_d_plated_bevor_fur", "Stormguard Plated Byrnie with Fur", [("viking_byrnie_knee_d",0),("viking_byrnie_knee_d.1",0),("viking_byrnie_knee_d.2",0),("viking_byrnie_knee_d.3",0),("viking_byrnie_knee_d.4",0)], itp_merchandise|itp_type_body_armor, 0, 2399, weight(23)|abundance(100)|head_armor(3)|body_armor(45)|leg_armor(18)|difficulty(5) ,imodbits_plate, [], [fac_kingdom_12] ],

["ms_byrnie_d_heavy", "Stormguard Heavy Armor", [("viking_byrnie_heavy_a",0),("viking_byrnie_heavy_a.1",0),("viking_byrnie_heavy_a.2",0),("viking_byrnie_heavy_a.3",0),("viking_byrnie_heavy_a.4",0),("viking_byrnie_heavy_a.5",0)], itp_merchandise|itp_type_body_armor, 0, 3869, weight(26)|abundance(100)|head_armor(5)|body_armor(52)|leg_armor(26)|difficulty(12) ,imodbits_plate, [], [fac_kingdom_12] ],
["ms_byrnie_d_heavy_plate", "Stormguard Heavy Plate Armor", [("viking_byrnie_heavy_b",0),("viking_byrnie_heavy_b.1",0),("viking_byrnie_heavy_b.2",0),("viking_byrnie_heavy_b.3",0),("viking_byrnie_heavy_b.4",0),("viking_byrnie_heavy_b.5",0),("viking_byrnie_heavy_b.6",0)], itp_merchandise|itp_type_body_armor, 0, 4399, weight(27)|abundance(100)|head_armor(5)|body_armor(59)|leg_armor(26)|difficulty(12) ,imodbits_plate, [], [fac_kingdom_12] ],

["ms_mail_shirt_a", "Mail Shirt", [("mail_shirt_viking",0)], itp_merchandise|itp_type_body_armor, 0, 1299, weight(23)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(22)|difficulty(5) ,imodbits_plate, [], [fac_kingdom_12] ],
["ms_mail_shirt_b", "Mail Shirt", [("mail_shirt_viking_blue",0)], itp_merchandise|itp_type_body_armor, 0, 1299, weight(23)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(22)|difficulty(5) ,imodbits_plate, [], [fac_kingdom_12] ],
["ms_mail_shirt_c", "Mail Shirt", [("mail_shirt_viking_green",0)], itp_merchandise|itp_type_body_armor, 0, 1299, weight(23)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(22)|difficulty(5) ,imodbits_plate, [], [fac_kingdom_12] ],

["ms_mail_shirt_heavy_a", "Stormguard Heavy Mail Shirt with Fur", [("mail_shirt_heavy_a",0),("mail_shirt_heavy_a.1",0),("mail_shirt_heavy_a.2",0),("mail_shirt_heavy_a.3",0),("mail_shirt_heavy_a.4",0),("mail_shirt_heavy_a.5",0),("mail_shirt_heavy_a.6",0)], itp_merchandise|itp_type_body_armor, 0, 4799, weight(25)|abundance(100)|head_armor(5)|body_armor(55)|leg_armor(30)|difficulty(5) ,imodbits_plate, [], [fac_kingdom_12] ],
["ms_mail_shirt_heavy_b", "Stormguard Heavy Mail Shirt", [("mail_shirt_heavy_b",0),("mail_shirt_heavy_b.1",0),("mail_shirt_heavy_b.2",0),("mail_shirt_heavy_b.3",0),("mail_shirt_heavy_b.4",0),("mail_shirt_heavy_b.5",0),("mail_shirt_heavy_b.6",0)], itp_merchandise|itp_type_body_armor, 0, 4699, weight(25)|abundance(100)|head_armor(5)|body_armor(55)|leg_armor(30)|difficulty(5) ,imodbits_plate, [], [fac_kingdom_12] ],
["ms_mail_shirt_heavy_c", "Stormguard Heavy Mail Shirt with Cloak", [("mail_shirt_heavy_c",0),("mail_shirt_heavy_c.1",0),("mail_shirt_heavy_c.2",0),("mail_shirt_heavy_c.3",0),("mail_shirt_heavy_c.4",0),("mail_shirt_heavy_c.5",0),("mail_shirt_heavy_c.6",0)], itp_merchandise|itp_type_body_armor, 0, 4419, weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(30)|difficulty(5) ,imodbits_plate, [], [fac_kingdom_12] ],
["ms_mail_shirt_heavy_d", "Stormguard Heavy Mail Shirt with Cloak", [("mail_shirt_heavy_d",0),("mail_shirt_heavy_d.1",0),("mail_shirt_heavy_d.2",0),("mail_shirt_heavy_d.3",0),("mail_shirt_heavy_d.4",0),("mail_shirt_heavy_d.5",0),("mail_shirt_heavy_d.6",0),("mail_shirt_heavy_d.7",0)], itp_merchandise|itp_type_body_armor, 0, 5699, weight(28)|abundance(100)|head_armor(0)|body_armor(61)|leg_armor(30)|difficulty(15) ,imodbits_plate, [], [fac_kingdom_12] ],
["ms_mail_shirt_heavy_e", "Stormguard Heavy Mail Shirt with Cloak", [("mail_shirt_heavy_e",0),("mail_shirt_heavy_e.1",0),("mail_shirt_heavy_e.2",0),("mail_shirt_heavy_e.3",0),("mail_shirt_heavy_e.4",0),("mail_shirt_heavy_e.5",0),("mail_shirt_heavy_e.6",0),("mail_shirt_heavy_e.7",0)], itp_merchandise|itp_type_body_armor, 0, 5899, weight(28)|abundance(100)|head_armor(6)|body_armor(61)|leg_armor(30)|difficulty(15) ,imodbits_plate, [], [fac_kingdom_12] ],

["ms_short_hauberk_a", "Short Hauberk", [("norman_short_hauberk",0)], itp_merchandise|itp_type_body_armor, 0, 1299, weight(22)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(11)|difficulty(5) ,imodbits_plate, [], [fac_kingdom_12] ],
["ms_short_hauberk_b", "Short Hauberk", [("norman_short_hauberk_blue",0)], itp_merchandise|itp_type_body_armor, 0, 1299, weight(22)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(11)|difficulty(5) ,imodbits_plate, [], [fac_kingdom_12] ],
["ms_short_hauberk_c", "Short Hauberk", [("norman_short_hauberk_yellow",0)], itp_merchandise|itp_type_body_armor, 0, 1299, weight(22)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(11)|difficulty(5) ,imodbits_plate, [], [fac_kingdom_12] ],

["ms_stormbringer_hauberk_a", "Hauberk", [("saxon_hauberk_a",0)], itp_merchandise|itp_type_body_armor, 0, 1599, weight(25)|abundance(100)|head_armor(0)|body_armor(36)|leg_armor(16)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_12] ],
["ms_stormbringer_hauberk_b", "Hauberk", [("saxon_hauberk_b",0)], itp_merchandise|itp_type_body_armor, 0, 1599, weight(25)|abundance(100)|head_armor(0)|body_armor(36)|leg_armor(16)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_12] ],
["ms_stormbringer_hauberk_c", "Hauberk", [("saxon_hauberk_c",0)], itp_merchandise|itp_type_body_armor, 0, 1599, weight(25)|abundance(100)|head_armor(0)|body_armor(36)|leg_armor(16)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_12] ],

["ms_huscarl_armor_a", "Huscarl Armor", [("huscarl_armour",0)], itp_merchandise|itp_type_body_armor, 0, 6791, weight(30)|abundance(1)|head_armor(0)|body_armor(56)|leg_armor(28)|difficulty(12) ,imodbits_plate, [], [fac_kingdom_4] ],

["ms_coat_of_plates_a", "Coat of Plates", [("nord_coat_of_plates",0)], itp_merchandise|itp_type_body_armor, 0, 8999, weight(30)|abundance(1)|head_armor(0)|body_armor(60)|leg_armor(25)|difficulty(12) ,imodbits_plate, [], [fac_kingdom_4, fac_kingdom_2, fac_kingdom_12] ],
["ms_coat_of_plates_b", "Coat of Plates", [("nord_coat_of_plates_pelt",0),("nord_coat_of_plates_pelt.1",0)], itp_merchandise|itp_type_body_armor, 0, 8999, weight(30)|abundance(1)|head_armor(0)|body_armor(60)|leg_armor(25)|difficulty(12) ,imodbits_plate, [], [fac_kingdom_4, fac_kingdom_2, fac_kingdom_12] ],

["ms_greaves_a", "Nordic Splinted Greaves", [("nord_splinted_greaves",0)], itp_merchandise|itp_type_foot_armor, 0, 2099, weight(2)|abundance(1)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(12) ,imodbits_cloth, [], [fac_kingdom_4, fac_kingdom_2, fac_kingdom_12] ],

["nord_lamellar_a", "Light Lamellar Vest", [("leather_lamellar_blk_small",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 592, weight(15)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_4] ],
["nord_lamellar_b", "Light Lamellar Vest with Decoration", [("nord_a",0),("nord_a.1",0),("nord_a.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 599, weight(16)|abundance(100)|head_armor(0)|body_armor(32)|leg_armor(5)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_4] ],
["nord_lamellar_c", "Light Lamellar Vest with Decoration", [("nord_b",0),("nord_b.1",0),("nord_b.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 599, weight(16)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(5)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_4] ],

["nord_light_a", "Light Nordic Armor", [("nord_light_a",0),("nord_light_a.1",0),("nord_light_a.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 993, weight(18)|abundance(100)|head_armor(0)|body_armor(26)|leg_armor(14)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_4] ],
["nord_light_b", "Light Nordic Armor with Mail", [("nord_light_b",0),("nord_light_b.1",0),("nord_light_b.2",0),("nord_light_b.3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 1344, weight(20)|abundance(100)|head_armor(0)|body_armor(33)|leg_armor(14)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_4] ],
["nord_light_c", "Light Nordic Armor with Mail", [("nord_light_c",0),("nord_light_c.1",0),("nord_light_c.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 1344, weight(20)|abundance(100)|head_armor(0)|body_armor(33)|leg_armor(14)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_4] ],

["nord_padded_a", "Padded Armor", [("nord_padd_a",0),("nord_padd_a.1",0),("nord_padd_a.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 1642, weight(20)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(19)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_4] ],
["nord_padded_b", "Padded Armor", [("nord_padd_b",0),("nord_padd_b.1",0),("nord_padd_b.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 1983, weight(21)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(19)|difficulty(11) ,imodbits_plate, [], [fac_kingdom_4] ],
["nord_padded_c", "Padded Armor with Decorations", [("nord_padd_c",0),("nord_padd_c.1",0),("nord_padd_c.2",0),("nord_padd_c.3",0),("nord_padd_c.4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 1699, weight(20)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(19)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_4] ],
["nord_padded_d", "Padded Armor with Bag", [("nord_padd_d",0),("nord_padd_d.1",0),("nord_padd_d.2",0),("nord_padd_d.3",0),("nord_padd_d.4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 1983, weight(21)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(19)|difficulty(11) ,imodbits_plate, [], [fac_kingdom_4] ],
["nord_padded_lam_a", "Padded Armor with Lamellar Vest", [("nord_padd_lam_a",0),("nord_padd_lam_a.1",0),("nord_padd_lam_a.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 1769, weight(21)|abundance(100)|head_armor(0)|body_armor(41)|leg_armor(19)|difficulty(10) ,imodbits_plate, [], [fac_kingdom_4] ],

["nord_archer_a", "Padded Armor with Hood", [("nord_tracer_a",0),("nord_tracer_a.1",0),("nord_tracer_a.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 1599, weight(18)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(19)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_4] ],
["nord_archer_b", "Padded Armor with Hood on Mail", [("nord_tracer_b",0),("nord_tracer_b.1",0),("nord_tracer_b.2",0),("nord_tracer_b.3",0),("nord_tracer_b.4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 1899, weight(20)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(19)|difficulty(10) ,imodbits_plate, [], [fac_kingdom_4] ],
["nord_archer_c", "Padded Armor with Hood", [("nord_tracer_c",0),("nord_tracer_c.1",0),("nord_tracer_c.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 1799, weight(19)|abundance(100)|head_armor(0)|body_armor(41)|leg_armor(19)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_4] ],

["nord_mail_a", "Nordic Mail Shirt", [("nord_mail_a",0),("nord_mail_a.1",0),("nord_mail_a.2",0),("nord_mail_a.3",0),("nord_mail_a.4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 3581, weight(25)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(19)|difficulty(11) ,imodbits_plate, [], [fac_kingdom_4] ],
["nord_mail_b", "Nordic Mail Shirt", [("nord_mail_b",0),("nord_mail_b.1",0),("nord_mail_b.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 3681, weight(25)|abundance(100)|head_armor(0)|body_armor(47)|leg_armor(19)|difficulty(11) ,imodbits_plate, [], [fac_kingdom_4] ],
["nord_mail_c", "Nordic Mail Shirt", [("nord_mail_c",0),("nord_mail_c.1",0),("nord_mail_c.2",0),("nord_mail_c.3",0),("nord_mail_c.4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 3681, weight(25)|abundance(100)|head_armor(0)|body_armor(47)|leg_armor(19)|difficulty(11) ,imodbits_plate, [], [fac_kingdom_4] ],

["nord_plate_a", "Nordic Light Plate", [("nord_plate_a",0),("nord_plate_a.1",0),("nord_plate_a.2",0),("nord_plate_a.3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 3981, weight(25)|abundance(100)|head_armor(2)|body_armor(49)|leg_armor(19)|difficulty(12) ,imodbits_plate, [], [fac_kingdom_4] ],
["nord_plate_b", "Nordic Light Plate", [("nord_plate_b",0),("nord_plate_b.1",0),("nord_plate_b.2",0),("nord_plate_b.3",0),("nord_plate_b.4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 4139, weight(25)|abundance(100)|head_armor(2)|body_armor(51)|leg_armor(19)|difficulty(13) ,imodbits_plate, [], [fac_kingdom_4] ],

# New nordic weapons
["nordic_hand_axe_a", "Hand Axe", [("axe_e",0),("axe_e.1",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 399 , weight(2)|difficulty(7)|spd_rtng(99) | weapon_length(65)|swing_damage(29 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_kingdom_4] ],
["nordic_hand_axe_b", "Hand Axe", [("axe_f",0),("axe_f.1",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 399 , weight(2)|difficulty(7)|spd_rtng(99) | weapon_length(65)|swing_damage(29 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_kingdom_4] ],
["nordic_hand_axe_c", "Hand Axe", [("heavy_cutting_axe",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 399 , weight(2)|difficulty(7)|spd_rtng(99) | weapon_length(65)|swing_damage(29 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_kingdom_4] ],
["nordic_hand_axe_d", "Slim Hand Axe", [("slim_axe",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 569 , weight(2)|difficulty(9)|spd_rtng(99) | weapon_length(75)|swing_damage(35 , cut) | thrust_damage(0 ,  pierce),imodbits_axe, [], [fac_kingdom_4] ],

["nordic_spear_a", "Hewing Spear", [("hewing_spear",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry,itc_staff|itcf_carry_spear, 619 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(165)|swing_damage(31 , cut) | thrust_damage(26 ,  pierce),imodbits_polearm, [], [fac_kingdom_4] ],

["nord_sword_a", "Nordic Sword", [("london1_sword",0),("london1_sword.1",0),("london1_sword.2",0),("london1_sword_scab", ixmesh_carry),("london1_sword_scab.1", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 299 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(80)|swing_damage(29 , cut) | thrust_damage(25 ,  pierce),imodbits_sword_high, [], [fac_kingdom_4] ],
["nord_sword_b", "Nordic Sword", [("london_sword_2",0),("london_sword_2_scab", ixmesh_carry),("london_sword_2_scab.1", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 399 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(90)|swing_damage(29 , cut) | thrust_damage(25 ,  pierce),imodbits_sword_high, [], [fac_kingdom_4] ],
["nord_sword_c", "Nordic Sword", [("norman_short_sword",0),("norman_short_sword_scab", ixmesh_carry),("norman_short_sword_scab.1", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 399 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(90)|swing_damage(29 , cut) | thrust_damage(25 ,  pierce),imodbits_sword_high, [], [fac_kingdom_4] ],
["nord_sword_d", "Nordic Sword", [("short_rus_sword",0),("scab_short_rus_sword", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 399 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(90)|swing_damage(29 , cut) | thrust_damage(25 ,  pierce),imodbits_sword_high, [], [fac_kingdom_4] ],

# ["saex_a", "Seax", [("gaelic_seax",0),("gaelic_seax_scab",ixmesh_carry),("gaelic_seax_scab.1",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary, itc_dagger|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 379 , weight(0.75)|difficulty(0)|spd_rtng(109) | weapon_length(70)|swing_damage(28 , cut) | thrust_damage(26 ,  pierce),imodbits_sword_high ],
# ["saex_b", "Seax", [("heavy_seax",0),("heavy_seax_scab",ixmesh_carry),("heavy_seax_scab.1",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary, itc_dagger|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 379 , weight(0.75)|difficulty(0)|spd_rtng(109) | weapon_length(70)|swing_damage(28 , cut) | thrust_damage(26 ,  pierce),imodbits_sword_high ],
# ["saex_c", "Seax", [("norman_seax",0),("norman_seax_scab",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary, itc_dagger|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 379 , weight(0.75)|difficulty(0)|spd_rtng(109) | weapon_length(70)|swing_damage(28 , cut) | thrust_damage(26 ,  pierce),imodbits_sword_high ],

# black horde items
["mh_helmet_heavy_a", "Heavy Hairako Helmet", [("mask_helmet1",0), ("mask_helmet1.1",0)], itp_merchandise|itp_type_head_armor, 0, 899, weight(2)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_8] ],

["mh_helmet_a", "Hairako War Helmet", [("mongol_helmet_x",0), ("mongol_helmet_x.1",0), ("mongol_helmet_x.2", 0)], itp_merchandise|itp_type_head_armor, 0, 359, weight(1)|abundance(100)|head_armor(36)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_8] ],
["mh_helmet_b", "Hairako War Helmet", [("mongol_helmet_x1",0), ("mongol_helmet_x1.1",0), ("mongol_helmet_x1.2", 0), ("mongol_helmet_x1.3", 0)], itp_merchandise|itp_type_head_armor, 0, 359, weight(1)|abundance(100)|head_armor(37)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_8] ],
["mh_helmet_c", "Hairako War Helmet", [("mongol_helmet_xa",0), ("mongol_helmet_xa.1",0), ("mongol_helmet_xa.2", 0), ("mongol_helmet_xa.3", 0)], itp_merchandise|itp_type_head_armor, 0, 359, weight(1)|abundance(100)|head_armor(37)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_8] ],
["mh_helmet_d", "Hairako War Helmet", [("mongol_helmet_xa1",0), ("mongol_helmet_xa1.1",0), ("mongol_helmet_xa1.2", 0), ("mongol_helmet_xa1.3", 0), ("mongol_helmet_xa1.4", 0)], itp_merchandise|itp_type_head_armor, 0, 359, weight(1)|abundance(100)|head_armor(37)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_8] ],
["mh_helmet_e", "Hairako War Helmet", [("mongol_helmet_xb",0), ("mongol_helmet_xb.1",0), ("mongol_helmet_xb.2", 0), ("mongol_helmet_xb.3", 0)], itp_merchandise|itp_type_head_armor, 0, 359, weight(1)|abundance(100)|head_armor(37)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_8] ],
["mh_helmet_f", "Hairako War Helmet", [("mongol_helmet_xe",0), ("mongol_helmet_xe.1",0), ("mongol_helmet_xe.2", 0), ("mongol_helmet_xe.3", 0), ("mongol_helmet_xe.4", 0), ("mongol_helmet_xe.5", 0)], itp_merchandise|itp_type_head_armor, 0, 359, weight(1)|abundance(100)|head_armor(37)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_8] ],
["mh_helmet_g", "Hairako War Helmet", [("mongol_helmet_xg",0), ("mongol_helmet_xg.1",0), ("mongol_helmet_xg.2", 0), ("mongol_helmet_xg.3", 0), ("mongol_helmet_xg.4", 0), ("mongol_helmet_xg.5", 0), ("mongol_helmet_xg.6", 0)], itp_merchandise|itp_type_head_armor, 0, 359, weight(1)|abundance(100)|head_armor(37)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_8] ],
["mh_helmet_j", "Hairako War Helmet", [("mongol_helmet_xg1",0), ("mongol_helmet_xg1.1",0), ("mongol_helmet_xg1.2", 0), ("mongol_helmet_xg1.3", 0), ("mongol_helmet_xg1.4", 0), ("mongol_helmet_xg1.5", 0)], itp_merchandise|itp_type_head_armor, 0, 359, weight(1)|abundance(100)|head_armor(37)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_8] ],
["mh_helmet_k", "Hairako War Helmet", [("mongol_helmet_xg2",0), ("mongol_helmet_xg2.1",0), ("mongol_helmet_xg2.2", 0), ("mongol_helmet_xg2.3", 0), ("mongol_helmet_xg2.4", 0), ("mongol_helmet_xg2.5", 0)], itp_merchandise|itp_type_head_armor, 0, 359, weight(1)|abundance(100)|head_armor(37)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_8] ],
["mh_helmet_l", "Hairako War Helmet", [("mongol_helmet_xh",0), ("mongol_helmet_xh.1",0), ("mongol_helmet_xh.2", 0), ("mongol_helmet_xh.3", 0), ("mongol_helmet_xh.4", 0), ("mongol_helmet_xh.5", 0)], itp_merchandise|itp_type_head_armor, 0, 359, weight(1)|abundance(100)|head_armor(37)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_8] ],
["mh_helmet_m", "Hairako War Helmet", [("mongol_helmet_xh1",0), ("mongol_helmet_xh1.1",0), ("mongol_helmet_xh1.2", 0), ("mongol_helmet_xh1.3", 0), ("mongol_helmet_xh1.4", 0), ("mongol_helmet_xh1.5", 0)], itp_merchandise|itp_type_head_armor, 0, 359, weight(1)|abundance(100)|head_armor(37)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_8] ],
["mh_helmet_n", "Hairako War Helmet", [("mongol_helmet_xi",0), ("mongol_helmet_xi.1",0), ("mongol_helmet_xi.2", 0), ("mongol_helmet_xi.3", 0), ("mongol_helmet_xi.4", 0)], itp_merchandise|itp_type_head_armor, 0, 359, weight(1)|abundance(100)|head_armor(37)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_8] ],

["mh_helmet_light_a", "Hairako Fur Hat", [("mongol_helmet_xc",0), ("mongol_helmet_xc.1",0), ("mongol_helmet_xc.2", 0), ("mongol_helmet_xc.3", 0)], itp_merchandise|itp_type_head_armor, 0, 299, weight(1)|abundance(100)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_8] ],

["mh_helmet_medium_a", "Hairako Helmet with Mail", [("mongol_helmet_xd",0), ("mongol_helmet_xd.1",0), ("mongol_helmet_xd.2", 0), ("mongol_helmet_xd.3", 0), ("mongol_helmet_xd.4", 0), ("mongol_helmet_xd.5", 0)], itp_merchandise|itp_type_head_armor, 0, 559, weight(1.7)|abundance(100)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_8] ],
["mh_helmet_medium_b", "Hairako Helmet with Mail", [("mongol_helmet_xf",0), ("mongol_helmet_xf.1",0), ("mongol_helmet_xf.2", 0), ("mongol_helmet_xf.3", 0), ("mongol_helmet_xf.4", 0)], itp_merchandise|itp_type_head_armor, 0, 559, weight(1.7)|abundance(100)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_8] ],

["mh_armor_cuirass_a", "Horde Heavy Leather Cuirass", [("mongol_armor_xy",0), ("mongol_armor_xy.1",0), ("mongol_armor_xy.2",0), ("mongol_armor_xy.3",0), ("mongol_armor_xy.4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,899 , weight(16)|abundance(100)|head_armor(0)|body_armor(28)|leg_armor(11)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_8] ],

["mh_armor_leather_a", "Horde Light Leather", [("mongol_armor_xxc",0), ("mongol_armor_xxc.2",0), ("mongol_armor_xxc.3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,699 , weight(13)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(11)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_8] ], 
["mh_armor_leather_b", "Horde Light Leather", [("mongol_armor_xxc_1",0), ("mongol_armor_xxc_1.2",0), ("mongol_armor_xxc_1.3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,699 , weight(13)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(11)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_8] ], 
["mh_armor_leather_c", "Horde Light Leather", [("mongol_armor_xxc_2",0), ("mongol_armor_xxc_2.2",0), ("mongol_armor_xxc_2.3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,699 , weight(13)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(11)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_8] ], 

["mh_armor_chest_a", "Horde Lamellar Cuirass", [("mongol_armor_xxd",0), ("mongol_armor_xxd.2",0), ("mongol_armor_xxd.3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,799 , weight(15)|abundance(100)|head_armor(0)|body_armor(32)|leg_armor(11)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_8] ], 
["mh_armor_chest_b", "Horde Lamellar Cuirass", [("mongol_armor_xxd_1",0), ("mongol_armor_xxd_1.2",0), ("mongol_armor_xxd_1.3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,799 , weight(15)|abundance(100)|head_armor(0)|body_armor(32)|leg_armor(11)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_8] ], 
["mh_armor_chest_c", "Horde Lamellar Cuirass", [("mongol_armor_xxd_2",0), ("mongol_armor_xxd_2.2",0), ("mongol_armor_xxd_2.3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,799 , weight(15)|abundance(100)|head_armor(0)|body_armor(32)|leg_armor(11)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_8] ], 

["mh_armor_lamellar_a", "Horde Lamellar Armor", [("mongol_armor_xx",0), ("mongol_armor_xx.2",0), ("mongol_armor_xx.3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,999 , weight(16)|abundance(100)|head_armor(0)|body_armor(36)|leg_armor(14)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_8] ], 
["mh_armor_lamellar_b", "Horde Lamellar Armor", [("mongol_armor_xxa",0), ("mongol_armor_xxa.2",0), ("mongol_armor_xxa.3",0), ("mongol_armor_xxa.4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,999 , weight(16)|abundance(100)|head_armor(0)|body_armor(36)|leg_armor(14)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_8] ], 
["mh_armor_lamellar_c", "Horde Lamellar Armor", [("mongol_armor_xxb",0), ("mongol_armor_xxb.2",0), ("mongol_armor_xxb.3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,999 , weight(16)|abundance(100)|head_armor(0)|body_armor(36)|leg_armor(14)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_8] ], 

["mh_armor_heavy_a", "Horde Heavy Armor", [("mongol_armor_heavy",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1599 , weight(20)|abundance(100)|head_armor(0)|body_armor(53)|leg_armor(18)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_8] ], 

["mh_armor_mail_a", "Horde Mail Armor", [("mongol_mail",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1259 , weight(19)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(12)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_8] ], 
["mh_armor_mail_b", "Horde Mail with Fur", [("mongol_mail_2",0), ("mongol_mail_2.1",0), ("mongol_mail_2.2",0), ("mongol_mail_2.3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1259 , weight(19)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(12)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_8] ], 
["mh_armor_mail_c", "Horde Mail with Fur", [("mongol_mail_2a",0), ("mongol_mail_2a.1",0), ("mongol_mail_2a.2",0), ("mongol_mail_2a.3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1259 , weight(19)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(12)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_8] ], 

["mh_horse_a","Horde War Horse", [("mongol_horse_heavy_x",0), ("mongol_horse_heavy_x.1",0), ("mongol_horse_heavy_x.2",0), ("mongol_horse_heavy_x.3",0), ("mongol_horse_heavy_x.4",0), ("mongol_horse_heavy_x.5",0), ("mongol_horse_heavy_x.6",0)], itp_merchandise|itp_type_horse, 0, 1699,abundance(50)|hit_points(165)|body_armor(40)|difficulty(4)|horse_speed(52)|horse_maneuver(50)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_8]],
["mh_horse_b","Horde War Horse", [("mongol_horse_heavy_xa",0), ("mongol_horse_heavy_xa.1",0), ("mongol_horse_heavy_xa.2",0), ("mongol_horse_heavy_xa.3",0), ("mongol_horse_heavy_xa.4",0), ("mongol_horse_heavy_xa.5",0), ("mongol_horse_heavy_xa.6",0)], itp_merchandise|itp_type_horse, 0, 1699,abundance(50)|hit_points(165)|body_armor(40)|difficulty(4)|horse_speed(52)|horse_maneuver(50)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_8]],
["mh_horse_c","Horde War Horse", [("mongol_horse_heavy_xb",0), ("mongol_horse_heavy_xb.1",0), ("mongol_horse_heavy_xb.2",0), ("mongol_horse_heavy_xb.3",0), ("mongol_horse_heavy_xb.4",0), ("mongol_horse_heavy_xb.5",0), ("mongol_horse_heavy_xb.6",0)], itp_merchandise|itp_type_horse, 0, 1699,abundance(50)|hit_points(165)|body_armor(40)|difficulty(4)|horse_speed(52)|horse_maneuver(50)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_8]],
["mh_horse_d","Horde War Horse", [("mongol_horse_armored",0), ("mongol_horse_armored.1",0), ("mongol_horse_armored.2",0), ("mongol_horse_armored.3",0), ("mongol_horse_armored.4",0), ("mongol_horse_armored.5",0), ("mongol_horse_armored.6",0)], itp_merchandise|itp_type_horse, 0, 1699,abundance(50)|hit_points(165)|body_armor(40)|difficulty(4)|horse_speed(52)|horse_maneuver(50)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_8]],
["mh_horse_e","Horde War Horse", [("mongol_elite_warhorse",0), ("mongol_elite_warhorse.1",0), ("mongol_elite_warhorse.2",0), ("mongol_elite_warhorse.3",0), ("mongol_elite_warhorse.4",0), ("mongol_elite_warhorse.5",0), ("mongol_elite_warhorse.6",0)], itp_merchandise|itp_type_horse, 0, 1699,abundance(50)|hit_points(165)|body_armor(40)|difficulty(4)|horse_speed(52)|horse_maneuver(50)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_8]],

["mh_bow_a", "Horde Bow", [("mongol_bow_x",0),("mongol_bow_x_case", ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 1099 , weight(1.25)|difficulty(5)|spd_rtng(100)|shoot_speed(88) | thrust_damage(29 ,pierce),imodbit_cracked | imodbit_bent | imodbit_masterwork, [], [fac_kingdom_8] ],
["mh_pike_a", "Horde Hafted Blade", [("mongol_pike_a",0), ("mongol_pike_a.1",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry, itcf_carry_spear|itc_guandao,499 , weight(3.25)|difficulty(0)|spd_rtng(93) | weapon_length(153)|swing_damage(40 , cut) | thrust_damage(21 ,  pierce),imodbits_polearm, [], [fac_kingdom_8] ],
["mh_pike_b", "Horde Hafted Blade", [("mongol_pike_b",0), ("mongol_pike_b.1",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry, itcf_carry_spear|itc_guandao,399 , weight(2.25)|difficulty(0)|spd_rtng(115) | weapon_length(130)|swing_damage(40 , cut) | thrust_damage(15 ,  pierce),imodbits_polearm, [], [fac_kingdom_8] ],

["mh_spear_a", "Horde Spear", [("mongol_spear_x",0), ("mongol_spear_x.1",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry,itc_staff|itcf_carry_spear,399 , weight(2.25)|difficulty(0)|spd_rtng(90) | weapon_length(192)|swing_damage(23 , cut) | thrust_damage(28 ,  pierce),imodbits_polearm, [], [fac_kingdom_8] ],
 
["mh_sword_a", "Horde Sabre", [("mongol_saber_a",0),("mongol_saber_a_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 159, weight(1.25)|difficulty(0)|spd_rtng(100) | weapon_length(90)|swing_damage(32 , cut),imodbits_sword_high, [], [fac_kingdom_8] ],

["mkk_gauntlets_sar_a","Sarranid Scale Gloves", [("gauntlets_arabs_a_L", 0)], itp_type_hand_armor|itp_merchandise, 0,710, weight(0.75)|abundance(100)|body_armor(5), imodbit_lordly, [], [fac_kingdom_6]],
["mkk_gauntlets_sar_b","Sarranid Decorated Scale Gloves", [("gauntlets_arabs_b_L", 0)], itp_type_hand_armor|itp_merchandise, 0,999, weight(0.75)|abundance(100)|body_armor(6), imodbit_lordly, [], [fac_kingdom_6]],
["mkk_gauntlets_mail_a","Mail Gloves", [("gauntlets_crysader_L", 0)], itp_type_hand_armor|itp_merchandise, 0,710, weight(0.75)|abundance(100)|body_armor(5), imodbits_none, [], [fac_kingdom_6]],
["mkk_gloves_a","Leather Gloves", [("gloves_a_L", 0)], itp_type_hand_armor|itp_merchandise, 0,710, weight(0.75)|abundance(100)|body_armor(3), imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_6]],
["mkk_gloves_b","Rich Leather Gloves", [("gloves_lord_L", 0)], itp_type_hand_armor|itp_merchandise, 0,899, weight(0.75)|abundance(100)|body_armor(4), imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_6]],
["mkk_gloves_c","Enchanted Leather Gloves", [("gloves_king_L", 0)], itp_type_hand_armor|itp_merchandise, 0,1399, weight(0.75)|abundance(1)|body_armor(8), imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_6]],

["civil_poor_boots_a","Sandals", [("civil_poor_boots_a", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,75, weight(1)|abundance(100)|leg_armor(1), imodbits_cloth, [], [fac_kingdom_6]],
["civil_rich_boots_a","Rich Boots", [("civil_rich_Boots_a", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,450, weight(1)|abundance(100)|leg_armor(18), imodbits_cloth, [], [fac_kingdom_6]],
["civil_rich_boots_b","Rich Boots", [("civil_rich_Boots_b", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,450, weight(1)|abundance(100)|leg_armor(18), imodbits_cloth, [], [fac_kingdom_6]],

["mkk_boots_common_a","Sarranid Boots", [("boots_tyrk_a", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,99, weight(1)|abundance(100)|leg_armor(10), imodbits_cloth, [], [fac_kingdom_6]],
["mkk_boots_common_b","Sarranid Boots", [("boots_tyrk_b", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,99, weight(1)|abundance(100)|leg_armor(10), imodbits_cloth, [], [fac_kingdom_6]],
["mkk_boots_common_c","Sarranid Boots", [("boots_tyrk_c", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,99, weight(1)|abundance(100)|leg_armor(10), imodbits_cloth, [], [fac_kingdom_6]],

["mkk_boots_a","Light Sarranid Boots", [("saracin_light_boot_a", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,159, weight(1)|abundance(100)|leg_armor(12), imodbits_cloth, [], [fac_kingdom_6]],
["mkk_boots_b","Light Sarranid Boots", [("saracin_light_boot_b", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,159, weight(1)|abundance(100)|leg_armor(12), imodbits_cloth, [], [fac_kingdom_6]],

["mkk_leather_boots_a","Sarranid Leather Boots", [("saracin_medium_boot_a", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,399, weight(1)|abundance(100)|leg_armor(20), imodbits_cloth, [], [fac_kingdom_6]],
["mkk_leather_boots_b","Sarranid Leather Boots", [("saracin_medium_boot_b", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,399, weight(1)|abundance(100)|leg_armor(20), imodbits_cloth, [], [fac_kingdom_6]],

["mkk_heavy_boots_a","Sarranid Heavy Boots", [("saracin_hard_boot_a", 0)], itp_type_foot_armor|itp_attach_armature, 0,1199, weight(2)|abundance(100)|leg_armor(34), imodbits_plate, [], [fac_kingdom_6]],
["mkk_heavy_boots_b","Sarranid Heavy Boots", [("saracin_hard_boot_b", 0)], itp_type_foot_armor|itp_attach_armature, 0,1199, weight(2)|abundance(100)|leg_armor(34), imodbits_plate, [], [fac_kingdom_6]],


["mkk_turban_a", "Turban", [("saracin_turban_a",0)], itp_merchandise|itp_type_head_armor, 0, 255, weight(2)|abundance(100)|head_armor(21)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_6] ],
["mkk_turban_b", "Turban", [("saracin_turban_b",0)], itp_merchandise|itp_type_head_armor, 0, 255, weight(2)|abundance(100)|head_armor(21)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_6] ],
["mkk_turban_c", "Turban", [("saracin_turban_c",0)], itp_merchandise|itp_type_head_armor, 0, 255, weight(2)|abundance(100)|head_armor(21)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_6] ],

["mkk_helm_sar_a","Light Sarranid Helmet", [("helm_saracin_3", 0)], itp_type_head_armor|itp_merchandise, 0,390, weight(1)|abundance(100)|head_armor(15)|difficulty(7), imodbits_none, [], [fac_kingdom_6]],
["mkk_helm_sar_b","Sarranid War Cap", [("helm_saracin_b", 0)], itp_type_head_armor|itp_merchandise, 0,390, weight(1)|abundance(100)|head_armor(15)|difficulty(7), imodbits_none, [], [fac_kingdom_6]],

["mkk_helm_warrior_a","Warrior Helmet", [("helm_saracin_2", 0)], itp_type_head_armor|itp_merchandise, 0,450, weight(2)|abundance(100)|head_armor(25)|difficulty(7), imodbit_reinforced, [], [fac_kingdom_6]],
["mkk_helm_warrior_b","Warrior Helmet", [("helm_saracin_a", 0)], itp_type_head_armor|itp_merchandise, 0,450, weight(2)|abundance(100)|head_armor(39)|difficulty(7), imodbit_reinforced, [], [fac_kingdom_6]],
["mkk_helm_warrior_c","Warrior Helmet", [("helm_saracin_j", 0)], itp_type_head_armor|itp_merchandise, 0,450, weight(2)|abundance(100)|head_armor(39)|difficulty(7), imodbit_reinforced, [], [fac_kingdom_6]],

["mkk_helm_mail_a","Mail Helmet", [("helm_saracin_f", 0)], itp_type_head_armor|itp_merchandise, 0,450, weight(2)|abundance(100)|head_armor(32)|difficulty(7), imodbit_reinforced, [], [fac_kingdom_6]],
["mkk_helm_mail_b","Mail Helmet", [("helm_saracin_1", 0)], itp_type_head_armor|itp_merchandise, 0,450, weight(2)|abundance(100)|head_armor(32)|difficulty(7), imodbit_reinforced, [], [fac_kingdom_6]],
["mkk_helm_mail_c","Mail Helmet", [("helm_saracin_d", 0)], itp_type_head_armor|itp_merchandise, 0,450, weight(2)|abundance(100)|head_armor(32)|difficulty(7), imodbit_reinforced, [], [fac_kingdom_6]],
["mkk_helm_mail_d","Mail Helmet", [("helm_saracin_e", 0)], itp_type_head_armor|itp_merchandise, 0,450, weight(2)|abundance(100)|head_armor(32)|difficulty(7), imodbit_reinforced, [], [fac_kingdom_6]],
["mkk_helm_mail_e","Mail Helmet", [("helm_saracin_f", 0)], itp_type_head_armor|itp_merchandise, 0,450, weight(2)|abundance(100)|head_armor(32)|difficulty(7), imodbit_reinforced, [], [fac_kingdom_6]],

["mkk_helm_light_sarranid","Light Sarranid Helmet", [("helm_saracin_c", 0)], itp_type_head_armor|itp_merchandise, 0,399, weight(2)|abundance(100)|head_armor(25)|difficulty(0), imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_6]],

["mkk_gulam_helm_a","Gulam Helmet", [("gulam_helm_a", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,390, weight(2)|abundance(100)|head_armor(45)|difficulty(7), imodbits_none, [], [fac_kingdom_6]],
["mkk_gulam_helm_b","Gulam Helmet", [("gulam_helm_b", 0),("gulam_helm_b_market", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise|itp_fit_to_head, 0,390, weight(2)|abundance(100)|head_armor(45)|difficulty(7), imodbits_none, [], [fac_kingdom_6]],
["mkk_gulam_helm_c","Gulam Helmet", [("gulam_helm_c", 0),("gulam_helm_c_market", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise|itp_fit_to_head, 0,390, weight(2)|abundance(100)|head_armor(45)|difficulty(7), imodbits_none, [], [fac_kingdom_6]],
["mkk_gulam_helm_d","Gulam Helmet", [("gulam_helm_d", 0),("gulam_helm_d_market", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise|itp_fit_to_head, 0,390, weight(2)|abundance(100)|head_armor(45)|difficulty(7), imodbits_none, [], [fac_kingdom_6]],
["mkk_gulam_helm_f","Gulam Helmet", [("gulam_helm_f", 0),("gulam_helm_f_market", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise|itp_fit_to_head|itp_covers_beard, 0,390, weight(2)|abundance(100)|head_armor(45)|difficulty(7), imodbits_none, [], [fac_kingdom_6]],

["mkk_sultan_helmet_a","Sultan's Helmet", [("helm_Sultan_saracens", 0),("helm_Sultan_saracens_market", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise|itp_fit_to_head|itp_covers_beard, 0,3990, weight(2)|abundance(1)|head_armor(58)|difficulty(17), imodbits_none, [], [fac_kingdom_6]],

["mkk_heavy_helmet_a", "Sarranid Heavy Cavalry Helmet", [("helm_tyrk_heavi_a",0), ("helm_tyrk_heavi_a.1",0)], itp_merchandise|itp_type_head_armor, 0, 1799, weight(2)|abundance(100)|head_armor(54)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_plate, [], [fac_kingdom_6] ],
["mkk_heavy_helmet_b", "Sarranid Heavy Cavalry Helmet", [("helm_tyrk_heavi_b",0), ("helm_tyrk_heavi_b.1",0)], itp_merchandise|itp_type_head_armor, 0, 1799, weight(2)|abundance(100)|head_armor(54)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_plate, [], [fac_kingdom_6] ],
["mkk_heavy_helmet_c", "Sarranid Heavy Cavalry Helmet", [("helm_tyrk_heavi_c",0), ("helm_tyrk_heavi_c.1",0)], itp_merchandise|itp_type_head_armor, 0, 1799, weight(2)|abundance(100)|head_armor(54)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_plate, [], [fac_kingdom_6] ],

["mkk_semi_heavy_helmet_a", "Sarranid Heavy Helmet", [("helm_tyrk_a",0), ("helm_tyrk_a.1",0), ("helm_tyrk_a_market",ixmesh_inventory), ("helm_tyrk_a_market.1",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 1699, weight(2)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, [], [fac_kingdom_6] ],
["mkk_semi_heavy_helmet_b", "Sarranid Heavy Helmet", [("helm_tyrk_b",0), ("helm_tyrk_b_market",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 1699, weight(2)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, [], [fac_kingdom_6] ],
["mkk_semi_heavy_helmet_c", "Sarranid Heavy Helmet", [("helm_tyrk_c",0), ("helm_tyrk_c_market",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 1699, weight(2)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, [], [fac_kingdom_6] ],
["mkk_semi_heavy_helmet_d", "Sarranid Heavy Helmet", [("helm_tyrk_d",0), ("helm_tyrk_d_market",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 1699, weight(2)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, [], [fac_kingdom_6] ],
["mkk_semi_heavy_helmet_e", "Sarranid Heavy Helmet", [("helm_tyrk_e",0), ("helm_tyrk_e.1",0), ("helm_tyrk_e.2",0), ("helm_tyrk_e_market",ixmesh_inventory), ("helm_tyrk_e_market.1",ixmesh_inventory), ("helm_tyrk_e_market.2",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 1699, weight(2)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, [], [fac_kingdom_6] ],
["mkk_semi_heavy_helmet_f", "Sarranid Heavy Helmet", [("helm_tyrk_f",0), ("helm_tyrk_f.1",0), ("helm_tyrk_f_market",ixmesh_inventory), ("helm_tyrk_f_market.1",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 1699, weight(2)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, [], [fac_kingdom_6] ],

["mkk_sultan_armor", "Sultan Armor", [("armor_Sultan_saracens",0), ("armor_Sultan_saracens.1",0), ("armor_Sultan_saracens.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,6289 , weight(20)|abundance(1)|head_armor(0)|body_armor(61)|leg_armor(26)|difficulty(18) ,imodbits_armor, [], [fac_kingdom_6] ],

["mkk_mamluke_a", "Mamluke Armor", [("tyrk_armor_heavi_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1699 , weight(20)|abundance(100)|head_armor(0)|body_armor(53)|leg_armor(23)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_6] ],
["mkk_mamluke_b", "Mamluke Armor", [("tyrk_armor_heavi_b",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1699 , weight(20)|abundance(100)|head_armor(0)|body_armor(53)|leg_armor(23)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_6] ],
["mkk_mamluke_c", "Mamluke Armor", [("tyrk_armor_heavi_c",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1699 , weight(20)|abundance(100)|head_armor(0)|body_armor(53)|leg_armor(23)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_6] ],

["mkk_archer_armor_a", "Sarranid Archers Armor", [("armor_medium_tyrk_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1299 , weight(16)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(12)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_6] ],
["mkk_archer_armor_b", "Sarranid Archers Armor", [("armor_medium_tyrk_b",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1299 , weight(16)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(12)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_6] ],
["mkk_archer_armor_c", "Sarranid Archers Armor", [("armor_medium_tyrk_c",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1299 , weight(16)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(12)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_6] ],
["mkk_archer_armor_d", "Sarranid Archers Armor", [("armor_medium_tyrk_d",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1299 , weight(16)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(12)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_6] ],

["mkk_infantry_armor_a", "Sarranid Infantry Armor", [("armor_medium_tyrk_e",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1499 , weight(20)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(21)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_6] ],
["mkk_infantry_armor_b", "Sarranid Infantry Armor", [("armor_medium_tyrk_f",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1499 , weight(20)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(21)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_6] ],

["mkk_black_scale_a", "Black Scale Armor", [("Ghulam_heavy_cavalryman_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1599 , weight(20)|abundance(100)|head_armor(0)|body_armor(53)|leg_armor(18)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_6] ],
["mkk_black_scale_b", "Black Scale Armor", [("Ghulam_heavy_cavalryman_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1599 , weight(20)|abundance(100)|head_armor(0)|body_armor(53)|leg_armor(18)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_6] ],
["mkk_black_scale_c", "Black Scale Armor", [("Ghulam_heavy_cavalryman_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1599 , weight(20)|abundance(100)|head_armor(0)|body_armor(53)|leg_armor(18)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_6] ],

["mkk_robe_a", "Warrior Robe", [("arabian_light_armor_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,519 , weight(12)|abundance(100)|head_armor(0)|body_armor(27)|leg_armor(11)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_6] ],
["mkk_robe_b", "Warrior Robe", [("arabian_light_armor_b",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,519 , weight(12)|abundance(100)|head_armor(0)|body_armor(27)|leg_armor(11)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_6] ],
["mkk_robe_c", "Warrior Robe", [("arabian_light_armor_c",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,519 , weight(12)|abundance(100)|head_armor(0)|body_armor(27)|leg_armor(11)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_6] ],
["mkk_robe_d", "Warrior Robe", [("arabian_light_armor_d",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,519 , weight(12)|abundance(100)|head_armor(0)|body_armor(27)|leg_armor(11)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_6] ],

["mkk_midi_robe_a", "Warrior Mail with Robe", [("armor_archer_saracin_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1199 , weight(17)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(16)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_6] ],
["mkk_midi_robe_b", "Warrior Mail with Robe", [("armor_archer_saracin_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1199 , weight(17)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(16)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_6] ],
["mkk_midi_robe_c", "Warrior Mail with Robe", [("armor_archer_saracin_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1199 , weight(17)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(16)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_6] ],
["mkk_midi_robe_d", "Warrior Mail with Robe", [("armor_archer_saracin_4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1199 , weight(17)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(16)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_6] ],
["mkk_midi_robe_e", "Warrior Mail with Robe", [("armor_archer_saracin_5",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1199 , weight(17)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(16)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_6] ],
["mkk_midi_robe_f", "Warrior Mail with Robe", [("armor_archer_saracin_6",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1199 , weight(17)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(16)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_6] ],

["mkk_scale_vest_a", "Scale Vest", [("heavy_armor_arabs_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1149 , weight(17)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(16)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_6] ],
["mkk_scale_vest_b", "Scale Vest", [("heavy_armor_arabs_b",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1149 , weight(17)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(16)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_6] ],
["mkk_scale_vest_c", "Scale Vest", [("heavy_armor_arabs_c_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1149 , weight(17)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(16)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_6] ],
["mkk_scale_vest_d", "Scale Vest", [("heavy_armor_arabs_d",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1149 , weight(17)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(16)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_6] ],
["mkk_scale_vest_e", "Scale Vest", [("heavy_armor_arabs_e",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1149 , weight(17)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(16)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_6] ],
["mkk_scale_vest_f", "Scale Vest", [("heavy_armor_arabs_f_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1149 , weight(17)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(16)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_6] ],

["mkk_scale_vest_alt_a", "Scale Vest with Pauldrons", [("heavy_armor_arabs_c",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1399 , weight(19)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(16)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_6] ],
["mkk_scale_vest_alt_b", "Scale Vest with Pauldrons", [("heavy_armor_arabs_f",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1399 , weight(19)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(16)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_6] ],

["saracin_hard_horses_a","Heavy Sarranid Horse", [("saracin_hard_horses_a", 0),("saracin_hard_horses_a", imodbit_heavy|imodbit_spirited)], itp_type_horse|itp_merchandise, 0,5000, weight(0)|abundance(10)|body_armor(40)|difficulty(3)|hit_points(200)|horse_maneuver(37)|horse_speed(45)|weapon_length(110)|horse_charge(50), imodbit_champion, [], [fac_kingdom_6]],
["saracin_hard_horses_b","Heavy Sarranid Horse", [("saracin_hard_horses_b", 0),("saracin_hard_horses_b", imodbit_heavy|imodbit_spirited)], itp_type_horse|itp_merchandise, 0,5000, weight(0)|abundance(10)|body_armor(40)|difficulty(3)|hit_points(200)|horse_maneuver(37)|horse_speed(45)|weapon_length(110)|horse_charge(50), imodbit_champion, [], [fac_kingdom_6]],
["saracin_hard_horses_c","Heavy Sarranid Horse", [("saracin_hard_horses_c", 0),("saracin_hard_horses_a", imodbit_heavy|imodbit_spirited)], itp_type_horse|itp_merchandise, 0,5000, weight(0)|abundance(10)|body_armor(40)|difficulty(3)|hit_points(200)|horse_maneuver(37)|horse_speed(45)|weapon_length(110)|horse_charge(50), imodbit_champion, [], [fac_kingdom_6]],
["saracin_hard_horses_d","Heavy Sarranid Horse", [("saracin_hard_horses_d", 0),("saracin_hard_horses_d", imodbit_heavy|imodbit_spirited)], itp_type_horse|itp_merchandise, 0,5000, weight(0)|abundance(10)|body_armor(40)|difficulty(3)|hit_points(200)|horse_maneuver(37)|horse_speed(45)|weapon_length(110)|horse_charge(50), imodbit_champion, [], [fac_kingdom_6]],
["saracin_hard_horses_a_v1","Heavy Sarranid Horse", [("saracin_hard_horses_a_v1", 0),("saracin_hard_horses_a_v1", imodbit_heavy|imodbit_spirited)], itp_type_horse|itp_merchandise, 0,5000, weight(0)|abundance(10)|body_armor(40)|difficulty(3)|hit_points(200)|horse_maneuver(37)|horse_speed(45)|weapon_length(110)|horse_charge(50), imodbit_champion, [], [fac_kingdom_6]],
["saracin_hard_horses_b_v1","Heavy Sarranid Horse", [("saracin_hard_horses_b_v1", 0),("saracin_hard_horses_b_v1", imodbit_heavy|imodbit_spirited)], itp_type_horse|itp_merchandise, 0,5000, weight(0)|abundance(10)|body_armor(40)|difficulty(3)|hit_points(200)|horse_maneuver(37)|horse_speed(45)|weapon_length(110)|horse_charge(50), imodbit_champion, [], [fac_kingdom_6]],
["saracin_hard_horses_c_v1","Heavy Sarranid Horse", [("saracin_hard_horses_c_v1", 0),("saracin_hard_horses_a_v1", imodbit_heavy|imodbit_spirited)], itp_type_horse|itp_merchandise, 0,5000, weight(0)|abundance(10)|body_armor(40)|difficulty(3)|hit_points(200)|horse_maneuver(37)|horse_speed(45)|weapon_length(110)|horse_charge(50), imodbit_champion, [], [fac_kingdom_6]],
["saracin_hard_horses_d_v1","Heavy Sarranid Horse", [("saracin_hard_horses_d_v1", 0),("saracin_hard_horses_d_v1", imodbit_heavy|imodbit_spirited)], itp_type_horse|itp_merchandise, 0,5000, weight(0)|abundance(10)|body_armor(40)|difficulty(3)|hit_points(200)|horse_maneuver(37)|horse_speed(45)|weapon_length(110)|horse_charge(50), imodbit_champion, [], [fac_kingdom_6]],
["saracen_horse_sultan","Sultan's Horse", [("saracen_horse_Sultan", 0)], itp_type_horse|itp_merchandise, 0,5000, weight(0)|abundance(10)|body_armor(40)|difficulty(3)|hit_points(200)|horse_maneuver(37)|horse_speed(45)|weapon_length(110)|horse_charge(50), imodbit_champion, [], [fac_kingdom_6]],

# Sonyer OSP Items
["maa_shield_a", "Adid Footman Shield", [("shielea",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 399, weight(2.5)|abundance(100)|hit_points(979)|body_armor(10)|spd_rtng(82)|shield_width(90),imodbits_shield, [], [fac_kingdom_11] ],
["maa_shield_a2", "Adid Footman Shield", [("shieleas",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 399, weight(2.5)|abundance(100)|hit_points(979)|body_armor(10)|spd_rtng(82)|shield_width(90),imodbits_shield, [], [fac_kingdom_11] ],
["maa_shield_a3", "Adid Footman Shield", [("shieleass",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 399, weight(2.5)|abundance(100)|hit_points(979)|body_armor(10)|spd_rtng(82)|shield_width(90),imodbits_shield, [], [fac_kingdom_11] ],
["maa_shield_a4", "Adid Footman Shield", [("shieleasss",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 399, weight(2.5)|abundance(100)|hit_points(979)|body_armor(10)|spd_rtng(82)|shield_width(90),imodbits_shield, [], [fac_kingdom_11] ],
["maa_shield_a5", "Adid Footman Shield", [("cruss",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 399, weight(2.5)|abundance(100)|hit_points(979)|body_armor(10)|spd_rtng(82)|shield_width(90),imodbits_shield, [], [fac_kingdom_11] ],
["maa_shield_a6", "Adid Footman Shield", [("crusss",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 399, weight(2.5)|abundance(100)|hit_points(979)|body_armor(10)|spd_rtng(82)|shield_width(90),imodbits_shield, [], [fac_kingdom_11] ],
["maa_shield_a7", "Adid Footman Shield", [("crussss",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 399, weight(2.5)|abundance(100)|hit_points(979)|body_armor(10)|spd_rtng(82)|shield_width(90),imodbits_shield, [], [fac_kingdom_11] ],
["maa_shield_a8", "Adid Footman Shield", [("crusads",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 399, weight(2.5)|abundance(100)|hit_points(979)|body_armor(10)|spd_rtng(82)|shield_width(90),imodbits_shield, [], [fac_kingdom_11] ],
["maa_shield_a9", "Adid Footman Shield", [("crusadss",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 399, weight(2.5)|abundance(100)|hit_points(979)|body_armor(10)|spd_rtng(82)|shield_width(90),imodbits_shield, [], [fac_kingdom_11] ],
["maa_shield_a10", "Adid Footman Shield", [("crusadsss",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 399, weight(2.5)|abundance(100)|hit_points(979)|body_armor(10)|spd_rtng(82)|shield_width(90),imodbits_shield, [], [fac_kingdom_11] ],
["maa_shield_a11", "Adid Footman Shield", [("crusadersh",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 399, weight(2.5)|abundance(100)|hit_points(979)|body_armor(10)|spd_rtng(82)|shield_width(90),imodbits_shield, [], [fac_kingdom_11] ],
["maa_shield_a12", "Adid Footman Shield", [("crusadershsss",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 399, weight(2.5)|abundance(100)|hit_points(979)|body_armor(10)|spd_rtng(82)|shield_width(90),imodbits_shield, [], [fac_kingdom_11] ],

["maa_round_shield_a", "Adid Round Shield", [("saracensh",0)], itp_type_shield, itcf_carry_round_shield, 299, weight(1.5)|hit_points(500)|body_armor(6)|spd_rtng(90)|shield_width(40),imodbits_shield, [], [fac_kingdom_11] ],
["maa_round_shield_a2", "Adid Round Shield", [("saracenshs",0)], itp_type_shield, itcf_carry_round_shield, 299, weight(1.5)|hit_points(500)|body_armor(6)|spd_rtng(90)|shield_width(40),imodbits_shield, [], [fac_kingdom_11] ],
["maa_round_shield_a3", "Adid Round Shield", [("saracenshss",0)], itp_type_shield, itcf_carry_round_shield, 299, weight(1.5)|hit_points(500)|body_armor(6)|spd_rtng(90)|shield_width(40),imodbits_shield, [], [fac_kingdom_11] ],
["maa_round_shield_a4", "Adid Round Shield", [("saracenshsss",0)], itp_type_shield, itcf_carry_round_shield, 299, weight(1.5)|hit_points(500)|body_armor(6)|spd_rtng(90)|shield_width(40),imodbits_shield, [], [fac_kingdom_11] ],

["maa_camel_rider_shield_a", "Camel Rider Shield", [("camel_rider_shield_a",0)], itp_type_shield, itcf_carry_round_shield, 339, weight(1.5)|hit_points(540)|body_armor(6)|spd_rtng(90)|shield_width(52),imodbits_shield, [], [fac_kingdom_11, fac_kingdom_6] ],
["maa_camel_rider_shield_b", "Camel Rider Shield", [("camel_rider_shield_b",0)], itp_type_shield, itcf_carry_round_shield, 339, weight(1.5)|hit_points(540)|body_armor(6)|spd_rtng(90)|shield_width(52),imodbits_shield, [], [fac_kingdom_11, fac_kingdom_6] ],
["maa_camel_rider_shield_c", "Camel Rider Shield", [("camel_rider_shield_c",0)], itp_type_shield, itcf_carry_round_shield, 339, weight(1.5)|hit_points(540)|body_armor(6)|spd_rtng(90)|shield_width(52),imodbits_shield, [], [fac_kingdom_11, fac_kingdom_6] ],
["maa_camel_rider_shield_d", "Camel Rider Shield", [("camel_rider_shield_d",0)], itp_type_shield, itcf_carry_round_shield, 339, weight(1.5)|hit_points(540)|body_armor(6)|spd_rtng(90)|shield_width(52),imodbits_shield, [], [fac_kingdom_11, fac_kingdom_6] ],
["maa_camel_rider_shield_e", "Camel Rider Shield", [("camel_rider_shield_e",0)], itp_type_shield, itcf_carry_round_shield, 339, weight(1.5)|hit_points(540)|body_armor(6)|spd_rtng(90)|shield_width(52),imodbits_shield, [], [fac_kingdom_11, fac_kingdom_6] ],
["maa_camel_rider_shield_f", "Camel Rider Shield", [("camel_rider_shield_f",0)], itp_type_shield, itcf_carry_round_shield, 339, weight(1.5)|hit_points(540)|body_armor(6)|spd_rtng(90)|shield_width(52),imodbits_shield, [], [fac_kingdom_11, fac_kingdom_6] ],

["maa_light_helmet_a", "Adid Light Helmet", [("sarr",0)], itp_merchandise|itp_type_head_armor, 0, 299, weight(2.5)|abundance(100)|head_armor(24)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_11] ],

["maa_mail_coif_a", "Adid Mail Helmet", [("turbanhelmsaa",0)], itp_merchandise|itp_type_head_armor, 0, 499, weight(2.5)|abundance(100)|head_armor(37)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_11] ],
["maa_mail_coif_a2", "Adid Mail Helmet", [("turbanhelmsa",0)], itp_merchandise|itp_type_head_armor, 0, 499, weight(2.5)|abundance(100)|head_armor(37)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_11] ],
["maa_mail_coif_a3", "Adid Mail Helmet", [("turbanhelms",0)], itp_merchandise|itp_type_head_armor, 0, 499, weight(2.5)|abundance(100)|head_armor(37)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_11] ],
["maa_mail_coif_b", "Adid Mail Helmet", [("turbanhelmss",0)], itp_merchandise|itp_type_head_armor, 0, 499, weight(2.5)|abundance(100)|head_armor(37)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_11] ],
["maa_mail_coif_c", "Adid Open Mail Helmet", [("turbanhelmsss",0)], itp_merchandise|itp_type_head_armor, 0, 459, weight(2.5)|abundance(100)|head_armor(34)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_11] ],

["maa_cavalry_a", "Adid Open Cavalry Helmet", [("ghuls",0),("ghuls.1",0)], itp_merchandise|itp_type_head_armor, 0, 499, weight(2.5)|abundance(100)|head_armor(37)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_11] ],
["maa_cavalry_b", "Adid Cavalry Helmet", [("ghulss",0),("ghulss.1",0)], itp_merchandise|itp_type_head_armor, 0, 599, weight(2.5)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_11] ],
["maa_cavalry_c", "Adid Cavalry Helmet", [("ghulsss",0),("ghulsss.1",0)], itp_merchandise|itp_type_head_armor, 0, 599, weight(2.5)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_11] ],
["maa_cavalry_c2", "Adid Cavalry Helmet", [("ghulssss",0)], itp_merchandise|itp_type_head_armor, 0, 599, weight(2.5)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_11] ],


["maa_coat_a", "Light Adid Cloth", [("saracenmailsss",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,99 , weight(9)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_11] ], 
["maa_coat_a2", "Light Adid Cloth", [("saracenmailsssss",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,99 , weight(9)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_11] ], 
["maa_coat_a3", "Light Adid Cloth", [("saracenmails",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,99 , weight(9)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_11] ], 

["maa_mail_a", "Adid Mail", [("saracenmails",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,459 , weight(24)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(10)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_11] ], 
["maa_mail_b", "Adid Mail with Cloth", [("saracenmailss",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,469 , weight(24)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(10)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_11] ], 
["maa_mail_b2", "Adid Mail with Cloth", [("saracenmailssss",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,469 , weight(24)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(10)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_11] ], 

["maa_scale_a", "Adid Scale Armor", [("lamelarghulam",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,599 , weight(22)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(10)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_11] ], 
["maa_scale_a2", "Adid Scale Armor", [("mailsarazin",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,599 , weight(22)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(10)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_11] ], 
["maa_scale_b", "Adid Scale on Mail", [("sarazinass",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,999 , weight(22)|abundance(100)|head_armor(0)|body_armor(53)|leg_armor(10)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_11] ], 

["maa_heavy_scale_a", "Adid Elite Scale Armor", [("saracenghulam",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1399 , weight(23)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(17)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_11] ], 

["maa_camel_a", "Camel", [("bedyin_camel",0)], itp_merchandise|itp_type_horse,0 ,999, weight(0)|abundance(100)|hit_points(200)|body_armor(20)|difficulty(0)|horse_speed(30)|horse_maneuver(30)|horse_charge(20)|horse_scale(90),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_11, fac_kingdom_6]],

["maa_camel_light_a", "Rider's Camel", [("camel_22",0)], itp_merchandise|itp_type_horse,0 ,1599, weight(0)|abundance(100)|hit_points(250)|body_armor(25)|difficulty(0)|horse_speed(40)|horse_maneuver(40)|horse_charge(30)|horse_scale(90),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_11, fac_kingdom_6]],
["maa_camel_light_b", "Rider's Camel", [("bedyin_camel_1",0),("bedyin_camel_1.1",0)], itp_merchandise|itp_type_horse,0 ,1999, weight(0)|abundance(100)|hit_points(250)|body_armor(25)|difficulty(0)|horse_speed(40)|horse_maneuver(40)|horse_charge(30)|horse_scale(90),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_11, fac_kingdom_6]],
["maa_camel_light_c", "Rider's Camel", [("bedyin_camel_a",0),("bedyin_camel_a.1",0)], itp_merchandise|itp_type_horse,0 ,1999, weight(0)|abundance(100)|hit_points(250)|body_armor(25)|difficulty(0)|horse_speed(40)|horse_maneuver(40)|horse_charge(30)|horse_scale(90),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_11, fac_kingdom_6]],
["maa_camel_light_d", "Rider's Camel", [("bedyin_camel_b",0),("bedyin_camel_b.1",0)], itp_merchandise|itp_type_horse,0 ,1999, weight(0)|abundance(100)|hit_points(250)|body_armor(25)|difficulty(0)|horse_speed(40)|horse_maneuver(40)|horse_charge(30)|horse_scale(90),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_11, fac_kingdom_6]],

["maa_camel_war_a", "War Camel", [("bedyin_camel_c",0),("bedyin_camel_c.1",0),("bedyin_camel_c.2",0)], itp_merchandise|itp_type_horse,0 ,2599, weight(0)|abundance(100)|hit_points(300)|body_armor(45)|difficulty(3)|horse_speed(45)|horse_maneuver(45)|horse_charge(45)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_11, fac_kingdom_6]],
["maa_camel_war_b", "War Camel", [("bedyin_camel_d",0),("bedyin_camel_d.1",0),("bedyin_camel_d.2",0)], itp_merchandise|itp_type_horse,0 ,2599, weight(0)|abundance(100)|hit_points(300)|body_armor(45)|difficulty(3)|horse_speed(45)|horse_maneuver(45)|horse_charge(45)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_11, fac_kingdom_6]],
["maa_camel_war_c", "War Camel", [("bedyin_camel_e",0),("bedyin_camel_e.1",0),("bedyin_camel_e.2",0)], itp_merchandise|itp_type_horse,0 ,2599, weight(0)|abundance(100)|hit_points(300)|body_armor(45)|difficulty(3)|horse_speed(45)|horse_maneuver(45)|horse_charge(45)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_11, fac_kingdom_6]],
["maa_camel_war_d", "War Camel", [("bedyin_camel_f",0),("bedyin_camel_f.1",0)], itp_merchandise|itp_type_horse,0 ,2599, weight(0)|abundance(100)|hit_points(300)|body_armor(45)|difficulty(3)|horse_speed(45)|horse_maneuver(45)|horse_charge(45)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_11, fac_kingdom_6]],

# SPAK OSP items
["ms_plain_shield_a", "Rusty Round Shield", [("2shield",0)], itp_type_shield, itcf_carry_round_shield,  140 , weight(4)|hit_points(330)|body_armor(6)|spd_rtng(90)|shield_width(40),imodbits_shield ],
["ms_metal_shield_a", "Metal Shield", [("hermitage_shield_1",0)], itp_type_shield, itcf_carry_round_shield,  140 , weight(4)|hit_points(1200)|body_armor(6)|spd_rtng(90)|shield_width(40),imodbits_shield ],
["ms_metal_shield_a2", "Metal Shield", [("hermitage_shield_2",0)], itp_type_shield, itcf_carry_round_shield,  140 , weight(4)|hit_points(1200)|body_armor(6)|spd_rtng(90)|shield_width(40),imodbits_shield ],
["ms_metal_shield_a3", "Metal Shield", [("hermitage_shield_3",0)], itp_type_shield, itcf_carry_round_shield,  140 , weight(4)|hit_points(1200)|body_armor(6)|spd_rtng(90)|shield_width(40),imodbits_shield ],
["ms_metal_shield_a4", "Metal Shield", [("hermitage_shield_4",0)], itp_type_shield, itcf_carry_round_shield,  140 , weight(4)|hit_points(1200)|body_armor(6)|spd_rtng(90)|shield_width(40),imodbits_shield ],
["ms_metal_shield_a5", "Metal Shield", [("hermitage_shield_5",0)], itp_type_shield, itcf_carry_round_shield,  140 , weight(4)|hit_points(1200)|body_armor(6)|spd_rtng(90)|shield_width(40),imodbits_shield ],

["ms_runic", "Runic Shield", [("alt_sh_run",0)], itp_type_shield, itcf_carry_round_shield,  140 , weight(4)|hit_points(330)|body_armor(6)|spd_rtng(90)|shield_width(40),imodbits_shield ],
["ms_doom", "Doom Shield", [("asmoday_seel",0)], itp_type_shield, itcf_carry_round_shield,  140 , weight(4)|hit_points(4531)|body_armor(40)|spd_rtng(90)|shield_width(40),imodbits_shield ],
["ms_heavy_shield", "Heavy Shield", [("heavy_shield2",0)], itp_type_shield, itcf_carry_round_shield,  140 , weight(4)|hit_points(330)|body_armor(6)|spd_rtng(90)|shield_width(40),imodbits_shield ],

["ms_great_axe_a", "Great Axe", [("2dblhead_ax",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 1299, weight(4.5)|difficulty(14)|spd_rtng(96) | weapon_length(90)|swing_damage(48 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["ms_great_axe_b", "Great Axe", [("dargor_axe",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 1399, weight(4.5)|difficulty(14)|spd_rtng(96) | weapon_length(100)|swing_damage(51 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["ms_flat_sword", "Wayfarer", [("flat_sword",0)], itp_type_two_handed_wpn| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip,2999 , weight(2.0)|difficulty(9)|spd_rtng(98) | weapon_length(110)|swing_damage(47 , cut) | thrust_damage(24 , pierce),imodbits_sword_high ],
["ms_hook_sword", "Hook Sword", [("hookSword_spak",0), ("hookSword_spak_scab",ixmesh_carry)], itp_type_two_handed_wpn| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,2599 , weight(2.0)|difficulty(9)|spd_rtng(98) | weapon_length(95)|swing_damage(47 , cut) | thrust_damage(0 , pierce),imodbits_sword_high ],
["ms_scythe", "Deadly Breathe", [("spak_IceAxe",0), ("spak_IceAxe.1",0)], itp_type_two_handed_wpn| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip,3999 , weight(2.0)|difficulty(16)|spd_rtng(98) | weapon_length(90)|swing_damage(55 , cut) | thrust_damage(31 , pierce),imodbits_sword_high ],
["ms_strange_sword", "Strange sword of Doom", [("asmoday_sword",0), ("asmoday_sword.1",0)], itp_type_two_handed_wpn| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip,3999 , weight(2.0)|difficulty(16)|spd_rtng(155) | weapon_length(100)|swing_damage(55 , cut) | thrust_damage(40 , pierce),imodbits_sword_high ],

["ms_butcher_sword", "Butcher Sword", [("butcher",0),("butcher_scab", ixmesh_carry)], itp_type_two_handed_wpn| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back|itcf_show_holster_when_drawn, 1499, weight(3)|difficulty(15)|spd_rtng(94) | weapon_length(90)|swing_damage(50, cut) | thrust_damage(31, pierce),imodbits_sword_high ],
["ms_flamberg", "Flamberge", [("flamberg",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back, 4699, weight(3)|difficulty(15)|spd_rtng(94) | weapon_length(125)|swing_damage(50, cut) | thrust_damage(31, pierce),imodbits_sword_high, [], [fac_kingdom_5, fac_kingdom_1, fac_kingdom_12] ],
["ms_flamberg_great", "Great Flamberge", [("flamberge",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back, 6899, weight(5)|difficulty(21)|spd_rtng(99) | weapon_length(155)|swing_damage(65, cut) | thrust_damage(40, pierce),imodbits_sword_high, [], [fac_kingdom_5, fac_kingdom_1, fac_kingdom_12] ],
["ms_two_h_sword_a", "Two Handed Sword", [("kingslayer",0),("kingslayer_scab",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back|itcf_show_holster_when_drawn, 999, weight(3)|difficulty(11)|spd_rtng(94) | weapon_length(120)|swing_damage(45, cut) | thrust_damage(31, pierce),imodbits_sword_high, [], [fac_kingdom_5, fac_kingdom_7, fac_kingdom_12] ],
["ms_two_h_sword_b", "Two Handed Sword", [("s_sword",0),("s_sword_scab",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back|itcf_show_holster_when_drawn, 999, weight(3)|difficulty(11)|spd_rtng(94) | weapon_length(120)|swing_damage(45, cut) | thrust_damage(31, pierce),imodbits_sword_high, [], [fac_kingdom_5, fac_kingdom_7, fac_kingdom_12] ],
["ms_two_h_sword_c", "Two Handed Sword", [("sp_2hsw",0),("sp_2hsw_sh",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back|itcf_show_holster_when_drawn, 999, weight(3)|difficulty(11)|spd_rtng(94) | weapon_length(120)|swing_damage(45, cut) | thrust_damage(31, pierce),imodbits_sword_high, [], [fac_kingdom_5, fac_kingdom_7, fac_kingdom_12] ],

["ms_helmet_bear_a", "Bear Helmet", [("bear_warior_helm",0)], itp_merchandise|itp_type_head_armor, 0, 299, weight(1)|abundance(1)|head_armor(21)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth,[], [fac_kingdom_4, fac_kingdom_2, fac_kingdom_12] ],

["ms_helmet_wolf_a", "Wolf Helmet", [("wolf_helm1",0)], itp_merchandise|itp_type_head_armor, 0, 349, weight(1)|abundance(1)|head_armor(29)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth,[], [fac_kingdom_4, fac_kingdom_2, fac_kingdom_12] ],
["ms_helmet_wolf_a2", "Wolf Helmet", [("wolf_helm2",0)], itp_merchandise|itp_type_head_armor, 0, 349, weight(1)|abundance(1)|head_armor(29)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth,[], [fac_kingdom_4, fac_kingdom_2, fac_kingdom_12] ],
["ms_helmet_wolf_a3", "Wolf Helmet", [("wolf_helm3",0)], itp_merchandise|itp_type_head_armor, 0, 349, weight(1)|abundance(1)|head_armor(29)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth,[], [fac_kingdom_4, fac_kingdom_2, fac_kingdom_12] ],
["ms_helmet_wolf_a4", "Wolf Helmet", [("wolf_helm4",0)], itp_merchandise|itp_type_head_armor, 0, 349, weight(1)|abundance(1)|head_armor(29)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth,[], [fac_kingdom_4, fac_kingdom_2, fac_kingdom_12] ],

["ms_great_helmet_a", "Great Helmet", [("2great_helmet_new",0)], itp_type_head_armor, 0, 999, weight(2.5)|abundance(100)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["ms_great_helmet_b", "Great Horned Kattle Hat", [("2kettle_hat_new",0)], itp_type_head_armor, 0, 999, weight(2.5)|abundance(100)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],

["ms_helmet_great_a", "Great Helmet of Doom", [("spak_helmet_k",0)], itp_type_head_armor, 0, 999, weight(2.5)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["ms_helmet_great_a2", "Great Helmet of Doom", [("spak_helmet_k2",0)], itp_type_head_armor, 0, 999, weight(2.5)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],

["ms_helmet_cult_a", "Great Helmet of Cultist", [("sub_helm",0)], itp_type_head_armor, 0, 999, weight(2.5)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["ms_helmet_cult_a2", "Great Helmet of Cultist", [("sub_helm4",0)], itp_type_head_armor, 0, 999, weight(2.5)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],

["ms_helmet_fiend_a", "Pit Fiend Helmet", [("sub_helm2",0)], itp_type_head_armor, 0, 2455, weight(2.5)|abundance(100)|head_armor(58)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["ms_helmet_fiend_a2", "Pit Fiend Helmet", [("sub_helm3",0)], itp_type_head_armor, 0, 2455, weight(2.5)|abundance(100)|head_armor(58)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],

["ms_helmet_dark_a", "Dark Horned Helmet", [("asmoday_helmet2",0)], itp_type_head_armor, 0, 999, weight(2.5)|abundance(100)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["ms_helmet_dark_b", "Dark Horned Warmask", [("sp_helm1",0)], itp_type_head_armor, 0, 999, weight(2.5)|abundance(100)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],

["ms_helmet_assasin_a", "Assasin Helmet", [("assassin_helmet",0)], itp_type_head_armor, 0, 699, weight(1)|abundance(100)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["ms_helmet_assasin_a2", "Assasin Helmet", [("assassin_helmet2",0)], itp_type_head_armor, 0, 799, weight(1)|abundance(100)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],

["ms_helmet_ghost", "Ghost Face", [("demon_hood",0)], itp_type_head_armor, 0, 9999, weight(1)|abundance(0)|head_armor(80)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["ms_helmet_golem", "Bronze Golem Head", [("g_helm_spak2",0)], itp_type_head_armor, 0, 9999, weight(1)|abundance(0)|head_armor(80)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["ms_helmet_heretic", "Heretic Helmet", [("glowing_helmet",0),("glowing_helmet.1",0)], itp_type_head_armor, 0, 9999, weight(1)|abundance(0)|head_armor(80)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["ms_helmet_skeleton", "Skullknight Helmet", [("scullhead4",0)], itp_type_head_armor, 0, 9999, weight(1)|abundance(0)|head_armor(80)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],

["ms_helmet_otherside_a", "Otherside Hunter Full Helmet with decorations", [("helmet_enforser",0),("helmet_enforser.1",0)], itp_type_head_armor, 0, 4569, weight(3)|abundance(0)|head_armor(60)|body_armor(0)|leg_armor(0)|difficulty(15) ,imodbits_plate ],
["ms_helmet_otherside_a2", "Otherside Hunter Full Helmet", [("helmet_enforser2",0)], itp_type_head_armor, 0, 4569, weight(3)|abundance(0)|head_armor(60)|body_armor(0)|leg_armor(0)|difficulty(15) ,imodbits_plate ],

["ms_helmet_darklord_a", "Darklord Helmet with Decorations", [("twilighthelm",0)], itp_type_head_armor, 0, 6999, weight(3)|abundance(0)|head_armor(69)|body_armor(0)|leg_armor(0)|difficulty(15) ,imodbits_plate ],
["ms_helmet_darklord_a2", "Darklord Helmet", [("twilighthelm2",0)], itp_type_head_armor, 0, 6999, weight(3)|abundance(0)|head_armor(69)|body_armor(0)|leg_armor(0)|difficulty(15) ,imodbits_plate ],

["ms_armor_plate_a", "Full Plate with Shoulder Guards", [("2full_plate_armor",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,2099 , weight(27)|abundance(70)|head_armor(0)|body_armor(56)|leg_armor(24)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_5] ], 
["ms_armor_plate_b", "Full Bronze Plate", [("splate_armor",0)], itp_type_body_armor|itp_covers_legs,0 ,2099 , weight(27)|abundance(5)|head_armor(0)|body_armor(56)|leg_armor(24)|difficulty(9) ,imodbits_armor ], 
["ms_armor_plate_c", "Full Plate with mail Skirt", [("splate_armor2",0)], itp_type_body_armor|itp_covers_legs,0 ,4999 , weight(27)|abundance(5)|head_armor(0)|body_armor(68)|leg_armor(36)|difficulty(9) ,imodbits_armor ], 

["ms_armor_bear", "Bear Warrior Armor", [("bear_warrior",0)], itp_type_body_armor|itp_covers_legs,0 ,1499 , weight(21)|abundance(25)|head_armor(0)|body_armor(49)|leg_armor(16)|difficulty(9) ,imodbits_armor ], 

["ms_armor_mamluke", "Elite Mamluke Mail", [("elite_cavalary",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1499 , weight(21)|abundance(25)|head_armor(0)|body_armor(55)|leg_armor(25)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_11] ], 

["ms_armor_dark_robe_a", "Cultist Robe", [("demonrobe",0)], itp_type_body_armor|itp_covers_legs,0 ,239 , weight(8)|abundance(5)|head_armor(0)|body_armor(21)|leg_armor(9)|difficulty(0) ,imodbits_armor ], 

["ms_armor_dark_a", "Dark Lord Armor", [("dark_lord_armor",0)], itp_type_body_armor|itp_covers_legs,0 ,9999 , weight(15)|abundance(25)|head_armor(4)|body_armor(75)|leg_armor(38)|difficulty(18) ,imodbits_armor ], 
["ms_armor_dark_a2", "Dark Lord Armor", [("dark_lord_armor2",0)], itp_type_body_armor|itp_covers_legs,0 ,9999 , weight(15)|abundance(25)|head_armor(4)|body_armor(75)|leg_armor(38)|difficulty(18) ,imodbits_armor ], 
["ms_armor_dark_b", "Dark Lord Armor", [("twiligh_armor",0)], itp_type_body_armor|itp_covers_legs,0 ,9999 , weight(15)|abundance(25)|head_armor(0)|body_armor(75)|leg_armor(38)|difficulty(18) ,imodbits_armor ], 

["ms_armor_heretic", "Heretic Armor", [("glowing_armor",0),("glowing_armor.1",0)], itp_type_body_armor|itp_covers_legs,0 ,9999 , weight(20)|abundance(5)|head_armor(0)|body_armor(80)|leg_armor(40)|difficulty(21) ,imodbits_armor ],

["ms_armor_doom_cult_a", "Doomsday Cult Armor on Jerkin", [("g_reinf_jerkin",0),("g_reinf_jerkin.1",0)], itp_type_body_armor|itp_covers_legs,0 ,3599 , weight(28)|abundance(5)|head_armor(0)|body_armor(59)|leg_armor(25)|difficulty(15) ,imodbits_armor ],
["ms_armor_doom_cult_b", "Doomsday Cult Armor on Tabard", [("g_tabard_a",0),("g_tabard_a.1",0)], itp_type_body_armor|itp_covers_legs,0 ,3599 , weight(28)|abundance(5)|head_armor(0)|body_armor(59)|leg_armor(25)|difficulty(15) ,imodbits_armor ],
["ms_armor_doom_cult_c", "Doomsday Cult Coat of Plates", [("spak_coat_of_plates_b",0),("spak_coat_of_plates_b.1",0)], itp_type_body_armor|itp_covers_legs,0 ,4099 , weight(28)|abundance(5)|head_armor(0)|body_armor(64)|leg_armor(30)|difficulty(17) ,imodbits_armor ],
["ms_armor_doom_cult_c2", "Doomsday Cult Coat of Plates", [("spak_coat_of_plates_d",0),("spak_coat_of_plates_d.1",0)], itp_type_body_armor|itp_covers_legs,0 ,4099 , weight(28)|abundance(5)|head_armor(0)|body_armor(64)|leg_armor(30)|difficulty(17) ,imodbits_armor ],
["ms_armor_doom_cult_c3", "Doomsday Cult Coat of Plates", [("spak_coat_of_plates_e",0),("spak_coat_of_plates_e.1",0)], itp_type_body_armor|itp_covers_legs,0 ,4099 , weight(28)|abundance(5)|head_armor(0)|body_armor(64)|leg_armor(30)|difficulty(17) ,imodbits_armor ],
["ms_armor_doom_cult_c4", "Doomsday Cult Coat of Plates", [("spak_coat_of_plates_f",0),("spak_coat_of_plates_f.1",0)], itp_type_body_armor|itp_covers_legs,0 ,4099 , weight(28)|abundance(5)|head_armor(0)|body_armor(64)|leg_armor(30)|difficulty(17) ,imodbits_armor ],
["ms_armor_doom_cult_c5", "Doomsday Cult Priest Coat of Plates", [("spak_coat_of_plates_f",0),("spak_coat_of_plates_f.1",0)], itp_type_body_armor|itp_covers_legs,0 ,4099 , weight(28)|abundance(5)|head_armor(0)|body_armor(64)|leg_armor(30)|difficulty(17) ,imodbits_armor ],

["ms_bear_greaves", "Bear Greves", [("bear_boots",0)], itp_type_foot_armor|itp_attach_armature,0, 999 , weight(2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(32)|difficulty(0) ,imodbits_armor ],

["ms_doom_cult_greaves_a", "Doomsday Cult Greaves", [("g_iron_greaves_a",0),("g_iron_greaves_a.1",0)], itp_type_foot_armor|itp_attach_armature,0, 999 , weight(2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(32)|difficulty(0) ,imodbits_armor ],
["ms_doom_cult_greaves_b", "Doomsday Cult Greaves", [("g_mail_boots_a",0),("g_mail_boots_a.1",0)], itp_type_foot_armor|itp_attach_armature,0, 999 , weight(2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(32)|difficulty(0) ,imodbits_armor ],
["ms_doom_cult_greaves_c", "Doomsday Cult Greaves", [("g_mail_chausses_a",0),("g_mail_chausses_a.1",0)], itp_type_foot_armor|itp_attach_armature,0, 999 , weight(2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(32)|difficulty(0) ,imodbits_armor ],

["ms_dark_boots_a", "Doom Lord Boots", [("twilight_boots",0)], itp_type_foot_armor|itp_attach_armature,0, 9999 , weight(2)|abundance(5)|head_armor(0)|body_armor(0)|leg_armor(45)|difficulty(15) ,imodbits_armor ],
["ms_demonic_boots_a", "Doom Lord Boots", [("demonic_boots",0),("demonic_boots.1",0)], itp_type_foot_armor|itp_attach_armature,0, 9999 , weight(2)|abundance(5)|head_armor(0)|body_armor(0)|leg_armor(45)|difficulty(15) ,imodbits_armor ],

["ms_doom_cult_gauntlets_a","Doom Cult Gauntlets", [("g_scale_gauntlets_a_L",0)], itp_type_hand_armor,0, 699, weight(0.75)|abundance(100)|body_armor(7)|difficulty(0),imodbits_armor],

["ms_bear_gauntlets","Bear Gauntlets", [("beargauntlets_L",0)], itp_type_hand_armor,0, 699, weight(0.75)|abundance(100)|body_armor(7)|difficulty(0),imodbits_armor],

["ms_dark_gauntlets_a","Doom Lord Gauntlets", [("twilight_gloves_L",0)], itp_type_hand_armor,0, 9999, weight(0.75)|abundance(5)|body_armor(15)|difficulty(12),imodbits_armor],
["ms_demonic_gauntlets_a","Heretic Gauntlets", [("demonic_gauntlets_L",0)], itp_type_hand_armor,0, 9999, weight(0.75)|abundance(5)|body_armor(15)|difficulty(12),imodbits_armor],

["surcoat_over_mail_undead_a", "Surcoat over Mail", [("surcoat_over_mail_undead_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1720 , weight(22)|abundance(1)|head_armor(0)|body_armor(43)|leg_armor(14)|difficulty(7) ,imodbits_armor ],
["surcoat_over_mail_undead_b", "Surcoat over Mail", [("surcoat_over_mail_undead_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1720 , weight(22)|abundance(1)|head_armor(0)|body_armor(43)|leg_armor(14)|difficulty(7) ,imodbits_armor ],

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
