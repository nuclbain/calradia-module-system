from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_map_icons import *

pmf_is_prisoner = 0x0001

####################################################################################################################
#  Each party template record contains the following fields:
#  1) Party-template id: used for referencing party-templates in other files.
#     The prefix pt_ is automatically added before each party-template id.
#  2) Party-template name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Faction
#  6) Personality. See header_parties.py for an explanation of personality flags.
#  7) List of stacks. Each stack record is a tuple that contains the following fields:
#    7.1) Troop-id. 
#    7.2) Minimum number of troops in the stack. 
#    7.3) Maximum number of troops in the stack. 
#    7.4) Member flags(optional). Use pmf_is_prisoner to note that this member is a prisoner.
#     Note: There can be at most 6 stacks.
####################################################################################################################


party_templates = [
  ("none","none",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
  ("rescued_prisoners","Rescued Prisoners",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
  ("enemy","Enemy",icon_gray_knight,0,fac_undeads,merchant_personality,[]),
  ("hero_party","Hero Party",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
####################################################################################################################
# Party templates before this point are hard-wired into the game and should not be changed. 
####################################################################################################################
##  ("old_garrison","Old Garrison",icon_chornovalley_knight,0,fac_neutral,merchant_personality,[]),
  ("village_defenders","Village Defenders",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,10,20),(trp_peasant_woman,0,4)]),

  ("cattle_herd","Cattle Herd",icon_cattle|carries_goods(10),0,fac_neutral,merchant_personality,[(trp_cattle,80,120)]),

##  ("vaegir_nobleman","Vaegir Nobleman",icon_chornovalley_knight|carries_goods(10)|pf_quest_party,0,fac_commoners,merchant_personality,[(trp_nobleman,1,1),(trp_chornovalley_knight,2,6),(trp_chornovalley_horseman,4,12)]),
##  ("swadian_nobleman","Swadian Nobleman",icon_gray_knight|carries_goods(10)|pf_quest_party,0,fac_commoners,merchant_personality,[(trp_nobleman,1,1),(trp_silver_rose_knight,2,6),(trp_silver_rose_man_at_arms,4,12)]),
# Ryan BEGIN
# bandit 0 - 100
# pillager 0 - 10
# marauder 0 - 10
# outlaw 0 - 10
# highwayman 0 - 5
# bandit_lord 0 - 1
# TODO: Check troops distribution and rebalance if needed
  (
    "looters","Looters Party",icon_axeman|carries_goods(8),0,fac_outlaws,bandit_personality,
    [(trp_bandit,0,10),(trp_looter,1,95)]
  ),
  (
    "warband_bandits","Bandits Warband",icon_axeman|carries_goods(8),0,fac_outlaws,bandit_personality,
    [(trp_bandit,20,30),(trp_looter,10,95)]
  ),
  # TODO:
  # (
  #   "outlawed_mercenary_company","Outlawed Mercenaries",icon_gray_knight|carries_goods(8),0,fac_outlaws,bandit_personality,
  #   [(trp_mercenary_cavalry,0,5),(trp_hired_blade,0,7),(trp_watchman,10,35),(trp_mercenary_crossbowman,10,30),(trp_mercenary_swordsman,2,12),(trp_mercenary_horseman,0,10)]
  # ),
  ("heretics","Doomcult Heretics",icon_gray_knight|carries_goods(20),0,fac_heretics,bandit_personality,[(trp_dark_cultist,0,20),(trp_cultist_acolyte,0,50)]),
# Ryan END
  ("manhunters","Manhunters",icon_gray_knight,0,fac_manhunters,soldier_personality,[(trp_manhunter,19,100)]),
##  ("peasant","Peasant",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,1,6),(trp_peasant_woman,0,7)]),

#  ("black_khergit_raiders","Black Khergit Raiders",icon_khergit_horseman_b|carries_goods(2),0,fac_black_khergits,bandit_personality,[(trp_black_khergit_guard,1,10),(trp_black_khergit_horseman,5,5)]),
  ("steppe_bandits","Steppe Bandits",icon_khergit|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_steppe_bandit,14,50)]),
  ("taiga_bandits","Tundra Bandits",icon_axeman|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_taiga_bandit,14,65)]),
  ("desert_bandits","Piaktu Bandits",icon_vaegir_knight|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_desert_bandit,14,65)]),
  ("forest_bandits","Forest Bandits",icon_axeman|carries_goods(2),0,fac_forest_bandits,bandit_personality,[(trp_forest_bandit,14,65)]),
  ("mountain_bandits","Mountain Bandits",icon_axeman|carries_goods(2),0,fac_mountain_bandits,bandit_personality,[(trp_mountain_bandit,14,60)]),
  ("sea_raiders","Sea Raiders",icon_axeman|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_sea_raider,15,60)]),
  ("awakened_party","Awakened Party",icon_gray_knight|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_skeleton_newborn,15,120)]),

  ("deserters","Deserters",icon_vaegir_knight|carries_goods(3),0,fac_deserters,bandit_personality,[]),
    
  ("merchant_caravan","Merchant Caravan",icon_gray_knight|carries_goods(20)|pf_auto_remove_in_town|pf_quest_party,0,fac_commoners,escorted_merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,5,25)]),
  ("troublesome_bandits","Troublesome Bandits",icon_axeman|carries_goods(9)|pf_quest_party,0,fac_outlaws,bandit_personality,[(trp_bandit,14,55)]),
  ("bandits_awaiting_ransom","Bandits Awaiting Ransom",icon_axeman|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_bandit,24,58),(trp_kidnapped_girl,1,1,pmf_is_prisoner)]),
  ("kidnapped_girl","Kidnapped Girl",icon_woman|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_kidnapped_girl,1,1)]),

  ("village_farmers","Village Farmers",icon_peasant|pf_civilian,0,fac_innocents,merchant_personality,[(trp_farmer,5,10),(trp_peasant_woman,3,8)]),

  ("spy_partners", "Unremarkable Travellers", icon_gray_knight|carries_goods(10)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy_partner,1,1),(trp_caravan_guard,5,11)]),
  ("runaway_serfs","Runaway Serfs",icon_peasant|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_farmer,6,7), (trp_peasant_woman,3,3)]),
  ("spy", "Ordinary Townsman", icon_gray_knight|carries_goods(4)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy,1,1)]),
  ("sacrificed_messenger", "Sacrificed Messenger", icon_gray_knight|carries_goods(3)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[]),
