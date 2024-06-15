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

upgrade2(troops, "nerpa_soldier", "nerpa_ranger", "nerpa_captain")

upgrade(troops, "nerpa_ranger", "nerpa_master_ranger")

upgrade(troops, "nerpa_captain", "nerpa_army_veteran")
upgrade(troops, "nerpa_army_veteran", "nerpa_mounted_veteran")
upgrade2(troops, "nerpa_mounted_veteran", "nerpa_commader", "nerpa_black_head")

# hairako troop tree
upgrade2(troops, "hairako_nomad", "hairako_footman", "hairako_archer")
upgrade2(troops, "hairako_footman", "hairako_infantry", "hairako_rider")

upgrade(troops, "hairako_infantry", "hairako_infantry_veteran")
upgrade(troops, "hairako_infantry_veteran", "hairako_shaitan")

upgrade(troops, "hairako_rider", "hairako_experienced_rider")
upgrade(troops, "hairako_experienced_rider", "hairako_mounted_shaitan")

upgrade(troops, "hairako_archer", "hairako_sniper")
upgrade(troops, "hairako_sniper", "hairako_sniper_elite")

# tauria
upgrade(troops, "tauria_recruit", "tauria_trooper")
upgrade2(troops, "tauria_trooper", "tauria_soldier", "tauria_crossbowman")
upgrade2(troops, "tauria_soldier", "tauria_foot_knight", "tauria_horseman")

upgrade(troops, "tauria_foot_knight", "tauria_sword_master")
upgrade(troops, "tauria_sword_master", "tauria_man_at_arms")

upgrade(troops, "tauria_horseman", "tauria_knight")
upgrade(troops, "tauria_knight", "tauria_noble_knight")

upgrade(troops, "tauria_crossbowman", "tauria_siege_crossbowman")

# elen
upgrade(troops, "elen_novice", "elen_footman")
upgrade2(troops, "elen_footman", "elen_fighter", "elen_archer")

upgrade(troops, "elen_fighter", "elen_light_infantry")
upgrade(troops, "elen_light_infantry", "elen_heavy_infantry")
upgrade(troops, "elen_heavy_infantry", "elen_cheif")

upgrade2(troops, "elen_archer", "elen_experienced_archer", "elen_sniper")

# adid
upgrade(troops, "adid_nomad_scout", "adid_desert_vanguard")
upgrade(troops, "adid_desert_vanguard", "adid_sultanate_vanguard")

upgrade2(troops, "adid_sultanate_vanguard", "adid_camel_rider", "adid_serpent_guard")
upgrade(troops, "adid_camel_rider", "adid_sandstalker")
upgrade(troops, "adid_serpent_guard", "adid_oasis_acolyte")

upgrade2(troops, "adid_oasis_acolyte", "adid_oasis_priest", "adid_royal_lancer")
upgrade(troops, "adid_oasis_priest", "adid_oasis_high_priest")
upgrade(troops, "adid_royal_lancer", "adid_golden_falcon")

# stormguard
upgrade(troops, "stormguard_mountaineer", "stormguard_thunderguard")
upgrade(troops, "stormguard_thunderguard", "stormguard_stormbringer")
upgrade(troops, "stormguard_stormbringer", "stormguard_avalanche_warrior")

upgrade2(
    troops,
    "stormguard_avalanche_warrior",
    "stormguard_lightning_rider",
    "stormguard_tempest_sentinel",
)
upgrade(troops, "stormguard_tempest_sentinel", "stormguard_elite_stormguard")

# new troop trees for native factions
upgrade2(troops, "silver_rose_recruit", "silver_rose_levy", "silver_rose_city_watch")
upgrade2(troops, "silver_rose_city_watch", "silver_rose_tower_guard", "silver_rose_wall_guard")

# native
upgrade2(troops, "silver_rose_levy", "silver_rose_milita", "silver_rose_scout")

