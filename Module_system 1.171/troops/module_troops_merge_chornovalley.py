from module_troops_utils import *

troops_chornovalley = [
    # CHORNOVALLEY UNITS BEGIN
    [
        "chornovalley_recruit",
        "Chornovalley Recruit",
        "Chornovalley Recruits",
        tf_guarantee_boots | tf_guarantee_armor,
        0,
        0,
        fac_kingdom_2,
        [
            itm_mace_a,
            itm_hatchet_a,
            itm_hatchet_b,
            itm_stones,
            itm_tab_shield_kite_a,
            itm_adventurer_hood_a,
            itm_felt_b,
            itm_felt_b_v1,
            (itm_brown_shirt_a, 0),
            (itm_brown_shirt_a_v1, 0),
            (itm_rough_brown_shirt_a, 0),
            (itm_rough_brown_shirt_a_v1, 0),
            itm_leather_gloves_a_v1,
            itm_hose_b,
            itm_poulaines_b,
        ],
        def_attrib | level(5),
        wp(60),
        knows_common,
        vaegir_face_younger_1,
        vaegir_face_middle_2,
    ],
    [
        "chornovalley_warden",
        "Chornovalley Warden",
        "Chornovalley Wardens",
        tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_shield
        | tf_guarantee_helmet,
        0,
        0,
        fac_kingdom_2,
        [
            itm_mace_a,
            itm_mace_a_v1,
            itm_heavy_axe_a,
            itm_maul_a,
            itm_adventurer_hood_a,
            itm_felt_b_v1,
            itm_padded_coif_a_v1,
            itm_padded_coif_b_v1,
            (itm_brown_shirt_a, 0),
            (itm_brown_shirt_a_v1, 0),
            (itm_rough_brown_shirt_a, 0),
            (itm_rough_brown_shirt_a_v1, 0),
            itm_leather_gloves_a,
            itm_hose_b,
            itm_poulaines_b,
        ],
        def_attrib | level(10),
        wp(90),
        knows_common,
        vaegir_face_young_1,
        vaegir_face_middle_2,
    ],
    [
        "chornovalley_gatekeeper",
        "Chornovalley Gatekeeper",
        "Chornovalley Gatekeepers",
        tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_shield
        | tf_guarantee_helmet,
        0,
        0,
        fac_kingdom_2,
        [
            itm_pickaxe_a,
            itm_pickaxe_a_v1,
            itm_spear_a,
            itm_spear_a_v1,
            itm_spear_a_v2,
            itm_tab_shield_kite_b,
            itm_sallet_d,
            itm_sallet_d_v1,
            itm_chapel_c,
            itm_chapel_c_v1,
            (itm_brown_aketon_a, imod_hardened),
            (itm_brown_aketon_a_v1, imod_hardened),
            (itm_brown_aketon_a_v2, imod_hardened),
            itm_leather_gloves_a,
            itm_hose_b,
            itm_poulaines_b,
        ],
        def_attrib | level(15),
        wp(120),
        knows_common,
        vaegir_face_young_1,
        vaegir_face_middle_2,
    ],
    [
        "chornovalley_scout",
        "Chornovalley Scout",
        "Chornovalley Scouts",
        tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_shield
        | tf_guarantee_helmet,
        0,
        0,
        fac_kingdom_2,
        [
            itm_mace_a_v1,
            itm_spear_a,
            itm_tab_shield_kite_b,
            itm_sallet_d,
            itm_sallet_d_v1,
            itm_chapel_c,
            itm_chapel_c_v1,
            (itm_brown_shirt_a, 0),
            (itm_brown_shirt_a_v1, 0),
            (itm_rough_brown_shirt_a, 0),
            (itm_rough_brown_shirt_a_v1, 0),
            itm_leather_gloves_a_v1,
            itm_hose_b,
            itm_poulaines_b,
        ],
        def_attrib | level(10),
        wp(90),
        knows_common,
        vaegir_face_young_1,
        vaegir_face_middle_2,
    ],
    [
        "chornovalley_hunter",
        "Chornovalley Hunter",
        "Chornovalley Hunters",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_2,
        [
            itm_arrows,
            itm_hunting_bow,
            itm_mace_1,
            itm_hatchet_b,
            itm_hatchet_a,
            itm_padded_coif_a_v1,
            itm_padded_coif_b_v1,
            (itm_brown_shirt_a, 0),
            (itm_brown_shirt_a_v1, 0),
            (itm_rough_brown_shirt_a, 0),
            (itm_rough_brown_shirt_a_v1, 0),
            itm_leather_gloves_a_v1,
            itm_hose_b,
            itm_poulaines_b,
        ],
        def_attrib | level(15),
        wp(120) | wp_archery(50),
        knows_ironflesh_1 | knows_power_draw_2 | knows_power_throw_1,
        vaegir_face_young_1,
        vaegir_face_old_2,
    ],
    [
        "chornovalley_longbowman",
        "Chornovalley Longbowman",
        "Chornovalley Longbowmen",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_2,
        [
            itm_arrows,
            itm_long_bow,
            itm_falchion_a,
            itm_padded_coif_a_v1,
            itm_padded_coif_b_v1,
            (itm_brown_aketon_a, 0),
            (itm_brown_aketon_a_v1, 0),
            (itm_brown_aketon_a_v2, 0),
            itm_leather_gloves_a_v1,
            itm_hose_b,
            itm_poulaines_b,
        ],
        def_attrib | level(20),
        wp(150) | wp_archery(50),
        knows_ironflesh_1
        | knows_power_draw_4
        | knows_athletics_6
        | knows_power_throw_1,
        vaegir_face_young_1,
        vaegir_face_older_2,
    ],
    [
        "chornovalley_warrior",
        "Chornovalley Warrior",
        "Chornovalley Warriors",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_2,
        [
            itm_heavy_war_axe_a,
            itm_heavy_war_axe_a_v1,
            itm_spear_a,
            itm_norman_shield_1,
            itm_tab_shield_round_b,
            itm_sallet_d,
            itm_sallet_d_v1,
            itm_sallet_d_v2,
            itm_sallet_d_v3,
            itm_chapel_c,
            itm_chapel_c_v1,
            (itm_brown_hauberk_a, 0),
            (itm_brown_hauberk_a_v1, 0),
            (itm_brown_hauberk_a_v2, 0),
            itm_leather_gloves_a_v1,
            itm_light_leather_boots_a,
            itm_light_leather_boots_b,
            itm_light_leather_boots_c,
        ],
        def_attrib | level(15),
        wp_melee(120),
        knows_athletics_2 | knows_ironflesh_4 | knows_power_strike_2 | knows_shield_2,
        vaegir_face_young_1,
        vaegir_face_old_2,
    ],
    [
        "chornovalley_sheriff",
        "Chornovalley Sheriff",
        "Chornovalley Sheriffs",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_2,
        [
            itm_heavy_war_axe_a,
            itm_heavy_war_axe_a_v1,
            itm_norman_shield_2,
            itm_spear_a,
            itm_tab_shield_round_b,
            itm_tab_shield_round_c,
            itm_tab_shield_small_round_b,
            itm_sallet_d_v3,
            itm_sallet_d_v4,
            itm_sallet_d_v5,
            itm_chapel_c_v2,
            itm_chapel_c_v3,
            (itm_brown_hauberk_a, imod_hardened),
            (itm_brown_hauberk_a_v1, imod_hardened),
            (itm_brown_hauberk_a_v2, imod_hardened),
            itm_leather_gloves_a_v1,
            itm_light_leather_boots_a,
            itm_light_leather_boots_b,
            itm_light_leather_boots_c,
            itm_mail_boots_a,
            itm_mail_boots_b,
            itm_mail_boots_c,
        ],
        def_attrib | level(20),
        wp_melee(150),
        knows_athletics_3 | knows_ironflesh_5 | knows_power_strike_3 | knows_shield_2,
        vaegir_face_young_1,
        vaegir_face_older_2,
    ],
    [
        "chornovalley_sergeant",
        "Chornovalley Sergeant",
        "Chornovalley Sergeants",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_2,
        [
            itm_heavy_war_axe_a,
            itm_heavy_war_axe_a_v1,
            itm_maul_b,
            itm_maul_b_v1,
            itm_sword_short_b_v2,
            itm_spear_a,
            itm_norman_shield_2,
            itm_norman_shield_3,
            itm_sallet_d_v4,
            itm_sallet_d_v5,
            (itm_brown_brigandine_b, 0),
            (itm_brown_brigandine_b_v1, 0),
            (itm_brown_brigandine_b, imod_reinforced),
            (itm_brown_brigandine_b_v1, imod_reinforced),
            itm_leather_gloves_a_v1,
            itm_plate_gauntlets_a,
            itm_plate_gauntlets_a_v1,
            itm_plate_boots_a,
            itm_plate_boots_b,
        ],
        def_attrib | level(25),
        wp_melee(180),
        knows_athletics_7 | knows_ironflesh_9 | knows_power_strike_7 | knows_shield_2,
        vaegir_face_young_1,
        vaegir_face_older_2,
    ],
    [
        "chornovalley_gunslider",
        "Chornovalley Gunslider",
        "Chornovalley Gunsliders",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_2,
        [
            itm_sword_short_a,
            itm_military_pick_a,
            itm_military_pick_a_v1,
            itm_military_pick_a_v2,
            itm_pistol_a,
            itm_pistol_b,
            itm_cartridges,
            itm_cervelliere_a,
            itm_facemask_a,
            (itm_brown_pourpoint_a, 0),
            (itm_brown_pourpoint_a, imod_sturdy),
            (itm_brown_pourpoint_a, imod_thick),
            itm_leather_gloves_a_v1,
            itm_light_leather_boots_a,
            itm_light_leather_boots_b,
            itm_light_leather_boots_c,
        ],
        def_attrib | level(20),
        wp_melee(150) | wp_firearm(50),
        knows_riding_2
        | knows_athletics_9
        | knows_shield_2
        | knows_ironflesh_5
        | knows_power_strike_4,
        vaegir_face_middle_1,
        vaegir_face_older_2,
    ],
    [
        "chornovalley_sniper",
        "Chornovalley Sniper",
        "Chornovalley Snipers",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_2,
        [
            itm_sword_short_a,
            itm_military_pick_a,
            itm_military_pick_a_v1,
            itm_military_pick_a_v2,
            itm_light_rifle_c,
            itm_light_rifle_d,
            itm_cartridges,
            itm_cervelliere_a,
            itm_facemask_a,
            (itm_brown_brigandine_a, 0),
            (itm_brown_brigandine_a, imod_hardened),
            (itm_brown_brigandine_a, imod_reinforced),
            (itm_brown_brigandine_a_v1, 0),
            (itm_brown_brigandine_a_v1, imod_hardened),
            (itm_brown_brigandine_a_v1, imod_reinforced),
            itm_leather_gloves_a_v1,
            itm_light_leather_boots_a,
            itm_light_leather_boots_b,
            itm_light_leather_boots_c,
        ],
        def_attrib | level(25),
        wp_melee(180) | wp_firearm(50),
        knows_riding_2
        | knows_athletics_9
        | knows_shield_2
        | knows_ironflesh_5
        | knows_power_strike_4,
        vaegir_face_middle_1,
        vaegir_face_older_2,
    ],
    [
        "chornovalley_horseman",
        "Chornovalley Horseman",
        "Chornovalley Horsemen",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_2,
        [
            itm_lance_a,
            itm_sword_a,
            itm_sword_a_v1,
            itm_tab_shield_kite_cav_a,
            (itm_brown_hauberk_a, imod_hardened),
            (itm_brown_hauberk_a_v1, imod_hardened),
            (itm_brown_hauberk_a_v2, imod_hardened),
            itm_leather_gloves_a_v1,
            itm_light_leather_boots_a,
            itm_light_leather_boots_b,
            itm_light_leather_boots_c,
            itm_hunter,
        ],
        def_attrib | level(20),
        wp(150),
        knows_riding_3 | knows_ironflesh_3 | knows_power_strike_3,
        vaegir_face_young_1,
        vaegir_face_older_2,
    ],
    [
        "chornovalley_knight",
        "Chornovalley Knight",
        "Chornovalley Knights",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_2,
        [
            itm_heavy_war_axe_b,
            itm_heavy_war_axe_b_v1,
            itm_lance_a,
            itm_tab_shield_kite_cav_b,
            itm_sallet_d_v4,
            itm_sallet_d_v5,
            (itm_brown_brigandine_b, 0),
            (itm_brown_brigandine_b_v1, 0),
            (itm_brown_brigandine_b, imod_reinforced),
            (itm_brown_brigandine_b_v1, imod_reinforced),
            itm_leather_gloves_a_v1,
            itm_plate_gauntlets_a,
            itm_plate_gauntlets_a_v1,
            itm_mail_boots_a,
            itm_mail_boots_b,
            itm_mail_boots_c,
            itm_hunter,
        ],
        def_attrib | level(25),
        wp(180),
        knows_riding_4 | knows_shield_2 | knows_ironflesh_4 | knows_power_strike_4,
        vaegir_face_middle_1,
        vaegir_face_older_2,
    ],
    [
        "vaegir_messenger",
        "Vaegir Messenger",
        "Vaegir Messengers",
        tf_mounted
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_gloves
        | tf_guarantee_horse
        | tf_guarantee_ranged,
        0,
        0,
        fac_kingdom_2,
        [
            itm_sword_medieval_b,
            itm_regular_leather_jerkin_a,
            itm_courser,
            itm_leather_gloves_a,
            itm_short_bow,
            itm_arrows,
        ],
        str_7 | agi_21 | int_4 | cha_4 | level(25),
        wp(130),
        knows_common | knows_riding_7 | knows_horse_archery_5 | knows_power_draw_5,
        vaegir_face_young_1,
        vaegir_face_older_2,
    ],
    [
        "vaegir_deserter",
        "Vaegir Deserter",
        "Vaegir Deserters",
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
            itm_regular_nomad_vest_a,
        ],
        str_10 | agi_5 | int_4 | cha_4 | level(14),
        wp(80),
        knows_ironflesh_1 | knows_power_draw_1,
        vaegir_face_young_1,
        vaegir_face_older_2,
    ],
    [
        "vaegir_prison_guard",
        "Prison Guard",
        "Prison Guards",
        tf_guarantee_shield
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet,
        0,
        0,
        fac_kingdom_2,
        [
            itm_ashwood_pike,
            itm_battle_fork,
            itm_bardiche,
            itm_battle_axe,
            itm_fighting_axe,
            itm_tab_shield_kite_b,
            itm_regular_leather_jerkin_b,
            itm_mail_coif,
            itm_mail_coif,
            itm_mail_coif,
            itm_cervelliere_a_v3,
            itm_leather_gloves_a,
        ],
        def_attrib | level(24),
        wp(130),
        knows_athletics_3 | knows_shield_2 | knows_ironflesh_3,
        vaegir_face_middle_1,
        vaegir_face_older_2,
    ],
    [
        "vaegir_castle_guard",
        "Castle Guard",
        "Castle Guards",
        tf_guarantee_shield
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet,
        0,
        0,
        fac_kingdom_2,
        [
            itm_ashwood_pike,
            itm_battle_fork,
            itm_bardiche,
            itm_battle_axe,
            itm_fighting_axe,
            itm_tab_shield_kite_d,
            itm_regular_leather_jerkin_b,
            itm_mail_coif,
            itm_mail_coif,
            itm_mail_coif,
            itm_cervelliere_a_v3,
            itm_leather_gloves_a,
        ],
        def_attrib | level(24),
        wp(130),
        knows_athletics_3 | knows_shield_2 | knows_ironflesh_3,
        vaegir_face_middle_1,
        vaegir_face_older_2,
    ],
    # CHORNOVALLEY UNITS END
]
