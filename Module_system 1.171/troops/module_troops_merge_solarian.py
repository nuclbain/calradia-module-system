from module_troops_utils import *

troops_solarian = [
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
            itm_falchion_a,
            itm_stones,
            itm_tab_shield_small_round_a,
            itm_yellow_turban_a,
            itm_yellow_turban_b,
            itm_yellow_turban_c,
            (itm_yellow_aketon_a, 0),
            (itm_yellow_aketon_a_v1, 0),
            itm_leather_gloves_a,
            itm_hose_f,
            itm_poulaines_f,
        ],
        def_attrib | level(5),
        wp(60),
        knows_common | knows_athletics_1,
        swadian_face_younger_1,
        swadian_face_middle_2,
    ],
    [
        "solarian_militia",
        "Solarian Militia",
        "Solarian Militias",
        tf_guarantee_boots | tf_guarantee_armor | tf_guarantee_shield,
        0,
        0,
        fac_kingdom_6,
        [
            itm_hatchet_a,
            itm_falchion_a,
            itm_mace_b,
            itm_spear_b,
            itm_stones,
            itm_tab_shield_small_round_a,
            itm_yellow_turban_a,
            itm_yellow_turban_b,
            itm_yellow_turban_c,
            (itm_yellow_aketon_a, imod_thick),
            (itm_yellow_aketon_a_v1, imod_thick),
            itm_leather_gloves_a,
            itm_hose_f,
            itm_poulaines_f,
        ],
        def_attrib | level(10),
        wp(90),
        knows_common
        | knows_athletics_2
        | knows_power_throw_1
        | knows_shield_1
        | knows_ironflesh_1,
        swadian_face_younger_1,
        swadian_face_middle_2,
    ],
    [
        "solarian_spearman",
        "Solarian Spearman",
        "Solarian Spearmen",
        tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_shield
        | tf_guarantee_helmet,
        0,
        0,
        fac_kingdom_6,
        [
            itm_spear_b,
            itm_spear_b_v1,
            itm_mace_b,
            itm_mace_b_v1,
            itm_tab_shield_small_round_a,
            itm_yellow_turban_chapel_a,
            itm_yellow_turban_chapel_a_v1,
            (itm_yellow_aketon_b, 0),
            (itm_yellow_aketon_b_v1, 0),
            itm_mail_mittens_a,
            itm_leather_gloves_a,
            itm_hose_f,
            itm_poulaines_f,
        ],
        def_attrib | level(15),
        wp(120),
        knows_common | knows_athletics_2 | knows_shield_2 | knows_ironflesh_3,
        swadian_face_younger_1,
        swadian_face_middle_2,
    ],
    [
        "solarian_sworn_spearman",
        "Solarian Sworn Spearman",
        "Solarian Sworn Spearmen",
        tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_shield
        | tf_guarantee_helmet
        | tf_guarantee_gloves,
        0,
        0,
        fac_kingdom_6,
        [
            itm_spear_b,
            itm_spear_b_v1,
            itm_mace_b,
            itm_mace_b_v1,
            itm_darts,
            itm_tab_shield_small_round_a,
            itm_yellow_turban_chapel_a,
            itm_yellow_turban_chapel_a_v1,
            itm_yellow_turban_sallet_a,
            itm_yellow_turban_sallet_a_v1,
            (itm_yellow_hauberk_a, 0),
            (itm_yellow_hauberk_a_v1, 0),
            (itm_yellow_hauberk_a, imod_thick),
            (itm_yellow_hauberk_a_v1, imod_thick),
            itm_mail_mittens_a,
            itm_leather_gloves_a,
            itm_hose_f,
            itm_poulaines_f,
        ],
        def_attrib | level(20),
        wp(150),
        knows_common
        | knows_athletics_3
        | knows_shield_3
        | knows_ironflesh_4
        | knows_power_strike_2
        | knows_power_throw_3,
        swadian_face_middle_1,
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
            itm_falchion_a,
            itm_falchion_a_v1,
            itm_falchion_a_v2,
            itm_mace_b,
            itm_spear_b,
            itm_darts,
            itm_tab_shield_small_round_a,
            itm_yellow_turban_a,
            itm_yellow_turban_b,
            itm_yellow_turban_c,
            (itm_yellow_aketon_a, imod_hardened),
            (itm_yellow_aketon_a_v1, imod_hardened),
            itm_leather_gloves_a,
            itm_hose_f,
            itm_poulaines_f,
        ],
        def_attrib | level(10),
        wp(90),
        knows_common
        | knows_athletics_2
        | knows_power_throw_1
        | knows_shield_1
        | knows_ironflesh_1,
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
            itm_sword_b_v3,
            itm_mace_b,
            itm_mace_b_v1,
            itm_darts,
            itm_solarian_round_shield_a,
            itm_solarian_footman_helmet_a,
            itm_solarian_footman_helmet_a_v1,
            (itm_yellow_hauberk_a, imod_reinforced),
            (itm_yellow_hauberk_a_v1, imod_reinforced),
            itm_leather_gloves_a,
            itm_leather_gloves_a_v1,
            itm_hose_f,
            itm_poulaines_f,
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
            itm_sword_b_v2,
            itm_sword_b_v3,
            itm_mace_b,
            itm_mace_b_v1,
            itm_mace_b_v2,
            itm_darts,
            itm_solarian_round_shield_a,
            itm_solarian_footman_helmet_a,
            itm_solarian_footman_helmet_a_v1,
            (itm_yellow_hauberk_b, 0),
            (itm_yellow_hauberk_b_v1, 0),
            itm_leather_gloves_a,
            itm_leather_gloves_a_v1,
            itm_leather_boots_a,
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
            itm_sword_b_v3,
            itm_sword_b_v4,
            itm_mace_b_v2,
            itm_polearm_voulge_c,
            itm_war_darts,
            itm_solarian_oval_shield_a,
            itm_solarian_footman_helmet_b,
            (itm_yellow_hauberk_c, imod_thick),
            (itm_yellow_hauberk_c_v1, imod_thick),
            itm_leather_gloves_a,
            itm_mail_mittens_a,
            itm_plate_gauntlets_a_v1,
            itm_leather_boots_a,
            itm_plate_boots_b,
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
            itm_war_darts,
            itm_war_darts,
            itm_falchion_a,
            itm_mace_b,
            itm_tab_shield_small_round_a,
            itm_yellow_turban_a,
            itm_yellow_turban_b,
            itm_yellow_turban_c,
            (itm_yellow_pourpoint_a, 0),
            itm_leather_gloves_a,
            itm_hose_f,
            itm_poulaines_f,
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
            itm_hunting_bow,
            itm_falchion_a,
            itm_mace_b,
            itm_tab_shield_small_round_a,
            itm_yellow_turban_chapel_a,
            itm_yellow_turban_chapel_a_v1,
            (itm_yellow_pourpoint_a, imod_sturdy),
            (itm_yellow_pourpoint_a, imod_thick),
            itm_leather_gloves_a,
            itm_leather_gloves_b,
            itm_hose_f,
            itm_poulaines_f,
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
            itm_long_bow,
            itm_sword_b_v3,
            itm_mace_b_v2,
            itm_solarian_round_shield_a,
            itm_solarian_footman_helmet_a,
            itm_solarian_footman_helmet_a_v1,
            (itm_yellow_hauberk_a, imod_reinforced),
            (itm_yellow_hauberk_a_v1, imod_reinforced),
            itm_leather_gloves_a_v1,
            itm_leather_gloves_b_v1,
            itm_hose_f,
            itm_poulaines_f,
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
            itm_sword_b,
            itm_lance_b,
            itm_lance_b_v1,
            itm_solarian_round_shield_a,
            itm_solarian_footman_helmet_a,
            itm_solarian_footman_helmet_a_v1,
            (itm_yellow_hauberk_a, imod_reinforced),
            (itm_yellow_hauberk_a_v1, imod_reinforced),
            itm_leather_gloves_a_v1,
            itm_mail_mittens_a,
            itm_mail_mittens_a_v1,
            itm_leather_boots_a,
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
            itm_sword_b,
            itm_sword_b_v1,
            itm_lance_b_v2,
            itm_lance_b_v3,
            itm_solarian_oval_shield_a,
            itm_solarian_footman_helmet_b,
            itm_solarian_footman_helmet_b_v1,
            (itm_yellow_hauberk_c, imod_thick),
            (itm_yellow_hauberk_c_v1, imod_thick),
            (itm_yellow_hauberk_c, imod_reinforced),
            (itm_yellow_hauberk_c_v1, imod_reinforced),
            itm_leather_gloves_a_v1,
            itm_mail_mittens_a,
            itm_plate_gauntlets_a_v1,
            itm_leather_boots_a,
            itm_plate_boots_a,
            itm_plate_boots_b,
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
