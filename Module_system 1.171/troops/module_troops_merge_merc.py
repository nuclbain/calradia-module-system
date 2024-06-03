from module_troops_utils import *

# ========================================================================================================
# Generic troops that dont really belong to any faction and mercenaries
# ========================================================================================================
troops_mercenaries = [
    # This troop is the troop marked as soldiers_begin
    [
        "farmer",
        "Farmer",
        "Farmers",
        tf_guarantee_armor,
        no_scene,
        reserved,
        fac_commoners,
        [
            itm_cleaver,
            itm_knife,
            itm_pitch_fork,
            itm_sickle,
            itm_club,
            itm_stones,
            itm_leather_cap,
            itm_felt_hat,
            itm_felt_hat,
            itm_shirt,
            itm_linen_tunic,
            itm_short_tunic,
            itm_poulaines_b,
            itm_poulaines_d,
        ],
        def_attrib | level(4),
        wp(60),
        knows_common,
        man_face_middle_1,
        man_face_old_2,
    ],
    [
        "townsman",
        "Townsman",
        "Townsmen",
        tf_guarantee_boots | tf_guarantee_armor,
        no_scene,
        reserved,
        fac_commoners,
        [
            itm_cleaver,
            itm_knife,
            itm_club,
            itm_quarter_staff,
            itm_dagger,
            itm_stones,
            itm_leather_cap,
            itm_linen_tunic,
            itm_short_tunic,
            itm_tunic_with_green_cape,
            itm_poulaines_b,
            itm_poulaines_d,
        ],
        def_attrib | level(4),
        wp(60),
        knows_common,
        mercenary_face_1,
        mercenary_face_2,
    ],
    [
        "watchman",
        "Watchman",
        "Watchmen",
        tf_guarantee_boots | tf_guarantee_armor | tf_guarantee_shield,
        no_scene,
        reserved,
        fac_commoners,
        [
            itm_bolts,
            itm_mace_3,
            itm_mace_3,
            itm_fighting_pick,
            itm_sword_medieval_a,
            itm_spear,
            itm_hunting_crossbow,
            itm_light_crossbow,
            itm_shield_kite_k,
            itm_short_tunic,
            itm_cheap_padding_a,
            itm_cheap_padding_b,
            itm_neutral_sallet_a,
            itm_neutral_sallet_b,
            itm_leather_gloves,
            itm_old_leather_gloves,
            itm_poulaines_b,
            itm_hose_b,
        ],
        def_attrib | level(9),
        wp(75),
        knows_common | knows_shield_1,
        mercenary_face_1,
        mercenary_face_2,
    ],
    [
        "caravan_guard",
        "Caravan Guard",
        "Caravan Guards",
        tf_mounted
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_horse
        | tf_guarantee_shield,
        no_scene,
        0,
        fac_commoners,
        [
            itm_fighting_pick,
            itm_sword_medieval_a,
            itm_sword_medieval_b,
            itm_sword_medieval_c_long,
            itm_sword_medieval_d_long,
            itm_spear,
            itm_shield_kite_k,
            itm_cheap_mail_a,
            itm_cheap_mail_b,
            itm_neutral_sallet_a,
            itm_neutral_sallet_b,
            itm_neutral_chapel_a,
            itm_neutral_kettlehat_a,
            itm_m_gloves_a,
            itm_poulaines_b,
            itm_hose_b,
            itm_saddle_horse,
        ],
        def_attrib | level(14),
        wp(85),
        knows_common | knows_riding_2 | knows_ironflesh_1 | knows_shield_3,
        mercenary_face_1,
        mercenary_face_2,
    ],
    [
        "mercenary_swordsman",
        "Mercenary Swordsman",
        "Mercenary Swordsmen",
        tf_mounted
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet
        | tf_guarantee_shield,
        no_scene,
        reserved,
        fac_commoners,
        [
            itm_scottish_sword,
            itm_grosse_messer_b,
            itm_crusader_sword,
            itm_longsword,
            itm_english_longsword,
            itm_german_bastard_sword,
            itm_shield_kite_k,
            itm_shield_heater_d,
            itm_neutral_aketon_a,
            itm_neutral_aketon_a_v1,
            itm_neutral_aketon_b,
            itm_neutral_aketon_c,
            itm_neutral_aketon_c_v1,
            itm_neutral_sallet_a,
            itm_neutral_sallet_b,
            itm_neutral_chapel_a,
            itm_neutral_kettlehat_a,
            itm_leather_gloves,
            itm_m_gloves_a,
            itm_poulaines_b,
            itm_hose_b,
            itm_leather_boots_a,
        ],
        def_attrib | level(20),
        wp(100),
        knows_common
        | knows_riding_3
        | knows_ironflesh_3
        | knows_shield_3
        | knows_power_strike_3,
        mercenary_face_1,
        mercenary_face_2,
    ],
    [
        "hired_blade",
        "Hired Blade",
        "Hired Blades",
        tf_mounted
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_gloves
        | tf_guarantee_helmet
        | tf_guarantee_shield,
        no_scene,
        reserved,
        fac_commoners,
        [
            itm_scottish_sword,
            itm_grosse_messer_b,
            itm_crusader_sword,
            itm_longsword,
            itm_english_longsword,
            itm_german_bastard_sword,
            itm_shield_kite_k,
            itm_shield_heater_d,
            itm_hauberk_neutral_a,
            itm_hauberk_neutral_a_v1,
            itm_neutral_sallet_a,
            itm_neutral_sallet_b,
            itm_neutral_chapel_a,
            itm_neutral_kettlehat_a,
            itm_m_gloves_a,
            itm_mail_mittens,
            itm_old_mail_gloves,
            itm_mail_boots_a,
            itm_mail_boots_b,
            itm_mail_boots_c,
        ],
        def_attrib | level(25),
        wp(130),
        knows_common
        | knows_riding_3
        | knows_athletics_5
        | knows_shield_5
        | knows_power_strike_5
        | knows_ironflesh_5,
        mercenary_face_1,
        mercenary_face_2,
    ],
    [
        "mercenary_crossbowman",
        "Mercenary Crossbowman",
        "Mercenary Crossbowmen",
        tf_guarantee_boots | tf_guarantee_armor | tf_guarantee_ranged,
        no_scene,
        reserved,
        fac_commoners,
        [
            itm_bolts,
            itm_mace_3,
            itm_mace_3,
            itm_fighting_pick,
            itm_side_sword,
            itm_longbowman_sword,
            itm_hunting_crossbow,
            itm_light_crossbow,
            itm_shield_kite_k,
            itm_neutral_aketon_a,
            itm_neutral_aketon_a_v1,
            itm_neutral_aketon_b,
            itm_neutral_aketon_c,
            itm_neutral_aketon_c_v1,
            itm_neutral_sallet_a,
            itm_neutral_sallet_b,
            itm_neutral_chapel_a,
            itm_neutral_kettlehat_a,
            itm_leather_gloves,
            itm_m_gloves_a,
            itm_poulaines_b,
            itm_hose_b,
        ],
        def_attrib | level(19),
        wp_one_handed(90)
        | wp_two_handed(90)
        | wp_polearm(90)
        | wp_archery(90)
        | wp_crossbow(130)
        | wp_throwing(90),
        knows_common | knows_athletics_5 | knows_shield_1,
        mercenary_face_1,
        mercenary_face_2,
    ],
    [
        "mercenary_horseman",
        "Mercenary Horseman",
        "Mercenary Horsemen",
        tf_mounted
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet
        | tf_guarantee_horse
        | tf_guarantee_shield,
        no_scene,
        reserved,
        fac_commoners,
        [
            itm_espada_eslavona_b,
            itm_espada_eslavona_a,
            itm_lance,
            itm_shield_heater_d,
            itm_hauberk_neutral_a,
            itm_hauberk_neutral_a_v1,
            itm_brigandine_neutral_a,
            itm_brigandine_neutral_a_v1,
            itm_brigandine_neutral_b,
            itm_brigandine_neutral_b_v1,
            itm_neutral_sallet_a,
            itm_neutral_sallet_b,
            itm_neutral_chapel_a,
            itm_neutral_kettlehat_a,
            itm_leather_gloves,
            itm_m_gloves_a,
            itm_leather_boots_a,
            itm_hunter,
        ],
        def_attrib | level(20),
        wp(100),
        knows_common
        | knows_riding_4
        | knows_ironflesh_3
        | knows_shield_2
        | knows_power_strike_3,
        mercenary_face_1,
        mercenary_face_2,
    ],
    [
        "mercenary_cavalry",
        "Mercenary Cavalry",
        "Mercenary Cavalry",
        tf_mounted
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet
        | tf_guarantee_horse
        | tf_guarantee_shield,
        no_scene,
        reserved,
        fac_commoners,
        [
            itm_crusader_sword,
            itm_longsword,
            itm_english_longsword,
            itm_german_bastard_sword,
            itm_lance,
            itm_shield_heater_d,
            itm_brigandine_neutral_heavy_a,
            itm_brigandine_neutral_heavy_a_v1,
            itm_brigandine_neutral_heavy_b,
            itm_brigandine_neutral_heavy_b_v1,
            itm_neutral_sallet_a,
            itm_neutral_sallet_b,
            itm_neutral_chapel_a,
            itm_neutral_kettlehat_a,
            itm_m_gloves_a,
            itm_mail_mittens,
            itm_old_mail_gloves,
            itm_mail_boots_a,
            itm_mail_boots_b,
            itm_mail_boots_c,
            itm_warhorse,
        ],
        def_attrib | level(25),
        wp(130),
        knows_common
        | knows_riding_5
        | knows_ironflesh_4
        | knows_shield_5
        | knows_power_strike_4,
        mercenary_face_1,
        mercenary_face_2,
    ],
    [
        "delgay_mercenary",
        "Delgay Mercenary",
        "Delgay Mercenaries",
        tf_mounted
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_horse
        | tf_guarantee_shield,
        no_scene,
        0,
        fac_commoners,
        [
            itm_solarian_turban_a,
            itm_solarian_turban_b,
            itm_solarian_turban_c,
            itm_solarian_mail_vest_f,
            itm_solarian_mail_vest_e,
            itm_eastern_scale_gloves_a,
            itm_eastern_scale_gloves_b,
            itm_desert_rich_boots_a,
            itm_desert_rich_boots_b,
            itm_maa_camel_rider_shield_a,
            itm_maa_camel_rider_shield_b,
            itm_maa_camel_rider_shield_c,
            itm_maa_camel_rider_shield_d,
            itm_maa_camel_rider_shield_e,
            itm_maa_camel_rider_shield_f,
            itm_sarranid_mace_1,
            itm_sarranid_axe_a,
            itm_sarranid_axe_b,
            itm_falshion_2,
            itm_falshion_1,
        ],
        def_attrib | level(14),
        wp(85),
        knows_common | knows_riding_2 | knows_ironflesh_1 | knows_shield_3,
        mercenary_face_1,
        mercenary_face_2,
    ],
    [
        "delgay_mercenary_assasin",
        "Delgay Mercenary Assasin",
        "Delgay Mercenaries Assasin",
        tf_mounted
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_horse
        | tf_guarantee_shield,
        no_scene,
        0,
        fac_commoners,
        [
            itm_solarian_turban_c,
            itm_solarian_armor_scale_c,
            itm_solarian_armor_scale_a,
            itm_eastern_scale_gloves_a,
            itm_eastern_scale_gloves_b,
            itm_desert_rich_boots_a,
            itm_desert_rich_boots_b,
            itm_maa_camel_rider_shield_a,
            itm_maa_camel_rider_shield_b,
            itm_maa_camel_rider_shield_c,
            itm_maa_camel_rider_shield_d,
            itm_maa_camel_rider_shield_e,
            itm_maa_camel_rider_shield_f,
            itm_falshion_2,
            itm_falshion_1,
            itm_throwing_daggers,
            itm_throwing_daggers,
        ],
        def_attrib | agi_25 | level(24),
        wp(150) | wp_throwing(220),
        knows_common
        | knows_riding_2
        | knows_ironflesh_9
        | knows_power_strike_4
        | knows_power_throw_10
        | knows_athletics_10
        | knows_shield_3,
        mercenary_face_1,
        mercenary_face_2,
    ],
    [
        "delgay_mercenary_rajas_killer",
        "Delgay Mercenary Rajas Killer",
        "Delgay Mercenaries Rajas Killers",
        tf_mounted
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_horse
        | tf_guarantee_shield,
        no_scene,
        0,
        fac_commoners,
        [
            itm_solarian_turban_c,
            itm_mkk_black_scale_a,
            itm_mkk_black_scale_b,
            itm_mkk_black_scale_c,
            itm_eastern_scale_gloves_a,
            itm_eastern_scale_gloves_b,
            itm_desert_rich_boots_a,
            itm_desert_rich_boots_b,
            itm_maa_camel_rider_shield_a,
            itm_maa_camel_rider_shield_b,
            itm_maa_camel_rider_shield_c,
            itm_maa_camel_rider_shield_d,
            itm_maa_camel_rider_shield_e,
            itm_maa_camel_rider_shield_f,
            itm_falshion_2,
            itm_falshion_1,
            itm_throwing_daggers,
            itm_throwing_daggers,
        ],
        def_attrib | agi_30 | str_30 | level(34),
        wp(250) | wp_throwing(420),
        knows_common
        | knows_riding_2
        | knows_ironflesh_10
        | knows_power_strike_8
        | knows_power_throw_10
        | knows_athletics_10
        | knows_shield_3,
        mercenary_face_1,
        mercenary_face_2,
    ],
    [
        "menegras_halberdier",
        "Menegras Halberdier",
        "Menegras Halberdiers",
        tf_guarantee_boots | tf_guarantee_armor | tf_guarantee_helmet,
        no_scene,
        reserved,
        fac_commoners,
        [
            itm_player_skull_helmet_a,
            itm_player_skull_helmet_b,
            itm_m_aketon_a,
            itm_m_aketon_b,
            itm_leather_gloves,
            itm_old_leather_gloves,
            itm_m_gloves_a,
            itm_poulaines_b,
            itm_poulaines_d,
            itm_guisarme,
            itm_swiss_halberd,
            itm_english_bill,
        ],
        def_attrib | level(14),
        wp(135),
        knows_common | knows_power_strike_2 | knows_ironflesh_2 | knows_athletics_2,
        mercenary_face_1,
        mercenary_face_2,
    ],
    [
        "experienced_menegras_halberdier",
        "Experienced Menegras Halberdier",
        "Experienced Menegras Halberdiers",
        tf_guarantee_boots | tf_guarantee_armor | tf_guarantee_helmet,
        no_scene,
        reserved,
        fac_commoners,
        [
            itm_player_skull_helmet_c,
            itm_player_skull_helmet_d,
            itm_m_hauberk_b,
            itm_m_hauberk_c,
            itm_mail_mittens,
            itm_old_mail_gloves,
            itm_m_gloves_a,
            itm_mail_boots_a,
            itm_mail_boots_b,
            itm_mail_boots_c,
            itm_guisarme,
            itm_swiss_halberd,
            itm_english_bill,
        ],
        def_attrib | level(20),
        wp(175),
        knows_common | knows_power_strike_3 | knows_ironflesh_3 | knows_athletics_3,
        mercenary_face_1,
        mercenary_face_2,
    ],
    [
        "menegras_halberdier_veteran",
        "Menegras Halberdier Veteran",
        "Menegras Halberdiers Veterans",
        tf_guarantee_boots | tf_guarantee_armor | tf_guarantee_helmet,
        no_scene,
        reserved,
        fac_commoners,
        [
            itm_player_skull_helmet_c,
            itm_player_skull_helmet_d,
            itm_m_brigandine_f,
            itm_m_brigandine_g,
            itm_mail_mittens,
            itm_m_gauntlets_a,
            itm_m_gauntlets_b,
            itm_plate_boots_a,
            itm_plate_boots_b,
            itm_guisarme,
            itm_swiss_halberd,
            itm_english_bill,
        ],
        def_attrib | level(26),
        wp(215),
        knows_common | knows_power_strike_4 | knows_ironflesh_4 | knows_athletics_4,
        mercenary_face_1,
        mercenary_face_2,
    ],
    [
        "mercenaries_end",
        "mercenaries_end",
        "mercenaries_end",
        0,
        no_scene,
        reserved,
        fac_commoners,
        [],
        def_attrib | level(4),
        wp(60),
        knows_common,
        mercenary_face_1,
        mercenary_face_2,
    ],
]
