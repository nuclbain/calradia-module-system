from module_troops_utils import *

troops_iron_crown = [
    # IRON CROWN UNITS BEGIN
    [
        "iron_crown_recruit",
        "Iron Crown Recruit",
        "Iron Crown Recruits",
        tf_guarantee_armor | tf_guarantee_boots,
        0,
        0,
        fac_kingdom_4,
        [
            itm_hatchet_b,
            itm_hatchet_a,
            itm_hammer_a,
            itm_long_pole_mace_a,
            itm_tab_shield_round_a,
            itm_pilgrim_hood,
            itm_felt_a,
            itm_felt_a_v1,
            itm_felt_a_v2,
            itm_felt_b,
            itm_felt_b_v1,
            (itm_rough_gray_shirt_a, 0),
            itm_leather_gloves_a,
            itm_hose_d,
            itm_poulaines_d,
        ],
        def_attrib | level(5),
        wp(60),
        knows_power_strike_1 | knows_power_throw_1 | knows_riding_1 | knows_athletics_1,
        nord_face_younger_1,
        nord_face_old_2,
    ],
    [
        "iron_crown_raider",
        "Iron Crown Raider",
        "Iron Crown Raiders",
        tf_guarantee_armor
        | tf_guarantee_shield
        | tf_guarantee_helmet
        | tf_guarantee_boots,
        0,
        0,
        fac_kingdom_4,
        [
            itm_sword_short_a,
            itm_spear_a,
            itm_tab_shield_round_a,
            itm_tab_shield_small_round_a,
            itm_tab_shield_round_b,
            itm_arming_cap_a,
            itm_nasal_helmet_a,
            itm_nasal_helmet_b,
            (itm_gray_aketon_a, 0),
            (itm_gray_aketon_a_v1, 0),
            (itm_gray_aketon_a_v2, 0),
            itm_leather_gloves_a,
            itm_leather_gloves_b,
            itm_leather_shoes_a_v1,
            itm_leather_shoes_b_v1,
        ],
        def_attrib | level(10),
        wp(90),
        knows_ironflesh_2
        | knows_power_strike_3
        | knows_riding_2
        | knows_athletics_2
        | knows_shield_1,
        nord_face_young_1,
        nord_face_old_2,
    ],
    [
        "iron_crown_reaver",
        "Iron Crown Reaver",
        "Iron Crown Reavers",
        tf_guarantee_armor
        | tf_guarantee_shield
        | tf_guarantee_helmet
        | tf_guarantee_boots,
        0,
        0,
        fac_kingdom_4,
        [
            itm_sword_short_b,
            itm_spear_a,
            itm_tab_shield_round_b,
            itm_tab_shield_round_c,
            itm_javelin,
            itm_nasal_helmet_a_v1,
            itm_nasal_helmet_b_v1,
            (itm_gray_aketon_a, imod_thick),
            (itm_gray_aketon_a_v1, imod_thick),
            (itm_gray_aketon_a_v2, imod_thick),
            itm_leather_gloves_a,
            itm_leather_gloves_b,
            itm_leather_shoes_a_v1,
            itm_leather_shoes_b_v1,
        ],
        def_attrib | level(15),
        wp(120),
        knows_ironflesh_3
        | knows_power_strike_4
        | knows_power_throw_3
        | knows_athletics_3
        | knows_shield_2,
        nord_face_young_1,
        nord_face_old_2,
    ],
    [
        "iron_crown_pirate",
        "Iron Crown Pirate",
        "Iron Crown Pirates",
        tf_guarantee_armor
        | tf_guarantee_boots
        | tf_guarantee_helmet
        | tf_guarantee_gloves
        | tf_guarantee_shield,
        0,
        0,
        fac_kingdom_4,
        [
            itm_sword_a,
            itm_spear_a,
            itm_tab_shield_round_b,
            itm_tab_shield_round_c,
            itm_javelin,
            itm_nasal_helmet_a_v2,
            itm_nasal_helmet_b_v2,
            (itm_gray_leather_armor_a, 0),
            (itm_gray_leather_armor_a_v1, 0),
            (itm_gray_leather_armor_a_v2, 0),
            itm_leather_gloves_a,
            itm_leather_gloves_b,
            itm_leather_shoes_a_v1,
            itm_leather_shoes_b_v1,
        ],
        def_attrib | level(20),
        wp(150),
        knows_ironflesh_4
        | knows_power_strike_5
        | knows_power_throw_4
        | knows_athletics_4
        | knows_shield_3,
        nord_face_young_1,
        nord_face_old_2,
    ],
    [
        "iron_crown_guardian",
        "Iron Crown Guardian",
        "Iron Crown Guardians",
        tf_guarantee_armor
        | tf_guarantee_shield
        | tf_guarantee_helmet
        | tf_guarantee_boots
        | tf_guarantee_gloves,
        0,
        0,
        fac_kingdom_4,
        [
            itm_heavy_axe_a,
            itm_javelin,
            itm_nasal_helmet_a_v2,
            itm_nasal_helmet_b_v2,
            (itm_gray_aketon_b, 0),
            (itm_gray_aketon_b_v1, 0),
            (itm_gray_aketon_b_v2, 0),
            itm_leather_gloves_a,
            itm_leather_gloves_b,
            itm_light_leather_boots_a_v1,
            itm_light_leather_boots_b_v1,
            itm_light_leather_boots_c_v1,
        ],
        def_attrib | level(20),
        wp(150) | wp_two_handed(50),
        knows_ironflesh_5 | knows_power_strike_6 | knows_athletics_5,
        nord_face_young_1,
        nord_face_old_2,
    ],
    [
        "iron_crown_footman",
        "Iron Crown Footman",
        "Iron Crown Footmen",
        tf_guarantee_armor
        | tf_guarantee_shield
        | tf_guarantee_helmet
        | tf_guarantee_gloves
        | tf_guarantee_boots,
        0,
        0,
        fac_kingdom_4,
        [
            itm_bardiche_a,
            itm_heavy_axe_a,
            itm_sword_short_b,
            itm_spear_a,
            itm_tab_shield_round_b,
            itm_tab_shield_round_c,
            itm_nasal_helmet_a_v2,
            itm_nasal_helmet_b_v2,
            (itm_gray_aketon_a, imod_reinforced),
            (itm_gray_aketon_a_v1, imod_reinforced),
            (itm_gray_aketon_a_v2, imod_reinforced),
            itm_leather_gloves_a,
            itm_leather_gloves_b,
            itm_leather_shoes_a_v1,
            itm_leather_shoes_b_v1,
        ],
        def_attrib | level(15),
        wp(120),
        knows_ironflesh_3
        | knows_power_strike_3
        | knows_power_throw_2
        | knows_riding_2
        | knows_athletics_3
        | knows_shield_2,
        nord_face_young_1,
        nord_face_old_2,
    ],
    [
        "iron_crown_man_at_arms",
        "Iron Crown Man-at-Arms",
        "Iron Crown Men-at-Arms",
        tf_guarantee_armor
        | tf_guarantee_shield
        | tf_guarantee_helmet
        | tf_guarantee_gloves
        | tf_guarantee_boots,
        0,
        0,
        fac_kingdom_4,
        [
            itm_heavy_war_axe_b,
            itm_heavy_war_axe_b_v1,
            itm_sword_a,
            itm_spear_a,
            itm_tab_shield_round_c,
            itm_nasal_helmet_a_v3,
            itm_nasal_helmet_b_v3,
            (itm_gray_leather_armor_a, imod_thick),
            (itm_gray_leather_armor_a_v1, imod_thick),
            (itm_gray_leather_armor_a_v2, imod_thick),
            itm_leather_gloves_a,
            itm_leather_gloves_b,
            itm_leather_boots_a,
        ],
        def_attrib | level(20),
        wp(150),
        knows_ironflesh_4
        | knows_power_strike_4
        | knows_power_throw_3
        | knows_riding_2
        | knows_athletics_4
        | knows_shield_3,
        nord_face_young_1,
        nord_face_older_2,
    ],
    [
        "iron_crown_vetaran",
        "Iron Crown Veteran",
        "Iron Crown Veterans",
        tf_guarantee_armor
        | tf_guarantee_shield
        | tf_guarantee_helmet
        | tf_guarantee_boots,
        0,
        0,
        fac_kingdom_4,
        [
            itm_sword_a,
            itm_sword_a_v1,
            itm_heavy_war_axe_b,
            itm_heavy_war_axe_b_v1,
            itm_spear_a,
            itm_throwing_axes,
            itm_tab_shield_round_d,
            itm_nasal_helmet_a_v3,
            itm_nasal_helmet_b_v3,
            (itm_gray_leather_armor_b, 0),
            (itm_gray_leather_armor_b_v1, 0),
            (itm_gray_leather_armor_b_v2, 0),
            (itm_gray_hauberk_a, 0),
            (itm_gray_hauberk_a_v1, 0),
            (itm_gray_hauberk_a_v2, 0),
            itm_mail_mittens_a,
            itm_mail_boots_a,
            itm_mail_boots_b,
            itm_mail_boots_c,
        ],
        def_attrib | level(25),
        wp(180),
        knows_ironflesh_5
        | knows_power_strike_5
        | knows_riding_3
        | knows_athletics_5
        | knows_shield_4,
        nord_face_young_1,
        nord_face_older_2,
    ],
    [
        "iron_crown_champion",
        "Iron Crown Champion",
        "Iron Crown Champions",
        tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_shield
        | tf_guarantee_helmet,
        0,
        0,
        fac_kingdom_4,
        [
            itm_sword_a,
            itm_sword_a_v1,
            itm_heavy_war_axe_b,
            itm_heavy_war_axe_b_v1,
            itm_spear_a,
            itm_throwing_axes,
            itm_tab_shield_round_d,
            itm_nasal_helmet_a_v4,
            itm_nasal_helmet_b_v4,
            (itm_gray_leather_armor_b, 0),
            (itm_gray_leather_armor_b_v1, 0),
            (itm_gray_leather_armor_b_v2, 0),
            (itm_gray_hauberk_a, 0),
            (itm_gray_hauberk_a_v1, 0),
            (itm_gray_hauberk_a_v2, 0),
            itm_mail_mittens_a,
            itm_plate_gauntlets_a,
            itm_plate_gauntlets_a_v1,
            itm_mail_boots_a,
            itm_plate_boots_b,
        ],
        def_attrib | level(30),
        wp(210),
        knows_ironflesh_9
        | knows_power_strike_7
        | knows_power_throw_5
        | knows_riding_2
        | knows_athletics_7
        | knows_shield_6,
        nord_face_middle_1,
        nord_face_older_2,
    ],
    [
        "iron_crown_halberdier",
        "Iron Crown Halberdier",
        "Iron Crown Halberdiers",
        tf_guarantee_armor
        | tf_guarantee_shield
        | tf_guarantee_boots
        | tf_guarantee_helmet
        | tf_guarantee_gloves,
        0,
        0,
        fac_kingdom_4,
        [
            itm_polearm_voulge_a,
            itm_polearm_voulge_b,
            itm_polearm_voulge_c,
            itm_throwing_axes,
            itm_nasal_helmet_a_v4,
            itm_nasal_helmet_b_v4,
            (itm_gray_hauberk_b, 0),
            (itm_gray_hauberk_b, imod_thick),
            (itm_gray_hauberk_b_v1, 0),
            (itm_gray_hauberk_b_v1, imod_thick),
            itm_plate_gauntlets_a,
            itm_plate_gauntlets_a_v1,
            itm_plate_gauntlets_a_v2,
            itm_plate_boots_b,
        ],
        def_attrib | level(25),
        wp(180) | wp_polearm(180),
        knows_ironflesh_6
        | knows_power_strike_7
        | knows_athletics_8
        | knows_power_throw_4,
        nord_face_young_1,
        nord_face_older_2,
    ],
    [
        "iron_crown_skirmisher",
        "Iron Crown Skirmisher",
        "Iron Crown Skirmisher",
        tf_guarantee_ranged | tf_guarantee_boots | tf_guarantee_armor,
        0,
        0,
        fac_kingdom_4,
        [
            itm_bolts,
            itm_bolts,
            itm_hunting_crossbow,
            itm_crossbow,
            itm_falchion_a,
            itm_arming_cap_a,
            itm_padded_coif_a,
            itm_padded_coif_a_v1,
            (itm_gray_aketon_a, 0),
            (itm_gray_aketon_a_v1, 0),
            (itm_gray_aketon_a_v2, 0),
            itm_hatchet_a,
            itm_leather_gloves_a,
            itm_hose_d,
            itm_poulaines_d,
        ],
        def_attrib | level(10),
        wp(90) | wp_archery(50),
        knows_ironflesh_1 | knows_power_draw_2 | knows_athletics_2,
        nord_face_young_1,
        nord_face_old_2,
    ],
    [
        "iron_crown_trained_skirmisher",
        "Iron Crown Trained Skirmisher",
        "Iron Crown Trained Skirmishers",
        tf_guarantee_ranged
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet
        | tf_guarantee_gloves,
        0,
        0,
        fac_kingdom_4,
        [
            itm_bolts,
            itm_bolts,
            itm_steel_bolts,
            itm_heavy_crossbow,
            itm_crossbow,
            itm_military_pick_a,
            itm_falchion_a,
            itm_nasal_helmet_a_v2,
            itm_nasal_helmet_b_v2,
            (itm_gray_leather_armor_a, 0),
            (itm_gray_leather_armor_a_v1, 0),
            (itm_gray_leather_armor_a_v2, 0),
            itm_leather_gloves_a,
            itm_leather_gloves_b,
            itm_leather_boots_a,
        ],
        def_attrib | level(15),
        wp(120) | wp_archery(50),
        knows_ironflesh_5 | knows_athletics_5 | knows_power_draw_6,
        nord_face_young_1,
        nord_face_old_2,
    ],
    [
        "nord_messenger",
        "Nord Messenger",
        "Nord Messengers",
        tf_mounted
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_gloves
        | tf_guarantee_horse
        | tf_guarantee_ranged,
        0,
        0,
        fac_kingdom_4,
        [
            itm_sword_viking_2,
            itm_leather_jerkin,
            itm_courser,
            itm_leather_gloves_a,
            itm_short_bow,
            itm_arrows,
        ],
        str_7 | agi_21 | int_4 | cha_4 | level(25),
        wp(130),
        knows_common | knows_riding_7 | knows_horse_archery_5 | knows_power_draw_5,
        nord_face_young_1,
        nord_face_older_2,
    ],
    [
        "nord_deserter",
        "Nord Deserter",
        "Nord Deserters",
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
            itm_leather_vest_regular_shirt_a,
            itm_nomad_armor,
        ],
        str_10 | agi_5 | int_4 | cha_4 | level(14),
        wp(80),
        knows_ironflesh_1 | knows_power_draw_1,
        nord_face_young_1,
        nord_face_older_2,
    ],
    [
        "nord_prison_guard",
        "Prison Guard",
        "Prison Guards",
        tf_guarantee_shield
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet,
        0,
        0,
        fac_kingdom_4,
        [
            itm_ashwood_pike,
            itm_battle_fork,
            itm_battle_axe,
            itm_fighting_axe,
            itm_tab_shield_round_d,
            itm_white_hauberk_a,
            itm_mail_coif,
            itm_mail_coif,
            itm_mail_coif,
            itm_cervelliere_a_v3,
            itm_leather_gloves_a,
        ],
        def_attrib | level(24),
        wp(130),
        knows_athletics_3 | knows_shield_2 | knows_ironflesh_3,
        nord_face_middle_1,
        nord_face_older_2,
    ],
    [
        "nord_castle_guard",
        "Castle Guard",
        "Castle Guards",
        tf_guarantee_shield
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet,
        0,
        0,
        fac_kingdom_4,
        [
            itm_ashwood_pike,
            itm_battle_fork,
            itm_battle_axe,
            itm_fighting_axe,
            itm_tab_shield_round_d,
            itm_tab_shield_round_e,
            itm_white_hauberk_a,
            itm_heraldic_mail_with_tabard,
            itm_mail_coif,
            itm_mail_coif,
            itm_mail_coif,
            itm_cervelliere_a_v3,
            itm_leather_gloves_a,
        ],
        def_attrib | level(24),
        wp(130),
        knows_athletics_3 | knows_shield_2 | knows_ironflesh_3,
        nord_face_middle_1,
        nord_face_older_2,
    ],
    # IRON CROWN UNITS END
]
