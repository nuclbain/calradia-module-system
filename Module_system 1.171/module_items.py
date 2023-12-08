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

["pilgrim_disguise", "Pilgrim Disguise", [("monie_a",0)], 0| itp_type_body_armor |itp_covers_legs |itp_civilian ,0, 25 , weight(2)|abundance(100)|head_armor(0)|body_armor(19)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["pilgrim_hood", "Pilgrim Hood", [("Pilgrim_Hood_A",0)], 0| itp_type_head_armor |itp_civilian  ,0, 35 , weight(1.25)|abundance(100)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

# ARMOR
#handwear
["leather_gloves","Leather Gloves", [("gloves_a_L",0)], itp_merchandise|itp_type_hand_armor,0, 90, weight(0.25)|abundance(120)|body_armor(2)|difficulty(0),imodbits_cloth],
["old_leather_gloves","Old Gloves", [("dethertir_gloves_L",0)], itp_merchandise|itp_type_hand_armor,0, 51, weight(0.25)|abundance(100)|body_armor(1)|difficulty(0),imodbits_cloth, [], [fac_kingdom_1]],
["decorated_leather_gloves_a","Decorated Leather Gloves", [("gloves_lord_L", 0)], itp_type_hand_armor|itp_merchandise, 0,125, weight(0.75)|abundance(100)|body_armor(3), imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_6]],
["decorated_leather_gloves_b","Royal Leather Gloves", [("gloves_king_L", 0)], itp_type_hand_armor|itp_merchandise, 0,125, weight(0.75)|abundance(100)|body_armor(3), imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_6]],

["mt_leather_gloves_a","Leather_gloves", [("glove4_L",0)], itp_merchandise|itp_type_hand_armor,0, 299, weight(0.75)|abundance(100)|body_armor(2)|difficulty(0),imodbits_cloth, [], [fac_kingdom_5, fac_kingdom_9, fac_kingdom_10]],
["mail_mittens","Mail Mittens", [("gauntlets_crysader_L",0)], itp_merchandise|itp_type_hand_armor,0, 350, weight(0.5)|abundance(100)|body_armor(4)|difficulty(0),imodbits_armor],
["old_mail_gloves","Old Mail Gloves", [("dethertir_gauntlets_L",0)], itp_merchandise|itp_type_hand_armor,0, 399, weight(0.75)|abundance(100)|body_armor(5)|difficulty(0),imodbits_armor, [], [fac_kingdom_1]],

["eastern_scale_gloves_a","Eastern Scale Gloves", [("gauntlets_arabs_a_L", 0)], itp_type_hand_armor|itp_merchandise, 0,710, weight(0.75)|abundance(100)|body_armor(5), imodbit_lordly, [], [fac_kingdom_6]],
["eastern_scale_gloves_b","Eastern Decorated Scale Gloves", [("gauntlets_arabs_b_L", 0)], itp_type_hand_armor|itp_merchandise, 0,919, weight(0.75)|abundance(100)|body_armor(6), imodbit_lordly, [], [fac_kingdom_6]],
["scale_gauntlets","Scale Gauntlets", [("scale_gauntlets_b_L",0)], itp_merchandise|itp_type_hand_armor,0, 710, weight(0.75)|abundance(100)|body_armor(5)|difficulty(0),imodbits_armor],
["lamellar_gauntlets","Lamellar Gauntlets", [("scale_gauntlets_a_L",0)], itp_merchandise|itp_type_hand_armor,0, 910, weight(0.9)|abundance(100)|body_armor(6)|difficulty(0),imodbits_armor],
["mt_scale_gloves_a","Scale Gloves", [("glove5_L",0)], itp_merchandise|itp_type_hand_armor,0, 559, weight(0.75)|abundance(100)|body_armor(5)|difficulty(0),imodbits_armor, [], [fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_10]],
["mt_scale_gloves_b","Scale Gloves", [("glove6_L",0)], itp_merchandise|itp_type_hand_armor,0, 559, weight(0.75)|abundance(100)|body_armor(5)|difficulty(0),imodbits_armor, [], [fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_9, fac_kingdom_10]],

["gauntlets","Gauntlets", [("gauntlets_L",0),("gauntlets_L",imodbit_reinforced)], itp_merchandise|itp_type_hand_armor,0, 1040, weight(1.0)|abundance(100)|body_armor(7)|difficulty(0),imodbits_armor],

["mt_gauntlets_a","Plate Gauntlets Gothic", [("glove1_L",0)], itp_merchandise|itp_type_hand_armor,0, 799, weight(0.75)|abundance(100)|body_armor(6)|difficulty(0),imodbits_armor, [], [fac_kingdom_10, fac_kingdom_9]],
["mt_gauntlets_a2","Plate Gauntlets Gothic", [("glove2_L",0)], itp_merchandise|itp_type_hand_armor,0, 799, weight(0.75)|abundance(100)|body_armor(6)|difficulty(0),imodbits_armor, [], [fac_kingdom_10, fac_kingdom_9]],
["mt_gauntlets_b","Mail Gloves", [("glove3_L",0)], itp_merchandise|itp_type_hand_armor,0, 599, weight(0.75)|abundance(100)|body_armor(5)|difficulty(0),imodbits_armor, [], [fac_kingdom_10, fac_kingdom_9]],

["m_gloves_a","Leather Gauntlets", [("leather_gauntlet_L",0)], itp_merchandise|itp_type_hand_armor,0, 499, weight(0.5)|abundance(100)|body_armor(4)|difficulty(0),imodbits_cloth],

["m_gauntlets_a","Plate Gauntlets", [("demi_gauntlets_L",0)], itp_merchandise|itp_type_hand_armor,0, 799, weight(0.75)|abundance(100)|body_armor(6)|difficulty(0),imodbits_armor],
["m_gauntlets_b","Plate Gauntlets", [("finger_gauntlets_L",0)], itp_merchandise|itp_type_hand_armor,0, 849, weight(0.85)|abundance(100)|body_armor(7)|difficulty(0),imodbits_armor],

