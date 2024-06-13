from module_troops_utils import *

troops_walkers = [
    # This troop is the troop marked as soldiers_end and town_walkers_begin
    # TOWN WALKERS BEGIN
    [
        "town_walker_1",
        "Townsman",
        "Townsmen",
        tf_guarantee_boots | tf_guarantee_armor,
        0,
        0,
        fac_commoners,
        [
            itm_short_tunic,
            itm_linen_tunic,
            itm_fur_coat,
            itm_coarse_tunic,
            itm_tabard_a,
            itm_leather_vest,
            itm_arena_tunic_white,
            itm_leather_apron,
            itm_shirt,
            itm_arena_tunic_green,
            itm_arena_tunic_blue,
            itm_fur_hat,
            itm_leather_cap,
            itm_straw_hat,
            itm_felt_hat,
            itm_hose_b,
            itm_hose_d,
            itm_poulaines_b,
            itm_poulaines_d,
        ],
        def_attrib | level(4),
        wp(60),
        knows_common,
        man_face_young_1,
        man_face_old_2,
    ],
    [
        "town_walker_2",
        "Townswoman",
        "Townswomen",
        tf_female | tf_guarantee_boots | tf_guarantee_armor,
        0,
        0,
        fac_commoners,
        [
            itm_blue_dress,
            itm_dress,
            itm_woolen_dress,
            itm_peasant_dress,
            itm_wimple_a,
            itm_wimple_with_veil,
            itm_female_hood,
            itm_hose_b,
            itm_hose_d,
            itm_poulaines_b,
            itm_poulaines_d,
        ],
        def_attrib | level(2),
        wp(40),
        knows_common,
        woman_face_1,
        woman_face_2,
    ],
    [
        "khergit_townsman",
        "Townsman",
        "Townsmen",
        tf_guarantee_boots | tf_guarantee_armor,
        0,
        0,
        fac_kingdom_6,
        [
            itm_solarian_turban_a,
            itm_solarian_turban_b,
            itm_solarian_robe_a,
            itm_solarian_aketon_a,
            itm_hose_b,
            itm_hose_d,
            itm_poulaines_b,
            itm_poulaines_d,
        ],
        def_attrib | level(4),
        wp(60),
        knows_common,
        swadian_face_younger_1,
        swadian_face_middle_2,
    ],
    [
        "khergit_townswoman",
        "Townswoman",
        "Townswomen",
        tf_female | tf_guarantee_boots | tf_guarantee_armor,
        0,
        0,
        fac_commoners,
        [
            itm_blue_dress,
            itm_dress,
            itm_woolen_dress,
            itm_peasant_dress,
            itm_wimple_a,
            itm_wimple_with_veil,
            itm_female_hood,
            itm_hose_b,
            itm_hose_d,
            itm_poulaines_b,
            itm_poulaines_d,
        ],
        def_attrib | level(2),
        wp(40),
        knows_common,
        woman_face_1,
        woman_face_2,
    ],
    [
        "sarranid_townsman",
        "Townsman",
        "Townsmen",
        tf_guarantee_boots | tf_guarantee_armor,
        0,
        0,
        fac_kingdom_6,
        [
            itm_solarian_turban_a,
            itm_solarian_turban_b,
            itm_solarian_robe_a,
            itm_solarian_aketon_a,
            itm_hose_b,
            itm_hose_d,
            itm_poulaines_b,
            itm_poulaines_d,
        ],
        def_attrib | level(4),
        wp(60),
        knows_common,
        swadian_face_younger_1,
        swadian_face_middle_2,
    ],
    [
        "sarranid_townswoman",
        "Townswoman",
        "Townswomen",
        tf_female | tf_guarantee_boots | tf_guarantee_armor,
        0,
        0,
        fac_commoners,
        [
            itm_sarranid_common_dress,
            itm_sarranid_common_dress_b,
            itm_sarranid_felt_head_cloth,
            itm_sarranid_felt_head_cloth_b,
            itm_hose_b,
            itm_hose_d,
            itm_poulaines_b,
            itm_poulaines_d,
        ],
        def_attrib | level(2),
        wp(40),
        knows_common,
        woman_face_1,
        woman_face_2,
    ],
    # TOWN WALKERS END
    # This troop is the troop marked as town_walkers_end and village_walkers_begin
    # VILLAGE WALKERS BEGIN
    [
        "village_walker_1",
        "Villager",
        "Villagers",
        tf_guarantee_boots | tf_guarantee_armor,
        0,
        0,
        fac_commoners,
        [
            itm_short_tunic,
            itm_linen_tunic,
            itm_coarse_tunic,
            itm_leather_vest,
            itm_leather_apron,
            itm_shirt,
            itm_fur_hat,
            itm_leather_cap,
            itm_straw_hat,
            itm_felt_hat,
            itm_hose_b,
            itm_hose_d,
            itm_poulaines_b,
            itm_poulaines_d,
        ],
        def_attrib | level(4),
        wp(60),
        knows_common,
        man_face_younger_1,
        man_face_older_2,
    ],
    [
        "village_walker_2",
        "Villager",
        "Villagers",
        tf_female | tf_guarantee_boots | tf_guarantee_armor,
        0,
        0,
        fac_commoners,
        [
            itm_blue_dress,
            itm_dress,
            itm_woolen_dress,
            itm_peasant_dress,
            itm_wimple_a,
            itm_wimple_with_veil,
            itm_female_hood,
            itm_hose_b,
            itm_hose_d,
            itm_poulaines_b,
            itm_poulaines_d,
        ],
        def_attrib | level(2),
        wp(40),
        knows_common,
        woman_face_1,
        woman_face_2,
    ],
    # VILLAGE WALKERS END
    # This troop is the troop marked as village_walkers_end and spy_walkers_begin
    # SPY WALKERS BEGIN
    [
        "spy_walker_1",
        "Townsman",
        "Townsmen",
        tf_guarantee_boots | tf_guarantee_armor | tf_guarantee_helmet,
        0,
        0,
        fac_commoners,
        [
            itm_short_tunic,
            itm_linen_tunic,
            itm_coarse_tunic,
            itm_tabard_a,
            itm_leather_vest,
            itm_robe,
            itm_leather_apron,
            itm_shirt,
            itm_fur_hat,
            itm_leather_cap,
            itm_straw_hat,
            itm_felt_hat,
            itm_hose_b,
            itm_hose_d,
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
        "spy_walker_2",
        "Townswoman",
        "Townswomen",
        tf_female | tf_guarantee_boots | tf_guarantee_armor | tf_guarantee_helmet,
        0,
        0,
        fac_commoners,
        [
            itm_blue_dress,
            itm_dress,
            itm_woolen_dress,
            itm_peasant_dress,
            itm_wimple_a,
            itm_wimple_with_veil,
            itm_female_hood,
            itm_hose_b,
            itm_hose_d,
            itm_poulaines_b,
            itm_poulaines_d,
        ],
        def_attrib | level(2),
        wp(40),
        knows_common,
        woman_face_1,
        woman_face_2,
    ],
    # SPY WALKERS END
    # BEGGARS BEGIN
    [
        "beggar_male",
        "Beggar",
        "Beggars",
        tf_guarantee_boots | tf_guarantee_armor,
        0,
        0,
        fac_commoners,
        [itm_robe, itm_pilgrim_disguise, itm_pilgrim_hood, itm_sandals_a],
        def_attrib | level(4),
        wp(60),
        knows_common,
        swadian_face_younger_1,
        swadian_face_middle_2,
    ],
    [
        "beggar_female",
        "Beggar",
        "Beggars",
        tf_female | tf_guarantee_boots | tf_guarantee_armor,
        0,
        0,
        fac_commoners,
        [itm_robe, itm_pilgrim_disguise, itm_pilgrim_hood, itm_sandals_a],
        def_attrib | level(4),
        wp(60),
        knows_common,
        woman_face_1,
        woman_face_2,
    ],
    # BEGGARS END
]
