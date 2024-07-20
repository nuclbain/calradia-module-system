from module_troops_utils import *

troops_tutorial = [
    [
        "tournament_master",
        "Tournament Master",
        "Tournament Master",
        tf_hero,
        scn_zendar_center | entry(1),
        reserved,
        fac_commoners,
        [itm_leather_boots_a, itm_nomad_armor],
        def_attrib | level(2),
        wp(20),
        knows_common,
        0x000000000008414401E28F534C8A2D09,
    ],
    [
        "trainer",
        "Trainer",
        "Trainer",
        tf_hero,
        scn_zendar_center | entry(2),
        reserved,
        fac_commoners,
        [itm_leather_boots_a, itm_leather_jerkin],
        def_attrib | level(2),
        wp(20),
        knows_common,
        0x00000000000430C701EA98836781647F,
    ],
    [
        "Constable_Hareck",
        "Constable Hareck",
        "Constable Hareck",
        tf_hero,
        scn_zendar_center | entry(5),
        reserved,
        fac_commoners,
        [itm_leather_boots_a, itm_regular_shirt_c],
        def_attrib | level(5),
        wp(20),
        knows_common,
        0x00000000000C41C001FB15234EB6DD3F,
    ],
    # Ryan BEGIN
    [
        "Ramun_the_slave_trader",
        "Ramun, the slave trader",
        "Ramun, the slave trader",
        tf_hero,
        no_scene,
        reserved,
        fac_commoners,
        [itm_leather_boots_a, itm_regular_shirt_c],
        def_attrib | level(5),
        wp(20),
        knows_common,
        0x0000000FD5105592385281C55B8E44EB00000000001D9B220000000000000000,
    ],
    [
        "guide",
        "Quick Jimmy",
        "Quick Jimmy",
        tf_hero,
        no_scene,
        0,
        fac_commoners,
        [itm_leather_boots_a, itm_regular_shirt_b],
        def_attrib | level(2),
        wp(20),
        knows_inventory_management_10,
        0x00000000000C318301F24E38A36E38E3,
    ],
    # Ryan END
    [
        "Xerina",
        "Xerina",
        "Xerina",
        tf_hero | tf_female,
        scn_the_happy_boar | entry(5),
        reserved,
        fac_commoners,
        [itm_leather_boots_a, itm_leather_jerkin],
        def_attrib | str_15 | agi_15 | level(39),
        wp(312),
        knows_power_strike_5
        | knows_ironflesh_5
        | knows_riding_6
        | knows_power_draw_4
        | knows_athletics_8
        | knows_shield_3,
        0x00000001AC0820074920561D0B51E6ED00000000001D40ED0000000000000000,
    ],
    [
        "Dranton",
        "Dranton",
        "Dranton",
        tf_hero,
        scn_the_happy_boar | entry(2),
        reserved,
        fac_commoners,
        [itm_leather_boots_a, itm_leather_vest_regular_shirt_a],
        def_attrib | str_15 | agi_14 | level(42),
        wp(324),
        knows_power_strike_5
        | knows_ironflesh_7
        | knows_riding_4
        | knows_power_draw_4
        | knows_athletics_4
        | knows_shield_3,
        0x0000000A460C3002470C50F3502879F800000000001CE0A00000000000000000,
    ],
    [
        "Kradus",
        "Kradus",
        "Kradus",
        tf_hero,
        scn_the_happy_boar | entry(3),
        reserved,
        fac_commoners,
        [itm_leather_boots_a, itm_padded_leather],
        def_attrib | str_15 | agi_14 | level(43),
        wp(270),
        knows_power_strike_5
        | knows_ironflesh_7
        | knows_riding_4
        | knows_power_draw_4
        | knows_athletics_4
        | knows_shield_3,
        0x0000000F5B1052C61CE1A9521DB1375200000000001ED31B0000000000000000,
    ],
    # Tutorial
    [
        "tutorial_trainer",
        "Training Ground Master",
        "Training Ground Master",
        tf_hero,
        0,
        0,
        fac_commoners,
        [itm_robe, itm_leather_boots_a],
        def_attrib | level(2),
        wp(20),
        knows_common,
        0x000000000008414401E28F534C8A2D09,
    ],
    [
        "tutorial_student_1",
        "{!}tutorial_student_1",
        "{!}tutorial_student_1",
        tf_guarantee_boots | tf_guarantee_armor,
        0,
        0,
        fac_neutral,
        [
            itm_leather_boots_a,
            itm_practice_sword,
            itm_practice_shield,
            itm_leather_jerkin,
            itm_padded_leather,
            itm_leather_armor,
            itm_padded_coif_a,
        ],
        def_attrib | level(2),
        wp(20),
        knows_common,
        swadian_face_young_1,
        swadian_face_old_2,
    ],
    [
        "tutorial_student_2",
        "{!}tutorial_student_2",
        "{!}tutorial_student_2",
        tf_guarantee_boots | tf_guarantee_armor,
        0,
        0,
        fac_neutral,
        [
            itm_leather_boots_a,
            itm_practice_sword,
            itm_practice_shield,
            itm_leather_jerkin,
            itm_padded_leather,
            itm_leather_armor,
            itm_padded_coif_a,
        ],
        def_attrib | level(2),
        wp(20),
        knows_common,
        swadian_face_young_1,
        swadian_face_old_2,
    ],
    [
        "tutorial_student_3",
        "{!}tutorial_student_3",
        "{!}tutorial_student_3",
        tf_guarantee_boots | tf_guarantee_armor,
        0,
        0,
        fac_neutral,
        [
            itm_leather_boots_a,
            itm_practice_staff,
            itm_leather_jerkin,
            itm_padded_leather,
            itm_leather_armor,
            itm_padded_coif_a,
        ],
        def_attrib | level(2),
        wp(20),
        knows_common,
        swadian_face_young_1,
        swadian_face_old_2,
    ],
    [
        "tutorial_student_4",
        "{!}tutorial_student_4",
        "{!}tutorial_student_4",
        tf_guarantee_boots | tf_guarantee_armor,
        0,
        0,
        fac_neutral,
        [
            itm_leather_boots_a,
            itm_practice_staff,
            itm_leather_jerkin,
            itm_padded_leather,
            itm_leather_armor,
            itm_padded_coif_a,
        ],
        def_attrib | level(2),
        wp(20),
        knows_common,
        swadian_face_young_1,
        swadian_face_old_2,
    ],
    # Sargoth
    # halkard, hardawk. lord_taucard lord_caupard. lord_paugard
    # Salt mine
    [
        "Galeas",
        "Galeas",
        "Galeas",
        tf_hero,
        0,
        reserved,
        fac_commoners,
        [itm_leather_boots_a, itm_regular_shirt_c],
        def_attrib | level(5),
        wp(20),
        knows_common,
        0x000000000004718201C073191A9BB10C,
    ],
    # Dhorak keep
    [
        "farmer_from_bandit_village",
        "Farmer",
        "Farmers",
        tf_guarantee_armor,
        no_scene,
        reserved,
        fac_commoners,
        [
            itm_leather_boots_a,
            itm_regular_shirt_b,
            itm_regular_shirt_b,
            itm_regular_shirt_a,
        ],
        def_attrib | level(4),
        wp(60),
        knows_common,
        man_face_middle_1,
        man_face_older_2,
    ],
    [
        "trainer_1",
        "Trainer",
        "Trainer",
        tf_hero,
        scn_training_ground_ranged_melee_1 | entry(6),
        reserved,
        fac_commoners,
        [itm_leather_boots_a, itm_leather_jerkin],
        def_attrib | level(2),
        wp(20),
        knows_common,
        0x0000000D0D1030C74AE8D661B651C6840000000000000E220000000000000000,
    ],
    [
        "trainer_2",
        "Trainer",
        "Trainer",
        tf_hero,
        scn_training_ground_ranged_melee_2 | entry(6),
        reserved,
        fac_commoners,
        [itm_leather_boots_a, itm_nomad_vest],
        def_attrib | level(2),
        wp(20),
        knows_common,
        0x0000000E5A04360428EC253846640B5D0000000000000EE80000000000000000,
    ],
    [
        "trainer_3",
        "Trainer",
        "Trainer",
        tf_hero,
        scn_training_ground_ranged_melee_3 | entry(6),
        reserved,
        fac_commoners,
        [itm_leather_boots_a, itm_padded_leather],
        def_attrib | level(2),
        wp(20),
        knows_common,
        0x0000000E4A0445822CA1A11AB1E9EAEA0000000000000F510000000000000000,
    ],
    [
        "trainer_4",
        "Trainer",
        "Trainer",
        tf_hero,
        scn_training_ground_ranged_melee_4 | entry(6),
        reserved,
        fac_commoners,
        [itm_leather_boots_a, itm_leather_jerkin],
        def_attrib | level(2),
        wp(20),
        knows_common,
        0x0000000E600452C32EF8E5BB92CF1C970000000000000FC20000000000000000,
    ],
    [
        "trainer_5",
        "Trainer",
        "Trainer",
        tf_hero,
        scn_training_ground_ranged_melee_5 | entry(6),
        reserved,
        fac_commoners,
        [itm_leather_boots_a, itm_leather_vest_regular_shirt_a],
        def_attrib | level(2),
        wp(20),
        knows_common,
        0x0000000E77082000150049A34C42EC960000000000000E080000000000000000,
    ],
]