#footwear
["civil_poor_boots_a","Sandals", [("civil_poor_boots_a", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,75, weight(1)|abundance(100)|leg_armor(1), imodbits_cloth, [], [fac_kingdom_6]],

["wrapping_boots", "Wrapping Boots", [("wrapping_boots_a",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 3 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(3)|difficulty(0) ,imodbits_cloth ],
["woolen_hose", "Woolen Hose", [("hose_default",0),("hose_default.1",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
["blue_hose", "Blue Hose", [("hose_default_blue",0),("hose_default_blue.1",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 11 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],

["m_hose_a", "Woolen Hose", [("hosen_blue",0), ("hosen_blue.1",0)], itp_merchandise|itp_type_foot_armor|itp_civilian|itp_attach_armature, 0, 12, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(4)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_7, fac_kingdom_5, fac_kingdom_9, fac_kingdom_10] ],
["m_hose_b", "Woolen Hose", [("hosen_brown",0), ("hosen_brown.1",0)], itp_merchandise|itp_type_foot_armor|itp_civilian|itp_attach_armature, 0, 12, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(4)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_7, fac_kingdom_5, fac_kingdom_9, fac_kingdom_10] ],
["m_hose_c", "Woolen Hose", [("hosen_green",0), ("hosen_green.1",0)], itp_merchandise|itp_type_foot_armor|itp_civilian|itp_attach_armature, 0, 12, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(4)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_7, fac_kingdom_5, fac_kingdom_9, fac_kingdom_10] ],
["m_hose_d", "Woolen Hose", [("hosen_red",0), ("hosen_red.1",0)], itp_merchandise|itp_type_foot_armor|itp_civilian|itp_attach_armature, 0, 12, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(4)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_7, fac_kingdom_5, fac_kingdom_9, fac_kingdom_10] ],
["m_hose_e", "Woolen Hose", [("hosen_yellow",0), ("hosen_yellow.1",0)], itp_merchandise|itp_type_foot_armor|itp_civilian|itp_attach_armature, 0, 12, weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(4)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_7, fac_kingdom_5, fac_kingdom_9, fac_kingdom_10] ],

["mkk_boots_common_a","Eastern Light Boots", [("boots_tyrk_a", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,99, weight(1)|abundance(100)|leg_armor(10), imodbits_cloth, [], [fac_kingdom_6]],
["mkk_boots_common_b","Eastern Light Boots", [("boots_tyrk_b", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,99, weight(1)|abundance(100)|leg_armor(10), imodbits_cloth, [], [fac_kingdom_6]],
["mkk_boots_common_c","Eastern Light Boots", [("boots_tyrk_c", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,99, weight(1)|abundance(100)|leg_armor(10), imodbits_cloth, [], [fac_kingdom_6]],

["mkk_boots_a","Desert Boots", [("saracin_light_boot_a", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,159, weight(1)|abundance(100)|leg_armor(12), imodbits_cloth, [], [fac_kingdom_6]],
["mkk_boots_b","Desert Boots", [("saracin_light_boot_b", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,159, weight(1)|abundance(100)|leg_armor(12), imodbits_cloth, [], [fac_kingdom_6]],

["hunter_boots", "Hunter Boots", [("hunter_boots_a",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature,0,
 19 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
["hide_boots", "Hide Boots", [("hide_boots_a",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 34 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["ankle_boots", "Ankle Boots", [("hosen_yellow",0), ("hosen_yellow.1",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 75 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["m_swadia_light_boots_a", "Ankle Boots", [("boot_light_crusader_a",0)], itp_type_foot_armor|itp_merchandise   ,0, 100 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(4)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_light_boots_b", "Ankle Boots", [("boot_light_crusader_b",0)], itp_type_foot_armor|itp_merchandise   ,0, 100 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(4)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],
["nomad_boots", "Nomad Boots", [("nomad_boots_new",0),("nomad_boots_new.1",0),("nomad_boots_new.2",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 90 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(14)|difficulty(0) ,imodbits_cloth ],

["m_swadia_milita_boots_a", "Light Leather Boots", [("boot_light_crusader_c",0)], itp_type_foot_armor|itp_merchandise   ,0, 150 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(7)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_4, fac_kingdom_12] ],
["m_swadia_milita_boots_b", "Light Leather Boots", [("boot_light_crusader_d",0)], itp_type_foot_armor|itp_merchandise   ,0, 150 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(7)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_1, fac_kingdom_4, fac_kingdom_12] ],

["adid_infantry_boots_a", "Adid infantry Boots", [("boot_average_crusader_a",0)], itp_type_foot_armor|itp_merchandise   ,0, 200 , weight(2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_11] ],
["adid_infantry_boots_b", "Adid infantry Boots", [("boot_average_crusader_b",0)], itp_type_foot_armor|itp_merchandise   ,0, 200 , weight(2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_11] ],

["m_swadia_leather_boots_a", "Short Leather Boots", [("boot_average_crusader_c",0)], itp_type_foot_armor|itp_merchandise   ,0, 150 , weight(2.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(14)|difficulty(0) ,imodbits_cloth,[], [] ],
["m_swadia_leather_boots_b", "Short Leather Boots", [("boot_average_crusader_d",0)], itp_type_foot_armor|itp_merchandise   ,0, 150 , weight(2.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(14)|difficulty(0) ,imodbits_cloth,[], [] ],

["leather_boots", "Leather Boots", [("leather_boots_default",0), ("leather_boots_default.1",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 174 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth ],
["m_leather_boots_a", "Leather Boots", [("leather_boots",0), ("leather_boots.1",0)], itp_merchandise|itp_type_foot_armor|itp_civilian|itp_attach_armature,0, 179 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth],
["civil_rich_boots_a","Eastern Leather Boots", [("civil_rich_Boots_a", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,199, weight(1)|abundance(100)|leg_armor(18), imodbits_cloth, [], [fac_kingdom_6, fac_kingdom_11]],
["civil_rich_boots_b","Eastern Leather Boots", [("civil_rich_Boots_b", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,199, weight(1)|abundance(100)|leg_armor(18), imodbits_cloth, [], [fac_kingdom_6, fac_kingdom_11]],

["mkk_leather_boots_a","Solarian Leather Boots", [("saracin_medium_boot_a", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,399, weight(1)|abundance(100)|leg_armor(20), imodbits_cloth, [], [fac_kingdom_6]],
["mkk_leather_boots_b","Solarian Leather Boots", [("saracin_medium_boot_b", 0)], itp_type_foot_armor|itp_attach_armature|itp_civilian, 0,399, weight(1)|abundance(100)|leg_armor(20), imodbits_cloth, [], [fac_kingdom_6]],

["mkk_heavy_boots_a","Solarian Heavy Boots", [("saracin_hard_boot_a", 0)], itp_type_foot_armor|itp_attach_armature, 0,1199, weight(2)|abundance(100)|leg_armor(34), imodbits_plate, [], [fac_kingdom_6]],
["mkk_heavy_boots_b","Solarian Heavy Boots", [("saracin_hard_boot_b", 0)], itp_type_foot_armor|itp_attach_armature, 0,1199, weight(2)|abundance(100)|leg_armor(34), imodbits_plate, [], [fac_kingdom_6]],

["m_greaves_a", "Steel Greaves", [("steel_greaves",0), ("steel_greaves.1",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature,0, 1099 , weight(2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(36)|difficulty(0) ,imodbits_armor ],
["m_greaves_b", "Light Steel Greaves", [("steel_greaves2",0), ("steel_greaves2.1",0), ("steel_greaves2.2",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature,0, 1099 , weight(2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(36)|difficulty(0) ,imodbits_armor ],

["mail_chausses", "Mail Chausses", [("boot16",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature  ,0,
 530 , weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(24)|difficulty(0) ,imodbits_armor ],

["eastern_mail_boots_a", "Eastern Mail Boots", [("shoes_crusader",0)], itp_type_foot_armor|itp_merchandise   ,0, 488 , weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_11] ],
["eastern_mail_boots_b", "Eastern Mail Boots", [("shoes_crusader_knight",0)], itp_type_foot_armor|itp_merchandise   ,0, 501 , weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_11] ],

["mt_greaves_a", "Steel Greaves", [("boot1",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature,0, 1099 , weight(2)|abundance(5)|head_armor(0)|body_armor(0)|leg_armor(36)|difficulty(0) ,imodbits_armor ],
["mt_greaves_b", "Steel Greaves", [("boot10",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature,0, 1099 , weight(2)|abundance(5)|head_armor(0)|body_armor(0)|leg_armor(36)|difficulty(0) ,imodbits_armor ],
["mt_greaves_c", "Steel Greaves with Scale", [("boot12",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature,0, 1099 , weight(2)|abundance(5)|head_armor(0)|body_armor(0)|leg_armor(36)|difficulty(0) ,imodbits_armor ],
["mt_greaves_f", "Steel Greaves", [("boot3",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature,0, 999 , weight(2)|abundance(5)|head_armor(0)|body_armor(0)|leg_armor(32)|difficulty(0) ,imodbits_armor ],
["mt_greaves_g", "Steel Greaves", [("boot5",0)], itp_merchandise|itp_type_foot_armor|itp_attach_armature,0, 999 , weight(2)|abundance(5)|head_armor(0)|body_armor(0)|leg_armor(32)|difficulty(0) ,imodbits_armor ],

["splinted_greaves", "Light Splinted Greaves", [("Greaves_A",0), ("Greaves_A.1",0), ("Greaves_A.2",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 455 , weight(2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(24)|difficulty(7) ,imodbits_armor ],
["splinted_leather_greaves", "Splinted Greaves", [("Greaves_B",0), ("Greaves_B.1",0), ("Greaves_B.2",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,883 , weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(29)|difficulty(0) ,imodbits_armor ],

["mail_boots", "Mail Boots", [("mail_boots_a",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature  ,0,
 1250 , weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(31)|difficulty(8) ,imodbits_armor ],
["iron_greaves", "Iron Greaves", [("iron_greaves_a",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
 1770 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_armor ],
["black_greaves", "Black Greaves", [("black_greaves",0)], itp_type_foot_armor  | itp_attach_armature,0,
 2361 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(35)|difficulty(0) ,imodbits_armor ],
["khergit_leather_boots", "Khergit Leather Boots", [("khergit_leather_boots",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 120 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(18)|difficulty(0) ,imodbits_cloth ],
["sarranid_boots_a", "Eastern Shoes", [("sarranid_shoes",0)], itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 30 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["sarranid_boots_b", "Eastern Leather Boots", [("sarranid_boots",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 120 , weight(2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth ],
["sarranid_boots_c", "Plated Boots", [("sarranid_camel_boots",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 280 , weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_plate ],
["sarranid_boots_d", "Eastern Mail Boots", [("sarranid_mail_chausses",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
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
["sarranid_lady_dress", "Eastern Lady Dress", [("sarranid_lady_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["sarranid_lady_dress_b", "Eastern Lady Dress", [("sarranid_lady_dress_b",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["sarranid_common_dress", "Eastern Dress", [("sarranid_common_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["sarranid_common_dress_b", "Eastern Dress", [("sarranid_common_dress_b",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["courtly_outfit", "Courtly Outfit", [("Rich_Surcoat_B",0),("Rich_Surcoat_B.1",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["nobleman_outfit", "Nobleman Outfit", [("Rich_Surcoat_A",0),], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(12)|difficulty(0) ,imodbits_cloth ], 
["nobleman_outfit_a", "Nobleman Outfit", [("Rich_Surcoat_C",0),], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(12)|difficulty(0) ,imodbits_cloth ], 
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
["shirt", "Shirt", [("Shirt_B",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 3 , weight(1)|abundance(100)|head_armor(0)|body_armor(5)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
 #NEW: was "linen_tunic"
["linen_tunic", "Linen Tunic", [("shirt_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
 #NEW was cvl_costume_a
["short_tunic", "Red Tunic", [("rich_tunic_a",0)], itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_cloth ], 
["tunic_with_green_cape", "Peasant Tunic", [("Peasant_Tunic_A",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ], 

#TODO:
 ["red_shirt", "Red Shirt", [("rich_tunic_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
 ["red_tunic", "Red Tunic", [("arena_tunicR_new",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],

 ["green_tunic", "Green Tunic", [("arena_tunicG_new",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
 ["blue_tunic", "Blue Tunic", [("arena_tunicB_new",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
["robe", "Robe", [("monie_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 31 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
#NEW: was coarse_tunic
["coarse_tunic", "Tunic with vest", [("coarse_tunic_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 47 , weight(2)|abundance(100)|head_armor(0)|body_armor(11)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["leather_apron", "Peasant Leather Vest", [("Peasant_Tunic_B",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 61 , weight(3)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(7)|difficulty(0) ,imodbits_cloth ],
#NEW: was tabard_a
["tabard", "Tabard", [("tabard_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 107 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
#NEW: was leather_vest
["leather_vest", "Leather Vest", [("leather_vest_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 146 , weight(4)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(7)|difficulty(0) ,imodbits_cloth ],
["steppe_armor", "Steppe Armor", [("lamellar_leather",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 195 , weight(5)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],

["blue_gambeson", "Blue & Red Gambeson", [("Gambeson_Two_Tones_A",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 270 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
["red_gambeson", "Red & Yellow Gambeson", [("Gambeson_Two_Tones_B",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
["gambeson", "Light Blue Gambeson", [("Gambeson_One_Tone_A",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 260 , weight(5)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
["m_padded_dark_a", "Black Padded Vest", [("Gambeson_One_Tone_B",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 299 , weight(10)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(7)|difficulty(0) ,imodbits_armor, [], [] ],
["m_padded_dark_b", "Gray Padded Vest", [("Gambeson_One_Tone_C",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 299 , weight(10)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(7)|difficulty(0) ,imodbits_armor, [], [] ],
["m_padded_dark_c", "Light Gray Padded Vest", [("Gambeson_One_Tone_D",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 299 , weight(10)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(7)|difficulty(0) ,imodbits_armor, [], [] ],
["m_padded_dark_a_mail", "Black Padded Vest with Mail", [("Gambeson_Mail_A",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 461 , weight(10)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(7)|difficulty(0) ,imodbits_armor, [], [] ],

#NEW: was aketon_a
["padded_cloth", "Aketon", [("Padded_Cloth_Cloacked_A",0),("Padded_Cloth_Cloacked_A.1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 297 , weight(11)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
#NEW:
 ["aketon_green", "Padded Cloth", [("padded_cloth_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 297 , weight(11)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

["m_iron_crown_aketon_a", "Iron Crown Aketon", [("Iron_Crown_Aketon_A",0), ("Iron_Crown_Aketon_A.1",0), ("Iron_Crown_Aketon_A.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,211 , weight(10)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_4] ],
["m_iron_crown_aketon_b", "Iron Crown Aketon", [("Iron_Crown_Aketon_B",0), ("Iron_Crown_Aketon_B.1",0), ("Iron_Crown_Aketon_B.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,211 , weight(10)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_4] ],

["m_iron_crown_scale_vest_a", "Iron Crown Scale Vest", [("Iron_Crown_Scale_Vest_A",0), ("Iron_Crown_Scale_Vest_A.1",0), ("Iron_Crown_Scale_Vest_A.2",0),("Iron_Crown_Scale_Vest_A.3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,381 , weight(15)|abundance(100)|head_armor(0)|body_armor(31)|leg_armor(6)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_4] ],
["m_iron_crown_scale_vest_b", "Iron Crown Scale Vest", [("Iron_Crown_Scale_Vest_B",0), ("Iron_Crown_Scale_Vest_B.1",0), ("Iron_Crown_Scale_Vest_B.2",0),("Iron_Crown_Scale_Vest_B.3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,407 , weight(15)|abundance(100)|head_armor(0)|body_armor(33)|leg_armor(6)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_4] ],
["m_iron_crown_scale_vest_c", "Iron Crown Scale Vest", [("Iron_Crown_Scale_Vest_C",0), ("Iron_Crown_Scale_Vest_C.1",0), ("Iron_Crown_Scale_Vest_C.2",0),("Iron_Crown_Scale_Vest_C.3",0),("Iron_Crown_Scale_Vest_C.4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,497 , weight(16)|abundance(100)|head_armor(0)|body_armor(36)|leg_armor(6)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_4] ],

["m_iron_crown_brigandine_a", "Iron Crown Brigandine", [("Iron_Crown_Brigandine_A",0), ("Iron_Crown_Brigandine_A.1",0), ("Iron_Crown_Brigandine_A.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,471 , weight(16)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(6)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_4] ],
["m_iron_crown_brigandine_b", "Iron Crown Brigandine", [("Iron_Crown_Brigandine_B",0), ("Iron_Crown_Brigandine_B.1",0), ("Iron_Crown_Brigandine_B.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,499 , weight(16)|abundance(100)|head_armor(0)|body_armor(36)|leg_armor(6)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_4] ],

["m_iron_crown_brigandine_mail_a", "Iron Crown Brigandine with Mail", [("Iron_Crown_Brigandine_C",0), ("Iron_Crown_Brigandine_C.1",0), ("Iron_Crown_Brigandine_C.2",0), ("Iron_Crown_Brigandine_C.3",0), ("Iron_Crown_Brigandine_C.4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,638 , weight(18)|abundance(100)|head_armor(0)|body_armor(41)|leg_armor(9)|difficulty(7) ,imodbits_armor, [], [fac_kingdom_4] ],
["m_iron_crown_brigandine_mail_b", "Iron Crown Brigandine with Mail", [("Iron_Crown_Brigandine_D",0), ("Iron_Crown_Brigandine_D.1",0), ("Iron_Crown_Brigandine_D.2",0), ("Iron_Crown_Brigandine_D.3",0), ("Iron_Crown_Brigandine_D.4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,819 , weight(19)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(16)|difficulty(7) ,imodbits_armor, [], [fac_kingdom_4] ],

["m_iron_crown_scale_a", "Iron Crown Scale Armor", [("Iron_Crown_Scale_A",0), ("Iron_Crown_Scale_A.1",0), ("Iron_Crown_Scale_A.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1299 , weight(19)|abundance(100)|head_armor(0)|body_armor(47)|leg_armor(17)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_4] ],
["m_iron_crown_scale_b", "Iron Crown Scale Armor", [("Iron_Crown_Scale_B",0), ("Iron_Crown_Scale_B.1",0), ("Iron_Crown_Scale_B.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1569 , weight(21)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(20)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_4] ],

["m_celestial_padded_cloth_a", "Padded Cloth", [("Celestial_Padded_Cloth_A",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 297 , weight(11)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_3] ],
["m_celestial_mail_a", "Mail Shirt", [("Celestial_Padded_Cloth_Mail_A",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 359 , weight(16)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(8)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_3] ],

["m_celestial_breastplate_a", "Celestial Breastplate", [("Celestial_Breastplate_A",0),("Celestial_Breastplate_A.1",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 1569 , weight(15)|abundance(100)|head_armor(0)|body_armor(32)|leg_armor(8)|difficulty(6) ,imodbits_armor, [], [fac_kingdom_3] ],
["m_celestial_breastplate_b", "Celestial Breastplate on Mail", [("Celestial_Breastplate_B",0),("Celestial_Breastplate_B.1",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 1672 , weight(18)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(11)|difficulty(7) ,imodbits_armor, [], [fac_kingdom_3] ],
["m_celestial_breastplate_c", "Celestial Breastplate on Mail", [("Celestial_Breastplate_C",0),("Celestial_Breastplate_C.1",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 1672 , weight(18)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(11)|difficulty(7) ,imodbits_armor, [], [fac_kingdom_3] ],

["m_celestial_breastplate_heavy_a", "Celestial Heavy Breastplate", [("Celestial_Breastplate_Heavy_A",0),("Celestial_Breastplate_Heavy_A.1",0), ("Celestial_Breastplate_Heavy_A.2",0), ("Celestial_Breastplate_Heavy_A.3",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 2133 , weight(21)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(16)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_3] ],
["m_celestial_breastplate_heavy_b", "Celestial Heavy Breastplate", [("Celestial_Breastplate_Heavy_B",0),("Celestial_Breastplate_Heavy_B.1",0), ("Celestial_Breastplate_Heavy_B.2",0), ("Celestial_Breastplate_Heavy_B.3",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 2233 , weight(21)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(21)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_3] ],

["m_celestial_plate_a", "Celestial Plate Armor", [("Celestial_Plate_Armor_A",0),("Celestial_Plate_Armor_A.1",0), ("Celestial_Plate_Armor_A.2",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 2233 , weight(22)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(21)|difficulty(10) ,imodbits_armor, [], [fac_kingdom_3] ],
["m_celestial_plate_b", "Celestial Plate Armor", [("Celestial_Plate_Armor_B",0),("Celestial_Plate_Armor_B.1",0), ("Celestial_Plate_Armor_B.2",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 2233 , weight(22)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(21)|difficulty(10) ,imodbits_armor, [], [fac_kingdom_3] ],

["m_celestial_plate_heavy_a", "Celestial Heavy Plate Armor", [("Celestial_Heavy_Plate_A",0),("Celestial_Heavy_Plate_A.1",0), ("Celestial_Heavy_Plate_A.2",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 2233 , weight(22)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(21)|difficulty(10) ,imodbits_armor, [], [fac_kingdom_3] ],

["m_alpine_aketon_a", "Alpine Aketon", [("Alpine_Dominion_Aketon_A",0), ("Alpine_Dominion_Aketon_A.1",0), ("Alpine_Dominion_Aketon_A.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,251 , weight(12)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_5] ],
["m_alpine_aketon_b", "Alpine Aketon", [("Alpine_Dominion_Aketon_B",0), ("Alpine_Dominion_Aketon_B.1",0), ("Alpine_Dominion_Aketon_B.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,251 , weight(12)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_5] ],

["m_alpine_padded_cloth_a", "Alpine Outfit", [("Alpine_Padded_Cloth_Cloacked_A",0),("Alpine_Padded_Cloth_Cloacked_A.1",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs ,0, 390 , weight(7)|abundance(100)|head_armor(0)|body_armor(23)|leg_armor(9)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_5]],
["m_alpine_padded_cloth_b", "Alpine Outfit", [("Alpine_Padded_Cloth_Cloacked_B",0),("Alpine_Padded_Cloth_Cloacked_B.1",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs ,0, 390 , weight(7)|abundance(100)|head_armor(0)|body_armor(23)|leg_armor(9)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_5]],
["m_alpine_padded_cloth_lamellar_a", "Alpine Outfit with Lamellar Vest", [("Alpine_Padded_Cloth_Cuirass_A",0),("Alpine_Padded_Cloth_Cuirass_A.1",0),("Alpine_Padded_Cloth_Cuirass_A.2",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs ,0, 455 , weight(12)|abundance(100)|head_armor(0)|body_armor(28)|leg_armor(9)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_5]],
["m_alpine_padded_cloth_lamellar_b", "Alpine Outfit with Lamellar Vest", [("Alpine_Padded_Cloth_Cuirass_B",0),("Alpine_Padded_Cloth_Cuirass_B.1",0),("Alpine_Padded_Cloth_Cuirass_B.2",0),("Alpine_Padded_Cloth_Cuirass_B.3",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs ,0, 579 , weight(15)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(9)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_5]],

["m_alpine_corrazina_a", "Alpine Corrazina Vest", [("Alpine_Dominion_Corrazina_A",0),("Alpine_Dominion_Corrazina_A.1",0),("Alpine_Dominion_Corrazina_A.2",0),("Alpine_Dominion_Corrazina_A.3",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs ,0, 619 , weight(15)|abundance(100)|head_armor(0)|body_armor(36)|leg_armor(13)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_5]],
["m_alpine_corrazina_b", "Alpine Corrazina Vest", [("Alpine_Dominion_Corrazina_B",0),("Alpine_Dominion_Corrazina_B.1",0),("Alpine_Dominion_Corrazina_B.2",0),("Alpine_Dominion_Corrazina_B.3",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs ,0, 659 , weight(15)|abundance(100)|head_armor(0)|body_armor(38)|leg_armor(13)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_5]],

["m_alpine_corrazina_full_a", "Alpine Corrazina", [("Alpine_Dominion_Corrazina_C",0),("Alpine_Dominion_Corrazina_C.1",0),("Alpine_Dominion_Corrazina_C.2",0),("Alpine_Dominion_Corrazina_C.3",0),("Alpine_Dominion_Corrazina_C.4",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs ,0, 769 , weight(17)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(15)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_5]],
["m_alpine_corrazina_full_b", "Alpine Corrazina", [("Alpine_Dominion_Corrazina_D",0),("Alpine_Dominion_Corrazina_D.1",0),("Alpine_Dominion_Corrazina_D.2",0),("Alpine_Dominion_Corrazina_D.3",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs ,0, 814 , weight(18)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(15)|difficulty(7) ,imodbits_armor, [], [fac_kingdom_5]],
["m_alpine_corrazina_full_c", "Alpine Corrazina", [("Alpine_Dominion_Corrazina_E",0),("Alpine_Dominion_Corrazina_E.1",0),("Alpine_Dominion_Corrazina_E.2",0),("Alpine_Dominion_Corrazina_E.3",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs ,0, 993 , weight(19)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(19)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_5]],

["m_alpine_full_plate_a", "Alpine Full Plate", [("Alpine_Dominion_Plate_A",0),("Alpine_Dominion_Plate_A.1",0),("Alpine_Dominion_Plate_A.2",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs ,0, 2349 , weight(24)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(22)|difficulty(10) ,imodbits_armor, [], [fac_kingdom_5]],


["rough_gambeson", "Rough Grey Gambeson", [("Chornovalley_Gambeson_A",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 290, weight(5)|abundance(100)|head_armor(0)|body_armor(24)|leg_armor(8)|difficulty(5) ,imodbits_cloth, [], [fac_kingdom_2] ],
["m_chornovalley_padded_cloth_a", "Padded Cloth", [("Chornovalley_Padded_Cloth_A",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 297 , weight(11)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_2] ],

["m_chornovalley_aketon_a", "Chornovalley Aketon", [("Chornovalley_Aketon_A",0), ("Chornovalley_Aketon_A.1",0), ("Chornovalley_Aketon_A.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,251 , weight(12)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_2] ],
["m_chornovalley_vest_a", "Chornovalley Leather Vest", [("Chornovalley_Leather_Vest_A",0), ("Chornovalley_Leather_Vest_A.1",0), ("Chornovalley_Leather_Vest_A.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,272 , weight(12)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_2] ],

["m_chornovalley_lamellar_vest_a", "Chornovalley Lamellar Vest", [("Chornovalley_Lamellar_A",0), ("Chornovalley_Lamellar_A.1",0), ("Chornovalley_Lamellar_A.2",0),("Chornovalley_Lamellar_A.3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,566 , weight(17)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(6)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_2] ],
["m_chornovalley_lamellar_vest_b", "Chornovalley Lamellar Vest", [("Chornovalley_Lamellar_B",0), ("Chornovalley_Lamellar_B.1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,641 , weight(18)|abundance(100)|head_armor(0)|body_armor(36)|leg_armor(12)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_2] ],
["m_chornovalley_lamellar_vest_c", "Chornovalley Lamellar Vest", [("Chornovalley_Lamellar_C",0), ("Chornovalley_Lamellar_C.1",0), ("Chornovalley_Lamellar_C.2",0), ("Chornovalley_Lamellar_C.3",0), ("Chornovalley_Lamellar_C.4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,633 , weight(18)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(6)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_2] ],
["m_chornovalley_lamellar_vest_d", "Chornovalley Lamellar Vest", [("Chornovalley_Lamellar_D",0), ("Chornovalley_Lamellar_D.1",0), ("Chornovalley_Lamellar_D.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,679 , weight(18)|abundance(100)|head_armor(0)|body_armor(38)|leg_armor(12)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_2] ],

["m_chornovalley_mail_a", "Chornovalley Mail", [("Chornovallery_Mail_A",0), ("Chornovallery_Mail_A.1",0), ("Chornovallery_Mail_A.2",0), ("Chornovallery_Mail_A.3",0), ("Chornovallery_Mail_A.4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,769 , weight(18)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(12)|difficulty(7) ,imodbits_armor, [], [fac_kingdom_2] ],
["m_chornovalley_mail_b", "Chornovalley Mail", [("Chornovallery_Mail_B",0), ("Chornovallery_Mail_B.1",0), ("Chornovallery_Mail_B.2",0), ("Chornovallery_Mail_B.3",0), ("Chornovallery_Mail_B.4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,812 , weight(19)|abundance(100)|head_armor(0)|body_armor(41)|leg_armor(12)|difficulty(7) ,imodbits_armor, [], [fac_kingdom_2] ],

["m_chornovalley_heavy_mail_a", "Chornovalley Heavy Mail", [("Chornovallery_Heavy_Mail_A",0), ("Chornovallery_Heavy_Mail_A.1",0), ("Chornovallery_Heavy_Mail_A.2",0), ("Chornovallery_Heavy_Mail_A.3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,998 , weight(21)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(23)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_2] ],
["m_chornovalley_heavy_mail_b", "Chornovalley Heavy Mail", [("Chornovallery_Heavy_Mail_B",0), ("Chornovallery_Heavy_Mail_B.1",0), ("Chornovallery_Heavy_Mail_B.2",0), ("Chornovallery_Heavy_Mail_B.3",0), ("Chornovallery_Heavy_Mail_B.4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1239 , weight(21)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(23)|difficulty(10) ,imodbits_armor, [], [fac_kingdom_2] ],

["m_chornovalley_heavy_lamellar_a", "Chornovalley Lamellar Armor", [("Chornovalley_Heavy_Lamellar_A",0), ("Chornovalley_Heavy_Lamellar_A.1",0), ("Chornovalley_Heavy_Lamellar_A.2",0), ("Chornovalley_Heavy_Lamellar_A.3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1343 , weight(19)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(23)|difficulty(10) ,imodbits_armor, [], [fac_kingdom_2] ],
["m_chornovalley_heavy_lamellar_b", "Chornovalley Lamellar Armor", [("Chornovalley_Heavy_Lamellar_B",0), ("Chornovalley_Heavy_Lamellar_B.1",0), ("Chornovalley_Heavy_Lamellar_B.2",0), ("Chornovalley_Heavy_Lamellar_B.3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1455 , weight(21)|abundance(100)|head_armor(0)|body_armor(57)|leg_armor(23)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_2] ],
["m_chornovalley_heavy_lamellar_c", "Chornovalley Lamellar Armor", [("Chornovalley_Heavy_Lamellar_C",0), ("Chornovalley_Heavy_Lamellar_C.1",0), ("Chornovalley_Heavy_Lamellar_C.2",0), ("Chornovalley_Heavy_Lamellar_C.3",0), ("Chornovalley_Heavy_Lamellar_C.4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1455 , weight(21)|abundance(100)|head_armor(0)|body_armor(57)|leg_armor(23)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_2] ],

["m_tauria_vest_a", "Tauria Vest", [("Tauria_Vest_A",0), ("Tauria_Vest_A.1",0), ("Tauria_Vest_A.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,287 , weight(9)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_9] ],
["m_tauria_vest_b", "Tauria Vest", [("Tauria_Vest_B",0), ("Tauria_Vest_B.1",0), ("Tauria_Vest_B.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,312 , weight(10)|abundance(100)|head_armor(0)|body_armor(27)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_9] ],

["m_tauria_vest_medium_a", "Tauria Curburg Vest", [("Tauria_Vest_C",0), ("Tauria_Vest_C.1",0), ("Tauria_Vest_C.2",0), ("Tauria_Vest_C.3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,452 , weight(15)|abundance(100)|head_armor(0)|body_armor(37)|leg_armor(10)|difficulty(7) ,imodbits_cloth, [], [fac_kingdom_9] ],

["m_tauria_vest_heavy_a", "Tauria Curburg Vest", [("Tauria_Vest_D",0), ("Tauria_Vest_D.1",0), ("Tauria_Vest_D.2",0), ("Tauria_Vest_D.3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,549 , weight(19)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(15)|difficulty(8) ,imodbits_cloth, [], [fac_kingdom_9] ],
["m_tauria_vest_heavy_b", "Tauria Curburg Vest", [("Tauria_Vest_E",0), ("Tauria_Vest_E.1",0), ("Tauria_Vest_E.2",0), ("Tauria_Vest_E.3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,789 , weight(24)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(15)|difficulty(9) ,imodbits_cloth, [], [fac_kingdom_9] ],

["m_tauria_plate_a", "Tauria Breastplate", [("Tauria_Plate_A",0), ("Tauria_Plate_A.1",0), ("Tauria_Plate_A.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,459 , weight(16)|abundance(100)|head_armor(0)|body_armor(37)|leg_armor(14)|difficulty(7) ,imodbits_cloth, [], [fac_kingdom_9] ],
["m_tauria_plate_b", "Tauria Breastplate", [("Tauria_Plate_B",0), ("Tauria_Plate_B.1",0), ("Tauria_Plate_B.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,499 , weight(17)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(14)|difficulty(7) ,imodbits_cloth, [], [fac_kingdom_9] ],
["m_tauria_plate_c", "Tauria Breastplate", [("Tauria_Plate_C",0), ("Tauria_Plate_C.1",0), ("Tauria_Plate_C.2",0), ("Tauria_Plate_C.3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,516 , weight(18)|abundance(100)|head_armor(0)|body_armor(41)|leg_armor(14)|difficulty(7) ,imodbits_cloth, [], [fac_kingdom_9] ],

["m_tauria_plate_mail_a", "Tauria Breastplate on Mail", [("Tauria_Plate_Mail_A",0), ("Tauria_Plate_Mail_A.1",0), ("Tauria_Plate_Mail_A.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,499 , weight(18)|abundance(100)|head_armor(0)|body_armor(41)|leg_armor(16)|difficulty(7) ,imodbits_cloth, [], [fac_kingdom_9] ],
["m_tauria_plate_mail_b", "Tauria Breastplate on Mail", [("Tauria_Plate_Mail_B",0), ("Tauria_Plate_Mail_B.1",0), ("Tauria_Plate_Mail_B.2",0), ("Tauria_Plate_Mail_B.3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,759 , weight(21)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(16)|difficulty(8) ,imodbits_cloth, [], [fac_kingdom_9] ],

["m_tauria_brigandine_a", "Tauria Brigandine", [("Tauria_Brigandine_A",0), ("Tauria_Brigandine_A.1",0), ("Tauria_Brigandine_A.2",0), ("Tauria_Brigandine_A.3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,799 , weight(25)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(16)|difficulty(9) ,imodbits_cloth, [], [fac_kingdom_9] ],
["m_tauria_brigandine_b", "Tauria Brigandine", [("Tauria_Brigandine_B",0), ("Tauria_Brigandine_B.1",0), ("Tauria_Brigandine_B.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1349 , weight(26)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(19)|difficulty(9) ,imodbits_cloth, [], [fac_kingdom_9] ],

["m_aketon_silver_rose_a", "Silver Rose Aketon", [("Silver_Rose_Aketon_Basic_A",0), ("Silver_Rose_Aketon_Basic_A.1",0), ("Silver_Rose_Aketon_Basic_A.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,251 , weight(12)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_1] ],
["m_aketon_silver_rose_b", "Silver Rose Aketon", [("Silver_Rose_Aketon_Basic_B",0), ("Silver_Rose_Aketon_Basic_B.1",0), ("Silver_Rose_Aketon_Basic_B.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,251 , weight(12)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_1] ],

["m_leather_silver_rose_b", "Silver Rose Leather Vest", [("Silver_Rose_Leather_A",0), ("Silver_Rose_Leather_A.1",0), ("Silver_Rose_Leather_A.2",0),("Silver_Rose_Leather_A.3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,251 , weight(12)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_1] ],

["m_silver_rose_gambeson_a", "Silver Rose Gambeson", [("Silver_Rose_Gambeson_A",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_1] ],

["m_swadia_recruit_a", "Silver Rose Aketon", [("Silver_Rose_Aketon",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 299 , weight(10)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(7)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],

["m_swadia_recruit_plated_a", "Silver Rose Plated Aketon", [("Silver_Rose_Aketon_Plated_A",0),("Silver_Rose_Aketon_Plated_A.1",0),("Silver_Rose_Aketon_Plated_A.2",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 1399 , weight(15)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(7)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_recruit_plated_b", "Silver Rose Plated Aketon", [("Silver_Rose_Aketon_Plated_B",0),("Silver_Rose_Aketon_Plated_B.1",0),("Silver_Rose_Aketon_Plated_B.2",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 1699 , weight(15)|abundance(100)|head_armor(0)|body_armor(33)|leg_armor(16)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_recruit_plated_c", "Silver Rose Plated Aketon", [("Silver_Rose_Aketon_Plated_B",0),("Silver_Rose_Aketon_Plated_B.1",0),("Silver_Rose_Aketon_Plated_B.2",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 1499 , weight(15)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(16)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],

["m_silver_rose_mail_a", "Silver Rose Mail", [("Silver_Rose_Mail_A",0), ("Silver_Rose_Mail_A.1",0), ("Silver_Rose_Mail_A.2",0), ("Silver_Rose_Mail_A.3",0), ("Silver_Rose_Mail_A.4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,789 , weight(18)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(17)|difficulty(7) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_silver_rose_mail_b", "Silver Rose Mail", [("Silver_Rose_Mail_B",0), ("Silver_Rose_Mail_B.1",0), ("Silver_Rose_Mail_B.2",0), ("Silver_Rose_Mail_B.3",0), ("Silver_Rose_Mail_B.4",0), ("Silver_Rose_Mail_B.5",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1307 , weight(18)|abundance(100)|head_armor(3)|body_armor(37)|leg_armor(17)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_1] ],

["m_silver_rose_brigandine_a", "Silver Rose Brigandine", [("Silver_Rose_Brigandine_A",0), ("Silver_Rose_Brigandine_A.1",0), ("Silver_Rose_Brigandine_A.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1199 , weight(24)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(20)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_silver_rose_brigandine_b", "Silver Rose Brigandine", [("Silver_Rose_Brigandine_B",0), ("Silver_Rose_Brigandine_B.1",0), ("Silver_Rose_Brigandine_B.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1199 , weight(24)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(17)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],

["m_silver_rose_breastplate_a", "Silver Rose Breastplate", [("Silver_Rose_Vest_A",0),("Silver_Rose_Vest_A.1",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 1569 , weight(15)|abundance(100)|head_armor(0)|body_armor(32)|leg_armor(16)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_silver_rose_breastplate_heavy_a", "Silver Rose Breastplate", [("Silver_Rose_Vest_B",0),("Silver_Rose_Vest_B.1",0),("Silver_Rose_Vest_B.2",0),("Silver_Rose_Vest_B.3",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 2391 , weight(23)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(21)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_silver_rose_breastplate_heavy_b", "Silver Rose Breastplate", [("Silver_Rose_Vest_C",0),("Silver_Rose_Vest_C.1",0),("Silver_Rose_Vest_C.2",0),("Silver_Rose_Vest_C.3",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 2077 , weight(22)|abundance(100)|head_armor(0)|body_armor(47)|leg_armor(21)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_1] ],

["m_silver_rose_plate_a", "Silver Rose Full Plate", [("Silver_Rose_Plate_Armor_A",0),("Silver_Rose_Plate_Armor_A.1",0),("Silver_Rose_Plate_Armor_A.2",0),("Silver_Rose_Plate_Armor_A.3",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 2416 , weight(25)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(25)|difficulty(11) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_silver_rose_plate_b", "Silver Rose Full Plate", [("Silver_Rose_Plate_Armor_B",0),("Silver_Rose_Plate_Armor_B.1",0),("Silver_Rose_Plate_Armor_B.2",0),("Silver_Rose_Plate_Armor_B.3",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 2416 , weight(25)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(25)|difficulty(11) ,imodbits_armor, [], [fac_kingdom_1] ],

["m_elen_leather_vest_a", "Elen Leather Vest", [("Elen_Leather_Vest_A",0), ("Elen_Leather_Vest_A.1",0), ("Elen_Leather_Vest_A.2",0), ("Elen_Leather_Vest_A.3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,334 , weight(12)|abundance(100)|head_armor(0)|body_armor(26)|leg_armor(7)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_10] ],
["m_elen_leather_vest_b", "Elen Leather Vest", [("Elen_Leather_Vest_B",0), ("Elen_Leather_Vest_B.1",0), ("Elen_Leather_Vest_B.2",0), ("Elen_Leather_Vest_B.3",0), ("Elen_Leather_Vest_B.4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,366 , weight(13)|abundance(100)|head_armor(0)|body_armor(27)|leg_armor(7)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_10] ],

["m_elen_vest_a", "Elen Plate Vest", [("Elen_Vest_A",0), ("Elen_Vest_A.1",0), ("Elen_Vest_A.2",0), ("Elen_Vest_A.3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,398 , weight(15)|abundance(100)|head_armor(0)|body_armor(32)|leg_armor(7)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_10] ],
["m_elen_vest_b", "Elen Plate Vest", [("Elen_Vest_B",0), ("Elen_Vest_B.1",0), ("Elen_Vest_B.2",0), ("Elen_Vest_B.3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,439 , weight(16)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(7)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_10] ],
["m_elen_vest_c", "Elen Plate Vest", [("Elen_Vest_C",0), ("Elen_Vest_C.1",0), ("Elen_Vest_C.2",0), ("Elen_Vest_C.3",0), ("Elen_Vest_C.4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,516 , weight(18)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(7)|difficulty(7) ,imodbits_cloth, [], [fac_kingdom_10] ],
["m_elen_vest_d", "Elen Plate Vest", [("Elen_Vest_D",0), ("Elen_Vest_D.1",0), ("Elen_Vest_D.2",0), ("Elen_Vest_D.3",0), ("Elen_Vest_D.4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,609 , weight(20)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(15)|difficulty(8) ,imodbits_cloth, [], [fac_kingdom_10] ],
["m_elen_vest_e", "Elen Plate Vest", [("Elen_Vest_E",0), ("Elen_Vest_E.1",0), ("Elen_Vest_E.2",0), ("Elen_Vest_E.3",0), ("Elen_Vest_E.4",0), ("Elen_Vest_E.5",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,629 , weight(20)|abundance(100)|head_armor(0)|body_armor(41)|leg_armor(15)|difficulty(8) ,imodbits_cloth, [], [fac_kingdom_10] ],

["m_elen_lamellar_a", "Elen Heavy Lamellar", [("Elen_Lamellar_A",0), ("Elen_Lamellar_A.1",0), ("Elen_Lamellar_A.2",0), ("Elen_Lamellar_A.3",0), ("Elen_Lamellar_A.4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,981 , weight(22)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(15)|difficulty(9) ,imodbits_cloth, [], [fac_kingdom_10] ],
["m_elen_lamellar_b", "Elen Heavy Lamellar", [("Elen_Lamellar_B",0), ("Elen_Lamellar_B.1",0), ("Elen_Lamellar_B.2",0), ("Elen_Lamellar_B.3",0), ("Elen_Lamellar_B.4",0), ("Elen_Lamellar_B.5",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,899 , weight(21)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(15)|difficulty(8) ,imodbits_cloth, [], [fac_kingdom_10] ],
["m_elen_lamellar_c", "Elen Heavy Lamellar", [("Elen_Lamellar_C",0), ("Elen_Lamellar_C.1",0), ("Elen_Lamellar_C.2",0), ("Elen_Lamellar_C.3",0), ("Elen_Lamellar_C.4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1095 , weight(23)|abundance(100)|head_armor(0)|body_armor(47)|leg_armor(15)|difficulty(9) ,imodbits_cloth, [], [fac_kingdom_10] ],
["m_elen_lamellar_d", "Elen Heavy Lamellar", [("Elen_Lamellar_D",0), ("Elen_Lamellar_D.1",0), ("Elen_Lamellar_D.2",0), ("Elen_Lamellar_D.3",0), ("Elen_Lamellar_D.4",0), ("Elen_Lamellar_D.5",0), ("Elen_Lamellar_D.6",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1295 , weight(26)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(15)|difficulty(9) ,imodbits_cloth, [], [fac_kingdom_10] ],

["m_elen_plated_leather_a", "Elen Plated Leather", [("Elen_Plate_A",0), ("Elen_Plate_A.1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1695 , weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(18)|difficulty(11) ,imodbits_cloth, [], [fac_kingdom_10] ],
["m_elen_plated_leather_b", "Elen Plated Leather", [("Elen_Plate_B",0), ("Elen_Plate_B.1",0), ("Elen_Plate_B.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1695 , weight(25)|abundance(100)|head_armor(0)|body_armor(55)|leg_armor(18)|difficulty(11) ,imodbits_cloth, [], [fac_kingdom_10] ],
["m_elen_plated_leather_c", "Elen Plated Leather", [("Elen_Plate_C",0), ("Elen_Plate_C.1",0), ("Elen_Plate_C.2",0), ("Elen_Plate_C.3",0), ("Elen_Plate_C.4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1695 , weight(25)|abundance(100)|head_armor(0)|body_armor(55)|leg_armor(18)|difficulty(11) ,imodbits_cloth, [], [fac_kingdom_10] ],

["hairako_long_coat_a", "Hairako Coat", [("Hairako_Long_Coat_A",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,87 , weight(7)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(8)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_8] ],
["hairako_long_coat_b", "Hairako Coat", [("Hairako_Long_Coat_B",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,87 , weight(7)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(8)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_8] ],
["hairako_long_coat_c", "Hairako Coat", [("Hairako_Long_Coat_C",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,87 , weight(7)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(8)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_8] ],
["hairako_long_coat_d", "Decorated Hairako Coat", [("Hairako_Long_Coat_D",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,87 , weight(7)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(8)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_8] ],

["hairako_infantry_vest_a", "Hairako Infantry Clothing", [("Hairako_Vest_A",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,138 , weight(7)|abundance(100)|head_armor(0)|body_armor(19)|leg_armor(8)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_8] ],
["hairako_infantry_vest_b", "Hairako Infantry Clothing", [("Hairako_Vest_B",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,144 , weight(7)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(8)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_8] ],
["hairako_infantry_vest_c", "Hairako Leather Cuirass", [("Hairako_Vest_C",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,155 , weight(9)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(8)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_8] ],
["hairako_infantry_vest_d", "Hairako Leather Armor", [("Hairako_Vest_D",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,246 , weight(13)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(8)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_8] ],

["hairako_long_coat_mail_a", "Long Hairako Coat with Mail", [("Hairako_Long_Coat_Mail_A",0), ("Hairako_Long_Coat_Mail_A.1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,217 , weight(16)|abundance(100)|head_armor(0)|body_armor(32)|leg_armor(8)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_8] ],
["hairako_long_coat_mail_b", "Long Hairako Coat with Mail", [("Hairako_Long_Coat_Mail_B",0), ("Hairako_Long_Coat_Mail_B.1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,217 , weight(16)|abundance(100)|head_armor(0)|body_armor(32)|leg_armor(8)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_8] ],

["hairako_long_coat_scale_a", "Long Hairako Coat with Scale", [("Hairako_Long_Coat_Scale_A",0), ("Hairako_Long_Coat_Scale_A.1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,499 , weight(18)|abundance(100)|head_armor(0)|body_armor(37)|leg_armor(8)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_8] ],
["hairako_long_coat_scale_b", "Long Hairako Coat with Scale", [("Hairako_Long_Coat_Scale_B",0), ("Hairako_Long_Coat_Scale_B.1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,499 , weight(18)|abundance(100)|head_armor(0)|body_armor(37)|leg_armor(8)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_8] ],
["hairako_long_coat_scale_c", "Long Hairako Coat with Scale", [("Hairako_Long_Coat_Scale_C",0), ("Hairako_Long_Coat_Scale_C.1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,592 , weight(20)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(15)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_8] ],
["hairako_long_coat_scale_d", "Long Hairako Coat with Scale", [("Hairako_Long_Coat_Scale_D",0), ("Hairako_Long_Coat_Scale_D.1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,592 , weight(20)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(15)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_8] ],

["hairako_full_mail_a", "Hairako Full Mail", [("Hairako_Long_Coat_Full_Mail_A",0), ("Hairako_Long_Coat_Full_Mail_A.1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1026 , weight(25)|abundance(100)|head_armor(0)|body_armor(47)|leg_armor(20)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_8] ],
["hairako_full_mail_b", "Hairako Full Mail", [("Hairako_Long_Coat_Full_Mail_B",0), ("Hairako_Long_Coat_Full_Mail_B.1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1026 , weight(25)|abundance(100)|head_armor(0)|body_armor(47)|leg_armor(20)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_8] ],

["m_nerpa_shirt", "Nerpa Shirt", [("Shirt_Nerpa_A",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 3 , weight(1)|abundance(100)|head_armor(0)|body_armor(5)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["m_nerpa_aketon_a", "Nerpa Aketon", [("Nerpa_Aketon_A",0), ("Nerpa_Aketon_A.1",0), ("Nerpa_Aketon_A.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,251 , weight(12)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(7)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_7] ],
["m_nerpa_aketon_b", "Nerpa Aketon", [("Nerpa_Aketon_B",0), ("Nerpa_Aketon_B.1",0), ("Nerpa_Aketon_B.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,289 , weight(13)|abundance(100)|head_armor(0)|body_armor(24)|leg_armor(7)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_7] ],

["m_nerpa_coat_of_plates_light_a", "Nerpa Light Coat of Plates", [("Nerpa_Coat_Of_Plates_A",0), ("Nerpa_Coat_Of_Plates_A.1",0), ("Nerpa_Coat_Of_Plates_A.2",0), ("Nerpa_Coat_Of_Plates_A.3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,345 , weight(15)|abundance(100)|head_armor(0)|body_armor(28)|leg_armor(7)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_7] ],
["m_nerpa_coat_of_plates_light_b", "Nerpa Light Coat of Plates", [("Nerpa_Coat_Of_Plates_B",0), ("Nerpa_Coat_Of_Plates_B.1",0), ("Nerpa_Coat_Of_Plates_B.2",0), ("Nerpa_Coat_Of_Plates_B.3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,365 , weight(16)|abundance(100)|head_armor(0)|body_armor(30)|leg_armor(7)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_7] ],

["m_nerpa_coat_of_plates_medium_a", "Nerpa Coat of Plates", [("Nerpa_Coat_Of_Plates_C",0), ("Nerpa_Coat_Of_Plates_C.1",0), ("Nerpa_Coat_Of_Plates_C.2",0), ("Nerpa_Coat_Of_Plates_C.3",0), ("Nerpa_Coat_Of_Plates_C.4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,399 , weight(17)|abundance(100)|head_armor(0)|body_armor(33)|leg_armor(7)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_7] ],
["m_nerpa_coat_of_plates_medium_b", "Nerpa Coat of Plates", [("Nerpa_Coat_Of_Plates_D",0), ("Nerpa_Coat_Of_Plates_D.1",0), ("Nerpa_Coat_Of_Plates_D.2",0), ("Nerpa_Coat_Of_Plates_D.3",0), ("Nerpa_Coat_Of_Plates_D.4",0), ("Nerpa_Coat_Of_Plates_D.5",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,414 , weight(19)|abundance(100)|head_armor(0)|body_armor(38)|leg_armor(9)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_7] ],

["m_nerpa_coat_of_plates_heavy_a", "Nerpa Heavy Coat of Plates", [("Nerpa_Coat_Of_Plates_E",0), ("Nerpa_Coat_Of_Plates_E.1",0), ("Nerpa_Coat_Of_Plates_E.2",0), ("Nerpa_Coat_Of_Plates_E.3",0), ("Nerpa_Coat_Of_Plates_E.4",0), ("Nerpa_Coat_Of_Plates_E.5",0), ("Nerpa_Coat_Of_Plates_E.6",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,414 , weight(21)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(9)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_7] ],
["m_nerpa_coat_of_plates_heavy_b", "Nerpa Heavy Coat of Plates", [("Nerpa_Coat_Of_Plates_F",0), ("Nerpa_Coat_Of_Plates_F.1",0), ("Nerpa_Coat_Of_Plates_F.2",0), ("Nerpa_Coat_Of_Plates_F.3",0), ("Nerpa_Coat_Of_Plates_F.4",0), ("Nerpa_Coat_Of_Plates_F.5",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,569 , weight(22)|abundance(100)|head_armor(0)|body_armor(47)|leg_armor(9)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_7] ],

["m_desert_bandit_a", "Desert Padded Vest", [("turk_bandit_a",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 345 , weight(10)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(11)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_11] ],
["m_desert_bandit_b", "Desert Mail", [("turk_bandit_b",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 561 , weight(17)|abundance(100)|head_armor(0)|body_armor(36)|leg_armor(11)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_11] ],
["m_desert_bandit_c", "Desert Scale Armor", [("turk_bandit_c",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 489 , weight(15)|abundance(100)|head_armor(0)|body_armor(32)|leg_armor(11)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_11] ],
["m_desert_bandit_d", "Desert Leather Vest", [("turk_bandit_d",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 351 , weight(13)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(11)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_11] ],

["mkk_black_scale_a", "Black Scale Armor", [("Ghulam_heavy_cavalryman_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1599 , weight(20)|abundance(100)|head_armor(0)|body_armor(53)|leg_armor(18)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_6] ],
["mkk_black_scale_b", "Black Scale Armor", [("Ghulam_heavy_cavalryman_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1599 , weight(20)|abundance(100)|head_armor(0)|body_armor(53)|leg_armor(18)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_6] ],
["mkk_black_scale_c", "Black Scale Armor", [("Ghulam_heavy_cavalryman_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1599 , weight(20)|abundance(100)|head_armor(0)|body_armor(53)|leg_armor(18)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_6] ],

["mkk_mamluke_a", "Mamluke Armor", [("tyrk_armor_heavi_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1699 , weight(20)|abundance(100)|head_armor(0)|body_armor(53)|leg_armor(23)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_6, fac_kingdom_11] ],
["mkk_mamluke_b", "Mamluke Armor", [("tyrk_armor_heavi_b",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1699 , weight(20)|abundance(100)|head_armor(0)|body_armor(53)|leg_armor(23)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_6, fac_kingdom_11] ],
["mkk_mamluke_c", "Mamluke Armor", [("tyrk_armor_heavi_c",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1699 , weight(20)|abundance(100)|head_armor(0)|body_armor(53)|leg_armor(23)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_6, fac_kingdom_11] ],

["mkk_sultan_armor", "Sultan Armor", [("armor_Sultan_saracens",0), ("armor_Sultan_saracens.1",0), ("armor_Sultan_saracens.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,6289 , weight(20)|abundance(1)|head_armor(0)|body_armor(61)|leg_armor(26)|difficulty(18) ,imodbits_armor, [], [fac_kingdom_6] ],

# BODY ARMOR BEGIN
# Poor Quality Body Armor
["craftable_aketon_a", "Aketon", [("Player_Aketon_A",0), ("Player_Aketon_A.1",0), ("Player_Aketon_A.2",0)], itp_craftable|itp_type_body_armor|itp_covers_legs,0 ,397 , weight(9)|abundance(100)|head_armor(0)|body_armor(23)|leg_armor(7)|difficulty(0) ,imodbits_cloth, [], [] ],
["craftable_padded_cloth_a", "Padded Cloth", [("Player_Padded_Cloth_A",0)], itp_craftable|itp_type_body_armor|itp_covers_legs ,0, 397 , weight(10)|abundance(100)|head_armor(0)|body_armor(24)|leg_armor(8)|difficulty(0) ,imodbits_cloth, [], [] ],
["craftable_mail_a", "Mail Shirt", [("Player_Padded_Cloth_Mail_A",0)], itp_craftable|itp_type_body_armor|itp_covers_legs ,0, 459 , weight(15)|abundance(100)|head_armor(0)|body_armor(36)|leg_armor(9)|difficulty(0) ,imodbits_cloth, [], [] ],
["craftable_coat_of_plates_light_a", "Light Coat of Plates", [("Player_Coat_Of_Plates_A",0), ("Player_Coat_Of_Plates_A.1",0), ("Player_Coat_Of_Plates_A.2",0), ("Player_Coat_Of_Plates_A.3",0)], itp_craftable|itp_type_body_armor|itp_covers_legs,0 ,445 , weight(14)|abundance(100)|head_armor(0)|body_armor(30)|leg_armor(14)|difficulty(0) ,imodbits_armor, [], [] ],
["craftable_coat_of_plates_light_b", "Light Coat of Plates", [("Player_Coat_Of_Plates_B",0), ("Player_Coat_Of_Plates_B.1",0), ("Player_Coat_Of_Plates_B.2",0), ("Player_Coat_Of_Plates_B.3",0)], itp_craftable|itp_type_body_armor|itp_covers_legs,0 ,465 , weight(15)|abundance(100)|head_armor(0)|body_armor(32)|leg_armor(14)|difficulty(0) ,imodbits_armor, [], [] ],
["craftable_coat_of_plates_medium_a", "Coat of Plates", [("Player_Coat_Of_Plates_C",0), ("Player_Coat_Of_Plates_C.1",0), ("Player_Coat_Of_Plates_C.2",0), ("Player_Coat_Of_Plates_C.3",0), ("Nerpa_Coat_Of_Plates_C.4",0)], itp_craftable|itp_type_body_armor|itp_covers_legs,0 ,599 , weight(17)|abundance(100)|head_armor(0)|body_armor(36)|leg_armor(14)|difficulty(0) ,imodbits_armor, [], [] ],
["craftable_coat_of_plates_medium_b", "Coat of Plates", [("Player_Coat_Of_Plates_D",0), ("Player_Coat_Of_Plates_D.1",0), ("Player_Coat_Of_Plates_D.2",0), ("Player_Coat_Of_Plates_D.3",0), ("Player_Coat_Of_Plates_D.4",0), ("Nerpa_Coat_Of_Plates_D.5",0)], itp_craftable|itp_type_body_armor|itp_covers_legs,0 ,614 , weight(19)|abundance(100)|head_armor(0)|body_armor(42)|leg_armor(14)|difficulty(0) ,imodbits_armor, [], [] ],

# Medium Quality Body Armor
["craftable_breastplate_a", "Breastplate", [("Player_Breastplate_A",0),("Player_Breastplate_A.1",0)], itp_craftable|itp_type_body_armor|itp_covers_legs ,0, 559 , weight(17)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(9)|difficulty(0) ,imodbits_armor, [], [] ],
["craftable_breastplate_b", "Breastplate on Mail", [("Player_Breastplate_B",0),("Player_Breastplate_B.1",0)], itp_craftable|itp_type_body_armor|itp_covers_legs ,0, 659 , weight(18)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(9)|difficulty(0) ,imodbits_armor, [], [] ],
["craftable_breastplate_c", "Heavy Breastplate on Mail", [("Player_Breastplate_Heavy_A",0),("Player_Breastplate_Heavy_A.1",0), ("Player_Breastplate_Heavy_A.2",0), ("Player_Breastplate_Heavy_A.3",0)], itp_craftable|itp_type_body_armor|itp_covers_legs ,0,1159 , weight(19)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(14)|difficulty(8) ,imodbits_armor, [], [] ],

["craftable_coat_of_plates_heavy_a", "Heavy Coat of Plates", [("Player_Coat_Of_Plates_E",0), ("Player_Coat_Of_Plates_E.1",0), ("Player_Coat_Of_Plates_E.2",0), ("Player_Coat_Of_Plates_E.3",0), ("Player_Coat_Of_Plates_E.4",0), ("Player_Coat_Of_Plates_E.5",0), ("Player_Coat_Of_Plates_E.6",0)], itp_craftable|itp_type_body_armor|itp_covers_legs,0 ,1515 , weight(21)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(15)|difficulty(9) ,imodbits_armor, [], [] ],
["craftable_coat_of_plates_heavy_b", "Heavy Coat of Plates", [("Player_Coat_Of_Plates_F",0), ("Player_Coat_Of_Plates_F.1",0), ("Player_Coat_Of_Plates_F.2",0), ("Player_Coat_Of_Plates_F.3",0), ("Player_Coat_Of_Plates_F.4",0), ("Player_Coat_Of_Plates_F.5",0)], itp_craftable|itp_type_body_armor|itp_covers_legs,0 ,1665 , weight(22)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(15)|difficulty(10) ,imodbits_armor, [], [] ],
["craftable_coat_of_plates_heavy_c", "Heavy Coat of Plates", [("Player_Coat_Of_Plates_G",0), ("Player_Coat_Of_Plates_G.1",0), ("Player_Coat_Of_Plates_G.2",0), ("Player_Coat_Of_Plates_G.3",0), ("Player_Coat_Of_Plates_G.4",0), ("Player_Coat_Of_Plates_G.5",0)], itp_craftable|itp_type_body_armor|itp_covers_legs,0 ,1765 , weight(23)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(18)|difficulty(11) ,imodbits_armor, [], [] ],

# High Quality Body Armor
["craftable_plated_leather_a", "Lamellar Leather", [("Player_Scale_A",0), ("Player_Scale_A.1",0)], itp_craftable|itp_type_body_armor|itp_covers_legs,0 ,1995 , weight(25)|abundance(100)|head_armor(0)|body_armor(55)|leg_armor(18)|difficulty(12) ,imodbits_armor, [], [] ],
["craftable_plated_leather_b", "Lamellar Leather", [("Player_Scale_B",0), ("Player_Scale_B.1",0), ("Player_Scale_B.2",0)], itp_craftable|itp_type_body_armor|itp_covers_legs,0 ,2395 , weight(25)|abundance(100)|head_armor(0)|body_armor(57)|leg_armor(18)|difficulty(12) ,imodbits_armor, [], [] ],
["craftable_plated_leather_c", "Lamellar Leather", [("Player_Scale_C",0), ("Player_Scale_C.1",0), ("Player_Scale_C.2",0), ("Player_Scale_C.3",0), ("Player_Scale_C.4",0)], itp_craftable|itp_type_body_armor|itp_covers_legs,0 ,2695 , weight(25)|abundance(100)|head_armor(0)|body_armor(60)|leg_armor(18)|difficulty(13) ,imodbits_armor, [], [] ],

["craftable_full_plate_a", "Full Plate", [("Player_Plate_Armor_A",0),("Player_Plate_Armor_A.1",0),("Player_Plate_Armor_A.2",0)], itp_craftable|itp_type_body_armor|itp_covers_legs ,0, 2549 , weight(24)|abundance(100)|head_armor(0)|body_armor(56)|leg_armor(22)|difficulty(12) ,imodbits_armor, [], []],
["craftable_full_plate_b", "Full Plate", [("Player_Plate_Armor_B",0),("Player_Plate_Armor_B.1",0),("Player_Plate_Armor_B.2",0)], itp_craftable|itp_type_body_armor|itp_covers_legs ,0, 3349 , weight(27)|abundance(100)|head_armor(0)|body_armor(63)|leg_armor(22)|difficulty(15) ,imodbits_armor, [], []],
["craftable_full_plate_c", "Full Plate", [("Player_Plate_Armor_C",0),("Player_Plate_Armor_C.1",0),("Player_Plate_Armor_C.2",0)], itp_craftable|itp_type_body_armor|itp_covers_legs ,0, 2649 , weight(24)|abundance(100)|head_armor(0)|body_armor(57)|leg_armor(23)|difficulty(12) ,imodbits_armor, [], []],
["craftable_full_plate_d", "Full Plate", [("Player_Plate_Armor_D",0),("Player_Plate_Armor_D.1",0),("Player_Plate_Armor_D.2",0)], itp_craftable|itp_type_body_armor|itp_covers_legs ,0, 3649 , weight(28)|abundance(100)|head_armor(0)|body_armor(65)|leg_armor(23)|difficulty(16) ,imodbits_armor, [], []],

["craftable_shell_plate_a", "Shell Plate", [("Player_Plate_Shell_A",0),("Player_Plate_Shell_A.1",0),("Player_Plate_Shell_A.2",0)], itp_craftable|itp_type_body_armor|itp_covers_legs ,0, 4949 , weight(31)|abundance(100)|head_armor(0)|body_armor(68)|leg_armor(25)|difficulty(18) ,imodbits_armor, [], []],
["craftable_shell_plate_b", "Shell Plate", [("Player_Plate_Shell_B",0),("Player_Plate_Shell_B.1",0),("Player_Plate_Shell_B.2",0)], itp_craftable|itp_type_body_armor|itp_covers_legs ,0, 5249 , weight(32)|abundance(100)|head_armor(0)|body_armor(69)|leg_armor(27)|difficulty(19) ,imodbits_armor, [], []],
["craftable_shell_plate_c", "Shell Plate", [("Player_Plate_Shell_C",0),("Player_Plate_Shell_C.1",0),("Player_Plate_Shell_C.2",0), ("Player_Plate_Shell_C.3",0)], itp_craftable|itp_type_body_armor|itp_covers_legs ,0, 5949 , weight(34)|abundance(100)|head_armor(0)|body_armor(72)|leg_armor(27)|difficulty(23) ,imodbits_armor, [], []],
# BODY ARMOR END

["m_aketon_forest_a", "Green Forester Aketon", [("aketon_two_tones_a",0), ("aketon_two_tones_a.1",0), ("aketon_two_tones_a.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,251 , weight(12)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], [] ],
["m_aketon_forest_b", "Green Forester Aketon", [("aketon_two_tones_b",0), ("aketon_two_tones_b.1",0), ("aketon_two_tones_b.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,329 , weight(14)|abundance(100)|head_armor(0)|body_armor(27)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], [] ],
["m_aketon_forest_c", "Green Forester Aketon with Mail", [("aketon_two_tones_c",0), ("aketon_two_tones_c.1",0), ("aketon_two_tones_c.2",0), ("aketon_two_tones_c.3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,329 , weight(18)|abundance(100)|head_armor(0)|body_armor(37)|leg_armor(6)|difficulty(0) ,imodbits_armor, [], [] ],

["m_aketon_old_a", "Old Aketon", [("aketon_old_a",0), ("aketon_old_a.1",0), ("aketon_old_a.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,251 , weight(12)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], [] ],
["m_aketon_old_b", "Old Aketon", [("aketon_old_b",0), ("aketon_old_b.1",0), ("aketon_old_b.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,251 , weight(12)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], [] ],
["m_aketon_old_c", "Old Aketon with Kneekops", [("aketon_kneecops_old",0), ("aketon_kneecops_old.1",0), ("aketon_kneecops_old.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,459 , weight(19)|abundance(100)|head_armor(0)|body_armor(27)|leg_armor(17)|difficulty(0) ,imodbits_cloth, [], [] ],

["m_aketon_black_a", "Black Aketon", [("Aketon_Black_A",0), ("Aketon_Black_A.1",0), ("Aketon_Black_A.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,399 , weight(13)|abundance(100)|head_armor(0)|body_armor(24)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [], [] ],
["m_aketon_black_b", "Black Aketon with Kneekops", [("Aketon_Black_B",0), ("Aketon_Black_B.1",0), ("Aketon_Black_B.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,459 , weight(19)|abundance(100)|head_armor(0)|body_armor(27)|leg_armor(17)|difficulty(0) ,imodbits_cloth, [], [] ],

 #NEW: was "leather_jerkin"
["leather_jerkin", "Leather Jerkin", [("Rough_Leather_Jerkin_A",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 321 , weight(6)|abundance(100)|head_armor(0)|body_armor(23)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["nomad_vest", "Nomad Vest", [("nomad_vest_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 360 , weight(7)|abundance(50)|head_armor(0)|body_armor(22)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["ragged_outfit", "Ragged Outfit", [("Padded_Cloth_Cloacked_B",0),("Padded_Cloth_Cloacked_B.1",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 390 , weight(7)|abundance(100)|head_armor(0)|body_armor(23)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
 #NEW: was padded_leather
["padded_leather", "Padded Leather", [("Leather_Vest_A",0), ("Leather_Vest_A.1",0), ("Leather_Vest_A.2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian,0, 454 , weight(12)|abundance(100)|head_armor(0)|body_armor(27)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["m_leather_vest_a", "Leather Vest", [("Leather_Vest_B",0), ("Leather_Vest_B.1",0), ("Leather_Vest_B.2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian,0, 454 , weight(12)|abundance(100)|head_armor(0)|body_armor(27)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["heavy_leather_vest", "Heavy Leather Vest", [("Leather_Cuirass_A",0), ("Leather_Cuirass_A.1",0), ("Leather_Cuirass_A.2",0), ("Leather_Cuirass_A.3",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian,0, 454 , weight(12)|abundance(100)|head_armor(0)|body_armor(27)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["tribal_warrior_outfit", "Tribal Warrior Outfit", [("Rough_Leather_Fur_A",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 520 , weight(14)|abundance(100)|head_armor(0)|body_armor(30)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["nomad_robe", "Nomad Robe", [("khergit_vest_c",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0,
 610 , weight(15)|abundance(100)|head_armor(0)|body_armor(32)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
#["heraldric_armor", "Heraldric Armor", [("tourn_armor_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 442 , weight(17)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(8)|difficulty(7) ,imodbits_armor ],
#NEW: was "std_lthr_coat"
["studded_leather_coat", "Studded Leather Coat", [("Rough_Leather_Jerkin_Mail_A",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 690 , weight(14)|abundance(100)|head_armor(0)|body_armor(36)|leg_armor(10)|difficulty(7) ,imodbits_armor ],

["lamellar_vest", "Lamellar Vest", [("lamellar_vest_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 970 , weight(18)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_cloth ],

["lamellar_vest_khergit", "Khergit Lamellar Vest", [("lamellar_vest_b",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 970 , weight(18)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_cloth ],

["mail_hauberk", "Mail Hauberk", [("Hauberk_Revised_A",0),("Hauberk_Revised_A.1",0),("Hauberk_Revised_A.2",0),("Hauberk_Revised_A.3",0),("Hauberk_Revised_A.4",0),("Hauberk_Revised_A.5",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(12)|difficulty(7) ,imodbits_armor ],

["m_hauberk_old_a", "Hauberk on Old Aketon", [("hauberk_old",0), ("hauberk_old.1",0), ("hauberk_old.2",0), ("hauberk_old.3",0), ("hauberk_old.4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,899 , weight(24)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(9)|difficulty(0) ,imodbits_armor, [], [] ], 

["m_hauberk_black_a", "Black Hauberk", [("Hauberk_Black_A",0), ("Hauberk_Black_A.1",0), ("Hauberk_Black_A.2",0), ("Hauberk_Black_A.3",0), ("Hauberk_Black_A.4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,899 , weight(24)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(9)|difficulty(0) ,imodbits_armor, [], [] ], 

["m_hauberk_mountain_a", "Mountain Hauberk", [("hauberk_mountain_a",0), ("hauberk_mountain_a.1",0), ("hauberk_mountain_a.2",0), ("hauberk_mountain_a.3",0), ("hauberk_mountain_a.4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,309 , weight(18)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(6)|difficulty(0) ,imodbits_armor, [], [] ],
["m_hauberk_mountain_b", "Mountain Hauberk", [("hauberk_mountain_b",0), ("hauberk_mountain_b.1",0), ("hauberk_mountain_b.2",0), ("hauberk_mountain_b.3",0), ("hauberk_mountain_b.4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,309 , weight(18)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(6)|difficulty(0) ,imodbits_armor, [], [] ],
["m_hauberk_mountain_c", "Mountain Hauberk", [("hauberk_mountain_c",0), ("hauberk_mountain_c.1",0), ("hauberk_mountain_c.2",0), ("hauberk_mountain_c.3",0), ("hauberk_mountain_c.4",0), ("hauberk_mountain_c.5",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,405 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(6)|difficulty(0) ,imodbits_armor, [], [] ],
["m_hauberk_mountain_d", "Mountain Hauberk", [("hauberk_mountain_d",0), ("hauberk_mountain_d.1",0), ("hauberk_mountain_d.2",0), ("hauberk_mountain_d.3",0), ("hauberk_mountain_d.4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,399 , weight(19)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(6)|difficulty(0) ,imodbits_armor, [], [] ],

["m_hauberk_navy_a", "Rider Hauberk", [("hauberk_navy_a",0), ("hauberk_navy_a.1",0), ("hauberk_navy_a.2",0), ("hauberk_navy_a.3",0), ("hauberk_navy_a.4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,493 , weight(24)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(12)|difficulty(7) ,imodbits_armor, [], [] ],
["m_hauberk_navy_b", "Rider Hauberk", [("hauberk_navy_b",0), ("hauberk_navy_b.1",0), ("hauberk_navy_b.2",0), ("hauberk_navy_b.3",0), ("hauberk_navy_b.4",0), ("hauberk_navy_b.5",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,599 , weight(24)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(12)|difficulty(8) ,imodbits_armor, [], [] ],
["m_hauberk_navy_c", "Rider Hauberk", [("hauberk_navy_c",0), ("hauberk_navy_c.1",0), ("hauberk_navy_c.2",0), ("hauberk_navy_c.3",0), ("hauberk_navy_c.4",0), ("hauberk_navy_c.5",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,719 , weight(28)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(12)|difficulty(9) ,imodbits_armor, [], [] ],

["black_breastplate_a", "Black Breastplate", [("Black_Breastplate_A",0), ("Black_Breastplate_A.1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,673 , weight(16)|abundance(100)|head_armor(0)|body_armor(36)|leg_armor(9)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_12] ],
["black_breastplate_b", "Black Breastplate", [("Black_Breastplate_B",0), ("Black_Breastplate_B.1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,871 , weight(20)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(9)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_12] ],
["black_breastplate_c", "Black Breastplate", [("Black_Breastplate_C",0), ("Black_Breastplate_C.1",0), ("Black_Breastplate_C.2",0), ("Black_Breastplate_C.3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,995 , weight(22)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(15)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_12] ],

["brigandine_red", "Brigandine", [("brigandine_b",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
 1830 , weight(19)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(12)|difficulty(0) ,imodbits_armor ],

["m_brigandine_navy_c", "Rider Brigandine", [("brigandine_navy_a",0), ("brigandine_navy_a.1",0), ("brigandine_navy_a.2",0), ("brigandine_navy_a.3",0), ("brigandine_navy_a.4",0), ("brigandine_navy_a.5",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1099 , weight(32)|abundance(100)|head_armor(0)|body_armor(51)|leg_armor(12)|difficulty(9) ,imodbits_armor, [], [] ],

["banded_armor", "Banded Armor", [("banded_armor_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2710 , weight(23)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(14)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_12] ],
#NEW: was hard_lthr_a
["cuir_bouilli", "Cuir Bouilli", [("cuir_bouilli_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3100 , weight(24)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(15)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_12] ],
["coat_of_plates", "Coat of Plates", [("Coat_Of_Plates_B",0), ("Coat_Of_Plates_B.1",0), ("Coat_Of_Plates_B.2",0), ("Coat_Of_Plates_B.3",0), ("Coat_Of_Plates_B.4",0), ("Coat_Of_Plates_B.5",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1828 , weight(21)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(8)|difficulty(8) ,imodbits_armor ],
["coat_of_plates_red", "Coat of Plates", [("Coat_Of_Plates_A",0), ("Coat_Of_Plates_A.1",0), ("Coat_Of_Plates_A.2",0), ("Coat_Of_Plates_A.3",0), ("Coat_Of_Plates_A.4",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,1945 , weight(22)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(8)|difficulty(8) ,imodbits_armor ],
["plate_armor", "Plate Armor", [("Plate_Armor_A",0), ("Plate_Armor_A.1",0), ("Plate_Armor_A.2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 6553 , weight(27)|abundance(100)|head_armor(0)|body_armor(55)|leg_armor(17)|difficulty(9) ,imodbits_plate ],
["black_armor", "Black Armor", [("Plate_Armor_B",0), ("Plate_Armor_B.1",0), ("Plate_Armor_B.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0, 9496 , weight(28)|abundance(100)|head_armor(0)|body_armor(57)|leg_armor(18)|difficulty(10) ,imodbits_plate ],
["black_plate", "Stormguard Black Armor", [("Stormguard_Black_Plate_A",0), ("Stormguard_Black_Plate_A.1",0), ("Stormguard_Black_Plate_A.2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs ,0, 9496 , weight(28)|abundance(100)|head_armor(0)|body_armor(58)|leg_armor(19)|difficulty(11) ,imodbits_plate, [], [fac_kingdom_12] ],

 ["sarranid_dress_a", "Dress", [("woolen_dress",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 33 , weight(1)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
 ["sarranid_dress_b", "Dress", [("woolen_dress",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 33 , weight(1)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],

#Quest-specific - perhaps can be used for prisoners, 
["burlap_tunic", "Burlap Tunic", [("Shirt_B",0)], itp_type_body_armor  |itp_covers_legs ,0,
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

["mt_hood_a", "Hood", [("helm10",0)], itp_merchandise|itp_type_head_armor, 0, 99, weight(0.5)|abundance(100)|head_armor(9)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_10] ],
["mt_hood_a2", "Hood", [("helm10_g",0)], itp_merchandise|itp_type_head_armor, 0, 99, weight(0.5)|abundance(100)|head_armor(9)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_10] ],
["mt_hood_a3", "Hood", [("helm10_l",0)], itp_merchandise|itp_type_head_armor, 0, 99, weight(0.5)|abundance(100)|head_armor(9)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_10] ],
["mt_hood_a4", "Hood", [("helm10_w",0)], itp_merchandise|itp_type_head_armor, 0, 99, weight(0.5)|abundance(100)|head_armor(9)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_10] ],

["large_hood_a", "Hood on Mail", [("Large_Hood_A",0)], itp_merchandise|itp_type_head_armor, 0, 159, weight(1.5)|abundance(100)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor, [], [] ],

["headcloth", "Headcloth", [("headcloth_a_new",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["woolen_hood", "Woolen Hood", [("woolen_hood",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["arming_cap", "Arming Cap", [("arming_cap_a_new",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 5 , weight(1)|abundance(100)|head_armor(7)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["m_arming_cap_a", "Brown Padded Arming Cap", [("Arming_Cap_A",0),("Arming_Cap_A.1",0),("Arming_Cap_A_inv",ixmesh_inventory),("Arming_Cap_A_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor  |itp_civilian|itp_attach_armature ,0, 49 , weight(2)|abundance(100)|head_armor(12)|body_armor(3)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["m_arming_cap_b", "Red Padded Arming Cap", [("Arming_Cap_B",0),("Arming_Cap_B.1",0),("Arming_Cap_B_inv",ixmesh_inventory),("Arming_Cap_B_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor  |itp_civilian|itp_attach_armature ,0, 49 , weight(2)|abundance(100)|head_armor(12)|body_armor(3)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["m_arming_cap_c", "Black Padded Arming Cap", [("Arming_Cap_C",0),("Arming_Cap_C.1",0),("Arming_Cap_C_inv",ixmesh_inventory),("Arming_Cap_C_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor  |itp_civilian|itp_attach_armature ,0, 49 , weight(2)|abundance(100)|head_armor(12)|body_armor(3)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["m_coif_cloth_a", "Black Coif", [("koif_monie_a",0)], itp_type_head_armor|itp_merchandise   ,0, 89 , weight(0.5)|abundance(100)|head_armor(12)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["m_coif_cloth_b", "Light Coif", [("koif_monie_b",0)], itp_type_head_armor|itp_merchandise   ,0, 89 , weight(0.5)|abundance(100)|head_armor(12)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],

["fur_hat", "Fur Hat", [("fur_hat_a_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["nomad_cap", "Nomad Cap", [("nomad_cap_a_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["nomad_cap_b", "Nomad Cap", [("nomad_cap_b_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(13)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["steppe_cap", "Steppe Cap", [("steppe_cap_a_new",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 14 , weight(1)|abundance(100)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["padded_coif", "Padded Coif", [("padded_coif_a_new",0)], itp_merchandise| itp_type_head_armor   ,0, 6 , weight(1)|abundance(100)|head_armor(11)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["m_padded_coif_a", "Padded Coif", [("Padded_Coif_A",0),("Padded_Coif_A.1",0),("Padded_Coif_A_inv",ixmesh_inventory),("Padded_Coif_A_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 61 , weight(2)|abundance(100)|head_armor(15)|body_armor(3)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["m_padded_coif_b", "Black Padded Coif", [("Padded_Coif_B",0),("Padded_Coif_B.1",0),("Padded_Coif_B_inv",ixmesh_inventory),("Padded_Coif_B_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 61 , weight(2)|abundance(100)|head_armor(15)|body_armor(3)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["woolen_cap", "Woolen Cap", [("woolen_cap_new",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 2 , weight(1)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["woolen_cap_new_b", "Woolen Cap", [("woolen_cap_new_b",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 2 , weight(1)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["woolen_cap_new_c", "Woolen Cap", [("woolen_cap_new_c",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 2 , weight(1)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["woolen_cap_new_d", "Woolen Cap", [("woolen_cap_new_d",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 2 , weight(1)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["woolen_cap_new_e", "Woolen Cap", [("woolen_cap_new_e",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 2 , weight(1)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["woolen_cap_new_f", "Woolen Cap", [("woolen_cap_new_f",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 2 , weight(1)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["felt_hat", "Felt Hat", [("felt_hat_a_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["felt_hat_b", "Felt Hat", [("felt_hat_b_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["itm_felt_hat_a", "Forester Felt Hat", [("Felt_A",0),("Felt_A.1",0),("Felt_A.2",0),("Felt_A_inv",ixmesh_inventory),("Felt_A_inv.1",ixmesh_inventory),("Felt_A_inv.2",ixmesh_inventory)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_attach_armature,0, 45 , weight(2)|abundance(100)|head_armor(12)|body_armor(3)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["itm_felt_hat_b", "Forester Felt Hat", [("Felt_B",0),("Felt_B.1",0),("Felt_B.2",0),("Felt_B_inv",ixmesh_inventory),("Felt_B_inv.1",ixmesh_inventory),("Felt_B_inv.2",ixmesh_inventory)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_attach_armature,0, 45 , weight(2)|abundance(100)|head_armor(12)|body_armor(3)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["itm_felt_hat_c", "Forester Felt Hat", [("Felt_C",0),("Felt_C.1",0),("Felt_C.2",0),("Felt_C_inv",ixmesh_inventory),("Felt_C_inv.1",ixmesh_inventory),("Felt_C_inv.2",ixmesh_inventory)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_attach_armature,0, 36 , weight(2)|abundance(100)|head_armor(10)|body_armor(2)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["itm_felt_hat_d", "Forester Felt Hat", [("Felt_D",0),("Felt_D.1",0),("Felt_D.2",0),("Felt_D_inv",ixmesh_inventory),("Felt_D_inv.1",ixmesh_inventory),("Felt_D_inv.2",ixmesh_inventory)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_attach_armature,0, 36 , weight(2)|abundance(100)|head_armor(10)|body_armor(2)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["leather_cap", "Leather Cap", [("leather_cap_a_new",0)], itp_merchandise| itp_type_head_armor|itp_civilian ,0, 8, weight(1)|abundance(100)|head_armor(18)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["female_hood", "Lady's Hood", [("ladys_hood_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 9 , weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["leather_steppe_cap_a", "Steppe Cap", [("Leather_Cap_A",0),("Leather_Cap_A.1",0),("Leather_Cap_A_inv",ixmesh_inventory),("Leather_Cap_A_inv.1",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature   ,0,
24 , weight(1)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["leather_steppe_cap_b", "Steppe Cap ", [("tattered_steppe_cap_b_new",0)], itp_merchandise|itp_type_head_armor   ,0, 
36 , weight(1)|abundance(100)|head_armor(16)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["leather_steppe_cap_c", "Steppe Cap", [("steppe_cap_a_new",0)], itp_merchandise|itp_type_head_armor   ,0, 51 , weight(1)|abundance(100)|head_armor(16)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["leather_warrior_cap", "Leather Warrior Cap", [("skull_cap_new_b",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 14 , weight(1)|abundance(100)|head_armor(18)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["skullcap", "Skullcap", [("skull_cap_new_a",0)], itp_merchandise| itp_type_head_armor   ,0, 60 , weight(1.0)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ],
["mail_coif", "Mail Coif", [("mail_coif_new",0)], itp_merchandise| itp_type_head_armor   ,0, 71 , weight(1.25)|abundance(100)|head_armor(22)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_armor ],

["m_coif_alternate_a", "Mail Coif", [("coif",0)], itp_merchandise|itp_type_head_armor|itp_covers_beard  ,0, 79 , weight(1.0)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_9] ],
["m_coif_alternate_b", "Balaclava Coif", [("balaclavacoif",0)], itp_merchandise|itp_type_head_armor|itp_covers_beard  ,0, 100 , weight(1.0)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_9] ],
["m_coif_alternate_c", "Full Face Coif", [("fullfacecoif",0)], itp_merchandise|itp_type_head_armor|itp_covers_beard  ,0, 129 , weight(1.0)|abundance(100)|head_armor(33)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_9] ],

["m_conical_helmet_a", "Conical Helmet", [("conichelm",0)], itp_merchandise|itp_type_head_armor  ,0, 163 , weight(2)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_9] ],

["m_flat_top_a", "Flat Top Helmet", [("flattophelmet",0)], itp_merchandise|itp_type_head_armor  ,0, 151 , weight(2)|abundance(100)|head_armor(34)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_9] ],

["m_pepperpot_a", "Pepperpot Flat Helmet", [("frenchpepperpot2",0)], itp_merchandise|itp_type_head_armor  ,0, 347 , weight(2)|abundance(100)|head_armor(43)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_9] ],
["m_pepperpot_b", "Pepperpot Flat Helmet", [("frenchpepperpot3",0)], itp_merchandise|itp_type_head_armor  ,0, 308 , weight(2)|abundance(100)|head_armor(41)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_9] ],
["m_pepperpot_c", "Pepperpot Flat Helmet", [("pepperpothelm1",0)], itp_merchandise|itp_type_head_armor  ,0, 323 , weight(2)|abundance(100)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_9] ],
["m_pepperpot_d", "Pepperpot Helmet", [("frenchpepperpot",0)], itp_merchandise|itp_type_head_armor  ,0, 418 , weight(2)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_9] ],

["m_munitions_helm_a", "Munitions Helmet", [("munitionshelm2",0)], itp_merchandise|itp_type_head_armor  ,0, 613 , weight(2)|abundance(100)|head_armor(47)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_9] ],
["m_munitions_helm_b", "Flat Munitions Helmet", [("munitionshelm1",0)], itp_merchandise|itp_type_head_armor  ,0, 698 , weight(2)|abundance(100)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_9] ],

["stormguard_helmet_a", "Stormguard Helmet", [("Stormguard_Helmet_A",0), ("Stormguard_Helmet_A.1",0),("Stormguard_Helmet_A_inv",ixmesh_inventory), ("Stormguard_Helmet_A_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 335 , weight(1.5)|abundance(100)|head_armor(32)|body_armor(1)|leg_armor(0)|difficulty(0) ,imodbits_plate,  [], [fac_kingdom_12]],
["stormguard_helmet_b", "Stormguard Helmet on Padded", [("Stormguard_Helmet_B",0), ("Stormguard_Helmet_B.1",0),("Stormguard_Helmet_B_inv",ixmesh_inventory), ("Stormguard_Helmet_B_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 386 , weight(1.5)|abundance(100)|head_armor(35)|body_armor(3)|leg_armor(0)|difficulty(0) ,imodbits_plate,  [], [fac_kingdom_12]],
["stormguard_helmet_c", "Decorated Stormguard Helmet on Padded", [("Stormguard_Helmet_C",0), ("Stormguard_Helmet_C.1",0), ("Stormguard_Helmet_C.2",0),("Stormguard_Helmet_C_inv",ixmesh_inventory), ("Stormguard_Helmet_C_inv.1",ixmesh_inventory), ("Stormguard_Helmet_C_inv.2",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 395 , weight(1.5)|abundance(100)|head_armor(36)|body_armor(3)|leg_armor(0)|difficulty(0) ,imodbits_plate,  [], [fac_kingdom_12]],

["stormguard_pointy_helmet_a", "Stormguard Tall Helmet", [("Stormguard_Pointy_Helmet_A",0), ("Stormguard_Pointy_Helmet_A.1",0),("Stormguard_Pointy_Helmet_A_inv",ixmesh_inventory), ("Stormguard_Pointy_Helmet_A_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 345 , weight(1.75)|abundance(100)|head_armor(36)|body_armor(1)|leg_armor(0)|difficulty(0) ,imodbits_plate,  [], [fac_kingdom_12]],
["stormguard_pointy_helmet_b", "Stormguard Tall Helmet", [("Stormguard_Pointy_Helmet_B",0), ("Stormguard_Pointy_Helmet_B.1",0),("Stormguard_Pointy_Helmet_B_inv",ixmesh_inventory), ("Stormguard_Pointy_Helmet_B_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 345 , weight(1.75)|abundance(100)|head_armor(36)|body_armor(1)|leg_armor(0)|difficulty(0) ,imodbits_plate,  [], [fac_kingdom_12]],
["stormguard_pointy_helmet_c", "Stormguard Tall Helmet on Padded", [("Stormguard_Pointy_Helmet_C",0), ("Stormguard_Pointy_Helmet_C.1",0),("Stormguard_Pointy_Helmet_C_inv",ixmesh_inventory), ("Stormguard_Pointy_Helmet_C_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 415 , weight(1.75)|abundance(100)|head_armor(39)|body_armor(2)|leg_armor(0)|difficulty(0) ,imodbits_plate,  [], [fac_kingdom_12]],
["stormguard_pointy_helmet_d", "Stormguard Tall Helmet on Padded", [("Stormguard_Pointy_Helmet_D",0), ("Stormguard_Pointy_Helmet_D.1",0),("Stormguard_Pointy_Helmet_D_inv",ixmesh_inventory), ("Stormguard_Pointy_Helmet_D_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 415 , weight(1.75)|abundance(100)|head_armor(39)|body_armor(2)|leg_armor(0)|difficulty(0) ,imodbits_plate,  [], [fac_kingdom_12]],
["stormguard_pointy_helmet_e", "Decorated Stormguard Tall Helmet on Padded", [("Stormguard_Pointy_Helmet_E",0), ("Stormguard_Pointy_Helmet_E.1",0), ("Stormguard_Pointy_Helmet_E.2",0),("Stormguard_Pointy_Helmet_E_inv",ixmesh_inventory), ("Stormguard_Pointy_Helmet_E_inv.1",ixmesh_inventory), ("Stormguard_Pointy_Helmet_E_inv.2",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 425 , weight(1.9)|abundance(100)|head_armor(40)|body_armor(3)|leg_armor(0)|difficulty(0) ,imodbits_plate,  [], [fac_kingdom_12]],

["stormguard_pointy_helmet_mail_a", "Stormguard Tall Helmet on Mail", [("Stormguard_Pointy_Helmet_Mail_A",0), ("Stormguard_Pointy_Helmet_Mail_A.1",0),("Stormguard_Pointy_Helmet_Mail_A_inv",ixmesh_inventory), ("Stormguard_Pointy_Helmet_Mail_A_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 515 , weight(2)|abundance(100)|head_armor(44)|body_armor(5)|leg_armor(0)|difficulty(8) ,imodbits_plate,  [], [fac_kingdom_12]],
["stormguard_pointy_helmet_mail_b", "Stormguard Tall Helmet on Mail", [("Stormguard_Pointy_Helmet_Mail_B",0), ("Stormguard_Pointy_Helmet_Mail_B.1",0),("Stormguard_Pointy_Helmet_Mail_B_inv",ixmesh_inventory), ("Stormguard_Pointy_Helmet_Mail_B_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 515 , weight(2)|abundance(100)|head_armor(44)|body_armor(5)|leg_armor(0)|difficulty(8) ,imodbits_plate,  [], [fac_kingdom_12]],
["stormguard_pointy_helmet_mail_c", "Decorated Stormguard Tall Helmet on Mail", [("Stormguard_Pointy_Helmet_Mail_C",0), ("Stormguard_Pointy_Helmet_Mail_C.1",0), ("Stormguard_Pointy_Helmet_Mail_C.2",0),("Stormguard_Pointy_Helmet_Mail_C_inv",ixmesh_inventory), ("Stormguard_Pointy_Helmet_Mail_C_inv.1",ixmesh_inventory), ("Stormguard_Pointy_Helmet_Mail_C_inv.2",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 525 , weight(2.25)|abundance(100)|head_armor(45)|body_armor(5)|leg_armor(0)|difficulty(8) ,imodbits_plate,  [], [fac_kingdom_12]],
["stormguard_pointy_helmet_mail_d", "Stormguard Tall Helmet with Mask", [("Stormguard_Pointy_Helmet_Mail_D",0), ("Stormguard_Pointy_Helmet_Mail_D.1",0), ("Stormguard_Pointy_Helmet_Mail_D.2",0),("Stormguard_Pointy_Helmet_Mail_D_inv",ixmesh_inventory), ("Stormguard_Pointy_Helmet_Mail_D_inv.1",ixmesh_inventory), ("Stormguard_Pointy_Helmet_Mail_D_inv.2",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 595 , weight(2.25)|abundance(100)|head_armor(48)|body_armor(5)|leg_armor(0)|difficulty(9) ,imodbits_plate,  [], [fac_kingdom_12]],

["stormguard_elite_helmet_a", "Stormguard Elite Helmet", [("Stormguard_Decorated_Helmet_A",0), ("Stormguard_Decorated_Helmet_A.1",0), ("Stormguard_Decorated_Helmet_A.2",0), ("Stormguard_Decorated_Helmet_A.3",0),("Stormguard_Decorated_Helmet_A_inv",ixmesh_inventory), ("Stormguard_Decorated_Helmet_A_inv.1",ixmesh_inventory), ("Stormguard_Decorated_Helmet_A_inv.2",ixmesh_inventory), ("Stormguard_Decorated_Helmet_A_inv.3",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 675 , weight(2.5)|abundance(100)|head_armor(49)|body_armor(5)|leg_armor(0)|difficulty(9) ,imodbits_plate,  [], [fac_kingdom_12]],
["stormguard_elite_helmet_b", "Stormguard Elite Helmet", [("Stormguard_Decorated_Helmet_B",0), ("Stormguard_Decorated_Helmet_B.1",0), ("Stormguard_Decorated_Helmet_B.2",0), ("Stormguard_Decorated_Helmet_B.3",0),("Stormguard_Decorated_Helmet_B_inv",ixmesh_inventory), ("Stormguard_Decorated_Helmet_B_inv.1",ixmesh_inventory), ("Stormguard_Decorated_Helmet_B_inv.2",ixmesh_inventory), ("Stormguard_Decorated_Helmet_B_inv.3",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 675 , weight(2.5)|abundance(100)|head_armor(49)|body_armor(5)|leg_armor(0)|difficulty(9) ,imodbits_plate,  [], [fac_kingdom_12]],
["stormguard_elite_helmet_c", "Stormguard Elite Helmet with Mask", [("Stormguard_Decorated_Helmet_C",0), ("Stormguard_Decorated_Helmet_C.1",0), ("Stormguard_Decorated_Helmet_C.2",0), ("Stormguard_Decorated_Helmet_C.3",0), ("Stormguard_Decorated_Helmet_C.4",0), ("Stormguard_Decorated_Helmet_C_inv",ixmesh_inventory), ("Stormguard_Decorated_Helmet_C_inv.1",ixmesh_inventory), ("Stormguard_Decorated_Helmet_C_inv.2",ixmesh_inventory), ("Stormguard_Decorated_Helmet_C_inv.3",ixmesh_inventory), ("Stormguard_Decorated_Helmet_C_inv.4",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 675 , weight(2.5)|abundance(100)|head_armor(52)|body_armor(5)|leg_armor(0)|difficulty(10) ,imodbits_plate,  [], [fac_kingdom_12]],

["alpine_chapel_a", "Alpine Crossbowman Chapel", [("Alpine_Chapel_A",0), ("Alpine_Chapel_A.1",0),("Alpine_Chapel_A_inv",ixmesh_inventory), ("Alpine_Chapel_A_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 333 , weight(1.5)|abundance(100)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate,  [], [fac_kingdom_5]],

["alpine_chapel_padded_a", "Alpine Crossbowman Chapel", [("Alpine_Chapel_B",0), ("Alpine_Chapel_B.1",0),("Alpine_Chapel_B_inv",ixmesh_inventory), ("Alpine_Chapel_B_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 348 , weight(1.5)|abundance(100)|head_armor(34)|body_armor(2)|leg_armor(0)|difficulty(0) ,imodbits_plate,  [], [fac_kingdom_5]],
["alpine_chapel_padded_b", "Alpine Crossbowman Chapel", [("Alpine_Chapel_C",0), ("Alpine_Chapel_C.1",0),("Alpine_Chapel_C.2",0), ("Alpine_Chapel_C_inv",ixmesh_inventory), ("Alpine_Chapel_C_inv.1",ixmesh_inventory), ("Alpine_Chapel_C_inv.2",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 369 , weight(1.5)|abundance(100)|head_armor(37)|body_armor(2)|leg_armor(0)|difficulty(0) ,imodbits_plate,  [], [fac_kingdom_5]],

["alpine_chapel_mail_a", "Alpine Crossbowman Chapel", [("Alpine_Chapel_D",0), ("Alpine_Chapel_D.1",0),("Alpine_Chapel_D_inv",ixmesh_inventory), ("Alpine_Chapel_D_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 412 , weight(1.5)|abundance(100)|head_armor(40)|body_armor(5)|leg_armor(0)|difficulty(0) ,imodbits_plate,  [], [fac_kingdom_5]],
["alpine_chapel_mail_b", "Alpine Crossbowman Chapel", [("Alpine_Chapel_E",0), ("Alpine_Chapel_E.1",0),("Alpine_Chapel_E.2",0), ("Alpine_Chapel_E_inv",ixmesh_inventory), ("Alpine_Chapel_E_inv.1",ixmesh_inventory), ("Alpine_Chapel_E_inv.2",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 499 , weight(1.5)|abundance(100)|head_armor(43)|body_armor(5)|leg_armor(0)|difficulty(0) ,imodbits_plate,  [], [fac_kingdom_5]],


["alpine_footman_helmet_a", "Alpine Helmet", [("Alpine_Helmet_A",0), ("Alpine_Helmet_A.1",0),("Alpine_Helmet_A_inv",ixmesh_inventory), ("Alpine_Helmet_A_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 348 , weight(1.5)|abundance(100)|head_armor(36)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate,  [], [fac_kingdom_5]],
["alpine_footman_helmet_b", "Alpine Helmet", [("Alpine_Helmet_B",0), ("Alpine_Helmet_B.1",0),("Alpine_Helmet_B_inv",ixmesh_inventory), ("Alpine_Helmet_B_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 366 , weight(1.5)|abundance(100)|head_armor(38)|body_armor(2)|leg_armor(0)|difficulty(0) ,imodbits_plate,  [], [fac_kingdom_5]],
["alpine_footman_helmet_c", "Alpine Helmet", [("Alpine_Helmet_C",0), ("Alpine_Helmet_C.1",0),("Alpine_Helmet_C_inv",ixmesh_inventory), ("Alpine_Helmet_C_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 416 , weight(1.5)|abundance(100)|head_armor(41)|body_armor(5)|leg_armor(0)|difficulty(0) ,imodbits_plate,  [], [fac_kingdom_5]],

["alpine_visored_helmet_a", "Alpine Visored Helmet", [("Alpine_Helmet_Visor_A",0), ("Alpine_Helmet_Visor_A.1",0), ("Alpine_Helmet_Visor_A.2",0),("Alpine_Helmet_Visor_A_inv",ixmesh_inventory), ("Alpine_Helmet_Visor_A_inv.1",ixmesh_inventory),("Alpine_Helmet_Visor_A_inv.2",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 470 , weight(1.75)|abundance(100)|head_armor(45)|body_armor(5)|leg_armor(0)|difficulty(8) ,imodbits_plate,  [], [fac_kingdom_5]],
["alpine_visored_helmet_b", "Alpine Visored Helmet", [("Alpine_Helmet_Visor_B",0), ("Alpine_Helmet_Visor_B.1",0), ("Alpine_Helmet_Visor_B.2",0),("Alpine_Helmet_Visor_B_inv",ixmesh_inventory), ("Alpine_Helmet_Visor_B_inv.1",ixmesh_inventory),("Alpine_Helmet_Visor_B_inv.2",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 470 , weight(1.75)|abundance(100)|head_armor(45)|body_armor(5)|leg_armor(0)|difficulty(8) ,imodbits_plate,  [], [fac_kingdom_5]],
["alpine_visored_helmet_c", "Alpine Visored Helmet", [("Alpine_Helmet_Visor_C",0), ("Alpine_Helmet_Visor_C.1",0), ("Alpine_Helmet_Visor_C.2",0),("Alpine_Helmet_Visor_C_inv",ixmesh_inventory), ("Alpine_Helmet_Visor_C_inv.1",ixmesh_inventory),("Alpine_Helmet_Visor_C_inv.2",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 479 , weight(1.75)|abundance(100)|head_armor(45)|body_armor(5)|leg_armor(0)|difficulty(8) ,imodbits_plate,  [], [fac_kingdom_5]],

["alpine_heavy_helmet_a", "Alpine Full Helmet", [("Alpine_Helmet_Heavy_A",0), ("Alpine_Helmet_Heavy_A.1",0), ("Alpine_Helmet_Heavy_A.2",0),("Alpine_Helmet_Heavy_A_inv",ixmesh_inventory), ("Alpine_Helmet_Heavy_A_inv.1",ixmesh_inventory),("Alpine_Helmet_Heavy_A_inv.2",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 781 , weight(2.25)|abundance(100)|head_armor(51)|body_armor(5)|leg_armor(0)|difficulty(10) ,imodbits_plate,  [], [fac_kingdom_5]],
["alpine_heavy_helmet_b", "Alpine Full Helmet", [("Alpine_Helmet_Heavy_B",0), ("Alpine_Helmet_Heavy_B.1",0), ("Alpine_Helmet_Heavy_B.2",0),("Alpine_Helmet_Heavy_B_inv",ixmesh_inventory), ("Alpine_Helmet_Heavy_B_inv.1",ixmesh_inventory),("Alpine_Helmet_Heavy_B_inv.2",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 781 , weight(2.25)|abundance(100)|head_armor(51)|body_armor(5)|leg_armor(0)|difficulty(10) ,imodbits_plate,  [], [fac_kingdom_5]],
["alpine_heavy_helmet_c", "Alpine Full Helmet", [("Alpine_Helmet_Heavy_C",0), ("Alpine_Helmet_Heavy_C.1",0), ("Alpine_Helmet_Heavy_C.2",0),("Alpine_Helmet_Heavy_C.3",0),("Alpine_Helmet_Heavy_C_inv",ixmesh_inventory), ("Alpine_Helmet_Heavy_C_inv.1",ixmesh_inventory),("Alpine_Helmet_Heavy_C_inv.2",ixmesh_inventory),("Alpine_Helmet_Heavy_C_inv.3",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 781 , weight(2.25)|abundance(100)|head_armor(51)|body_armor(5)|leg_armor(0)|difficulty(10) ,imodbits_plate,  [], [fac_kingdom_5]],

["mkk_turban_a", "Turban", [("saracin_turban_a",0)], itp_merchandise|itp_type_head_armor, 0, 255, weight(2)|abundance(100)|head_armor(21)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_6, fac_kingdom_10] ],
["mkk_turban_b", "Turban", [("saracin_turban_b",0)], itp_merchandise|itp_type_head_armor, 0, 255, weight(2)|abundance(100)|head_armor(21)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_6, fac_kingdom_10] ],
["mkk_turban_c", "Turban", [("saracin_turban_c",0)], itp_merchandise|itp_type_head_armor, 0, 255, weight(2)|abundance(100)|head_armor(21)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_6, fac_kingdom_10] ],

["mkk_helm_sar_a","Light Eastern Helmet", [("helm_saracin_3", 0)], itp_type_head_armor|itp_merchandise, 0,390, weight(1)|abundance(100)|head_armor(15)|difficulty(7), imodbits_none, [], [fac_kingdom_6]],
["mkk_helm_sar_b","Eastern War Cap", [("helm_saracin_b", 0)], itp_type_head_armor|itp_merchandise, 0,390, weight(1)|abundance(100)|head_armor(15)|difficulty(7), imodbits_none, [], [fac_kingdom_6]],

["mkk_helm_warrior_a","Warrior Helmet", [("helm_saracin_2", 0)], itp_type_head_armor|itp_merchandise, 0,450, weight(2)|abundance(100)|head_armor(25)|difficulty(7), imodbit_reinforced, [], [fac_kingdom_6]],
["mkk_helm_warrior_b","Warrior Helmet", [("helm_saracin_a", 0)], itp_type_head_armor|itp_merchandise, 0,450, weight(2)|abundance(100)|head_armor(39)|difficulty(7), imodbit_reinforced, [], [fac_kingdom_6]],
["mkk_helm_warrior_c","Warrior Helmet", [("helm_saracin_j", 0)], itp_type_head_armor|itp_merchandise, 0,450, weight(2)|abundance(100)|head_armor(39)|difficulty(7), imodbit_reinforced, [], [fac_kingdom_6]],

["mkk_helm_mail_a","Mail Helmet", [("helm_saracin_f", 0)], itp_type_head_armor|itp_merchandise, 0,450, weight(2)|abundance(100)|head_armor(32)|difficulty(7), imodbit_reinforced, [], [fac_kingdom_6]],
["mkk_helm_mail_b","Mail Helmet", [("helm_saracin_1", 0)], itp_type_head_armor|itp_merchandise, 0,450, weight(2)|abundance(100)|head_armor(32)|difficulty(7), imodbit_reinforced, [], [fac_kingdom_6]],
["mkk_helm_mail_c","Mail Helmet", [("helm_saracin_d", 0)], itp_type_head_armor|itp_merchandise, 0,450, weight(2)|abundance(100)|head_armor(32)|difficulty(7), imodbit_reinforced, [], [fac_kingdom_6]],
["mkk_helm_mail_d","Mail Helmet", [("helm_saracin_e", 0)], itp_type_head_armor|itp_merchandise, 0,450, weight(2)|abundance(100)|head_armor(32)|difficulty(7), imodbit_reinforced, [], [fac_kingdom_6]],
["mkk_helm_mail_e","Mail Helmet", [("helm_saracin_f", 0)], itp_type_head_armor|itp_merchandise, 0,450, weight(2)|abundance(100)|head_armor(32)|difficulty(7), imodbit_reinforced, [], [fac_kingdom_6]],

["mkk_helm_light_sarranid","Light Eastern Helmet", [("helm_saracin_c", 0)], itp_type_head_armor|itp_merchandise, 0,399, weight(2)|abundance(100)|head_armor(25)|difficulty(0), imodbit_reinforced|imodbit_lordly, [], [fac_kingdom_6]],

["mkk_heavy_helmet_a", "Eastern Heavy Cavalry Helmet", [("helm_tyrk_heavi_a",0), ("helm_tyrk_heavi_a.1",0)], itp_merchandise|itp_type_head_armor, 0, 1799, weight(2)|abundance(100)|head_armor(54)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_plate, [], [fac_kingdom_6] ],
["mkk_heavy_helmet_b", "Eastern Heavy Cavalry Helmet", [("helm_tyrk_heavi_b",0), ("helm_tyrk_heavi_b.1",0)], itp_merchandise|itp_type_head_armor, 0, 1799, weight(2)|abundance(100)|head_armor(54)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_plate, [], [fac_kingdom_6] ],
["mkk_heavy_helmet_c", "Eastern Heavy Cavalry Helmet", [("helm_tyrk_heavi_c",0), ("helm_tyrk_heavi_c.1",0)], itp_merchandise|itp_type_head_armor, 0, 1799, weight(2)|abundance(100)|head_armor(54)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_plate, [], [fac_kingdom_6] ],

["mkk_semi_heavy_helmet_a", "Eastern Heavy Helmet", [("helm_tyrk_a",0), ("helm_tyrk_a.1",0), ("helm_tyrk_a_market",ixmesh_inventory), ("helm_tyrk_a_market.1",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 1699, weight(2)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, [], [fac_kingdom_6] ],
["mkk_semi_heavy_helmet_b", "Eastern Heavy Helmet", [("helm_tyrk_b",0), ("helm_tyrk_b_market",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 1699, weight(2)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, [], [fac_kingdom_6] ],
["mkk_semi_heavy_helmet_c", "Eastern Heavy Helmet", [("helm_tyrk_c",0), ("helm_tyrk_c_market",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 1699, weight(2)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, [], [fac_kingdom_6] ],
["mkk_semi_heavy_helmet_d", "Eastern Heavy Helmet", [("helm_tyrk_d",0), ("helm_tyrk_d_market",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 1699, weight(2)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, [], [fac_kingdom_6] ],
["mkk_semi_heavy_helmet_e", "Eastern Heavy Helmet", [("helm_tyrk_e",0), ("helm_tyrk_e.1",0), ("helm_tyrk_e.2",0), ("helm_tyrk_e_market",ixmesh_inventory), ("helm_tyrk_e_market.1",ixmesh_inventory), ("helm_tyrk_e_market.2",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 1699, weight(2)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, [], [fac_kingdom_6] ],
["mkk_semi_heavy_helmet_f", "Eastern Heavy Helmet", [("helm_tyrk_f",0), ("helm_tyrk_f.1",0), ("helm_tyrk_f_market",ixmesh_inventory), ("helm_tyrk_f_market.1",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 1699, weight(2)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, [], [fac_kingdom_6] ],

["mkk_sultan_helmet_a","Sultan's Helmet", [("helm_Sultan_saracens", 0),("helm_Sultan_saracens_market", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise|itp_fit_to_head|itp_covers_beard, 0,3990, weight(2)|abundance(1)|head_armor(58)|difficulty(17), imodbits_none, [], [fac_kingdom_6]],

["hairako_helmet_a", "Hairako Helmet", [("Hairako_Helmet_A",0), ("Hairako_Helmet_A.1",0),("Hairako_Helmet_A_inv",ixmesh_inventory), ("Hairako_Helmet_A_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 154 , weight(1.5)|abundance(100)|head_armor(31)|body_armor(2)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_8]],
["hairako_helmet_b", "Hairako Decorated Helmet", [("Hairako_Helmet_B",0), ("Hairako_Helmet_B.1",0), ("Hairako_Helmet_B.2",0),("Hairako_Helmet_B_inv",ixmesh_inventory), ("Hairako_Helmet_B_inv.1",ixmesh_inventory), ("Hairako_Helmet_B_inv.2",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 159 , weight(1.5)|abundance(100)|head_armor(31)|body_armor(2)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_8]],
["hairako_helmet_c", "Hairako Helmet with Neckguard", [("Hairako_Helmet_C",0), ("Hairako_Helmet_C.1",0), ("Hairako_Helmet_C.2",0),("Hairako_Helmet_C_inv",ixmesh_inventory), ("Hairako_Helmet_C_inv.1",ixmesh_inventory), ("Hairako_Helmet_C_inv.2",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 187 , weight(1.5)|abundance(100)|head_armor(34)|body_armor(2)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_8]],

["hairako_nasal_helmet_a", "Hairako Infantry Helmet", [("Hairako_Helmet_Noseguard_A",0), ("Hairako_Helmet_Noseguard_A.1",0),("Hairako_Helmet_Noseguard_A_inv",ixmesh_inventory), ("Hairako_Helmet_Noseguard_A_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 190 , weight(1.75)|abundance(100)|head_armor(35)|body_armor(2)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_8]],
["hairako_nasal_helmet_b", "Hairako Infantry Helmet", [("Hairako_Helmet_Noseguard_B",0), ("Hairako_Helmet_Noseguard_B.1",0),("Hairako_Helmet_Noseguard_B_inv",ixmesh_inventory), ("Hairako_Helmet_Noseguard_B_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 190 , weight(1.75)|abundance(100)|head_armor(35)|body_armor(2)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_8]],
["hairako_nasal_helmet_c", "Hairako Infantry Helmet", [("Hairako_Helmet_Noseguard_C",0), ("Hairako_Helmet_Noseguard_C.1",0),("Hairako_Helmet_Noseguard_C_inv",ixmesh_inventory), ("Hairako_Helmet_Noseguard_C_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 190 , weight(1.75)|abundance(100)|head_armor(35)|body_armor(2)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_8]],
["hairako_nasal_helmet_d", "Hairako Infantry Helmet", [("Hairako_Helmet_Noseguard_D",0), ("Hairako_Helmet_Noseguard_D.1",0),("Hairako_Helmet_Noseguard_D_inv",ixmesh_inventory), ("Hairako_Helmet_Noseguard_D_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 190 , weight(1.75)|abundance(100)|head_armor(35)|body_armor(2)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_8]],
["hairako_nasal_helmet_e", "Hairako Infantry Helmet with Neckguard", [("Hairako_Helmet_Noseguard_E",0), ("Hairako_Helmet_Noseguard_E.1",0), ("Hairako_Helmet_Noseguard_E.2",0),("Hairako_Helmet_Noseguard_E_inv",ixmesh_inventory), ("Hairako_Helmet_Noseguard_E_inv.1",ixmesh_inventory), ("Hairako_Helmet_Noseguard_E_inv.2",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 244 , weight(2)|abundance(100)|head_armor(38)|body_armor(2)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_8]],

["hairako_mail_helmet_a", "Hairako Mail Helmet", [("Hairako_Helmet_Mail_A",0), ("Hairako_Helmet_Mail_A.1",0), ("Hairako_Helmet_Mail_A.2",0),("Hairako_Helmet_Mail_A_inv",ixmesh_inventory), ("Hairako_Helmet_Mail_A_inv.1",ixmesh_inventory), ("Hairako_Helmet_Mail_A_inv.2",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 348 , weight(2.25)|abundance(100)|head_armor(44)|body_armor(5)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_8]],
["hairako_mail_helmet_b", "Hairako Mail Helmet", [("Hairako_Helmet_Mail_B",0), ("Hairako_Helmet_Mail_B.1",0), ("Hairako_Helmet_Mail_B.2",0),("Hairako_Helmet_Mail_B_inv",ixmesh_inventory), ("Hairako_Helmet_Mail_B_inv.1",ixmesh_inventory), ("Hairako_Helmet_Mail_B_inv.2",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 348 , weight(2.25)|abundance(100)|head_armor(44)|body_armor(5)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_8]],
["hairako_mail_helmet_c", "Hairako Mail Helmet", [("Hairako_Helmet_Mail_C",0), ("Hairako_Helmet_Mail_C.1",0), ("Hairako_Helmet_Mail_C.2",0),("Hairako_Helmet_Mail_C_inv",ixmesh_inventory), ("Hairako_Helmet_Mail_C_inv.1",ixmesh_inventory), ("Hairako_Helmet_Mail_C_inv.2",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 348 , weight(2.25)|abundance(100)|head_armor(44)|body_armor(5)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_8]],
["hairako_mail_helmet_d", "Hairako Mail Helmet", [("Hairako_Helmet_Mail_D",0), ("Hairako_Helmet_Mail_D.1",0), ("Hairako_Helmet_Mail_D.2",0),("Hairako_Helmet_Mail_D_inv",ixmesh_inventory), ("Hairako_Helmet_Mail_D_inv.1",ixmesh_inventory), ("Hairako_Helmet_Mail_D_inv.2",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 348 , weight(2.25)|abundance(100)|head_armor(44)|body_armor(5)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_8]],

["nerpa_barbuta_open_a", "Barbute", [("Barbuta_E",0), ("Barbuta_E_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 248, weight(1.25)|abundance(100)|head_armor(39)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_7] ],
["nerpa_barbuta_open_b", "Barbute", [("Barbuta_G",0), ("Barbuta_G_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 999, weight(1.25)|abundance(100)|head_armor(39)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_7] ],

["nerpa_barbuta_open_cloth_a", "Barbute on Cloth", [("Nerpa_Barbuta_A",0), ("Nerpa_Barbuta_A.1",0),("Nerpa_Barbuta_A_inv",ixmesh_inventory), ("Nerpa_Barbuta_A_inv.1",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 289, weight(1.25)|abundance(100)|head_armor(39)|body_armor(2)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_7] ],
["nerpa_barbuta_open_cloth_b", "Barbute on Cloth", [("Nerpa_Barbuta_B",0), ("Nerpa_Barbuta_B.1",0),("Nerpa_Barbuta_B_inv",ixmesh_inventory), ("Nerpa_Barbuta_B_inv.1",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 289, weight(1.25)|abundance(100)|head_armor(39)|body_armor(2)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_7] ],

["nerpa_barbuta_open_padded_a", "Barbute on Padded", [("Nerpa_Barbuta_Padded_A",0), ("Nerpa_Barbuta_Padded_A.1",0), ("Nerpa_Barbuta_Padded_A_inv",ixmesh_inventory), ("Nerpa_Barbuta_Padded_A_inv.1",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 311, weight(1.5)|abundance(100)|head_armor(41)|body_armor(3)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_7] ],
["nerpa_barbuta_open_padded_b", "Barbute on Padded", [("Nerpa_Barbuta_Padded_B",0), ("Nerpa_Barbuta_Padded_B.1",0), ("Nerpa_Barbuta_Padded_B_inv",ixmesh_inventory), ("Nerpa_Barbuta_Padded_B_inv.1",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 315, weight(1.5)|abundance(100)|head_armor(41)|body_armor(3)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_7] ],

["nerpa_barbuta_open_red", "Decorated Barbute", [("Barbuta_B",0), ("Barbuta_B_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 959, weight(1.25)|abundance(100)|head_armor(39)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_7] ],
["nerpa_barbuta_open_nasal", "Barbute with Nasal", [("Barbuta_B_Hinged_Nasal",0), ("Barbuta_B_Hinged_Nasal_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 1099, weight(1.25)|abundance(100)|head_armor(41)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_7] ],

["nerpa_barbuta_a", "Barbute", [("Barbuta_A",0), ("Barbuta_A_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 1139, weight(1.5)|abundance(100)|head_armor(43)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_7] ],
["nerpa_barbuta_b", "Barbute", [("Barbuta_C",0), ("Barbuta_C_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 1139, weight(1.5)|abundance(100)|head_armor(43)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_7] ],
["nerpa_barbuta_c", "Barbute", [("Barbuta_F",0), ("Barbuta_F_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 1139, weight(1.5)|abundance(100)|head_armor(43)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_7] ],

["nerpa_barbuta_mail_a", "Barbute on Mail", [("Nerpa_Barbuta_Mail_A",0), ("Nerpa_Barbuta_Mail_A.1",0), ("Nerpa_Barbuta_Mail_A_inv",ixmesh_inventory), ("Nerpa_Barbuta_Mail_A_inv.1",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 699, weight(2.0)|abundance(100)|head_armor(46)|body_armor(5)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_7] ],
["nerpa_barbuta_mail_b", "Barbute on Mail", [("Nerpa_Barbuta_Mail_B",0), ("Nerpa_Barbuta_Mail_B.1",0), ("Nerpa_Barbuta_Mail_B_inv",ixmesh_inventory), ("Nerpa_Barbuta_Mail_B_inv.1",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 699, weight(2.0)|abundance(100)|head_armor(46)|body_armor(5)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_7] ],

["elen_nasal_a", "Elen Nasal Helmet", [("Elen_Nasal_A",0), ("Elen_Nasal_A.1",0),("Elen_Nasal_A_inv",ixmesh_inventory), ("Elen_Nasal_A_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 144 , weight(1.5)|abundance(100)|head_armor(31)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_10]],
["elen_nasal_b", "Elen Nasal Helmet", [("Elen_Nasal_B",0), ("Elen_Nasal_B.1",0),("Elen_Nasal_B_inv",ixmesh_inventory), ("Elen_Nasal_B_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 144 , weight(1.5)|abundance(100)|head_armor(31)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_10]],

["elen_nasal_padded_a", "Elen Nasal Helmet on Padded", [("Elen_Nasal_Padded_A",0), ("Elen_Nasal_Padded_A.1",0),("Elen_Nasal_Padded_A_inv",ixmesh_inventory), ("Elen_Nasal_Padded_A_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 201 , weight(1.75)|abundance(100)|head_armor(34)|body_armor(3)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_10]],
["elen_nasal_padded_b", "Decorated Elen Nasal Helmet on Padded", [("Elen_Nasal_Padded_B",0), ("Elen_Nasal_Padded_B.1",0), ("Elen_Nasal_Padded_B.2",0),("Elen_Nasal_Padded_B_inv",ixmesh_inventory), ("Elen_Nasal_Padded_B_inv.1",ixmesh_inventory), ("Elen_Nasal_Padded_B_inv.2",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 221 , weight(1.75)|abundance(100)|head_armor(35)|body_armor(3)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_10]],

["elen_nasal_mail_a", "Elen Nasal Helmet on Mail", [("Elen_Nasal_Mail_A",0), ("Elen_Nasal_Mail_A.1",0),("Elen_Nasal_Mail_A_inv",ixmesh_inventory), ("Elen_Nasal_Mail_A_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 261 , weight(2.25)|abundance(100)|head_armor(38)|body_armor(5)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_10]],
["elen_nasal_mail_b", "Elen Nasal Helmet on Mail", [("Elen_Nasal_Mail_B",0), ("Elen_Nasal_Mail_B.1",0), ("Elen_Nasal_Mail_B.2",0),("Elen_Nasal_Mail_B_inv",ixmesh_inventory), ("Elen_Nasal_Mail_B_inv.1",ixmesh_inventory), ("Elen_Nasal_Mail_B_inv.2",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 313 , weight(2.5)|abundance(100)|head_armor(43)|body_armor(5)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_10]],
["elen_nasal_mail_c", "Decorated Elen Nasal Helmet on Mail", [("Elen_Nasal_Mail_C",0), ("Elen_Nasal_Mail_C.1",0), ("Elen_Nasal_Mail_C.2",0), ("Elen_Nasal_Mail_C.3",0) ,("Elen_Nasal_Mail_C_inv",ixmesh_inventory), ("Elen_Nasal_Mail_C_inv.1",ixmesh_inventory), ("Elen_Nasal_Mail_C_inv.2",ixmesh_inventory), ("Elen_Nasal_Mail_C_inv.3",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 313 , weight(2.5)|abundance(100)|head_armor(43)|body_armor(5)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_10]],

["elen_great_helm_a", "Elen Great Helmet", [("Elen_Great_Helm_A",0)], itp_merchandise| itp_type_head_armor   ,0, 1140 , weight(2.5)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_plate, [], [fac_kingdom_10]],
["elen_great_helm_b", "Elen Great Helmet", [("Elen_Great_Helm_B",0)], itp_merchandise| itp_type_head_armor   ,0, 1140 , weight(2.5)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_plate, [], [fac_kingdom_10]],
["elen_great_helm_c", "Elen Great Helmet", [("Elen_Great_Helm_C",0)], itp_merchandise| itp_type_head_armor   ,0, 1140 , weight(2.5)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(11) ,imodbits_plate, [], [fac_kingdom_10]],

["iron_crown_scullcap_a", "Iron Crown Skullcap", [("Iron_Crown_Skull_Cap_A",0), ("Iron_Crown_Skull_Cap_A.1",0),("Iron_Crown_Skull_Cap_A_inv",ixmesh_inventory), ("Iron_Crown_Skull_Cap_A_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 83 , weight(1.0)|abundance(100)|head_armor(24)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_4]],
["iron_crown_scullcap_b", "Iron Crown Skullcap", [("Iron_Crown_Skull_Cap_B",0), ("Iron_Crown_Skull_Cap_B.1",0),("Iron_Crown_Skull_Cap_B_inv",ixmesh_inventory), ("Iron_Crown_Skull_Cap_B_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 83 , weight(1.0)|abundance(100)|head_armor(24)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_4]],

["iron_crown_nasal_a", "Iron Crown Nasal Helmet", [("Iron_Crown_Nasal_D",0), ("Iron_Crown_Nasal_D.1",0),("Iron_Crown_Nasal_D_inv",ixmesh_inventory), ("Iron_Crown_Nasal_D_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 138 , weight(1.5)|abundance(100)|head_armor(29)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_4]],
["iron_crown_nasal_b", "Iron Crown Nasal Helmet", [("Iron_Crown_Nasal_E",0), ("Iron_Crown_Nasal_E.1",0),("Iron_Crown_Nasal_E_inv",ixmesh_inventory), ("Iron_Crown_Nasal_E_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 145 , weight(1.5)|abundance(100)|head_armor(31)|body_armor(3)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_4]],
["iron_crown_nasal_c", "Iron Crown Nasal Helmet", [("Iron_Crown_Nasal_F",0), ("Iron_Crown_Nasal_F.1",0),("Iron_Crown_Nasal_F_inv",ixmesh_inventory), ("Iron_Crown_Nasal_F_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 201 , weight(1.75)|abundance(100)|head_armor(34)|body_armor(5)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_4]],

["iron_crown_nasal_reinforced_a", "Reinforced Iron Crown Nasal Helmet", [("Iron_Crown_Nasal_A",0), ("Iron_Crown_Nasal_A.1",0),("Iron_Crown_Nasal_A_inv",ixmesh_inventory), ("Iron_Crown_Nasal_A_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 156 , weight(1.5)|abundance(100)|head_armor(33)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_4]],
["iron_crown_nasal_reinforced_b", "Reinforced Iron Crown Nasal Helmet", [("Iron_Crown_Nasal_B",0), ("Iron_Crown_Nasal_B.1",0),("Iron_Crown_Nasal_B_inv",ixmesh_inventory), ("Iron_Crown_Nasal_B_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 201 , weight(1.5)|abundance(100)|head_armor(35)|body_armor(2)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_4]],
["iron_crown_nasal_reinforced_c", "Reinforced Iron Crown Nasal Helmet", [("Iron_Crown_Nasal_C",0), ("Iron_Crown_Nasal_C.1",0),("Iron_Crown_Nasal_C_inv",ixmesh_inventory), ("Iron_Crown_Nasal_C_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 291 , weight(1.75)|abundance(100)|head_armor(38)|body_armor(5)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_4]],

["iron_crown_footman_helmet_a", "Iron Crown Footman Helmet", [("Iron_Crown_Footman_Helmet_A",0), ("Iron_Crown_Footman_Helmet_A.1",0),("Iron_Crown_Footman_Helmet_A_inv",ixmesh_inventory), ("Iron_Crown_Footman_Helmet_A_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 238 , weight(1.5)|abundance(100)|head_armor(36)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_4]],
["iron_crown_footman_helmet_b", "Iron Crown Footman Helmet", [("Iron_Crown_Footman_Helmet_B",0), ("Iron_Crown_Footman_Helmet_B.1",0),("Iron_Crown_Footman_Helmet_B_inv",ixmesh_inventory), ("Iron_Crown_Footman_Helmet_B_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 308 , weight(1.5)|abundance(100)|head_armor(39)|body_armor(2)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_4]],
["iron_crown_footman_helmet_c", "Iron Crown Footman Helmet", [("Iron_Crown_Footman_Helmet_C",0), ("Iron_Crown_Footman_Helmet_C.1",0),("Iron_Crown_Footman_Helmet_C_inv",ixmesh_inventory), ("Iron_Crown_Footman_Helmet_C_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 457 , weight(1.75)|abundance(100)|head_armor(43)|body_armor(5)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_4]],

["iron_crown_king_helmet_a", "Iron Crown King Helmet", [("Iron_Crown_King_Helmet_A",0), ("Iron_Crown_King_Helmet_A.1",0),("Iron_Crown_King_Helmet_A_inv",ixmesh_inventory), ("Iron_Crown_King_Helmet_A_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 2899 , weight(1.5)|abundance(1)|head_armor(48)|body_armor(6)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_4]],

["chornovalley_skullcap_helmet_a", "Chornovalley Nasal Helmet", [("Chornovalley_Skullcap_A",0), ("Chornovalley_Skullcap_A.1",0),("Chornovalley_Skullcap_A_inv",ixmesh_inventory), ("Chornovalley_Skullcap_A_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 56 , weight(1.0)|abundance(100)|head_armor(20)|body_armor(3)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_2]],
["chornovalley_skullcap_helmet_b", "Chornovalley Nasal Helmet", [("Chornovalley_Skullcap_B",0), ("Chornovalley_Skullcap_B.1",0),("Chornovalley_Skullcap_B.2",0),("Chornovalley_Skullcap_B_inv",ixmesh_inventory), ("Chornovalley_Skullcap_B_inv.1",ixmesh_inventory),("Chornovalley_Skullcap_B_inv.2",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 69 , weight(1.0)|abundance(100)|head_armor(23)|body_armor(3)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_2]],

["chornovalley_footman_helmet_a", "Chornovalley Nasal Helmet", [("Chornovalley_Nasal_A",0), ("Chornovalley_Nasal_A.1",0),("Chornovalley_Nasal_A_inv",ixmesh_inventory), ("Chornovalley_Nasal_A_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 149 , weight(1.5)|abundance(100)|head_armor(29)|body_armor(3)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_2]],
["chornovalley_footman_helmet_b", "Chornovalley Nasal Helmet on Mail", [("Chornovalley_Nasal_B",0), ("Chornovalley_Nasal_B.1",0),("Chornovalley_Nasal_B_inv",ixmesh_inventory), ("Chornovalley_Nasal_B_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 254 , weight(2.0)|abundance(100)|head_armor(34)|body_armor(3)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_2]],

["chornovalley_infantry_helmet_a", "Chornovalley Infantry Helmet", [("Chornovalley_Infantry_Helmet_A",0), ("Chornovalley_Infantry_Helmet_A.1",0),("Chornovalley_Infantry_Helmet_A_inv",ixmesh_inventory), ("Chornovalley_Infantry_Helmet_A_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 299 , weight(2.0)|abundance(100)|head_armor(37)|body_armor(3)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_2]],
["chornovalley_infantry_helmet_b", "Chornovalley Infantry Helmet with Visor", [("Chornovalley_Infantry_Helmet_B",0), ("Chornovalley_Infantry_Helmet_B.1",0),("Chornovalley_Infantry_Helmet_B.2",0),("Chornovalley_Infantry_Helmet_B_inv",ixmesh_inventory), ("Chornovalley_Infantry_Helmet_B_inv.1",ixmesh_inventory),("Chornovalley_Infantry_Helmet_B.2",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 351 , weight(2.3)|abundance(100)|head_armor(40)|body_armor(3)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_2]],
["chornovalley_infantry_helmet_c", "Chornovalley Infantry Helmet on Mail", [("Chornovalley_Infantry_Helmet_C",0), ("Chornovalley_Infantry_Helmet_C.1",0),("Chornovalley_Infantry_Helmet_C.2",0),("Chornovalley_Infantry_Helmet_C_inv",ixmesh_inventory), ("Chornovalley_Infantry_Helmet_C_inv.1",ixmesh_inventory),("Chornovalley_Infantry_Helmet_C_inv.2",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 413 , weight(2.9)|abundance(100)|head_armor(45)|body_armor(5)|leg_armor(0)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_2]],
["chornovalley_infantry_helmet_d", "Chornovalley Infantry Helmet on Mail", [("Chornovalley_Infantry_Helmet_D",0), ("Chornovalley_Infantry_Helmet_D.1",0),("Chornovalley_Infantry_Helmet_D.2",0),("Chornovalley_Infantry_Helmet_D.3",0),("Chornovalley_Infantry_Helmet_D_inv",ixmesh_inventory), ("Chornovalley_Infantry_Helmet_D_inv.1",ixmesh_inventory),("Chornovalley_Infantry_Helmet_D_inv.2",ixmesh_inventory),("Chornovalley_Infantry_Helmet_D_inv.3",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 419 , weight(2.9)|abundance(100)|head_armor(45)|body_armor(5)|leg_armor(0)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_2]],

["footman_helmet", "Footman's Helmet", [("Skull_Cap_A",0), ("Skull_Cap_A.1",0),("Skull_Cap_A_inv",ixmesh_inventory), ("Skull_Cap_A_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 95 , weight(1.5)|abundance(100)|head_armor(24)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_1]],

["silver_rose_footman_helmet", "Footman's Helmet", [("Silver_Rose_Skull_Cap_A",0), ("Silver_Rose_Skull_Cap_A.1",0),("Silver_Rose_Skull_Cap_A_inv",ixmesh_inventory), ("Silver_Rose_Skull_Cap_A_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 95 , weight(1.5)|abundance(100)|head_armor(24)|body_armor(3)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_1]],
["silver_rose_footman_helmet_cloth", "Footman's Helmet", [("Silver_Rose_Skull_Cap_B",0), ("Silver_Rose_Skull_Cap_B.1",0),("Silver_Rose_Skull_Cap_B_inv",ixmesh_inventory), ("Silver_Rose_Skull_Cap_B_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 80 , weight(1.5)|abundance(100)|head_armor(24)|body_armor(2)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_1]],

["silver_rose_capelina_a", "Silver Rose Capelina", [("Silver_Rose_Capelina_A",0), ("Silver_Rose_Capelina_A.1",0),("Silver_Rose_Capelina_A_inv",ixmesh_inventory), ("Silver_Rose_Capelina_A_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 135 , weight(1.5)|abundance(100)|head_armor(34)|body_armor(2)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_1]],
["silver_rose_capelina_b", "Silver Rose Capelina", [("Silver_Rose_Capelina_B",0), ("Silver_Rose_Capelina_B.1",0),("Silver_Rose_Capelina_B_inv",ixmesh_inventory), ("Silver_Rose_Capelina_B_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 135 , weight(1.5)|abundance(100)|head_armor(34)|body_armor(2)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_1]],

["silver_rose_capelina_mail_a", "Silver Rose Capelina on Mail", [("Silver_Rose_Capelina_C",0), ("Silver_Rose_Capelina_C.1",0),("Silver_Rose_Capelina_C_inv",ixmesh_inventory), ("Silver_Rose_Capelina_B_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 231 , weight(2.0)|abundance(100)|head_armor(36)|body_armor(5)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_1]],
["silver_rose_capelina_mail_b", "Silver Rose Capelina with Mask", [("Silver_Rose_Capelina_D",0), ("Silver_Rose_Capelina_D.1",0),("Silver_Rose_Capelina_D.2",0),("Silver_Rose_Capelina_D_inv",ixmesh_inventory), ("Silver_Rose_Capelina_D_inv.1",ixmesh_inventory), ("Silver_Rose_Capelina_D_inv.2",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 317 , weight(3.0)|abundance(100)|head_armor(44)|body_armor(5)|leg_armor(0)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_1]],

["silver_rose_mask", "Mask Helmet", [("Silver_Rose_Mask_A",0), ("Silver_Rose_Mask_A.1",0),("Silver_Rose_Mask_A_inv",ixmesh_inventory), ("Silver_Rose_Mask_A_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 280 , weight(2.5)|abundance(100)|head_armor(41)|body_armor(2)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_1]],
["silver_rose_mask_mail", "Mask Helmet with Mail", [("Silver_Rose_Mask_B",0), ("Silver_Rose_Mask_B.1",0),("Silver_Rose_Mask_B_inv",ixmesh_inventory), ("Silver_Rose_Mask_B_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 357 , weight(3.0)|abundance(100)|head_armor(45)|body_armor(5)|leg_armor(0)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_1]],

#missing...
["nasal_helmet", "Nasal Helmet", [("nasal_helmet_b",0)], itp_merchandise| itp_type_head_armor   ,0, 121 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["norman_helmet", "Helmet with Cap", [("norman_helmet_a",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head ,0, 147 , weight(1.25)|abundance(100)|head_armor(28)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["segmented_helmet", "Segmented Helmet", [("segmented_helm_new",0)], itp_merchandise| itp_type_head_armor   ,0, 174 , weight(1.25)|abundance(100)|head_armor(31)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["helmet_with_neckguard", "Helmet with Neckguard", [("neckguard_helm_new",0)], itp_merchandise| itp_type_head_armor   ,0, 
190 , weight(1.5)|abundance(100)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["flat_topped_helmet", "Flat Topped Helmet", [("Flattop_Helmet_A",0),("Flattop_Helmet_A.1",0),("Flattop_Helmet_A.2",0),("Flattop_Helmet_A_inv",ixmesh_inventory), ("Flattop_Helmet_A_inv.1",ixmesh_inventory), ("Flattop_Helmet_A_inv.2",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 
203 , weight(1.75)|abundance(100)|head_armor(33)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_1]],
["kettle_hat", "Kettle Hat", [("kettle_hat_new",0)], itp_merchandise| itp_type_head_armor,0, 
240 , weight(1.75)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["m_spiked_helmet_a", "Spiked Helmet on Padded", [("Spiked_Helmet_A",0), ("Spiked_Helmet_A.1",0),("Spiked_Helmet_A_inv",ixmesh_inventory), ("Spiked_Helmet_A_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 209 , weight(1.75)|abundance(100)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_1]],
["silver_rose_spiked_helmet_a", "Spiked Helmet on Padded", [("Silver_Rose_Spiked_Helmet_A",0), ("Silver_Rose_Spiked_Helmet_A.1",0),("Silver_Rose_Spiked_Helmet_A_inv",ixmesh_inventory), ("Silver_Rose_Spiked_Helmet_A_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 209 , weight(1.75)|abundance(100)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_1]],
["silver_rose_spiked_helmet_b", "Spiked Helmet on Padded", [("Silver_Rose_Spiked_Helmet_B",0), ("Silver_Rose_Spiked_Helmet_B.1",0),("Silver_Rose_Spiked_Helmet_B_inv",ixmesh_inventory), ("Silver_Rose_Spiked_Helmet_B_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 209 , weight(1.75)|abundance(100)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_1]],

["spiked_helmet", "Spiked Helmet", [("Spiked_Helmet_B",0), ("Spiked_Helmet_B.1",0),("Spiked_Helmet_B_inv",ixmesh_inventory), ("Spiked_Helmet_B_inv.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 278 , weight(2)|abundance(100)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_1]],

["silver_rose_scout_helmet_a", "Silver Rose Scout Helmet", [("Silver_Rose_Scout_Helmet_A",0), ("Silver_Rose_Scout_Helmet_A.1",0),("Silver_Rose_Scout_Helmet_A.2",0),("Silver_Rose_Scout_Helmet_A_inv",ixmesh_inventory), ("Silver_Rose_Scout_Helmet_A_inv.1",ixmesh_inventory), ("Silver_Rose_Scout_Helmet_A_inv.2",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 209 , weight(1.75)|abundance(100)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_1]],

["m_bandit_turban_a", "Turban", [("beduin_turban_a",0),("beduin_turban_a_mark",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 56 , weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_11]],
["m_bandit_turban_b", "Turban", [("beduin_turban_b",0),("beduin_turban_b_mark",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 56 , weight(1)|abundance(100)|head_armor(11)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_11]],
["m_bandit_turban_c", "Turban", [("beduin_turban_c",0),("beduin_turban_c.1",0),("beduin_turban_c_mark",ixmesh_inventory),("beduin_turban_c_mark.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 56 , weight(1)|abundance(100)|head_armor(12)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_11]],
["m_bandit_turban_d", "Turban", [("beduin_turban_d",0),("beduin_turban_d.1",0),("beduin_turban_d_mark",ixmesh_inventory),("beduin_turban_d_mark.1",ixmesh_inventory)], itp_merchandise| itp_type_head_armor|itp_attach_armature   ,0, 56 , weight(1)|abundance(100)|head_armor(12)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_11]],

["adid_cavalry_helmet_a","Adid Cavalry Helmet", [("gulam_helm_a", 0)], itp_type_head_armor|itp_merchandise|itp_fit_to_head, 0,519, weight(2)|abundance(100)|head_armor(45)|difficulty(7), imodbits_none, [], [fac_kingdom_11]],
["adid_helmet_a","Adid Helmet", [("gulam_helm_b", 0),("gulam_helm_b_market", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise|itp_fit_to_head, 0,390, weight(2)|abundance(100)|head_armor(38)|difficulty(7), imodbits_none, [], [fac_kingdom_11]],
["adid_helmet_b","Adid Helmet", [("gulam_helm_c", 0),("gulam_helm_c_market", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise|itp_fit_to_head, 0,390, weight(2)|abundance(100)|head_armor(37)|difficulty(7), imodbits_none, [], [fac_kingdom_11]],
["adid_helmet_c","Adid Helmet", [("gulam_helm_d", 0),("gulam_helm_d_market", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise|itp_fit_to_head, 0,390, weight(2)|abundance(100)|head_armor(39)|difficulty(7), imodbits_none, [], [fac_kingdom_11]],
["adid_elite_helmet_a","Adid Heavy Helmet", [("gulam_helm_f", 0),("gulam_helm_f_market", ixmesh_inventory)], itp_type_head_armor|itp_attach_armature|itp_merchandise|itp_fit_to_head|itp_covers_beard, 0,894, weight(2)|abundance(100)|head_armor(49)|difficulty(9), imodbits_none, [], [fac_kingdom_11]],

["nordic_helmet", "Nordic Helmet", [("helmet_w_eyeguard_new",0)], itp_merchandise| itp_type_head_armor   ,0, 340 , weight(2)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["khergit_lady_hat", "Khergit Lady Hat", [("khergit_lady_hat",0)],  itp_type_head_armor   |itp_civilian |itp_doesnt_cover_hair | itp_fit_to_head,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["khergit_lady_hat_b", "Khergit Lady Leather Hat", [("khergit_lady_hat_b",0)], itp_type_head_armor  | itp_doesnt_cover_hair | itp_fit_to_head  |itp_civilian ,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["sarranid_felt_hat", "Eastern Felt Hat", [("sar_helmet3",0)], itp_merchandise| itp_type_head_armor   ,0, 16 , weight(2)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_cloth ],
["turban", "Turban", [("tuareg_open",0)], itp_merchandise| itp_type_head_armor   ,0, 28 , weight(1)|abundance(100)|head_armor(11)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_cloth ],
["desert_turban", "Desert Turban", [("tuareg",0)], itp_merchandise| itp_type_head_armor | itp_covers_beard ,0, 38 , weight(1.50)|abundance(100)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_cloth ],
["sarranid_warrior_cap", "Eastern Warrior Cap", [("tuareg_helmet",0)], itp_merchandise| itp_type_head_armor | itp_covers_beard  ,0, 90 , weight(2)|abundance(100)|head_armor(19)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["solarian_horseman_helmet", "Horseman Helmet", [("sar_helmet2",0)], itp_merchandise| itp_type_head_armor   ,0, 180 , weight(2.75)|abundance(100)|head_armor(25)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["sarranid_helmet1", "Eastern Keffiyeh Helmet", [("sar_helmet1",0)], itp_merchandise| itp_type_head_armor   ,0, 290 , weight(2.50)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["sarranid_mail_coif", "Eastern Mail Coif", [("tuareg_helmet2",0)], itp_merchandise| itp_type_head_armor ,0, 430 , weight(3)|abundance(100)|head_armor(41)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["sarranid_veiled_helmet", "Eastern Veiled Helmet", [("sar_helmet4",0)], itp_merchandise| itp_type_head_armor | itp_covers_beard  ,0, 810 , weight(3.50)|abundance(100)|head_armor(47)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
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
["m_bascinet_a", "Bascinet", [("zitta_bascinet_novisor",0),("zitta_bascinet_novisor_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 559, weight(2)|abundance(100)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_3] ],
["m_bascinet_b", "Visored Bascinet", [("zitta_bascinet",0),("zitta_bascinet_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 659, weight(2.5)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_3] ],

["bascinet", "Sallet", [("sallet_a",0),("sallet_a.1",0),("sallet_a_inv",ixmesh_inventory),("sallet_a_inv.1",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature   ,0, 479 , weight(2.25)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_3]],
["bascinet_2", "Sallet on Mail", [("sallet_a_mail",0),("sallet_a_mail.1",0),("sallet_a_mail_inv",ixmesh_inventory),("sallet_a_mail_inv.1",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature   ,0, 479 , weight(2.25)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_3]],
["bascinet_3", "Closed Sallet on Mail", [("sallet_a_mail_closed",0),("sallet_a_mail_closed.1",0),("sallet_a_mail_closed_inv",ixmesh_inventory),("sallet_a_mail_closed_inv.1",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature   ,0, 479 , weight(2.25)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_3]],

["m_chapel_light_a", "Chapel-De-Fer on Cloth", [("chapel_de_fer_cloth1",0), ("chapel_de_fer_cloth1.1",0),("chapel_de_fer_cloth1_inv",ixmesh_inventory), ("chapel_de_fer_cloth1_inv.1",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 459, weight(2)|abundance(100)|head_armor(43)|body_armor(2)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_7] ],
["m_chapel_light_b", "Chapel-De-Fer on Padded", [("chapel_de_fer_cloth2",0), ("chapel_de_fer_cloth2.1",0),("chapel_de_fer_cloth2_inv",ixmesh_inventory), ("chapel_de_fer_cloth2_inv.1",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 499, weight(2)|abundance(100)|head_armor(43)|body_armor(4)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_7] ],
["m_chapel_light_c", "Chapel-De-Fer on Cloth", [("chapel_de_fer_cloth3",0), ("chapel_de_fer_cloth3.1",0),("chapel_de_fer_cloth3_inv",ixmesh_inventory), ("chapel_de_fer_cloth3_inv.1",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 499, weight(2)|abundance(100)|head_armor(43)|body_armor(4)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_7] ],

["m_kattle_a", "Eyeslot Kattlehat", [("eyeslot_kettlehat",0), ("eyeslot_kettlehat.1",0),("eyeslot_kettlehat_inv",ixmesh_inventory), ("eyeslot_kettlehat_inv.1",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 499, weight(2)|abundance(100)|head_armor(43)|body_armor(2)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_7] ],

["m_chapel_heavy_a", "Chapel-De-Fer on Mail", [("chapel_de_fer_mail1",0), ("chapel_de_fer_mail1.1",0),("chapel_de_fer_mail1_inv",ixmesh_inventory), ("chapel_de_fer_mail1_inv.1",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 659, weight(2.5)|abundance(100)|head_armor(46)|body_armor(8)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_7] ],
["m_chapel_heavy_b", "Chapel-De-Fer on Mail", [("chapel_de_fer_mail2",0), ("chapel_de_fer_mail2.1",0),("chapel_de_fer_mail2_inv",ixmesh_inventory), ("chapel_de_fer_mail2_inv.1",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 659, weight(2.5)|abundance(100)|head_armor(46)|body_armor(8)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_7] ],
["m_chapel_heavy_c", "Chapel-De-Fer on Mail", [("chapel_de_fer_mail3",0), ("chapel_de_fer_mail3.1",0),("chapel_de_fer_mail3_inv",ixmesh_inventory), ("chapel_de_fer_mail3_inv.1",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 659, weight(2.5)|abundance(100)|head_armor(46)|body_armor(8)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_7] ],

["m_sallet_light_a", "Sallet", [("sallet_c",0), ("sallet_c.1",0),("sallet_c_inv",ixmesh_inventory), ("sallet_c_inv.1",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 399, weight(1.75)|abundance(100)|head_armor(39)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_7] ],
["m_sallet_light_b", "Sallet with Bevor", [("sallet_c_bevor",0), ("sallet_c_bevor.1",0), ("sallet_c_bevor.2",0),("sallet_c_bevor_inv",ixmesh_inventory), ("sallet_c_bevor_inv.1",ixmesh_inventory), ("sallet_c_bevor_inv.2",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 499, weight(2)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_7] ],
["m_sallet_light_c", "Sallet on Cloth", [("sallet_d",0), ("sallet_d.1",0),("sallet_d_inv",ixmesh_inventory), ("sallet_d_inv.1",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 399, weight(2)|abundance(100)|head_armor(39)|body_armor(2)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_7] ],

["m_sallet_heavy_a", "Closed Sallet", [("sallet_a_closed1",0), ("sallet_a_closed1.1",0), ("sallet_a_closed1.2", 0),("sallet_a_closed1_inv",ixmesh_inventory), ("sallet_a_closed1_inv.1",ixmesh_inventory), ("sallet_a_closed1_inv.2",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 599, weight(2.5)|abundance(100)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_7] ],
["m_sallet_heavy_b", "Closed Sallet", [("sallet_a_closed2",0), ("sallet_a_closed2.1",0), ("sallet_a_closed2.2", 0),("sallet_a_closed2_inv",ixmesh_inventory), ("sallet_a_closed2_inv.1",ixmesh_inventory), ("sallet_a_closed2_inv.2",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 599, weight(2.5)|abundance(100)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_7] ],
["m_sallet_heavy_c", "Open Sallet", [("sallet_a_open1",0), ("sallet_a_open1.1",0),("sallet_a_open1_inv",ixmesh_inventory), ("sallet_a_open1_inv.1",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 499, weight(2.5)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_7] ],
["m_sallet_heavy_d", "Open Sallet", [("sallet_a_open2",0), ("sallet_a_open2.1",0),("sallet_a_open2_inv",ixmesh_inventory), ("sallet_a_open2_inv.1",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 499, weight(2.5)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_7] ],

["m_sallet_black_a", "Closed Sallet Black", [("sallet_b_closed1",0), ("sallet_b_closed1.1",0), ("sallet_b_closed1.2", 0),("sallet_b_closed1_inv",ixmesh_inventory), ("sallet_b_closed1_inv.1",ixmesh_inventory), ("sallet_b_closed1_inv.2",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 599, weight(2.5)|abundance(100)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_7] ],
["m_sallet_black_b", "Closed Sallet Black", [("sallet_b_closed2",0), ("sallet_b_closed2.1",0), ("sallet_b_closed2.2", 0),("sallet_b_closed2_inv",ixmesh_inventory), ("sallet_b_closed2_inv.1",ixmesh_inventory), ("sallet_b_closed2_inv.2",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 599, weight(2.5)|abundance(100)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_7] ],
["m_sallet_black_c", "Open Sallet Black", [("sallet_b_open1",0), ("sallet_b_open1.1",0),("sallet_b_open1_inv",ixmesh_inventory), ("sallet_b_open1_inv.1",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 499, weight(2.5)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_7] ],
["m_sallet_black_d", "Open Sallet Black", [("sallet_b_open2",0), ("sallet_b_open2.1",0),("sallet_b_open2_inv",ixmesh_inventory), ("sallet_b_open2_inv.1",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_attach_armature, 0, 499, weight(2.5)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_7] ],

["guard_helmet", "Guard Helmet", [("reinf_helmet_new",0)], itp_merchandise| itp_type_head_armor   ,0, 555 , weight(2.5)|abundance(100)|head_armor(47)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["black_helmet", "Black Helmet", [("black_helm",0)], itp_type_head_armor,0, 638 , weight(2.75)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["full_helm", "Full Helm", [("great_helmet_new_b",0)], itp_merchandise| itp_type_head_armor |itp_covers_head ,0, 811 , weight(2.5)|abundance(100)|head_armor(51)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["great_helmet", "Great Helmet", [("great_helmet_new",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0, 980 , weight(2.75)|abundance(100)|head_armor(53)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["winged_great_helmet", "Winged Great Helmet", [("maciejowski_helmet_new",0)], itp_merchandise|itp_type_head_armor|itp_covers_head,0, 1240 , weight(2.75)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],


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
["pickaxe",         "Pickaxe", [("bb_pickaxe_1_bigger",0)], itp_craftable|itp_type_one_handed_wpn|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
27 , weight(3)|difficulty(0)|spd_rtng(99) | weapon_length(70)|swing_damage(19 , pierce) | thrust_damage(0 ,  pierce),imodbits_pick ],
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

["falchion",         "Falchion", [("luc_falchion",0)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 
105 , weight(2.5)|difficulty(8)|spd_rtng(98) | weapon_length(73)|swing_damage(30 , cut) | thrust_damage(0 ,  pierce),imodbits_sword ],
["eastern_falchion", "Eastern Falchion", [("luc_sarranid_falchion",0)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 189 , weight(2.75)|difficulty(8)|spd_rtng(95) | weapon_length(90)|swing_damage(30 , cut) | thrust_damage(0 ,  pierce),imodbits_sword ],
["straight_falchion", "Falchion", [("luc_english_falchion",0)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 235 , weight(2.75)|difficulty(9)|spd_rtng(95) | weapon_length(88)|swing_damage(32 , cut) | thrust_damage(0 ,  pierce),imodbits_sword ],
["shortened_bill",         "Bill", [("luc_shortened_bill",0)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 
199 , weight(2.5)|difficulty(8)|spd_rtng(98) | weapon_length(73)|swing_damage(33 , cut) | thrust_damage(0 ,  pierce),imodbits_sword ],

["falshion_1","Falshion", [("falshion_1", 0),("falshion_1_scab", ixmesh_carry)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itc_scimitar,200, weight(2)|abundance(100)|difficulty(8)|spd_rtng(100)|weapon_length(63)|thrust_damage(0, pierce)|swing_damage(28, cut), imodbits_none, [], [fac_kingdom_1]],
["falshion_2","Falshion", [("falshion_2", 0)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_carry_sword_left_hip|itc_scimitar,105, weight(2.5)|abundance(100)|difficulty(8)|spd_rtng(96)|weapon_length(73)|thrust_damage(0, pierce)|swing_damage(28, cut), imodbits_none, [], [fac_kingdom_6]],

["scimitar",         "Scimitar", [("scimitar_a",0),("scab_scimeter_a", ixmesh_carry)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(1.5)|difficulty(0)|spd_rtng(101) | weapon_length(97)|swing_damage(30 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],
["scimitar_b",         "Elite Scimitar", [("scimitar_b",0),("scab_scimeter_b", ixmesh_carry)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
290 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(103)|swing_damage(32 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],
["m_scimitar_a", "Zulfiqar", [("luc_zulfiqar",0)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 308 , weight(1.5)|difficulty(9)|spd_rtng(100) | weapon_length(99)|swing_damage(33 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],

["arabian_sword_a",         "Solarian Sword", [("saracin_sword_a",0),("scab_saracin_sword_a", ixmesh_carry)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 108 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(97)|swing_damage(26 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high ],
["arabian_sword_b",         "Solarian Arming Sword", [("saracin_sword_b",0),("scab_saracin_sword_b", ixmesh_carry)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 218 , weight(1.7)|difficulty(0)|spd_rtng(99) | weapon_length(97)|swing_damage(28 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high ],
["sarranid_cavalry_sword",         "Solarian Cavalry Sword", [("saracin_sword_d",0),("scab_saracin_sword_d", ixmesh_carry)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 310 , weight(1.5)|difficulty(0)|spd_rtng(98) | weapon_length(103)|swing_damage(28 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high ],
["arabian_sword_d",         "Solarian Guard Sword", [("saracin_sword_c",0),("scab_saracin_sword_c", ixmesh_carry)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,  420 , weight(1.7)|difficulty(0)|spd_rtng(99) | weapon_length(103)|swing_damage(30 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ],
["arabian_sword_c", "Solarian Guard Sword", [("saracin_sword_e",0),("scab_saracin_sword_e", ixmesh_carry)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 460 , weight(1.7)|difficulty(0)|spd_rtng(99) | weapon_length(103)|swing_damage(32 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ],

["great_sword",         "Great Sword", [("luc_sword_of_war_z1",0),("luc_sword_of_war_z1_scab", ixmesh_carry)], itp_craftable|itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back|itcf_show_holster_when_drawn,
 423 , weight(2.75)|difficulty(10)|spd_rtng(95) | weapon_length(125)|swing_damage(39 , cut) | thrust_damage(31 ,  pierce),imodbits_sword_high ],
["sword_of_war", "Sword of War", [("luc_sword_of_war_z1",0),("luc_sword_of_war_z1_scab", ixmesh_carry)], itp_craftable|itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back|itcf_show_holster_when_drawn,
 524 , weight(3)|difficulty(11)|spd_rtng(94) | weapon_length(130)|swing_damage(40 , cut) | thrust_damage(31 ,  pierce),imodbits_sword_high ],
["hatchet",         "Hatchet", [("luc_hatchet_g",0)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
13 , weight(2)|difficulty(0)|spd_rtng(97) | weapon_length(60)|swing_damage(23 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["hand_axe",         "Hand Axe", [("hatchet_k2",0)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
24 , weight(2)|difficulty(7)|spd_rtng(95) | weapon_length(75)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["fighting_axe", "Fighting Axe", [("luc_burgundian_axe",0)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
77 , weight(2.5)|difficulty(9)|spd_rtng(92) | weapon_length(90)|swing_damage(31 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["heavy_infantry_axe", "Heavy Infantry Axe", [("luc_german_horseman_axe",0)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
179 , weight(2.5)|difficulty(9)|spd_rtng(95) | weapon_length(80)|swing_damage(32 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["axe", "Axe", [("luc_executioners_axe",0)], itp_craftable|itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 
65 , weight(4)|difficulty(8)|spd_rtng(91) | weapon_length(108)|swing_damage(32 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["voulge_short", "Voulge", [("voulge",0)], itp_craftable|itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 
129 , weight(4.5)|difficulty(8)|spd_rtng(87) | weapon_length(119)|swing_damage(35 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["battle_axe", "Battle Axe", [("luc_battle_axe",0)], itp_craftable|itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 
240 , weight(5)|difficulty(9)|spd_rtng(88) | weapon_length(108)|swing_damage(41 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["war_axe", "War Axe", [("luc_war_axe",0)], itp_craftable|itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 
264 , weight(5)|difficulty(10)|spd_rtng(86) | weapon_length(110)|swing_damage(43 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["sword_two_handed_b",         "Two Handed Sword", [("sword_two_handed_b",0)], itp_craftable|itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back,
 670 , weight(2.75)|difficulty(10)|spd_rtng(97) | weapon_length(110)|swing_damage(40 , cut) | thrust_damage(28 ,  pierce),imodbits_sword_high ],
["sword_two_handed_a",         "Great Sword", [("sword_two_handed_a",0)], itp_craftable|itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back,
 1123 , weight(2.75)|difficulty(10)|spd_rtng(96) | weapon_length(120)|swing_damage(42 , cut) | thrust_damage(29 ,  pierce),imodbits_sword_high ],


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
["m_one_handed_knight_axe_a", "One Handed Knight Axe", [("luc_knightly_axe_one_handed",0)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 671 , weight(2.5)|difficulty(11)|spd_rtng(98) | weapon_length(85)|swing_damage(37 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["m_one_handed_knight_axe_b", "One Handed Knight Axe", [("luc_knightly_axe_one_handed_b",0)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 699 , weight(2.5)|difficulty(11)|spd_rtng(98) | weapon_length(90)|swing_damage(37 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["m_two_handed_knight_axe_b","Two Handed Knight Axe", [("luc_knightly_axe_two_handed",0)], itp_craftable|itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,679 , weight(4.0)|difficulty(13)|spd_rtng(99) | weapon_length(95)|swing_damage(44 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["m_two_handed_heavy_axe_a","Heavy Two Handed Axe", [("luc_two_handed_axe_1",0)], itp_craftable|itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,199 , weight(4.0)|difficulty(10)|spd_rtng(99) | weapon_length(90)|swing_damage(38 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["m_two_handed_heavy_axe_b","Heavy Two Handed Axe", [("luc_two_handed_axe_2",0)], itp_craftable|itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,199 , weight(4.0)|difficulty(10)|spd_rtng(99) | weapon_length(90)|swing_damage(38 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

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
["m_voulge_a", "Army Voulge", [("luc_saxon_voulge",0)], itp_type_polearm|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itcf_carry_spear|itc_staff, 299 , weight(3.5)|difficulty(12)|spd_rtng(88) | weapon_length(175)|swing_damage(45 , cut) | thrust_damage(19 ,  pierce),imodbits_axe ],
["m_voulge_b", "Army Voulge", [("luc_saxon_voulge_b",0)], itp_type_polearm|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itcf_carry_spear|itc_staff, 345 , weight(3.75)|difficulty(12)|spd_rtng(86) | weapon_length(175)|swing_damage(47 , cut) | thrust_damage(21 ,  pierce),imodbits_axe ],
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

["crusader_sword_a","Swort Sword", [("crusaders_swords_a", 0),("crusader_sword_a_scabbard", ixmesh_carry)], itp_craftable|itp_type_one_handed_wpn|itp_primary, itcf_carry_sword_left_hip|itc_longsword|itcf_show_holster_when_drawn,299, weight(1.5)|abundance(100)|spd_rtng(105)|weapon_length(75)|thrust_damage(20, pierce)|swing_damage(28, cut), imodbits_none, []],
["crusader_sword_b","Sword", [("crusader_sword_b", 0),("crusader_sword_b_scabbard", ixmesh_carry)], itp_craftable|itp_type_one_handed_wpn|itp_primary, itcf_carry_sword_left_hip|itc_longsword|itcf_show_holster_when_drawn,299, weight(1.5)|abundance(100)|spd_rtng(102)|weapon_length(86)|thrust_damage(20, pierce)|swing_damage(28, cut), imodbits_none, []],
["crusader_sword_c","Sword", [("crusader_sword_c", 0),("crusader_sword_c_scabbard", ixmesh_carry)], itp_craftable|itp_type_one_handed_wpn|itp_primary, itcf_carry_sword_left_hip|itc_longsword|itcf_show_holster_when_drawn,299, weight(1.5)|abundance(100)|spd_rtng(102)|weapon_length(86)|thrust_damage(20, pierce)|swing_damage(28, cut), imodbits_none, []],

["crusader_long_sword_a","Long Sword", [("crusader_long_sword_a", 0),("crusader_long_sword_a_scabbard", ixmesh_carry)], itp_craftable|itp_type_one_handed_wpn|itp_primary, itcf_carry_sword_left_hip|itc_longsword|itcf_show_holster_when_drawn,526, weight(4)|abundance(100)|spd_rtng(100)|weapon_length(100)|swing_damage(34, cut)|thrust_damage(26, pierce), imodbits_none, [], [fac_kingdom_1]],
["crusader_long_sword_b","Long Sword", [("crusader_long_sword_b", 0),("crusader_long_sword_b_scabbard", ixmesh_carry)], itp_craftable|itp_type_one_handed_wpn|itp_primary, itcf_carry_sword_left_hip|itc_longsword|itcf_show_holster_when_drawn,526, weight(4)|abundance(100)|spd_rtng(100)|weapon_length(100)|swing_damage(34, cut)|thrust_damage(26, pierce), imodbits_none, [], [fac_kingdom_1]],
["crusader_long_sword_c","Long Sword", [("crusader_long_sword_c", 0),("crusader_long_sword_c_scabbard", ixmesh_carry)], itp_craftable|itp_type_one_handed_wpn|itp_primary, itcf_carry_sword_left_hip|itc_longsword|itcf_show_holster_when_drawn,526, weight(4)|abundance(100)|spd_rtng(100)|weapon_length(100)|swing_damage(34, cut)|thrust_damage(26, pierce), imodbits_none, [], [fac_kingdom_1]],

["k_long_sword_a","Knight Lognsword", [("k_long_sword_a", 0),("k_long_sword_a_scabbard", ixmesh_carry)], itp_craftable|itp_type_one_handed_wpn|itp_primary, itcf_carry_sword_left_hip|itc_longsword|itcf_show_holster_when_drawn,679, weight(4)|abundance(100)|spd_rtng(100)|weapon_length(100)|swing_damage(37, cut)|thrust_damage(31, pierce), imodbits_none, [], [fac_kingdom_1]],
["k_long_sword_b","Knight Lognsword", [("k_long_sword_b", 0),("k_long_sword_b_scabbard", ixmesh_carry)], itp_craftable|itp_type_one_handed_wpn|itp_primary, itcf_carry_sword_left_hip|itc_longsword|itcf_show_holster_when_drawn,679, weight(4)|abundance(100)|spd_rtng(100)|weapon_length(100)|swing_damage(37, cut)|thrust_damage(31, pierce), imodbits_none, [], [fac_kingdom_1]],
["k_long_sword_c","Knight Lognsword", [("k_long_sword_c", 0),("k_long_sword_c_scabbard", ixmesh_carry)], itp_craftable|itp_type_one_handed_wpn|itp_primary, itcf_carry_sword_left_hip|itc_longsword|itcf_show_holster_when_drawn,679, weight(4)|abundance(100)|spd_rtng(100)|weapon_length(100)|swing_damage(37, cut)|thrust_damage(31, pierce), imodbits_none, [], [fac_kingdom_1]],

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

["m_morningstar_a", "Light Morningstar", [("luc_morningstar",0)], itp_craftable|itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 499 , weight(3.0)|difficulty(8)|spd_rtng(98) | weapon_length(75)|swing_damage(26 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],
["m_morningstar_b", "Light Morningstar", [("luc_morningstar_2",0)], itp_craftable|itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 499 , weight(3.0)|difficulty(8)|spd_rtng(98) | weapon_length(75)|swing_damage(26 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],
["m_morningstar_c", "Light Morningstar", [("luc_morningstar_3",0)], itp_craftable|itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 569 , weight(3.0)|difficulty(9)|spd_rtng(98) | weapon_length(80)|swing_damage(31 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],
["m_mace_army", "Army Mace", [("luc_mace_straight_hard",0)], itp_craftable|itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 334 , weight(3.0)|difficulty(0)|spd_rtng(98) | weapon_length(75)|swing_damage(26 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
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

["sarranid_two_handed_mace_1",         "Iron Mace", [("mace_long_d",0)], itp_craftable|itp_type_two_handed_wpn|itp_can_knock_down|itp_two_handed|itp_merchandise| itp_primary|itp_crush_through|itp_unbalanced, itc_greatsword|itcf_carry_axe_back,
470 , weight(4.5)|difficulty(0)|spd_rtng(90) | weapon_length(95)|swing_damage(35 , blunt) | thrust_damage(22 ,  blunt),imodbits_mace ],

["m_two_handed_ball_mace", "Ball Mace", [("luc_ball_mace_two_handed",0)], itp_craftable|itp_type_two_handed_wpn|itp_can_knock_down|itp_two_handed|itp_merchandise| itp_primary|itp_crush_through|itp_unbalanced, itc_greatsword|itcf_carry_axe_back,470 , weight(4.5)|difficulty(0)|spd_rtng(90) | weapon_length(95)|swing_damage(35 , blunt) | thrust_damage(22 ,  blunt),imodbits_mace ],
["m_two_handed_flanged_mace", "Flanged Mace", [("luc_flanged_two_handed",0)], itp_craftable|itp_type_two_handed_wpn|itp_can_knock_down|itp_two_handed|itp_merchandise| itp_primary|itp_crush_through|itp_unbalanced, itc_greatsword|itcf_carry_axe_back,470 , weight(4.5)|difficulty(0)|spd_rtng(90) | weapon_length(95)|swing_damage(35 , blunt) | thrust_damage(22 ,  blunt),imodbits_mace ],

["m_one_handed_ball_mace", "Ball Mace", [("luc_ball_mace_one_handed",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 899 , weight(3.0)|difficulty(11)|spd_rtng(98) | weapon_length(75)|swing_damage(32 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["m_one_handed_flanged_mace", "Flanged Mace", [("luc_flanged_one_handed",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 899 , weight(3.0)|difficulty(11)|spd_rtng(98) | weapon_length(75)|swing_damage(32 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],

["sarranid_mace_1",         "Iron Mace", [("mace_small_d",0)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise|itp_can_knock_down |itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
 45 , weight(2.0)|difficulty(0)|spd_rtng(99) | weapon_length(73)|swing_damage(22 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["sarranid_axe_a", "Iron Battle Axe", [("one_handed_battle_axe_g",0)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 250 , weight(1.65)|difficulty(9)|spd_rtng(97) | weapon_length(71)|swing_damage(35 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["sarranid_axe_b", "Iron War Axe", [("one_handed_battle_axe_h",0)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 360 , weight(1.75)|difficulty(9)|spd_rtng(97) | weapon_length(71)|swing_damage(38 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["m_iron_axe_a", "Iron War Axe", [("luc_iron_hand_axe_g",0)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 360 , weight(1.75)|difficulty(9)|spd_rtng(97) | weapon_length(71)|swing_damage(38 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["m_iron_axe_b", "Iron War Axe", [("luc_iron_hand_axe_h",0)], itp_craftable|itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 360 , weight(1.75)|difficulty(9)|spd_rtng(97) | weapon_length(71)|swing_damage(38 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["sarranid_two_handed_axe_a",         "Eastern Battle Axe", [("two_handed_battle_axe_g",0)], itp_craftable|itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 350 , weight(3.0)|difficulty(10)|spd_rtng(89) | weapon_length(95)|swing_damage(49 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["sarranid_two_handed_axe_b",         "Eastern War Axe", [("two_handed_battle_axe_h",0)], itp_craftable|itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 280 , weight(2.50)|difficulty(10)|spd_rtng(90) | weapon_length(90)|swing_damage(46 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

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
["m_pole_hammer_a",  "Pole Hammer", [("luc_pole_hammer_z",0)], itp_craftable|itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed, itc_cutting_spear|itcf_carry_spear, 515 , weight(3.0)|difficulty(0)|spd_rtng(83) | weapon_length(120)|swing_damage(38, blunt) | thrust_damage(38 ,  pierce),imodbits_polearm ],
# 378 , weight(3.5)|difficulty(12)|spd_rtng(92) | weapon_length(160)|swing_damage(20 ,blunt) | thrust_damage(31 ,  pierce),imodbits_polearm ],
["m_pole_hammer_b",  "Pole Hammer", [("luc_polehammer_z4",0)], itp_craftable|itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed, itc_cutting_spear|itcf_carry_spear, 515 , weight(3.0)|difficulty(0)|spd_rtng(83) | weapon_length(120)|swing_damage(38, blunt) | thrust_damage(38 ,  pierce),imodbits_polearm ],
# 378 , weight(3.5)|difficulty(12)|spd_rtng(92) | weapon_length(160)|swing_damage(20 ,blunt) | thrust_damage(31 ,  pierce),imodbits_polearm ],
["m_war_hammer_a",  "War Hammer", [("lucerne_hammer_edited",0)], itp_craftable|itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed, itc_cutting_spear|itcf_carry_spear, 499 , weight(3.0)|difficulty(0)|spd_rtng(81) | weapon_length(120)|swing_damage(38, pierce) | thrust_damage(38 ,  pierce),imodbits_polearm ],

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
 ["tab_shield_tauria_a", "Tauria Shield",   [("tableau_shield_sarranid_a" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 56 , weight(3)|hit_points(280)|body_armor(4)|spd_rtng(90)|shield_width(40)|shield_height(55),imodbits_shield,
  [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_sarranid_shield_a", ":agent_no", ":troop_no")])]],  
 ["tab_shield_tauria_b", "Tauria Shield",   [("tableau_shield_sarranid_b" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
 174 , weight(3)|hit_points(360)|body_armor(8)|spd_rtng(90)|shield_width(45)|shield_height(60),imodbits_shield,
  [(ti_on_init_item,[(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_sarranid_shield_b", ":agent_no", ":troop_no")])]],  
 ["tab_shield_tauria_c", "Tauria Guard Shield",   [("tableau_shield_sarranid_c" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_board_shield,
 360 , weight(3)|hit_points(430)|body_armor(10)|spd_rtng(88)|shield_width(40)|shield_height(50),imodbits_shield,
  [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_sarranid_shield_c", ":agent_no", ":troop_no")])]], 
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
["rich_outfit", "Rich Outfit", [("Rich_Surcoat_D",0),("Rich_Surcoat_D.1",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
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
["m_swadia_common_helmet_a", "Old Helmet", [("dethertir_helm_a",0),("dethertir_helm_a.1",0)], itp_type_head_armor|itp_merchandise   ,0, 864 , weight(1)|abundance(100)|head_armor(39)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_common_helmet_b", "Old Helmet", [("dethertir_helm_b",0),("dethertir_helm_b.1",0)], itp_type_head_armor|itp_merchandise   ,0, 599 , weight(1)|abundance(100)|head_armor(30)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],
["m_swadia_common_helmet_c", "Old Helmet", [("dethertir_helm_c",0),("dethertir_helm_c.1",0)], itp_type_head_armor|itp_merchandise   ,0, 599 , weight(1)|abundance(100)|head_armor(30)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_1] ],

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

["m_swadia_lord_helmet_a", "Swadian High Knight Helmet", [("helm_king_Jerusalem",0),("helm_king_Jerusalem_market",ixmesh_carry)], itp_type_head_armor|itp_merchandise|itp_attach_armature   ,0, 1995 , weight(2.5)|abundance(100)|head_armor(53)|body_armor(0)|leg_armor(0)|difficulty(13) ,imodbits_armor, [], [fac_kingdom_1] ],

# Custom mod armors
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

["mt_leather_boots_a", "Leather Boots", [("boot13",0)], itp_merchandise|itp_type_foot_armor|itp_civilian|itp_attach_armature,0, 179 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_9, fac_kingdom_10] ],
["mt_leather_boots_b", "Leather Boots", [("boot4",0)], itp_merchandise|itp_type_foot_armor|itp_civilian|itp_attach_armature,0, 179 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_9, fac_kingdom_10] ],
["mt_leather_boots_c", "Leather Boots", [("boot6",0)], itp_merchandise|itp_type_foot_armor|itp_civilian|itp_attach_armature,0, 179 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_9, fac_kingdom_10] ],
["mt_leather_boots_d", "Leather Boots", [("boot7",0)], itp_merchandise|itp_type_foot_armor|itp_civilian|itp_attach_armature,0, 179 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_9, fac_kingdom_10] ],
["mt_leather_boots_e", "Leather Boots", [("boot8",0)], itp_merchandise|itp_type_foot_armor|itp_civilian|itp_attach_armature,0, 179 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_9, fac_kingdom_10] ],

["mkk_archer_armor_a", "Eastern Archers Armor", [("armor_medium_tyrk_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1299 , weight(16)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(12)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_6] ],
["mkk_archer_armor_b", "Eastern Archers Armor", [("armor_medium_tyrk_b",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1299 , weight(16)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(12)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_6] ],
["mkk_archer_armor_c", "Eastern Archers Armor", [("armor_medium_tyrk_c",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1299 , weight(16)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(12)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_6] ],
["mkk_archer_armor_d", "Eastern Archers Armor", [("armor_medium_tyrk_d",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1299 , weight(16)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(12)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_6] ],

["mkk_infantry_armor_a", "Eastern Infantry Armor", [("armor_medium_tyrk_e",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1499 , weight(20)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(21)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_6] ],
["mkk_infantry_armor_b", "Eastern Infantry Armor", [("armor_medium_tyrk_f",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs,0 ,1499 , weight(20)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(21)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_6] ],

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

["surcoat_over_mail_undead_a", "Surcoat over Mail", [("surcoat_over_mail_undead_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1720 , weight(22)|abundance(1)|head_armor(0)|body_armor(43)|leg_armor(14)|difficulty(7) ,imodbits_armor ],
["surcoat_over_mail_undead_b", "Surcoat over Mail", [("surcoat_over_mail_undead_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1720 , weight(22)|abundance(1)|head_armor(0)|body_armor(43)|leg_armor(14)|difficulty(7) ,imodbits_armor ],

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
