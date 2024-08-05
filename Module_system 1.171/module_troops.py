import sys
import os

# Adding 'troops' directory to the path
current_dir = os.path.dirname(os.path.abspath(__file__))
troops_dir = os.path.join(current_dir, "troops")
sys.path.append(troops_dir)

from module_troops_utils_merge import *

# Troop upgrade declarations
upgrade(troops, "farmer", "watchman")
upgrade(troops, "townsman", "watchman")
upgrade2(troops, "watchman", "caravan_guard", "mercenary_crossbowman")
upgrade2(troops, "caravan_guard", "mercenary_swordsman", "mercenary_horseman")
upgrade(troops, "mercenary_swordsman", "hired_blade")
upgrade(troops, "mercenary_horseman", "mercenary_cavalry")

upgrade(troops, "delgay_mercenary", "delgay_mercenary_assasin")
upgrade(troops, "delgay_mercenary_assasin", "delgay_mercenary_rajas_killer")

upgrade(troops, "menegras_halberdier", "experienced_menegras_halberdier")
upgrade(troops, "experienced_menegras_halberdier", "menegras_halberdier_veteran")

#  nerpa troop tree
upgrade(troops, "nerpa_recruit", "nerpa_footman")
upgrade2(troops, "nerpa_footman", "nerpa_soldier", "nerpa_yeoman")
upgrade(troops, "nerpa_yeoman", "nerpa_trickshot")

upgrade(troops, "nerpa_ranger", "nerpa_master_ranger")

upgrade(troops, "nerpa_captain", "nerpa_army_veteran")
upgrade(troops, "nerpa_army_veteran", "nerpa_black_head")
upgrade(troops, "nerpa_mounted_veteran", "nerpa_commader")

# hairako troop tree
upgrade2(troops, "hairako_nomad", "hairako_footman", "hairako_archer")

upgrade(troops, "hairako_infantry", "hairako_infantry_veteran")
upgrade(troops, "hairako_infantry_veteran", "hairako_shaitan")

upgrade(troops, "hairako_rider", "hairako_experienced_rider")
upgrade(troops, "hairako_experienced_rider", "hairako_mounted_shaitan")

upgrade(troops, "hairako_sniper", "hairako_sniper_elite")

# tauria
upgrade(troops, "tauria_recruit", "tauria_trooper")

upgrade(troops, "tauria_soldier", "tauria_foot_knight")
upgrade(troops, "tauria_foot_knight", "tauria_sword_master")
upgrade(troops, "tauria_sword_master", "tauria_man_at_arms")

upgrade(troops, "tauria_horseman", "tauria_knight")
upgrade(troops, "tauria_knight", "tauria_noble_knight")

upgrade(troops, "tauria_crossbowman", "tauria_siege_crossbowman")

# elen
upgrade(troops, "elen_novice", "elen_footman")

upgrade(troops, "elen_fighter", "elen_light_infantry")
upgrade(troops, "elen_light_infantry", "elen_heavy_infantry")
upgrade(troops, "elen_heavy_infantry", "elen_cheif")

upgrade2(troops, "elen_archer", "elen_experienced_archer", "elen_sniper")

# adid
upgrade(troops, "adid_nomad_scout", "adid_desert_vanguard")
upgrade(troops, "adid_desert_vanguard", "adid_sultanate_vanguard")

upgrade(troops, "adid_camel_rider", "adid_sandstalker")
upgrade(troops, "adid_serpent_guard", "adid_oasis_acolyte")

upgrade(troops, "adid_oasis_acolyte", "adid_oasis_priest")
upgrade(troops, "adid_oasis_priest", "adid_oasis_high_priest")
upgrade(troops, "adid_royal_lancer", "adid_golden_falcon")

# stormguard
upgrade2(troops, "stormguard_mountaineer", "stormguard_thunderguard", "stormguard_hunter")
upgrade(troops, "stormguard_thunderguard", "stormguard_witch_hunter")
upgrade(troops, "stormguard_stormbringer", "stormguard_avalanche_warrior")

upgrade(
    troops,
    "stormguard_avalanche_warrior",
    "stormguard_tempest_sentinel",
)
upgrade(troops, "stormguard_tempest_sentinel", "stormguard_elite_stormguard")

upgrade(troops, "stormguard_lightning_rider", "stormguard_master_of_order")

# [I] Silver Rose Recruit
# |- [II] Silver Rose Levy
# |     |- [III] Silver Rose Militia
# |     |- [III] Silver Rose Scout
# |- [II] Silver Rose City Watch
# |     |- [III] Silver Rose Tower Guard
# |     |- [III] Silver Rose Wall Guard
upgrade2(troops, "silver_rose_recruit", "silver_rose_levy", "silver_rose_city_watch")
upgrade2(troops, "silver_rose_city_watch", "silver_rose_tower_guard", "silver_rose_wall_guard")
upgrade2(troops, "silver_rose_levy", "silver_rose_milita", "silver_rose_scout")

