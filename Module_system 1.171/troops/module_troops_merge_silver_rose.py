from module_troops_utils import *

troops_silver_rose = [
    # SILVER ROSE UNITS BEGIN
    [
        "silver_rose_recruit",
        "Silver Rose Recruit",
        "Silver Rose Recruits",
        tf_guarantee_armor | tf_guarantee_boots,
        0,
        0,
        fac_kingdom_1,
        [
            itm_scythe,
            itm_hatchet,
            itm_pitch_fork,
            itm_stones,
            itm_pickaxe,
            itm_falshion_1,
            itm_tab_shield_heater_a,
            itm_tab_shield_round_a,
            (itm_red_aketon_a, 0),
            (itm_red_aketon_a, imodbit_thick),
            (itm_red_aketon_a_v1, 0),
            (itm_red_aketon_a_v1, imodbit_thick),
            (itm_red_aketon_a_v2, 0),
            (itm_red_aketon_a_v2, imodbit_thick),
            itm_arming_cap_a,
            itm_felt_a,
            itm_felt_a_v1,
            itm_felt_a_v2,
            itm_felt_b,
            itm_felt_b_v1,
            itm_old_leather_gloves,
            itm_hose_b,
            itm_poulaines_b,
        ],
        def_attrib | level(5),
        wp(60),
        knows_common,
        swadian_face_younger_1,
        swadian_face_middle_2,
    ],
    [
        "silver_rose_levy",
        "Silver Rose Levy",
        "Silver Rose Levy",
        tf_guarantee_armor | tf_guarantee_boots | tf_guarantee_helmet,
        0,
        0,
        fac_kingdom_1,
        [
            itm_falshion_1,
            itm_swadia_oval_shield_1,
            itm_swadia_oval_shield_2,
            itm_cervelliere_a,
            itm_cervelliere_b,
            itm_leather_gloves,
            itm_hose_e,
        ],
        def_attrib | level(10),
        wp(90),
        knows_common,
        swadian_face_younger_1,
        swadian_face_middle_2,
    ],
    [
        "silver_rose_scout",
        "Silver Rose Scout",
        "Silver Rose Scouts",
        tf_mounted
        | tf_guarantee_armor
        | tf_guarantee_boots
        | tf_guarantee_helmet
        | tf_guarantee_horse
        | tf_guarantee_shield,
        0,
        0,
        fac_kingdom_1,
        [
            itm_swadia_oval_shield_1,
            itm_swadia_oval_shield_2,
            itm_leather_gloves,
            itm_hunter,
            itm_hose_e,
        ],
        def_attrib | level(15),
        wp(120),
        knows_common | knows_riding_3,
        swadian_face_young_1,
        swadian_face_old_2,
    ],
    [
        "silver_rose_milita",
        "Silver Rose Militia",
        "Silver Rose Militia",
        tf_guarantee_armor
        | tf_guarantee_boots
        | tf_guarantee_shield
        | tf_guarantee_helmet,
        0,
        0,
        fac_kingdom_1,
        [
            itm_crusader_spear_inf_a,
            itm_crusader_spear_inf_b,
            itm_crusader_spear_inf_c,
            itm_swadia_oval_shield_1,
            itm_swadia_oval_shield_2,
            itm_cervelliere_a,
            itm_cervelliere_b,
            itm_leather_gloves,
            itm_m_gloves_a,
            itm_leather_boots_a,
        ],
        def_attrib | level(15),
        wp(120),
        knows_common,
        swadian_face_young_1,
        swadian_face_old_2,
    ],
    [
        "silver_rose_footman",
        "Silver Rose Footman",
        "Silver Rose Footmen",
        tf_guarantee_armor
        | tf_guarantee_boots
        | tf_guarantee_shield
        | tf_guarantee_helmet,
        0,
        0,
        fac_kingdom_1,
        [
            itm_shortened_bill,
            itm_winged_mace,
            itm_flanged_mace,
            itm_crusader_spear_inf_a,
            itm_swadia_footman_shield_1,
            itm_swadia_footman_shield_2,
            itm_leather_gloves,
            itm_m_gloves_a,
            itm_leather_boots_a,
        ],
        def_attrib | level(20),
        wp_melee(150),
        knows_common
        | knows_ironflesh_3
        | knows_shield_2
        | knows_athletics_2
        | knows_power_strike_2,
        swadian_face_young_1,
        swadian_face_old_2,
    ],
    [
        "silver_rose_hacker",
        "Silver Rose Hacker",
        "Silver Rose Hackers",
        tf_guarantee_shield
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet,
        0,
        0,
        fac_kingdom_1,
        [
            itm_shortened_bill,
            itm_m_mace_knight,
            itm_swadia_footman_shield_1,
            itm_swadia_footman_shield_2,
            itm_mail_coif,
            itm_leather_gloves,
            itm_m_gloves_a,
            itm_mail_boots_a,
        ],
        def_attrib | str_22 | agi_25 | level(25),
        wp_melee(180) | wp_one_handed(50),
        knows_common | knows_ironflesh_5 | knows_power_strike_4 | knows_athletics_5,
        swadian_face_middle_1,
        swadian_face_old_2,
    ],
    [
        "silver_rose_infantry",
        "Silver Rose Infantry",
        "Silver Rose Infantry",
        tf_guarantee_shield
        | tf_guarantee_armor
        | tf_guarantee_boots
        | tf_guarantee_helmet,
        0,
        0,
        fac_kingdom_1,
        [
            itm_pike,
            itm_fighting_pick,
            itm_bastard_sword_a,
            itm_sword_medieval_a,
            itm_sword_medieval_b_small,
            itm_swadia_footman_shield_1,
            itm_swadia_footman_shield_2,
            itm_swadia_footman_shield_3,
            itm_swadia_footman_shield_4,
            itm_old_mail_gloves,
            itm_m_gloves_a,
            itm_mail_boots_a,
        ],
        def_attrib | level(25),
        wp_melee(180),
        knows_common
        | knows_riding_3
        | knows_ironflesh_4
        | knows_power_strike_3
        | knows_shield_3
        | knows_athletics_3,
        swadian_face_middle_1,
        swadian_face_old_2,
    ],
    [
        "silver_rose_sergeant",
        "Silver Rose Sergeant",
        "Silver Rose Sergeants",
        tf_mounted
        | tf_guarantee_shield
        | tf_guarantee_armor
        | tf_guarantee_boots
        | tf_guarantee_helmet,
        0,
        0,
        fac_kingdom_1,
        [
            itm_axe_crusader_a,
            itm_axe_crusader_b,
            itm_crusader_spear_inf_a,
            itm_swadia_footman_shield_1,
            itm_swadia_footman_shield_2,
            itm_swadia_footman_shield_3,
            itm_swadia_footman_shield_4,
            itm_m_gloves_a,
            itm_m_gauntlets_a,
            itm_plate_boots_a,
            itm_plate_boots_b,
        ],
        def_attrib | str_30 | agi_20 | level(30),
        wp_melee(210) | wp_one_handed(50) | wp_polearm(50),
        knows_common
        | knows_shield_4
        | knows_ironflesh_4
        | knows_power_strike_4
        | knows_athletics_4,
        swadian_face_middle_1,
        swadian_face_older_2,
    ],
    [
        "silver_rose_crossbowman",
        "Silver Rose Crossbowman",
        "Silver Rose Crossbowmen",
        tf_guarantee_ranged
        | tf_guarantee_armor
        | tf_guarantee_boots
        | tf_guarantee_helmet,
        0,
        0,
        fac_kingdom_1,
        [
            itm_bolts,
            itm_light_crossbow,
            itm_hunting_crossbow,
            itm_shortened_bill,
            itm_winged_mace,
            itm_flanged_mace,
            itm_swadia_oval_shield_1,
            itm_swadia_oval_shield_2,
            itm_hose_e,
        ],
        def_attrib | level(20),
        wp(150),
        knows_common | knows_riding_2 | knows_ironflesh_1,
        swadian_face_young_1,
        swadian_face_middle_2,
    ],
    [
        "silver_rose_trained_crossbowman",
        "Silver Rose Trained Crossbowman",
        "Silver Rose Trained Crossbowmen",
        tf_guarantee_ranged
        | tf_guarantee_armor
        | tf_guarantee_boots
        | tf_guarantee_helmet,
        0,
        0,
        fac_kingdom_1,
        [
            itm_bolts,
            itm_crossbow,
            itm_light_crossbow,
            itm_shortened_bill,
            itm_winged_mace,
            itm_flanged_mace,
            itm_swadia_oval_shield_1,
            itm_swadia_oval_shield_2,
            itm_leather_gloves,
            itm_hose_e,
        ],
        def_attrib | level(25),
        wp(180) | wp_crossbow(50),
        knows_common | knows_riding_2 | knows_ironflesh_1 | knows_athletics_1,
        swadian_face_young_1,
        swadian_face_old_2,
    ],
    [
        "silver_rose_sharpshooter",
        "Silver Rose Sharpshooter",
        "Silver Rose Sharpshooters",
        tf_guarantee_ranged
        | tf_guarantee_armor
        | tf_guarantee_boots
        | tf_guarantee_helmet,
        0,
        0,
        fac_kingdom_1,
        [
            itm_bolts,
            itm_crossbow,
            itm_crossbow,
            itm_heavy_crossbow,
            itm_shortened_bill,
            itm_m_mace_knight,
            itm_axe_crusader_1,
            itm_winged_mace,
            itm_flanged_mace,
            itm_swadia_oval_shield_1,
            itm_swadia_oval_shield_2,
            itm_leather_gloves,
            itm_m_gloves_a,
            itm_leather_boots_a,
        ],
        def_attrib | level(30),
        wp(210) | wp_crossbow(50),
        knows_common
        | knows_power_draw_3
        | knows_ironflesh_1
        | knows_power_strike_1
        | knows_athletics_2,
        swadian_face_middle_1,
        swadian_face_older_2,
    ],
    [
        "silver_rose_horseman",
        "Silver Rose Horseman",
        "Silver Rose Horsemen",
        tf_mounted
        | tf_guarantee_armor
        | tf_guarantee_helmet
        | tf_guarantee_boots
        | tf_guarantee_horse
        | tf_guarantee_shield,
        0,
        0,
        fac_kingdom_1,
        [
            itm_morningstar,
            itm_swadia_oval_shield_1,
            itm_swadia_oval_shield_2,
            itm_hunter,
            itm_hunter,
            itm_hunter_b,
            itm_hunter_c,
            itm_m_gloves_a,
            itm_leather_boots_a,
            itm_mail_boots_a,
        ],
        def_attrib | level(30),
        wp_melee(210),
        knows_common
        | knows_riding_3
        | knows_ironflesh_4
        | knows_power_strike_4
        | knows_shield_3
        | knows_athletics_3,
        swadian_face_middle_1,
        swadian_face_old_2,
    ],
    [
        "silver_rose_man_at_arms",
        "Silver Rose Man at Arms",
        "Silver Rose Men at Arms",
        tf_mounted
        | tf_guarantee_armor
        | tf_guarantee_helmet
        | tf_guarantee_boots
        | tf_guarantee_horse
        | tf_guarantee_shield,
        0,
        0,
        fac_kingdom_1,
        [
            itm_lance,
            itm_swadia_kite_shield_1,
            itm_swadia_kite_shield_2,
            itm_m_gloves_a,
            itm_hunter,
            itm_hunter_b,
            itm_hunter_c,
            itm_hunter_d,
            itm_mail_boots_a,
            itm_leather_boots_a,
            itm_plate_boots_b,
        ],
        def_attrib | level(35),
        wp_melee(240),
        knows_common
        | knows_riding_4
        | knows_ironflesh_5
        | knows_shield_2
        | knows_power_strike_5,
        swadian_face_young_1,
        swadian_face_old_2,
    ],
    [
        "silver_rose_knight",
        "Silver Rose Knight",
        "Silver Rose Knights",
        tf_mounted
        | tf_guarantee_armor
        | tf_guarantee_gloves
        | tf_guarantee_helmet
        | tf_guarantee_boots
        | tf_guarantee_horse
        | tf_guarantee_shield,
        0,
        0,
        fac_kingdom_1,
        [
            itm_crusader_knight_spear_a,
            itm_swadia_heater_shield_1,
            itm_swadia_heater_shield_2,
            itm_m_gauntlets_a,
            itm_silver_rose_heavy_horse_a,
            itm_plate_boots_a,
            itm_plate_boots_b,
            itm_mail_boots_a,
        ],
        def_attrib | level(40),
        wp_melee(270),
        knows_common
        | knows_riding_5
        | knows_shield_5
        | knows_ironflesh_8
        | knows_power_strike_8,
        swadian_face_middle_1,
        swadian_face_older_2,
    ],
    [
        "swadian_messenger",
        "Swadian Messenger",
        "Swadian Messengers",
        tf_mounted
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_gloves
        | tf_guarantee_horse
        | tf_guarantee_ranged,
        0,
        0,
        fac_kingdom_1,
        [
            itm_sword_medieval_a,
            itm_leather_jerkin,
            itm_courser,
            itm_leather_gloves,
            itm_light_crossbow,
            itm_bolts,
        ],
        str_7 | agi_21 | int_4 | cha_4 | level(25),
        wp(130),
        knows_common | knows_riding_7 | knows_horse_archery_5,
        swadian_face_young_1,
        swadian_face_old_2,
    ],
    [
        "swadian_deserter",
        "Swadian Deserter",
        "Swadian Deserters",
        tf_guarantee_ranged | tf_guarantee_boots | tf_guarantee_armor,
        0,
        0,
        fac_deserters,
        [
            itm_bolts,
            itm_light_crossbow,
            itm_hunting_crossbow,
            itm_dagger,
            itm_club,
            itm_voulge,
            itm_wooden_shield,
            itm_leather_jerkin,
            itm_padded_cloth,
            itm_padded_coif,
            itm_footman_helmet,
            itm_iron_crown_nasal_a,
        ],
        def_attrib | level(14),
        wp(80),
        knows_common | knows_riding_2 | knows_ironflesh_1,
        swadian_face_young_1,
        swadian_face_old_2,
    ],
    [
        "swadian_prison_guard",
        "Prison Guard",
        "Prison Guards",
        tf_guarantee_shield
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet,
        0,
        0,
        fac_kingdom_1,
        [
            itm_awlpike,
            itm_pike,
            itm_great_sword,
            itm_morningstar,
            itm_sword_medieval_b,
            itm_tab_shield_heater_c,
            itm_coat_of_plates,
            itm_plate_armor,
            itm_sallet_c,
            itm_black_helmet,
            itm_sallet_a,
            itm_sallet_c,
            itm_leather_gloves,
        ],
        def_attrib | level(25),
        wp(130),
        knows_common | knows_shield_3 | knows_ironflesh_3 | knows_power_strike_3,
        swadian_face_young_1,
        swadian_face_old_2,
    ],
    [
        "swadian_castle_guard",
        "Castle Guard",
        "Castle Guards",
        tf_guarantee_shield
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet,
        0,
        0,
        fac_kingdom_1,
        [
            itm_awlpike,
            itm_pike,
            itm_great_sword,
            itm_morningstar,
            itm_sword_medieval_b,
            itm_tab_shield_heater_c,
            itm_tab_shield_heater_d,
            itm_coat_of_plates,
            itm_plate_armor,
            itm_sallet_c,
            itm_black_helmet,
            itm_sallet_a,
            itm_sallet_c,
            itm_leather_gloves,
        ],
        def_attrib | level(25),
        wp(130),
        knows_common | knows_shield_3 | knows_ironflesh_3 | knows_power_strike_3,
        swadian_face_young_1,
        swadian_face_old_2,
    ],
    # SILVER ROSE UNITS END
]
