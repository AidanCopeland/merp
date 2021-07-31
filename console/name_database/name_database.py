# -*- coding: utf-8 -*-
"""
Creates the name_database which provides access to a database of character names.

Classes:
    name_database
"""
import sys
import dice
import trace_log as trace

sys.path.append('../../')


class NameDatabase:
    """
    The database of character names, sorted by race and gender.

    Methods:
        __init__(self)
        init_name_database(self)
        get_races(self)
        set_race(self, race)
        get_num_males(self)
        get_num_females(self)
        get_male(self)
        get_female(self)
        get_either(self)
    """
    def __init__(self):
        trace.entry()
        dice.randomize()
        self.name_database = {}
        self.init_name_database()
        self.set_race("Beffraen")
        self.males = []
        self.females = []
        self.current_race = ""
        trace.exit()

    def init_name_database(self):
        """
        Set up the contents of the name database.
        """
        self.name_database = {
            "Beffraen":
            [
                ["Draeg", "Gabran", "Maelgym", "Sereccan", "Shelbym", "Sherl", "Tegid"],
                ["Boghan", "Deira"]
            ],
            "Beorning":
            [
                ["Beoraborn", "Beorn", "Beornan", "Braig", "Egil", "Freobeort", "Grimbeorn",
                 "Grimbold", "Hallan", "Hethlind", "Imlahir", "Raudabern"],
                []
            ],
            "Black Numenorean":
            [
                ["Adûmir", "Aduntarik", "Akallazor", "Akbulkathar", "Alukhôr", "Ancantar",
                 "Anglach", "Arkhâd", "Armeirtän", "Arolic", "Athrazoc", "Balzathor", "Borathôr",
                 "Bragolmaitë", "Camdir", "Cyrmeirmûr", "Desinôr", "Durac", "Durbaran", "Eärantar",
                 "Falmar", "Fältur", "Fëagwath", "Fuinur", "Gastmorgath", "Gimilkhâd", "Gimilkhor",
                 "Gimilzôr", "Gulthuin", "Härderin", "Herudur", "Herumor", "Imralion", "Imrazim",
                 "Imrazôr", "Ingar", "Kaldûrmeir", "Khoradûr", "Krûsnak", "Leärdinoth", "Maben",
                 "Mireädur", "Morarthdur", "Morlammen", "Naldûrgath", "Nimruzagar", "Nûrmir",
                 "Oric", "Peldûr", "Pharaphion", "Phorakôn", "Pon Acark", "Raenar", "Sakal",
                 "Sakaladun", "Sakalthôr", "Sangarunya", "Sargan", "Seregul", "Tarfuluth",
                 "Teldûmeir", "Telicur", "Tharadoc", "Tredûrith", "Tredûrmerith", "Tûl-mir",
                 "Tulôr", "Ukandar", "Uthcû", "Valgavia", "Vilmûr", "Wyatan", "Zimrathôn",
                 "Zimtarik", "Zokhad", "Zuxzuldûr"],
                ["Akûrarii", "Araphor", "Bävire", "Beruthiel", "Eädur", "Eläemir", "Inzilbêth ",
                 "Miruimor", "Mûrabeth", "Rozilan", "Telerien", "Zimraphel"]
            ],
            "Dorwinadan":
            [
                ["Arcatia", "Ballin", "Baradi", "Behhrin", "Bendretta", "Cardily", "Davmps",
                 "Dolwin",  "Drel", "Drusso", "Dudannis", "Forlet", "Garth", "Garvanon", "Gollo",
                 "Handel", "Jorga", "Kiral", "Korl", "Lada", "Legios", "Mikel", "Morse",
                 "Noralda", "Rambal", "Rant", "Rencil", "Rof", "Sethrian", "Tavlo", "Tieran",
                 "Vosca"],
                ["Biarda", "Ciarda", "Fregia", "Gilyn", "Julia", "Nenladil"]
            ],
            "Dunadan":
            [
                ["Aderil", "Adrazôr", "Aeghan", "Aegnor", "Aerandir", "Aervellon", "Agonar",
                 "Aladil", "Alagarn", "Alandur", "Aldamir", "Aldúrin", "Allurac", "Amadar",
                 "Amandil", "Amaron", "Amarthion", "Amdir", "Amferen", "Amlaith", "Amondil",
                 "Amrod", "Amrohir", "Amtaur", "Anaras", "Anardil", "Anarond", "Anborn", "Andril",
                 "Angbor", "Angelimar", "Angon", "Angrim", "Annoras", "Anvelig", "Aradan",
                 "Aradil", "Arador", "Araglas", "Arahâd", "Aranarth", "Aranel", "Araval", "Aravir",
                 "Arcambion", "Arcle", "Arcondur", "Ardehir", "Arfanhil", "Arganil", "Arinethir",
                 "Arlaith", "Arlend", "Arûkhor", "Atano", "Aurandir", "Avram", "Balan", "Balcam",
                 "Ballath", "Barach", "Baragin", "Baragund", "Barahir", "Baramor", "Baranfindel",
                 "Baranor", "Barendil", "Barfindil", "Belchamion", "Belcthir", "Belechael",
                 "Belechul", "Belecthor", "Beleg", "Belegdur", "Belegorn", "Belegund", "Beletar",
                 "Belvor", "Beran", "Berdil", "Beregar", "Beregond", "Beregor", "Beren",
                 "Berendúr", "Beretar", "Bergil", "Bergrand", "Berillan", "Betheal", "Bondan",
                 "Boranas", "Borandil", "Boranglim", "Borgil", "Boromir", "Borondir", "Brandir",
                 "Breglor", "Bregol", "Bregolas", "Brethil", "Brethildur", "Caerlinc", "Caldamir",
                 "Calendur", "Calimehtar", "Calimmacil", "Calimon", "Calion", "Calmacil",
                 "Calvellon", "Camagal", "Camallin", "Cambre", "Camdir", "Camlan", "Camlin",
                 "Caraglin", "Caramir", "Carandae", "Carandor", "Caranthir", "Carnendil",
                 "Carradar", "Cebervoth", "Celarin", "Celdrahil", "Celebdur", "Celebrindor",
                 "Celefarn", "Celefaroth", "Celepharn", "Celephir", "Cemendur", "Ceren", "Cimrion",
                 "Ciramir", "Círdus", "Cirion", "Ciryaher", "Ciryang", "Ciryatur", "Ciryon",
                 "Coratar", "Cormacar", "Cospatric", "Cristion", "Cuimarion", "Curistel",
                 "Curmegil", "Curudur", "Daeron", "Daeros", "Dagnir", "Dairos", "Dairuin",
                 "Damrod", "Darion", "Daroc", "Daroín", "Denethor", "Derufin", "Derulin",
                 "Dervorin", "Desirin", "Dindal", "Dintur", "Dior", "Direvel", "Dírhael",
                 "Dírhavel", "Dongorath", "Doramir", "Dorandrand", "Dorias", "Dorien", "Dorrin",
                 "Drégon", "Dregorsgil", "Dromil", "Duilin", "Duinhir", "Dunsûl", "Dúraladh",
                 "Duranil", "Durbil", "Durgin", "Durvar", "Éanfled", "Eärbaldol", "Eardil",
                 "Eärdil", "Eärnil", "Eärnur", "Echorion", "Ecthelion", "Edhelion", "Edrahil",
                 "Egalmoth", "Egulë", "Ekuris", "Elatar", "Eldacar", "Eldahil", "Eldamir",
                 "Elenaerion", "Elendin", "Elvir", "Encalion", "Eradan", "Erador", "Erchamion",
                 "Erchvir", "Erdil", "Eregdur", "Erelion", "Erellont", "Erestor", "Erhuan",
                 "Erthil", "Ervegil", "Ervithdin", "Esgaldor", "Estel", "Estelmo", "Everithil",
                 "Falastir", "Falathar", "Falather", "Falmathil", "Faltar", "Faltur", "Fanuidhol",
                 "Faradon", "Farahail", "Faramir", "Farandir", "Farnithain", "Fergerin",
                 "Findamir", "Findegil", "Finglin", "Finlong", "Finralin", "Finrod", "Fondil",
                 "Fordelin", "Forodil", "Fuindil", "Fuinur", "Gabbon", "Galadhrion", "Galadrahil",
                 "Galdor", "Galwë", "Gamallin", "Gathdîn", "Gedron", "Geiri", "Gelmir", "Gethron",
                 "Gevas", "Giladan", "Gilcúdor", "Girion", "Gloredhel", "Glorfindel", "Golantir",
                 "Golasgil", "Gontran", "Gonvegil", "Gordacar", "Gorlim", "Goromil", "Guldúmir",
                 "Gundor", "Gwathvoron", "Gwindor", "Haddil", "Hador", "Haedric", "Halach",
                 "Halamir", "Halbarad", "Haldan", "Haldarion", "Halgon", "Hallacar", "Hallas",
                 "Handir", "Harmadil", "Hathol", "Hearon", "Helvorn", "Henderch", "Herion",
                 "Herluin", "Heruvorn", "Hieryan", "Hiraew", "Hirgon", "Hirluin", "Hunthor",
                 "Huor", "Hurin", "Hydril", "Iderion", "Idrazor", "Imkel", "Imlach", "Imrahad",
                 "Imrahâd", "Imrahil", "Ingold", "Ingwë", "Inhael", "Intorin", "Ionel", "Iovin",
                 "Irdaal", "Irdamir", "Irhalmir", "Irmion", "Isildur", "Ithildir", "Ithilrain",
                 "Kelvarguin", "Kirvin", "Lhachglin", "Lindal", "Lith", "Lórin", "Lorindol",
                 "Lotharion", "Luinil", "Luthien", "Mablung", "Maeglin", "Magor", "Malbeth",
                 "Malborn", "Malcam", "Malfinwë", "Malion", "Mallach", "Mallin", "Mallindor",
                 "Mallor", "Malloth", "Malvagor", "Malvegil", "Marach", "Marados", "Marahil",
                 "Mardil", "Marendil", "Marmedon", "Meladorn", "Meldin", "Melforn", "Melrandir",
                 "Meneldil", "Meneldir", "Meneldor", "Menelmir", "Mengron", "Merembeleg", "Mereth",
                 "Methillir", "Minalcar", "Minastir", "Mindacil", "Minohtar", "Mirenil", "Mîrkano",
                 "Mirnidar", "Monach", "Moradan", "Morchaint", "Mordulin", "Morgalad", "Morvagor",
                 "Nadhaim", "Narmacil", "Naurdil", "Neithan", "Neldorn", "Nerumir", "Nimengel",
                 "Nimhir", "Nimír", "Nimrilien", "Nimroch", "Niniel", "Ninko", "Nísi", "Nomrel",
                 "Odo", "Odonil", "Ondoher", "Opperith", "Orbragol", "Orchaldor", "Orinas",
                 "Ormendel", "Orodreth", "Ostoher", "Oswy", "Othirhan", "Oxrandir", "Palandal",
                 "Palandar", "Palandir", "Palarcam", "Palomire", "Parigan", "Parmandil",
                 "Pelendur", "Perion", "Perorren", "Pilinnur", "Piréna", "Poddit", "Portnithor",
                 "Quenandil", "Queneldor", "Quiacil", "Radhruin", "Ragnir", "Ragnor", "Randi",
                 "Rathumus", "Rendail", "Revorn", "Rhovanhen", "Rhovannin", "Rhukar", "Rincar",
                 "Ringlin", "Ringmir", "Ringór", "Rinhil", "Roane", "Rocúrion", "Rodhel",
                 "Roensen", "Roginor", "Romer", "Romin", "Ronindil", "Ruinir", "Saerol",
                 "Sarvelich", "Seregdal", "Shakhôr", "Solorion", "Sorondothor", "Sûlistar",
                 "Surion", "Taladhan", "Talathorn", "Tamir", "Tarannon", "Tarassar", "Tarbeth",
                 "Tardegil", "Tarfil", "Targon", "Tarhad", "Tarminion", "Tarquillan", "Tauron",
                 "Teiglor", "Telchrist", "Telegorn", "Telemnar", "Telethal", "Telumehtar",
                 "Tensidir", "Tergon", "Terieth", "Terision", "Thalion", "Thireny", "Thorondir",
                 "Thorongil", "Thorûth", "Tigon", "Tillórin", "Tiranir", "Tirazôr", "Tirgil",
                 "Tirion", "Tirwin", "Tolodin", "Tonekil", "Túan", "Tuminir", "Tuor", "Turgon",
                 "Turin", "Turjomil", "Ulbar", "Urthel", "Uthrin", "Vagaig", "Valacar", "Valadan",
                 "Valandil", "Vardamavi", "Vardamir", "Veantur", "Vëantur", "Verylen", "Viliarith",
                 "Vilyatir", "Vinyaran", "Voromir", "Vorondil", "Voronthor", "Warris", "Zamin",
                 "Zardellum"],
                ["Aelindur", "Aeriel", "Aerin", "Aerinel", "Almiel", "Alquawen", "Anóriel",
                 "Áraliniel", "Aranwen", "Arienwen", "Arisiel", "Astrith", "Belewen", "Bellaniel",
                 "Bessandis", "Caladwen", "Calamere", "Caliel", "Calime", "Camarina", "Caraniel",
                 "Celebriel", "Celeserwen", "Colmorwë", "Corrian", "Darana", "Dinturien",
                 "Edhetariel", "Eldiriel", "Ellothiel", "Elmericel", "Elosian", "Emeldir", "Emerie",
                 "Erendis", "Erennis", "Esteliel", "Ethudil", "Faivë", "Fanuilë", "Fimalcá",
                 "Finduilas", "Finriel", "Firiel", "Gaerwen", "Galina", "Galwen", "Gamin", "Gillan",
                 "Gilmith", "Gilorwen", "Gilraen", "Gilronwen", "Gilweth", "Glíwen", "Gysiel",
                 "Haedoriel", "Helluin", "Hiraew", "Idril", "Ilmarë", "Imberin", "Imisiel", "Jin",
                 "Kireil", "Laurelach", "Lessith", "Lorin", "Lothiriel", "Lothíriel", "Lúthien",
                 "Lyana", "Malloriel", "Melian", "Melindwen", "Melloriel", "Melmereth", "Meriel",
                 "Merien", "Mindiel", "Míraladhwen", "Míriel", "Mírien", "Morwen", "Nariel",
                 "Nartheliel", "Nassiel", "Neldoriel", "Nienor", "Niniel", "Níriel", "Ólanwen",
                 "Pelenwen", "Pelewen", "Perlothiel", "Rophirë", "Rosíthil", "Rûmenna", "Saranelda",
                 "Seregonwen", "Serinde", "Serindë", "Sernesta", "Silivrien", "Silmarien",
                 "Silrien", "Sirith", "Sondinwë", "Sulimith", "Sulinwë", "Súlinwë", "Talfannan",
                 "Telperien", "Tollanwen", "Túriel", "Vanána", "Voronwë", "Wintila", "Yendílwë"]
            ],
            "Dunlending":
            [
                ["Adeyn", "Aidhan", "Albaraich", "Amithol", "Amthol", "Ancú", "Anduinil", "Aonghas",
                 "Arleg", "Baga", "Barnur", "Belligel", "Berma", "Beul", "Bheil", "Blaith",
                 "Bomaynee", "Borar", "Borkul", "Borru", "Brego", "Bruad", "Cadwallon",
                 "Cagh Monûnaw", "Cairmach", "Calach", "Calmuad", "Canth", "Cartmel", "Ceasgair",
                 "Cenne", "Cern", "Chulainn", "Cies", "Cinard", "Cisid", "Cluad", "Clúan", "Clyn",
                 "Cober", "Coel", "Coelmun", "Coeshay", "Crennen", "Cú", "Cuag", "Cunnat",
                 "Daonghlas", "Darnic", "Dervorin", "Drualphien", "Dumfa", "Dunadd", "Durth",
                 "Eagan", "Easgan", "Ebbo", "Edallaigh", "Eion", "Elharian", "Enion", "Eskerzen",
                 "Feannan", "Feirr", "Feldas", "Feundig", "Fimran", "Fiorel", "Foskat", "Furish",
                 "Furn", "Furth", "Fwen", "Fyn", "Gaoth", "Gariac", "Glurin", "Gorgan", "Gov",
                 "Guik", "Haedrec", "Harec", "Hasso", "Hoegwar", "Iarlless", "Iestin", "Illtud",
                 "Jerl", "Jeroibha", "Josherë", "Kasselrim", "Khathog", "Kurf", "Kurna", "Lanaigh",
                 "Larth", "Llwei", "Lumban", "Magone", "Marroc", "Maschbram", "Meórag", "Merro",
                 "Mert", "Moctallan", "Morthec", "Naum", "Nidd", "Nig", "Nudan", "Oravai",
                 "Oravarri", "Orcare", "Orvig", "Osgan", "Pad", "Padrey", "Pesc", "Pureneir",
                 "Ragi", "Raltin", "Raonull", "Ries", "Riscen", "Roggowen", "Rovik", "Rulart",
                 "Saddro", "Scammar", "Scoel", "Seammu", "Seinacaid", "Shoglic", "Sibroc", "Smardo",
                 "Sogran", "Solofhen", "Sult", "Surnir", "Suvac", "Talegi", "Telleman", "Tfalz",
                 "Thebo", "Thirrio", "Thrangir", "Torac", "Torifal", "Trmac", "Tughaibh", "Ulf",
                 "Uner", "Urchoid", "Urdrek", "Urlaglin", "Vagibreg", "Varen", "Voisiol", "Werlar",
                 "Wuftana", "Wulf"],
                ["Anrea", "Brennan", "Cea", "Cila", "Derna", "Derra", "Egwar", "Eribhen",
                 "Fecandra", "Feorna", "Haeldwyn", "Ishel", "Measgan", "Merwai", "Reghian", "Retha",
                 "Riadégha", "Sionnach", "Sudha", "Tanray", "Tughaib", "Urganna", "Uthanna",
                 "Ygana"]
            ],
            "Easterling":
            [
                ["Adajo", "Aegach", "Akonid", "Ariks", "Arkish", "Baleksar", "Barakat", "Bassan",
                 "Belechor", "Bór", "Borhan", "Borlach", "Borlad", "Borthand", "Braith", "Carfe",
                 "Celgor", "Chukka", "Demik", "Dudannis", "Dûmra", "Esseu", "Ethacali", "Ethem",
                 "Evit", "Geer", "Gol Makov", "Gorin", "Gorion", "Gozef", "Grallon", "Grasty",
                 "Grimling", "Guton", "Heludar", "Hord", "Hos", "Huil", "Hungh", "Huskash", "Huz",
                 "Hûz", "Jukath", "Jyaganoth", "Jyganoth", "Karamar", "Katrisel", "Kav",
                 "Kav Gorka", "Keemac", "Koumiss", "Lorgam", "Lorthand", "Mahto", "Meonid",
                 "Mercaver", "Mhôrlen", "Mungrod", "Neburcha", "Nevido", "Orash", "Ormar",
                 "Rechorca", "Rof", "Senzal", "Shabun", "Shakal", "Skauril", "Slovas", "Thuram",
                 "Tinta", "Tros", "Uldor", "Ulfang", "Ulfast", "Ulwarth", "Urdrath", "Vacros",
                 "Varchaz", "Vrak", "Wiliaruk", "Wiliatun", "Wiliazen", "Zorab"],
                ["Gisela", "Jasala", "Kadida", "Shanva", "Totila", "Tuva"]
            ],
            "Eriadoran":
            [
                ["Aelfred", "Aescstan", "Aethelan", "Algen", "Amalin", "Amplac", "Andril", "Aranas",
                 "Arondil", "Arteveld", "Atano", "Aysteac", "Bail", "Barahdell", "Barkwell",
                 "Barliman", "Beregond", "Bernar", "Bethlam", "Bill", "Bob", "Boinand", "Bondan",
                 "Braith", "Burthurin", "Carmil", "Carnion", "Cerwiff", "Cethwin", "Chal",
                 "Chapster", "Chiarold", "Cobman", "Colfen", "Cormac", "Cormacar", "Curudur",
                 "Curuvegil", "Cuthan", "Dagobert", "Dairuin", "Delrin", "Derelon", "Dethor",
                 "Dirkal", "Dongorath", "Dórmir", "Drake", "Drun", "Duffy", "Duoveris Cleg",
                 "Eamir", "Edrec", "Eliver", "Emendil", "Emerdan", "Envir", "Eowic", "Eratil",
                 "Ergrem", "Eríbhen", "Erig", "Erling", "Euric", "Farrenar", "Feinhíril", "Feld",
                 "Feldas", "Fimarn", "Firdok", "Forlong", "Fwen", "Gaem Wulsen", "Galun", "Gellain",
                 "Gendar", "Grethor", "Gulstaff", "Guntar", "Halbered", "Halfast", "Hallas", "Ham",
                 "Haren", "Harluinar", "Harran", "Harry", "Haver", "Herucalmo", "Hiiri", "Hiri",
                 "Hobson", "Hujai", "Ibal", "Irurn", "Jeirn", "Jeshan", "Kellir", "Korbrild",
                 "Kuball", "Laifrin", "Lamarod", "Lamril", "Len", "Lengha", "Lhachglin", "Limlach",
                 "Lindorië", "Lith", "Lorgas", "Lóthand", "Luinand", "Lúvagor", "Mablung", "Mag",
                 "Mallick", "Marluk", "Mat", "Michl", "Moff", "Nasen", "Navir", "Oget", "Olby",
                 "Orchaldor", "Ornil", "Pate", "Pegmar", "Pilkun", "Pultar", "Purdin", "Purth",
                 "Rannor", "Ravambor", "Rigdarabin", "Rory", "Rubb", "Rudiger", "Ruem Laer",
                 "Runnal", "Rush", "Sarkar", "Shebrim", "Shiril", "Sigmar", "Sisebuth", "Sovorn",
                 "Surk", "Svinder", "Talmabrith", "Tarhad", "Telemnar", "Telethal", "Theave",
                 "Thelgrom", "Thramir", "Thuidimer", "Tilmarin", "Tirrin", "Tolman", "Tregon",
                 "Tuggle", "Turgarin", "Turibor", "Turoth", "Turumir", "Ulgar", "Vengaree", "Virin",
                 "Virloch", "Welar", "Werlard", "Will", "Wilrith", "Zarby"],
                ["Angrid", "Aysteas", "Barelwen", "Bereth", "Bredda", "Brithwen", "Bura", "Cora",
                 "Currael", "Daisy", "Deniel", "Effie", "Egale", "Eilwen", "Elisa", "Eriel",
                 "Hannei", "Hiriel", "Holly", "Idris", "Iriel", "Kerit", "Maisy", "Mirrin",
                 "Morwen", "Murryelle", "Rellin", "Severtha", "Sirrin", "Tempi", "Torendra"]
            ],
            "Haradan":
            [
                ["Abdahkil", "Ablish", "Amrukh", "Arcil", "Aru-Sûm", "Ashdam", "Barthanan",
                 "Belphegor", "Bidash", "Bläs", "Brom", "Carlon", "Carnen Mek", "Casarac", "Cluth",
                 "Cudûma", "Culcamalin", "Dabadda", "Dejyk", "Del Imat", "Derei", "Dulish", "Dulo",
                 "Epef", "Es-amu", "Esfur", "Eshefar", "Flerit Klorin", "Garlan Det", "Gimmin",
                 "Hamid", "Harath do Ramam", "Harij", "Harith", "Ikûr", "Jaeru", "Jalib",
                 "Jamak Spijun", "Jarnir", "Kalatar", "Karaag", "Karamac", "Karan", "Klú Relortin",
                 "Krinda", "Kub Nara", "Kuran", "Leizha", "Ló-desmic", "Lonkuran", "Machun",
                 "Malezar", "Manari", "Matsûm", "Merul", "Min Oturna", "Moraiza Satark", "Nahir",
                 "Nard", "Ne-baraca", "Neddet", "Ne-eslem", "Ne-ula", "Ne-upka", "Ne-wull",
                 "Nomikon", "Obed", "Oeren", "Ombûr", "Orbul", "Orcir", "Ordun Halbor", "Orf Tello",
                 "Ormul", "Ossim", "Padua Bar", "Paji", "Par Shetti", "Pathan", "Pernelion",
                 "Peshtin", "Pon Olarti", "Pon Opar", "Pujist Din", "Qesset", "Rhavas", "Ricenaris",
                 "Runeren", "Sakur do 'Akil", "Samaub Narett", "Sazar Parn", "Sen Jerrek",
                 "Shardoz", "Shebbin Vûr", "Simbu", "Slú Carlon", "Slûcrac", "Sofan do Sofan",
                 "Sokol Sova", "Suljati Sey", "Tabaya Kas", "Tahar do Sakur", "Tarkas",
                 "Tartas Izain", "Tel Azef", "Tennith Borbul", "Terendil", "The Gusar", "The Póa",
                 "The Pust", "Tolodin", "Tónn", "Tor Mitari", "Ulaca", "Ulcathur", "Ulfacs",
                 "Ulrith", "Uma", "Umbin Swé", "Vamman Carl", "Wimbur", "Wote", "Yezmin",
                 "Yud do Sarsor", "Zäde", "Zimrakhil", "Zumman"],
                ["Arza sut Timman", "Bethin Omul", "Ebarthon", "Emuna", "Jefya", "Leriaj", "Lesjia",
                 "Lyli", "Nurna", "Shabla", "Shamara sut Katub", "Thena", "Tiena"]
            ],
            "Hillman":
            [
                ["Bragha", "Bram-op-Bran", "Bregg", "Brend", "Briam", "Broggha", "Jo-nag", "Krennt",
                 "Llewen", "Llewt", "Mong-Finn", "Mon-raggh", "Movran", "Nagwech", "Nalle",
                 "Paddro", "Seammu", "Sispar", "Twi Righa", "Twi Twir", "Vennolandua", "Wistan"],
                ["Ap-Brigg", "Ap-Coleen"]
            ],
            "Lossoth":
            [
                ["Chosum", "Culnun", "Daled", "Frannard", "Grimk", "Gromk", "Iltatuuli",
                 "Karhunkäsi", "Lufsen", "Lumipallo", "Nuorilintu", "Pitää", "Puolikarhu",
                 "Trimani", "Yhedksän"],
                ["Pieni", "Punakäsi", "Sadenainen", "Sinipilvi", "Unisoturi", "Vanha"]
            ],
            "Northman":
            [
                ["Aelfred", "Aelfric", "Agiluf", "Alboin", "Albwini", "Aldaric", "Aldhelm", "Aldor",
                 "Aldoric", "Alfraits", "Alfward", "Antharis", "Aradacer", "Asgaric", "Atagavia",
                 "Athugavia", "Audarik", "Augimund", "Bain", "Baldor", "Balg", "Bancadan", "Bard",
                 "Baric", "Barlof", "Baumyakund", "Beadarof", "Bemyakund", "Beneric", "Beortnov",
                 "Bonigild", "Brach", "Braegla", "Brand", "Breagla", "Sarador", "Brego",
                 "Tharendin", "Targon", "Breor", "Brëor", "Breorh", "Brocking", "Broehir",
                 "Haurian", "Brogdin", "Brug", "Brytta", "Buhrgavia", "Carloman", "Caviltar",
                 "Ceorl", "Charibert", "Chilperic", "Brenith", "Chlodomir", "Chlotar", "Cilis",
                 "Corl", "Cormac", "Harmandil", "Daef-Udra", "Daelgild", "Dagobert", "Dani",
                 "Darian", "Dartel", "Demarii", "Déor", "Déorwine", "Dieraglir", "Dorvic",
                 "Drafend", "Druhtiridya", "Drukka", "Dúnhere", "Dunnarth", "Earm", "Ebroin",
                 "Edorhil", "Edwodyn", "Ehwarik", "Elfhelm", "Ellollen", "Eloric", "Eniad",
                 "Eoaric", "Éoder", "Éodoric", "Éofor", "Éomund", "Eorein", "Eormenlic", "Éothain",
                 "Erkenbrand", "Eudail", "Falryen", "Fastred", "Fengel", "Fennric", "Fidoric",
                 "Folca", "Folcred", "Folcwine", "Folgar", "Folric", "Fornagath", "Forthwini",
                 "Fram", "Fréa", "Freaga", "Fréahár", "Fréaláf", "Fréalóf", "Fréalor", "Freamund",
                 "Fréawine", "Freca", "Fréga", "Froedhir", "Frumgar", "Fryancryn", "Fylaric",
                 "Galariks", "Galmod", "Gamling", "Gardagd", "Gartila", "Gárulf", "Gerse", "Girion",
                 "Gléowine", "Glyorivia", "Gnorn", "Goldwine", "Gordai", "Gorghiric", "Goshafoc",
                 "Gram", "Gríma", "Grimabalth", "Grimbold", "Gripa", "Gristlung", "Gudrinc",
                 "Guidariks", "Guntram", "Gurth", "Guthláf", "Guthwin", "Gwyn", "Haed", "Halfred",
                 "Háma", "Harding", "Heleder", "Helin", "Hemming", "Herefara", "Herewulf", "Herion",
                 "Herubrand", "Hestan", "Heth", "Hilderinc", "Hilman", "Hoeg Cuerd", "Hofding",
                 "Holting", "Horn", "Hréowalda", "Hrothgar", "Huc", "Hundin", "Hurm", "Hwaetrinc",
                 "Hygegrim", "Jerriad", "Jiord", "Kennit", "Konnul", "Korlin", "Krulla", "Kynoden",
                 "Lain", "Lann", "Lanning", "Lefwin", "Léod", "Léodurth", "Leovigild", "Léovric",
                 "Leowin", "Liam", "Ligrador", "Linlocc", "Lisgaria", "Lorril", "Lorthis",
                 "Maecwin", "Maethelgar", "Mahrbrand", "Mahrcared", "Mahrwini", "Marach", "Marhari",
                 "Marhcared", "Marhwini", "Marlo", "Matorn", "Merovech", "Mikilarn", "Nial",
                 "Nithya", "Odagavia", "Odavacer", "Ogar", "Orduclax", "Osric", "Oterics",
                 "Otogorth", "Pathirad", "Penda", "Pepin", "Portik", "Raendoric", "Rello",
                 "Rognachar", "Romauld", "Rotaris", "Saewic", "Saewulf", "Sahail", "Sallan", "Saym",
                 "Scoderath", "Sculding", "Shinrinc", "Sigfast", "Sigiswulf", "Sigwerd", "Sorandil",
                 "Sunlending", "Swertling", "Swithwulf", "Taraim", "Thal Éolsen", "Thandrain",
                 "Thang", "Thelas", "Thenesleag", "Théodolinda", "Théodwine", "Theoren", "Therge",
                 "Thiudawini", "Thordil", "Thorlavan", "Thuidimer", "Tonfall", "Tosti", "Uirdriks",
                 "Ulno", "Ulred", "Umbor", "Uphelb", "Utlash", "Valdor", "Vandorag", "Vellser",
                 "Vergandrieg", "Viclaf", "Vidugavia", "Vidurafin", "Vidustain", "Vilorc",
                 "Viloric", "Vogir", "Volaf", "Vormenric", "Vracoth", "Waggeorn", "Wakr",
                 "Walvoric", "Waulcho", "Waulrics", "Weriúch", "Wídfara", "Widuhund", "Wiglaf",
                 "Wistan", "Witbert", "Wolwin", "Wuilaric", "Wulf", "Wulfr", "Wuthgild", "Yarri",
                 "Ymp", "Ynarri"],
                ["Aldora", "Anni", "Ariberta", "Aud", "Beawyn", "Béawyn", "Béotta", "Blosoma",
                 "Bogatung", "Borgenda", "Brinwica", "Bronwyn", "Brunehaut", "Dunheuet", "Elfhild",
                 "Éothwyn", "Eudesuntha", "Flana", "Flota", "Forwen", "Fréawyn", "Fredegonde",
                 "Freowyn", "Fréowyn", "Fulda", "Gaervicca", "Gelda", "Gelmir", "Gretta",
                 "Gudelinda", "Haleth", "Hild", "Hildegripa", "Illinith", "Jirfelien", "Kelai",
                 "Laren", "Leofa", "Liwisintha", "Marhforn", "Marluh", "Marodwyn", "Minual",
                 "Odalinda", "Raedwyn", "Rémahild", "Riguntha", "Rinel", "Rose", "Sahali",
                 "Sauilswintha", "Shagedla", "Sigebeorta", "Spearwa", "Stanchela", "Sulwen",
                 "Súlwyn", "Syndrith", "Thraer", "Unn", "Valcrigge", "Vidumavi", "Wilda", "Woedwyn"]
            ],
            "Gondorian":
            [
                ["Allit", "Amrod", "Andra", "Araclin", "Aranna", "Arantar", "Arcle", "Argirion",
                 "Axor", "Balthrod", "Barmir", "Beldin", "Belebragol", "Beregond", "Boron",
                 "Bracken", "Brandir", "Bregor", "Brelam", "Brettring", "Calenorn", "Calmacil",
                 "Camulion", "Cannal", "Carcamir", "Carnendil", "Cealan", "Cendralion", "Civrui",
                 "Clennan", "Clothiel", "Coerba", "Conul", "Croggan", "Dagar", "Dagnir", "Dagobert",
                 "Damrod", "Derufin", "Dirhavel", "Domar", "Dorelas", "Doreoren", "Duinhir", "Eben",
                 "Ecuris", "Edacar", "Edwilber", "Eldanon", "Elegar", "Elin", "Eolson", "Erkam",
                 "Fallin", "Fallor", "Ferrin", "Findegil", "Fíriel", "Forlong", "Fornact", "Gael",
                 "Galad", "Galbar", "Galf", "Gam", "Gelmir", "Gerdon", "Gildor", "Gorlim",
                 "Grathian", "Grillic", "Hace", "Halbar", "Haldir", "Halifor", "Hallatan", "Halmir",
                 "Handir", "Hargon", "Hatharya", "Havnis", "Helbran", "Herion", "Herucalmo",
                 "Herumir", "Hirgon", "Horluin", "Hossadam", "Hunthor", "Hurin", "Imlach", "Ini",
                 "Iorlas", "Joraal", "Kaldir", "Kíron", "Krobon", "Lanios", "Lidimir", "Mablung",
                 "Maeflad", "Malbeth", "Maldring", "Malegorn", "Mard", "Meriot", "Merithdil",
                 "Midhroch", "Midmin", "Minasdan", "Mino", "Morreg", "Myall", "Myarnil", "Naurudûn",
                 "Neldorn", "Olby", "Oric", "Ormon", "Padderec", "Palanthrar", "Palol", "Palvano",
                 "Pauren", "Penemith", "Perdido", "Perion", "Pinto", "Portik", "Pwyll", "Ragnir",
                 "Ragnor", "Rastarin", "Rewin", "Rieldir", "Rillit", "Ringmir", "Rogan", "Rogeth",
                 "Rognir", "Rohtur", "Saeros", "Seregon", "Serendur", "Shebbin", "Shorrie",
                 "Sinyadal", "Siobal", "Syron", "Tárain", "Targon", "Tarlang", "Telissûring",
                 "Tergon", "Terimbrel", "Tharagun", "Tharanon", "Thoril", "Thorondil", "Thorondir",
                 "Tinindil", "Torgir", "Tuor", "Ulbar", "Ulbor", "Uldros", "Ullis", "Ulrad",
                 "Úrcamir", "Urlagin", "Urranta", "Vagor", "Vandor", "Varak", "Verden", "Vinië",
                 "Wafar", "Walec", "Wartik", "Widlo", "Wilrith", "Zarby"],
                ["Bereth", "Boromis", "Brilwen", "Caenesta", "Carnel", "Degla", "Dorien", "Emeldir",
                 "Fanariel", "Fíriel", "Frandica", "Garreth", "Gilwen", "Glindiel", "Grena",
                 "Haleth", "Idril", "Ioanna", "Ioreth", "Jesec Cael", "Kinda", "Lissuin", "Luinen",
                 "Miena", "Miriel", "Nanya", "Nimriel", "Odelard", "Raniel", "Stefa", "Sunil",
                 "Taska", "Treva", "Tyreath", "Uruiwen", "Yoruvë"]
            ],
            "Variag":
            [
                ["Azzad", "Curuband", "Gorovod", "Itana", "Mardrash", "Ovatha", "Uma", "Valhad"],
                []
            ],
            "Woodman":
            [
                ["Bardir", "Clemendan", "Gramberot", "Hírband", "Rothaar", "Theamond", "Theuderic",
                 "Thuiric", "Tiralgar", "Waulfa", "Windlore", "Woffung"],
                ["Amala", "Roenda", "Sigeberta", "Súlwine"]
            ],
            "Wose":
            [
                ["Ari-Ghân", "Ari-Ghín", "Ari-Lam", "Azakhad", "Borin", "Buri-Jun", "Buri-Khûrni",
                 "Clatu", "Daldin", "Dhân", "Effem", "Fanghîn", "Furin", "Ghân-buri-Ghân", "Ghîm",
                 "Gôr-khan-gôr", "Khûn-buri-Khûn", "Narvi", "Nhâk-Bûran", "Nivtur", "Om-buri-Om",
                 "Om-ura-Om", "Ôn-Eno", "Ôn-Ikana", "Ôn-Iko", "Ôn-Tomu", "Ôn-uri-Gès", "Or-Dîn",
                 "Or-Lân", "Or-Prâga", "Rhân-guri-Rhân", "Róin", "Viddis"],
                ["Pôn-ora-Pôn"]
            ],
            "Dwarf":
            [
                ["Ai", "Aldan", "Aldor", "Alf", "Althjof", "An", "Andvari", "Angrod", "Atilik",
                 "Aurvang", "Austri", "Azaghal", "Báin", "Bair", "Baldur", "Balin", "Balli",
                 "Balrim", "Barin", "Bávor", "Bifur", "Bildr", "Billing", "Bofur", "Bohór",
                 "Bombur", "Bowlin", "Bróin", "Bruni", "Brór", "Buri", "Burin", "Bwalin", "Cori",
                 "Craier", "Dain", "Dáin", "Dár", "Dáram", "Darim", "Darin", "Darzum", "Dhebun",
                 "Dhemim", "Dheo", "Dibin", "Dintam", "Dirn", "Dolgthrasir", "Dolin", "Dóm", "Dór",
                 "Dori", "Dralin", "Drarin", "Draupnir", "Drúhar", "Drúin", "Drús", "Duf",
                 "Duildin", "Durzil", "Dvalin", "Dwáin", "Dwalin", "Eikinskjaldi", "Falin", "Farin",
                 "Fíli", "Finn", "Fjalar", "Flói", "Fóli", "Fori", "Forin", "Fræg", "Frár", "Freri",
                 "Frerin", "Fror", "Frór", "Frósti", "Frúhar", "Frúin", "Fulla", "Fundin", "Gáin",
                 "Ghamim", "Ghar", "Gimbal", "Gimithor", "Gimlin", "Ginnar", "Glein", "Gloin",
                 "Glorin", "Grális", "Gróin", "Grolin", "Gror", "Gulla", "Gura", "Gurh", "Gurim",
                 "Gurin", "Gurn", "Halin", "Hannar", "Haugspori", "Hepti", "Hlevang", "Hor",
                 "Hornbori", "Ibír", "Ibûn", "Jari", "Kaidin", "Kalin", "Kallin", "Khadak", "Khain",
                 "Khanil", "Khanli", "Khîm", "Khorni", "Kíli", "Kóri", "Kuri", "Líli", "Lit",
                 "Lofar", "Lóni", "Miffli", "Miffli", "Mîm", "Mjothvitnir", "Moranar", "Motsognir",
                 "Nain", "Náin", "Nali", "Náli", "Nár", "Naric", "Narmire", "Naug", "Nedilli",
                 "Niping", "Nithi", "Nori", "Northri", "Nurís", "Nyi", "Nyr", "Nyrath", "Obun",
                 "Ohtar", "Oin", "Óin", "Omim", "Onar", "Ori", "Orn", "Purfin", "Rálin",
                 "Rathsvith", "Regin", "Rhomin", "Rhotti", "Rúrin", "Seldur", "Skafith", "Skirfir",
                 "Suthri", "Sviur", "Tali", "Thalin", "Tharangul", "Thekk", "Thelór", "Thíst",
                 "Thorin", "Thráin", "Thrangull", "Thrár", "Threlin", "Thrír", "Throdin", "Thror",
                 "Thrórin", "Thrúr", "Thúlin", "Thurin", "Tili", "Tíli", "Vestri", "Vigg", "Vili",
                 "Vindalf", "Virfir", "Vit", "Yngvi", "Zafor", "Zdori", "Zeddic", "Zorn", "Zrór"],
                ["Bís", "Brís", "Dís", "Drúis", "Durí", "Freris", "Grís", "Harnekil", "Silnoi",
                 "Thrís", "Tís", "Welís"]
            ],
            "Elf":
            [
                ["Adunavar", "Aegnor", "Aldan", "Aldohir", "Amdir", "Amdír", "Amras", "Amrod",
                 "Amroth", "Andovon", "Annael", "Aranto", "Aranwë", "Arculagar", "Arduin",
                 "Ardûval", "Arminas", "Arophel", "Ascarnil", "Bathor", "Beleg", "Belion",
                 "Bladorthin", "Bodmin", "Brandir", "Brethil", "Calendir", "Cambragol", "Camgalen",
                 "Camring", "Camthalion", "Caranfin", "Carihir", "Carnil", "Celedhring", "Celegorm",
                 "Celequar", "Círdor", "Coibor", "Cornen", "Curubor", "Daeron", "Daniros",
                 "Denethor", "Ecthelion", "Ectheon", "Edrahil", "Eglavirdan", "Eldarion",
                 "Elemmírë", "Elenril", "Elerior", "Elfaron", "Eluréd", "Elurín", "Elwë", "Eöl",
                 "Erestor", "Erocil", "Estelin", "Faleriod", "Falfed", "Fanar", "Fanari", "Fëabor",
                 "Fëatur", "Fendomë", "Filegdir", "Finculin", "Fingon", "Finrod", "Finwë",
                 "Froithir", "Fuinur", "Gaerdaer", "Galadlin", "Galador", "Galandeor", "Galdor",
                 "Galenlain", "Galerin", "Galion", "Galvilya", "Gelmir", "Gihellin", "Gildor",
                 "Gilraen", "Ginfilian", "Glorinadan", "Glosnar", "Gorthaur", "Gwilidhol",
                 "Gwindion", "Halatir", "Haldir", "Heladil", "Helkama", "Hílanor", "Hilvanar",
                 "Hiradur", "Hîrforn", "Huinen", "Indis", "Ingwë", "Istagol", "Kénwë", "Kheleglin",
                 "Khelekar", "Khelgin", "Khilia", "Klaen", "Laerion", "Larrithin", "Laurrë",
                 "Lenwë", "Lyaan", "Lyrin", "Mablung", "Maedhros", "Maeglin", "Maellin", "Maglor",
                 "Malthir", "Mendal", "Merethorn", "Meryalë", "Miles", "Moran", "Mornaur",
                 "Morthaur", "Mourfuin", "Nardhol", "Nenledil", "Nestador", "Olwë", "Orophin",
                 "Orrerë", "Palandor", "Pelnimloth", "Persuvious", "Ragnor", "Randae", "Rhovamir",
                 "Ringlin", "Ruindel", "Rúmil", "Saeros", "Sarkaxë", "Striuk'ir", "Sûlarin",
                 "Sûldun", "Súlherok", "Sûlherok", "Súlkano", "Súlor", "Taurclax", "Taurion",
                 "Taurnil", "Teletasarë", "Terelorn", "Terilaen", "Thalos", "Thanadirian",
                 "Tharúdan", "Turgon", "Turlindë", "Ufëa", "Ulcamer", "Vaal Gark", "Vairesûl",
                 "Valandor", "Valkrist", "Vallin", "Valmorgûl", "Valnaur", "Valsûl", "Vidarlin",
                 "Vilyadhol", "Voronwë"],
                ["Adaldrida", "Aiwë", "Amarië", "Ardana", "Aredhel", "Arhendhiril", "Ariel",
                 "Arien", "Arvairë", "Arverethiel", "Belladonna", "Bellindiel", "Brethilwen",
                 "Calime", "Derna", "Eariel", "Eärwen", "Eldebeth", "Elendor", "Elenwe", "Elenwë",
                 "Elindiel", "Elwing", "Erdíniel", "Fëamírë", "Fëatur", "Finduilas", "Gilmith",
                 "Gwaedun", "Idril", "Ivren", "Jesprin", "Lalaith", "Linsûl", "Losp'indel", "Lysa",
                 "Mally", "Marwen", "Merilwen", "Míriel", "Morloth", "Namirë", "Nernadel",
                 "Nimrodel", "Óriel", "Othariel", "Rána", "Rilia", "Saeraladhwen", "Silion",
                 "Sirnaur", "Tara", "Tathariel", "Teiglin", "Tirial", "Tiriel", "Tolwen", "Valglin",
                 "Vasariel", "Yavëkamba"]
            ],
            "Hobbit":
            [
                ["Adalgrim", "Adelard", "Amaranth", "Andwise", "Anson", "Ashturg", "Babbin",
                 "Balbo", "Berilac", "Bert", "Bilbo", "Bingo", "Blaggo", "Blanco", "Bodo", "Bowman",
                 "Broggo", "Bucca", "Bungo", "Carl", "Chuff", "Cleff", "Coldomac", "Coney",
                 "Cotman", "Cottar", "Dallo", "Dinodas", "Doddle", "Doderic", "Dodinas", "Droggo",
                 "Drogo", "Dromibar", "Dudo", "Elfstan", "Erling", "Eustace", "Everard", "Falco",
                 "Fastolph", "Fastred", "Fencon", "Ferdibrand", "Ferdinand", "Ferumbras",
                 "Filibert", "Flambard", "Folco", "Fortinbras", "Fosco", "Fredegar", "Frodo", "Gam",
                 "Gerontius", "Gorbadoc", "Gorbulas", "Gorhendad", "Gormadoc", "Gresham", "Griffo",
                 "Gundabald", "Hal", "Halfast", "Halfred", "Hamfast", "Hamson", "Harding",
                 "Hending", "Hildibrand", "Hildifons", "Hildigard", "Hildigrim", "Hob", "Hobson",
                 "Holfast", "Holman", "Hugo", "Ilberick", "Isembard", "Isembold", "Isengar",
                 "Isengrim", "Isumbras", "Isundras", "Jolly", "Kocho", "Largo", "Longo", "Lotho",
                 "Lotto", "Madoc", "Maitlow", "Manlow", "Marcho", "Marmadas", "Marmadoc", "Marroc",
                 "Menegilda", "Mentha", "Merimac", "Merimas", "Merry", "Milo", "Minto", "Moro",
                 "Mosco", "Muggrath", "Mungo", "Muzgash", "Nick", "Nob", "Odo", "Odovacar", "Olo",
                 "Orgulas", "Otho", "Paladin", "Pencho", "Permagin", "Pippin", "Pollo", "Polo",
                 "Ponto", "Porto", "Posco", "Reginard", "Robin", "Rorimac", "Rudigar", "Rufus",
                 "Sadoc", "Samwise", "Sancho", "Saradas", "Saradoc", "Seredic", "Sigismond", "Ted",
                 "Thoddo", "Tobold", "Togo", "Tolman", "Tom", "Tully", "Tunny", "Uklurg", "Wag",
                 "Wilcome", "Wilibald", "Will", "Willie", "Wiseman", "Worshem", "Zarbag"],
                ["Adamantha", "Angelica", "Asphodel", "Baromba", "Belba", "Bell", "Beryl", "Calamy",
                 "Camellia", "Celandine", "Chica", "Dahlia", "Daisy", "Diamond", "Donnamira",
                 "Dora", "Eglantine", "Elanor", "Esmeralda", "Estella", "Fairly", "Gilly",
                 "Goldilocks", "Hanna", "Hilda", "Holly", "Laura", "Leffly", "Lily", "Linda",
                 "Lobelia", "Lolly", "Malva", "Margott", "Marigold", "May", "Mayferry", "Melilot",
                 "Mimosa", "Mirabella", "Molly", "Myrtle", "Pansy", "Pearl", "Peony", "Pervinca",
                 "Pimpernel", "Poppy", "Precious", "Primrose", "Primula", "Prisca", "Rosa",
                 "Rosamunda", "Rose", "Rowan", "Ruby", "Salvia", "Tanta"]
            ],
            "Orc":
            [
                ["One-Fang", "Akargûn", "Arthrug", "Arthuan", "Azog", "Balcmeg", "Balkhmog",
                 "Barfka", "Bokdankh", "Bolg", "Bolvag", "Bralg", "Bugrug", "Bukra", "Bulkupar",
                 "Cro", "Dakalmog", "Daumdorût", "Dolgrist", "Dorglas", "Drurgandra", "Dunadd",
                 "Durba", "Durg-Orsh", "Fektalgh", "Fha-khorlash", "Forak", "Gaballol", "Garg",
                 "Garny", "Gaskbuz", "Ghardak", "Ghashurlagk", "Glashtoc", "Gorbag", "Gorbla",
                 "Gormuk", "Gorron", "Gorthak", "Grac", "Grachuk", "Grashukh", "Grashûkh",
                 "Grashur", "Grishnákh", "Grizbat", "Hagrakh", "Hukor", "Hurog", "Ikgor", "Karagat",
                 "Kargmaushat", "Kharghiz", "Lagduf", "Leegrash", "Lug", "Lugdush", "Lurd",
                 "Lurshas", "Lurshras", "Luzog", "Malkur", "Marlug", "Maugrath", "Mauhúr", "Mogshi",
                 "Mordanak", "Muagan", "Nadash", "Nagan", "Narkga", "Narlga", "Natak", "Nazog",
                 "Nurgash", "Nurl", "Obad", "Ogrod", "One Fang", "Orcobal", "Orthrod", "Pochack",
                 "Radbug", "Ragavaug", "Rashkûk", "Rask", "Regdûk", "Rekka", "Rhukska", "Rugat",
                 "Rulthak", "Savgak", "Scutsparg", "Shagog", "Shagrat", "Shagrath", "Shagrug",
                 "Shardakh", "Sharzig", "Shergnakh", "Skargnakh", "Skoralg", "Snaga", "Storlaga",
                 "Strulug", "Thergor", "Ufthak", "Uftog", "Ugluk", "Ukog", "Ukrish", "Ulgin",
                 "Ulzog", "Unhir", "Urfa", "Urfase", "Urgubal", "Urgurk", "Urmek", "Urudrak",
                 "Utor", "Utsar", "Uunk", "Virsh", "Volog", "Wargiz", "Yagrash", "Yazhgar", "Zalg",
                 "Zurtak"],
                []
            ]
        }

    def get_races(self):
        """
        Returns the set of races in the database.
        :return: String containing the name of each race in the database.
        """
        trace.entry()
        trace.detail("Name database length %r" % len(self.name_database))
        trace.exit()
        return sorted(self.name_database.keys())

    def set_race(self, race):
        """
        Updates variables following a change to requested race.
        :param race: The requested race.
        """
        trace.detail("Set race to %r" % race)
        self.current_race = race
        self.males = self.name_database[race][0]
        self.females = self.name_database[race][1]
        trace.detail("Number of males %r" % len(self.males))
        trace.detail("Number of females %r" % len(self.females))

    def get_num_males(self):
        """
        Returns the number of male names in the current database.
        :return:
        """
        return len(self.males)

    def get_num_females(self):
        """
        Returns the number of female names in the current database.
        """
        return len(self.females)

    def get_male(self):
        """
        Returns a male name.
        """
        roll = dice.dcustom(len(self.males))
        trace.detail("Roll %r, gives %s" % (roll, self.males[roll-1]))
        return self.males[roll - 1]

    def get_female(self):
        """
        Returns a female name.
        """
        roll = dice.dcustom(len(self.females))
        trace.detail("Roll %r, gives %s" % (roll, self.females[roll-1]))
        return self.females[roll - 1]

    def get_either(self):
        """
        Returns a name that is either male or female.
        :return: The name returned, including a gender identifier.
        """
        max_number = len(self.males) + len(self.females)
        roll = dice.dcustom(max_number)
        trace.detail("Roll %r" % roll)
        trace.detail("Number of males %r" % len(self.males))
        if roll <= len(self.males):
            male: str = self.males[roll - 1]
            trace.detail("Return %s" % male)
            return male + " (M)"
        else:
            roll = roll - len(self.males)
            trace.detail("Roll now %r" % roll)
            trace.detail("Return %s" % self.females[roll-1])
            female: str = self.females[roll - 1]
            trace.detail("Return %s" % female)
            return female + " (F)"