# [I] Silver Rose Footman
# |- [II] Silver Rose Hacker
# |- [II] Silver Rose Infantry
# |     |- [III] Silver Rose Sergeant
upgrade2(troops, "silver_rose_footman", "silver_rose_hacker", "silver_rose_infantry")
upgrade(troops, "silver_rose_infantry", "silver_rose_sergeant")

# [I] Silver Rose Crossbowman
# |- [II] Silver Rose Trained Crossbowman
# |     |- [III] Silver Rose Sharpshooter
upgrade(troops, "silver_rose_crossbowman", "silver_rose_trained_crossbowman")
upgrade(troops, "silver_rose_trained_crossbowman", "silver_rose_sharpshooter")

# [I] Silver Rose Squire
# |- [II] Silver Rose Horseman
# |     |- [III] Silver Rose Man-at-Arms
# |     |     |- [IV] Silver Rose Knight
upgrade(troops, "silver_rose_squire", "silver_rose_horseman")
upgrade(troops, "silver_rose_horseman", "silver_rose_man_at_arms")
upgrade(troops, "silver_rose_man_at_arms", "silver_rose_knight")

# [I] Chornovalley Recruit
# |- [II] Chornovalley Scout
# |     |- [III] Chornovalley Hunter
# |     |     |- [IV] Chornovalley Longbowman
# |- [II] Chornovalley Warden
# |     |- [III] Chornovalley Gatekeeper
upgrade2(troops, "chornovalley_recruit", "chornovalley_scout", "chornovalley_warden")
upgrade(troops, "chornovalley_scout", "chornovalley_hunter")
upgrade(troops, "chornovalley_hunter", "chornovalley_longbowman")
upgrade(troops, "chornovalley_warden", "chornovalley_gatekeeper")

# [I] Chornovalley Warrior
# |- [II] Chornovalley Sheriff
# |     |- [III] Chornovalley Sergeant
upgrade(troops, "chornovalley_warrior", "chornovalley_sheriff")
upgrade(troops, "chornovalley_sheriff", "chornovalley_sergeant")

# [I] Chornovalley Gunslider
# |- [II] Chornovalley Sniper
upgrade(troops, "chornovalley_gunslider", "chornovalley_sniper")

# [I] Chornovalley Horseman
# |- [II] Chornovalley Knight
upgrade(troops, "chornovalley_horseman", "chornovalley_knight")

# [I] Celestial Recruit
# |- [II] Celestial Voulgier
# |     |- [III] Celestial Houseguard
# |     |     |- [IV] Celestial Footman
# |- [II] Celestial Archer
upgrade2(troops, "celestial_recruit", "celestial_voulgier", "celestial_archer")
upgrade(troops, "celestial_voulgier", "celestial_houseguard")
upgrade(troops, "celestial_houseguard", "celestial_footman")

# [I] Celestial Milita
# |- [II] Celestial Armsman
# |     |- [III] Celestial Sergeant
# |     |     |- [IV] Celestial Commander
# |- [II] Celestial Foot Knight
upgrade2(troops, "celestial_milita", "celestial_armsman", "celestial_foot_knight")
upgrade(troops, "celestial_armsman", "celestial_sergeant")
upgrade(troops, "celestial_sergeant", "celestial_commander")

# [I] Celestial Hunter
# |- [II] Celestial Crossbowman
upgrade(troops, "celestial_hunter", "celestial_crossbowman")

# [I] Celestial Squire
# |- [II] Celestial Initiate Knight
# |     |- [III] Celestial Lancer
upgrade(troops, "celestial_squire", "celestial_initiate_knight")
upgrade(troops, "celestial_initiate_knight", "celestial_lancer") 

# [I] Iron Crown Recruit
# |- [II] Iron Crown Raider
# |     |- [III] Iron Crown Reaver
# |     |     |- [IV] Iron Crown Pirate
# |     |     |- [IV] Iron Crown Guardian
upgrade(troops, "iron_crown_recruit", "iron_crown_raider")
upgrade(troops, "iron_crown_raider", "iron_crown_reaver")
upgrade2(troops, "iron_crown_reaver", "iron_crown_pirate", "iron_crown_guardian")

# [I] Iron Crown Footman
# |- [II] Iron Crown Man-at-Arms
# |     |- [III] Iron Crown Veteran
# |     |     |- [IV] Iron Crown Champion
# |     |- [III] Iron Crown Halberdier
upgrade(troops, "iron_crown_footman", "iron_crown_man_at_arms")
upgrade2(
    troops, "iron_crown_man_at_arms", "iron_crown_vetaran", "iron_crown_halberdier"
)
upgrade(troops, "iron_crown_vetaran", "iron_crown_champion")

# [I] Iron Crown Skirmisher
# |- [II] Iron Crown Trained Skirmisher
upgrade(troops, "iron_crown_skirmisher", "iron_crown_trained_skirmisher")

# [I] Alpine Recruit
# |- [II] Alpine Levy
# |- [II] Alpine Watchman
# |     |- [III] Alpine Militia
upgrade2(troops, "alpine_recruit", "alpine_levy", "alpine_watchman")
upgrade(troops, "alpine_watchman", "alpine_militia")

