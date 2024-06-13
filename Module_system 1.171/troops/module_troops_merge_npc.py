from module_troops_utils import *

troops_npc = [
    # NPC system changes begin
    # Companions
    [
        "kingdom_heroes_including_player_begin",
        "kingdom_heroes_including_player_begin",
        "kingdom_heroes_including_player_begin",
        tf_hero,
        0,
        reserved,
        fac_kingdom_1,
        [],
        lord_attrib,
        wp(220),
        knows_lord_1,
        0x000000000010918A01F248377289467D,
    ],
    [
        "npc1",
        "Hurey",
        "Hurey",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [itm_ragged_outfit, itm_studded_club, itm_leather_boots_a],
        str_11 | agi_13 | int_12 | cha_7 | level(3),
        wp(110),
        knows_tracker_npc
        | knows_tactics_3
        | knows_ironflesh_3
        | knows_power_strike_1
        | knows_pathfinding_3
        | knows_athletics_2
        | knows_tracking_1
        | knows_riding_2,  # skills 2/3 player at that level
        0x0000000E730065C420DB6DB6DB6DDEFF00000000001DB6F00000000000000000,
    ],
    [
        "npc2",
        "Mesym",
        "Mesym",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [itm_stormguard_aketon_plated_a, itm_m_pole_hammer_a, itm_poulaines_d],
        str_17 | agi_7 | int_11 | cha_12 | level(8),
        wp(170),
        knows_trainer_3
        | knows_weapon_master_4
        | knows_ironflesh_5
        | knows_athletics_2
        | knows_leadership_3,
        0x0000000BFF003440209B6E38E06DBEFF00000000001F36E10000000000000000,
    ],
    [
        "npc3",
        "Evel Droby",
        "Evel Droby",
        tf_female | tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_hunter_c,
            itm_tabard_d,
            itm_mt_leather_gloves_a,
            itm_hose_a,
            itm_royal_mace_decorated,
        ],
        str_6 | agi_9 | int_18 | cha_9 | level(1),
        wp(20),
        knows_wound_treatment_5
        | knows_trade_1
        | knows_first_aid_4
        | knows_surgery_5
        | knows_athletics_1
        | knows_riding_4,
        0x00000004A204300436DB6DB6DB6DFEFF00000000001DB6DB0000000000000000,
    ],
    [
        "npc4",
        "Ilhan",
        "Ilhan",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_stormguard_aketon_a,
            itm_heavy_infantry_axe,
            itm_mt_leather_gloves_a,
            itm_leather_boots_a,
            itm_throwing_knives,
        ],
        str_10 | agi_19 | int_13 | cha_10 | level(10),
        wp(145),
        knows_weapon_master_2
        | knows_power_strike_2
        | knows_riding_2
        | knows_athletics_5
        | knows_looting_5
        | knows_power_throw_7
        | knows_tactics_2
        | knows_leadership_2,
        0x0000000B7D00130020DB6DB6DB6DBEFF00000000001DB6E80000000000000000,
    ],
    [
        "npc5",
        "Gyliam Gare",
        "Gyliam Gare",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_banded_armor,
            itm_sallet_c,
            itm_m_gloves_a,
            itm_shortened_bill,
            itm_light_rifle_a,
            itm_mail_boots_a,
            itm_cartridges,
        ],
        str_23 | agi_17 | int_12 | cha_17 | level(15),
        wp(180) | wp_firearm(260),
        knows_warrior_npc
        | knows_riding_2
        | knows_horse_archery_3
        | knows_leadership_5
        | knows_weapon_master_5,
        0x0000000DFF00115420DB6DB6DB6DBEFF00000000001DB6E80000000000000000,
    ],
    [
        "npc6",
        "Ames",
        "Ames",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [itm_saddle_horse, itm_chornovalley_vest_a, itm_hatchet, itm_leather_shoes_a],
        str_10 | agi_12 | int_16 | cha_18 | level(3),
        wp(65),
        knows_riding_2
        | knows_trade_6
        | knows_inventory_management_5
        | knows_trainer_1
        | knows_leadership_1,
        0x0000000D401001CF20DB6DB6DB6DFEFF00000000001DB6D00000000000000000,
    ],
    [
        "npc7",
        "Malia Willey",
        "Malia Willey",
        tf_female | tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [itm_gambeson, itm_spear],
        str_8 | agi_9 | int_10 | cha_6 | level(2),
        wp(80),
        knows_tracker_npc
        | knows_tracking_5
        | knows_athletics_8
        | knows_spotting_5
        | knows_pathfinding_8
        | knows_power_draw_2,
        0x000000031F08000206D86DB64B4DB6DB00000000001DB6C30000000000000000,
    ],
    [
        "npc8",
        "Eryet Allard",
        "Eryet Allard",
        tf_female | tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [itm_tribal_warrior_outfit, itm_leather_boots_b, itm_sword_viking_1],
        str_9 | agi_10 | int_9 | cha_10 | level(7),
        wp(90),
        knows_warrior_npc
        | knows_weapon_master_3
        | knows_power_strike_2
        | knows_athletics_2
        | knows_leadership_3
        | knows_tactics_1,
        0x0000000FFE08000300DB6DB6496208D400000000001D86FC0000000000000000,
    ],
    [
        "npc9",
        "Aduhash",
        "Aduhash",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_mkk_mamluke_a,
            itm_eastern_scale_gloves_a,
            itm_sarranid_two_handed_mace_1,
            itm_m_bandit_turban_a,
            itm_desert_leather_boots_a,
        ],
        str_25 | agi_17 | int_12 | cha_14 | level(16),
        wp(200),
        knows_warrior_npc
        | knows_weapon_master_5
        | knows_riding_3
        | knows_athletics_3
        | knows_leadership_1
        | knows_power_strike_6,
        0x00000001900471C6125B69FCDB6DBEFF00000000001DB6FB0000000000000000,
    ],
    [
        "npc10",
        "Zela",
        "Zela",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_coat_of_plates,
            itm_medium_rifle_f,
            itm_cartridges,
            itm_scottish_sword,
            itm_tab_shield_pavise_d,
            itm_mail_boots_b,
            itm_m_gauntlets_a,
        ],
        str_15 | agi_13 | int_9 | cha_11 | level(8),
        wp(105) | wp_firearm(300),
        knows_warrior_npc
        | knows_weapon_master_5
        | knows_tactics_1
        | knows_leadership_1
        | knows_ironflesh_5
        | knows_trainer_4
        | knows_first_aid_2,
        0x0000000190042348058365C91C7D8EFF00000000001DE6FB0000000000000000,
    ],
    [
        "npc11",
        "Jane",
        "Jane",
        tf_female | tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [itm_studded_leather_coat, itm_poulaines_b, itm_falshion_1],
        str_8 | agi_11 | int_10 | cha_10 | level(2),
        wp(70),
        knows_merchant_npc
        | knows_weapon_master_1
        | knows_first_aid_1
        | knows_wound_treatment_2,
        0x00000006000C000206186196918DB8E400000000001D48C40000000000000000,
    ],
    [
        "npc12",
        "Pai Khoi-Kao",
        "Pai Khoi-Kao",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_lamellar_vest,
            itm_light_rifle_d,
            itm_cartridges,
            itm_flanged_mace,
            itm_light_leather_boots_a,
            itm_m_gloves_a,
        ],
        str_12 | agi_17 | int_13 | cha_7 | level(4),
        wp(85) | wp_firearm(200),
        knows_merchant_npc
        | knows_ironflesh_1
        | knows_power_strike_1
        | knows_surgery_4
        | knows_wound_treatment_3
        | knows_first_aid_3,
        0x00000001BF044383201D6A24DA6DBCFF00000000001DB6F80000000000000000,
    ],
    [
        "npc13",
        "Dondo",
        "Dondo",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_m_hauberk_mountain_d,
            itm_m_gloves_a,
            itm_leather_boots_b,
            itm_m_scimitar_a,
        ],
        str_9 | agi_13 | int_12 | cha_8 | level(3),
        wp(80),
        knows_warrior_npc
        | knows_riding_2
        | knows_leadership_2
        | knows_athletics_2
        | knows_ironflesh_2
        | knows_power_strike_1
        | knows_weapon_master_1,
        0x00000001BF0474D420DC6A36EA6DBCFF00000000001DB6F80000000000000000,
    ],
    [
        "npc14",
        "Elrel",
        "Elrel",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [itm_shirt, itm_leather_shoes_b, itm_sword_medieval_b_small],
        str_9 | agi_8 | int_11 | cha_8 | level(5),
        wp(100),
        knows_warrior_npc
        | knows_trainer_4
        | knows_weapon_master_3
        | knows_power_strike_1,
        0x00000001BE00024545136DC11B79FCDB00000000001DB6E80000000000000000,
    ],
    [
        "npc15",
        "Phamas",
        "Phamas",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [itm_robe, itm_maul, itm_eastern_scale_gloves_b, itm_leather_shoes_b],
        str_9 | agi_9 | int_12 | cha_8 | level(7),
        wp(80),
        knows_warrior_npc
        | knows_tactics_2
        | knows_engineer_4
        | knows_trade_3
        | knows_tracking_1
        | knows_spotting_1,
        0x0000000FB110600020DB6DD9226DBF7F00000000001DB6F80000000000000000,
    ],
    [
        "npc16",
        "Kina",
        "Kina",
        tf_female | tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [itm_short_tunic, itm_battle_trident, itm_hose_a],
        str_12 | agi_11 | int_8 | cha_7 | level(2),
        wp(80),
        knows_tracker_npc | knows_power_strike_4 | knows_athletics_2,
        0x00000000000C3001009849A2494288CB00000000001DA6830000000000000000,
    ],
    # NPC system changes end
    # Special NPCs
    [
        "quartermaster",
        "Quartermaster",
        "Quartermaster",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [itm_leather_jerkin, itm_hose_d, itm_club],
        str_7 | agi_7 | int_7 | cha_7 | level(1),
        wp(40),
        knows_common,
        swadian_face_older_2,
        swadian_face_old_2,
    ],
]
