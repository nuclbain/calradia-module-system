from module_troops_utils import *

troops_manhunters = [
    # SLAVE TRADERS BEGIN
    [
        "manhunter",
        "Manhunter",
        "Manhunters",
        tf_mounted
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet
        | tf_guarantee_horse
        | tf_guarantee_shield,
        0,
        0,
        fac_manhunters,
        [
            itm_mace_3,
            itm_winged_mace,
            itm_eyeslot_kettlehat_a_v1,
            itm_padded_cloth,
            itm_aketon_green,
            itm_aketon_green,
            itm_wooden_shield,
            itm_leather_boots_a,
            itm_sumpter_horse,
        ],
        def_attrib | level(10),
        wp(50),
        knows_common,
        bandit_face1,
        bandit_face2,
    ],
    [
        "slave_driver",
        "Slave Driver",
        "Slave Drivers",
        tf_mounted
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet
        | tf_guarantee_horse,
        0,
        0,
        fac_slavers,
        [
            itm_club_with_spike_head,
            itm_sallet_c,
            itm_tribal_warrior_outfit,
            itm_nordic_shield,
            itm_leather_gloves_a,
            itm_leather_boots_a,
            itm_steppe_horse,
        ],
        def_attrib | level(14),
        wp(80),
        knows_common,
        bandit_face1,
        bandit_face2,
    ],
    [
        "slave_hunter",
        "Slave Hunter",
        "Slave Hunters",
        tf_mounted
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet
        | tf_guarantee_horse
        | tf_guarantee_shield,
        0,
        0,
        fac_slavers,
        [
            itm_winged_mace,
            itm_maul,
            itm_eyeslot_kettlehat_a_v2,
            itm_tab_shield_round_c,
            itm_leather_gloves_a,
            itm_leather_boots_a,
            itm_mail_boots_a,
            itm_courser,
        ],
        def_attrib | level(18),
        wp(90),
        knows_common,
        bandit_face1,
        bandit_face2,
    ],
    [
        "slave_crusher",
        "Slave Crusher",
        "Slave Crushers",
        tf_mounted
        | tf_guarantee_boots
        | tf_guarantee_armor
        | tf_guarantee_helmet
        | tf_guarantee_horse
        | tf_guarantee_shield,
        0,
        0,
        fac_slavers,
        [
            itm_sledgehammer,
            itm_spiked_mace,
            itm_white_hauberk_a,
            itm_sallet_b,
            itm_sallet_c,
            itm_mail_mittens_a,
            itm_tab_shield_round_d,
            itm_leather_boots_a,
            itm_mail_boots_a,
            itm_hunter,
        ],
        def_attrib | level(22),
        wp(110),
        knows_common | knows_riding_4 | knows_power_strike_3,
        bandit_face1,
        bandit_face2,
    ],
    [
        "slaver_chief",
        "Slaver Chief",
        "Slaver Chiefs",
        tf_mounted | tf_guarantee_all_wo_ranged,
        0,
        0,
        fac_slavers,
        [
            itm_military_hammer,
            itm_steel_shield,
            itm_mail_mittens_a,
            itm_sallet_c,
            itm_plate_boots_b,
            itm_warhorse,
        ],
        def_attrib | level(26),
        wp(130),
        knows_common | knows_riding_4 | knows_power_strike_5,
        bandit_face1,
        bandit_face2,
    ],
    # SLAVE TRADERS END
]