# [I] Alpine Footman
# |- [II] Alpine Swordsman
# |     |- [III] Alpine Elite Swordsman
# |- [II] Alpine Spearman
# |     |- [III] Alpine Trained Spearman
# |     |     |- [IV] Alpine Veteran Spearman
# |     |     |     |- [V] Alpine Man-at-Arms
upgrade2(troops, "alpine_footman", "alpine_swordsman", "alpine_spearman")
upgrade(troops, "alpine_swordsman", "alpine_elite_swordsman")

upgrade(troops, "alpine_spearman", "alpine_trained_spearman")
upgrade(troops, "alpine_trained_spearman", "alpine_veteran_spearman")
upgrade(troops, "alpine_veteran_spearman", "alpine_man_at_arms")

# [I] Alpine Scout
# |- [II] Alpine Horseman
upgrade(troops, "alpine_scout", "alpine_horseman")

# [I] Alpine Crossbowman
# |- [II] Alpine Trained Crossbowman
# |     |- [III] Alpine Veteran Crossbowman
# |     |     |- [IV] Alpine Sharpshooter
upgrade(troops, "alpine_crossbowman", "alpine_trained_crossbowman")
upgrade(troops, "alpine_trained_crossbowman", "alpine_veteran_crossbowman")
upgrade(troops, "alpine_veteran_crossbowman", "alpine_sharpshooter")

# [I] Solarian Recruit
# |- [II] Solarian Militia
# |     |- [III] Solarian Spearman
# |     |     |- [IV] Solarian Sworn Spearman
upgrade(troops, "solarian_recruit", "solarian_militia")
upgrade(troops, "solarian_militia", "solarian_spearman")
upgrade(troops, "solarian_spearman", "solarian_sworn_spearman")

# [I] Solarian Footman
# |- [II] Solarian Veteran Footman
# |     |- [III] Solarian Infantry
# |     |     |- [IV] Solarian Guard
upgrade(troops, "solarian_footman", "solarian_veteran_footman")
upgrade(troops, "solarian_veteran_footman", "solarian_infantry")
upgrade(troops, "solarian_infantry", "solarian_guard")

# [I] Solarian Skirmisher
# |- [II] Solarian Archer
# |     |- [III] Solarian Master Archer
upgrade(troops, "solarian_skirmisher", "solarian_archer")
upgrade(troops, "solarian_archer", "solarian_master_archer")

# [I] Solarian Horseman
# |- [II] Solarian Knight
upgrade(troops, "solarian_horseman", "solarian_knight")


#        Looter
#        /        \
#      Bandit   Outlaw
#      /      \         /
# Pillager   Marauder  Highwayman
#                     |
#               Bandit Lord
upgrade2(troops, "looter", "bandit", "outlaw")
upgrade2(troops, "bandit", "pillager", "marauder")

upgrade(troops, "outlaw", "highwayman")
upgrade(troops, "highwayman", "bandit_lord")

# Cultists
upgrade(troops, "cultist_acolyte", "dark_cultist")
upgrade(troops, "dark_cultist", "occultist")
upgrade2(troops, "occultist", "veilweaver", "veiled_inquisitor")

upgrade2(troops, "scavenger", "scavenger_brute", "scavenger_crossbowman")
upgrade(troops, "scavenger_brute", "scavenger_shock_trooper")

# new tree connections
upgrade(troops, "mountain_bandit", "mountain_bandit_warrior")
upgrade(troops, "forest_bandit", "forest_outlaw")
upgrade(troops, "steppe_bandit", "steppe_bandit_warrior")
upgrade(troops, "steppe_bandit_warrior", "steppe_bandit_leader")

upgrade(troops, "taiga_bandit", "taiga_bandit_cheiftain")
upgrade(troops, "sea_raider", "sea_raider_warlord")
upgrade(troops, "desert_bandit", "desert_bandit_master")
upgrade2(
    troops, "desert_bandit_master", "desert_bandit_horseman", "desert_bandit_ronin"
)
upgrade(troops, "desert_bandit_horseman", "desert_bandit_leader")
# new tree connections ended

# upgrade2(troops,"bandit","brigand","mercenary_swordsman")
upgrade(troops, "manhunter", "slave_driver")

# upgrade(troops,"forest_bandit","mercenary_crossbowman")

upgrade(troops, "slave_driver", "slave_hunter")
upgrade(troops, "slave_hunter", "slave_crusher")
upgrade(troops, "slave_crusher", "slaver_chief")

upgrade(troops, "follower_woman", "hunter_woman")
upgrade(troops, "hunter_woman", "fighter_woman")

upgrade(troops, "fighter_woman", "sword_sister")
upgrade(troops, "refugee", "follower_woman")
upgrade(troops, "peasant_woman", "follower_woman")
# modmerger_start version=201 type=2
try:
    component_name = "troops"
    var_set = {"troops": troops}
    from modmerger import modmerge

    modmerge(var_set)
except:
    raise
# modmerger_end
