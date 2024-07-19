from module_troops_utils import *

# Undefined an unsorted troops and utility troops
# that don't fit into any other category
troops_undefined = [
    # Chests
    [
        "zendar_chest",
        "{!}Zendar Chest",
        "{!}Zendar Chest",
        tf_hero | tf_inactive,
        0,
        reserved,
        fac_neutral,
        [],
        def_attrib | level(18),
        wp(60),
        knows_common,
        0,
    ],
    [
        "tutorial_chest_1",
        "{!}Melee Weapons Chest",
        "{!}Melee Weapons Chest",
        tf_hero | tf_inactive,
        0,
        reserved,
        fac_neutral,
        [
            itm_tutorial_sword,
            itm_tutorial_axe,
            itm_tutorial_spear,
            itm_tutorial_club,
            itm_tutorial_battle_axe,
        ],
        def_attrib | level(18),
        wp(60),
        knows_common,
        0,
    ],
    [
        "tutorial_chest_2",
        "{!}Ranged Weapons Chest",
        "{!}Ranged Weapons Chest",
        tf_hero | tf_inactive,
        0,
        reserved,
        fac_neutral,
        [
            itm_tutorial_short_bow,
            itm_tutorial_arrows,
            itm_tutorial_crossbow,
            itm_tutorial_bolts,
            itm_tutorial_throwing_daggers,
        ],
        def_attrib | level(18),
        wp(60),
        knows_common,
        0,
    ],
    [
        "bonus_chest_1",
        "{!}Bonus Chest",
        "{!}Bonus Chest",
        tf_hero | tf_inactive,
        0,
        reserved,
        fac_neutral,
        [itm_strange_armor, itm_strange_short_sword],
        def_attrib | level(18),
        wp(60),
        knows_common,
        0,
    ],
    [
        "bonus_chest_2",
        "{!}Bonus Chest",
        "{!}Bonus Chest",
        tf_hero | tf_inactive,
        0,
        reserved,
        fac_neutral,
        [itm_strange_boots, itm_strange_sword],
        def_attrib | level(18),
        wp(60),
        knows_common,
        0,
    ],
    [
        "bonus_chest_3",
        "{!}Bonus Chest",
        "{!}Bonus Chest",
        tf_hero | tf_inactive,
        0,
        reserved,
        fac_neutral,
        [itm_strange_helmet, itm_strange_great_sword],
        def_attrib | level(18),
        wp(60),
        knows_common,
        0,
    ],
    # New chests
    [
        "bonus_chest_4",
        "{!}Bonus Chest",
        "{!}Bonus Chest",
        tf_hero | tf_inactive,
        0,
        reserved,
        fac_neutral,
        [],
        def_attrib | level(18),
        wp(60),
        knows_common,
        0,
    ],
    [
        "bonus_chest_5",
        "{!}Bonus Chest",
        "{!}Bonus Chest",
        tf_hero | tf_inactive,
        0,
        reserved,
        fac_neutral,
        [itm_sallet_a_v5, itm_axe_crusader_1],
        def_attrib | level(18),
        wp(60),
        knows_common,
        0,
    ],
    [
        "household_possessions",
        "{!}household_possessions",
        "{!}household_possessions",
        tf_hero | tf_inactive | tf_is_merchant,
        0,
        reserved,
        fac_neutral,
        [],
        def_attrib | level(18),
        wp(60),
        knows_inventory_management_10,
        0,
    ],
    # These are used as arrays in the scripts.
    [
        "temp_array_a",
        "{!}temp_array_a",
        "{!}temp_array_a",
        tf_hero | tf_inactive,
        0,
        reserved,
        fac_neutral,
        [],
        def_attrib | level(18),
        wp(60),
        knows_common,
        0,
    ],
    [
        "temp_array_b",
        "{!}temp_array_b",
        "{!}temp_array_b",
        tf_hero | tf_inactive,
        0,
        reserved,
        fac_neutral,
        [],
        def_attrib | level(18),
        wp(60),
        knows_common,
        0,
    ],
    [
        "temp_array_c",
        "{!}temp_array_c",
        "{!}temp_array_c",
        tf_hero | tf_inactive,
        0,
        reserved,
        fac_neutral,
        [],
        def_attrib | level(18),
        wp(60),
        knows_common,
        0,
    ],
    [
        "stack_selection_amounts",
        "{!}stack_selection_amounts",
        "{!}stack_selection_amounts",
        tf_hero | tf_inactive,
        0,
        reserved,
        fac_neutral,
        [],
        def_attrib,
        0,
        knows_common,
        0,
    ],
    [
        "stack_selection_ids",
        "{!}stack_selection_ids",
        "{!}stack_selection_ids",
        tf_hero | tf_inactive,
        0,
        reserved,
        fac_neutral,
        [],
        def_attrib,
        0,
        knows_common,
        0,
    ],
    [
        "notification_menu_types",
        "{!}notification_menu_types",
        "{!}notification_menu_types",
        tf_hero | tf_inactive,
        0,
        reserved,
        fac_neutral,
        [],
        def_attrib,
        0,
        knows_common,
        0,
    ],
    [
        "notification_menu_var1",
        "{!}notification_menu_var1",
        "{!}notification_menu_var1",
        tf_hero | tf_inactive,
        0,
        reserved,
        fac_neutral,
        [],
        def_attrib,
        0,
        knows_common,
        0,
    ],
    [
        "notification_menu_var2",
        "{!}notification_menu_var2",
        "{!}notification_menu_var2",
        tf_hero | tf_inactive,
        0,
        reserved,
        fac_neutral,
        [],
        def_attrib,
        0,
        knows_common,
        0,
    ],
    [
        "banner_background_color_array",
        "{!}banner_background_color_array",
        "{!}banner_background_color_array",
        tf_hero | tf_inactive,
        0,
        reserved,
        fac_neutral,
        [],
        def_attrib,
        0,
        knows_common,
        0,
    ],
    [
        "multiplayer_data",
        "{!}multiplayer_data",
        "{!}multiplayer_data",
        tf_hero | tf_inactive,
        0,
        reserved,
        fac_neutral,
        [],
        def_attrib,
        0,
        knows_common,
        0,
    ],
    # Add Extra Quest NPCs below this point
    [
        "local_merchant",
        "Local Merchant",
        "Local Merchants",
        tf_guarantee_boots | tf_guarantee_armor,
        0,
        0,
        fac_commoners,
        [itm_peasant_regular_shirt_a_v1, itm_butchering_knife],
        def_attrib | level(5),
        wp(40),
        knows_power_strike_1,
        merchant_face_1,
        merchant_face_2,
    ],
    [
        "tax_rebel",
        "Peasant Rebel",
        "Peasant Rebels",
        tf_guarantee_armor,
        0,
        reserved,
        fac_commoners,
        [
            itm_cleaver,
            itm_knife,
            itm_pitch_fork,
            itm_sickle,
            itm_club,
            itm_stones,
            itm_arming_cap_a,
            itm_felt_a,
            itm_felt_b,
            itm_regular_shirt_b,
            itm_regular_shirt_d,
        ],
        def_attrib | level(4),
        wp(60),
        knows_common,
        vaegir_face1,
        vaegir_face2,
    ],
    [
        "trainee_peasant",
        "Peasant",
        "Peasants",
        tf_guarantee_armor,
        0,
        reserved,
        fac_commoners,
        [
            itm_cleaver,
            itm_knife,
            itm_pitch_fork,
            itm_sickle,
            itm_club,
            itm_stones,
            itm_arming_cap_a,
            itm_felt_a,
            itm_felt_b,
            itm_regular_shirt_b,
            itm_regular_shirt_d,
        ],
        def_attrib | level(4),
        wp(60),
        knows_common,
        vaegir_face1,
        vaegir_face2,
    ],
    [
        "fugitive",
        "Nervous Man",
        "Nervous Men",
        tf_guarantee_boots | tf_guarantee_armor,
        0,
        0,
        fac_commoners,
        [
            itm_regular_shirt_b,
            itm_regular_shirt_d,
            itm_tabard_a,
            itm_leather_vest_regular_shirt_a,
            itm_arming_cap_a,
            itm_sword_medieval_b,
            itm_throwing_daggers,
        ],
        def_attrib | str_24 | agi_25 | level(26),
        wp(180),
        knows_common | knows_power_throw_6 | knows_power_strike_6 | knows_ironflesh_9,
        man_face_middle_1,
        man_face_old_2,
    ],
    [
        "belligerent_drunk",
        "Belligerent Drunk",
        "Belligerent Drunks",
        tf_guarantee_boots | tf_guarantee_armor,
        0,
        0,
        fac_commoners,
        [
            itm_sword_short_a,
            itm_tabard_a,
            itm_brown_shirt_a,
            itm_brown_shirt_a_v1,
            itm_arming_cap_a,
            itm_leather_gloves_a,
            itm_hose_d,
            itm_poulaines_d,
        ],
        def_attrib | str_20 | agi_8 | level(15),
        wp(120),
        knows_common | knows_power_strike_2 | knows_ironflesh_9,
        bandit_face1,
        bandit_face2,
    ],
    [
        "hired_assassin",
        "Hired Assassin",
        "Hired Assassin",
        tf_guarantee_boots | tf_guarantee_armor,
        0,
        0,
        fac_commoners,  # they look like belligerent drunks
        [
            itm_regular_shirt_b,
            itm_regular_shirt_d,
            itm_tabard_a,
            itm_leather_vest_regular_shirt_a,
            itm_arming_cap_a,
            itm_sword_viking_1,
        ],
        def_attrib | str_20 | agi_16 | level(20),
        wp(180),
        knows_common | knows_power_strike_5 | knows_ironflesh_3,
        bandit_face1,
        bandit_face2,
    ],
    [
        "fight_promoter",
        "Rough-Looking Character",
        "Rough-Looking Character",
        tf_guarantee_boots | tf_guarantee_armor,
        0,
        0,
        fac_commoners,
        [
            itm_regular_shirt_b,
            itm_regular_shirt_d,
            itm_tabard_a,
            itm_leather_vest_regular_shirt_a,
            itm_arming_cap_a,
            itm_sword_viking_1,
        ],
        def_attrib | str_20 | agi_16 | level(20),
        wp(180),
        knows_common | knows_power_strike_5 | knows_ironflesh_3,
        bandit_face1,
        bandit_face2,
    ],
    [
        "spy",
        "Ordinary Townsman",
        "Ordinary Townsmen",
        tf_mounted
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_gloves
        | tf_guarantee_horse,
        0,
        0,
        fac_neutral,
        [itm_sword_viking_1, itm_leather_jerkin, itm_courser, itm_leather_gloves_a],
        def_attrib | agi_11 | level(20),
        wp(130),
        knows_common,
        man_face_middle_1,
        man_face_older_2,
    ],
    [
        "spy_partner",
        "Unremarkable Townsman",
        "Unremarkable Townsmen",
        tf_mounted
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_gloves
        | tf_guarantee_horse,
        0,
        0,
        fac_neutral,
        [itm_sword_medieval_b, itm_leather_jerkin, itm_courser, itm_leather_gloves_a],
        def_attrib | agi_11 | level(10),
        wp(130),
        knows_common,
        vaegir_face1,
        vaegir_face2,
    ],
    [
        "nurse_for_lady",
        "Nurse",
        "Nurse",
        tf_female | tf_guarantee_armor,
        0,
        reserved,
        fac_commoners,
        [itm_robe, itm_black_hood],
        def_attrib | level(4),
        wp(60),
        knows_common,
        woman_face_1,
        woman_face_2,
    ],
    [
        "temporary_minister",
        "Minister",
        "Minister",
        tf_guarantee_armor | tf_guarantee_boots,
        0,
        reserved,
        fac_commoners,
        [itm_tabard_d],
        def_attrib | level(4),
        wp(60),
        knows_common,
        man_face_middle_1,
        man_face_older_2,
    ],
    [
        "quick_battle_6_player",
        "{!}quick_battle_6_player",
        "{!}quick_battle_6_player",
        tf_hero,
        0,
        reserved,
        fac_player_faction,
        [
            itm_padded_cloth,
            itm_cervelliere_a,
            itm_sword_medieval_b,
            itm_crossbow,
            itm_bolts,
            itm_plate_covered_round_shield,
        ],
        knight_attrib_1,
        wp(130),
        knight_skills_1,
        0x000000000008010B01F041A9249F65FD,
    ],
    # Multiplayer ai troops
    [
        "silver_rose_trained_crossbowman_multiplayer_ai",
        "Swadian Crossbowman",
        "Swadian Crossbowmen",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_1,
        [
            itm_bolts,
            itm_crossbow,
            itm_sword_medieval_a,
            itm_tab_shield_heater_b,
            itm_leather_jerkin,
            itm_leather_armor,
        ],
        def_attrib | level(19),
        wp_melee(90) | wp_crossbow(100),
        knows_common
        | knows_ironflesh_4
        | knows_athletics_6
        | knows_shield_5
        | knows_power_strike_3,
        swadian_face_young_1,
        swadian_face_old_2,
    ],
    [
        "silver_rose_infantry_multiplayer_ai",
        "Swadian Infantry",
        "Swadian Infantry",
        tf_guarantee_all_wo_ranged,
        0,
        0,
        fac_kingdom_1,
        [
            itm_pike,
            itm_bastard_sword_a,
            itm_tab_shield_heater_c,
            itm_studded_leather_coat,
            itm_flat_top_b_v1,
        ],
        def_attrib | level(19),
        wp_melee(105),
        knows_common
        | knows_ironflesh_5
        | knows_shield_4
        | knows_power_strike_5
        | knows_athletics_4,
        swadian_face_middle_1,
        swadian_face_old_2,
    ],
    [
        "silver_rose_man_at_arms_multiplayer_ai",
        "Swadian Man at Arms",
        "Swadian Men at Arms",
        tf_mounted | tf_guarantee_all_wo_ranged,
        0,
        0,
        fac_kingdom_1,
        [
            itm_lance,
            itm_bastard_sword_a,
            itm_tab_shield_heater_cav_a,
            itm_hunter,
        ],
        def_attrib | level(19),
        wp_melee(100),
        knows_common
        | knows_riding_4
        | knows_ironflesh_4
        | knows_shield_4
        | knows_power_strike_4
        | knows_athletics_1,
        swadian_face_young_1,
        swadian_face_old_2,
    ],
    [
        "chornovalley_longbowman_multiplayer_ai",
        "Vaegir Archer",
        "Vaegir Archers",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_2,
        [
            itm_arrows,
            itm_scimitar,
            itm_nomad_bow,
            itm_leather_vest_regular_shirt_a,
            itm_cervelliere_a_v3,
        ],
        def_attrib | str_12 | level(19),
        wp_melee(70) | wp_archery(110),
        knows_ironflesh_4 | knows_power_draw_5 | knows_athletics_6 | knows_shield_2,
        vaegir_face_young_1,
        vaegir_face_older_2,
    ],
    [
        "vaegir_spearman_multiplayer_ai",
        "Vaegir Spearman",
        "Vaegir Spearmen",
        tf_guarantee_all_wo_ranged,
        0,
        0,
        fac_kingdom_2,
        [
            itm_padded_leather,
            itm_cervelliere_a_v3,
            itm_spear,
            itm_tab_shield_kite_b,
            itm_mace_1,
            itm_javelin,
        ],
        def_attrib | str_12 | level(19),
        wp_melee(90),
        knows_ironflesh_4
        | knows_athletics_6
        | knows_power_throw_3
        | knows_power_strike_3
        | knows_shield_2,
        vaegir_face_young_1,
        vaegir_face_older_2,
    ],
    [
        "chornovalley_horseman_multiplayer_ai",
        "Vaegir Horseman",
        "Vaegir Horsemen",
        tf_mounted | tf_guarantee_all_wo_ranged,
        0,
        0,
        fac_kingdom_2,
        [
            itm_battle_axe,
            itm_scimitar,
            itm_lance,
            itm_tab_shield_kite_cav_a,
            itm_studded_leather_coat,
            itm_lamellar_vest,
            itm_cervelliere_a_v3,
            itm_saddle_horse,
        ],
        def_attrib | level(19),
        wp(100),
        knows_riding_4 | knows_ironflesh_4 | knows_power_strike_4 | knows_shield_3,
        vaegir_face_young_1,
        vaegir_face_older_2,
    ],
    [
        "khergit_dismounted_lancer_multiplayer_ai",
        "Khergit Dismounted Lancer",
        "Khergit Dismounted Lancer",
        tf_guarantee_all_wo_ranged,
        0,
        0,
        fac_kingdom_3,
        [
            itm_sword_khergit_4,
            itm_spiked_mace,
            itm_one_handed_war_axe_b,
            itm_one_handed_war_axe_a,
            itm_hafted_blade_a,
            itm_hafted_blade_b,
            itm_heavy_lance,
            itm_lance,
            itm_khergit_cavalry_helmet,
            itm_khergit_war_helmet,
            itm_lamellar_vest_khergit,
            itm_tribal_warrior_outfit,
            itm_leather_gloves_a,
            itm_mail_mittens_a,
            itm_tab_shield_small_round_b,
            itm_tab_shield_small_round_c,
        ],
        def_attrib | level(19),
        wp(100),
        knows_riding_4
        | knows_power_strike_1
        | knows_power_draw_4
        | knows_power_throw_2
        | knows_ironflesh_1
        | knows_horse_archery_1,
        khergit_face_middle_1,
        khergit_face_older_2,
    ],
    [
        "celestial_sergeant_multiplayer_ai",
        "Khergit Horse Archer",
        "Khergit Horse Archers",
        tf_mounted | tf_guarantee_all,
        0,
        0,
        fac_kingdom_3,
        [
            itm_sword_khergit_3,
            itm_khergit_bow,
            itm_khergit_arrows,
            itm_tab_shield_small_round_b,
            itm_khergit_cavalry_helmet,
            itm_tribal_warrior_outfit,
            itm_steppe_horse,
        ],
        def_attrib | level(19),
        wp(90) | wp_archery(100),
        knows_riding_6 | knows_power_draw_5 | knows_shield_2 | knows_horse_archery_5,
        khergit_face_middle_1,
        khergit_face_older_2,
    ],
    [
        "celestial_lancer_multiplayer_ai",
        "Khergit Lancer",
        "Khergit Lancers",
        tf_guarantee_all_wo_ranged,
        0,
        0,
        fac_kingdom_3,
        [
            itm_sword_khergit_4,
            itm_spiked_mace,
            itm_one_handed_war_axe_b,
            itm_one_handed_war_axe_a,
            itm_hafted_blade_a,
            itm_hafted_blade_b,
            itm_heavy_lance,
            itm_lance,
            itm_khergit_guard_helmet,
            itm_khergit_cavalry_helmet,
            itm_khergit_war_helmet,
            itm_lamellar_vest_khergit,
            itm_leather_gloves_a,
            itm_mail_mittens_a,
            itm_tab_shield_small_round_b,
            itm_tab_shield_small_round_c,
            itm_courser,
        ],
        def_attrib | level(19),
        wp(100),
        knows_riding_7
        | knows_power_strike_2
        | knows_power_draw_4
        | knows_power_throw_2
        | knows_ironflesh_1
        | knows_horse_archery_1,
        khergit_face_middle_1,
        khergit_face_older_2,
    ],
    [
        "iron_crown_vetaran_multiplayer_ai",
        "Nord Footman",
        "Nord Footmen",
        tf_guarantee_all_wo_ranged,
        0,
        0,
        fac_kingdom_4,
        [
            itm_sword_viking_2,
            itm_one_handed_battle_axe_b,
            itm_two_handed_axe,
            itm_tab_shield_round_d,
            itm_throwing_axes,
            itm_mail_coif,
            itm_white_hauberk_a,
            itm_leather_gloves_a,
        ],
        def_attrib | level(19),
        wp(130),
        knows_ironflesh_3
        | knows_power_strike_5
        | knows_power_throw_3
        | knows_athletics_5
        | knows_shield_3,
        nord_face_young_1,
        nord_face_older_2,
    ],
    [
        "nord_scout_multiplayer_ai",
        "Nord Scout",
        "Nord Scouts",
        tf_mounted | tf_guarantee_all,
        0,
        0,
        fac_kingdom_4,
        [
            itm_javelin,
            itm_sword_viking_1,
            itm_two_handed_axe,
            itm_spear,
            itm_tab_shield_round_a,
            itm_cervelliere_a,
            itm_leather_jerkin,
            itm_saddle_horse,
        ],
        def_attrib | level(19),
        wp(100),
        knows_riding_5
        | knows_ironflesh_2
        | knows_power_strike_2
        | knows_shield_1
        | knows_horse_archery_2
        | knows_power_throw_3,
        nord_face_young_1,
        nord_face_older_2,
    ],
    [
        "iron_crown_trained_skirmisher_multiplayer_ai",
        "Nord Archer",
        "Nord Archers",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_4,
        [
            itm_arrows,
            itm_two_handed_axe,
            itm_sword_viking_2,
            itm_short_bow,
            itm_leather_jerkin,
            itm_blue_tunic,
            itm_eyeslot_kettlehat_a_v1,
            itm_arming_cap_a,
        ],
        def_attrib | str_11 | level(19),
        wp_melee(80) | wp_archery(110),
        knows_ironflesh_4
        | knows_power_strike_2
        | knows_shield_1
        | knows_power_draw_5
        | knows_athletics_6,
        nord_face_young_1,
        nord_face_old_2,
    ],
    [
        "alpine_veteran_crossbowman_multiplayer_ai",
        "Rhodok Crossbowman",
        "Rhodok Crossbowmen",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_5,
        [
            itm_fighting_pick,
            itm_club_with_spike_head,
            itm_maul,
            itm_tab_shield_pavise_c,
            itm_heavy_crossbow,
            itm_bolts,
            itm_arming_cap_a,
            itm_padded_leather,
        ],
        def_attrib | level(19),
        wp_melee(100) | wp_crossbow(120),
        knows_common
        | knows_ironflesh_4
        | knows_shield_5
        | knows_power_strike_3
        | knows_athletics_6,
        rhodok_face_middle_1,
        rhodok_face_older_2,
    ],
    [
        "alpine_veteran_spearman_multiplayer_ai",
        "Rhodok Spearman",
        "Rhodok Spearmen",
        tf_guarantee_all_wo_ranged,
        0,
        0,
        fac_kingdom_5,
        [
            itm_ashwood_pike,
            itm_war_spear,
            itm_pike,
            itm_club_with_spike_head,
            itm_sledgehammer,
            itm_tab_shield_pavise_c,
            itm_sword_medieval_a,
            itm_arming_cap_a,
            itm_gray_hauberk_a,
            itm_ragged_outfit,
        ],
        def_attrib | level(19),
        wp(115),
        knows_common
        | knows_ironflesh_5
        | knows_shield_3
        | knows_power_strike_4
        | knows_athletics_3,
        rhodok_face_young_1,
        rhodok_face_older_2,
    ],
    [
        "rhodok_scout_multiplayer_ai",
        "Rhodok Scout",
        "Rhodok Scouts",
        tf_mounted | tf_guarantee_all,
        0,
        0,
        fac_kingdom_5,
        # TODO: Change weapons, copied from Nord Scout
        [
            itm_sword_medieval_a,
            itm_tab_shield_heater_cav_a,
            itm_light_lance,
            itm_cervelliere_a,
            itm_aketon_green,
            itm_ragged_outfit,
            itm_saddle_horse,
        ],
        def_attrib | level(19),
        wp(100),
        knows_riding_5
        | knows_ironflesh_2
        | knows_power_strike_2
        | knows_shield_1
        | knows_horse_archery_2
        | knows_power_throw_3,
        rhodok_face_young_1,
        rhodok_face_older_2,
    ],
    [
        "solarian_infantry_multiplayer_ai",
        "Sarranid Infantry",
        "Sarranid Infantries",
        tf_guarantee_shield
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet,
        0,
        0,
        fac_kingdom_6,
        [
            itm_sword_b_v1,
            itm_mace_3,
            itm_spear,
            itm_tab_shield_kite_c,
        ],
        def_attrib | level(20),
        wp_melee(105),
        knows_common | knows_riding_3 | knows_ironflesh_2 | knows_shield_3,
        swadian_face_middle_1,
        swadian_face_old_2,
    ],
    [
        "solarian_archer_multiplayer_ai",
        "Sarranid Archer",
        "Sarranid Archers",
        tf_guarantee_ranged | tf_guarantee_boots | tf_guarantee_armor,
        0,
        0,
        fac_kingdom_6,
        [
            itm_arrows,
            itm_nomad_bow,
            itm_sword_b,
        ],
        def_attrib | level(19),
        wp_melee(90) | wp_archery(100),
        knows_common | knows_riding_2 | knows_ironflesh_1,
        swadian_face_young_1,
        swadian_face_old_2,
    ],
    [
        "solarian_horseman_multiplayer_ai",
        "Sarranid Horseman",
        "Sarranid Horsemen",
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
            itm_lance,
            itm_sword_b_v1,
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
    # Multiplayer troops (they must have the base items only, nothing else)
    [
        "silver_rose_trained_crossbowman_multiplayer",
        "Swadian Crossbowman",
        "Swadian Crossbowmen",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_1,
        [
            itm_bolts,
            itm_crossbow,
            itm_sword_medieval_b_small,
            itm_tab_shield_heater_a,
            itm_red_shirt_a,
        ],
        str_14 | agi_15 | def_attrib_multiplayer | level(19),
        wpe(90, 60, 180, 90),
        knows_common_multiplayer
        | knows_ironflesh_2
        | knows_athletics_4
        | knows_shield_5
        | knows_power_strike_2
        | knows_riding_1,
        swadian_face_young_1,
        swadian_face_old_2,
    ],
    [
        "silver_rose_infantry_multiplayer",
        "Swadian Infantry",
        "Swadian Infantry",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_1,
        [itm_sword_medieval_a, itm_tab_shield_heater_a, itm_red_tunic],
        str_15 | agi_15 | def_attrib_multiplayer | level(20),
        wpex(105, 130, 110, 40, 60, 110),
        knows_common_multiplayer
        | knows_ironflesh_5
        | knows_shield_4
        | knows_power_strike_4
        | knows_power_throw_2
        | knows_athletics_6
        | knows_riding_1,
        swadian_face_middle_1,
        swadian_face_old_2,
    ],
    [
        "silver_rose_man_at_arms_multiplayer",
        "Swadian Man at Arms",
        "Swadian Men at Arms",
        tf_mounted | tf_guarantee_all,
        0,
        0,
        fac_kingdom_1,
        [
            itm_lance,
            itm_sword_medieval_a,
            itm_tab_shield_heater_a,
            itm_red_tunic,
            itm_saddle_horse,
        ],
        str_14 | agi_16 | def_attrib_multiplayer | level(20),
        wp_melee(110),
        knows_common_multiplayer
        | knows_riding_5
        | knows_ironflesh_3
        | knows_shield_2
        | knows_power_throw_2
        | knows_power_strike_3
        | knows_athletics_3,
        swadian_face_young_1,
        swadian_face_old_2,
    ],
    #  ["swadian_mounted_crossbowman_multiplayer","Swadian Mounted Crossbowman","Swadian Mounted Crossbowmen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_1,
    #   [itm_bolts,itm_light_crossbow,itm_tab_shield_heater_cav_a,itm_bastard_sword_a,
    #    itm_red_shirt_a,itm_saddle_horse],
    #   def_attrib_multiplayer|level(20),wp_melee(100)|wp_crossbow(120),knows_common_multiplayer|knows_riding_4|knows_shield_3|knows_ironflesh_3|knows_horse_archery_2|knows_power_strike_3|knows_athletics_2|knows_shield_2,swadian_face_young_1, swadian_face_old_2],
    [
        "chornovalley_longbowman_multiplayer",
        "Vaegir Archer",
        "Vaegir Archers",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_2,
        [itm_arrows, itm_mace_1, itm_nomad_bow, itm_regular_shirt_b],
        str_14 | agi_14 | def_attrib_multiplayer | str_12 | level(19),
        wpe(80, 150, 60, 80),
        knows_common_multiplayer
        | knows_ironflesh_2
        | knows_power_draw_7
        | knows_athletics_3
        | knows_shield_2
        | knows_riding_1,
        vaegir_face_young_1,
        vaegir_face_older_2,
    ],
    [
        "vaegir_spearman_multiplayer",
        "Vaegir Spearman",
        "Vaegir spearman",
        tf_guarantee_ranged
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet
        | tf_guarantee_ranged
        | tf_guarantee_shield,
        0,
        0,
        fac_kingdom_2,
        [itm_spear, itm_tab_shield_kite_a, itm_mace_1, itm_regular_shirt_b],
        str_15 | agi_15 | def_attrib_multiplayer | str_12 | level(19),
        wpex(110, 100, 130, 30, 50, 120),
        knows_common_multiplayer
        | knows_ironflesh_4
        | knows_shield_2
        | knows_power_throw_3
        | knows_power_strike_4
        | knows_athletics_6
        | knows_riding_1,
        vaegir_face_young_1,
        vaegir_face_older_2,
    ],
    [
        "chornovalley_horseman_multiplayer",
        "Vaegir Horseman",
        "Vaegir Horsemen",
        tf_mounted | tf_guarantee_all,
        0,
        0,
        fac_kingdom_2,
        [
            itm_scimitar,
            itm_lance,
            itm_tab_shield_kite_cav_a,
            itm_regular_shirt_b,
            itm_saddle_horse,
        ],
        str_16 | agi_15 | def_attrib_multiplayer | level(19),
        wpe(110, 90, 60, 110),
        knows_common_multiplayer
        | knows_riding_5
        | knows_ironflesh_4
        | knows_power_strike_3
        | knows_shield_3
        | knows_power_throw_4
        | knows_horse_archery_1,
        vaegir_face_young_1,
        vaegir_face_older_2,
    ],
    [
        "celestial_sergeant_multiplayer",
        "Khergit Horse Archer",
        "Khergit Horse Archers",
        tf_mounted | tf_guarantee_all,
        0,
        0,
        fac_kingdom_3,
        [
            itm_sword_khergit_1,
            itm_nomad_bow,
            itm_arrows,
            itm_khergit_armor,
            itm_leather_steppe_cap_a,
            itm_steppe_horse,
        ],
        str_15 | agi_18 | def_attrib_multiplayer | level(21),
        wpe(70, 142, 60, 100),
        knows_common_multiplayer
        | knows_riding_2
        | knows_power_draw_5
        | knows_horse_archery_3
        | knows_athletics_3
        | knows_shield_1,
        khergit_face_middle_1,
        khergit_face_older_2,
    ],
    [
        "khergit_infantry_multiplayer",
        "Khergit Infantry",
        "Khergit Infantries",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_3,
        [
            itm_sword_khergit_1,
            itm_spear,
            itm_tab_shield_small_round_a,
            itm_steppe_armor,
            itm_leather_gloves_a,
        ],
        str_14 | agi_15 | def_attrib_multiplayer | level(19),
        wp(110),
        knows_common_multiplayer
        | knows_ironflesh_3
        | knows_power_throw_3
        | knows_shield_4
        | knows_power_strike_3
        | knows_athletics_6
        | knows_riding_1,
        khergit_face_middle_1,
        khergit_face_older_2,
    ],
    [
        "celestial_lancer_multiplayer",
        "Khergit Lancer",
        "Khergit Lancers",
        tf_mounted | tf_guarantee_all,
        0,
        0,
        fac_kingdom_3,
        [
            itm_sword_khergit_1,
            itm_lance,
            itm_tab_shield_small_round_a,
            itm_khergit_armor,
            itm_leather_steppe_cap_a,
            itm_steppe_horse,
        ],
        str_15 | agi_14 | def_attrib_multiplayer | level(21),
        wp(115),
        knows_common_multiplayer
        | knows_riding_6
        | knows_ironflesh_3
        | knows_power_throw_3
        | knows_shield_4
        | knows_power_strike_3
        | knows_athletics_4,
        khergit_face_middle_1,
        khergit_face_older_2,
    ],
    [
        "iron_crown_trained_skirmisher_multiplayer",
        "Nord Archer",
        "Nord Archers",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_4,
        [itm_arrows, itm_sword_viking_2_small, itm_short_bow, itm_blue_tunic],
        str_15 | agi_14 | def_attrib_multiplayer | str_11 | level(15),
        wpe(90, 150, 60, 80),
        knows_common_multiplayer
        | knows_ironflesh_2
        | knows_power_strike_2
        | knows_shield_3
        | knows_power_draw_5
        | knows_athletics_3
        | knows_riding_1,
        nord_face_young_1,
        nord_face_old_2,
    ],
    [
        "iron_crown_vetaran_multiplayer",
        "Nord Huscarl",
        "Nord Huscarls",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_4,
        [
            itm_sword_viking_1,
            itm_one_handed_war_axe_a,
            itm_tab_shield_round_a,
            itm_blue_tunic,
        ],
        str_17 | agi_15 | def_attrib_multiplayer | level(24),
        wpex(110, 135, 100, 40, 60, 140),
        knows_common_multiplayer
        | knows_ironflesh_4
        | knows_power_strike_5
        | knows_power_throw_4
        | knows_athletics_6
        | knows_shield_3
        | knows_riding_1,
        nord_face_young_1,
        nord_face_older_2,
    ],
    [
        "nord_scout_multiplayer",
        "Nord Scout",
        "Nord Scouts",
        tf_mounted | tf_guarantee_all,
        0,
        0,
        fac_kingdom_4,
        [
            itm_javelin,
            itm_sword_viking_1,
            itm_spear,
            itm_tab_shield_small_round_a,
            itm_blue_tunic,
            itm_saddle_horse,
        ],
        str_16 | agi_15 | def_attrib_multiplayer | level(19),
        wp(105),
        knows_common_multiplayer
        | knows_riding_6
        | knows_ironflesh_2
        | knows_power_strike_2
        | knows_shield_1
        | knows_horse_archery_3
        | knows_power_throw_3
        | knows_athletics_3,
        vaegir_face_young_1,
        vaegir_face_older_2,
    ],
    [
        "alpine_veteran_crossbowman_multiplayer",
        "Rhodok Crossbowman",
        "Rhodok Crossbowmen",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_5,
        [
            itm_crossbow,
            itm_bolts,
            itm_fighting_pick,
            itm_tab_shield_pavise_a,
            itm_peasant_regular_shirt_a,
        ],
        str_16 | agi_15 | def_attrib_multiplayer | level(20),
        wpe(100, 60, 180, 90),
        knows_common_multiplayer
        | knows_ironflesh_2
        | knows_shield_2
        | knows_power_strike_2
        | knows_athletics_4
        | knows_riding_1,
        rhodok_face_middle_1,
        rhodok_face_older_2,
    ],
    [
        "alpine_man_at_arms_multiplayer",
        "Rhodok Sergeant",
        "Rhodok Sergeants",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_5,
        [itm_fighting_pick, itm_tab_shield_pavise_a, itm_spear, itm_green_tunic],
        str_16 | agi_14 | def_attrib_multiplayer | level(20),
        wpex(110, 100, 140, 30, 50, 110),
        knows_common_multiplayer
        | knows_ironflesh_4
        | knows_shield_5
        | knows_power_strike_4
        | knows_power_throw_1
        | knows_athletics_6
        | knows_riding_1,
        rhodok_face_middle_1,
        rhodok_face_older_2,
    ],
    [
        "rhodok_horseman_multiplayer",
        "Rhodok Horseman",
        "Rhodok Horsemen",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_5,
        [
            itm_sword_medieval_a,
            itm_tab_shield_heater_cav_a,
            itm_light_lance,
            itm_green_tunic,
            itm_saddle_horse,
        ],
        str_15 | agi_15 | def_attrib_multiplayer | level(20),
        wp(100),
        knows_common_multiplayer
        | knows_riding_4
        | knows_ironflesh_3
        | knows_shield_3
        | knows_power_strike_3
        | knows_power_throw_1
        | knows_athletics_3,
        rhodok_face_middle_1,
        rhodok_face_older_2,
    ],
    [
        "solarian_archer_multiplayer",
        "Sarranid Archer",
        "Sarranid Archers",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_6,
        [],
        str_15 | agi_16 | def_attrib_multiplayer | str_12 | level(19),
        wpe(80, 150, 60, 80),
        knows_common_multiplayer
        | knows_ironflesh_4
        | knows_power_draw_5
        | knows_athletics_3
        | knows_shield_2
        | knows_riding_1
        | knows_weapon_master_1,
        vaegir_face_young_1,
        vaegir_face_older_2,
    ],
    [
        "solarian_footman_multiplayer",
        "Sarranid Footman",
        "Sarranid footman",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_6,
        [
            itm_bamboo_spear,
            itm_tab_shield_kite_a,
            itm_sword_b,
        ],
        str_14 | agi_15 | def_attrib_multiplayer | str_12 | level(19),
        wpex(110, 100, 130, 30, 50, 120),
        knows_common_multiplayer
        | knows_ironflesh_4
        | knows_shield_2
        | knows_power_throw_3
        | knows_power_strike_4
        | knows_athletics_6
        | knows_riding_1,
        vaegir_face_young_1,
        vaegir_face_older_2,
    ],
    [
        "solarian_knight_multiplayer",
        "Sarranid Mamluke",
        "Sarranid Mamluke",
        tf_mounted | tf_guarantee_all,
        0,
        0,
        fac_kingdom_6,
        [
            itm_sword_b,
            itm_lance,
            itm_tab_shield_small_round_a,
            itm_saddle_horse,
        ],
        str_15 | agi_14 | def_attrib_multiplayer | level(19),
        wpe(110, 90, 60, 110),
        knows_common_multiplayer
        | knows_riding_5
        | knows_ironflesh_3
        | knows_power_strike_2
        | knows_shield_3
        | knows_power_throw_2
        | knows_weapon_master_1,
        vaegir_face_young_1,
        vaegir_face_older_2,
    ],
    [
        "multiplayer_end",
        "{!}multiplayer_end",
        "{!}multiplayer_end",
        0,
        0,
        0,
        fac_kingdom_5,
        [],
        0,
        0,
        0,
        0,
        0,
    ],
    # Player history array
    [
        "log_array_entry_type",
        "{!}Local Merchant",
        "{!}Local Merchant",
        tf_guarantee_boots | tf_guarantee_armor,
        0,
        0,
        fac_commoners,
        [itm_peasant_regular_shirt_a_v1, itm_butchering_knife],
        def_attrib | level(5),
        wp(40),
        knows_power_strike_1,
        merchant_face_1,
        merchant_face_2,
    ],
    [
        "log_array_entry_time",
        "{!}Local Merchant",
        "{!}Local Merchant",
        tf_guarantee_boots | tf_guarantee_armor,
        0,
        0,
        fac_commoners,
        [itm_peasant_regular_shirt_a_v1, itm_butchering_knife],
        def_attrib | level(5),
        wp(40),
        knows_power_strike_1,
        merchant_face_1,
        merchant_face_2,
    ],
    [
        "log_array_actor",
        "{!}Local Merchant",
        "{!}Local Merchant",
        tf_guarantee_boots | tf_guarantee_armor,
        0,
        0,
        fac_commoners,
        [itm_peasant_regular_shirt_a_v1, itm_butchering_knife],
        def_attrib | level(5),
        wp(40),
        knows_power_strike_1,
        merchant_face_1,
        merchant_face_2,
    ],
    [
        "log_array_center_object",
        "{!}Local Merchant",
        "{!}Local Merchant",
        tf_guarantee_boots | tf_guarantee_armor,
        0,
        0,
        fac_commoners,
        [itm_peasant_regular_shirt_a_v1, itm_butchering_knife],
        def_attrib | level(5),
        wp(40),
        knows_power_strike_1,
        merchant_face_1,
        merchant_face_2,
    ],
    [
        "log_array_center_object_lord",
        "{!}Local Merchant",
        "{!}Local Merchant",
        tf_guarantee_boots | tf_guarantee_armor,
        0,
        0,
        fac_commoners,
        [itm_peasant_regular_shirt_a_v1, itm_butchering_knife],
        def_attrib | level(5),
        wp(40),
        knows_power_strike_1,
        merchant_face_1,
        merchant_face_2,
    ],
    [
        "log_array_center_object_faction",
        "{!}Local Merchant",
        "{!}Local Merchant",
        tf_guarantee_boots | tf_guarantee_armor,
        0,
        0,
        fac_commoners,
        [itm_peasant_regular_shirt_a_v1, itm_butchering_knife],
        def_attrib | level(5),
        wp(40),
        knows_power_strike_1,
        merchant_face_1,
        merchant_face_2,
    ],
    [
        "log_array_troop_object",
        "{!}Local Merchant",
        "{!}Local Merchant",
        tf_guarantee_boots | tf_guarantee_armor,
        0,
        0,
        fac_commoners,
        [itm_peasant_regular_shirt_a_v1, itm_butchering_knife],
        def_attrib | level(5),
        wp(40),
        knows_power_strike_1,
        merchant_face_1,
        merchant_face_2,
    ],
    [
        "log_array_troop_object_faction",
        "{!}Local Merchant",
        "{!}Local Merchant",
        tf_guarantee_boots | tf_guarantee_armor,
        0,
        0,
        fac_commoners,
        [itm_peasant_regular_shirt_a_v1, itm_butchering_knife],
        def_attrib | level(5),
        wp(40),
        knows_power_strike_1,
        merchant_face_1,
        merchant_face_2,
    ],
    [
        "log_array_faction_object",
        "{!}Local Merchant",
        "{!}Local Merchant",
        tf_guarantee_boots | tf_guarantee_armor,
        0,
        0,
        fac_commoners,
        [itm_peasant_regular_shirt_a_v1, itm_butchering_knife],
        def_attrib | level(5),
        wp(40),
        knows_power_strike_1,
        merchant_face_1,
        merchant_face_2,
    ],
    [
        "quick_battle_troop_1",
        "Sir Artorio of Nerpa",
        "Sir Artorio of Nerpa",
        tf_hero,
        0,
        0,
        fac_kingdom_1,
        [
            itm_plate_gauntlets_a_v1,
            itm_tab_shield_pavise_d,
            itm_throwing_spears,
        ],
        str_30 | agi_30 | int_12 | cha_12 | level(55),
        wpex(400, 300, 500, 200, 200, 350),
        knows_athletics_10
        | knows_shield_7
        | knows_weapon_master_7
        | knows_power_throw_8
        | knows_power_strike_9
        | knows_ironflesh_10,
        0x0000000E7F10400836DB6DB6DB6DDBB600000000001DB6DB0000000000000000,
        swadian_face_old_2,
    ],
    [
        "quick_battle_troop_2",
        "Borato",
        "Borato",
        tf_hero,
        0,
        0,
        fac_kingdom_1,
        [
            itm_leather_gloves_a_v1,
            itm_tab_shield_heater_d,
            itm_sniper_crossbow,
            itm_steel_bolts,
        ],
        str_30 | agi_30 | int_11 | cha_18 | level(54),
        wpex(400, 100, 200, 450, 100, 100),
        knows_athletics_10
        | knows_shield_10
        | knows_weapon_master_10
        | knows_power_strike_8
        | knows_ironflesh_8,
        0x000000097F1065C636DB6DB6DB6DDBB600000000001DB6DB0000000000000000,
        swadian_face_old_2,
    ],
    [
        "quick_battle_troop_3",
        "Francisco",
        "Francisco",
        tf_hero,
        0,
        0,
        fac_kingdom_1,
        [
            itm_regular_shirt_a,
            itm_plate_gauntlets_a_v1,
            itm_tab_shield_heater_cav_b,
            itm_heavy_lance,
            itm_mt_horse_c2,
        ],
        str_30 | agi_30 | int_11 | cha_18 | level(54),
        wpex(400, 400, 400, 100, 100, 100),
        knows_athletics_10
        | knows_shield_10
        | knows_riding_10
        | knows_weapon_master_10
        | knows_power_strike_8
        | knows_ironflesh_8,
        0x000000000010014536DB6DB6DB6DDBB600000000001DB6DB0000000000000000,
        swadian_face_old_2,
    ],
    [
        "quick_battle_troop_4",
        "Elindero the Tower",
        "Elindero the Tower",
        tf_hero,
        0,
        0,
        fac_kingdom_1,
        [
            itm_regular_shirt_a,
            itm_plate_gauntlets_a_v1,
            itm_steel_shield,
            itm_mt_horse_c2,
        ],
        str_30 | agi_30 | int_11 | cha_18 | level(54),
        wpex(400, 200, 450, 100, 100, 100),
        knows_athletics_10
        | knows_shield_10
        | knows_weapon_master_10
        | knows_power_strike_8
        | knows_ironflesh_8,
        0x0000000F3F10219436DB6DB6DB6DDBB600000000001DB6DB0000000000000000,
        swadian_face_old_2,
    ],
    [
        "quick_battle_troop_5",
        "Sir Skolle",
        "Sir Skolle",
        tf_hero,
        0,
        0,
        fac_kingdom_1,
        [itm_regular_shirt_a, itm_plate_gauntlets_a, itm_plate_covered_round_shield],
        str_30 | agi_30 | int_11 | cha_18 | level(54),
        wpex(600, 200, 200, 100, 100, 100),
        knows_athletics_10
        | knows_shield_10
        | knows_weapon_master_10
        | knows_power_strike_8
        | knows_ironflesh_8,
        0x0000000FFF10321336DB6DB6DB6DDBB600000000001DB6DB0000000000000000,
        swadian_face_old_2,
    ],
    [
        "quick_battle_troop_6",
        "Xan",
        "Xan",
        tf_hero,
        0,
        0,
        fac_kingdom_1,
        [
            itm_steppe_horse,
            itm_strong_bow,
            itm_barbed_arrows,
            itm_plate_covered_round_shield,
        ],
        str_30 | agi_30 | int_11 | cha_18 | level(54),
        wpex(450, 200, 200, 450, 100, 100),
        knows_athletics_6
        | knows_shield_10
        | knows_weapon_master_10
        | knows_power_strike_8
        | knows_ironflesh_8
        | knows_riding_10,
        0x0000000FFF08338536DB6DB6DB6DDB6D00000000001DB6DB0000000000000000,
        swadian_face_old_2,
    ],
    [
        "quick_battle_troop_7",
        "Gylas",
        "Gylas",
        tf_hero,
        0,
        0,
        fac_kingdom_1,
        [
            itm_leather_gloves_a_v1,
            itm_war_bow,
            itm_bodkin_arrows,
            itm_bodkin_arrows,
        ],
        str_30 | agi_30 | int_11 | cha_18 | level(54),
        wpex(240, 200, 200, 500, 100, 100),
        knows_athletics_6
        | knows_shield_5
        | knows_weapon_master_10
        | knows_power_strike_8
        | knows_ironflesh_8
        | knows_power_draw_10,
        0x0000000FFF08338536DB6DB6DB6DDB6D00000000001DB6DB0000000000000000,
        swadian_face_old_2,
    ],
    [
        "quick_battle_troop_8",
        "Hamart Boley",
        "Hamart Boley",
        tf_hero,
        0,
        0,
        fac_kingdom_1,
        [
            itm_leather_gloves_a_v1,
            itm_war_bow,
            itm_barbed_arrows,
        ],
        str_30 | agi_30 | int_11 | cha_18 | level(54),
        wpex(240, 200, 200, 500, 100, 100),
        knows_athletics_10
        | knows_shield_5
        | knows_weapon_master_10
        | knows_power_strike_8
        | knows_ironflesh_8
        | knows_power_draw_10,
        0x00000006FF00219436DB6DB6DB6DFF6500000000001DB6DB0000000000000000,
        swadian_face_old_2,
    ],
    [
        "quick_battle_troop_9",
        "Eward",
        "Eward",
        tf_hero,
        0,
        0,
        fac_kingdom_1,
        [itm_heavy_throwing_axes, itm_tab_shield_round_e],
        str_30 | agi_30 | int_11 | cha_18 | level(56),
        wpex(240, 500, 100, 100, 100, 400),
        knows_athletics_10
        | knows_shield_5
        | knows_weapon_master_10
        | knows_power_strike_10
        | knows_ironflesh_10,
        0x0000000FF108330906DB6DB6DB6DDB6C00000000001DB6F80000000000000000,
        swadian_face_old_2,
    ],
    [
        "quick_battle_troop_10",
        "Axlerd Githal",
        "Axlerd Githal",
        tf_hero,
        0,
        0,
        fac_kingdom_1,
        [],
        str_30 | agi_30 | int_11 | cha_18 | level(56),
        wpex(500, 500, 100, 100, 100, 100),
        knows_athletics_10
        | knows_shield_5
        | knows_weapon_master_10
        | knows_power_strike_10
        | knows_ironflesh_10,
        0x0000000FFF08434906076C3A1B1DFFFF00000000001DB6380000000000000000,
        swadian_face_old_2,
    ],
    [
        "quick_battle_troop_11",
        "Ezzenmer",
        "Ezzenmer",
        tf_hero,
        0,
        0,
        fac_kingdom_1,
        [],
        str_30 | agi_30 | int_11 | cha_18 | level(69),
        wpex(0, 900, 0, 0, 0, 0),
        knows_athletics_10
        | knows_weapon_master_10
        | knows_power_strike_10
        | knows_ironflesh_10,
        0x0000000FFF08738006056C3A1B1DFFFF00000000001DB6380000000000000000,
        swadian_face_old_2,
    ],
    [
        "quick_battle_troop_12",
        "Bronze Ganaka",
        "Bronze Ganaka",
        tf_hero,
        0,
        0,
        fac_kingdom_1,
        [itm_battle_fork, itm_leather_gloves_a_v1],
        str_30 | agi_30 | int_11 | cha_18 | level(54),
        wpex(0, 0, 900, 0, 0, 0),
        knows_athletics_10
        | knows_weapon_master_10
        | knows_power_strike_10
        | knows_ironflesh_10,
        0x0000000E7F08244036DB6DB6DB6EDD6D00000000001DB6F30000000000000000,
        swadian_face_old_2,
    ],
    [
        "quick_battle_troops_end",
        "{!}quick_battle_troops_end",
        "{!}quick_battle_troops_end",
        0,
        0,
        0,
        fac_kingdom_5,
        [],
        0,
        0,
        0,
        0,
        0,
    ],
    [
        "tutorial_fighter_1",
        "Novice Fighter",
        "Fighters",
        tf_hero,
        0,
        0,
        fac_kingdom_2,
        [itm_regular_shirt_b],
        def_attrib | level(1),
        wp_melee(10),
        knows_athletics_1 | knows_ironflesh_2 | knows_shield_2,
        0x000000088C1073144252B1929A85569300000000000496A50000000000000000,
        vaegir_face_older_2,
    ],
    [
        "tutorial_fighter_2",
        "Novice Fighter",
        "Fighters",
        tf_hero,
        0,
        0,
        fac_kingdom_2,
        [itm_green_tunic],
        def_attrib | level(1),
        wp_melee(10),
        knows_athletics_1 | knows_ironflesh_2 | knows_shield_2,
        0x000000088B08049056AB56566135C46500000000001DDA1B0000000000000000,
        vaegir_face_older_2,
    ],
    [
        "tutorial_fighter_3",
        "Regular Fighter",
        "Fighters",
        tf_hero,
        0,
        0,
        fac_kingdom_2,
        [itm_green_tunic],
        def_attrib | level(9),
        wp_melee(50),
        knows_athletics_1 | knows_ironflesh_2 | knows_shield_2,
        0x00000008BC00400654914A3B0D0DE74D00000000001D584E0000000000000000,
        vaegir_face_older_2,
    ],
    [
        "tutorial_fighter_4",
        "Veteran Fighter",
        "Fighters",
        tf_hero,
        0,
        0,
        fac_kingdom_2,
        [itm_regular_shirt_b],
        def_attrib | level(16),
        wp_melee(110),
        knows_athletics_1 | knows_ironflesh_3 | knows_power_strike_2 | knows_shield_2,
        0x000000089910324A495175324949671800000000001CD8AB0000000000000000,
        vaegir_face_older_2,
    ],
    [
        "tutorial_archer_1",
        "Archer",
        "Archers",
        tf_guarantee_ranged | tf_guarantee_boots | tf_guarantee_armor,
        0,
        0,
        fac_kingdom_2,
        [
            itm_leather_jerkin,
            itm_leather_vest_regular_shirt_a,
        ],
        def_attrib | str_12 | level(19),
        wp_melee(70) | wp_archery(110),
        knows_ironflesh_1
        | knows_power_draw_2
        | knows_athletics_2
        | knows_power_throw_1,
        vaegir_face_young_1,
        vaegir_face_older_2,
    ],
    [
        "tutorial_master_archer",
        "Archery Trainer",
        "Archery Trainer",
        tf_hero,
        0,
        0,
        fac_kingdom_2,
        [itm_regular_shirt_b],
        def_attrib | str_12 | level(19),
        wp_melee(70) | wp_archery(110),
        knows_ironflesh_1
        | knows_power_draw_2
        | knows_athletics_2
        | knows_power_throw_1,
        0x0000000EA508540642F34D461D2D54A300000000001D5D9A0000000000000000,
        vaegir_face_older_2,
    ],
    [
        "tutorial_rider_1",
        "Rider",
        "{!}Vaegir Knights",
        tf_mounted
        | tf_guarantee_boots
        | tf_guarantee_gloves
        | tf_guarantee_armor
        | tf_guarantee_helmet
        | tf_guarantee_horse
        | tf_guarantee_shield,
        0,
        0,
        fac_kingdom_2,
        [itm_green_tunic, itm_hunter, itm_saddle_horse, itm_leather_gloves_a],
        def_attrib | level(24),
        wp(130),
        knows_riding_4 | knows_shield_2 | knows_ironflesh_3 | knows_power_strike_2,
        vaegir_face_middle_1,
        vaegir_face_older_2,
    ],
    [
        "tutorial_rider_2",
        "Horse archer",
        "{!}Khergit Horse Archers",
        tf_mounted
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_ranged
        | tf_guarantee_horse,
        0,
        0,
        fac_kingdom_3,
        [
            itm_tribal_warrior_outfit,
            itm_nomad_robe,
            itm_tab_shield_small_round_a,
            itm_steppe_horse,
        ],
        def_attrib | level(14),
        wp(80) | wp_archery(110),
        knows_riding_5
        | knows_power_draw_3
        | knows_ironflesh_1
        | knows_horse_archery_4
        | knows_power_throw_1,
        khergit_face_young_1,
        khergit_face_older_2,
    ],
    [
        "tutorial_master_horseman",
        "Riding Trainer",
        "Riding Trainer",
        tf_hero,
        0,
        0,
        fac_kingdom_2,
        [itm_leather_vest_regular_shirt_a],
        def_attrib | str_12 | level(19),
        wp_melee(70) | wp_archery(110),
        knows_ironflesh_1
        | knows_power_draw_2
        | knows_athletics_2
        | knows_power_throw_1,
        0x0000000EA0084140478A692894BA185500000000001D4AF30000000000000000,
        vaegir_face_older_2,
    ],
    [
        "swadian_merchant",
        "Merchant of Praven",
        "{!}Prominent",
        tf_hero | tf_randomize_face,
        0,
        reserved,
        fac_kingdom_4,
        [itm_sword_great_a, itm_tabard_e],
        def_attrib | level(2),
        wp(20),
        knows_common,
        man_face_middle_1,
        mercenary_face_2,
    ],
    [
        "vaegir_merchant",
        "Merchant of Reyvadin",
        "{!}Prominent",
        tf_hero | tf_randomize_face,
        0,
        reserved,
        fac_kingdom_5,
        [itm_sword_great_a, itm_tabard_f],
        def_attrib | level(2),
        wp(20),
        knows_common,
        man_face_middle_1,
        mercenary_face_2,
    ],
    [
        "khergit_merchant",
        "Merchant of Tulga",
        "{!}Prominent",
        tf_hero | tf_randomize_face,
        0,
        reserved,
        fac_kingdom_1,
        [itm_sword_great_a, itm_red_gambeson],
        def_attrib | level(2),
        wp(20),
        knows_common,
        man_face_middle_1,
        mercenary_face_2,
    ],
    [
        "nord_merchant",
        "Merchant of Sargoth",
        "{!}Prominent",
        tf_hero | tf_randomize_face,
        0,
        reserved,
        fac_kingdom_2,
        [itm_sword_great_a, itm_red_gambeson],
        def_attrib | level(2),
        wp(20),
        knows_common,
        man_face_middle_1,
        mercenary_face_2,
    ],
    [
        "rhodok_merchant",
        "Merchant of Jelkala",
        "{!}Prominent",
        tf_hero | tf_randomize_face,
        0,
        reserved,
        fac_kingdom_3,
        [itm_sword_great_a, itm_leather_jerkin],
        def_attrib | level(2),
        wp(20),
        knows_common,
        man_face_middle_1,
        mercenary_face_2,
    ],
    [
        "sarranid_merchant",
        "Merchant of Shariz",
        "{!}Prominent",
        tf_hero | tf_randomize_face,
        0,
        reserved,
        fac_kingdom_6,
        [],
        def_attrib | level(2),
        wp(20),
        knows_common,
        man_face_middle_1,
        mercenary_face_2,
    ],
    [
        "startup_merchants_end",
        "startup_merchants_end",
        "startup_merchants_end",
        tf_hero,
        0,
        0,
        fac_commoners,
        [],
        def_attrib | level(2),
        wp(20),
        knows_inventory_management_10,
        0,
    ],
    [
        "sea_raider_leader",
        "Sea Raider Captain",
        "Sea Raider Captains",
        tf_hero | tf_guarantee_all_wo_ranged,
        0,
        0,
        fac_outlaws,
        [
            itm_arrows,
            itm_sword_viking_1,
            itm_sword_viking_2,
            itm_fighting_axe,
            itm_battle_axe,
            itm_spear,
            itm_nordic_shield,
            itm_nordic_shield,
            itm_nordic_shield,
            itm_wooden_shield,
            itm_long_bow,
            itm_javelin,
            itm_throwing_axes,
            itm_mail_coif,
            itm_mail_coif,
            itm_eyeslot_kettlehat_a_v1,
            itm_gray_hauberk_a,
            itm_white_hauberk_a,
        ],
        def_attrib | level(24),
        wp(110),
        knows_ironflesh_2
        | knows_power_strike_2
        | knows_power_draw_3
        | knows_power_throw_2
        | knows_riding_1
        | knows_athletics_2,
        nord_face_young_1,
        nord_face_old_2,
    ],
    [
        "looter_leader",
        "Robber",
        "Looters",
        tf_hero,
        0,
        0,
        fac_outlaws,
        [
            itm_hatchet_b,
            itm_club,
            itm_butchering_knife,
            itm_falchion_a,
            itm_rawhide_coat,
            itm_stones,
            itm_nomad_armor,
            itm_nomad_armor,
            itm_woolen_cap,
            itm_woolen_cap,
        ],
        def_attrib | level(4),
        wp(20),
        knows_common,
        0x00000001B80032473AC49738206626B200000000001DA7660000000000000000,
        bandit_face2,
    ],
    [
        "bandit_leaders_end",
        "bandit_leaders_end",
        "bandit_leaders_end",
        tf_hero,
        0,
        0,
        fac_commoners,
        [],
        def_attrib | level(2),
        wp(20),
        knows_inventory_management_10,
        0,
    ],
    [
        "relative_of_merchant",
        "Merchant's Brother",
        "{!}Prominent",
        tf_hero,
        0,
        0,
        fac_kingdom_2,
        [itm_regular_shirt_b],
        def_attrib | level(1),
        wp_melee(10),
        knows_athletics_1 | knows_ironflesh_2 | knows_shield_2,
        0x00000000320410022D2595495491AFA400000000001D9AE30000000000000000,
        mercenary_face_2,
    ],
    [
        "relative_of_merchants_end",
        "relative_of_merchants_end",
        "relative_of_merchants_end",
        tf_hero,
        0,
        0,
        fac_commoners,
        [],
        def_attrib | level(2),
        wp(20),
        knows_inventory_management_10,
        0,
    ],
    [
        "silver_rose_trained_crossbowman_multiplayer_coop_tier_1",
        "Swadian Crossbowman",
        "Swadian Crossbowmen",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_1,
        [
            itm_hunting_crossbow,
            itm_bolts,
            itm_fighting_pick,
            itm_tab_shield_heater_a,
            itm_arming_cap_a,
            itm_padded_cloth,
        ],
        level(4) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "silver_rose_infantry_multiplayer_coop_tier_1",
        "Swadian Infantry",
        "Swadian Infantry",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_1,
        [itm_spiked_club, itm_tab_shield_heater_b, itm_felt_a, itm_peasant_regular_shirt_a_v1],
        level(4) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "silver_rose_man_at_arms_multiplayer_coop_tier_1",
        "Swadian Man at Arms",
        "Swadian Men at Arms",
        tf_mounted | tf_guarantee_all,
        0,
        0,
        fac_kingdom_1,
        [
            itm_light_lance,
            itm_sword_medieval_b_small,
            itm_tab_shield_heater_a,
            itm_arming_cap_a,
            itm_leather_gloves_a,
            itm_padded_cloth,
            itm_warhorse,
        ],
        level(4) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "chornovalley_longbowman_multiplayer_coop_tier_1",
        "Vaegir Archer",
        "Vaegir Archers",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_2,
        [itm_arrows, itm_axe, itm_hunting_bow, itm_regular_shirt_b],
        level(4) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "vaegir_spearman_multiplayer_coop_tier_1",
        "Vaegir Spearman",
        "Vaegir spearman",
        tf_guarantee_ranged
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet
        | tf_guarantee_ranged
        | tf_guarantee_shield,
        0,
        0,
        fac_kingdom_2,
        [itm_tab_shield_kite_a, itm_axe, itm_rawhide_coat],
        level(4) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "chornovalley_horseman_multiplayer_coop_tier_1",
        "Vaegir Horseman",
        "Vaegir Horsemen",
        tf_mounted | tf_guarantee_all,
        0,
        0,
        fac_kingdom_2,
        [itm_spear, itm_tab_shield_kite_cav_a, itm_regular_shirt_b, itm_hunter],
        level(4) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "celestial_sergeant_multiplayer_coop_tier_1",
        "Khergit Horse Archer",
        "Khergit Horse Archers",
        tf_mounted | tf_guarantee_all,
        0,
        0,
        fac_kingdom_3,
        [
            itm_sword_khergit_1,
            itm_nomad_bow,
            itm_arrows,
            itm_steppe_armor,
            itm_steppe_horse,
        ],
        level(4) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "khergit_infantry_multiplayer_coop_tier_1",
        "Khergit Infantry",
        "Khergit Infantries",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_3,
        [
            itm_sword_khergit_1,
            itm_tab_shield_small_round_a,
            itm_steppe_armor,
            itm_leather_gloves_a,
        ],
        level(4) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "celestial_lancer_multiplayer_coop_tier_1",
        "Khergit Lancer",
        "Khergit Lancers",
        tf_mounted | tf_guarantee_all,
        0,
        0,
        fac_kingdom_3,
        [
            itm_spear,
            itm_tab_shield_small_round_a,
            itm_steppe_armor,
            itm_steppe_cap,
            itm_leather_gloves_a,
            itm_courser,
        ],
        level(4) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "iron_crown_trained_skirmisher_multiplayer_coop_tier_1",
        "Nord Archer",
        "Nord Archers",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_4,
        [itm_arrows, itm_sword_viking_2_small, itm_short_bow, itm_blue_tunic],
        level(4) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "iron_crown_vetaran_multiplayer_coop_tier_1",
        "Nord Huscarl",
        "Nord Huscarls",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_4,
        [
            itm_sword_viking_1,
            itm_one_handed_war_axe_a,
            itm_tab_shield_round_a,
            itm_blue_tunic,
        ],
        level(4) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "nord_scout_multiplayer_coop_tier_1",
        "Nord Scout",
        "Nord Scouts",
        tf_mounted | tf_guarantee_all,
        0,
        0,
        fac_kingdom_4,
        [
            itm_javelin,
            itm_war_spear,
            itm_tab_shield_small_round_a,
            itm_blue_tunic,
            itm_saddle_horse,
        ],
        level(4) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "alpine_veteran_crossbowman_multiplayer_coop_tier_1",
        "Rhodok Crossbowman",
        "Rhodok Crossbowmen",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_5,
        [
            itm_crossbow,
            itm_bolts,
            itm_fighting_pick,
            itm_tab_shield_pavise_a,
            itm_peasant_regular_shirt_a,
        ],
        level(4) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "alpine_man_at_arms_multiplayer_coop_tier_1",
        "Rhodok Sergeant",
        "Rhodok Sergeants",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_5,
        [
            itm_military_cleaver_b,
            itm_tab_shield_pavise_a,
            itm_darts,
            itm_green_tunic,
            itm_arming_cap_a,
        ],
        level(4) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "rhodok_horseman_multiplayer_coop_tier_1",
        "Rhodok Horseman",
        "Rhodok Horsemen",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_5,
        [
            itm_tab_shield_heater_cav_a,
            itm_light_lance,
            itm_green_tunic,
            itm_padded_coif_a,
            itm_saddle_horse,
        ],
        level(4) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "solarian_archer_multiplayer_coop_tier_1",
        "Sarranid Archer",
        "Sarranid Archers",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_6,
        [],
        level(4) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "solarian_footman_multiplayer_coop_tier_1",
        "Sarranid Footman",
        "Sarranid footman",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_6,
        [],
        level(4) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "solarian_knight_multiplayer_coop_tier_1",
        "Sarranid Mamluke",
        "Sarranid Mamluke",
        tf_mounted | tf_guarantee_all,
        0,
        0,
        fac_kingdom_6,
        [
            itm_lance,
            itm_tab_shield_small_round_a,
            itm_arabian_horse_a,
        ],
        level(4) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "silver_rose_trained_crossbowman_multiplayer_coop_tier_2",
        "Swadian Crossbowman",
        "Swadian Crossbowmen",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_1,
        [
            itm_spiked_club,
            itm_crossbow,
            itm_bolts,
            itm_tab_shield_heater_b,
            itm_arming_cap_a,
            itm_red_gambeson,
        ],
        level(5) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "silver_rose_infantry_multiplayer_coop_tier_2",
        "Swadian Infantry",
        "Swadian Infantry",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_1,
        [
            itm_sword_medieval_b,
            itm_tab_shield_heater_c,
            itm_spear,
            itm_mail_coif,
            itm_leather_gloves_a,
            itm_mail_with_tunic_red,
        ],
        level(5) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "silver_rose_man_at_arms_multiplayer_coop_tier_2",
        "Swadian Man at Arms",
        "Swadian Men at Arms",
        tf_mounted | tf_guarantee_all,
        0,
        0,
        fac_kingdom_1,
        [
            itm_lance,
            itm_sword_medieval_a,
            itm_tab_shield_heater_b,
            itm_sallet_a_v5,
            itm_leather_gloves_a,
            itm_olive_hauberk_a_v1,
            itm_warhorse,
        ],
        level(5) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "chornovalley_longbowman_multiplayer_coop_tier_2",
        "Vaegir Archer",
        "Vaegir Archers",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_2,
        [
            itm_barbed_arrows,
            itm_axe,
            itm_nomad_bow,
            itm_leather_vest_regular_shirt_a,
        ],
        level(5) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "vaegir_spearman_multiplayer_coop_tier_2",
        "Vaegir Spearman",
        "Vaegir spearman",
        tf_guarantee_ranged
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet
        | tf_guarantee_ranged
        | tf_guarantee_shield,
        0,
        0,
        fac_kingdom_2,
        [
            itm_javelin,
            itm_scimitar,
            itm_tab_shield_kite_b,
            itm_leather_jerkin,
            itm_leather_gloves_a,
        ],
        level(5) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "chornovalley_horseman_multiplayer_coop_tier_2",
        "Vaegir Horseman",
        "Vaegir Horsemen",
        tf_mounted | tf_guarantee_all,
        0,
        0,
        fac_kingdom_2,
        [
            itm_war_spear,
            itm_tab_shield_kite_cav_b,
            itm_javelin,
            itm_studded_leather_coat,
            itm_leather_gloves_a,
            itm_hunter,
        ],
        level(5) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "celestial_sergeant_multiplayer_coop_tier_2",
        "Khergit Horse Archer",
        "Khergit Horse Archers",
        tf_mounted | tf_guarantee_all,
        0,
        0,
        fac_kingdom_3,
        [
            itm_sword_khergit_2,
            itm_khergit_bow,
            itm_barbed_arrows,
            itm_steppe_armor,
            itm_leather_steppe_cap_a,
            itm_steppe_horse,
        ],
        level(5) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "khergit_infantry_multiplayer_coop_tier_2",
        "Khergit Infantry",
        "Khergit Infantries",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_3,
        [
            itm_sword_khergit_2,
            itm_tab_shield_small_round_b,
            itm_javelin,
            itm_tribal_warrior_outfit,
            itm_leather_gloves_a,
        ],
        level(5) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "celestial_lancer_multiplayer_coop_tier_2",
        "Khergit Lancer",
        "Khergit Lancers",
        tf_mounted | tf_guarantee_all,
        0,
        0,
        fac_kingdom_3,
        [
            itm_war_spear,
            itm_tab_shield_small_round_b,
            itm_javelin,
            itm_tribal_warrior_outfit,
            itm_leather_steppe_cap_b,
            itm_courser,
        ],
        level(5) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "iron_crown_trained_skirmisher_multiplayer_coop_tier_2",
        "Nord Archer",
        "Nord Archers",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_4,
        [
            itm_arrows,
            itm_sword_viking_2,
            itm_long_bow,
            itm_leather_jerkin,
        ],
        level(5) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "iron_crown_vetaran_multiplayer_coop_tier_2",
        "Nord Huscarl",
        "Nord Huscarls",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_4,
        [
            itm_one_handed_war_axe_a,
            itm_tab_shield_round_b,
            itm_throwing_axes,
            itm_leather_jerkin,
            itm_leather_gloves_a,
        ],
        level(5) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "nord_scout_multiplayer_coop_tier_2",
        "Nord Scout",
        "Nord Scouts",
        tf_mounted | tf_guarantee_all,
        0,
        0,
        fac_kingdom_4,
        [
            itm_javelin,
            itm_lance,
            itm_tab_shield_small_round_a,
            itm_leather_jerkin,
            itm_leather_gloves_a,
            itm_saddle_horse,
        ],
        level(5) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "alpine_veteran_crossbowman_multiplayer_coop_tier_2",
        "Rhodok Crossbowman",
        "Rhodok Crossbowmen",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_5,
        [
            itm_heavy_crossbow,
            itm_bolts,
            itm_club_with_spike_head,
            itm_tab_shield_pavise_b,
            itm_leather_armor,
            itm_leather_gloves_a,
            itm_arming_cap_a,
        ],
        level(5) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "alpine_man_at_arms_multiplayer_coop_tier_2",
        "Rhodok Sergeant",
        "Rhodok Sergeants",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_5,
        [
            itm_military_cleaver_b,
            itm_tab_shield_pavise_b,
            itm_war_darts,
            itm_padded_cloth,
            itm_leather_gloves_a,
        ],
        level(5) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "rhodok_horseman_multiplayer_coop_tier_2",
        "Rhodok Horseman",
        "Rhodok Horsemen",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_5,
        [
            itm_tab_shield_heater_cav_b,
            itm_heavy_lance,
            itm_javelin,
            itm_padded_cloth,
            itm_leather_gloves_a,
            itm_saddle_horse,
        ],
        level(5) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "solarian_archer_multiplayer_coop_tier_2",
        "Sarranid Archer",
        "Sarranid Archers",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_6,
        [
            itm_barbed_arrows,
            itm_mace_a,
            itm_nomad_bow,
            itm_leather_gloves_a,
        ],
        level(5) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "solarian_footman_multiplayer_coop_tier_2",
        "Sarranid Footman",
        "Sarranid footman",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_6,
        [
            itm_tab_shield_kite_b,
            itm_hatchet_b_v1,
            itm_javelin,
            itm_leather_gloves_a,
        ],
        level(5) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "solarian_knight_multiplayer_coop_tier_2",
        "Sarranid Mamluke",
        "Sarranid Mamluke",
        tf_mounted | tf_guarantee_all,
        0,
        0,
        fac_kingdom_6,
        [
            itm_heavy_lance,
            itm_tab_shield_small_round_b,
            itm_javelin,
            itm_leather_gloves_a,
            itm_arabian_horse_a,
        ],
        level(5) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "silver_rose_trained_crossbowman_multiplayer_coop_tier_3",
        "Swadian Crossbowman",
        "Swadian Crossbowmen",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_1,
        [
            itm_sword_medieval_b,
            itm_heavy_crossbow,
            itm_steel_bolts,
            itm_tab_shield_heater_c,
            itm_sallet_c,
            itm_leather_jerkin,
        ],
        level(6) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "silver_rose_infantry_multiplayer_coop_tier_3",
        "Swadian Infantry",
        "Swadian Infantry",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_1,
        [
            itm_bastard_sword_a,
            itm_awlpike,
            itm_tab_shield_heater_c,
            itm_sallet_a,
            itm_mail_mittens_a,
        ],
        level(6) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "silver_rose_man_at_arms_multiplayer_coop_tier_3",
        "Swadian Man at Arms",
        "Swadian Men at Arms",
        tf_mounted | tf_guarantee_all,
        0,
        0,
        fac_kingdom_1,
        [
            itm_heavy_lance,
            itm_bastard_sword_b,
            itm_tab_shield_heater_cav_a,
            itm_flat_top_b_v1,
            itm_mail_mittens_a,
            itm_warhorse,
        ],
        level(6) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "chornovalley_longbowman_multiplayer_coop_tier_3",
        "Vaegir Archer",
        "Vaegir Archers",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_2,
        [
            itm_barbed_arrows,
            itm_scimitar_b,
            itm_strong_bow,
            itm_leather_jerkin,
            itm_leather_gloves_a,
        ],
        level(6) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "vaegir_spearman_multiplayer_coop_tier_3",
        "Vaegir Spearman",
        "Vaegir spearman",
        tf_guarantee_ranged
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet
        | tf_guarantee_ranged
        | tf_guarantee_shield,
        0,
        0,
        fac_kingdom_2,
        [
            itm_scimitar_b,
            itm_tab_shield_kite_b,
            itm_javelin,
            itm_leather_gloves_a,
        ],
        level(6) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "chornovalley_horseman_multiplayer_coop_tier_3",
        "Vaegir Horseman",
        "Vaegir Horsemen",
        tf_mounted | tf_guarantee_all,
        0,
        0,
        fac_kingdom_2,
        [
            itm_heavy_lance,
            itm_tab_shield_kite_cav_b,
            itm_javelin,
            itm_hunter,
            itm_mail_mittens_a,
        ],
        level(6) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "celestial_sergeant_multiplayer_coop_tier_3",
        "Khergit Horse Archer",
        "Khergit Horse Archers",
        tf_mounted | tf_guarantee_all,
        0,
        0,
        fac_kingdom_3,
        [
            itm_sword_khergit_3,
            itm_strong_bow,
            itm_khergit_arrows,
            itm_tribal_warrior_outfit,
            itm_leather_steppe_cap_c,
            itm_steppe_horse,
        ],
        level(6) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "khergit_infantry_multiplayer_coop_tier_3",
        "Khergit Infantry",
        "Khergit Infantries",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_3,
        [
            itm_hafted_blade_a,
            itm_javelin,
            itm_leather_steppe_cap_c,
            itm_mail_mittens_a,
        ],
        level(6) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "celestial_lancer_multiplayer_coop_tier_3",
        "Khergit Lancer",
        "Khergit Lancers",
        tf_mounted | tf_guarantee_all,
        0,
        0,
        fac_kingdom_3,
        [
            itm_heavy_lance,
            itm_tab_shield_small_round_a,
            itm_leather_steppe_cap_c,
            itm_courser,
        ],
        level(6) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "iron_crown_trained_skirmisher_multiplayer_coop_tier_3",
        "Nord Archer",
        "Nord Archers",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_4,
        [
            itm_barbed_arrows,
            itm_sword_viking_3,
            itm_long_bow,
            itm_leather_jerkin,
            itm_leather_gloves_a,
        ],
        level(6) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "iron_crown_vetaran_multiplayer_coop_tier_3",
        "Nord Huscarl",
        "Nord Huscarls",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_4,
        [
            itm_one_handed_war_axe_b,
            itm_tab_shield_round_d,
            itm_heavy_throwing_axes,
        ],
        level(6) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "nord_scout_multiplayer_coop_tier_3",
        "Nord Scout",
        "Nord Scouts",
        tf_mounted | tf_guarantee_all,
        0,
        0,
        fac_kingdom_4,
        [
            itm_throwing_spears,
            itm_heavy_lance,
            itm_tab_shield_small_round_b,
            itm_saddle_horse,
        ],
        level(6) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "alpine_veteran_crossbowman_multiplayer_coop_tier_3",
        "Rhodok Crossbowman",
        "Rhodok Crossbowmen",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_5,
        [
            itm_sniper_crossbow,
            itm_steel_bolts,
            itm_military_cleaver_c,
            itm_tab_shield_pavise_c,
            itm_padded_cloth,
            itm_leather_gloves_a,
        ],
        level(6) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "alpine_man_at_arms_multiplayer_coop_tier_3",
        "Rhodok Sergeant",
        "Rhodok Sergeants",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_5,
        [
            itm_tab_shield_pavise_c,
            itm_military_cleaver_c,
            itm_javelin,
            itm_ragged_outfit,
            itm_eyeslot_kettlehat_a_v2,
            itm_mail_mittens_a,
        ],
        level(6) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "rhodok_horseman_multiplayer_coop_tier_3",
        "Rhodok Horseman",
        "Rhodok Horsemen",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_5,
        [
            itm_javelin,
            itm_tab_shield_heater_cav_b,
            itm_heavy_lance,
            itm_ragged_outfit,
            itm_sallet_b,
            itm_mail_mittens_a,
            itm_saddle_horse,
        ],
        level(6) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "solarian_archer_multiplayer_coop_tier_3",
        "Sarranid Archer",
        "Sarranid Archers",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_6,
        [
            itm_khergit_arrows,
            itm_mace_a,
            itm_nomad_bow,
            itm_leather_gloves_a,
        ],
        level(6) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "solarian_footman_multiplayer_coop_tier_3",
        "Sarranid Footman",
        "Sarranid footman",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_6,
        [
            itm_jarid,
            itm_tab_shield_kite_c,
            itm_hatchet_b_v1,
            itm_mail_mittens_a,
        ],
        level(6) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "solarian_knight_multiplayer_coop_tier_3",
        "Sarranid Mamluke",
        "Sarranid Mamluke",
        tf_mounted | tf_guarantee_all,
        0,
        0,
        fac_kingdom_6,
        [
            itm_heavy_lance,
            itm_tab_shield_small_round_b,
            itm_jarid,
            itm_mail_mittens_a,
            itm_arabian_horse_a,
        ],
        level(6) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "silver_rose_trained_crossbowman_multiplayer_coop_tier_4",
        "Swadian Crossbowman",
        "Swadian Crossbowmen",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_1,
        [
            itm_sword_medieval_b,
            itm_sniper_crossbow,
            itm_steel_bolts,
            itm_tab_shield_heater_c,
            itm_sallet_a_v5,
            itm_leather_gloves_a,
            itm_olive_hauberk_a_v1,
        ],
        level(7) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "silver_rose_infantry_multiplayer_coop_tier_4",
        "Swadian Infantry",
        "Swadian Infantry",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_1,
        [
            itm_bastard_sword_b,
            itm_awlpike_long,
            itm_tab_shield_heater_d,
            itm_sallet_c,
            itm_plate_gauntlets_a_v1,
            itm_coat_of_plates,
        ],
        level(7) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "silver_rose_man_at_arms_multiplayer_coop_tier_4",
        "Swadian Man at Arms",
        "Swadian Men at Arms",
        tf_mounted | tf_guarantee_all,
        0,
        0,
        fac_kingdom_1,
        [
            itm_great_lance,
            itm_morningstar,
            itm_tab_shield_heater_cav_b,
            itm_great_helmet,
            itm_plate_gauntlets_a_v1,
            itm_coat_of_plates_red,
            itm_warhorse,
        ],
        level(7) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "chornovalley_longbowman_multiplayer_coop_tier_4",
        "Vaegir Archer",
        "Vaegir Archers",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_2,
        [
            itm_barbed_arrows,
            itm_bardiche,
            itm_war_bow,
            itm_lamellar_vest,
            itm_leather_gloves_a,
        ],
        level(7) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "vaegir_spearman_multiplayer_coop_tier_4",
        "Vaegir Spearman",
        "Vaegir spearman",
        tf_guarantee_ranged
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet
        | tf_guarantee_ranged
        | tf_guarantee_shield,
        0,
        0,
        fac_kingdom_2,
        [
            itm_bardiche,
            itm_javelin,
            itm_mail_mittens_a,
        ],
        level(7) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "chornovalley_horseman_multiplayer_coop_tier_4",
        "Vaegir Horseman",
        "Vaegir Horsemen",
        tf_mounted | tf_guarantee_all,
        0,
        0,
        fac_kingdom_2,
        [
            itm_heavy_lance,
            itm_tab_shield_kite_cav_b,
            itm_javelin,
            itm_hunter,
        ],
        level(7) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "celestial_sergeant_multiplayer_coop_tier_4",
        "Khergit Horse Archer",
        "Khergit Horse Archers",
        tf_mounted | tf_guarantee_all,
        0,
        0,
        fac_kingdom_3,
        [
            itm_hafted_blade_b,
            itm_strong_bow,
            itm_khergit_arrows,
            itm_lamellar_vest_khergit,
            itm_khergit_guard_helmet,
            itm_steppe_horse,
        ],
        level(7) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "khergit_infantry_multiplayer_coop_tier_4",
        "Khergit Infantry",
        "Khergit Infantries",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_3,
        [
            itm_hafted_blade_b,
            itm_tab_shield_small_round_a,
            itm_jarid,
            itm_khergit_war_helmet,
        ],
        level(7) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "celestial_lancer_multiplayer_coop_tier_4",
        "Khergit Lancer",
        "Khergit Lancers",
        tf_mounted | tf_guarantee_all,
        0,
        0,
        fac_kingdom_3,
        [
            itm_great_lance,
            itm_tab_shield_small_round_c,
            itm_khergit_war_helmet,
            itm_courser,
        ],
        level(7) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "iron_crown_trained_skirmisher_multiplayer_coop_tier_4",
        "Nord Archer",
        "Nord Archers",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_4,
        [
            itm_khergit_arrows,
            itm_sword_viking_3,
            itm_long_bow,
            itm_gray_hauberk_a,
            itm_leather_gloves_a,
        ],
        level(7) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "iron_crown_vetaran_multiplayer_coop_tier_4",
        "Nord Huscarl",
        "Nord Huscarls",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_4,
        [
            itm_great_axe,
            itm_tab_shield_round_e,
            itm_heavy_throwing_axes,
            itm_banded_armor,
        ],
        level(7) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "nord_scout_multiplayer_coop_tier_4",
        "Nord Scout",
        "Nord Scouts",
        tf_mounted | tf_guarantee_all,
        0,
        0,
        fac_kingdom_4,
        [
            itm_throwing_spears,
            itm_great_lance,
            itm_tab_shield_small_round_c,
            itm_white_hauberk_a,
            itm_saddle_horse,
        ],
        level(7) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "alpine_veteran_crossbowman_multiplayer_coop_tier_4",
        "Rhodok Crossbowman",
        "Rhodok Crossbowmen",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_5,
        [
            itm_sniper_crossbow,
            itm_steel_bolts,
            itm_sledgehammer,
            itm_tab_shield_pavise_d,
            itm_mail_with_tunic_green,
            itm_eyeslot_kettlehat_a_v2,
            itm_leather_gloves_a,
        ],
        level(7) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "alpine_man_at_arms_multiplayer_coop_tier_4",
        "Rhodok Sergeant",
        "Rhodok Sergeants",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_5,
        [
            itm_two_handed_cleaver,
            itm_tab_shield_pavise_d,
            itm_javelin,
            itm_plate_gauntlets_a_v1,
            itm_m_bascinet_b,
        ],
        level(7) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "rhodok_horseman_multiplayer_coop_tier_4",
        "Rhodok Horseman",
        "Rhodok Horsemen",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_5,
        [
            itm_javelin,
            itm_tab_shield_heater_cav_b,
            itm_great_lance,
            itm_plate_gauntlets_a_v1,
            itm_m_bascinet_b,
            itm_saddle_horse,
        ],
        level(7) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "solarian_archer_multiplayer_coop_tier_4",
        "Sarranid Archer",
        "Sarranid Archers",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_6,
        [
            itm_khergit_arrows,
            itm_mace_a_v1,
            itm_strong_bow,
            itm_leather_gloves_a,
        ],
        level(7) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "solarian_footman_multiplayer_coop_tier_4",
        "Sarranid Footman",
        "Sarranid footman",
        tf_guarantee_all,
        0,
        0,
        fac_kingdom_6,
        [
            itm_bamboo_spear,
            itm_tab_shield_kite_c,
            itm_sword_b,
        ],
        level(7) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "solarian_knight_multiplayer_coop_tier_4",
        "Sarranid Mamluke",
        "Sarranid Mamluke",
        tf_mounted | tf_guarantee_all,
        0,
        0,
        fac_kingdom_6,
        [
            itm_sword_b,
            itm_lance,
            itm_tab_shield_small_round_c,
            itm_arabian_horse_a,
        ],
        level(7) | str_20,
        wp(300),
        knows_power_draw_10 | knows_power_throw_10 | knows_riding_10,
        0,
        0,
    ],
    [
        "coop_faction_troop_templates_end",
        "{!}multiplayer_end",
        "{!}multiplayer_end",
        0,
        0,
        0,
        fac_kingdom_5,
        [],
        0,
        0,
        0,
        0,
        0,
    ],
    # tier 1
    [
        "npc1_1",
        "Hurey",
        "Hurey",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [itm_khergit_armor, itm_knife, itm_courser],
        str_16 | agi_17 | int_6 | cha_30 | level(25),
        wpex(250, 80, 140, 160, 90, 250),
        knows_tracking_10
        | knows_engineer_10
        | knows_first_aid_10
        | knows_surgery_10
        | knows_wound_treatment_10
        | knows_tactics_10
        | knows_trainer_10
        | knows_looting_10
        | knows_ironflesh_1
        | knows_power_strike_7
        | knows_pathfinding_3
        | knows_athletics_5
        | knows_tracking_1
        | knows_riding_6
        | knows_power_throw_7
        | knows_power_draw_5,  # skills 2/3 player at that level
        0x0000000E730065C420DB6DB6DB6DDEFF00000000001DB6F00000000000000000,
    ],
    [
        "npc2_1",
        "Mesym",
        "Mesym",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [itm_regular_shirt_b, itm_club, itm_saddle_horse],
        str_14 | agi_17 | int_6 | cha_30 | level(25),
        wpex(240, 130, 170, 150, 170, 90),
        knows_tracking_10
        | knows_engineer_10
        | knows_first_aid_10
        | knows_surgery_10
        | knows_wound_treatment_10
        | knows_tactics_10
        | knows_trainer_10
        | knows_looting_10
        | knows_trade_2
        | knows_weapon_master_1
        | knows_ironflesh_1
        | knows_wound_treatment_1
        | knows_athletics_5
        | knows_first_aid_1
        | knows_leadership_1
        | knows_riding_4
        | knows_power_strike_7
        | knows_power_draw_3
        | knows_power_throw_3,
        0x0000000BFF003440209B6E38E06DBEFF00000000001F36E10000000000000000,
    ],
    [
        "npc3_1",
        "Evel Droby",
        "Evel Droby",
        tf_female | tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [itm_dress, itm_knife, itm_hunter],
        str_24 | agi_13 | int_6 | cha_30 | level(25),
        wpex(190, 80, 240, 180, 180, 80),
        knows_tracking_10
        | knows_engineer_10
        | knows_first_aid_10
        | knows_surgery_10
        | knows_wound_treatment_10
        | knows_tactics_10
        | knows_trainer_10
        | knows_looting_10
        | knows_wound_treatment_1
        | knows_trade_1
        | knows_first_aid_3
        | knows_surgery_1
        | knows_athletics_6
        | knows_riding_8
        | knows_power_strike_5
        | knows_power_draw_3
        | knows_power_throw_3,
        0x00000004A204300436DB6DB6DB6DFEFF00000000001DB6DB0000000000000000,
    ],
    [
        "npc4_1",
        "Ilhan",
        "Ilhan",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [itm_leather_jerkin, itm_sword_medieval_a, itm_hunter],
        str_20 | agi_13 | int_6 | cha_30 | level(25),
        wpex(210, 230, 200, 90, 100, 95),
        knows_tracking_10
        | knows_engineer_10
        | knows_first_aid_10
        | knows_surgery_10
        | knows_wound_treatment_10
        | knows_tactics_10
        | knows_trainer_10
        | knows_looting_10
        | knows_weapon_master_2
        | knows_power_strike_9
        | knows_riding_8
        | knows_athletics_7
        | knows_power_throw_3
        | knows_first_aid_1
        | knows_surgery_1
        | knows_tactics_2
        | knows_leadership_2
        | knows_power_draw_2,
        0x0000000B7D00130020DB6DB6DB6DBEFF00000000001DB6E80000000000000000,
    ],
    [
        "npc5_1",
        "Gyliam Gare",
        "Gyliam Gare",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [itm_nomad_vest, itm_sword_khergit_1, itm_steppe_horse],
        str_18 | agi_13 | int_6 | cha_30 | level(25),
        wpex(160, 80, 130, 250, 50, 230),
        knows_tracking_10
        | knows_engineer_10
        | knows_first_aid_10
        | knows_surgery_10
        | knows_wound_treatment_10
        | knows_tactics_10
        | knows_trainer_10
        | knows_looting_10
        | knows_riding_7
        | knows_horse_archery_9
        | knows_power_draw_8
        | knows_leadership_2
        | knows_weapon_master_1
        | knows_power_strike_5
        | knows_power_throw_8
        | knows_athletics_5,
        0x0000000DFF00115420DB6DB6DB6DBEFF00000000001DB6E80000000000000000,
    ],
    [
        "npc6_1",
        "Ames",
        "Ames",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [itm_tabard_a, itm_sword_medieval_a, itm_sumpter_horse],
        str_20 | agi_19 | int_6 | cha_30 | level(25),
        wpex(240, 210, 180, 90, 100, 80),
        knows_tracking_10
        | knows_engineer_10
        | knows_first_aid_10
        | knows_surgery_10
        | knows_wound_treatment_10
        | knows_tactics_10
        | knows_trainer_10
        | knows_looting_10
        | knows_riding_7
        | knows_weapon_master_2
        | knows_athletics_8
        | knows_trainer_1
        | knows_leadership_1
        | knows_power_strike_7
        | knows_power_draw_2
        | knows_power_throw_3,
        0x0000000D401001CF20DB6DB6DB6DFEFF00000000001DB6D00000000000000000,
    ],
    [
        "npc7_1",
        "Malia Willey",
        "Malia Willey",
        tf_female | tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_ragged_outfit,
            itm_hunting_bow,
            itm_arrows,
            itm_quarter_staff,
            itm_arabian_horse_b,
        ],
        str_16 | agi_13 | int_6 | cha_30 | level(25),
        wpex(90, 80, 230, 280, 110, 130),
        knows_tracking_10
        | knows_engineer_10
        | knows_first_aid_10
        | knows_surgery_10
        | knows_wound_treatment_10
        | knows_tactics_10
        | knows_trainer_10
        | knows_looting_10
        | knows_tracking_2
        | knows_athletics_8
        | knows_spotting_1
        | knows_pathfinding_1
        | knows_power_draw_10
        | knows_riding_4
        | knows_power_strike_6
        | knows_power_throw_5,
        0x000000031F08000206D86DB64B4DB6DB00000000001DB6C30000000000000000,
    ],
    [
        "npc8_1",
        "Eryet Allard",
        "Eryet Allard",
        tf_female | tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [itm_tribal_warrior_outfit, itm_sword_viking_1, itm_courser],
        str_18 | agi_15 | int_6 | cha_30 | level(25),
        wpex(190, 250, 80, 120, 80, 250),
        knows_tracking_10
        | knows_engineer_10
        | knows_first_aid_10
        | knows_surgery_10
        | knows_wound_treatment_10
        | knows_tactics_10
        | knows_trainer_10
        | knows_looting_10
        | knows_weapon_master_3
        | knows_athletics_10
        | knows_leadership_3
        | knows_tactics_1
        | knows_riding_4
        | knows_power_strike_10
        | knows_power_draw_2
        | knows_power_throw_8,
        0x0000000FFE08000300DB6DB6496208D400000000001D86FC0000000000000000,
    ],
    [
        "npc9_1",
        "Aduhash",
        "Aduhash",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [itm_tabard_a, itm_sword_medieval_b_small, itm_courser],
        str_22 | agi_19 | int_6 | cha_30 | level(25),
        wpex(80, 230, 130, 220, 70, 160),
        knows_tracking_10
        | knows_engineer_10
        | knows_first_aid_10
        | knows_surgery_10
        | knows_wound_treatment_10
        | knows_tactics_10
        | knows_trainer_10
        | knows_looting_10
        | knows_weapon_master_1
        | knows_riding_4
        | knows_athletics_6
        | knows_leadership_1
        | knows_tactics_1
        | knows_power_strike_4
        | knows_power_draw_7
        | knows_power_throw_5,
        0x00000001900471C6125B69FCDB6DBEFF00000000001DB6FB0000000000000000,
    ],
    [
        "npc10_1",
        "Zela",
        "Zela",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [itm_padded_leather, itm_crossbow, itm_bolts, itm_pickaxe_a_v1, itm_saddle_horse],
        str_24 | agi_19 | int_6 | cha_30 | level(25),
        wpex(170, 80, 80, 160, 290, 150),
        knows_tracking_10
        | knows_engineer_10
        | knows_first_aid_10
        | knows_surgery_10
        | knows_wound_treatment_10
        | knows_tactics_10
        | knows_trainer_10
        | knows_looting_10
        | knows_weapon_master_3
        | knows_tactics_1
        | knows_leadership_1
        | knows_ironflesh_3
        | knows_trainer_2
        | knows_first_aid_2
        | knows_riding_4
        | knows_power_strike_5
        | knows_power_draw_5
        | knows_power_throw_5
        | knows_athletics_7,
        0x0000000190042348058365C91C7D8EFF00000000001DE6FB0000000000000000,
    ],
    [
        "npc11_1",
        "Jane",
        "Jane",
        tf_female | tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [itm_peasant_regular_shirt_a_v1, itm_falchion_a, itm_sumpter_horse],
        str_16 | agi_17 | int_6 | cha_30 | level(25),
        wpex(140, 230, 130, 80, 210, 170),
        knows_tracking_10
        | knows_engineer_10
        | knows_first_aid_10
        | knows_surgery_10
        | knows_wound_treatment_10
        | knows_tactics_10
        | knows_trainer_10
        | knows_looting_10
        | knows_weapon_master_1
        | knows_first_aid_1
        | knows_wound_treatment_2
        | knows_ironflesh_3
        | knows_inventory_management_5
        | knows_riding_4
        | knows_power_strike_5
        | knows_power_draw_2
        | knows_power_throw_7
        | knows_athletics_5,
        0x00000006000C000206186196918DB8E400000000001D48C40000000000000000,
    ],
    [
        "npc12_1",
        "Pai Khoi-Kao",
        "Pai Khoi-Kao",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [itm_pilgrim_disguise, itm_staff, itm_sumpter_horse],
        str_16 | agi_17 | int_6 | cha_30 | level(25),
        wpex(120, 110, 290, 80, 110, 120),
        knows_tracking_10
        | knows_engineer_10
        | knows_first_aid_10
        | knows_surgery_10
        | knows_wound_treatment_10
        | knows_tactics_10
        | knows_trainer_10
        | knows_looting_10
        | knows_ironflesh_1
        | knows_power_strike_7
        | knows_surgery_4
        | knows_wound_treatment_3
        | knows_first_aid_3
        | knows_riding_4
        | knows_power_draw_2
        | knows_power_throw_3
        | knows_athletics_7,
        0x00000001BF044383201D6A24DA6DBCFF00000000001DB6F80000000000000000,
    ],
    [
        "npc13_1",
        "Dondo",
        "Dondo",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [itm_nomad_robe, itm_scimitar, itm_courser],
        str_14 | agi_17 | int_6 | cha_30 | level(25),
        wpex(250, 80, 140, 210, 110, 140),
        knows_tracking_10
        | knows_engineer_10
        | knows_first_aid_10
        | knows_surgery_10
        | knows_wound_treatment_10
        | knows_tactics_10
        | knows_trainer_10
        | knows_looting_10
        | knows_riding_9
        | knows_leadership_2
        | knows_athletics_5
        | knows_ironflesh_2
        | knows_power_strike_6
        | knows_weapon_master_1
        | knows_power_draw_7
        | knows_power_throw_4,
        0x00000001BF0474D420DC6A36EA6DBCFF00000000001DB6F80000000000000000,
    ],
    [
        "npc14_1",
        "Elrel",
        "Elrel",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [itm_tabard_f, itm_sword_medieval_b_small, itm_courser],
        str_18 | agi_19 | int_6 | cha_30 | level(25),
        wpex(280, 170, 170, 170, 170, 180),
        knows_tracking_10
        | knows_engineer_10
        | knows_first_aid_10
        | knows_surgery_10
        | knows_wound_treatment_10
        | knows_tactics_10
        | knows_trainer_10
        | knows_looting_10
        | knows_trainer_4
        | knows_weapon_master_3
        | knows_leadership_2
        | knows_power_strike_1
        | knows_riding_7
        | knows_power_strike_7
        | knows_power_draw_6
        | knows_power_throw_6
        | knows_athletics_8,
        0x00000001BE00024545136DC11B79FCDB00000000001DB6E80000000000000000,
    ],
    [
        "npc15_1",
        "Phamas",
        "Phamas",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [itm_tabard_d, itm_sword_medieval_b_small, itm_hunter],
        str_18 | agi_13 | int_6 | cha_30 | level(25),
        wpex(190, 290, 130, 210, 90, 90),
        knows_tracking_10
        | knows_engineer_10
        | knows_first_aid_10
        | knows_surgery_10
        | knows_wound_treatment_10
        | knows_tactics_10
        | knows_trainer_10
        | knows_looting_10
        | knows_tactics_2
        | knows_engineer_4
        | knows_trade_3
        | knows_tracking_1
        | knows_spotting_1
        | knows_riding_6
        | knows_power_strike_7
        | knows_power_draw_7
        | knows_power_throw_3
        | knows_athletics_5,
        0x0000000FB110600020DB6DD9226DBF7F00000000001DB6F80000000000000000,
    ],
    [
        "npc16_1",
        "Kina",
        "Kina",
        tf_female | tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [itm_peasant_dress, itm_dagger, itm_throwing_knives, itm_saddle_horse],
        str_14 | agi_17 | int_6 | cha_30 | level(25),
        wpex(260, 10, 100, 160, 30, 300),
        knows_tracking_10
        | knows_engineer_10
        | knows_first_aid_10
        | knows_surgery_10
        | knows_wound_treatment_10
        | knows_tactics_10
        | knows_trainer_10
        | knows_looting_10
        | knows_power_throw_10
        | knows_athletics_10
        | knows_power_strike_8
        | knows_riding_4
        | knows_power_draw_5,
        0x00000000000C3001009849A2494288CB00000000001DA6830000000000000000,
    ],
    # tier 2
    [
        "npc1_2",
        "Hurey",
        "Hurey",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_leather_steppe_cap_c,
            itm_leather_gloves_a,
            itm_nomad_robe,
            itm_sword_medieval_b_small,
            itm_courser,
        ],
        str_16 | agi_17 | int_12 | cha_7 | level(14),
        wp(60),
        knows_tracker_npc
        | knows_ironflesh_1
        | knows_power_strike_1
        | knows_pathfinding_3
        | knows_athletics_2
        | knows_tracking_1
        | knows_riding_2,  # skills 2/3 player at that level
        0x0000000E730065C420DB6DB6DB6DDEFF00000000001DB6F00000000000000000,
    ],
    [
        "npc2_2",
        "Mesym",
        "Mesym",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_eyeslot_kettlehat_a_v1,
            itm_padded_leather,
            itm_mace_2,
            itm_tab_shield_small_round_a,
            itm_saddle_horse,
        ],
        str_14 | agi_17 | int_11 | cha_6 | level(14),
        wp(40),
        knows_merchant_npc
        | knows_trade_2
        | knows_weapon_master_1
        | knows_ironflesh_1
        | knows_wound_treatment_1
        | knows_athletics_2
        | knows_first_aid_1
        | knows_leadership_1,
        0x0000000BFF003440209B6E38E06DBEFF00000000001F36E10000000000000000,
    ],
    [
        "npc3_2",
        "Evel Droby",
        "Evel Droby",
        tf_female | tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_leather_jerkin,
            itm_sword_medieval_b_small,
            itm_hunter,
        ],
        str_24 | agi_13 | int_11 | cha_6 | level(14),
        wp(20),
        knows_merchant_npc
        | knows_wound_treatment_1
        | knows_trade_1
        | knows_first_aid_3
        | knows_surgery_1
        | knows_athletics_1
        | knows_riding_1,
        0x00000004A204300436DB6DB6DB6DFEFF00000000001DB6DB0000000000000000,
    ],
    [
        "npc4_2",
        "Ilhan",
        "Ilhan",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_eyeslot_kettlehat_a_v2,
            itm_leather_gloves_a,
            itm_studded_leather_coat,
            itm_sword_medieval_c,
            itm_tab_shield_heater_c,
            itm_hunter,
        ],
        str_20 | agi_13 | int_13 | cha_10 | level(27),
        wp(110),
        knows_warrior_npc
        | knows_weapon_master_2
        | knows_power_strike_2
        | knows_riding_2
        | knows_athletics_2
        | knows_power_throw_2
        | knows_first_aid_1
        | knows_surgery_1
        | knows_tactics_2
        | knows_leadership_2,
        0x0000000B7D00130020DB6DB6DB6DBEFF00000000001DB6E80000000000000000,
    ],
    [
        "npc5_2",
        "Gyliam Gare",
        "Gyliam Gare",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_sword_khergit_2,
            itm_tab_shield_small_round_b,
            itm_leather_steppe_cap_b,
            itm_tribal_warrior_outfit,
            itm_steppe_horse,
        ],
        str_18 | agi_13 | int_12 | cha_7 | level(23),
        wp(90),
        knows_warrior_npc
        | knows_riding_2
        | knows_horse_archery_3
        | knows_power_draw_3
        | knows_leadership_2
        | knows_weapon_master_1,
        0x0000000DFF00115420DB6DB6DB6DBEFF00000000001DB6E80000000000000000,
    ],
    [
        "npc6_2",
        "Ames",
        "Ames",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_bastard_sword_a,
            itm_mail_coif,
            itm_mail_with_tunic_red,
            itm_sumpter_horse,
        ],
        str_20 | agi_19 | int_10 | cha_5 | level(25),
        wp(105),
        knows_warrior_npc
        | knows_riding_2
        | knows_weapon_master_2
        | knows_power_strike_2
        | knows_athletics_3
        | knows_trainer_1
        | knows_leadership_1,
        0x0000000D401001CF20DB6DB6DB6DFEFF00000000001DB6D00000000000000000,
    ],
    [
        "npc7_2",
        "Malia Willey",
        "Malia Willey",
        tf_female | tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_voulge,
            itm_short_bow,
            itm_barbed_arrows,
            itm_leather_gloves_a,
            itm_studded_leather_coat,
            itm_arabian_horse_b,
        ],
        str_16 | agi_13 | int_10 | cha_6 | level(17),
        wp(80),
        knows_tracker_npc
        | knows_tracking_2
        | knows_athletics_2
        | knows_spotting_1
        | knows_pathfinding_1
        | knows_power_draw_2,
        0x000000031F08000206D86DB64B4DB6DB00000000001DB6C30000000000000000,
    ],
    [
        "npc8_2",
        "Eryet Allard",
        "Eryet Allard",
        tf_female | tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [itm_sword_viking_2, itm_mail_coif, itm_gray_hauberk_a, itm_courser],
        str_18 | agi_15 | int_9 | cha_10 | level(26),
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
        "npc9_2",
        "Aduhash",
        "Aduhash",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_sword_medieval_c,
            itm_leather_vest_regular_shirt_a,
            itm_courser,
        ],
        str_22 | agi_19 | int_7 | cha_8 | level(17),
        wp(100),
        knows_warrior_npc
        | knows_weapon_master_1
        | knows_riding_1
        | knows_athletics_1
        | knows_leadership_1
        | knows_tactics_1
        | knows_power_strike_1,
        0x00000001900471C6125B69FCDB6DBEFF00000000001DB6FB0000000000000000,
    ],
    [
        "npc10_2",
        "Zela",
        "Zela",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_military_sickle_a,
            itm_heavy_crossbow,
            itm_bolts,
            itm_mail_coif,
            itm_leather_gloves_a,
            itm_aketon_green,
            itm_saddle_horse,
        ],
        str_24 | agi_19 | int_9 | cha_11 | level(27),
        wp(105),
        knows_warrior_npc
        | knows_weapon_master_3
        | knows_tactics_1
        | knows_leadership_1
        | knows_ironflesh_3
        | knows_trainer_2
        | knows_first_aid_2,
        0x0000000190042348058365C91C7D8EFF00000000001DE6FB0000000000000000,
    ],
    [
        "npc11_2",
        "Jane",
        "Jane",
        tf_female | tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_hatchet_b,
            itm_arming_cap_a,
            itm_leather_gloves_a,
            itm_padded_cloth,
            itm_sumpter_horse,
        ],
        str_16 | agi_17 | int_10 | cha_10 | level(26),
        wp(70),
        knows_merchant_npc
        | knows_weapon_master_1
        | knows_first_aid_1
        | knows_wound_treatment_2
        | knows_ironflesh_3
        | knows_inventory_management_5,
        0x00000006000C000206186196918DB8E400000000001D48C40000000000000000,
    ],
    [
        "npc12_2",
        "Pai Khoi-Kao",
        "Pai Khoi-Kao",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_iron_staff,
            itm_padded_coif_a,
            itm_leather_gloves_a,
            itm_pilgrim_disguise,
            itm_sumpter_horse,
        ],
        str_16 | agi_17 | int_13 | cha_7 | level(20),
        wp(30),
        knows_merchant_npc
        | knows_ironflesh_1
        | knows_power_strike_1
        | knows_surgery_4
        | knows_wound_treatment_3
        | knows_first_aid_3,
        0x00000001BF044383201D6A24DA6DBCFF00000000001DB6F80000000000000000,
    ],
    [
        "npc13_2",
        "Dondo",
        "Dondo",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_scimitar,
            itm_tab_shield_small_round_b,
            itm_courser,
        ],
        str_14 | agi_17 | int_12 | cha_8 | level(19),
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
        "npc14_2",
        "Elrel",
        "Elrel",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_sword_medieval_b,
            itm_tab_shield_heater_c,
            itm_mail_coif,
            itm_studded_leather_coat,
            itm_courser,
        ],
        str_18 | agi_19 | int_11 | cha_8 | level(23),
        wp(100),
        knows_warrior_npc
        | knows_trainer_4
        | knows_weapon_master_3
        | knows_leadership_2
        | knows_power_strike_1,
        0x00000001BE00024545136DC11B79FCDB00000000001DB6E80000000000000000,
    ],
    [
        "npc15_2",
        "Phamas",
        "Phamas",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_long_axe,
            itm_sallet_a_v5,
            itm_leather_gloves_a,
            itm_red_gambeson,
            itm_hunter,
        ],
        str_18 | agi_13 | int_12 | cha_8 | level(25),
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
        "npc16_2",
        "Kina",
        "Kina",
        tf_female | tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_sword_viking_2_small,
            itm_light_throwing_axes,
            itm_sallet_a_v5,
            itm_leather_gloves_a,
            itm_leather_jerkin,
            itm_saddle_horse,
        ],
        str_14 | agi_17 | int_8 | cha_7 | level(17),
        wp(80),
        knows_tracker_npc
        | knows_power_throw_3
        | knows_athletics_2
        | knows_power_strike_1,
        0x00000000000C3001009849A2494288CB00000000001DA6830000000000000000,
    ],
    # tier 3
    [
        "npc1_3",
        "Hurey",
        "Hurey",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_khergit_war_helmet,
            itm_lamellar_vest_khergit,
            itm_sword_medieval_c_small,
            itm_courser,
        ],
        str_16 | agi_17 | int_12 | cha_7 | level(14),
        wp(60),
        knows_tracker_npc
        | knows_ironflesh_1
        | knows_power_strike_1
        | knows_pathfinding_3
        | knows_athletics_2
        | knows_tracking_1
        | knows_riding_2,  # skills 2/3 player at that level
        0x0000000E730065C420DB6DB6DB6DDEFF00000000001DB6F00000000000000000,
    ],
    [
        "npc2_3",
        "Mesym",
        "Mesym",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_leather_gloves_a,
            itm_gray_hauberk_a,
            itm_mace_3,
            itm_tab_shield_small_round_b,
            itm_saddle_horse,
        ],
        str_14 | agi_17 | int_11 | cha_6 | level(14),
        wp(40),
        knows_merchant_npc
        | knows_trade_2
        | knows_weapon_master_1
        | knows_ironflesh_1
        | knows_wound_treatment_1
        | knows_athletics_2
        | knows_first_aid_1
        | knows_leadership_1,
        0x0000000BFF003440209B6E38E06DBEFF00000000001F36E10000000000000000,
    ],
    [
        "npc3_3",
        "Evel Droby",
        "Evel Droby",
        tf_female | tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_cervelliere_a,
            itm_leather_gloves_a,
            itm_sword_medieval_c_small,
            itm_hunter,
        ],
        str_24 | agi_13 | int_11 | cha_6 | level(14),
        wp(20),
        knows_merchant_npc
        | knows_wound_treatment_1
        | knows_trade_1
        | knows_first_aid_3
        | knows_surgery_1
        | knows_athletics_1
        | knows_riding_1,
        0x00000004A204300436DB6DB6DB6DFEFF00000000001DB6DB0000000000000000,
    ],
    [
        "npc4_3",
        "Ilhan",
        "Ilhan",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_sallet_b,
            itm_leather_gloves_a,
            itm_sword_medieval_c_long,
            itm_tab_shield_heater_c,
            itm_hunter,
        ],
        str_20 | agi_13 | int_13 | cha_10 | level(27),
        wp(110),
        knows_warrior_npc
        | knows_weapon_master_2
        | knows_power_strike_2
        | knows_riding_2
        | knows_athletics_2
        | knows_power_throw_2
        | knows_first_aid_1
        | knows_surgery_1
        | knows_tactics_2
        | knows_leadership_2,
        0x0000000B7D00130020DB6DB6DB6DBEFF00000000001DB6E80000000000000000,
    ],
    [
        "npc5_3",
        "Gyliam Gare",
        "Gyliam Gare",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_scimitar,
            itm_tab_shield_small_round_c,
            itm_khergit_cavalry_helmet,
            itm_leather_gloves_a,
            itm_lamellar_vest,
            itm_steppe_horse,
        ],
        str_18 | agi_13 | int_12 | cha_7 | level(23),
        wp(90),
        knows_warrior_npc
        | knows_riding_2
        | knows_horse_archery_3
        | knows_power_draw_3
        | knows_leadership_2
        | knows_weapon_master_1,
        0x0000000DFF00115420DB6DB6DB6DBEFF00000000001DB6E80000000000000000,
    ],
    [
        "npc6_3",
        "Ames",
        "Ames",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_bastard_sword_b,
            itm_flat_top_b_v1,
            itm_mail_mittens_a,
            itm_olive_hauberk_a_v1,
            itm_sumpter_horse,
        ],
        str_20 | agi_19 | int_10 | cha_5 | level(25),
        wp(105),
        knows_warrior_npc
        | knows_riding_2
        | knows_weapon_master_2
        | knows_power_strike_2
        | knows_athletics_3
        | knows_trainer_1
        | knows_leadership_1,
        0x0000000D401001CF20DB6DB6DB6DFEFF00000000001DB6D00000000000000000,
    ],
    [
        "npc7_3",
        "Malia Willey",
        "Malia Willey",
        tf_female | tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_long_bardiche,
            itm_strong_bow,
            itm_barbed_arrows,
            itm_mail_coif,
            itm_leather_gloves_a,
            itm_white_hauberk_a,
            itm_arabian_horse_b,
        ],
        str_16 | agi_13 | int_10 | cha_6 | level(17),
        wp(80),
        knows_tracker_npc
        | knows_tracking_2
        | knows_athletics_2
        | knows_spotting_1
        | knows_pathfinding_1
        | knows_power_draw_2,
        0x000000031F08000206D86DB64B4DB6DB00000000001DB6C30000000000000000,
    ],
    [
        "npc8_3",
        "Eryet Allard",
        "Eryet Allard",
        tf_female | tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_battle_axe,
            itm_leather_gloves_a,
            itm_white_hauberk_a,
            itm_courser,
        ],
        str_18 | agi_15 | int_9 | cha_10 | level(26),
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
        "npc9_3",
        "Aduhash",
        "Aduhash",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_sword_medieval_c_long,
            itm_leather_gloves_a,
            itm_lamellar_vest,
            itm_courser,
        ],
        str_22 | agi_19 | int_7 | cha_8 | level(17),
        wp(100),
        knows_warrior_npc
        | knows_weapon_master_1
        | knows_riding_1
        | knows_athletics_1
        | knows_leadership_1
        | knows_tactics_1
        | knows_power_strike_1,
        0x00000001900471C6125B69FCDB6DBEFF00000000001DB6FB0000000000000000,
    ],
    [
        "npc10_3",
        "Zela",
        "Zela",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_military_pick,
            itm_heavy_crossbow,
            itm_steel_bolts,
            itm_eyeslot_kettlehat_a_v2,
            itm_leather_gloves_a,
            itm_mail_with_tunic_green,
            itm_saddle_horse,
        ],
        str_24 | agi_19 | int_9 | cha_11 | level(27),
        wp(105),
        knows_warrior_npc
        | knows_weapon_master_3
        | knows_tactics_1
        | knows_leadership_1
        | knows_ironflesh_3
        | knows_trainer_2
        | knows_first_aid_2,
        0x0000000190042348058365C91C7D8EFF00000000001DE6FB0000000000000000,
    ],
    [
        "npc11_3",
        "Jane",
        "Jane",
        tf_female | tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_hatchet_b_v1,
            itm_arming_cap_a,
            itm_leather_gloves_a,
            itm_sumpter_horse,
        ],
        str_16 | agi_17 | int_10 | cha_10 | level(26),
        wp(70),
        knows_merchant_npc
        | knows_weapon_master_1
        | knows_first_aid_1
        | knows_wound_treatment_2
        | knows_ironflesh_3
        | knows_inventory_management_5,
        0x00000006000C000206186196918DB8E400000000001D48C40000000000000000,
    ],
    [
        "npc12_3",
        "Pai Khoi-Kao",
        "Pai Khoi-Kao",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_iron_staff,
            itm_mail_coif,
            itm_mail_mittens_a,
            itm_pilgrim_disguise,
            itm_sumpter_horse,
        ],
        str_16 | agi_17 | int_13 | cha_7 | level(20),
        wp(30),
        knows_merchant_npc
        | knows_ironflesh_1
        | knows_power_strike_1
        | knows_surgery_4
        | knows_wound_treatment_3
        | knows_first_aid_3,
        0x00000001BF044383201D6A24DA6DBCFF00000000001DB6F80000000000000000,
    ],
    [
        "npc13_3",
        "Dondo",
        "Dondo",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_scimitar,
            itm_tab_shield_small_round_c,
            itm_courser,
        ],
        str_14 | agi_17 | int_12 | cha_8 | level(19),
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
        "npc14_3",
        "Elrel",
        "Elrel",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_sword_medieval_c,
            itm_tab_shield_heater_c,
            itm_sallet_b,
            itm_leather_gloves_a,
            itm_courser,
        ],
        str_18 | agi_19 | int_11 | cha_8 | level(23),
        wp(100),
        knows_warrior_npc
        | knows_trainer_4
        | knows_weapon_master_3
        | knows_leadership_2
        | knows_power_strike_1,
        0x00000001BE00024545136DC11B79FCDB00000000001DB6E80000000000000000,
    ],
    [
        "npc15_3",
        "Phamas",
        "Phamas",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_long_axe_b,
            itm_sallet_c,
            itm_mail_mittens_a,
            itm_olive_hauberk_a_v1,
            itm_hunter,
        ],
        str_18 | agi_13 | int_12 | cha_8 | level(25),
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
        "npc16_3",
        "Kina",
        "Kina",
        tf_female | tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_sword_viking_2_small,
            itm_throwing_axes,
            itm_leather_gloves_a,
            itm_lamellar_vest,
            itm_saddle_horse,
        ],
        str_14 | agi_17 | int_8 | cha_7 | level(17),
        wp(80),
        knows_tracker_npc
        | knows_power_throw_3
        | knows_athletics_2
        | knows_power_strike_1,
        0x00000000000C3001009849A2494288CB00000000001DA6830000000000000000,
    ],
    # tier 4
    [
        "npc1_4",
        "Hurey",
        "Hurey",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_khergit_guard_helmet,
            itm_khergit_guard_armor,
            itm_sword_viking_3_small,
            itm_courser,
        ],
        str_16 | agi_17 | int_12 | cha_7 | level(14),
        wp(60),
        knows_tracker_npc
        | knows_ironflesh_1
        | knows_power_strike_1
        | knows_pathfinding_3
        | knows_athletics_2
        | knows_tracking_1
        | knows_riding_2,  # skills 2/3 player at that level
        0x0000000E730065C420DB6DB6DB6DDEFF00000000001DB6F00000000000000000,
    ],
    [
        "npc2_4",
        "Mesym",
        "Mesym",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_mail_coif,
            itm_mail_mittens_a,
            itm_white_hauberk_a,
            itm_mace_4,
            itm_tab_shield_small_round_c,
            itm_saddle_horse,
        ],
        str_14 | agi_17 | int_11 | cha_6 | level(14),
        wp(40),
        knows_merchant_npc
        | knows_trade_2
        | knows_weapon_master_1
        | knows_ironflesh_1
        | knows_wound_treatment_1
        | knows_athletics_2
        | knows_first_aid_1
        | knows_leadership_1,
        0x0000000BFF003440209B6E38E06DBEFF00000000001F36E10000000000000000,
    ],
    [
        "npc3_4",
        "Evel Droby",
        "Evel Droby",
        tf_female | tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_sallet_c,
            itm_plate_gauntlets_a_v1,
            itm_full_plate_armor_a,
            itm_sword_viking_3_small,
            itm_hunter,
        ],
        str_24 | agi_13 | int_11 | cha_6 | level(14),
        wp(20),
        knows_merchant_npc
        | knows_wound_treatment_1
        | knows_trade_1
        | knows_first_aid_3
        | knows_surgery_1
        | knows_athletics_1
        | knows_riding_1,
        0x00000004A204300436DB6DB6DB6DFEFF00000000001DB6DB0000000000000000,
    ],
    [
        "npc4_4",
        "Ilhan",
        "Ilhan",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_m_bascinet_b,
            itm_heraldic_mail_with_tabard,
            itm_sword_medieval_d_long,
            itm_tab_shield_heater_d,
            itm_hunter,
        ],
        str_20 | agi_13 | int_13 | cha_10 | level(27),
        wp(110),
        knows_warrior_npc
        | knows_weapon_master_2
        | knows_power_strike_2
        | knows_riding_2
        | knows_athletics_2
        | knows_power_throw_2
        | knows_first_aid_1
        | knows_surgery_1
        | knows_tactics_2
        | knows_leadership_2,
        0x0000000B7D00130020DB6DB6DB6DBEFF00000000001DB6E80000000000000000,
    ],
    [
        "npc5_4",
        "Gyliam Gare",
        "Gyliam Gare",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_scimitar_b,
            itm_tab_shield_small_round_c,
            itm_khergit_guard_helmet,
            itm_steppe_horse,
        ],
        str_18 | agi_13 | int_12 | cha_7 | level(23),
        wp(90),
        knows_warrior_npc
        | knows_riding_2
        | knows_horse_archery_3
        | knows_power_draw_3
        | knows_leadership_2
        | knows_weapon_master_1,
        0x0000000DFF00115420DB6DB6DB6DBEFF00000000001DB6E80000000000000000,
    ],
    [
        "npc6_4",
        "Ames",
        "Ames",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_sword_great_a,
            itm_sallet_a,
            itm_plate_gauntlets_a_v1,
            itm_cuir_bouilli,
            itm_sumpter_horse,
        ],
        str_20 | agi_19 | int_10 | cha_5 | level(25),
        wp(105),
        knows_warrior_npc
        | knows_riding_2
        | knows_weapon_master_2
        | knows_power_strike_2
        | knows_athletics_3
        | knows_trainer_1
        | knows_leadership_1,
        0x0000000D401001CF20DB6DB6DB6DFEFF00000000001DB6D00000000000000000,
    ],
    [
        "npc7_4",
        "Malia Willey",
        "Malia Willey",
        tf_female | tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_great_long_bardiche,
            itm_war_bow,
            itm_khergit_arrows,
            itm_heraldic_mail_with_tabard,
            itm_arabian_horse_b,
        ],
        str_16 | agi_13 | int_10 | cha_6 | level(17),
        wp(80),
        knows_tracker_npc
        | knows_tracking_2
        | knows_athletics_2
        | knows_spotting_1
        | knows_pathfinding_1
        | knows_power_draw_2,
        0x000000031F08000206D86DB64B4DB6DB00000000001DB6C30000000000000000,
    ],
    [
        "npc8_4",
        "Eryet Allard",
        "Eryet Allard",
        tf_female | tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_great_axe,
            itm_mail_mittens_a,
            itm_banded_armor,
            itm_courser,
        ],
        str_18 | agi_15 | int_9 | cha_10 | level(26),
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
        "npc9_4",
        "Aduhash",
        "Aduhash",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_bastard_sword_b,
            itm_banded_armor,
            itm_courser,
        ],
        str_22 | agi_19 | int_7 | cha_8 | level(17),
        wp(100),
        knows_warrior_npc
        | knows_weapon_master_1
        | knows_riding_1
        | knows_athletics_1
        | knows_leadership_1
        | knows_tactics_1
        | knows_power_strike_1,
        0x00000001900471C6125B69FCDB6DBEFF00000000001DB6FB0000000000000000,
    ],
    [
        "npc10_4",
        "Zela",
        "Zela",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_military_pick,
            itm_sniper_crossbow,
            itm_steel_bolts,
            itm_m_bascinet_b,
            itm_mail_mittens_a,
            itm_saddle_horse,
        ],
        str_24 | agi_19 | int_9 | cha_11 | level(27),
        wp(105),
        knows_warrior_npc
        | knows_weapon_master_3
        | knows_tactics_1
        | knows_leadership_1
        | knows_ironflesh_3
        | knows_trainer_2
        | knows_first_aid_2,
        0x0000000190042348058365C91C7D8EFF00000000001DE6FB0000000000000000,
    ],
    [
        "npc11_4",
        "Jane",
        "Jane",
        tf_female | tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_hatchet_a,
            itm_great_helmet,
            itm_plate_gauntlets_a_v1,
            itm_sumpter_horse,
        ],
        str_16 | agi_17 | int_10 | cha_10 | level(26),
        wp(70),
        knows_merchant_npc
        | knows_weapon_master_1
        | knows_first_aid_1
        | knows_wound_treatment_2
        | knows_ironflesh_3
        | knows_inventory_management_5,
        0x00000006000C000206186196918DB8E400000000001D48C40000000000000000,
    ],
    [
        "npc12_4",
        "Pai Khoi-Kao",
        "Pai Khoi-Kao",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_iron_staff,
            itm_eyeslot_kettlehat_a_v2,
            itm_plate_gauntlets_a_v1,
            itm_sumpter_horse,
        ],
        str_16 | agi_17 | int_13 | cha_7 | level(20),
        wp(30),
        knows_merchant_npc
        | knows_ironflesh_1
        | knows_power_strike_1
        | knows_surgery_4
        | knows_wound_treatment_3
        | knows_first_aid_3,
        0x00000001BF044383201D6A24DA6DBCFF00000000001DB6F80000000000000000,
    ],
    [
        "npc13_4",
        "Dondo",
        "Dondo",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_scimitar_b,
            itm_tab_shield_small_round_c,
            itm_courser,
        ],
        str_14 | agi_17 | int_12 | cha_8 | level(19),
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
        "npc14_4",
        "Elrel",
        "Elrel",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_sword_medieval_d_long,
            itm_tab_shield_heater_d,
            itm_great_helmet,
            itm_plate_gauntlets_a_v1,
            itm_heraldic_mail_with_surcoat,
            itm_courser,
        ],
        str_18 | agi_19 | int_11 | cha_8 | level(23),
        wp(100),
        knows_warrior_npc
        | knows_trainer_4
        | knows_weapon_master_3
        | knows_leadership_2
        | knows_power_strike_1,
        0x00000001BE00024545136DC11B79FCDB00000000001DB6E80000000000000000,
    ],
    [
        "npc15_4",
        "Phamas",
        "Phamas",
        tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_long_axe_c,
            itm_m_bascinet_b,
            itm_heraldic_mail_with_surcoat,
            itm_hunter,
        ],
        str_18 | agi_13 | int_12 | cha_8 | level(25),
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
        "npc16_4",
        "Kina",
        "Kina",
        tf_female | tf_hero | tf_unmoveable_in_party_window,
        0,
        reserved,
        fac_commoners,
        [
            itm_sword_viking_3_small,
            itm_heavy_throwing_axes,
            itm_saddle_horse,
        ],
        str_14 | agi_17 | int_8 | cha_7 | level(17),
        wp(80),
        knows_tracker_npc
        | knows_power_throw_3
        | knows_athletics_2
        | knows_power_strike_1,
        0x00000000000C3001009849A2494288CB00000000001DA6830000000000000000,
    ],
    [
        "coop_companion_equipment_ui_0",
        "{!}multiplayer_end",
        "{!}multiplayer_end",
        0,
        0,
        0,
        fac_kingdom_5,
        [],
        0,
        0,
        0,
        0,
        0,
    ],
    [
        "coop_companion_equipment_ui_0_f",
        "{!}multiplayer_end",
        "{!}multiplayer_end",
        tf_female,
        0,
        0,
        fac_kingdom_5,
        [],
        0,
        0,
        0,
        0,
        0,
    ],
    [
        "coop_companion_equipment_ui_1",
        "{!}multiplayer_end",
        "{!}multiplayer_end",
        0,
        0,
        0,
        fac_kingdom_5,
        [],
        0,
        0,
        0,
        0,
        0,
    ],
    [
        "coop_companion_equipment_ui_1_f",
        "{!}multiplayer_end",
        "{!}multiplayer_end",
        tf_female,
        0,
        0,
        fac_kingdom_5,
        [],
        0,
        0,
        0,
        0,
        0,
    ],
    [
        "coop_companion_equipment_sets_end",
        "{!}multiplayer_end",
        "{!}multiplayer_end",
        0,
        0,
        0,
        fac_kingdom_5,
        [],
        0,
        0,
        0,
        0,
        0,
    ],
    ##diplomacy begin
    # SB : fixed plural name (hero name), TODO actually use name/gender in hiring dialogues
    [
        "dplmc_chamberlain",
        "Chamberlain Aubrey de Vere",
        "Aubrey de Vere",
        tf_hero | tf_male,
        0,
        0,
        fac_commoners,
        [itm_tabard_f],
        def_attrib | level(10),
        wp(40),
        knows_inventory_management_10,
        0x0000000DFC0C238838E571C8D469C91B00000000001E39230000000000000000,
    ],
    [
        "dplmc_constable",
        "Constable Miles de Gloucester",
        "Miles de Gloucester",
        tf_hero | tf_male,
        0,
        0,
        fac_commoners,
        [itm_dplmc_coat_of_plates_red_constable],
        knight_attrib_4,
        wp_melee(200),
        knows_common
        | knows_shield_3
        | knows_ironflesh_3
        | knows_power_strike_4
        | knows_athletics_4,
        0x0000000B4B1015054B1B4D591CBA28D300000000001E472B0000000000000000,
    ],
    [
        "dplmc_chancellor",
        "Chancellor Herfast",
        "Herfast",
        tf_hero | tf_male,
        0,
        0,
        fac_commoners,
        [itm_tabard_f],
        def_attrib | level(10),
        wp(40),
        knows_inventory_management_10,
        0x00000009A20C21CF491BAD28A28628D400000000001E371A0000000000000000,
    ],
    [
        "dplmc_messenger",
        "Messenger",
        "Messengers",
        tf_mounted
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_gloves
        | tf_guarantee_horse
        | tf_guarantee_ranged,
        0,
        0,
        fac_neutral,
        [
            itm_sword_medieval_a,
            itm_leather_jerkin,
            itm_courser,
            itm_leather_gloves_a,
            itm_light_crossbow,
            itm_bolts,
        ],
        def_attrib | agi_21 | int_30 | cha_21 | level(25),
        wp(130),
        knows_common | knows_riding_7 | knows_horse_archery_5 | knows_leadership_7,
        man_face_young_1,
        man_face_old_2,
    ],
    [
        "dplmc_scout",
        "Scout",
        "Scouts",
        tf_mounted
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_gloves
        | tf_guarantee_horse
        | tf_guarantee_ranged,
        0,
        0,
        fac_neutral,
        [
            itm_sword_medieval_a,
            itm_leather_jerkin,
            itm_courser,
            itm_leather_gloves_a,
            itm_light_crossbow,
            itm_bolts,
        ],
        def_attrib | agi_21 | int_30 | cha_21 | level(25),
        wp(130),
        knows_common | knows_riding_7 | knows_horse_archery_5 | knows_leadership_7,
        man_face_young_1,
        man_face_old_2,
    ],
    # recruiter kit begin
    [
        "dplmc_recruiter",
        "Recruiter",
        "Recruiter",
        tf_mounted
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_gloves
        | tf_guarantee_horse
        | tf_guarantee_ranged,
        0,
        0,
        fac_neutral,
        [
            itm_sword_medieval_a,
            itm_leather_jerkin,
            itm_courser,
            itm_leather_gloves_a,
            itm_light_crossbow,
            itm_bolts,
        ],
        def_attrib | agi_21 | int_30 | cha_21 | level(25),
        wp(130),
        knows_common | knows_riding_7 | knows_horse_archery_5 | knows_leadership_7,
        swadian_face_young_1,
        swadian_face_old_2,
    ],
    # recruiter kit end
    ##diplomacy end
]
