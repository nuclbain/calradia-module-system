from module_troops_utils import *

troops_celestial = [
    # CELESTIAL UNITS BEGIN
    [
        "celestial_recruit",
        "Celestial Recruit",
        "Celestial Recruits",
        tf_guarantee_boots | tf_guarantee_armor,
        0,
        0,
        fac_kingdom_3,
        [
            itm_hammer_a,
            itm_falchion_a,
            itm_voulge_a,
            itm_tab_shield_round_a,
            itm_tab_shield_tauria_a,
            itm_arming_cap_a,
            (itm_olive_aketon_a, 0),
            (itm_olive_aketon_a_v1, 0),
            (itm_olive_aketon_a_v2, 0),
            (itm_olive_aketon_a_v3, 0),
            itm_poulaines_d,
            itm_hose_d,
        ],
        def_attrib | level(5),
        wp(60),
        knows_common | knows_athletics_3 | knows_power_draw_2 | knows_horse_archery_2,
        swadian_face_young_1,
        swadian_face_old_2,
    ],
    [
        "celestial_voulgier",
        "Celestial Voulgier",
        "Celestial Voulgiers",
        tf_guarantee_boots | tf_guarantee_armor | tf_guarantee_helmet,
        0,
        0,
        fac_kingdom_3,
        [
            itm_falchion_a_v2,
            itm_sword_short_a_v1,
            itm_voulge_a,
            itm_tab_shield_tauria_a,
            itm_arming_cap_a,
            itm_cervelliere_b,
            itm_chapel_a,
            itm_chapel_a_v1,
            (itm_olive_aketon_a, imod_thick),
            (itm_olive_aketon_a, imod_hardened),
            (itm_olive_aketon_a_v1, imod_thick),
            (itm_olive_aketon_a_v1, imod_hardened),
            itm_leather_gloves_a,
            itm_leather_gloves_a_v1,
            itm_poulaines_d,
            itm_hose_d,
        ],
        def_attrib | level(10),
        wp(90),
        knows_common | knows_athletics_4 | knows_power_strike_3 | knows_power_draw_2,
        swadian_face_young_1,
        swadian_face_old_2,
    ],
    [
        "celestial_archer",
        "Celestial Archer",
        "Celestial Archers",
        tf_guarantee_boots | tf_guarantee_armor | tf_guarantee_helmet | tf_guarantee_gloves | tf_guarantee_ranged,
        0,
        0,
        fac_kingdom_3,
        [
            itm_hunting_bow,
            itm_arrows,
            itm_falchion_a,
            itm_sword_short_a,
            itm_military_pick_a,
            itm_voulge_a,
            itm_arming_cap_a,
            itm_cervelliere_a_v1,
            itm_chapel_a,
            itm_chapel_a_v1,
            (itm_olive_aketon_a, 0),
            (itm_olive_aketon_a_v1, 0),
            itm_leather_gloves_a_v1,
            itm_poulaines_d,
            itm_hose_d,
        ],
        def_attrib | level(10),
        wp(90) | wp_archery(50),
        knows_common | knows_athletics_4 | knows_power_strike_1 | knows_power_draw_4,
        swadian_face_young_1,
        swadian_face_old_2,
    ],
    [
        "celestial_houseguard",
        "Celestial Houseguard",
        "Celestial Houseguards",
        tf_guarantee_boots | tf_guarantee_armor | tf_guarantee_helmet | tf_guarantee_shield,
        0,
        0,
        fac_kingdom_3,
        [
            itm_sword_short_a_v1,
            itm_falchion_a_v2,
            itm_polehammer_d,
            itm_voulge_a,
            itm_tab_shield_tauria_a,
            itm_cervelliere_b_v1,
            itm_chapel_a_v3,
            (itm_lamellar_cuirass_a, 0),
            (itm_lamellar_cuirass_a, imod_reinforced),
            (itm_lamellar_cuirass_a_v1, 0),
            (itm_lamellar_cuirass_a_v1, imod_reinforced),
            itm_leather_gloves_a_v1,
            itm_leather_boots_a,
        ],
        def_attrib | level(15),
        wp(120),
        knows_common | knows_athletics_4 | knows_power_strike_3 | knows_power_draw_2,
        swadian_face_young_1,
        swadian_face_old_2,
    ],
    [
        "celestial_footman",
        "Celestial Footman",
        "Celestial Footmen",
        tf_guarantee_boots | tf_guarantee_armor | tf_guarantee_helmet | tf_guarantee_shield | tf_guarantee_gloves,
        0,
        0,
        fac_kingdom_3,
        [
            itm_sword_short_a_v1,
            itm_polehammer_a,
            itm_polehammer_b,
            itm_tab_shield_tauria_a,
            itm_morion_a_v2,
            (itm_olive_hauberk_a, imod_reinforced),
            (itm_olive_hauberk_a_v1, imod_reinforced),
            (itm_olive_hauberk_a_v2, imod_reinforced),
            (itm_olive_hauberk_a_v3, imod_reinforced),
            itm_leather_gloves_a_v1,
            itm_hose_d,
            itm_poulaines_d,
        ],
        def_attrib | level(20),
        wp(150),
        knows_common | knows_athletics_5 | knows_power_strike_4 | knows_power_draw_3,
        swadian_face_young_1,
        swadian_face_old_2,
    ],
    [
        "celestial_milita",
        "Celestial Milita",
        "Celestial Milita",
        tf_guarantee_boots | tf_guarantee_armor | tf_guarantee_helmet | tf_guarantee_shield | tf_guarantee_gloves,
        0,
        0,
        fac_kingdom_3,
        [
            itm_sword_a,
            itm_sword_a_v1,
            itm_voulge_a,
            itm_polehammer_d,
            itm_spear_a,
            itm_otto_shield_heraldic_a,
            itm_tab_shield_tauria_a,
            itm_morion_b_v1,
            itm_morion_b_v2,
            (itm_olive_aketon_b, imod_reinforced),
            (itm_olive_aketon_b_v1, imod_reinforced),
            (itm_olive_aketon_b_v2, imod_reinforced),
            (itm_olive_aketon_b_v3, imod_reinforced),
            itm_leather_gloves_a_v1,
            itm_hose_d,
            itm_poulaines_d,
        ],
        def_attrib | level(10),
        wp(90),
        knows_shield_2 | knows_ironflesh_4 | knows_power_strike_4,
        swadian_face_younger_1,
        swadian_face_old_2,
    ],
    [
        "celestial_hunter",
        "Celestial Hunter",
        "Celestial Hunters",
        tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet
        | tf_guarantee_shield
        | tf_guarantee_gloves
        | tf_guarantee_ranged,
        0,
        0,
        fac_kingdom_3,
        [
            itm_falchion_a,
            itm_military_pick_a,
            itm_hunting_crossbow,
            itm_bolts,
            itm_tab_shield_tauria_a,
            itm_chapel_a,
            itm_chapel_a_v1,
            (itm_olive_aketon_a, imod_reinforced),
            (itm_olive_aketon_a_v1, imod_reinforced),
            (itm_olive_aketon_a_v2, imod_reinforced),
            (itm_olive_aketon_a_v3, imod_reinforced),
            itm_leather_gloves_a_v1,
            itm_hose_d,
            itm_poulaines_d,
        ],
        def_attrib | level(10),
        wp(90) | wp_crossbow(50),
        knows_common | knows_athletics_5,
        swadian_face_younger_1,
        swadian_face_old_2,
    ],
    [
        "celestial_crossbowman",
        "Celestial Crossbowman",
        "Celestial Crossbowmen",
        tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet
        | tf_guarantee_shield
        | tf_guarantee_gloves
        | tf_guarantee_ranged,
        0,
        0,
        fac_kingdom_3,
        [
            itm_falchion_a,
            itm_military_pick_a,
            itm_sniper_crossbow,
            itm_heavy_crossbow,
            itm_bolts,
            itm_steel_bolts,
            itm_piercing_bolts,
            itm_tab_shield_tauria_a,
            itm_chapel_a_v2,
            itm_chapel_a_v3,
            (itm_olive_aketon_b, imod_reinforced),
            (itm_olive_aketon_b_v1, imod_reinforced),
            (itm_olive_aketon_b_v2, imod_reinforced),
            (itm_olive_aketon_b_v3, imod_reinforced),
            itm_leather_gloves_a_v1,
            itm_hose_d,
            itm_poulaines_d,
        ],
        def_attrib | level(15),
        wp(120) | wp_crossbow(50),
        knows_common | knows_athletics_8 | knows_power_strike_3,
        swadian_face_younger_1,
        swadian_face_old_2,
    ],
    [
        "celestial_armsman",
        "Celestial Armsman",
        "Celestial Armsmen",
        tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet
        | tf_guarantee_shield
        | tf_guarantee_gloves,
        0,
        0,
        fac_kingdom_3,
        [
            itm_falchion_a,
            itm_polehammer_a,
            itm_polehammer_c,
            itm_polehammer_c_v1,
            itm_tab_shield_tauria_a,
            itm_otto_shield_heraldic_a,
            itm_otto_shield_heraldic_a_v1,
            itm_morion_a_v2,
            (itm_olive_hauberk_b, imod_reinforced),
            (itm_olive_hauberk_b_v1, imod_reinforced),
            (itm_olive_hauberk_b_v2, imod_reinforced),
            (itm_olive_hauberk_b_v3, imod_reinforced),
            itm_leather_gloves_a_v1,
            itm_poulaines_d,
            itm_hose_d,
        ],
        def_attrib | level(15),
        wp(120),
        knows_common | knows_ironflesh_5 | knows_shield_1 | knows_power_strike_2,
        swadian_face_young_1,
        swadian_face_older_2,
    ],
    [
        "celestial_foot_knight",
        "Celestial Foot Knight",
        "Celestial Foot Knights",
        tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet
        | tf_guarantee_shield
        | tf_guarantee_gloves,
        0,
        0,
        fac_kingdom_3,
        [
            itm_falchion_c_v2,
            itm_sword_great_a,
            itm_sword_great_a_v1,
            itm_tab_shield_tauria_a,
            itm_morion_b_v4,
            itm_morion_b_v5,
            (itm_olive_brigandine_d, 0),
            (itm_olive_brigandine_d_v1, 0),
            itm_leather_gloves_a_v1,
            itm_poulaines_d,
            itm_hose_d,
        ],
        def_attrib | level(15),
        wp(120) | wp_two_handed(50),
        knows_athletics_6 | knows_ironflesh_5 | knows_power_strike_5,
        swadian_face_young_1,
        swadian_face_older_2,
    ],
    [
        "celestial_sergeant",
        "Celestial Sergeant",
        "Celestial Sergeants",
        tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet
        | tf_guarantee_shield
        | tf_guarantee_gloves,
        0,
        0,
        fac_kingdom_3,
        [
            itm_sword_a_v2,
            itm_sword_a_v3,
            itm_poleaxe_a,
            itm_tab_shield_tauria_a,
            itm_morion_b_v4,
            itm_morion_b_v5,
            (itm_olive_brigandine_d, 0),
            (itm_olive_brigandine_d_v1, 0),
            itm_leather_gloves_a_v1,
            itm_mail_boots_a,
            itm_mail_boots_b,
            itm_mail_boots_c,
        ],
        def_attrib | level(20),
        wp(150),
        knows_power_strike_5 | knows_ironflesh_3 | knows_athletics_6 | knows_shield_1,
        swadian_face_middle_1,
        swadian_face_older_2,
    ],
    [
        "celestial_commander",
        "Celestial Commander",
        "Celestial Commanders",
        tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet
        | tf_guarantee_shield
        | tf_guarantee_gloves,
        0,
        0,
        fac_kingdom_3,
        [
            itm_sword_a_v2,
            itm_axe_a,
            itm_axe_a_v1,
            itm_axe_a_v2,
            itm_polehammer_a,
            itm_polehammer_b,
            itm_otto_shield_heraldic_a,
            itm_otto_shield_heraldic_a_v1,
            itm_morion_b_v4,
            itm_morion_b_v5,
            (itm_olive_churburg_mail_a, 0),
            (itm_olive_churburg_mail_b, 0),
            (itm_olive_churburg_mail_c, 0),
            itm_plate_gauntlets_a,
            itm_plate_gauntlets_a_v1,
            itm_plate_boots_a,
            itm_plate_boots_b,
        ],
        def_attrib | level(25),
        wp(180) | wp_polearm(50),
        knows_power_strike_8 | knows_ironflesh_10 | knows_shield_8 | knows_athletics_8,
        swadian_face_middle_1,
        swadian_face_older_2,
    ],
    [
        "celestial_squire",
        "Celestial Squire",
        "Celestial Squires",
        tf_guarantee_boots | tf_guarantee_armor | tf_guarantee_helmet | tf_guarantee_gloves,
        0,
        0,
        fac_kingdom_3,
        [
            itm_sword_a_v2,
            itm_sword_a_v3,
            itm_tab_shield_tauria_a,
            itm_morion_a_v2,
            itm_morion_b_v2,
            (itm_olive_aketon_b, imod_reinforced),
            (itm_olive_aketon_b_v1, imod_reinforced),
            (itm_olive_aketon_b_v2, imod_reinforced),
            (itm_olive_aketon_b_v3, imod_reinforced),
            itm_leather_gloves_a_v1,
            itm_leather_boots_a,
        ],
        def_attrib | level(15),
        wp(120),
        knows_power_strike_3 | knows_ironflesh_3 | knows_athletics_4,
        swadian_face_young_1,
        swadian_face_older_2,
    ],
    [
        "celestial_initiate_knight",
        "Celestial Initiate Knight",
        "Celestial Initiate Knights",
        tf_mounted | tf_guarantee_all_wo_ranged,
        0,
        0,
        fac_kingdom_3,
        [
            itm_lance_a,
            itm_sword_a_v2,
            itm_sword_a_v3,
            itm_tab_shield_tauria_a,
            itm_morion_a_v2,
            itm_morion_b_v2,
            (itm_olive_aketon_b, imod_reinforced),
            (itm_olive_aketon_b_v1, imod_reinforced),
            (itm_olive_aketon_b_v2, imod_reinforced),
            (itm_olive_aketon_b_v3, imod_reinforced),
            itm_leather_gloves_a_v1,
            itm_leather_boots_a,
            itm_hunter,
        ],
        def_attrib | level(20),
        wp(150),
        knows_riding_5 | knows_power_strike_4 | knows_ironflesh_4 | knows_shield_2,
        swadian_face_middle_1,
        swadian_face_older_2,
    ],
    [
        "celestial_lancer",
        "Celestial Lancer",
        "Celestial Lancers",
        tf_mounted | tf_guarantee_all_wo_ranged,
        0,
        0,
        fac_kingdom_3,
        [
            itm_lance_a,
            itm_sword_knight_a,
            itm_axe_a,
            itm_tab_shield_tauria_b,
            itm_morion_b_v4,
            itm_morion_b_v5,
            (itm_full_plate_armor_a, 0),
            itm_leather_gloves_a_v1,
            itm_plate_gauntlets_a,
            itm_plate_gauntlets_a_v1,
            itm_plate_boots_a,
            itm_plate_boots_b,
            itm_warhorse,
        ],
        def_attrib | level(25),
        wp(180),
        knows_riding_7 | knows_power_strike_9 | knows_ironflesh_7 | knows_shield_2,
        swadian_face_middle_1,
        swadian_face_older_2,
    ],
    [
        "khergit_messenger",
        "Khergit Messenger",
        "Khergit Messengers",
        tf_mounted
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_gloves
        | tf_guarantee_horse
        | tf_guarantee_ranged,
        0,
        0,
        fac_kingdom_3,
        [
            itm_sword_khergit_2,
            itm_leather_jerkin,
            itm_courser,
            itm_leather_gloves_a,
            itm_short_bow,
            itm_arrows,
        ],
        str_7 | agi_21 | int_4 | cha_4 | level(25),
        wp(125),
        knows_common | knows_riding_7 | knows_horse_archery_5 | knows_power_draw_5,
        khergit_face_young_1,
        khergit_face_older_2,
    ],
    [
        "khergit_deserter",
        "Khergit Deserter",
        "Khergit Deserters",
        tf_guarantee_ranged | tf_guarantee_boots | tf_guarantee_armor,
        0,
        0,
        fac_deserters,
        [
            itm_arrows,
            itm_spiked_mace,
            itm_axe,
            itm_sword_khergit_1,
            itm_short_bow,
            itm_short_bow,
            itm_hunting_bow,
            itm_javelin,
            itm_javelin,
            itm_steppe_cap,
            itm_khergit_armor,
            itm_steppe_armor,
            itm_tribal_warrior_outfit,
        ],
        str_10 | agi_5 | int_4 | cha_4 | level(14),
        wp(80),
        knows_ironflesh_1 | knows_power_draw_1,
        khergit_face_young_1,
        khergit_face_older_2,
    ],
    [
        "khergit_prison_guard",
        "Prison Guard",
        "Prison Guards",
        tf_guarantee_shield
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet,
        0,
        0,
        fac_kingdom_3,
        [
            itm_sword_khergit_3,
            itm_tab_shield_small_round_b,
            itm_tab_shield_small_round_a,
            itm_lamellar_vest_khergit,
            itm_khergit_guard_helmet,
            itm_khergit_cavalry_helmet,
        ],
        def_attrib | level(24),
        wp(130),
        knows_athletics_5 | knows_shield_2 | knows_ironflesh_5,
        khergit_face_middle_1,
        khergit_face_older_2,
    ],
    [
        "khergit_castle_guard",
        "Castle Guard",
        "Castle Guards",
        tf_guarantee_shield
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet,
        0,
        0,
        fac_kingdom_3,
        [
            itm_sword_khergit_4,
            itm_tab_shield_small_round_b,
            itm_tab_shield_small_round_a,
            itm_lamellar_vest_khergit,
            itm_khergit_guard_helmet,
            itm_khergit_cavalry_helmet,
        ],
        def_attrib | level(24),
        wp(130),
        knows_athletics_5 | knows_shield_2 | knows_ironflesh_5,
        khergit_face_middle_1,
        khergit_face_older_2,
    ],
    # CELESTIAL UNITS END
]