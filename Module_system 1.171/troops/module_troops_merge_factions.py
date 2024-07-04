from module_troops_utils import *

troops_factions = [
    [
        "nerpa_recruit",
        "Nerpa Recruit",
        "Nerpa Recruits",
        tf_guarantee_armor | tf_guarantee_boots,
        0,
        0,
        fac_kingdom_7,
        [
            itm_arming_cap_a,
            itm_sword_medieval_c_small,
            itm_mace_2,
            itm_mace_4,
            itm_poulaines_b,
            itm_hose_b,
            itm_tab_shield_pavise_a,
        ],
        def_attrib | level(5),
        wp(60),
        knows_common,
        swadian_face_younger_1,
        swadian_face_middle_2,
    ],
    [
        "nerpa_footman",
        "Nerpa Footman",
        "Nerpa Footmen",
        tf_guarantee_armor | tf_guarantee_boots | tf_guarantee_helmet,
        0,
        0,
        fac_kingdom_7,
        [
            itm_sword_medieval_c_small,
            itm_mace_2,
            itm_mace_4,
            itm_tab_shield_pavise_a,
            itm_poulaines_b,
            itm_hose_b,
        ],
        def_attrib | level(10),
        wp(90),
        knows_common,
        swadian_face_younger_1,
        swadian_face_middle_2,
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
            itm_sword_medieval_c_small,
            itm_mace_2,
            itm_mace_4,
            itm_long_bow,
            itm_arrows,
            itm_poulaines_b,
            itm_hose_b,
        ],
        def_attrib | level(15),
        wp(100) | wp_archery(50),
        knows_common | knows_power_draw_3,
        swadian_face_younger_1,
        swadian_face_middle_2,
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
            itm_sword_medieval_c_small,
            itm_mace_2,
            itm_mace_4,
            itm_long_bow,
            itm_arrows,
            itm_leather_boots_a,
        ],
        def_attrib | level(20),
        wp(130) | wp_archery(50),
        knows_common | knows_power_draw_6,
        swadian_face_younger_1,
        swadian_face_middle_2,
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
            itm_sword_medieval_c_small,
            itm_mace_2,
            itm_mace_4,
            itm_tab_shield_pavise_c,
            itm_leather_boots_a,
        ],
        def_attrib | level(15),
        wp(120),
        knows_common,
        swadian_face_younger_1,
        swadian_face_middle_2,
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
            itm_sword_medieval_c_small,
            itm_mace_2,
            itm_mace_4,
            itm_tab_shield_pavise_c,
            itm_leather_gloves_a,
            itm_mail_boots_a,
        ],
        def_attrib | level(20),
        wp(150),
        knows_common | knows_ironflesh_2 | knows_power_strike_2 | knows_athletics_3,
        swadian_face_younger_1,
        swadian_face_middle_2,
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
            itm_sword_medieval_c_small,
            itm_awlpike,
            itm_awlpike_long,
            itm_tab_shield_pavise_c,
            itm_leather_gloves_a_v1,
            itm_mail_boots_a,
        ],
        def_attrib | level(25),
        wp(180) | wp_polearm(50),
        knows_common | knows_ironflesh_5 | knows_power_strike_5 | knows_athletics_3,
        swadian_face_old_1,
        swadian_face_old_2,
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
            itm_sword_medieval_c_small,
            itm_awlpike,
            itm_awlpike_long,
            itm_steel_shield,
            itm_leather_gloves_a_v1,
            itm_mail_boots_a,
            itm_leather_boots_a,
            itm_hunter,
        ],
        def_attrib | level(30),
        wp(210) | wp_polearm(50),
        knows_common
        | knows_ironflesh_5
        | knows_power_strike_5
        | knows_athletics_3
        | knows_riding_5,
        swadian_face_old_1,
        swadian_face_old_2,
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
            itm_sword_medieval_c_small,
            itm_awlpike,
            itm_awlpike_long,
            itm_steel_shield,
            itm_leather_gloves_a_v1,
            itm_plate_gauntlets_a,
            itm_mail_boots_a,
            itm_warhorse,
        ],
        def_attrib | level(35),
        wp(240) | wp_polearm(50),
        knows_common
        | knows_ironflesh_6
        | knows_power_strike_6
        | knows_athletics_3
        | knows_riding_8,
        swadian_face_old_1,
        swadian_face_old_2,
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
            itm_military_cleaver_c,
            itm_tab_shield_pavise_d,
            itm_leather_gloves_a_v1,
            itm_plate_gauntlets_a_v1,
            itm_plate_gauntlets_a,
            itm_mail_boots_a,
        ],
        def_attrib | level(35),
        wp(240) | wp_one_handed(50),
        knows_common | knows_ironflesh_10 | knows_power_strike_10 | knows_athletics_8,
        swadian_face_old_1,
        swadian_face_old_2,
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
            itm_sword_medieval_c_small,
            itm_war_darts,
            itm_tab_shield_pavise_c,
            itm_leather_gloves_a_v1,
            itm_leather_boots_a,
        ],
        def_attrib | level(20),
        wp(120) | wp_throwing(50),
        knows_common | knows_ironflesh_3 | knows_power_throw_4 | knows_athletics_2,
        swadian_face_younger_1,
        swadian_face_middle_2,
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
            itm_sword_medieval_c_small,
            itm_throwing_spears,
            itm_tab_shield_pavise_c,
            itm_leather_gloves_a_v1,
            itm_mail_boots_a,
        ],
        def_attrib | level(25),
        wp(150) | wp_throwing(50),
        knows_common | knows_ironflesh_5 | knows_power_throw_7 | knows_athletics_4,
        swadian_face_old_1,
        swadian_face_old_2,
    ],
    # hairako
    [
        "hairako_nomad",
        "Hairako Nomad",
        "Hairako Nomads",
        tf_guarantee_armor | tf_guarantee_boots,
        0,
        0,
        fac_kingdom_8,
        [
            itm_leather_covered_round_shield,
            itm_m_plain_round_shield_a,
            itm_tab_shield_round_a,
            itm_scimitar,
            itm_scimitar_b,
            itm_mace_1,
            itm_hose_d,
            itm_poulaines_d,
        ],
        def_attrib | level(5),
        wp(60),
        knows_common,
        khergit_face_young_1,
        khergit_face_young_2,
    ],
    [
        "hairako_footman",
        "Hairako Footman",
        "Hairako Footmans",
        tf_guarantee_armor
        | tf_guarantee_boots
        | tf_guarantee_helmet
        | tf_guarantee_shield,
        0,
        0,
        fac_kingdom_8,
        [
            itm_leather_gloves_a,
            itm_leather_gloves_a_v1,
            itm_tab_shield_tauria_a,
            itm_arabian_sword_a,
            itm_arabian_sword_b,
            itm_war_spear,
            itm_mace_2,
            itm_mace_3,
            itm_hose_d,
            itm_poulaines_d,
        ],
        def_attrib | level(10),
        wp(90),
        knows_common,
        khergit_face_young_1,
        khergit_face_young_2,
    ],
    [
        "hairako_infantry",
        "Hairako Infantry",
        "Hairako Infantries",
        tf_guarantee_armor
        | tf_guarantee_boots
        | tf_guarantee_helmet
        | tf_guarantee_shield,
        0,
        0,
        fac_kingdom_8,
        [
            itm_leather_gloves_a,
            itm_leather_gloves_a_v1,
            itm_leather_gloves_a,
            itm_mail_mittens_a_v1,
            itm_tab_shield_tauria_a,
            itm_sarranid_cavalry_sword,
            itm_arabian_sword_b,
            itm_war_spear,
            itm_mace_4,
            itm_mace_3,
            itm_desert_leather_boots_a,
        ],
        def_attrib | level(15),
        wp(120),
        knows_common,
        khergit_face_young_1,
        khergit_face_young_2,
    ],
    [
        "hairako_infantry_veteran",
        "Hairako Infantry Veteran",
        "Hairako Infantry Veterans",
        tf_guarantee_armor
        | tf_guarantee_boots
        | tf_guarantee_helmet
        | tf_guarantee_shield
        | tf_guarantee_gloves,
        0,
        0,
        fac_kingdom_8,
        [
            itm_leather_gloves_a_v1,
            itm_mail_mittens_a,
            itm_leather_gloves_a,
            itm_mail_mittens_a_v1,
            itm_tab_shield_tauria_a,
            itm_sarranid_cavalry_sword,
            itm_arabian_sword_d,
            itm_battle_trident,
            itm_ranseur,
            itm_mace_4,
            itm_mace_3,
            itm_desert_leather_boots_a,
            itm_desert_leather_boots_b,
        ],
        def_attrib | level(20),
        wp(150),
        knows_common | knows_athletics_5 | knows_power_strike_4,
        khergit_face_middle_1,
        khergit_face_old_2,
    ],
    [
        "hairako_shaitan",
        "Hairako Shaitan",
        "Hairako Shaitans",
        tf_guarantee_armor
        | tf_guarantee_boots
        | tf_guarantee_helmet
        | tf_guarantee_shield
        | tf_guarantee_gloves,
        0,
        0,
        fac_kingdom_8,
        [
            itm_leather_gloves_a_v1,
            itm_mail_mittens_a,
            itm_eastern_scale_gloves_b,
            itm_eastern_scale_gloves_a,
            itm_tab_shield_tauria_b,
            itm_sarranid_cavalry_sword,
            itm_arabian_sword_d,
            itm_arabian_sword_c,
            itm_battle_trident,
            itm_ranseur,
            itm_desert_heavy_boots_a,
            itm_desert_heavy_boots_b,
        ],
        def_attrib | level(25),
        wp(180),
        knows_common | knows_athletics_10 | knows_power_strike_9 | knows_ironflesh_10,
        khergit_face_middle_1,
        khergit_face_old_2,
    ],
    [
        "hairako_rider",
        "Hairako Rider",
        "Hairako Riders",
        tf_mounted
        | tf_guarantee_horse
        | tf_guarantee_armor
        | tf_guarantee_helmet
        | tf_guarantee_shield
        | tf_guarantee_boots
        | tf_guarantee_gloves,
        0,
        0,
        fac_kingdom_8,
        [
            itm_leather_gloves_a,
            itm_leather_gloves_a_v1,
            itm_leather_gloves_a,
            itm_mail_mittens_a_v1,
            itm_tab_shield_tauria_a,
            itm_sarranid_cavalry_sword,
            itm_arabian_sword_b,
            itm_steppe_horse,
            itm_desert_leather_boots_a,
            itm_desert_leather_boots_b,
        ],
        def_attrib | level(15),
        wp(120),
        knows_common | knows_riding_4,
        khergit_face_young_1,
        khergit_face_young_2,
    ],
    [
        "hairako_experienced_rider",
        "Hairako Experienced Rider",
        "Hairako Experienced Riders",
        tf_mounted
        | tf_guarantee_horse
        | tf_guarantee_armor
        | tf_guarantee_helmet
        | tf_guarantee_shield
        | tf_guarantee_boots
        | tf_guarantee_gloves,
        0,
        0,
        fac_kingdom_8,
        [
            itm_mail_mittens_a,
            itm_mail_mittens_a_v1,
            itm_leather_gloves_a,
            itm_tab_shield_tauria_a,
            itm_sarranid_cavalry_sword,
            itm_arabian_sword_b,
            itm_steppe_horse,
            itm_steppe_horse_b,
            itm_desert_leather_boots_a,
            itm_desert_leather_boots_b,
        ],
        def_attrib | level(20),
        wp(150),
        knows_common | knows_riding_5 | knows_ironflesh_4,
        khergit_face_old_1,
        khergit_face_old_2,
    ],
    [
        "hairako_mounted_shaitan",
        "Hairako Mounted Shaitan",
        "Hairako Mounted Shaitans",
        tf_mounted
        | tf_guarantee_horse
        | tf_guarantee_armor
        | tf_guarantee_helmet
        | tf_guarantee_shield
        | tf_guarantee_boots
        | tf_guarantee_gloves,
        0,
        0,
        fac_kingdom_8,
        [
            itm_mail_mittens_a,
            itm_mail_mittens_a_v1,
            itm_eastern_scale_gloves_a,
            itm_eastern_scale_gloves_b,
            itm_tab_shield_tauria_b,
            itm_sarranid_cavalry_sword,
            itm_arabian_sword_b,
            itm_arabian_sword_c,
            itm_horseman_poleaxe_a,
            itm_horseman_poleaxe_b,
            itm_steppe_horse_b,
            itm_steppe_horse_c,
            itm_steppe_horse_d,
            itm_desert_heavy_boots_a,
            itm_desert_heavy_boots_b,
        ],
        def_attrib | level(25),
        wp(180),
        knows_common | knows_riding_8 | knows_ironflesh_10 | knows_power_strike_7,
        khergit_face_old_1,
        khergit_face_old_2,
    ],
    [
        "hairako_archer",
        "Hairako Archer",
        "Hairako Archers",
        tf_guarantee_armor | tf_guarantee_boots | tf_guarantee_ranged,
        0,
        0,
        fac_kingdom_8,
        [
            itm_tab_shield_tauria_a,
            itm_scimitar,
            itm_scimitar_b,
            itm_mace_1,
            itm_sword_khergit_1,
            itm_strong_bow,
            itm_arrows,
            itm_desert_leather_boots_a,
            itm_desert_leather_boots_b,
        ],
        def_attrib | level(10),
        wp(90) | wp_archery(50),
        knows_common | knows_power_draw_4,
        khergit_face_young_1,
        khergit_face_young_2,
    ],
    [
        "hairako_sniper",
        "Hairako Sniper",
        "Hairako Snipers",
        tf_guarantee_armor | tf_guarantee_boots | tf_guarantee_ranged,
        0,
        0,
        fac_kingdom_8,
        [
            itm_tab_shield_tauria_a,
            itm_arabian_sword_a,
            itm_arabian_sword_b,
            itm_mace_2,
            itm_ranseur,
            itm_strong_bow,
            itm_arrows,
            itm_desert_leather_boots_a,
            itm_desert_leather_boots_b,
        ],
        def_attrib | level(15),
        wp(120) | wp_archery(50),
        knows_common | knows_power_draw_6,
        khergit_face_young_1,
        khergit_face_young_2,
    ],
    [
        "hairako_sniper_elite",
        "Hairako Sniper Elite",
        "Hairako Sniper Elites",
        tf_guarantee_armor | tf_guarantee_boots | tf_guarantee_ranged,
        0,
        0,
        fac_kingdom_8,
        [
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
            itm_desert_heavy_boots_b,
        ],
        def_attrib | level(20),
        wp(180) | wp_archery(50),
        knows_common | knows_power_draw_9 | knows_athletics_5 | knows_ironflesh_4,
        khergit_face_old_1,
        khergit_face_old_2,
    ],
    # tauria
    # TODO: battle priest and spearman/helbardier
    [
        "tauria_recruit",
        "Tauria Recruit",
        "Tauria Recruits",
        tf_guarantee_armor | tf_guarantee_boots,
        0,
        0,
        fac_kingdom_9,
        [
            itm_tab_shield_tauria_a,
            itm_falchion_a,
            itm_hatchet_a,
            itm_boar_spear,
            itm_scythe,
            itm_mace_1,
            itm_poulaines_d,
            itm_hose_d,
        ],
        def_attrib | level(5),
        wp(60),
        knows_common,
        swadian_face_young_1,
        swadian_face_young_2,
    ],
    [
        "tauria_trooper",
        "Tauria Trooper",
        "Tauria Troopers",
        tf_guarantee_armor | tf_guarantee_boots,
        0,
        0,
        fac_kingdom_9,
        [
            itm_leather_gloves_a,
            itm_mail_coif,
            itm_tab_shield_tauria_a,
            itm_boar_spear,
            itm_falchion_a,
            itm_voulge,
            itm_poulaines_d,
            itm_hose_d,
            itm_leather_shoes_a,
            itm_leather_shoes_b,
        ],
        def_attrib | level(10),
        wp(90),
        knows_common,
        swadian_face_young_1,
        swadian_face_young_2,
    ],
    [
        "tauria_soldier",
        "Tauria Soldier",
        "Tauria Soldiers",
        tf_guarantee_armor
        | tf_guarantee_boots
        | tf_guarantee_helmet
        | tf_guarantee_shield
        | tf_guarantee_gloves,
        0,
        0,
        fac_kingdom_9,
        [
            itm_leather_gloves_a,
            itm_mail_mittens_a_v1,
            itm_leather_gloves_a_v1,
            itm_mail_coif,
            itm_flat_top_a,
            itm_tab_shield_tauria_a,
            itm_crusader_spear_a,
            itm_axe_crusader_a,
            itm_winged_mace,
            itm_leather_boots_a,
        ],
        def_attrib | level(15),
        wp(120),
        knows_common,
        swadian_face_young_1,
        swadian_face_young_2,
    ],
    [
        "tauria_foot_knight",
        "Tauria Foot Knight",
        "Tauria Foot Knights",
        tf_guarantee_armor
        | tf_guarantee_boots
        | tf_guarantee_helmet
        | tf_guarantee_shield
        | tf_guarantee_gloves,
        0,
        0,
        fac_kingdom_9,
        [
            itm_leather_gloves_a,
            itm_mail_mittens_a_v1,
            itm_leather_gloves_a_v1,
            itm_tab_shield_tauria_a,
            itm_tab_shield_tauria_b,
            itm_crusader_spear_a,
            itm_crusader_spear_b,
            itm_axe_crusader_a,
            itm_axe_crusader_b,
            itm_winged_mace,
            itm_flanged_mace,
            itm_leather_boots_a,
            itm_mail_boots_a,
        ],
        def_attrib | level(20),
        wp(150),
        knows_common,
        swadian_face_young_1,
        swadian_face_young_2,
    ],
    [
        "tauria_sword_master",
        "Tauria Sword Master",
        "Tauria Sword Masters",
        tf_guarantee_armor
        | tf_guarantee_boots
        | tf_guarantee_helmet
        | tf_guarantee_shield
        | tf_guarantee_gloves,
        0,
        0,
        fac_kingdom_9,
        [
            itm_mail_mittens_a_v1,
            itm_leather_gloves_a_v1,
            itm_tab_shield_tauria_a,
            itm_tab_shield_tauria_b,
            itm_crusader_spear_a,
            itm_crusader_spear_b,
            itm_axe_crusader_1,
            itm_axe_crusader_b,
            itm_winged_mace,
            itm_flanged_mace,
            itm_leather_boots_a,
            itm_mail_boots_a,
            itm_mail_boots_b,
        ],
        def_attrib | level(25),
        wp(180),
        knows_common,
        swadian_face_young_1,
        swadian_face_young_2,
    ],
    [
        "tauria_man_at_arms",
        "Tauria Man-at-Arms",
        "Tauria Men-at-Arms",
        tf_guarantee_armor
        | tf_guarantee_boots
        | tf_guarantee_helmet
        | tf_guarantee_shield
        | tf_guarantee_gloves,
        0,
        0,
        fac_kingdom_9,
        [
            itm_mail_mittens_a_v1,
            itm_leather_gloves_a_v1,
            itm_plate_gauntlets_a_v1,
            itm_tab_shield_tauria_c,
            itm_tab_shield_tauria_b,
            itm_crusader_spear_b,
            itm_crusader_spear_c,
            itm_axe_crusader_1,
            itm_axe_crusader_c,
            itm_flanged_mace,
            itm_mail_boots_a,
            itm_mail_boots_b,
            itm_plate_boots_b,
        ],
        def_attrib | level(30),
        wp(210),
        knows_common | knows_ironflesh_7 | knows_power_strike_7,
        swadian_face_old_1,
        swadian_face_old_2,
    ],
    [
        "tauria_horseman",
        "Tauria Horseman",
        "Tauria Horsemans",
        tf_guarantee_armor
        | tf_guarantee_boots
        | tf_guarantee_helmet
        | tf_guarantee_shield
        | tf_mounted
        | tf_guarantee_horse,
        0,
        0,
        fac_kingdom_9,
        [
            itm_leather_gloves_a,
            itm_mail_mittens_a_v1,
            itm_leather_gloves_a_v1,
            itm_mail_coif,
            itm_tab_shield_tauria_a,
            itm_lance,
            itm_axe_crusader_a,
            itm_winged_mace,
            itm_hunter,
            itm_leather_boots_a,
            itm_mail_boots_a,
            itm_mail_boots_b,
        ],
        def_attrib | level(20),
        wp(150),
        knows_common | knows_riding_3,
        swadian_face_young_1,
        swadian_face_young_2,
    ],
    [
        "tauria_knight",
        "Tauria Knight",
        "Tauria Knights",
        tf_guarantee_armor
        | tf_guarantee_boots
        | tf_guarantee_helmet
        | tf_guarantee_shield
        | tf_mounted
        | tf_guarantee_horse
        | tf_guarantee_gloves,
        0,
        0,
        fac_kingdom_9,
        [
            itm_mail_mittens_a_v1,
            itm_leather_gloves_a_v1,
            itm_tab_shield_tauria_a,
            itm_tab_shield_tauria_b,
            itm_axe_crusader_1,
            itm_axe_crusader_b,
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
            itm_mail_boots_c,
        ],
        def_attrib | level(25),
        wp(180),
        knows_common | knows_riding_5 | knows_ironflesh_4,
        swadian_face_young_1,
        swadian_face_young_2,
    ],
    [
        "tauria_noble_knight",
        "Tauria Noble Knight",
        "Tauria Noble Knights",
        tf_guarantee_armor
        | tf_guarantee_boots
        | tf_guarantee_helmet
        | tf_guarantee_shield
        | tf_mounted
        | tf_guarantee_horse
        | tf_guarantee_gloves,
        0,
        0,
        fac_kingdom_9,
        [
            itm_mail_mittens_a_v1,
            itm_leather_gloves_a_v1,
            itm_tab_shield_tauria_a,
            itm_tab_shield_tauria_b,
            itm_axe_crusader_1,
            itm_winged_mace,
            itm_flanged_mace,
            itm_lance,
            itm_mt_horse_c11,
            itm_plate_boots_b,
            itm_plate_boots_a,
        ],
        def_attrib | level(30),
        wp(210) | wp_melee(50),
        knows_common | knows_riding_8 | knows_ironflesh_10 | knows_power_strike_10,
        swadian_face_old_1,
        swadian_face_old_2,
    ],
    [
        "tauria_crossbowman",
        "Tauria Crossbowman",
        "Tauria Crossbowmans",
        tf_guarantee_armor
        | tf_guarantee_boots
        | tf_guarantee_helmet
        | tf_guarantee_shield
        | tf_guarantee_ranged,
        0,
        0,
        fac_kingdom_9,
        [
            itm_tab_shield_tauria_a,
            itm_winged_mace,
            itm_flanged_mace,
            itm_axe_crusader_b,
            itm_heavy_crossbow,
            itm_bolts,
            itm_poulaines_d,
            itm_hose_d,
        ],
        def_attrib | level(15),
        wp(120) | wp_crossbow(50),
        knows_common,
        swadian_face_young_1,
        swadian_face_young_2,
    ],
    [
        "tauria_siege_crossbowman",
        "Tauria Siege Crossbowman",
        "Tauria Siege Crossbowmans",
        tf_guarantee_armor
        | tf_guarantee_boots
        | tf_guarantee_helmet
        | tf_guarantee_shield
        | tf_guarantee_ranged,
        0,
        0,
        fac_kingdom_9,
        [
            itm_mail_coif,
            itm_tab_shield_tauria_a,
            itm_tab_shield_tauria_b,
            itm_winged_mace,
            itm_flanged_mace,
            itm_axe_crusader_b,
            itm_falchion_a,
            itm_axe_crusader_c,
            itm_heavy_crossbow,
            itm_sniper_crossbow,
            itm_bolts,
            itm_leather_boots_a,
        ],
        def_attrib | level(20),
        wp(150) | wp_crossbow(50),
        knows_common,
        swadian_face_middle_1,
        swadian_face_old_2,
    ],
    # elen
    [
        "elen_novice",
        "Elen Novice",
        "Elen Novices",
        tf_guarantee_armor | tf_guarantee_boots,
        0,
        0,
        fac_kingdom_10,
        [
            itm_arming_cap_a,
            itm_leather_gloves_a,
            itm_mace_1,
            itm_hatchet_b,
            itm_spear,
            itm_tab_shield_tauria_a,
            itm_hose_b,
            itm_poulaines_b,
        ],
        def_attrib | level(5),
        wp(60),
        knows_common | swadian_face_young_1,
        swadian_face_young_2,
    ],
    [
        "elen_footman",
        "Elen Footman",
        "Elen Footmen",
        tf_guarantee_armor | tf_guarantee_boots | tf_guarantee_helmet,
        0,
        0,
        fac_kingdom_10,
        [
            itm_leather_gloves_a,
            itm_falchion_a,
            itm_flanged_mace,
            itm_military_scythe,
            itm_fighting_axe,
            itm_tab_shield_tauria_a,
            itm_hose_b,
            itm_poulaines_b,
        ],
        def_attrib | level(10),
        wp(90),
        knows_common | swadian_face_young_1,
        swadian_face_young_2,
    ],
    [
        "elen_fighter",
        "Elen Fighter",
        "Elen Fighters",
        tf_guarantee_armor
        | tf_guarantee_boots
        | tf_guarantee_helmet
        | tf_guarantee_shield,
        0,
        0,
        fac_kingdom_10,
        [
            itm_leather_gloves_a,
            itm_leather_gloves_a_v1,
            itm_tab_shield_tauria_a,
            itm_hose_b,
            itm_poulaines_b,
            itm_leather_boots_a,
        ],
        def_attrib | level(15),
        wp(120),
        knows_common | knows_ironflesh_2,
        swadian_face_young_1,
        swadian_face_young_2,
    ],
    [
        "elen_light_infantry",
        "Elen Light Infantry",
        "Elen Light Infantries",
        tf_guarantee_armor
        | tf_guarantee_boots
        | tf_guarantee_helmet
        | tf_guarantee_shield
        | tf_guarantee_gloves,
        0,
        0,
        fac_kingdom_10,
        [
            itm_leather_gloves_a_v1,
            itm_mail_mittens_a_v1,
            itm_mail_mittens_a,
            itm_flanged_mace,
            itm_winged_mace,
            itm_m_glaive_b,
            itm_military_scythe,
            itm_crusader_spear_inf_a,
            itm_tab_shield_tauria_a,
            itm_leather_boots_a,
            itm_leather_boots_b,
            itm_mail_boots_a,
        ],
        def_attrib | level(20),
        wp(150),
        knows_common | knows_ironflesh_3,
        swadian_face_young_1,
        swadian_face_young_2,
    ],
    [
        "elen_heavy_infantry",
        "Elen Heavy Infantry",
        "Elen Heavy Infantries",
        tf_guarantee_armor
        | tf_guarantee_boots
        | tf_guarantee_helmet
        | tf_guarantee_shield
        | tf_guarantee_gloves,
        0,
        0,
        fac_kingdom_10,
        [
            itm_leather_gloves_a_v1,
            itm_mail_mittens_a_v1,
            itm_mail_mittens_a,
            itm_plate_gauntlets_a_v1,
            itm_heavy_infantry_axe,
            itm_strange_winged_mace,
            itm_winged_mace,
            itm_m_glaive_b,
            itm_m_glaive_a,
            itm_crusader_spear_inf_b,
            itm_tab_shield_tauria_a,
            itm_mail_boots_a,
            itm_mail_boots_b,
            itm_plate_boots_a,
            itm_plate_boots_b,
        ],
        def_attrib | level(25),
        wp(180),
        knows_common | knows_ironflesh_5 | knows_power_strike_5,
        swadian_face_young_1,
        swadian_face_young_2,
    ],
    [
        "elen_cheif",
        "Elen Cheif",
        "Elen Cheifs",
        tf_guarantee_armor
        | tf_guarantee_boots
        | tf_guarantee_helmet
        | tf_guarantee_shield
        | tf_guarantee_gloves
        | tf_guarantee_horse,
        0,
        0,
        fac_kingdom_10,
        [
            itm_mail_mittens_a_v1,
            itm_mail_mittens_a,
            itm_crusader_knight_spear_a,
            itm_crusader_knight_spear_b,
            itm_tab_shield_tauria_a,
            itm_mail_boots_a,
            itm_mail_boots_b,
            itm_plate_boots_a,
            itm_plate_boots_b,
        ],
        tier_two_attrib | level(30),
        wp(210),
        knows_common | knows_ironflesh_9 | knows_power_strike_9 | knows_riding_8,
        swadian_face_young_1,
        swadian_face_young_2,
    ],
    [
        "elen_archer",
        "Elen Archer",
        "Elen Archers",
        tf_guarantee_armor
        | tf_guarantee_boots
        | tf_guarantee_helmet
        | tf_guarantee_shield
        | tf_guarantee_gloves
        | tf_guarantee_ranged,
        0,
        0,
        fac_kingdom_10,
        [
            itm_leather_gloves_a,
            itm_mace_1,
            itm_hatchet_b,
            itm_arrows,
            itm_hunting_bow,
            itm_leather_boots_a,
            itm_leather_boots_b,
            itm_hose_b,
            itm_poulaines_b,
        ],
        def_attrib | level(15),
        wp(120) | wp_archery(50),
        knows_common | knows_ironflesh_2 | knows_power_draw_3,
        swadian_face_young_1,
        swadian_face_young_2,
    ],
    [
        "elen_experienced_archer",
        "Elen Experienced Archer",
        "Elen Experienced Archers",
        tf_guarantee_armor
        | tf_guarantee_boots
        | tf_guarantee_helmet
        | tf_guarantee_shield
        | tf_guarantee_gloves
        | tf_guarantee_ranged,
        0,
        0,
        fac_kingdom_10,
        [
            itm_leather_gloves_a,
            itm_falchion_a,
            itm_flanged_mace,
            itm_fighting_axe,
            itm_arrows,
            itm_long_bow,
            itm_leather_boots_a,
            itm_leather_boots_b,
            itm_hose_b,
            itm_poulaines_b,
        ],
        def_attrib | level(20),
        wp(150) | wp_archery(50),
        knows_common | knows_ironflesh_2 | knows_power_draw_4,
        swadian_face_young_1,
        swadian_face_young_2,
    ],
    [
        "elen_sniper",
        "Elen Sniper",
        "Elen Snipers",
        tf_guarantee_armor
        | tf_guarantee_boots
        | tf_guarantee_helmet
        | tf_guarantee_shield
        | tf_guarantee_gloves
        | tf_guarantee_ranged,
        0,
        0,
        fac_kingdom_10,
        [
            itm_leather_gloves_a,
            itm_falchion_a,
            itm_flanged_mace,
            itm_tab_shield_pavise_b,
            itm_tab_shield_pavise_c,
            itm_crossbow,
            itm_bolts,
            itm_leather_boots_a,
            itm_leather_boots_b,
            itm_mail_boots_a,
            itm_mail_boots_b,
        ],
        def_attrib | level(20),
        wp(150) | wp_crossbow(70),
        knows_common | knows_ironflesh_2 | knows_power_strike_2,
        swadian_face_young_1,
        swadian_face_young_2,
    ],
    # Adid units
    # Nomad Scout - Desert Vanguard - Sultanate Vanguard
    [
        "adid_nomad_scout",
        "Adid Nomad Scout",
        "Adid Nomad Scouts",
        tf_guarantee_boots | tf_guarantee_armor,
        0,
        0,
        fac_kingdom_11,
        [
            itm_leather_gloves_a_v1,
            itm_spiked_club,
            itm_falchion_a,
            itm_falchion_b,
            itm_long_spiked_club,
            itm_tab_shield_tauria_a,
            itm_leather_shoes_a,
            itm_leather_shoes_b,
        ],
        def_attrib | level(5),
        wp(60),
        knows_common,
        swadian_face_younger_1,
        swadian_face_middle_2,
    ],
    [
        "adid_desert_vanguard",
        "Adid Desert Vanguard",
        "Adid Desert Vanguards",
        tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet
        | tf_guarantee_shield,
        0,
        0,
        fac_kingdom_11,
        [
            itm_leather_gloves_a_v1,
            itm_leather_gloves_a,
            itm_scimitar,
            itm_falchion_a,
            itm_falchion_b,
            itm_voulge_a,
            itm_spear,
            itm_tab_shield_tauria_a,
            itm_leather_shoes_a,
            itm_leather_shoes_b,
        ],
        def_attrib | level(10),
        wp(90),
        knows_common,
        swadian_face_young_1,
        swadian_face_middle_2,
    ],
    [
        "adid_sultanate_vanguard",
        "Adid Sultanate Vanguard",
        "Adid Sultanate Vanguards",
        tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet
        | tf_guarantee_shield
        | tf_guarantee_gloves,
        0,
        0,
        fac_kingdom_11,
        [
            itm_leather_gloves_a,
            itm_leather_gloves_a,
            itm_leather_gloves_a_v1,
            itm_falchion_a,
            itm_falchion_b,
            itm_hafted_blade_a,
            itm_hafted_blade_b,
            itm_hafted_blade_c,
            itm_hafted_blade_d,
            itm_hafted_blade_e,
            itm_hafted_blade_f,
            itm_tab_shield_tauria_a,
            itm_leather_shoes_a,
            itm_leather_shoes_b,
        ],
        def_attrib | level(15),
        wp(120),
        knows_common,
        swadian_face_young_1,
        swadian_face_middle_2,
    ],
    # Sultanate Vanguard - Camel Rider - Sandstalker
    [
        "adid_camel_rider",
        "Adid Camel Rider",
        "Adid Camel Riders",
        tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet
        | tf_guarantee_shield
        | tf_guarantee_gloves
        | tf_mounted
        | tf_guarantee_horse
        | tf_guarantee_ranged,
        0,
        0,
        fac_kingdom_11,
        [
            itm_leather_gloves_a_v1,
            itm_falchion_a,
            itm_falchion_b,
            itm_nomad_bow,
            itm_arrows,
            itm_maa_camel_light_c,
            itm_maa_camel_light_d,
            itm_tab_shield_tauria_a,
            itm_leather_shoes_a,
            itm_leather_shoes_b,
        ],
        def_attrib | level(20),
        wp(150) | wp_archery(50),
        knows_common | knows_riding_5 | knows_horse_archery_5,
        swadian_face_young_1,
        swadian_face_middle_2,
    ],
    [
        "adid_sandstalker",
        "Adid Sandstalker",
        "Adid Sandstalkers",
        tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet
        | tf_guarantee_shield
        | tf_guarantee_gloves
        | tf_mounted
        | tf_guarantee_horse
        | tf_guarantee_ranged,
        0,
        0,
        fac_kingdom_11,
        [
            itm_leather_gloves_a_v1,
            itm_leather_gloves_a,
            itm_leather_gloves_a,
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
            itm_light_leather_boots_c,
        ],
        def_attrib | level(25),
        wp(180) | wp_archery(50),
        knows_common | knows_riding_5 | knows_horse_archery_8,
        swadian_face_young_1,
        swadian_face_middle_2,
    ],
    # Sultanate Vanguard - Serpent Guard - Oasis Acolyte
    [
        "adid_serpent_guard",
        "Adid Serpent Guard",
        "Adid Serpent Guards",
        tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet
        | tf_guarantee_shield
        | tf_guarantee_gloves,
        0,
        0,
        fac_kingdom_11,
        [
            itm_mail_mittens_a,
            itm_mail_mittens_a_v1,
            itm_leather_gloves_a_v1,
            itm_strange_winged_mace,
            itm_strange_winged_mace_decorated,
            itm_falchion_b,
            itm_hafted_blade_a,
            itm_hafted_blade_b,
            itm_hafted_blade_c,
            itm_hafted_blade_d,
            itm_hafted_blade_e,
            itm_hafted_blade_f,
            itm_tab_shield_tauria_a,
            itm_light_leather_boots_a,
            itm_light_leather_boots_b,
            itm_light_leather_boots_c,
        ],
        def_attrib | level(20),
        wp(150) | wp_polearm(50),
        knows_common,
        swadian_face_young_1,
        swadian_face_middle_2,
    ],
    [
        "adid_oasis_acolyte",
        "Adid Oasis Acolyte",
        "Adid Oasis Acolytes",
        tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet
        | tf_guarantee_shield
        | tf_guarantee_gloves,
        0,
        0,
        fac_kingdom_11,
        [
            itm_mail_mittens_a,
            itm_mail_mittens_a_v1,
            itm_falchion_b,
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
            itm_light_leather_boots_c,
        ],
        def_attrib | level(25),
        wp(180) | wp_polearm(50),
        knows_common | knows_ironflesh_4 | knows_power_throw_4,
        swadian_face_young_1,
        swadian_face_middle_2,
    ],
    # Oasis Acolyte - Oasis Priest - Oasis High Priest
    [
        "adid_oasis_priest",
        "Adid Oasis Priest",
        "Adid Oasis Priests",
        tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet
        | tf_guarantee_shield
        | tf_guarantee_gloves,
        0,
        0,
        fac_kingdom_11,
        [
            itm_mail_mittens_a,
            itm_mail_mittens_a_v1,
            itm_eastern_scale_gloves_a,
            itm_eastern_scale_gloves_b,
            itm_falchion_b,
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
            itm_light_leather_boots_c,
        ],
        def_attrib | level(30),
        wp(210) | wp_polearm(50),
        knows_common
        | knows_ironflesh_9
        | knows_power_strike_5
        | knows_athletics_6
        | knows_power_throw_5,
        swadian_face_young_1,
        swadian_face_middle_2,
    ],
    [
        "adid_oasis_high_priest",
        "Adid Oasis High Priest",
        "Adid Oasis High Priests",
        tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet
        | tf_guarantee_shield
        | tf_guarantee_gloves,
        0,
        0,
        fac_kingdom_11,
        [
            itm_eastern_scale_gloves_a,
            itm_eastern_scale_gloves_b,
            itm_falchion_b,
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
            itm_mail_boots_c,
        ],
        def_attrib | level(35),
        wp(240) | wp_polearm(50),
        knows_common
        | knows_ironflesh_10
        | knows_power_strike_10
        | knows_athletics_6
        | knows_power_throw_7,
        swadian_face_young_1,
        swadian_face_middle_2,
    ],
    # Oasis Acolyte - Royal Lancer - Golden Falcon
    [
        "adid_royal_lancer",
        "Adid Royal Lancer",
        "Adid Royal Lancers",
        tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet
        | tf_guarantee_shield
        | tf_guarantee_gloves
        | tf_mounted
        | tf_guarantee_horse,
        0,
        0,
        fac_kingdom_11,
        [
            itm_mail_mittens_a,
            itm_mail_mittens_a_v1,
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
            itm_mail_boots_c,
        ],
        def_attrib | level(30),
        wp(210),
        knows_common | knows_ironflesh_9 | knows_power_strike_5 | knows_riding_6,
        swadian_face_young_1,
        swadian_face_middle_2,
    ],
    [
        "adid_golden_falcon",
        "Adid Golden Falcon",
        "Adid Golden Falcons",
        tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet
        | tf_guarantee_shield
        | tf_guarantee_gloves
        | tf_mounted
        | tf_guarantee_horse,
        0,
        0,
        fac_kingdom_11,
        [
            itm_mail_mittens_a,
            itm_mail_mittens_a_v1,
            itm_eastern_scale_gloves_a,
            itm_eastern_scale_gloves_b,
            itm_sarranid_cavalry_sword,
            itm_hatchet_a,
            itm_hatchet_b,
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
            itm_mail_boots_c,
        ],
        def_attrib | level(35),
        wp(240),
        knows_common | knows_ironflesh_10 | knows_power_strike_7 | knows_riding_8,
        swadian_face_young_1,
        swadian_face_middle_2,
    ],
    # Stormguard units
    # Mountaineer - Thunderguard - Stormbringers - Avalanche Warriors
    [
        "stormguard_mountaineer",
        "Stormguard Mountaineer",
        "Stormguard Mountaineers",
        tf_guarantee_armor | tf_guarantee_boots,
        0,
        0,
        fac_kingdom_12,
        [
            itm_pilgrim_hood,
            itm_leather_gloves_a,
            itm_hatchet_a,
            itm_falchion_a,
            itm_pickaxe_a_v1,
            itm_tab_shield_tauria_a,
            itm_boar_spear,
            itm_poulaines_d,
        ],
        def_attrib | level(5),
        wp(60),
        knows_common,
        swadian_face_younger_1,
        swadian_face_middle_2,
    ],
    [
        "stormguard_thunderguard",
        "Stormguard Thunderguard",
        "Stormguard Thunderguards",
        tf_guarantee_armor | tf_guarantee_boots | tf_guarantee_shield,
        0,
        0,
        fac_kingdom_12,
        [
            itm_leather_gloves_a,
            itm_pickaxe_a_v1,
            itm_tab_shield_tauria_a,
            itm_boar_spear,
            itm_broad_spear,
            itm_poulaines_d,
        ],
        def_attrib | level(10),
        wp(90),
        knows_common,
        swadian_face_young_1,
        swadian_face_middle_2,
    ],
    [
        "stormguard_stormbringer",
        "Srormguard Stormbringer",
        "Srormguard Stormbringers",
        tf_guarantee_armor
        | tf_guarantee_boots
        | tf_guarantee_shield
        | tf_guarantee_helmet,
        0,
        0,
        fac_kingdom_12,
        [
            itm_axe_crusader_a,
            itm_tab_shield_tauria_a,
            itm_tab_shield_heater_c,
            itm_two_handed_battle_axe_2,
            itm_leather_gloves_a,
            itm_leather_gloves_a_v1,
            itm_leather_boots_a,
        ],
        def_attrib | level(15),
        wp(120) | wp_two_handed(50),
        knows_common,
        swadian_face_young_1,
        swadian_face_middle_2,
    ],
    [
        "stormguard_avalanche_warrior",
        "Stormguard Avalanche Warrior",
        "Stormguard Avalanche Warriors",
        tf_guarantee_armor
        | tf_guarantee_boots
        | tf_guarantee_shield
        | tf_guarantee_helmet
        | tf_guarantee_gloves,
        0,
        0,
        fac_kingdom_12,
        [
            itm_coat_of_plates,
            itm_coat_of_plates_v1,
            itm_coat_of_plates_v2,
            itm_mail_mittens_a_v1,
            itm_mail_mittens_a,
            itm_leather_gloves_a_v1,
            itm_axe_crusader_a,
            itm_axe_crusader_b,
            itm_mace_4,
            itm_shield_heater_d,
            itm_tab_shield_tauria_a,
            itm_sword_great_a,
            itm_throwing_spears,
            itm_leather_boots_a,
        ],
        def_attrib | level(20),
        wp(150) | wp_two_handed(50),
        knows_common,
        swadian_face_young_1,
        swadian_face_middle_2,
    ],
    # Avalanche Warriors - Lightning Riders
    [
        "stormguard_lightning_rider",
        "Stormguard Lightning Rider",
        "Stormguard Lightning Riders",
        tf_guarantee_armor
        | tf_guarantee_boots
        | tf_guarantee_shield
        | tf_guarantee_helmet
        | tf_guarantee_gloves
        | tf_mounted
        | tf_guarantee_horse,
        0,
        0,
        fac_kingdom_12,
        [
            itm_coat_of_plates,
            itm_coat_of_plates_v1,
            itm_coat_of_plates,
            itm_coat_of_plates_v1,
            itm_coat_of_plates_v2,
            itm_leather_gloves_a_v1,
            itm_mail_mittens_a_v1,
            itm_mail_mittens_a,
            itm_axe_crusader_a,
            itm_axe_crusader_b,
            itm_axe_crusader_1,
            itm_tab_shield_tauria_a,
            itm_light_lance,
            itm_throwing_spears,
            itm_warhorse,
            itm_black_knight_horse_a,
            itm_mail_boots_a,
            itm_mail_boots_b,
            itm_mail_boots_c,
            itm_leather_boots_a,
        ],
        def_attrib | level(25),
        wp(180),
        knows_common | knows_riding_5,
        swadian_face_young_1,
        swadian_face_middle_2,
    ],
    # Avalanche Warriors - Tempest Sentinels - Elite Stormguard
    [
        "stormguard_tempest_sentinel",
        "Stormguard Tempest Sentinel",
        "Stormguard Tempest Sentinels",
        tf_guarantee_armor
        | tf_guarantee_boots
        | tf_guarantee_shield
        | tf_guarantee_helmet
        | tf_guarantee_gloves,
        0,
        0,
        fac_kingdom_12,
        [
            itm_coat_of_plates,
            itm_coat_of_plates_v1,
            itm_coat_of_plates_v2,
            itm_plate_gauntlets_a,
            itm_plate_gauntlets_a_v1,
            itm_one_handed_battle_axe_c,
            itm_tab_shield_tauria_b,
            itm_sword_great_a,
            itm_war_axe,
            itm_shortened_voulge,
            itm_throwing_spears,
            itm_mail_boots_a,
            itm_mail_boots_b,
            itm_mail_boots_c,
        ],
        def_attrib | level(25),
        wp(180) | wp_two_handed(50),
        knows_common | knows_power_throw_6,
        swadian_face_young_1,
        swadian_face_middle_2,
    ],
    [
        "stormguard_elite_stormguard",
        "Stormguard Elite",
        "Stormguard Elite",
        tf_guarantee_armor
        | tf_guarantee_boots
        | tf_guarantee_shield
        | tf_guarantee_helmet
        | tf_guarantee_gloves,
        0,
        0,
        fac_kingdom_12,
        [
            itm_coat_of_plates_v3,
            itm_plate_gauntlets_a_v1,
            itm_axe_crusader_1,
            itm_tab_shield_tauria_b,
            itm_bec_de_corbin_a,
            itm_heavy_throwing_axes,
            itm_throwing_spears,
            itm_plate_boots_a,
            itm_plate_boots_b,
        ],
        def_attrib | level(30),
        wp(210) | wp_polearm(50),
        knows_common | knows_power_throw_9,
        swadian_face_young_1,
        swadian_face_middle_2,
    ],
    [
        "alpine_recruit",
        "Alpine Recruit",
        "Alpine Recruits",
        tf_guarantee_boots | tf_guarantee_armor,
        0,
        0,
        fac_kingdom_5,
        [
            itm_pitch_fork,
            itm_voulge_a,
            itm_falchion_a,
            itm_arming_cap_a,
            itm_mace_1,
            itm_shield_kite_k,
            itm_leather_gloves_a_v1,
            itm_hose_f,
            itm_poulaines_f,
        ],
        def_attrib | level(5),
        wp(60),
        knows_common | knows_power_draw_2 | knows_ironflesh_1,
        rhodok_face_younger_1,
        rhodok_face_old_2,
    ],
    [
        "alpine_levy",
        "Alpine Levy",
        "Alpine Levy",
        tf_guarantee_boots | tf_guarantee_armor,
        0,
        0,
        fac_kingdom_5,
        [
            itm_spear,
            itm_mace_2,
            itm_mace_3,
            itm_mace_4,
            itm_shield_kite_k,
            itm_arming_cap_a,
            itm_leather_gloves_a_v1,
            itm_leather_gloves_a_v1,
            itm_leather_gloves_a,
            itm_hose_f,
            itm_poulaines_f,
        ],
        def_attrib | level(10),
        wp(90),
        knows_common | knows_power_draw_2 | knows_ironflesh_1,
        rhodok_face_young_1,
        rhodok_face_old_2,
    ],
    [
        "alpine_footman",
        "Alpine Footman",
        "Alpine Footmen",
        tf_guarantee_boots | tf_guarantee_armor | tf_guarantee_helmet,
        0,
        0,
        fac_kingdom_5,
        [
            itm_sword_medieval_c_long,
            itm_sword_medieval_d_long,
            itm_shield_kite_i,
            itm_shield_kite_k,
            itm_leather_gloves_a_v1,
            itm_leather_gloves_a,
            itm_leather_gloves_a,
            itm_hose_f,
            itm_poulaines_f,
        ],
        def_attrib | level(10),
        wp(90) | wp_one_handed(50),
        knows_common
        | knows_ironflesh_2
        | knows_shield_1
        | knows_power_strike_2
        | knows_athletics_1,
        rhodok_face_young_1,
        rhodok_face_old_2,
    ],
    [
        "alpine_swordsman",
        "Alpine Swordsman",
        "Alpine Swordsmen",
        tf_guarantee_armor | tf_guarantee_helmet | tf_guarantee_shield,
        0,
        0,
        fac_kingdom_5,
        [
            itm_morningstar,
            itm_shield_kite_i,
            itm_shield_kite_k,
            itm_leather_gloves_a_v1,
            itm_mail_mittens_a,
            itm_mail_mittens_a_v1,
            itm_leather_boots_a,
        ],
        def_attrib | level(15),
        wp(120) | wp_one_handed(50),
        knows_common
        | knows_ironflesh_5
        | knows_shield_1
        | knows_power_strike_5
        | knows_athletics_1,
        rhodok_face_young_1,
        rhodok_face_old_2,
    ],
    [
        "alpine_elite_swordsman",
        "Alpine Elite Swordsman",
        "Alpine Elite Swordsmen",
        tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet
        | tf_guarantee_shield
        | tf_guarantee_gloves,
        0,
        0,
        fac_kingdom_5,
        [
            itm_morningstar,
            itm_shield_kite_i,
            itm_shield_kite_k,
            itm_leather_gloves_a_v1,
            itm_mail_mittens_a,
            itm_mail_mittens_a_v1,
            itm_leather_boots_a,
            itm_mail_boots_a,
        ],
        def_attrib | level(20),
        wp(150) | wp_one_handed(50),
        knows_common
        | knows_ironflesh_8
        | knows_shield_6
        | knows_power_strike_8
        | knows_athletics_5,
        rhodok_face_young_1,
        rhodok_face_old_2,
    ],
    [
        "alpine_spearman",
        "Alpine Spearman",
        "Alpine Spearmen",
        tf_guarantee_boots | tf_guarantee_armor | tf_guarantee_helmet,
        0,
        0,
        fac_kingdom_5,
        [
            itm_crusader_spear_inf_a,
            itm_crusader_spear_inf_b,
            itm_crusader_spear_inf_c,
            itm_tab_shield_pavise_b,
            itm_falchion_a,
            itm_leather_gloves_a_v1,
            itm_leather_gloves_a,
            itm_leather_boots_a,
            itm_mail_boots_a,
            itm_mail_boots_b,
        ],
        def_attrib | level(15),
        wp(120),
        knows_common
        | knows_ironflesh_2
        | knows_shield_1
        | knows_power_strike_2
        | knows_athletics_1,
        rhodok_face_young_1,
        rhodok_face_old_2,
    ],
    [
        "alpine_scout",
        "Alpine Scout",
        "Alpine Scouts",
        tf_mounted
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet
        | tf_guarantee_shield
        | tf_guarantee_horse,
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
            itm_leather_gloves_a_v1,
            itm_saddle_horse,
            itm_leather_boots_a,
            itm_hose_f,
            itm_poulaines_f,
        ],
        def_attrib | level(20),
        wp(150),
        knows_common
        | knows_ironflesh_5
        | knows_riding_4
        | knows_shield_3
        | knows_power_strike_4
        | knows_athletics_3,
        rhodok_face_young_1,
        rhodok_face_old_2,
    ],
    [
        "alpine_horseman",
        "Alpine Horseman",
        "Alpine Horsemen",
        tf_mounted
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet
        | tf_guarantee_shield
        | tf_guarantee_shield
        | tf_guarantee_gloves
        | tf_guarantee_horse,
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
            itm_leather_gloves_a_v1,
            itm_hunter,
            itm_leather_boots_a,
            itm_mail_boots_a,
        ],
        def_attrib | level(25),
        wp(180),
        knows_common
        | knows_ironflesh_6
        | knows_shield_7
        | knows_power_strike_6
        | knows_riding_7,
        rhodok_face_young_1,
        rhodok_face_old_2,
    ],
    [
        "alpine_trained_spearman",
        "Alpine Trained Spearman",
        "Alpine Trained Spearmen",
        tf_guarantee_boots | tf_guarantee_armor | tf_guarantee_shield,
        0,
        0,
        fac_kingdom_5,
        [
            itm_crusader_spear_inf_a,
            itm_crusader_spear_inf_b,
            itm_crusader_spear_inf_c,
            itm_tab_shield_pavise_c,
            itm_leather_gloves_a_v1,
            itm_plate_boots_b,
            itm_mail_boots_a,
            itm_mail_boots_b,
            itm_leather_boots_a,
        ],
        def_attrib | level(20),
        wp(150) | wp_polearm(50),
        knows_common
        | knows_ironflesh_3
        | knows_shield_2
        | knows_power_strike_2
        | knows_athletics_2,
        rhodok_face_young_1,
        rhodok_face_older_2,
    ],
    [
        "alpine_veteran_spearman",
        "Alpine Veteran Spearman",
        "Alpine Veteran Spearmen",
        tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet
        | tf_guarantee_shield,
        0,
        0,
        fac_kingdom_5,
        [
            itm_crusader_spear_a,
            itm_crusader_spear_b,
            itm_crusader_spear_c,
            itm_tab_shield_pavise_c,
            itm_plate_gauntlets_a_v1,
            itm_plate_gauntlets_a,
            itm_mail_boots_a,
            itm_mail_boots_b,
            itm_plate_boots_b,
        ],
        def_attrib | level(25),
        wp(180) | wp_polearm(50),
        knows_common
        | knows_ironflesh_5
        | knows_shield_3
        | knows_power_strike_4
        | knows_athletics_3,
        rhodok_face_young_1,
        rhodok_face_older_2,
    ],
    [
        "alpine_man_at_arms",
        "Alpine Man-at-Arms",
        "Alpine Men-at-Arms",
        tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet
        | tf_guarantee_shield
        | tf_guarantee_gloves,
        0,
        0,
        fac_kingdom_5,
        [
            itm_crusader_spear_a,
            itm_crusader_spear_b,
            itm_crusader_spear_c,
            itm_tab_shield_pavise_d,
            itm_plate_gauntlets_a_v1,
            itm_plate_gauntlets_a,
            itm_plate_boots_a,
            itm_plate_boots_b,
        ],
        def_attrib | level(30),
        wp(210) | wp_polearm(50),
        knows_common
        | knows_ironflesh_9
        | knows_shield_5
        | knows_power_strike_9
        | knows_athletics_6,
        rhodok_face_middle_1,
        rhodok_face_older_2,
    ],
    [
        "alpine_crossbowman",
        "Alpine Crossbowman",
        "Alpine Crossbowmen",
        tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet
        | tf_guarantee_ranged,
        0,
        0,
        fac_kingdom_5,
        [
            itm_sword_medieval_a,
            itm_falchion_a,
            itm_club_with_spike_head,
            itm_tab_shield_pavise_b,
            itm_crossbow,
            itm_bolts,
            itm_leather_gloves_a_v1,
            itm_hose_f,
            itm_poulaines_f,
        ],
        def_attrib | level(15),
        wp(120) | wp_crossbow(50),
        knows_common
        | knows_ironflesh_2
        | knows_shield_1
        | knows_power_strike_1
        | knows_athletics_2,
        rhodok_face_young_1,
        rhodok_face_older_2,
    ],
    [
        "alpine_trained_crossbowman",
        "Alpine Trained Crossbowman",
        "Alpine Trained Crossbowmen",
        tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet
        | tf_guarantee_ranged
        | tf_guarantee_shield,
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
            itm_leather_gloves_a_v1,
            itm_hose_f,
            itm_poulaines_f,
        ],
        def_attrib | level(20),
        wp(150) | wp_crossbow(50),
        knows_common
        | knows_ironflesh_1
        | knows_shield_2
        | knows_power_strike_2
        | knows_athletics_3,
        rhodok_face_young_1,
        rhodok_face_older_2,
    ],
    [
        "alpine_veteran_crossbowman",
        "Alpine Veteran Crossbowman",
        "Alpine Veteran Crossbowmen",
        tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet
        | tf_guarantee_ranged
        | tf_guarantee_shield,
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
            itm_leather_gloves_a_v1,
            itm_hose_f,
            itm_poulaines_f,
            itm_leather_boots_a,
        ],
        def_attrib | level(25),
        wp(180) | wp_crossbow(50),
        knows_common
        | knows_ironflesh_2
        | knows_shield_3
        | knows_power_strike_3
        | knows_athletics_4,
        rhodok_face_middle_1,
        rhodok_face_older_2,
    ],
    [
        "alpine_sharpshooter",
        "Alpine Sharpshooter",
        "Alpine Sharpshooters",
        tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet
        | tf_guarantee_ranged
        | tf_guarantee_shield,
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
            itm_leather_gloves_a_v1,
            itm_mail_boots_a,
        ],
        def_attrib | level(30),
        wp(210) | wp_crossbow(50),
        knows_common
        | knows_ironflesh_3
        | knows_shield_4
        | knows_power_strike_4
        | knows_athletics_6,
        rhodok_face_middle_1,
        rhodok_face_older_2,
    ],
    [
        "rhodok_messenger",
        "Rhodok Messenger",
        "Rhodok Messengers",
        tf_mounted
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_gloves
        | tf_guarantee_horse
        | tf_guarantee_ranged,
        0,
        0,
        fac_kingdom_5,
        [
            itm_sword_medieval_b,
            itm_leather_jerkin,
            itm_courser,
            itm_leather_gloves_a,
            itm_short_bow,
            itm_arrows,
        ],
        def_attrib | agi_21 | level(25),
        wp(130),
        knows_common | knows_riding_7 | knows_horse_archery_5 | knows_power_draw_5,
        rhodok_face_middle_1,
        rhodok_face_older_2,
    ],
    [
        "rhodok_deserter",
        "Rhodok Deserter",
        "Rhodok Deserters",
        tf_guarantee_ranged | tf_guarantee_boots | tf_guarantee_armor,
        0,
        0,
        fac_deserters,
        [
            itm_arrows,
            itm_spiked_mace,
            itm_axe,
            itm_falchion_a,
            itm_short_bow,
            itm_short_bow,
            itm_hunting_bow,
            itm_javelin,
            itm_javelin,
            itm_steppe_cap,
            itm_leather_vest,
            itm_leather_vest,
            itm_nomad_armor,
        ],
        def_attrib | str_10 | level(14),
        wp(80),
        knows_ironflesh_1 | knows_power_draw_1,
        rhodok_face_middle_1,
        rhodok_face_older_2,
    ],
    [
        "rhodok_prison_guard",
        "Prison Guard",
        "Prison Guards",
        tf_guarantee_shield
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet,
        0,
        0,
        fac_kingdom_5,
        [
            itm_ashwood_pike,
            itm_battle_fork,
            itm_battle_axe,
            itm_fighting_axe,
            itm_tab_shield_pavise_b,
            itm_sallet_b,
            itm_leather_gloves_a,
        ],
        def_attrib | level(24),
        wp(130),
        knows_athletics_3 | knows_shield_2 | knows_ironflesh_3,
        rhodok_face_middle_1,
        rhodok_face_older_2,
    ],
    [
        "rhodok_castle_guard",
        "Castle Guard",
        "Castle Guards",
        tf_guarantee_shield
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet,
        0,
        0,
        fac_kingdom_5,
        [
            itm_ashwood_pike,
            itm_battle_fork,
            itm_battle_axe,
            itm_fighting_axe,
            itm_tab_shield_pavise_c,
            itm_sallet_b,
            itm_leather_gloves_a,
        ],
        def_attrib | level(24),
        wp(130),
        knows_athletics_3 | knows_shield_2 | knows_ironflesh_3,
        rhodok_face_middle_1,
        rhodok_face_older_2,
    ],
    # peasant - retainer - footman - man-at-arms -  knight
    [
        "solarian_recruit",
        "Solarian Recruit",
        "Solarian Recruits",
        tf_guarantee_boots | tf_guarantee_armor,
        0,
        0,
        fac_kingdom_6,
        [
            itm_hatchet_a,
            itm_club,
            itm_stones,
            itm_desert_boots_a,
            itm_desert_boots_b,
        ],
        def_attrib | level(5),
        wp(60),
        knows_common | knows_athletics_1,
        swadian_face_younger_1,
        swadian_face_middle_2,
    ],
    [
        "solarian_footman",
        "Solarian Footman",
        "Solarian Footmen",
        tf_guarantee_boots | tf_guarantee_armor | tf_guarantee_shield,
        0,
        0,
        fac_kingdom_6,
        [
            itm_falchion_b,
            itm_leather_gloves_a,
            itm_desert_leather_boots_a,
            itm_desert_leather_boots_b,
        ],
        def_attrib | level(10),
        wp(90),
        knows_common | knows_athletics_2,
        swadian_face_young_1,
        swadian_face_old_2,
    ],
    [
        "solarian_veteran_footman",
        "Solarian Veteran Footman",
        "Solarian Veteran Footmen",
        tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_shield
        | tf_guarantee_helmet,
        0,
        0,
        fac_kingdom_6,
        [
            itm_arabian_sword_a,
            itm_arabian_sword_b,
            itm_jarid,
            itm_arabian_sword_a,
            itm_mace_3,
            itm_leather_gloves_a,
            itm_eastern_scale_gloves_a,
            itm_desert_leather_boots_a,
            itm_desert_leather_boots_b,
        ],
        def_attrib | level(15),
        wp(120),
        knows_common
        | knows_athletics_2
        | knows_power_throw_2
        | knows_ironflesh_1
        | knows_power_strike_2
        | knows_shield_2,
        swadian_face_young_1,
        swadian_face_old_2,
    ],
    [
        "solarian_infantry",
        "Solarian Infantry",
        "Solarian Infantries",
        tf_guarantee_shield
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet,
        0,
        0,
        fac_kingdom_6,
        [
            itm_jarid,
            itm_hatchet_b,
            itm_arabian_sword_b,
            itm_mace_3,
            itm_mail_mittens_a,
            itm_eastern_scale_gloves_a,
            itm_eastern_scale_gloves_b,
            itm_desert_leather_boots_a,
            itm_desert_leather_boots_b,
        ],
        def_attrib | level(20),
        wp(150),
        knows_common
        | knows_riding_3
        | knows_ironflesh_2
        | knows_power_strike_3
        | knows_shield_3
        | knows_power_throw_3
        | knows_athletics_3,
        swadian_face_middle_1,
        swadian_face_old_2,
    ],
    [
        "solarian_guard",
        "Solarian Guard",
        "Solarian Guards",
        tf_mounted
        | tf_guarantee_shield
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet,
        0,
        0,
        fac_kingdom_6,
        [
            itm_military_pick,
            itm_hatchet_a,
            itm_jarid,
            itm_scimitar_b,
            itm_mace_4,
            itm_eastern_scale_gloves_b,
            itm_desert_heavy_boots_a,
            itm_desert_heavy_boots_b,
        ],
        def_attrib | level(25),
        wp(180),
        knows_common
        | knows_shield_3
        | knows_ironflesh_10
        | knows_power_strike_8
        | knows_power_throw_4
        | knows_athletics_9,
        swadian_face_middle_1,
        swadian_face_older_2,
    ],
    [
        "solarian_skirmisher",
        "Solarian Skirmisher",
        "Solarian Skirmishers",
        tf_guarantee_ranged | tf_guarantee_boots | tf_guarantee_armor,
        0,
        0,
        fac_kingdom_6,
        [
            itm_jarid,
            itm_jarid,
            itm_arabian_sword_a,
            itm_spiked_club,
            itm_leather_gloves_a,
            itm_leather_gloves_a_v1,
            itm_desert_leather_boots_a,
            itm_desert_leather_boots_b,
        ],
        def_attrib | level(15),
        wp(120),
        knows_common
        | knows_riding_2
        | knows_power_throw_2
        | knows_ironflesh_1
        | knows_athletics_3,
        swadian_face_young_1,
        swadian_face_middle_2,
    ],
    [
        "solarian_archer",
        "Solarian Archer",
        "Solarian Archers",
        tf_guarantee_ranged | tf_guarantee_boots | tf_guarantee_armor,
        0,
        0,
        fac_kingdom_6,
        [
            itm_arrows,
            itm_arrows,
            itm_nomad_bow,
            itm_arabian_sword_a,
            itm_leather_gloves_a,
            itm_leather_gloves_a_v1,
            itm_desert_leather_boots_a,
            itm_desert_leather_boots_b,
        ],
        def_attrib | level(20),
        wp(150),
        knows_common
        | knows_power_draw_3
        | knows_ironflesh_2
        | knows_power_throw_3
        | knows_athletics_4,
        swadian_face_young_1,
        swadian_face_old_2,
    ],
    [
        "solarian_master_archer",
        "Solarian Master Archer",
        "Solarian Master Archers",
        tf_guarantee_ranged
        | tf_mounted
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet,
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
            itm_leather_gloves_a,
            itm_leather_gloves_a_v1,
            itm_desert_leather_boots_a,
            itm_desert_leather_boots_b,
        ],
        def_attrib | level(25),
        wp(180),
        knows_common
        | knows_power_draw_4
        | knows_power_throw_4
        | knows_ironflesh_3
        | knows_athletics_5,
        swadian_face_middle_1,
        swadian_face_older_2,
    ],
    [
        "solarian_horseman",
        "Solarian Horseman",
        "Solarian Horsemen",
        tf_mounted
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet
        | tf_guarantee_horse
        | tf_guarantee_shield,
        0,
        0,
        fac_kingdom_6,
        [
            itm_arabian_sword_b,
            itm_scimitar_b,
            itm_mace_4,
            itm_eastern_scale_gloves_a,
            itm_mail_mittens_a_v1,
            itm_mail_mittens_a,
            itm_desert_leather_boots_a,
            itm_desert_leather_boots_b,
            itm_saracin_hard_horses_a_v1,
            itm_saracin_hard_horses_b_v1,
            itm_saracin_hard_horses_c_v1,
            itm_saracin_hard_horses_d_v1,
        ],
        def_attrib | level(20),
        wp_melee(150),
        knows_common
        | knows_riding_4
        | knows_ironflesh_2
        | knows_shield_2
        | knows_power_strike_3,
        swadian_face_young_1,
        swadian_face_old_2,
    ],
    [
        "solarian_knight",
        "Solarian Knight",
        "Solarian Knights",
        tf_mounted
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_gloves
        | tf_guarantee_helmet
        | tf_guarantee_horse
        | tf_guarantee_shield,
        0,
        0,
        fac_kingdom_6,
        [
            itm_scimitar_b,
            itm_mace_a_v1,
            itm_sarranid_cavalry_sword,
            itm_eastern_scale_gloves_b,
            itm_eastern_scale_gloves_a,
            itm_desert_heavy_boots_a,
            itm_desert_heavy_boots_b,
            itm_saracin_hard_horses_a,
            itm_saracin_hard_horses_b,
            itm_saracin_hard_horses_c,
            itm_saracin_hard_horses_d,
        ],
        def_attrib | level(25),
        wp_melee(180),
        knows_common
        | knows_riding_6
        | knows_shield_5
        | knows_ironflesh_8
        | knows_power_strike_9,
        swadian_face_middle_1,
        swadian_face_older_2,
    ],
    [
        "sarranid_messenger",
        "Sarranid Messenger",
        "Sarranid Messengers",
        tf_mounted
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_gloves
        | tf_guarantee_horse
        | tf_guarantee_ranged,
        0,
        0,
        fac_kingdom_6,
        [
            itm_lance,
            itm_arabian_sword_b,
            itm_scimitar_b,
            itm_mace_4,
            itm_tab_shield_small_round_b,
            itm_courser,
            itm_hunter,
        ],
        def_attrib | level(20),
        wp_melee(100),
        knows_common
        | knows_riding_4
        | knows_ironflesh_2
        | knows_shield_2
        | knows_power_strike_3,
        swadian_face_young_1,
        swadian_face_old_2,
    ],
    [
        "sarranid_deserter",
        "Sarranid Deserter",
        "Sarranid Deserters",
        tf_guarantee_ranged | tf_guarantee_boots | tf_guarantee_armor,
        0,
        0,
        fac_deserters,
        [
            itm_lance,
            itm_arabian_sword_b,
            itm_scimitar_b,
            itm_mace_4,
            itm_tab_shield_small_round_b,
            itm_arabian_horse_a,
        ],
        def_attrib | level(20),
        wp_melee(100),
        knows_common
        | knows_riding_4
        | knows_ironflesh_2
        | knows_shield_2
        | knows_power_strike_3,
        swadian_face_young_1,
        swadian_face_old_2,
    ],
    [
        "sarranid_prison_guard",
        "Prison Guard",
        "Prison Guards",
        tf_guarantee_shield
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet,
        0,
        0,
        fac_kingdom_6,
        [
            itm_arabian_sword_b,
            itm_scimitar_b,
            itm_war_spear,
            itm_mace_4,
            itm_mail_mittens_a,
            itm_leather_gloves_a,
            itm_tab_shield_kite_d,
        ],
        def_attrib | level(25),
        wp_melee(135) | wp_throwing(100),
        knows_common | knows_shield_3 | knows_ironflesh_3 | knows_power_strike_3,
        swadian_face_middle_1,
        swadian_face_older_2,
    ],
    [
        "sarranid_castle_guard",
        "Castle Guard",
        "Castle Guards",
        tf_guarantee_shield
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet,
        0,
        0,
        fac_kingdom_6,
        [
            itm_arabian_sword_b,
            itm_scimitar_b,
            itm_war_spear,
            itm_mace_4,
            itm_mail_mittens_a,
            itm_leather_gloves_a,
            itm_tab_shield_kite_d,
        ],
        def_attrib | level(25),
        wp_melee(135) | wp_throwing(100),
        knows_common | knows_shield_3 | knows_ironflesh_3 | knows_power_strike_3,
        swadian_face_middle_1,
        swadian_face_older_2,
    ],
]
