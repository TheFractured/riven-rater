URL = {
    'base': 'https://{proxy}.api.pvp.net/api/lol/{region}/{url}',
    'summoner_by_name': 'v{version}/summoner/by-name/{names}',
    'stats': 'v{version}/stats/by-summoner/{summonerId}',
    'champion_mastery': '/championmastery/location/{platformId}/player/{playerId}/champion/{championId}',
    'champion_mastery_base': 'https://{proxy}.api.pvp.net/{url}',
    'champion.gg': 'http://api.champion.gg'
}

API_VERSIONS = {
    'summoner': '1.4',
    'champion': '1.2',
    'stats': '1.3',
    'champion_mastery': ''
}

REGIONS = {
    'north_america': 'na',
    'global': 'global'
}

LOCATION = {
    'north_america': 'NA1'
}

SUMMONER_ID = {
    'thefracturedmind': '29175220',
    'fee1sbadman': '32719776'
}

SEASON = {
    'Season_2016': 'SEASON2016'
}

MASTERIES = {
    '6142': 'Oppressor: Deal 2.5% increased damage to targets with impaired movement (slow, stun, root, taunt, etc.)',
    '6141': 'Bounty Hunter: Deal 1% increased damage for each unique enemy champion you have killed',
    '6121': 'Double Edged Sword: Melee: Deal 3% additional damage, take 1.5% additional damage. Ranged: Deal and take 2% additional damage',
    '6122': 'Feast: Killing a unit restores 20 Health (25 second cooldown)',
    '6161': 'Warlord\'s Bloodlust: Your critical strikes on enemy champions heal you for 5%-25% of the damage dealt (based on your level) and grant you 30% attack speed for 4 seconds (2 second cooldown)',
    '6162': 'Fervor of Battle: You generate stacks of Fervor by hitting enemy champions with attacks and abilities. Your basic attacks deal 1-14 bonus physical damage (based on your level) to enemy champions for each of your stacks of Fervor (max 8 stacks).Attacking enemy champions generates 1 stack of Fervor (2 for melee champions) and damaging enemy champions with an ability generates 2 stacks of Fervor (2 second cooldown). Stacks of Fervor last 6 seconds.',
    '6164': 'Deathfire Touch: Your damaging abilities cause enemy champions to take additional magic damage equal to 8 + 60% of your Bonus Attack Damage and 25% of your Ability Power, over 4 seconds. <br><br>Deathfire Touch has reduced effectiveness when applied by area of effect and damage over time abilities.<br>     - Area of Effect: 2 second duration. <br>     - Damage over time: 1 second duration.',
    '6343': 'Dangerous Game: Champion kills and assists restore 5% of your missing Health and Mana',
    '6342': 'Bandit: Gain 1 gold for each nearby minion killed by an ally. Gain 3 gold (10 if melee) when hitting an enemy champion with a basic attack (5 second cooldown)',
    '6262': 'Strength of the Ages: Siege minions and large monsters that you or nearby allied champions kill grant 20 and 10 permanent Health, respectively (300 max). After reaching the max bonus, these kills instead restore 6% of your Maximum Health.',
    '6263': '+4% Damage Reduction. 6% of the damage from enemy champions taken by the nearest allied champion is dealt to you instead. Damage is not redirected if you are below 5% of your maximum health.' 'Bond of Stone',
    '6261': 'Grasp of the Undying: Every 4 seconds in combat your next attack against an enemy champion steals life equal to 3% of your max Health (halved for ranged champions, deals magic damage)',
    '6223': 'Tough Skin You take 2 less damage from champion and neutral monster basic attacks',
    '6221': 'Explorer: +15 Movement Speed in Brush and River',
    '6323': 'Assassin: Deal 2% increased damage to champions when no allied champions are nearby',
    '6322': 'Secret Stash: Your Potions and Elixirs last 10% longer.<br><br>Your Health Potions are replaced with Biscuits that restore 20 Health and 10 Mana instantly on use',
    '6321': 'Runic Affinity: Buffs from neutral monsters last 15% longer',
    '6363': 'Windspeaker\'s Blessing: Your heals and shields are 10% stronger. Additionally, your shields and heals on other allies increase their armor by 5-22 (based on level) and their magic resistance by half that amount for 3 seconds.',
    '6362': 'Thunderlord\'s Decree: Your 3rd attack or damaging spell against the same enemy champion calls down a lightning strike, dealing magic damage in the area. Damage: 10 per level, plus 30% of your Bonus Attack Damage, and 10% of your Ability Power (25-15 second cooldown, based on level).',
    '6361': 'Stormraider\'s Surge:Dealing 30% of a champion\'s max Health within 2.5 seconds grants you 40% Movement Speed and 75% Slow Resistance for 3 seconds (10 second cooldown).',
    '6212': 'Unyielding: +5% Bonus Armor and Magic Resist',
    '6211': 'Recovery: +2.0 Health per 5 seconds',
    '6151': 'Battering Blows: +7% Armor Penetration',
    '6154': 'Piercing Thoughts: +7% Magic Penetration',
    '6241': 'Insight: Reduces the cooldown of Summoner Spells by 15%',
    '6242': 'Perseverance: +50% Base Health Regen, increased to +200% when below 25% Health',
    '6352': 'Intelligence: Your Cooldown Reduction cap is increased to 45% and you gain 5% Cooldown Reduction',
    '6351': 'Precision: Gain 3 + 0.3 per level Magic Penetration and Armor Penetration',
    '6114': 'Sorcery: +2.0% increased Ability damage',
    '6131': 'Vampirism: +2.0% Lifesteal and Spell Vamp',
    '6111': 'Fury: +4% Attack Speed',
    '6134': 'Natural Talent: +10 Attack Damage and 15 Ability Power at level 18 (0.55 Attack Damage and 0.83 Ability Power per level)',
    '6312': 'Savagery: Single target attacks and spells deal 5 bonus damage to minions and monsters',
    '6311': 'Wanderer: +3% Movement Speed out of combat',
    '6331': 'Merciless: Deal 5% increased damage to champions below 40% Health',
    '6332': 'Meditation: Regenerate 1.5% of your missing Mana every 5 seconds',
    '6252': 'Legendary Guardian: +3 Armor and Magic Resist for each nearby enemy champion',
    '6251': 'Swiftness: +15% Tenacity and Slow Resist',
    '6231': 'Runic Armor: Shields, healing, regeneration, and lifesteal on you are 8% stronger',
    '6232': 'Veteran\'s Scars: +45 Health'
}

