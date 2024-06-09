import string

from module_info import *
from module_troops import *

from process_common import *

# from process_operations import *

num_face_numeric_keys = 4

def save_troops():
    file = open(export_dir + "troops.txt", "w")
    file.write("troopsfile version 2\n")
    file.write("%d " % len(troops))
    for troop in troops:
        troop_len = len(troop)
        if troop_len == 11:
            troop[11:11] = [0, 0, 0, 0, 0]
        elif troop_len == 12:
            troop[12:12] = [0, 0, 0, 0]
        elif troop_len == 13:
            troop[13:13] = [0, 0, 0]
        elif troop_len == 14:
            troop[14:14] = [0, 0]
        elif troop_len == 15:
            troop[15:15] = [0]
        if troop[4] > 0:
            id_no = find_object(troops, convert_to_identifier(troop[0]))

        file.write(
            "\ntrp_%s %s %s %s %d %d %d %d %d %d\n  "
            % (
                convert_to_identifier(troop[0]),
                replace_spaces(troop[1]),
                replace_spaces(troop[2]),
                replace_spaces(str(troop[13])),
                troop[3],
                troop[4],
                troop[5],
                troop[6],
                troop[14],
                troop[15],
            )
        )
        inventory_list = troop[7]
        for inventory_item in inventory_list:
            if(type(inventory_item) == types.ListType) or (type(inventory_item) == types.TupleType):
              file.write("%d %d "%(inventory_item[0], inventory_item[1]<<24))
            else:
              file.write("%d 0 "%inventory_item)
        for i in xrange(64 - len(inventory_list)):
            file.write("-1 0 ")
        file.write("\n ")
        attrib = troop[8]
        strength = attrib & 0xFF
        agility = (attrib >> 8) & 0xFF
        intelligence = (attrib >> 16) & 0xFF
        charisma = (attrib >> 24) & 0xFF
        starting_level = (attrib >> level_bits) & level_mask

        file.write(
            " %d %d %d %d %d\n"
            % (strength, agility, intelligence, charisma, starting_level)
        )
        wp_word = troop[9]
        for wp in xrange(num_weapon_proficiencies):
            wp_level = wp_word & 0x3FF
            file.write(" %d" % wp_level)
            wp_word = wp_word >> 10
        file.write("\n")

        skill_array = troop[10]
        for i in xrange(num_skill_words):
            file.write("%d " % ((skill_array >> (i * 32)) & 0xFFFFFFFF))
        file.write("\n  ")

        face_keys = [troop[11], troop[12]]

        for fckey in face_keys:
            word_keys = []
            for word_no in xrange(num_face_numeric_keys):
                word_keys.append((fckey >> (64 * word_no)) & 0xFFFFFFFFFFFFFFFF)
            for word_no in xrange(num_face_numeric_keys):
                file.write("%d " % (word_keys[(num_face_numeric_keys - 1) - word_no]))

        file.write("\n")
    file.close()

def two_to_pow(x):
    result = 1
    for i in xrange(x):
        result = result * 2
    return result

def save_python_header():
    file = open("./ID_troops.py", "w")
    for i_troop in xrange(len(troops)):
        file.write(
            "trp_%s = %d\n" % (convert_to_identifier(troops[i_troop][0]), i_troop)
        )
    file.close()

print("Exporting troops data")
save_python_header()
save_troops()
