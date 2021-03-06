#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file is part of swnamer.
# https://github.com/heynemann/swnamer

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2014 Bernardo Heynemann heynemann@gmail.com

PLANETS_LIST = (
    'Raxus-Prime',
    'Alderaan',
    'Anoat',
    'Ansion',
    'Bespin',
    'Bogden',
    'Boz-Pity',
    'Cato-Neimoidia',
    'Centax-1',
    'Centax-2',
    'Centax-3',
    'Chenini',
    'Corellia',
    'Coruscant',
    'Dagobah',
    'Dantooine',
    'Endor',
    'Felucia',
    'Geonosis',
    'Ghomrassen',
    'Guermessa',
    'Hesperidium',
    'Hoth',
    'Iego',
    'Jestefad',
    'Kamino',
    'Kashyyyk',
    'Kessel',
    'Malastare',
    'Mustafar',
    'Mygeeto',
    'Naboo',
    'Nar-Shaddaa',
    'Ohma-Dun',
    'Ord-Mantell',
    'Polis-Massa',
    'Rori',
    'Saleucami',
    'Subterrel',
    'Sullust',
    'Taanab',
    'Tatooine',
    'Tund',
    'Utapau',
    'Utapau-7',
    'Yavin',
    'Yavin-IV',
)

SPECIES_LIST = (
    "Abyssin",
    "Aleena",
    "Amanin",
    "Ansionian",
    "Anomid",
    "Annoo-dat",
    "Anx",
    "Anzati",
    "Aqualish",
    "Arcona",
    "Argazdan",
    "Arkanian",
    "Aruzan",
    "Askajian",
    "Assembler",
    "Balosar",
    "Bando-Gora",
    "Barabel",
    "Besalisk",
    "Bimm",
    "Bith",
    "Blood-Carver",
    "Boltrunians",
    "Bomarr-Monks",
    "Bothan",
    "Bouncer",
    "Caamasi",
    "Cathar",
    "Carondian",
    "Celegian",
    "Cerean",
    "Chadra-Fan",
    "Chagrian",
    "Chazrach",
    "Chiss",
    "Chistori",
    "Clawdite",
    "Codru-Ji",
    "Coway",
    "Croke",
    "Dantari",
    "Dashade",
    "Defel",
    "Devaronian",
    "Drachnam",
    "Draethos",
    "Drall",
    "Dressellian",
    "Droch",
    "Droid",
    "Drovian",
    "Dug",
    "Duros",
    "Echani",
    "Elom",
    "Elomin",
    "Epicanthix",
    "ErKit",
    "Ewok",
    "Evocii",
    "Falleen",
    "Far-Outsiders",
    "Feeorin",
    "Ferroans",
    "Firrerreo",
    "Fosh",
    "Frozian",
    "Frozarns",
    "Gado",
    "Gamorrean",
    "Gand",
    "Gank",
    "GenDai",
    "Gerb",
    "Geonosian",
    "Givin",
    "Gizka",
    "Glymphid",
    "Gorax",
    "Gorith",
    "Gorog",
    "Gossam",
    "Gotal",
    "Gran",
    "Gree",
    "Grizmallt",
    "Gungan",
    "Gwurran",
    "Habassa",
    "Hallotan",
    "Hapan",
    "Himoran",
    "Hnemthean",
    "Hoojib",
    "Huk",
    "Human",
    "Hssis",
    "Hutt",
    "Iktotchi",
    "Iridonian",
    "Ishi-Tib",
    "Ithorian",
    "Jabiimas",
    "Jawa",
    "Kaleesh",
    "Kaminoan",
    "Kel-Dor",
    "Keshiri",
    "Kiffar",
    "Kitonak",
    "Klatooinian",
    "Kobok",
    "Kowakian-Monkey-Lizard",
    "Kubaz",
    "Kurtzen",
    "Kushiban",
    "Kwa",
    "Kwi",
    "Lannik",
    "Latter",
    "Lepi",
    "Letaki",
    "Lurmen",
    "Mandalorians",
    "Massassi",
    "Melodie",
    "Mimbanite",
    "Miraluka",
    "Mirialan",
    "Mon-Calamari",
    "Mustafarian",
    "Muun",
    "Myneyrsh",
    "Myriad",
    "Nagai",
    "Nautolan",
    "Neimoidian",
    "Nelvaanian",
    "Neti",
    "Nikto",
    "Noghri",
    "Nosaurian",
    "Ogemite",
    "Omwati",
    "Ongree",
    "Ortolan",
    "Oswaft",
    "Palowick",
    "Paaerduag",
    "Pauan",
    "Phlog",
    "Polis-Massans",
    "Priapulin",
    "Psadan",
    "Pweck",
    "Quarren",
    "Quermian",
    "Rakata",
    "Ranat",
    "Rishii",
    "Rodian",
    "Roonan",
    "Ruurian",
    "Ryn",
    "Rattataki",
    "Saffa",
    "Sanyassan",
    "Saurin",
    "Selkath",
    "Selonian",
    "Shawda-Ubb",
    "Shiido",
    "Shistavanen",
    "Sikan",
    "Sith",
    "Skakoan",
    "Sneevel",
    "Snivvian",
    "Squib",
    "Ssi-Ruuk",
    "Stereb",
    "Sullustan",
    "Talortai",
    "Tarasin",
    "Talz",
    "Taung",
    "Tchuukthai",
    "Teek",
    "Teevan",
    "Thakwaash",
    "Theelin",
    "Thennqora",
    "Terentatek",
    "Thisspiasian",
    "Thrella",
    "Timoliini",
    "Tlanda-Til",
    "Tof",
    "Togorian",
    "Togruta",
    "Toydarian",
    "Trandoshan",
    "Trianii",
    "Troig",
    "Tunroth",
    "Tusken-Raider",
    "Twilek",
    "Ubese",
    "Ugnaught",
    "Umbaran",
    "Unu",
    "Utai",
    "Utapaun",
    "Vaathkree",
    "Vagaari",
    "Veknoid",
    "Vella",
    "Verpine",
    "Vodran",
    "Vor",
    "Voxyn",
    "Vratix",
    "Vulptereen",
    "Vurk",
    "Wampa",
    "Weequay",
    "Whaladon",
    "Wharl",
    "Whill",
    "Whiphid",
    "Wirutid",
    "Wol-Cabasshite",
    "Wookiee",
    "Woostoid",
    "Wroonian",
    "Xting",
    "Xexto",
    "Ybith",
    "Yaka",
    "Yevetha",
    "Yuuzhan-Vong",
    "Yuvernian",
    "Yuzzem",
    "Yuzzum",
    "Zabrak",
    "Zeltron",
    "Zhell",
    "Zygerrian",
)