# upgrade2(troops, "silver_rose_milita", "silver_rose_footman", "silver_rose_crossbowman")
upgrade2(troops, "silver_rose_footman", "silver_rose_hacker", "silver_rose_infantry")
upgrade(troops, "silver_rose_infantry", "silver_rose_sergeant")

upgrade(troops, "silver_rose_crossbowman", "silver_rose_trained_crossbowman")
upgrade(troops, "silver_rose_trained_crossbowman", "silver_rose_sharpshooter")

# upgrade(troops, "silver_rose_horseman", "silver_rose_man_at_arms")
# upgrade(troops, "silver_rose_man_at_arms", "silver_rose_knight")

upgrade(troops, "chornovalley_recruit", "chornovalley_scout")
upgrade2(troops, "chornovalley_scout", "chornovalley_warrior", "chornovalley_hunter")
upgrade(troops, "chornovalley_hunter", "chornovalley_longbowman")

upgrade2(
    troops, "chornovalley_warrior", "chornovalley_sheriff", "chornovalley_horseman"
)
upgrade2(
    troops, "chornovalley_sheriff", "chornovalley_gunslider", "chornovalley_sergeant"
)

upgrade(troops, "chornovalley_horseman", "chornovalley_knight")

upgrade2(troops, "celestial_recruit", "celestial_milita", "celestial_hunter")
upgrade(troops, "celestial_hunter", "celestial_crossbowman")

upgrade2(troops, "celestial_milita", "celestial_armsman", "celestial_foot_knight")
upgrade2(troops, "celestial_armsman", "celestial_lancer", "celestial_sergeant")
upgrade(troops, "celestial_sergeant", "celestial_commander")

upgrade2(troops, "iron_crown_recruit", "iron_crown_raider", "iron_crown_skirmisher")
upgrade(troops, "iron_crown_raider", "iron_crown_footman")
upgrade(troops, "iron_crown_footman", "iron_crown_man_at_arms")
upgrade2(
    troops, "iron_crown_man_at_arms", "iron_crown_vetaran", "iron_crown_halberdier"
)
upgrade(troops, "iron_crown_vetaran", "iron_crown_champion")

upgrade(troops, "iron_crown_skirmisher", "iron_crown_trained_skirmisher")

upgrade2(troops, "alpine_recruit", "alpine_levy", "alpine_footman")
upgrade(troops, "alpine_footman", "alpine_swordsman")
upgrade(troops, "alpine_swordsman", "alpine_elite_swordsman")

upgrade2(troops, "alpine_levy", "alpine_spearman", "alpine_crossbowman")
upgrade2(troops, "alpine_spearman", "alpine_trained_spearman", "alpine_scout")
upgrade(troops, "alpine_scout", "alpine_horseman")
upgrade(troops, "alpine_trained_spearman", "alpine_veteran_spearman")
upgrade(troops, "alpine_veteran_spearman", "alpine_man_at_arms")

upgrade(troops, "alpine_crossbowman", "alpine_trained_crossbowman")
upgrade(troops, "alpine_trained_crossbowman", "alpine_veteran_crossbowman")  # new 1.126
upgrade(troops, "alpine_veteran_crossbowman", "alpine_sharpshooter")


upgrade(troops, "solarian_recruit", "solarian_footman")

upgrade2(troops, "solarian_footman", "solarian_veteran_footman", "solarian_skirmisher")
upgrade2(troops, "solarian_veteran_footman", "solarian_horseman", "solarian_infantry")
upgrade(troops, "solarian_infantry", "solarian_guard")
upgrade(troops, "solarian_skirmisher", "solarian_archer")

upgrade(troops, "solarian_archer", "solarian_master_archer")

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

# new tree connections
upgrade(troops, "mountain_bandit", "alpine_recruit")
upgrade(troops, "forest_bandit", "silver_rose_levy")
upgrade(troops, "steppe_bandit", "steppe_bandit_warrior")
upgrade(troops, "steppe_bandit_warrior", "steppe_bandit_leader")

upgrade(troops, "taiga_bandit", "chornovalley_recruit")
upgrade(troops, "sea_raider", "iron_crown_recruit")
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