CHAMPION_ID = {
    'Aatrox': '266',
    'Ahri': '103',
    'Akali': '84',
    'Alistar': '12',
    'Ammu': '32',
    'Anivia': '34',
    'Annie': '1',
    'Ashe': '22',
    'Azir': '268',
    'Bard': '432',
    'Blitzcrank': '53',
    'Brand': '63',
    'Braum': '201',
    'Caitlyn': '51',
    'Cassiopeia': '69',
    'Cho-Gath': '31',
    'Corki': '42',
    'Darius': '122',
    'Diana': '131',
    'Dr. Mundo': '36',
    'Draven': '119',
    'Ekko': '245',
    'Elise': '60',
    'Evelynn': '28',
    'Ezreal': '81',
    'Fiddlesticks': '9',
    'Fiora': '114',
    'Fizz': '105',
    'Galio': '3',
    'Gangplank': '41',
    'Garen': '86',
    'Gnar': '150',
    'Gragas': '79',
    'Graves': '104',
    'Hecarim': '120',
    'Heimerdinger': '74',
    'Illaoi': '420',
    'Irelia': '39',
    'Janna': '40',
    'Jarvan IV': '59',
    'Jax': '24',
    'Jayce': '126',
    'Jhin': '202',
    'Jinx': '222',
    'Kalista': '429',
    'Karma': '43',
    'Karthus': '30',
    'Kassadin': '38',
    'Katarina': '55',
    'Kayle': '10',
    'Kennen': '85',
    'Kha-Zix': '121',
    'Kindred': '203',
    'Kog-Maw': '96',
    'LeBlanc': '7',
    'Lee Sin': '64',
    'Leona': '89',
    'Lissandra': '127',
    'Lucian': '236',
    'Lulu': '117',
    'Lux': '99',
    'Malphite': '54',
    'Malzahar': '90',
    'Maokai': '54',
    'Master Yi': '11',
    'Miss Fortune': '21',
    'Mordekaiser': '82',
    'Morgana': '25',
    'Nami': '267',
    'Nasus': '75',
    'Nautilus': '111',
    'Nidalee': '76',
    'Nocturne': '56',
    'Nunu': '20',
    'Olaf': '2',
    'Orianna': '61',
    'Pantheon': '80',
    'Poppy': '78',
    'Quinn': '133',
    'Rammus': '33',
    'Rek-Sai': '421',
    'Renekton': '58',
    'Rengar': '107',
    'Riven': '92',
    'Rumble': '68',
    'Ryze': '13',
    'Sejuani': '113',
    'Shaco': '35',
    'Shen': '98',
    'Shyvana': '102',
    'Singed': '27',
    'Sion': '14',
    'Sivir': '15',
    'Skarner': '72',
    'Sona': '37',
    'Soraka': '16',
    'Swain': '50',
    'Syndra': '134',
    'Tahm Kench': '223',
    'Talon': '91',
    'Taric': '44',
    'Teemo': '17',
    'Thresh': '412',
    'Tristana': '18',
    'Trundle': '48',
    'Tryndamere': '23',
    'Twisted Fate': '4',
    'Twitch': '29',
    'Udyr': '77',
    'Urgot': '6',
    'Varus': '110',
    'Vayne': '67',
    'Veigar': '45',
    'Vel-Koz': '161',
    'Vi': '254',
    'Viktor': '112',
    'Vladimir': '8',
    'Volibear': '106',
    'Warwick': '19',
    'Wukong': '62',
    'Xerath': '101',
    'Xin Zhao': '5',
    'Yaso': '157',
    'Yorick': '83',
    'Zac': '154',
    'Zed': '238',
    'Ziggs': '115',
    'Zilean': '26',
    'Zyra': '143'
}