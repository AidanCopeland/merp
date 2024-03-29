#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Imports character secondary skills information from JSON and stores it in a key, value format.

Functions:
    init_secondary_skills(secondary_skills_json_object)
"""
import string
import sys
from collections import OrderedDict
import trace_log as trace

sys.path.append('../../')

SKILL_ACTING = "Acting"
JSON_ACTING = "acting"
SKILL_ADMINISTRATION = "Administration"
JSON_ADMINISTRATION = "administration"
SKILL_ADRENAL_CONCENTRATION = "Adrenal Concentration"
JSON_ADRENAL_CONCENTRATION = "adrenal-concentration"
SKILL_ADVERTISING = "Advertising"
JSON_ADVERTISING = "advertising"
SKILL_ALCHEMY = "Alchemy"
JSON_ALCHEMY = "alchemy"
SKILL_ALERTNESS = "Alertness"
JSON_ALERTNESS = "alertness"
SKILL_ANIMAL_HANDLING = "Animal Handling"
JSON_ANIMAL_HANDLING = "animal-handling"
SKILL_ANIMAL_HEALING = "Animal Healing"
JSON_ANIMAL_HEALING = "animal-healing"
SKILL_ANIMAL_HUSBANDRY = "Animal Husbandry"
JSON_ANIMAL_HUSBANDRY = "animal-husbandry"
SKILL_ANIMAL_TRAINING = "Animal Training"
JSON_ANIMAL_TRAINING = "animal-training"
SKILL_ANTHROPOLOGY = "Anthropology"
JSON_ANTHROPOLOGY = "anthropology"
SKILL_APPRAISAL = "Appraisal"
JSON_APPRAISAL = "appraisal"
SKILL_ARCHITECTURE = "Architecture"
JSON_ARCHITECTURE = "architecture"
SKILL_ASTRONOMY = "Astronomy"
JSON_ASTRONOMY = "astronomy"
SKILL_ATHLETIC_GAMES = "Athletic Games"
JSON_ATHLETIC_GAMES = "athletic-games"
SKILL_BEAST_MASTERY = "Beast Mastery"
JSON_BEAST_MASTERY = "beast-mastery"
SKILL_BEGGING = "Begging"
JSON_BEGGING = "begging"
SKILL_BIOCHEMISTRY = "Biochemistry"
JSON_BIOCHEMISTRY = "biochemistry"
SKILL_BOAT_PILOT = "Boat Pilot"
JSON_BOAT_PILOT = "boat-pilot"
SKILL_CARTOGRAPHY = "Cartography"
JSON_CARTOGRAPHY = "cartography"
SKILL_CLEANSING_TRANCE = "Cleansing Trance"
JSON_CLEANSING_TRANCE = "cleansing-trance"
SKILL_CONTROL_LYCANTHROPY = "Control Lycanthropy"
JSON_CONTROL_LYCANTHROPY = "control-lycanthropy"
SKILL_CONTACTING_SECONDARY = "Contacting"
JSON_CONTACTING_SECONDARY = "contacting"
SKILL_CONTORTIONS = "Contortions"
JSON_CONTORTIONS = "contortions"
SKILL_COOKING = "Cooking"
JSON_COOKING = "cooking"
SKILL_CULTURE = "Culture"
SKILL_CULTURE_WILD = "Culture*"
JSON_CULTURE = "culture"
SKILL_DANCING = "Dancing"
JSON_DANCING = "dancing"
SKILL_DEATH_TRANCE = "Death Trance"
JSON_DEATH_TRANCE = "death-trance"
SKILL_DEMON_DEVIL_LORE = "Demon/Devil Lore"
JSON_DEMON_DEVIL_LORE = "demon-devil-lore"
SKILL_DETECT_TRAPS = "Detect Traps"
JSON_DETECT_TRAPS = "detect-traps"
SKILL_DIAGNOSTICS = "Diagnostics"
JSON_DIAGNOSTICS = "diagnostics"
SKILL_DIPLOMACY_SECONDARY = "Diplomacy"
JSON_DIPLOMACY_SECONDARY = "diplomacy"
SKILL_DISCERN_WOUNDS = "Discern Wounds"
JSON_DISCERN_WOUNDS = "discern-wounds"
SKILL_DISTANCE_RUNNING = "Distance Running"
JSON_DISTANCE_RUNNING = "distance-running"
SKILL_DOWSING = "Dowsing"
JSON_DOWSING = "dowsing"
SKILL_DROWSING = "Drowsing"
JSON_DROWSING = "drowsing"
SKILL_DRAGON_LORE = "Dragon Lore"
JSON_DRAGON_LORE = "dragon-lore"
SKILL_DREAM_LORE = "Dream Lore"
JSON_DREAM_LORE = "dream-lore"
SKILL_DRAFTING = "Drafting"
JSON_DRAFTING = "drafting"
SKILL_DRIVING = "Driving"
JSON_DRIVING = "driving"
SKILL_DRUG_TOLERANCE = "Drug Tolerance"
JSON_DRUG_TOLERANCE = "drug-tolerance"
SKILL_ENGINEERING = "Engineering"
JSON_ENGINEERING = "engineering"
SKILL_EVALUATE_ARMOUR = "Evaluate Armour"
JSON_EVALUATE_ARMOUR = "evaluate-armour"
SKILL_EVALUATE_METAL = "Evaluate Metal"
JSON_EVALUATE_METAL = "evaluate-metal"
SKILL_EVALUATE_STONE = "Evaluate Stone"
JSON_EVALUATE_STONE = "evaluate-stone"
SKILL_EVALUATE_WEAPON = "Evaluate Weapon"
JSON_EVALUATE_WEAPON = "evaluate-weapon"
SKILL_FAERIE_LORE = "Faerie Lore"
JSON_FAERIE_LORE = "faerie-lore"
SKILL_FAUNA_LORE = "Fauna Lore"
SKILL_FAUNA_LORE_WILD = "Fauna Lore*"
JSON_FAUNA_LORE = "fauna-lore"
SKILL_FIRST_AID = "First Aid"
JSON_FIRST_AID = "first-aid"
SKILL_FLETCHING = "Fletching"
JSON_FLETCHING = "fletching"
SKILL_FLORA_LORE = "Flora Lore"
SKILL_FLORA_LORE_WILD = "Flora Lore*"
JSON_FLORA_LORE = "flora-lore"
SKILL_GAMBLING = "Gambling"
JSON_GAMBLING = "gambling"
SKILL_GIMMICKRY = "Gimmickry"
JSON_GIMMICKRY = "gimmickry"
SKILL_HEALING_TRANCE = "Healing Trance"
JSON_HEALING_TRANCE = "healing-trance"
SKILL_HERALDRY = "Heraldry"
SKILL_HERALDRY_WILD = "Heraldry*"
JSON_HERALDRY = "heraldry"
SKILL_HERDING = "Herding"
JSON_HERDING = "herding"
SKILL_HISTORY = "History"
SKILL_HISTORY_WILD = "History*"
JSON_HISTORY = "history"
SKILL_HORTICULTURE = "Horticulture"
JSON_HORTICULTURE = "horticulture"
SKILL_HYPNOSIS = "Hypnosis"
JSON_HYPNOSIS = "hypnosis"
SKILL_JUGGLING = "Juggling"
JSON_JUGGLING = "juggling"
SKILL_JUMPING = "Jumping"
JSON_JUMPING = "jumping"
SKILL_LEADERSHIP_SECONDARY = "Leadership"
JSON_LEADERSHIP_SECONDARY = "leadership"
SKILL_LEATHER_CRAFTS = "Leather-crafts"
JSON_LEATHER_CRAFTS = "leather-crafts"
SKILL_LOCATE_HIDDEN = "Locate Hidden"
JSON_LOCATE_HIDDEN = "locate-hidden"
SKILL_MAPPING = "Mapping"
JSON_MAPPING = "mapping"
SKILL_MATHS = "Maths"
JSON_MATHS = "maths"
SKILL_MECHANITION = "Mechanition"
JSON_MECHANITION = "mechanition"
SKILL_MEDITATION = "Meditation"
JSON_MEDITATION = "Meditation"
SKILL_METAL_CRAFTS = "Metal-crafts"
JSON_METAL_CRAFTS = "metal-crafts"
SKILL_METAL_LORE = "Metal Lore"
JSON_METAL_LORE = "metal-lore"
SKILL_MIDWIFERY = "Midwifery"
JSON_MIDWIFERY = "midwifery"
SKILL_MILITARY_ORGANISATION = "Military Organisation"
JSON_MILITARY_ORGANISATION = "military-organisation"
SKILL_MIMERY = "Mimery"
JSON_MIMERY = "mimery"
SKILL_MIMICRY = "Mimicry"
JSON_MIMICRY = "mimicry"
SKILL_MINGLING = "Mingling"
JSON_MINGLING = "mingling"
SKILL_MINING = "Mining"
JSON_MINING = "mining"
SKILL_MNEMONICS = "Mnemonics"
JSON_MNEMONICS = "mnemonics"
SKILL_MUSIC = "Music"
JSON_MUSIC = "music"
SKILL_OBSERVATION = "Observation"
JSON_OBSERVATION = "observation"
SKILL_OPERATING_EQUIPMENT = "Operating Equipment"
JSON_OPERATING_EQUIPMENT = "operating-equipment"
SKILL_ORIENTEERING = "Orienteering"
JSON_ORIENTEERING = "orienteering"
SKILL_PAINTING = "Painting"
JSON_PAINTING = "painting"
SKILL_PERCEPTION = "Perception"
JSON_PERCEPTION = "perception"
SKILL_PHILOSOPHY = "Philosophy"
JSON_PHILOSOPHY = "philosophy"
SKILL_PLAY_INSTRUMENT = "Play Instrument"
JSON_PLAY_INSTRUMENT = "play-instrument"
SKILL_POETIC_IMPROVISATION = "Poetic Improvisation"
JSON_POETIC_IMPROVISATION = "poetic-improvisation"
SKILL_POETRY = "Poetry"
JSON_POETRY = "poetry"
SKILL_POISON_TOLERANCE = "Poison Tolerance"
JSON_POISON_TOLERANCE = "poison-tolerance"
SKILL_PROPAGANDA = "Propaganda"
JSON_PROPAGANDA = "propaganda"
SKILL_PSYCHOLOGY = "Psychology"
JSON_PSYCHOLOGY = "psychology"
SKILL_PUBLIC_SPEAKING_SECONDARY = "Public Speaking"
JSON_PUBLIC_SPEAKING_SECONDARY = "public-speaking"
SKILL_REGION_LORE = "Region Lore"
SKILL_REGION_LORE_WILD = "Region Lore*"
JSON_REGION_LORE = "region-lore"
SKILL_RELIGION = "Religion"
JSON_RELIGION = "religion"
SKILL_ROPE_MASTERY = "Rope Mastery"
JSON_ROPE_MASTERY = "rope-mastery"
SKILL_SCIENTIFIC_RESEARCH = "Scientific Research"
JSON_SCIENTIFIC_RESEARCH = "scientific-research"
SKILL_SCRIBING = "Scribing"
JSON_SCRIBING = "scribing"
SKILL_SCROUNGING = "Scrounging"
JSON_SCROUNGING = "scrounging"
SKILL_SCULPTING = "Sculpting"
JSON_SCULPTING = "sculpting"
SKILL_SECOND_AID = "Second Aid"
JSON_SECOND_AID = "second-aid"
SKILL_SEDUCTION = "Seduction"
JSON_SEDUCTION = "seduction"
SKILL_SENSE_AMBUSH = "Sense Ambush"
JSON_SENSE_AMBUSH = "sense-ambush"
SKILL_SERVICE = "Service"
JSON_SERVICE = "service"
SKILL_SEWING_WEAVING = "Sewing/Weaving"
JSON_SEWING_WEAVING = "sewing-weaving"
SKILL_SIEGE_ENGINEERING = "Siege Engineering"
JSON_SIEGE_ENGINEERING = "siege-engineering"
SKILL_SINGING = "Singing"
JSON_SINGING = "singing"
SKILL_SITUATIONAL_AWARENESS = "Situational Awareness"
JSON_SITUATIONAL_AWARENESS = "situational-awareness"
SKILL_SKATING = "Skating"
JSON_SKATING = "skating"
SKILL_SKINNING = "Skinning"
JSON_SKINNING = "skinning"
SKILL_SLEEP_TRANCE = "Sleep Trance"
JSON_SLEEP_TRANCE = "sleep-trace"
SKILL_SMITHING = "Smithing"
JSON_SMITHING = "smithing"
SKILL_BLINDFIGHTING_SECONDARY = "Blindfighting/SLA"
JSON_BLINDFIGHTING_SECONDARY = "blindfighting"
SKILL_SPRINTING = "Sprinting"
JSON_SPRINTING = "sprinting"
SKILL_STILT_WALKING = "Stilt-walking"
JSON_STILT_WALKING = "stilt-walking"
SKILL_STONE_LORE = "Stone Lore"
JSON_STONE_LORE = "stone-lore"
SKILL_STONE_CRAFTS = "Stone-crafts"
JSON_STONE_CRAFTS = "stone-crafts"
SKILL_STORY_TELLING = "Story Telling"
JSON_STORY_TELLING = "story-telling"
SKILL_SURFING = "Surfing"
JSON_SURFING = "surfing"
SKILL_SURGERY = "Surgery"
JSON_SURGERY = "surgery"
SKILL_TACTICAL_GAMES = "Tactical Games"
JSON_TACTICAL_GAMES = "tactical-games"
SKILL_TACTICS = "Tactics"
JSON_TACTICS = "tactics"
SKILL_TALE_TELLING = "Tale Telling"
JSON_TALE_TELLING = "tale-telling"
SKILL_TIME_SENSE = "Time Sense"
JSON_TIME_SENSE = "time-sense"
SKILL_TRADING = "Trading"
JSON_TRADING = "trading"
SKILL_TRADING_LORE = "Trading Lore"
JSON_TRADING_LORE = "trading-lore"
SKILL_TRANSCEND_ARMOUR = "Transcend Armour"
JSON_TRANSCEND_ARMOUR = "transcend-armour"
SKILL_TUMBLING = "Tumbling"
JSON_TUMBLING = "tumbling"
SKILL_UNDEAD_LORE = "Undead Lore"
JSON_UNDEAD_LORE = "undead-lore"
SKILL_USING_PREPARED_HERBS = "Using Prepared Herbs"
JSON_USING_PREPARED_HERBS = "using-prepared-herbs"
SKILL_VENTRILOQUISM = "Ventriloquism"
JSON_VENTRILOQUISM = "ventriloquism"
SKILL_WEIGHT_LIFTING = "Weight Lifting"
JSON_WEIGHT_LIFTING = "weight-lifting"
SKILL_WOOD_CRAFTS = "Wood-crafts"
JSON_WOOD_CRAFTS = "wood-crafts"

json_input_map = {
    JSON_ACTING: SKILL_ACTING,
    JSON_ADMINISTRATION: SKILL_ADMINISTRATION,
    JSON_ADRENAL_CONCENTRATION: SKILL_ADRENAL_CONCENTRATION,
    JSON_ADVERTISING: SKILL_ADVERTISING,
    JSON_ALCHEMY: SKILL_ALCHEMY,
    JSON_ALERTNESS: SKILL_ALERTNESS,
    JSON_ANIMAL_HANDLING: SKILL_ANIMAL_HANDLING,
    JSON_ANIMAL_HEALING: SKILL_ANIMAL_HEALING,
    JSON_ANIMAL_HUSBANDRY: SKILL_ANIMAL_HUSBANDRY,
    JSON_ANIMAL_TRAINING: SKILL_ANIMAL_TRAINING,
    JSON_ANTHROPOLOGY: SKILL_ANTHROPOLOGY,
    JSON_APPRAISAL: SKILL_APPRAISAL,
    JSON_ARCHITECTURE: SKILL_ARCHITECTURE,
    JSON_ASTRONOMY: SKILL_ASTRONOMY,
    JSON_ATHLETIC_GAMES: SKILL_ATHLETIC_GAMES,
    JSON_BEAST_MASTERY: SKILL_BEAST_MASTERY,
    JSON_BEGGING: SKILL_BEGGING,
    JSON_BIOCHEMISTRY: SKILL_BIOCHEMISTRY,
    JSON_BOAT_PILOT: SKILL_BOAT_PILOT,
    JSON_CARTOGRAPHY: SKILL_CARTOGRAPHY,
    JSON_CLEANSING_TRANCE: SKILL_CLEANSING_TRANCE,
    JSON_CONTROL_LYCANTHROPY: SKILL_CONTROL_LYCANTHROPY,
    JSON_CONTACTING_SECONDARY: SKILL_CONTACTING_SECONDARY,
    JSON_CONTORTIONS: SKILL_CONTORTIONS,
    JSON_COOKING: SKILL_COOKING,
    JSON_CULTURE: SKILL_CULTURE,
    JSON_DANCING: SKILL_DANCING,
    JSON_DEATH_TRANCE: SKILL_DEATH_TRANCE,
    JSON_DEMON_DEVIL_LORE: SKILL_DEMON_DEVIL_LORE,
    JSON_DETECT_TRAPS: SKILL_DETECT_TRAPS,
    JSON_DIAGNOSTICS: SKILL_DIAGNOSTICS,
    JSON_DIPLOMACY_SECONDARY: SKILL_DIPLOMACY_SECONDARY,
    JSON_DISCERN_WOUNDS: SKILL_DISCERN_WOUNDS,
    JSON_DISTANCE_RUNNING: SKILL_DISTANCE_RUNNING,
    JSON_DOWSING: SKILL_DOWSING,
    JSON_DRAGON_LORE: SKILL_DRAGON_LORE,
    JSON_DREAM_LORE: SKILL_DREAM_LORE,
    JSON_DRAFTING: SKILL_DRAFTING,
    JSON_DRIVING: SKILL_DRIVING,
    JSON_DRUG_TOLERANCE: SKILL_DRUG_TOLERANCE,
    JSON_ENGINEERING: SKILL_ENGINEERING,
    JSON_EVALUATE_ARMOUR: SKILL_EVALUATE_ARMOUR,
    JSON_EVALUATE_METAL: SKILL_EVALUATE_METAL,
    JSON_EVALUATE_STONE: SKILL_EVALUATE_STONE,
    JSON_EVALUATE_WEAPON: SKILL_EVALUATE_WEAPON,
    JSON_FAERIE_LORE: SKILL_FAERIE_LORE,
    JSON_FAUNA_LORE: SKILL_FAUNA_LORE,
    JSON_FIRST_AID: SKILL_FIRST_AID,
    JSON_FLETCHING: SKILL_FLETCHING,
    JSON_FLORA_LORE: SKILL_FLORA_LORE,
    JSON_GAMBLING: SKILL_GAMBLING,
    JSON_GIMMICKRY: SKILL_GIMMICKRY,
    JSON_HEALING_TRANCE: SKILL_HEALING_TRANCE,
    JSON_HERALDRY: SKILL_HERALDRY,
    JSON_HERDING: SKILL_HERDING,
    JSON_HISTORY: SKILL_HISTORY,
    JSON_HORTICULTURE: SKILL_HORTICULTURE,
    JSON_HYPNOSIS: SKILL_HYPNOSIS,
    JSON_JUGGLING: SKILL_JUGGLING,
    JSON_JUMPING: SKILL_JUMPING,
    JSON_LEADERSHIP_SECONDARY: SKILL_LEADERSHIP_SECONDARY,
    JSON_LEATHER_CRAFTS: SKILL_LEATHER_CRAFTS,
    JSON_LOCATE_HIDDEN: SKILL_LOCATE_HIDDEN,
    JSON_MAPPING: SKILL_MAPPING,
    JSON_MATHS: SKILL_MATHS,
    JSON_MECHANITION: SKILL_MECHANITION,
    JSON_MEDITATION: SKILL_MEDITATION,
    JSON_METAL_CRAFTS: SKILL_METAL_CRAFTS,
    JSON_METAL_LORE: SKILL_METAL_LORE,
    JSON_MIDWIFERY: SKILL_MIDWIFERY,
    JSON_MILITARY_ORGANISATION: SKILL_MILITARY_ORGANISATION,
    JSON_MIMERY: SKILL_MIMERY,
    JSON_MIMICRY: SKILL_MIMICRY,
    JSON_MINGLING: SKILL_MINGLING,
    JSON_MNEMONICS: SKILL_MNEMONICS,
    JSON_MUSIC: SKILL_MUSIC,
    JSON_OBSERVATION: SKILL_OBSERVATION,
    JSON_OPERATING_EQUIPMENT: SKILL_OPERATING_EQUIPMENT,
    JSON_ORIENTEERING: SKILL_ORIENTEERING,
    JSON_PAINTING: SKILL_PAINTING,
    JSON_PERCEPTION: SKILL_PERCEPTION,
    JSON_PHILOSOPHY: SKILL_PHILOSOPHY,
    JSON_PLAY_INSTRUMENT: SKILL_PLAY_INSTRUMENT,
    JSON_POETIC_IMPROVISATION: SKILL_POETIC_IMPROVISATION,
    JSON_POETRY: SKILL_POETRY,
    JSON_POISON_TOLERANCE: SKILL_POISON_TOLERANCE,
    JSON_PROPAGANDA: SKILL_PROPAGANDA,
    JSON_PSYCHOLOGY: SKILL_PSYCHOLOGY,
    JSON_PUBLIC_SPEAKING_SECONDARY: SKILL_PUBLIC_SPEAKING_SECONDARY,
    JSON_RELIGION: SKILL_RELIGION,
    JSON_REGION_LORE: SKILL_REGION_LORE,
    JSON_ROPE_MASTERY: SKILL_ROPE_MASTERY,
    JSON_SCIENTIFIC_RESEARCH: SKILL_SCIENTIFIC_RESEARCH,
    JSON_SCRIBING: SKILL_SCRIBING,
    JSON_SCROUNGING: SKILL_SCROUNGING,
    JSON_SCULPTING: SKILL_SCULPTING,
    JSON_SECOND_AID: SKILL_SECOND_AID,
    JSON_SEDUCTION: SKILL_SEDUCTION,
    JSON_SENSE_AMBUSH: SKILL_SENSE_AMBUSH,
    JSON_SERVICE: SKILL_SERVICE,
    JSON_SEWING_WEAVING: SKILL_SEWING_WEAVING,
    JSON_SIEGE_ENGINEERING: SKILL_SIEGE_ENGINEERING,
    JSON_SINGING: SKILL_SINGING,
    JSON_SITUATIONAL_AWARENESS: SKILL_SITUATIONAL_AWARENESS,
    JSON_SKATING: SKILL_SKATING,
    JSON_SKINNING: SKILL_SKINNING,
    JSON_SLEEP_TRANCE: SKILL_SLEEP_TRANCE,
    JSON_SMITHING: SKILL_SMITHING,
    JSON_BLINDFIGHTING_SECONDARY: SKILL_BLINDFIGHTING_SECONDARY,
    JSON_SPRINTING: SKILL_SPRINTING,
    JSON_STILT_WALKING: SKILL_STILT_WALKING,
    JSON_STONE_LORE: SKILL_STONE_LORE,
    JSON_STONE_CRAFTS: SKILL_STONE_CRAFTS,
    JSON_STORY_TELLING: SKILL_STORY_TELLING,
    JSON_SURFING: SKILL_SURFING,
    JSON_SURGERY: SKILL_SURGERY,
    JSON_TACTICAL_GAMES: SKILL_TACTICAL_GAMES,
    JSON_TACTICS: SKILL_TACTICS,
    JSON_TALE_TELLING: SKILL_TALE_TELLING,
    JSON_TIME_SENSE: SKILL_TIME_SENSE,
    JSON_TRADING: SKILL_TRADING,
    JSON_TRADING_LORE: SKILL_TRADING_LORE,
    JSON_TRANSCEND_ARMOUR: SKILL_TRANSCEND_ARMOUR,
    JSON_TUMBLING: SKILL_TUMBLING,
    JSON_UNDEAD_LORE: SKILL_UNDEAD_LORE,
    JSON_USING_PREPARED_HERBS: SKILL_USING_PREPARED_HERBS,
    JSON_VENTRILOQUISM: SKILL_VENTRILOQUISM,
    JSON_WEIGHT_LIFTING: SKILL_WEIGHT_LIFTING,
    JSON_WOOD_CRAFTS: SKILL_WOOD_CRAFTS
}

# Add the profession bonus for each profession and level
# Add the stat bonus for each stat: map from stat name to stat bonus?
# Need to recognise if skills haven't been set.
# List of non-standard skills to loop through and check?


def init_secondary_skills(secondary_skills_json_object):
    """
    Populate a set of secondary skills in an Abilities object.
    :param secondary_skills_json_object: JSON object containing secondary skills information.
    :return: Parsed secondary skills information.
    """
    trace.entry()
    secondary_skills = OrderedDict()
    if secondary_skills_json_object is not None:
        for json_skill in list(secondary_skills_json_object.keys()):
            skill_value = secondary_skills_json_object[json_skill]
            skill_name = json_input_map.get(json_skill)
            if skill_name is None:
                trace.flow("Unexpected skill %s, convert JSON name" % json_skill)
                skill_words = json_skill.split('-')
                skill_name_lc = (' '.join(skill_words))
                skill_name = string.capwords(skill_name_lc)
            secondary_skills[skill_name] = skill_value

    trace.exit()
    return secondary_skills