##  ("conspirator", "Conspirators", icon_gray_knight|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_conspirator,3,4)]),
##  ("conspirator_leader", "Conspirator Leader", icon_gray_knight|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_conspirator_leader,1,1)]),
##  ("peasant_rebels", "Peasant Rebels", icon_peasant,0,fac_peasant_rebels,bandit_personality,[(trp_peasant_rebel,33,97)]),
##  ("noble_refugees", "Noble Refugees", icon_gray_knight|carries_goods(12)|pf_quest_party,0,fac_noble_refugees,merchant_personality,[(trp_noble_refugee,3,5),(trp_noble_refugee_woman,5,7)]),

  ("forager_party","Foraging Party",icon_gray_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("scout_party","Scouts",icon_gray_knight|carries_goods(1)|pf_show_faction,0,fac_commoners,bandit_personality,[]),
  ("patrol_party","Patrol",icon_gray_knight|carries_goods(2)|pf_show_faction,0,fac_commoners,soldier_personality,[]),
#  ("war_party", "War Party",icon_gray_knight|carries_goods(3),0,fac_commoners,soldier_personality,[]),
  ("messenger_party","Messenger",icon_gray_knight|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("raider_party","Raiders",icon_gray_knight|carries_goods(16)|pf_quest_party,0,fac_commoners,bandit_personality,[]),
  ("raider_captives","Raider Captives",0,0,fac_commoners,0,[(trp_peasant_woman,6,30,pmf_is_prisoner)]),
  ("kingdom_caravan_party","Caravan",icon_mule|carries_goods(25)|pf_show_faction,0,fac_commoners,merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,12,40)]),
  ("prisoner_train_party","Prisoner Train",icon_gray_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("default_prisoners","Default Prisoners",0,0,fac_commoners,0,[(trp_bandit,5,10,pmf_is_prisoner)]),

  ("routed_warriors","Routed Enemies",icon_vaegir_knight,0,fac_commoners,soldier_personality,[]),


# Caravans
  ("center_reinforcements","Reinforcements",icon_axeman|carries_goods(16),0,fac_commoners,soldier_personality,[(trp_townsman,5,30),(trp_watchman,4,20)]),  

  ("kingdom_hero_party","War Party",icon_flagbearer_a|pf_show_faction|pf_default_behavior,0,fac_commoners,soldier_personality,[]),
  
# Reinforcements
  # each faction includes three party templates. One is less-modernised, one is med-modernised and one is high-modernised
  # less-modernised templates are generally includes 7-14 troops in total, 
  # med-modernised templates are generally includes 5-10 troops in total, 
  # high-modernised templates are generally includes 3-5 troops in total

  ("kingdom_1_reinforcements_a", "{!}kingdom_1_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_silver_rose_levy,5,10),(trp_silver_rose_milita,2,4)]),
  ("kingdom_1_reinforcements_b", "{!}kingdom_1_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_silver_rose_footman,3,6),(trp_silver_rose_crossbowman,2,4)]),
  ("kingdom_1_reinforcements_c", "{!}kingdom_1_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_silver_rose_man_at_arms,2,4),(trp_silver_rose_trained_crossbowman,1,2)]), #Swadians are a bit less-powered thats why they have a bit more troops in their modernised party template (3-6, others 3-5)

  ("kingdom_2_reinforcements_a", "{!}kingdom_2_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_chornovalley_recruit,5,10),(trp_chornovalley_scout,2,4)]),
  ("kingdom_2_reinforcements_b", "{!}kingdom_2_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_chornovalley_warrior,2,4),(trp_chornovalley_hunter,2,4),(trp_chornovalley_scout,1,2)]),
  ("kingdom_2_reinforcements_c", "{!}kingdom_2_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_chornovalley_horseman,2,3),(trp_chornovalley_sheriff,1,2),(trp_chornovalley_knight,1,2)]),

  ("kingdom_3_reinforcements_a", "{!}kingdom_3_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_khergit_tribesman,3,5),(trp_khergit_skirmisher,4,9)]), #Khergits are a bit less-powered thats why they have a bit more 2nd upgraded(trp_khergit_skirmisher) than non-upgraded one(trp_khergit_tribesman).
  ("kingdom_3_reinforcements_b", "{!}kingdom_3_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_khergit_horseman,2,4),(trp_khergit_horse_archer,2,4),(trp_khergit_skirmisher,1,2)]),
  ("kingdom_3_reinforcements_c", "{!}kingdom_3_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_khergit_horseman,2,4),(trp_khergit_veteran_horse_archer,2,3)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)

  ("kingdom_4_reinforcements_a", "{!}kingdom_4_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_nord_footman,5,10),(trp_nord_recruit,2,4)]),
  ("kingdom_4_reinforcements_b", "{!}kingdom_4_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_nord_huntsman,2,5),(trp_nord_archer,2,3),(trp_nord_footman,1,2)]),
  ("kingdom_4_reinforcements_c", "{!}kingdom_4_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_nord_warrior,3,5),(trp_nord_tracer,3,5),(trp_nord_guard,1,5),(trp_nord_veteran,1,5)]),

  ("kingdom_5_reinforcements_a", "{!}kingdom_5_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_rhodok_tribesman,5,10),(trp_rhodok_spearman,2,4)]),
  ("kingdom_5_reinforcements_b", "{!}kingdom_5_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_rhodok_crossbowman,3,6),(trp_rhodok_trained_crossbowman,2,4)]),
  ("kingdom_5_reinforcements_c", "{!}kingdom_5_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_rhodok_veteran_spearman,2,3),(trp_rhodok_veteran_crossbowman,1,2)]), 

  ("kingdom_6_reinforcements_a", "{!}kingdom_6_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_sarranid_recruit,5,10),(trp_sarranid_footman,2,4)]),
  ("kingdom_6_reinforcements_b", "{!}kingdom_6_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_sarranid_skirmisher,2,4),(trp_sarranid_veteran_footman,2,3),(trp_sarranid_footman,1,3)]),
  ("kingdom_6_reinforcements_c", "{!}kingdom_6_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_sarranid_horseman,3,5)]),

  ("kingdom_7_reinforcements_a", "{!}kingdom_7_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_nerpa_recruit,5,12),(trp_nerpa_footman,3,5)]),
  ("kingdom_7_reinforcements_b", "{!}kingdom_7_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_nerpa_soldier,2,4),(trp_nerpa_captain,2,3),(trp_nerpa_ranger,2,4),(trp_nerpa_yeoman,2,4)]),
  ("kingdom_7_reinforcements_c", "{!}kingdom_7_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_nerpa_master_ranger,3,5), (trp_nerpa_army_veteran,3,5), (trp_nerpa_mounted_veteran,3,5), (trp_nerpa_commader,1,2), (trp_nerpa_black_head,1,2)]),

  ("kingdom_8_reinforcements_a", "{!}kingdom_8_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_hairako_nomad,5,15),(trp_hairako_footman,3,8)]),
  ("kingdom_8_reinforcements_b", "{!}kingdom_8_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_hairako_infantry,2,8),(trp_hairako_infantry_veteran,2,3),(trp_hairako_archer,2,4)]),
  ("kingdom_8_reinforcements_c", "{!}kingdom_8_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_hairako_rider,3,5), (trp_hairako_experienced_rider,3,5), (trp_hairako_sniper,3,5), (trp_hairako_shaitan,1,2), (trp_hairako_mounted_shaitan,1,2)]),

  ("kingdom_9_reinforcements_a", "{!}kingdom_9_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_tauria_recruit,5,15),(trp_tauria_trooper,3,4)]),
  ("kingdom_9_reinforcements_b", "{!}kingdom_9_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_tauria_soldier,2,8),(trp_tauria_foot_knight,1,3),(trp_tauria_crossbowman,2,7)]),
  ("kingdom_9_reinforcements_c", "{!}kingdom_9_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_tauria_siege_crossbowman,3,5), (trp_tauria_man_at_arms,3,5), (trp_tauria_horseman,3,5), (trp_tauria_knight,1,2), (trp_tauria_noble_knight,1,2)]),

  ("kingdom_10_reinforcements_a", "{!}kingdom_10_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_elen_forester,5,15),(trp_elen_footman,3,4)]),
  ("kingdom_10_reinforcements_b", "{!}kingdom_10_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_elen_fighter,2,8),(trp_elen_light_infantry,1,3),(trp_elen_archer,2,7)]),
  ("kingdom_10_reinforcements_c", "{!}kingdom_10_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_elen_heavy_infantry,3,5), (trp_elen_cheif,3,5), (trp_elen_sniper,3,5), (trp_elen_white_hood,1,2)]),

  # Kingdom 11 troops
  # Tier 1
  # trp_adid_nomad_scout = 77
  # trp_adid_desert_vanguard = 78
  # trp_adid_sultanate_vanguard = 79
  # Tier 2
  # trp_adid_camel_rider = 80
  # trp_adid_sandstalker = 81
  # trp_adid_serpent_guard = 82
  # trp_adid_oasis_acolyte = 83
  # Tier 3
  # trp_adid_oasis_priest = 84
  # trp_adid_oasis_high_priest = 85
  # trp_adid_royal_lancer = 86
  # trp_adid_golden_falcon = 87
  ("kingdom_11_reinforcements_a", "{!}kingdom_11_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_adid_nomad_scout,5,15),(trp_adid_desert_vanguard,3,4),(trp_adid_sultanate_vanguard,3,4)]),
  ("kingdom_11_reinforcements_b", "{!}kingdom_11_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_adid_camel_rider,2,8),(trp_adid_sandstalker,1,3),(trp_adid_serpent_guard,2,7),(trp_adid_oasis_acolyte,2,7)]),
  ("kingdom_11_reinforcements_c", "{!}kingdom_11_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_adid_oasis_priest,3,5), (trp_adid_oasis_high_priest,3,5), (trp_adid_royal_lancer,3,5), (trp_adid_golden_falcon,1,2)]),

  ("kingdom_12_reinforcements_a", "{!}kingdom_12_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_stormguard_mountaineer,5,15),(trp_stormguard_thunderguard,3,4)]),
  ("kingdom_12_reinforcements_b", "{!}kingdom_12_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_elen_fighter,2,8),(trp_stormguard_stormbringer,1,3),(trp_stormguard_avalanche_warrior,2,7)]),
  ("kingdom_12_reinforcements_c", "{!}kingdom_12_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_stormguard_tempest_sentinel,3,5), (trp_stormguard_lightning_rider,3,5), (trp_stormguard_elite_stormguard,3,5)]),

##  ("kingdom_1_reinforcements_a", "kingdom_1_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_silver_rose_footman,3,7),(trp_silver_rose_crossbowman,5,10),(trp_silver_rose_milita,11,26)]),
##  ("kingdom_1_reinforcements_b", "kingdom_1_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_silver_rose_man_at_arms,5,10),(trp_silver_rose_infantry,5,10),(trp_silver_rose_trained_crossbowman,3,8)]),
##  ("kingdom_1_reinforcements_c", "kingdom_1_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_silver_rose_knight,2,6),(trp_silver_rose_sergeant,2,5),(trp_silver_rose_sharpshooter,2,5)]),
##
##  ("kingdom_2_reinforcements_a", "kingdom_2_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_chornovalley_warrior,3,7),(trp_chornovalley_hunter,5,10),(trp_chornovalley_scout,11,26)]),
##  ("kingdom_2_reinforcements_b", "kingdom_2_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_chornovalley_horseman,4,9),(trp_chornovalley_sheriff,5,10),(trp_chornovalley_longbowman,3,8)]),
##  ("kingdom_2_reinforcements_c", "kingdom_2_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_chornovalley_knight,3,7),(trp_chornovalley_gunslider,2,5),(trp_vaegir_marksman,2,5)]),
##
##  ("kingdom_3_reinforcements_a", "kingdom_3_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_khergit_horseman,3,7),(trp_khergit_skirmisher,5,10),(trp_khergit_tribesman,11,26)]),
##  ("kingdom_3_reinforcements_b", "kingdom_3_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_khergit_veteran_horse_archer,4,9),(trp_khergit_horse_archer,5,10),(trp_khergit_horseman,3,8)]),
##  ("kingdom_3_reinforcements_c", "kingdom_3_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_khergit_lancer,3,7),(trp_khergit_veteran_horse_archer,2,5),(trp_khergit_horse_archer,2,5)]),
##
##  ("kingdom_4_reinforcements_a", "kingdom_4_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_nord_trained_footman,3,7),(trp_nord_footman,5,10),(trp_nord_recruit,11,26)]),
##  ("kingdom_4_reinforcements_b", "kingdom_4_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_nord_veteran,4,9),(trp_nord_warrior,5,10),(trp_nord_footman,3,8)]),
##  ("kingdom_4_reinforcements_c", "kingdom_4_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_nord_champion,1,3),(trp_nord_veteran,2,5),(trp_nord_warrior,2,5)]),
##
##  ("kingdom_5_reinforcements_a", "kingdom_5_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_rhodok_spearman,3,7),(trp_rhodok_crossbowman,5,10),(trp_rhodok_tribesman,11,26)]),
##  ("kingdom_5_reinforcements_b", "kingdom_5_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_rhodok_trained_spearman,4,9),(trp_rhodok_spearman,5,10),(trp_rhodok_crossbowman,3,8)]),
##  ("kingdom_5_reinforcements_c", "kingdom_5_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_rhodok_sergeant,3,7),(trp_rhodok_veteran_spearman,2,5),(trp_rhodok_veteran_crossbowman,2,5)]),



  ("steppe_bandit_lair" ,"Steppe Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_steppe_bandit,15,58)]),
  ("taiga_bandit_lair","Tundra Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_taiga_bandit,15,58)]),
  ("desert_bandit_lair" ,"Desert Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_desert_bandit,15,58)]),
  ("forest_bandit_lair" ,"Forest Bandit Camp",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_forest_bandit,15,58)]),
  ("mountain_bandit_lair" ,"Mountain Bandit Hideout",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_mountain_bandit,15,58)]),
  ("sea_raider_lair","Sea Raider Landing",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_sea_raider,15,50)]),
  ("looter_lair","Kidnappers' Hideout",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_looter,15,25)]),
  
  ("bandit_lair_templates_end","{!}bandit_lair_templates_end",icon_axeman|carries_goods(2)|pf_is_static,0,fac_outlaws,bandit_personality,[(trp_sea_raider,15,50)]),

  ("leaded_looters","Band of robbers",icon_axeman|carries_goods(8)|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_looter_leader,1,1),(trp_looter,3,3)]),

  ##diplomacy begin
  ("dplmc_spouse","Your spouse",icon_woman_b|pf_civilian|pf_show_faction,0,fac_neutral,merchant_personality,[]),

  ("dplmc_gift_caravan","Your Caravan",icon_mule|carries_goods(25)|pf_show_faction,0,fac_commoners,escorted_merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,5,25)]),
  #recruiter kit begin
   ("dplmc_recruiter","Recruiter",icon_flagbearer_b|pf_show_faction,0,fac_neutral,merchant_personality,[(trp_dplmc_recruiter,1,1)]),
  #recruiter kit end
   ##diplomacy end
]

# modmerger_start version=201 type=2
try:
    component_name = "party_templates"
    var_set = { "party_templates" : party_templates }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end
