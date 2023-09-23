####################################################################################################################
#  Each quest record contains the following fields:
#  1) Info page id: used for referencing info pages in other files. The prefix ip_ is automatically added before each info page id.
#  2) Info page name: Name displayed in the info page screen.
#
####################################################################################################################
##diplomacy start+
from module_constants import DPLMC_DIPLOMACY_VERSION_STRING
##diplomacy end+

info_pages = [
##diplomacy start+
("dplmc_info", "Diplomacy Mod", "The Diplomacy mod adds some features to the game.  Most of them are accessed via your minister and several new potential employees: a chamberlain, a constable, and a chancellor.  You gain the opportunity to hire a chamberlain when you get your first village, a constable when you gain your first castle, and a chancellor when you gain your first town.  If you dismiss one of your employees, you may be able to rehire them through a well-connected spouse or one of the travellers who frequent the taverns of Calradia.^^Aside from these the mod has other features as well, which can be accessed from the Camp menu.^^This mod uses Diplomacy Version "+DPLMC_DIPLOMACY_VERSION_STRING+"."),
("dplmc_autoloot", "Autoloot", "Autoloot settings are managed through the camp menu.  It allows you to have your companions (named heroes, not ordinary soldiers) automatically select equipment from the loot after a battle.  In order for this feature to be enabled, one of the following must be true: someone in your party must have a Looting score of 2 or better, someone in your party must have an Inventory Management score of 3 or better, or the player himself must have an Inventory Management score of 2 or better."),
("dplmc_autosell", "Autosell", "The Autosell feature allows you to sell many items to a merchant all at once, instead of selling them one at a time.  Autosell settings are managed through the Town menu, where you can specify which types of items you want to be able to sell (e.g. you might not want to automatically sell horses) and a price limit (for example, you might not want to automatically sell any items that cost more than 200 denars).^^ There are two primary ways to use autosell.  If you speak to a Horse Merchant, Armorer, or Weapon Merchant in a town, there is a conversation option to sell items of a particular type.  Also, when visiting a town there will be an option in the Marketplace section of the menu to automatically sell your items throughout the town.^^ For people who used Autosell in other mods, note that this sells from your own inventory, according to certain rules.  Items you have equipped will never be sold, and neither will the first three items in your inventory.  After that, autosell also skips anything that it thinks might be your personal equipment (since people often have more than one set).  Regardless of whether you have them equipped, it won't sell your best bow, crossbow, armor, helmet, boots, or gloves.  If you have a bow you can use, it won't sell your best three packs of arrows, and if you have a crossbow it won't sell your best three packs of bolts.  For shields, one-handed weapons, two-handed weapons, polearms, and horses, it won't sell your best or second-best item.  Your best three throwing weapons also will not be sold.  However, items that your character is unable to use are considered fair game."),
##diplomacy end+
 ("morale", "Morale", "Morale represents the ability and willingness of the troops in a party to summon up the endurance, bravery, and discipline they need to face the stresses of battle and the march. It is not the same thing as the troops' happiness. Elite troops may grumble and whine about the hardships of campaigning -- but then stand together as one when the arrows start to fly. On the other hand, a commander who gives his men everything they want may find that they grow soft, and waiver before the enemy's charge.^^ Morale's greatest impact is on a party's behavior in battle, determining how aggressively troops engage the enemy, and how likely they are to break and run if they perceive the tide of battle turning against them. Morale also affects a party's march speed, as a less motivated party will move more slowly, as the men are not pushing themselves to their physical limit, and pause more frequently, as it waits for stragglers to catch up. Finally, a party with very low morale will start to suffer desertions.^^ Some factors that affect morale are intuitive. For example, a charismatic commander with a reputation for winning battles can infuse his or her men with a sense of confidence. Leaders who give their men well ample and varied supplies of food, and pay them on time, demonstrate that they care about their troops' welfare, and are less likely to lead them into disaster.^^ Other factors are less intuitive -- particularly those related to a party's sense of group cohesion. In a small tight-knit party, for example, men will often fight hard against daunting odds to avoid showing cowardice before their comrades-in-arms. A large party on the other hand may see its cohesion strained, as the commander has less time to supervise the men, listen to their grievances, and resolve their disputes. Frequent battles will strengthen the bonds between men, while long periods without combat will see the troops become bored and quarrelsome.^^ The morale report, accessibly by hitting the 'reports' button will give the player a sense of the factors affecting his or her men's morale."),
 ("economy", "Economy", "Towns and villages in Calradia need a wide variety of goods for their populations to remain healthy and productive. First in importance is food. Grain is the staple crop of Calradia, but people also need fat and protein in the form of meat, fish, or cheese. It takes almost as much work to preserve meat as to produce it in the first place, so salt is also in high demand. After food comes clothing: heavy wool, lighter linens, or luxurious velvet. Finally, people need the tools of their trade: ironware, pottery, leatherware, and, of course, arms, armor, and horses for war.^^Most agricultural products are produced in the villages, while artisans in the towns specialize in manufactured or artisanal goods like fabrics or ironware. Also, different resources can be found in different parts of the country. Consequently, the key to prosperity in Calradia is trade -- both between the villages and the towns, and between the major towns themselves.^^When trade flows, goods will be available and affordable, the population of a center will be healthy and energetic, and migrants will flock from the nearby regions. The center will produce more, consume more, and be able to contribute more in taxes to their lords. When trade dries up, towns and villages will see their workers flee to seek work elsewhere, and economic activity will drift to a stand-still. Thus, it is in the interests of rulers to protect trade routes from the hazards of war and banditry. A smart merchant, however, may want to seek out towns which have become isolated from the rest of the land, as he or she may be able to turn a tidy profit from the resulting price imbalances.^^Because villagers usually plan to take their goods to market in towns, village markets will be rather quiet places, and villagers will buy cheap and sell dear. Serious merchants will stick to the towns to make a profit, although some parties may decide to make a quick stop in a village to acquire supplies.^^A player who wants to know about the factors affecting a region's prosperity can speak to the guildmaster of the local town. Other information can be gleaned from passers-by, although they might not know very much outside of their own particular trade."),
 ("courtship", "Courtship", "Players may wish to marry into one of Calradia's noble families. Marriage is not necessary for a player to rise in power and stature, but it does provide players with an opportunity to improve their relation with lords and establish a claim to the throne.^^Marriage requirements will be different for males and females. A male character will usually need to pursue a traditional path of courtship. He should establish a reputation in Calradian aristocratic society, get on good terms with his bride's parents or guardians, and then woo the lady according to local custom. If a player grows impatient, he may attempt to take a shortcut -- but there will be consequences in his relations with other lords.^^A male character should keep in mind that other lords will be competing with him for the affections of the kingdom's ladies. Also, a lady's tastes are unpredictable, and a player may also find that the object of his love does not love him in return. Romance, in Calradia as elsewhere, does not always prosper. Of course, a player may resort to other, less gentlemanly means of winning a lady's heart, but again, that will have a serious impact on his reputation.^^To get started on the path of courtship, a male player should try to get involved in the social life of the Calradian aristocracy, attending feasts and tournaments. Also, wandering troubadours and poets can serve as a useful repository of information on courtship, and keep the player up to date about the latest gossip.^^Female characters can also marry -- but they should keep in mind that Calradian society is very traditional, and, as adventurers, they have chosen a very unconventional path for a woman. A female character may have to look for a while to find a lord who is open-minded enough to marry her.^^On the bright side, a female character does not have to go through the elaborate rituals of courtship, and she also may gain more from a marriage than her male counterpart. For a woman adventurer, marriage can be a quick path to power -- and an unscrupulous character may be able to use her husband as a tool of her political ambitions."),
 ("politics", "Politics", "The realms of Calradia, although they represent different cultures, all adhere to the same basic political system: feudalism. Feudalism is based on the relationships between individuals: the oaths of loyalty given by a vassal to his or her liege. In exchange for this oath, the vassal will usually receive a fief, a parcel of land whose income will be used by the vassal to raise troops to support the liege in time of war. A liege also has an obligation to protect his vassals, and to treat them justly.^^This is how it works in theory, anyway. In practice, vassals will not always work in their factions' interests, particular as they are often quarreling with one another. Nobles have different personalities, and sometimes those personalities clash. Or, perhaps two nobles were once friends, but fell out over in the aftermath of a setback or a defeat -- or because they both were wooing the same lady. Jealousies will also surface as they vie for the favor of the king -- perhaps over newly conquered lands, or over who will be given the coveted office of marshal, the lord in charge of organizing large-scale campaigns.^^When one realm in Calradia makes war on another, the political unity of the each kingdom is as important as the quality or number of its soldiers in determining the outcome. In a cohesive kingdom, nobles will join together in a large force to sweep their opponents before them. In a kingdom divided by petty quarrels, lords will fail to respond to the marshal's summons, or drift away to attend to their own business if a campaign is not going well. A faction's political cohesion will also impact warfare when campaigns are not in progress. In a divided faction, lords will be less likely to join together on raids and patrols, and come to each other's defense.^^If it seems self-defeating for nobles to bicker and quarrel when the enemy is just over the horizon, keep this in mind -- ultimately, a noble's loyalty goes not to a particular faction or culture, but to himself and to his family. If a noble fears that his faction is collapsing, or if he is being neglected by his liege, he can usually find a reason to withdraw his oath of allegiance, and change sides. Players should keep this in mind, as they may find that there are opportunities to turn discontented former enemies into allies."),
 ("character_backgrounds", "Character_Backgrounds", "A player character in Calradia may choose to come from a variety of social backgrounds. This choice will affect not just his or her starting skills and equipment, but also the course of his or her career as an adventurer.^^War and politics in Calradia are traditionally dominated by male aristocrats. A nobleman player character may find that he is invited into this 'old boys' club' fairly quickly, but women and commoners may face a few extra hurdles on the way. If you choose to start the game as a male nobleman, you can think of it as the 'easy' setting. Starting as a noblewoman or a male commoner is somewhat more difficult, and starting as a female commoner is probably the most challenging way to begin a game.^^However, women have some starting advantages. Simply by taking up arms, a female warrior will draw attention to herself, and she may find that she can build up her reputation faster than a male. Also, it is traditionally easier for a woman to marry up the social ladder than it is for a man, and a woman may find she can gain more from a strategic marital alliance than her male counterpart.^^Finally, keep in mind that the game does not place any limits on the upward mobility of characters based on their background. Noble or common, male or female, married or unmarried -- anyone can rise to become ruler of all Calradia, if they are sufficiently brave, lucky, or resourceful."),
 ("military_campaigns", "Military Campaigns", "When kingdoms in Calradia go to war, their armies have two basic offensive options. They can try to attack villages and lay waste to the countryside, damaging their enemy's prestige and economy. Or, they can try to seize and hold castles or towns, taking territory This second option can involve long, bloody sieges, but will yield more decisive results.^^It is important to note that the realms of Calradia do not field standing armies, which remain in the field as long as the ruler desires. Rather, Calradian realms are protected by feudal levies comprised of the major nobles and their individual retinues.  Sometimes, these nobles launch their own private attacks into enemy territory, but the most decisive events will usually take place when the great hosts are assembled. The kingdom's marshal, a noble appointed by the king, will summon the host before the campaign and lead them out to battle. However, he should be careful not to keep them in the field too long. Otherwise, the host will begin to disintegrate, as the vassals drift off to pursue their own business, and the army will be vulnerable to a counter-attack.^^For this reason, the rhythm of wars in Calradia often resemble the rhythm of a duel between two individual combatants. One side will gather its strength and seek to land a blow against the enemy's territory. If the marshal spends too little time gathering the vassals, he may not be able to do any real damage. If he spends too much time, then the campaign may end before it has even begun. A large realm will have an advantage over a smaller one, just as a brawny combatant has an edge over a smaller foe, but a realm's political cohesion can also be a factor, just as a fighter with great stamina can outlast her opponent. Sometimes, the armies of two realms will meet head on, resulting in a major battle in which both numbers and morale will decide the outcome.^^Kingdoms will have imperfect intelligence about their enemies. Attacking lords will need to frequently scout enemy territory to determine which fortresses may be vulnerable. An army defending its homeland will benefit from the alarms raised by castles and towns, which broadcast intelligence about enemy movements in the area. Such intelligence will be imprecise, however, particularly when it comes to numbers. A defending force which sets out to raise a siege or rescue a village may be able to overwhelm an unprepared attacker -- or it may miscalculate, and find that it is the one to be overwhelmed. Attackers, in turn, must be careful how far they advance into enemy territory, with aggressive marshals venturing further than cautious ones.^^Players will be expected to join in their faction's military campaign, either by joining the host, or by scouting ahead into enemy territory. Some players may find that their realm's marshal is too cautious, or too aggressive, for their tastes. In this case, they can intrigue with other lords to try to replace the marshal, or build support to become the marshal themselves.^^Most wars are of limited duration. A king who goes to war will, for the sake of honor, feel obligated to pursue the conflict for a short while. However, unless he is soundly beating his enemy. he may soon start looking for a way out of the conflict, lest he leave himself vulnerable to an attack by a third party. Calradia's rulers are keenly aware that today's ally may be tomorrow's enemy, and vice versa."),
]

# modmerger_start version=201 type=2
try:
    component_name = "info_pages"
    var_set = { "info_pages" : info_pages }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end