CHARACTER_LIST = (
    'Ask-Aak',
    'Abeloth',
    'Gial-Ackbar',
    'Acros-Krik',
    'King-Adas',
    'Ak-Rev',
    'Stass-Allie',
    'Almec',
    'Mas-Amedda',
    'Amee',
    'Padme-Amidala',
    'Darth-Andeddu',
    'Nom-Anor',
    'Bail-Antilles',
    'Raymus-Antilles',
    'Wedge-Antilles',
    'Queen-Apailana',
    'Appo',
    'Passel-Argente',
    'Faro-Argyus',
    'Seti-Ashgad',
    'Attichitcuk',
    'Tavion-Axmis',
    'Azrakel',
    'Azzameen-Family',
    'Ponda-Baba',
    'Kitster-Banai',
    'Darth-Bandon',
    'Cad-Bane',
    'Darth-Bane',
    'Moradmin-Bast',
    'Beed',
    'Garm-Bel-Iblis',
    'Sio-Bibble',
    'Depa-Billaba',
    'Jar-Jar-Binks',
    'Deliah-Blue',
    'Blue-Max',
    'Bly',
    'Bossk',
    'Bollux',
    'Lux-Bonteri',
    'Mina-Bonteri',
    'Borvo-the-Hutt',
    'Empatojayos-Brand',
    'Malcor-Brashin',
    'Noa-Briqualon',
    'Maris-Brood',
    'Sora-Bulq',
    'C-3PO',
    'Darth-Caedus',
    'Lando-Calrissian',
    'Yomin-Carr',
    'Joruus-Cbaoth',
    'Tycho-Celchu',
    'Kadlah-Cha',
    'Wyrpuuk-Cha',
    'Charal',
    'Chewbacca',
    'Chine-kal',
    'Chief-Chirpa',
    'Nas-Choka',
    'Shok-Choka',
    'Rush-Clovis',
    'Cody',
    'Darth-Cognus',
    'Jeremoch-Colton',
    'Corde',
    'Airen-Cracken',
    'Cradossk',
    'Salacious-Crumb',
    'Arvel-Crynyd',
    'Figrin-Dan',
    'Natasi-Daala',
    'DaGara',
    'Hego-Damask',
    'Joclad-Danva',
    'Biggs-Darklighter',
    'Oro-Dassyne',
    'Gizor-Delso',
    'Dengar',
    'Bren-Derlin',
    'Desann',
    'Darth-Desolous',
    'Dharhan',
    'Ima-Gun-Di',
    'Vilim-Disra',
    'Teneniel-Djo',
    'Lott-Dod',
    'Jan-Dodonna',
    'Daultay-Dofine',
    'Count-Dooku',
    'Dormé',
    'Cin-Drallig',
    'Hiram-Drayson',
    'Dunhausen',
    'Dunwell',
    'Lok-Durd',
    'Durge',
    'Kyp-Durron',
    'Echo',
    'Juno-Eclipse',
    'Bant-Eerin',
    'Ebe-Endocott',
    'Eirtaé',
    'Elan',
    'Embo',
    'Emtrey',
    'EV-9D9',
    'Morallo-Eval',
    'Cornelius-Evazan',
    'Ezra-Bridger',
    'Keyan-Farlander',
    'Onaconda-Farr',
    'Jagged-Fel',
    'Roan-Fel',
    'Soontir-Fel',
    'Davin-Felth',
    'Jango-Fett',
    'Boba-Fett',
    'Borsk-Feylya',
    'Kit-Fisto',
    'Fives',
    'Bib-Fortuna',
    'Fox',
    'Adi-Gallia',
    'Ganodi',
    'Gardulla-the-Hutt',
    'Nautag-Dal-Gargan-II',
    'Garindan',
    'Saw-Gerrera',
    'Steela-Gerrera',
    'Mirta-Gev',
    'Joelle-Golda',
    'Gonk-Droid',
    'Greeata',
    'Gree',
    'Greedo',
    'Janus-Greejatus',
    'Falon-Grey',
    'General-Grievous',
    'Gungi',
    'Nute-Gunray',
    'Rune-Haako',
    'Rako-Hardeen',
    'Harrar',
    'Hera-Syndulla',
    'ASharad-Hett',
    'Hevy',
    'San-Hill',
    'Bertroff-Hissa',
    'Corran-Horn',
    'Huyang',
    'Ikrit',
    'Armand-Isard',
    'Ysanne-Isard',
    'Irek-Ismaren',
    'Prince-Isolder',
    'Jabba-the-Hutt',
    'Mara-Jade-Skywalker',
    'Shimrra-Jamaane',
    'Queen-Jamillia',
    'Wes-Janson',
    'Jarael',
    'Carnor-Jax',
    'Jedgar',
    'Jek-14',
    'Jerec',
    'Jerjerrod',
    'Jet',
    'Dexter-Jettster',
    'Qui-Gon-Jinn',
    'Jubnuk',
    'Bardan-Jusik',
    'Tenel-Ka',
    'Tee-Watt-Kaa',
    'Kadann',
    'Kael',
    'Kir-Kanos',
    'Saul-Karath',
    'Karina-the-Great',
    'Talon-Karrde',
    'Jodo-Kast',
    'Kyle-Katarn',
    'King-Katuunko',
    'Coleman-Kcaj',
    'Obi-Wan-Kenobi',
    'Gavar-Khai',
    'Vestara-Khai',
    'Ki-Adi-Mundi',
    'Klaatu',
    'Kleef',
    'Ken',
    'Derek-Klivian',
    'Agen-Kolar',
    'Plo-Koon',
    'Jaden-Korr',
    'Rahm-Kota',
    'Krayn',
    'Darth-Krayt',
    'Pong-Krell',
    'Ludo-Kressh',
    'KKruhk',
    'Satine-Kryze',
    'Exar-Kun',
    'Anya-Kuro',
    'Tsavong-Lah',
    'Beru-Lars',
    'Cliegg-Lars',
    'Owen-Lars',
    'Bevel-Lemelisk',
    'Xamuel-Lennox',
    'Lobot',
    'Logray',
    'Lowbacca',
    'Lumiya',
    'Crix-Madine',
    'Shu-Mai',
    'Mako',
    'Darth-Malak',
    'Malé-Dee',
    'Darth-Malgus',
    'Mama-the-Hutt',
    'Ody-Mandrell',
    'Galen-Marek',
    'Kento-Marek',
    'Darth-Marr',
    'Darth-Maul',
    'Mawhonic',
    'Droopy-McCool',
    'Pharl-McQuarrie',
    'Lyn-Me',
    'Tion-Medon',
    'Darth-Millennial',
    'General-Rom-Mohc',
    'Kasan-Moor',
    'Sly-Moore',
    'Morley',
    'Mon-Mothma',
    'Conan-Antonio-Motti',
    'Kudar-Mubat',
    'Karness-Muur',
    'Muzzer',
    'Jobal-Naberrie',
    'Pooja-Naberrie',
    'Ruwee-Naberrie',
    'Ryoo-Naberrie',
    'Sola-Naberrie',
    'Freedon-Nadd',
    'Momaw-Nadon',
    'Boss-Rugor-Nass',
    'Lorth-Needa',
    'Queen-Neeyutnee',
    'Darth-Nihl',
    'Darth-Nihilus',
    'Ona-Nobis',
    'Chopaa-Notimo',
    'Jocasta-Nu',
    'Po-Nudo',
    'Nien-Nunb',
    'Astri-Oddo',
    'Barriss-Offee',
    'Hondo-Ohnaka',
    'Ric-Olie',
    'Ferus-Olin',
    'Solace-Olin',
    'Cal-Omas',
    'Omega-Squad',
    'Granta-Omega',
    'Carth-Onasi',
    'Onimi',
    'Oola',
    'Savage-Opress',
    'Canderous-Ordo',
    'Bail-Prestor-Organa',
    'Queen-Breha-Organa',
    'Princess-Leia-Organa',
    'Orrin',
    'Jan-Ors',
    'General-Otto',
    'Kendal-Ozzel',
    'Pablo-Jill',
    'Ajunta-Pall',
    'Emperor-Palpatine',
    'Captain-Panaka',
    'Baron-Papanoida',
    'Chi-Eekway-Papanoida',
    'Paploo',
    'Kazdan-Paratus',
    'Jax-Pavan',
    'Gilad-Pellaeon',
    'Rosh-Penin',
    'Sate-Pestage',
    'Even-Piell',
    'Firmus-Piett',
    'Darth-Plagueis',
    'Poggle-the-Lesser',
    'Yarael-Poof',
    'Jek-Tono-Porkins',
    'Nahdonnis-Praji',
    'Pugwis-',
    'Ulic-Qel-Droma',
    'Ooryl-Qrygg',
    'Ben-Quadrinaros',
    'Danni-Quee',
    'Sarcev-Quest',
    'Malavi-Quinn',
    'Vuffi-Raa',
    'Ahri-Raas',
    'Rabe',
    'Marka-Ragnos',
    'Qu-Rahn',
    'Dak-Ralter',
    'Oppo-Rancisis',
    'Rappertunie',
    'Max-Rebo',
    'Dash-Rendar',
    'Gualt-Rennow',
    'Ree-Yees',
    'Revan',
    'Rex',
    'Carlist-Rieekan',
    'Rogue-Squadron',
    'Rookie-One',
    'Rotta-the-Hutt',
    'Rukh',
    'Sabe',
    'Sache',
    'Naga-Sadow',
    'Sage-Boneria',
    'Sarkli',
    'Sarn',
    'Miraj-Scintel',
    'Saba-Sebatyne',
    'Sebulba',
    'Aayla-Secura',
    'Kohl-Seerdon',
    'Zev-Senesca',
    'Shedao-Shai',
    'Bastila-Shan',
    'Satele-Shan',
    'Echuu-Shen-Jon',
    'Garris-Shrike',
    'Darth-Sidious',
    'Sifo-Dyas',
    'Aurra-Sing',
    'Darth-Sion',
    'Kal-Skirata',
    'Anakin-Skywalker',
    'Ben-Skywalker',
    'Cade-Skywalker',
    'Kol-Skywalker',
    'Luke-Skywalker',
    'Shmi-Skywalker',
    'Sy-Snootles',
    'Osi-Sobeck',
    'Anakin-Solo',
    'Allana-Solo',
    'Han-Solo',
    'Jaina-Solo',
    'Thrackan-Sal-Solo',
    'Uta-Sorn',
    'Maarek-Stele',
    'Ozzik-Sturn',
    'Lama-Su',
    'Sugi',
    'Nomi-Sunrider',
    'Meetra-Surik',
    'Gavyn-Sykes',
    'Cham-Syndulla',
    'Orn-Free-Taa',
    'Siri-Tachi',
    'Cassio-Tagge',
    'Tahl',
    'Darth-Talon',
    'Mother-Talzin',
    'Wat-Tambor',
    'Riff-Tamson',
    'Sevrance-Tann',
    'Ahsoka-Tano',
    'Tarfful',
    'Wilhuff-Tarkin',
    'Merillion-Tarko',
    'Roos-Tarpals',
    'Teebo',
    'Booster-Terrik',
    'Mirax-Terrik',
    'Mod-Terrik',
    'Tessek',
    'Bria-Tharen',
    'Thire',
    'Thistleborn',
    'Thrawn',
    'Raynar-Thul',
    'Shaak-Ti',
    'Ace-Tiberious',
    'Tibor',
    'Grodin-Tierce',
    'Rufaan-Tigellinus',
    'Saesee-Tiin',
    'Tikkes',
    'Meena-Tills',
    'Wag-Too',
    'Darth-Traya',
    'Coleman-Trebor',
    'Si-Treemba',
    'Antinnis-Tremayne',
    'Trench',
    'Triclops',
    'Trioculus',
    'Longo-Two-Guns',
    'Gregar-Typho',
    'Darth-Tyranus',
    'Luminara-Unduli',
    'Darth-Vader',
    'Finis-Valorum',
    'Shado-Vao',
    'Walon-Vau',
    'Nahdar-Vebb',
    'Morlish-Veed',
    'Maximilian-Veers',
    'Tahiri-Veila',
    'Ailyn-Vel',
    'Sintas-Vel',
    'Asajj-Ventress',
    'Vergere',
    'Vette',
    'Vima-Da-Boda',
    'Nuvo-Vindi',
    'Pre-Vizsla',
    'Quinlan-Vos',
    'Komari-Vosa',
    'Wald',
    'Warlug',
    'Warok',
    'Wicket-Warrick',
    'Watto',
    'Watts',
    'Taun-We',
    'Zam-Wesell',
    'Beru-Whitesun',
    'Mace-Windu',
    'Winter',
    'Wittin',
    'Wolffe',
    'Wuher',
    'Darth-Wyyrlok',
    'Xanatos',
    'Prince-Xizor',
    'Yaddle',
    'Yane',
    'Yoda',
    'Joh-Yowza',
    'Wullf-Yularen',
    'Zaalbar',
    'Jenna-Zan-Arbor',
    'Tyber-Zann',
    'Darth-Zannah',
    'Fang-Zar',
    'Zekk',
    'Ziro-the-Hutt',
    'Zorba-the-Hutt',
    'Zuckuss',
    'Commodore-Zuggs',
)
