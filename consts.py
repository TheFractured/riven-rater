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

#TODO: Change this to static data API call
MASTERIES = {
    '6123': 'Expose Weakness: Damaging enemy champions causes them to take 3% more damage from your allies',
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

#TODO: Change this to a call to the Static Data API to maintain all champion ID's
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

#TODO: Change this to an API call to Riot's static data API
RUNES = {
      "5235": {
         "id": 5235,
         "description": "+3.85 ability power",
         "name": "Quintessence of Ability Power",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "black"
         }
      },
      "5234": {
         "id": 5234,
         "description": "-0.21% cooldowns per level (-3.9% at champion level 18)",
         "name": "Quintessence of Scaling Cooldown Reduction",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "black"
         }
      },
      "5233": {
         "id": 5233,
         "description": "-1.95% cooldowns",
         "name": "Quintessence of Cooldown Reduction",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "black"
         }
      },
      "5370": {
         "id": 5370,
         "description": "+0.064 Energy regen/5 sec per level (+1.15 at champion level 18)",
         "name": "Greater Seal of Scaling Energy Regeneration",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "yellow"
         }
      },
      "5230": {
         "id": 5230,
         "description": "+0.22 health regen / 5 sec. per level (+3.96 at champion level 18)",
         "name": "Quintessence of Scaling Health Regeneration",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "black"
         }
      },
      "8016": {
         "id": 8016,
         "description": "+1.39% movement speed",
         "name": "Quintessence of the Speedy Specter",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "black"
         }
      },
      "5374": {
         "id": 5374,
         "description": "+5.4 Energy",
         "name": "Greater Quintessence of Energy",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "black"
         }
      },
      "8015": {
         "id": 8015,
         "description": "+24 health",
         "name": "Quintessence of Bountiful Treats",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "black"
         }
      },
      "5373": {
         "id": 5373,
         "description": "+1.575 Energy regen/5 sec",
         "name": "Greater Quintessence of Energy Regeneration",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "black"
         }
      },
      "5372": {
         "id": 5372,
         "description": "+0.161 Energy/level (+2.89 at level 18)",
         "name": "Greater Glyph of Scaling Energy",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "blue"
         }
      },
      "8017": {
         "id": 8017,
         "description": "+4.56 ability power",
         "name": "Quintessence of the Witches Brew",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "black"
         }
      },
      "5371": {
         "id": 5371,
         "description": "+2.2 Energy",
         "name": "Greater Glyph of Energy",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "blue"
         }
      },
      "8012": {
         "id": 8012,
         "description": "-0.75% cooldowns",
         "name": "Glyph of the Soaring Slalom",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "blue"
         }
      },
      "8011": {
         "id": 8011,
         "description": "+0.66 ability power",
         "name": "Lesser Glyph of the Challenger",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "blue"
         }
      },
      "8014": {
         "id": 8014,
         "description": "+1.85 magic penetration",
         "name": "Quintessence of the Piercing Screech",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "black"
         }
      },
      "8013": {
         "id": 8013,
         "description": "+2.37 armor penetration",
         "name": "Quintessence of the Headless Horseman",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "black"
         }
      },
      "5368": {
         "id": 5368,
         "description": "+2% experience gained",
         "name": "Greater Quintessence of Experience",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "black"
         }
      },
      "5369": {
         "id": 5369,
         "description": "+0.63 Energy regen/5 sec",
         "name": "Greater Seal of Energy Regeneration",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "yellow"
         }
      },
      "8008": {
         "id": 8008,
         "description": "+2% critical damage",
         "name": "Mark of the Combatant",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "red"
         }
      },
      "8009": {
         "id": 8009,
         "description": "+3.56 health",
         "name": "Lesser Seal of the Medalist",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "yellow"
         }
      },
      "5229": {
         "id": 5229,
         "description": "+2.1 health regen / 5 sec.",
         "name": "Quintessence of Health Regeneration",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "black"
         }
      },
      "5227": {
         "id": 5227,
         "description": "+3.11 magic resist",
         "name": "Quintessence of Magic Resist",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "black"
         }
      },
      "5228": {
         "id": 5228,
         "description": "+0.29 magic resist per level (+5.22 at champion level 18)",
         "name": "Quintessence of Scaling Magic Resist",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "black"
         }
      },
      "5225": {
         "id": 5225,
         "description": "+3.32 armor",
         "name": "Quintessence of Armor",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "black"
         }
      },
      "5226": {
         "id": 5226,
         "description": "+0.29 armor per level (+5.22 at champion level 18)",
         "name": "Quintessence of Scaling Armor",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "black"
         }
      },
      "8021": {
         "id": 8021,
         "description": "+26 health",
         "name": "Greater Quintessence of Frosty Health",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "black"
         }
      },
      "8020": {
         "id": 8020,
         "description": "+2.56 armor penetration",
         "name": "Greater Quintessence of the Deadly Wreath",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "black"
         }
      },
      "5221": {
         "id": 5221,
         "description": "+1.99 armor penetration",
         "name": "Quintessence of Armor Penetration",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "black"
         }
      },
      "5224": {
         "id": 5224,
         "description": "+2.1 health per level (+37.8 at champion level 18)",
         "name": "Quintessence of Scaling Health",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "black"
         }
      },
      "5223": {
         "id": 5223,
         "description": "+20 health",
         "name": "Quintessence of Health",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "black"
         }
      },
      "5361": {
         "id": 5361,
         "description": "+1.25 mana regen / 5 sec.",
         "name": "Greater Quintessence of Mana Regeneration",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "black"
         }
      },
      "5360": {
         "id": 5360,
         "description": "+4.17 mana per level (+75.06 at champion level 18)",
         "name": "Greater Quintessence of Scaling Mana",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "black"
         }
      },
      "5363": {
         "id": 5363,
         "description": "+2.01 magic penetration",
         "name": "Greater Quintessence of Magic Penetration",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "black"
         }
      },
      "5362": {
         "id": 5362,
         "description": "+0.24 mana regen / 5 sec. per level (+4.32 at champion level 18)",
         "name": "Greater Quintessence of Scaling Mana Regeneration",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "black"
         }
      },
      "5365": {
         "id": 5365,
         "description": "+1.5% movement speed",
         "name": "Greater Quintessence of Movement Speed",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "black"
         }
      },
      "5367": {
         "id": 5367,
         "description": "+1 gold / 10 sec.",
         "name": "Greater Quintessence of Gold",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "black"
         }
      },
      "8022": {
         "id": 8022,
         "description": "+1.5% movement speed",
         "name": "Greater Quintessence of Sugar Rush",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "black"
         }
      },
      "5366": {
         "id": 5366,
         "description": "-5% time dead",
         "name": "Greater Quintessence of Revival",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "black"
         }
      },
      "5357": {
         "id": 5357,
         "description": "+4.95 ability power",
         "name": "Greater Quintessence of Ability Power",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "black"
         }
      },
      "5358": {
         "id": 5358,
         "description": "+0.43 ability power per level (+7.74 at champion level 18)",
         "name": "Greater Quintessence of Scaling Ability Power",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "black"
         }
      },
      "5359": {
         "id": 5359,
         "description": "+37.5 mana",
         "name": "Greater Quintessence of Mana",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "black"
         }
      },
      "8019": {
         "id": 8019,
         "description": "+2.01 magic penetration",
         "name": "Greater Quintessence of the Piercing Present",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "black"
         }
      },
      "5219": {
         "id": 5219,
         "description": "+1.44% critical chance",
         "name": "Quintessence of Critical Chance",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "black"
         }
      },
      "5214": {
         "id": 5214,
         "description": "+0.19 attack damage per level (+3.42 at champion level 18)",
         "name": "Quintessence of Scaling Attack Damage",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "black"
         }
      },
      "5215": {
         "id": 5215,
         "description": "+3.51% attack speed",
         "name": "Quintessence of Attack Speed",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "black"
         }
      },
      "5217": {
         "id": 5217,
         "description": "+3.47% critical damage",
         "name": "Quintessence of Critical Damage",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "black"
         }
      },
      "5253": {
         "id": 5253,
         "description": "+1.28 armor penetration",
         "name": "Greater Mark of Armor Penetration",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "red"
         }
      },
      "5251": {
         "id": 5251,
         "description": "+0.93% critical chance",
         "name": "Greater Mark of Critical Chance",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "red"
         }
      },
      "5257": {
         "id": 5257,
         "description": "+0.91 armor",
         "name": "Greater Mark of Armor",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "red"
         }
      },
      "5256": {
         "id": 5256,
         "description": "+0.54 health per level (+9.72 at champion level 18)",
         "name": "Greater Mark of Scaling Health",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "red"
         }
      },
      "5255": {
         "id": 5255,
         "description": "+3.47 health",
         "name": "Greater Mark of Health",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "red"
         }
      },
      "5356": {
         "id": 5356,
         "description": "-0.28% cooldowns per level (-5% at champion level 18)",
         "name": "Greater Quintessence of Scaling Cooldown Reduction",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "black"
         }
      },
      "5355": {
         "id": 5355,
         "description": "-2.5% cooldowns",
         "name": "Greater Quintessence of Cooldown Reduction",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "black"
         }
      },
      "8035": {
         "id": 8035,
         "description": "+1.5% movement speed",
         "name": "Greater Quintessence of Studio Rumble",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "black"
         }
      },
      "5352": {
         "id": 5352,
         "description": "+0.28 health regen / 5 sec. per level (+5.04 at champion level 18)",
         "name": "Greater Quintessence of Scaling Health Regeneration",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "black"
         }
      },
      "5351": {
         "id": 5351,
         "description": "+2.7 health regen / 5 sec.",
         "name": "Greater Quintessence of Health Regeneration",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "black"
         }
      },
      "5350": {
         "id": 5350,
         "description": "+0.37 magic resist per level (+6.66 at champion level 18)",
         "name": "Greater Quintessence of Scaling Magic Resist",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "black"
         }
      },
      "5348": {
         "id": 5348,
         "description": "+0.38 armor per level (+6.84 at champion level 18)",
         "name": "Greater Quintessence of Scaling Armor",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "black"
         }
      },
      "5349": {
         "id": 5349,
         "description": "+4 magic resist",
         "name": "Greater Quintessence of Magic Resist",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "black"
         }
      },
      "5346": {
         "id": 5346,
         "description": "+2.7 health per level (+48.6 at champion level 18)",
         "name": "Greater Quintessence of Scaling Health",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "black"
         }
      },
      "5347": {
         "id": 5347,
         "description": "+4.26 armor",
         "name": "Greater Quintessence of Armor",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "black"
         }
      },
      "5249": {
         "id": 5249,
         "description": "+2.23% critical damage",
         "name": "Greater Mark of Critical Damage",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "red"
         }
      },
      "5247": {
         "id": 5247,
         "description": "+1.7% attack speed",
         "name": "Greater Mark of Attack Speed",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "red"
         }
      },
      "5240": {
         "id": 5240,
         "description": "+0.19 mana regen / 5 sec. per level (+3.42 at champion level 18)",
         "name": "Quintessence of Scaling Mana Regeneration",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "black"
         }
      },
      "5241": {
         "id": 5241,
         "description": "+1.56 magic penetration",
         "name": "Quintessence of Magic Penetration",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "black"
         }
      },
      "5243": {
         "id": 5243,
         "description": "+1.17% movement speed",
         "name": "Quintessence of Movement Speed",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "black"
         }
      },
      "5246": {
         "id": 5246,
         "description": "+0.13 attack damage per level (+2.43 at champion level 18)",
         "name": "Greater Mark of Scaling Attack Damage",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "red"
         }
      },
      "5245": {
         "id": 5245,
         "description": "+0.95 attack damage",
         "name": "Greater Mark of Attack Damage",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "red"
         }
      },
      "5343": {
         "id": 5343,
         "description": "+2.56 armor penetration",
         "name": "Greater Quintessence of Armor Penetration",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "black"
         }
      },
      "5345": {
         "id": 5345,
         "description": "+26 health",
         "name": "Greater Quintessence of Health",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "black"
         }
      },
      "5341": {
         "id": 5341,
         "description": "+1.86% critical chance",
         "name": "Greater Quintessence of Critical Chance",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "black"
         }
      },
      "5339": {
         "id": 5339,
         "description": "+4.46% critical damage",
         "name": "Greater Quintessence of Critical Damage",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "black"
         }
      },
      "5335": {
         "id": 5335,
         "description": "+2.25 attack damage",
         "name": "Greater Quintessence of Attack Damage",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "black"
         }
      },
      "5336": {
         "id": 5336,
         "description": "+0.25 attack damage per level (+4.5 at champion level 18)",
         "name": "Greater Quintessence of Scaling Attack Damage",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "black"
         }
      },
      "5337": {
         "id": 5337,
         "description": "+4.5% attack speed",
         "name": "Greater Quintessence of Attack Speed",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "black"
         }
      },
      "5236": {
         "id": 5236,
         "description": "+0.34 ability power per level (+6.12 at champion level 18)",
         "name": "Quintessence of Scaling Ability Power",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "black"
         }
      },
      "5237": {
         "id": 5237,
         "description": "+29.17 mana",
         "name": "Quintessence of Mana",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "black"
         }
      },
      "5238": {
         "id": 5238,
         "description": "+3.24 mana per level (+58.32 at champion level 18)",
         "name": "Quintessence of Scaling Mana",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "black"
         }
      },
      "5239": {
         "id": 5239,
         "description": "+0.97 mana regen / 5 sec.",
         "name": "Quintessence of Mana Regeneration",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "black"
         }
      },
      "5129": {
         "id": 5129,
         "description": "+0.72% critical chance",
         "name": "Mark of Critical Chance",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "red"
         }
      },
      "5330": {
         "id": 5330,
         "description": "+1.17 mana per level (+21.06 at champion level 18)",
         "name": "Greater Seal of Scaling Mana",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "yellow"
         }
      },
      "5127": {
         "id": 5127,
         "description": "+1.74% critical damage",
         "name": "Mark of Critical Damage",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "red"
         }
      },
      "5331": {
         "id": 5331,
         "description": "+0.41 mana regen / 5 sec.",
         "name": "Greater Seal of Mana Regeneration",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "yellow"
         }
      },
      "5332": {
         "id": 5332,
         "description": "+0.065 mana regen / 5 sec. per level (+1.17 at champion level 18)",
         "name": "Greater Seal of Scaling Mana Regeneration",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "yellow"
         }
      },
      "5400": {
         "id": 5400,
         "description": "+0.5 Armor Penetration / +0.34 Magic Penetration",
         "name": "Lesser Mark of Hybrid Penetration",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "red"
         }
      },
      "5327": {
         "id": 5327,
         "description": "+0.59 ability power",
         "name": "Greater Seal of Ability Power",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "yellow"
         }
      },
      "5131": {
         "id": 5131,
         "description": "+1 armor penetration",
         "name": "Mark of Armor Penetration",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "red"
         }
      },
      "5325": {
         "id": 5325,
         "description": "-0.36% cooldowns",
         "name": "Greater Seal of Cooldown Reduction",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "yellow"
         }
      },
      "5135": {
         "id": 5135,
         "description": "+0.71 armor",
         "name": "Mark of Armor",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "red"
         }
      },
      "5134": {
         "id": 5134,
         "description": "+0.42 health per level (+7.56 at champion level 18)",
         "name": "Mark of Scaling Health",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "red"
         }
      },
      "5329": {
         "id": 5329,
         "description": "+6.89 mana",
         "name": "Greater Seal of Mana",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "yellow"
         }
      },
      "5133": {
         "id": 5133,
         "description": "+2.7 health",
         "name": "Mark of Health",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "red"
         }
      },
      "5328": {
         "id": 5328,
         "description": "+0.1 ability power per level (+1.8 at champion level 18)",
         "name": "Greater Seal of Scaling Ability Power",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "yellow"
         }
      },
      "5115": {
         "id": 5115,
         "description": "+20.83 mana",
         "name": "Lesser Quintessence of Mana",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "black"
         }
      },
      "5116": {
         "id": 5116,
         "description": "+2.31 mana per level (+41.58 at champion level 18)",
         "name": "Lesser Quintessence of Scaling Mana",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "black"
         }
      },
      "5117": {
         "id": 5117,
         "description": "+0.69 mana regen / 5 sec.",
         "name": "Lesser Quintessence of Mana Regeneration",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "black"
         }
      },
      "5118": {
         "id": 5118,
         "description": "+0.14 mana regen / 5 sec. per level (+2.52 at champion level 18)",
         "name": "Lesser Quintessence of Scaling Mana Regeneration",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "black"
         }
      },
      "5410": {
         "id": 5410,
         "description": "+0.84% Life Steal",
         "name": "Lesser Quintessence of Life Steal",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "black"
         }
      },
      "5320": {
         "id": 5320,
         "description": "+0.1 magic resist per level (+1.8 at champion level 18)",
         "name": "Greater Seal of Scaling Magic Resist",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "yellow"
         }
      },
      "5119": {
         "id": 5119,
         "description": "+1.11 magic penetration",
         "name": "Lesser Quintessence of Magic Penetration",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "black"
         }
      },
      "5411": {
         "id": 5411,
         "description": "+1.17% Life Steal",
         "name": "Quintessence of Life Steal",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "black"
         }
      },
      "5321": {
         "id": 5321,
         "description": "+0.56 health regen / 5 sec.",
         "name": "Greater Seal of Health Regeneration",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "yellow"
         }
      },
      "5322": {
         "id": 5322,
         "description": "+0.11 health regen / 5 sec. per level (+1.98 at champion level 18)",
         "name": "Greater Seal of Scaling Health Regeneration",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "yellow"
         }
      },
      "5409": {
         "id": 5409,
         "description": "+2% Spellvamp.",
         "name": "Greater Quintessence of Spell Vamp",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "black"
         }
      },
      "5404": {
         "id": 5404,
         "description": "+0.84% increased health.",
         "name": "Lesser Quintessence of Percent Health",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "black"
         }
      },
      "5403": {
         "id": 5403,
         "description": "+0.25 gold / 10 sec.",
         "name": "Greater Seal of Gold",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "yellow"
         }
      },
      "5402": {
         "id": 5402,
         "description": "+0.9 Armor Penetration / +0.62 Magic Penetration",
         "name": "Greater Mark of Hybrid Penetration",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "red"
         }
      },
      "5316": {
         "id": 5316,
         "description": "+1.33 health per level (+24 at champion level 18)",
         "name": "Greater Seal of Scaling Health",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "yellow"
         }
      },
      "5121": {
         "id": 5121,
         "description": "+0.83% movement speed",
         "name": "Lesser Quintessence of Movement Speed",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "black"
         }
      },
      "5401": {
         "id": 5401,
         "description": "+0.7 Armor Penetration / +0.48 Magic Penetration",
         "name": "Mark of Hybrid Penetration",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "red"
         }
      },
      "5315": {
         "id": 5315,
         "description": "+8 health",
         "name": "Greater Seal of Health",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "yellow"
         }
      },
      "5408": {
         "id": 5408,
         "description": "+1.56% Spellvamp.",
         "name": "Quintessence of Spell Vamp",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "black"
         }
      },
      "5318": {
         "id": 5318,
         "description": "+0.16 armor per level (+3 at champion level 18)",
         "name": "Greater Seal of Scaling Armor",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "yellow"
         }
      },
      "5123": {
         "id": 5123,
         "description": "+0.74 attack damage",
         "name": "Mark of Attack Damage",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "red"
         }
      },
      "5407": {
         "id": 5407,
         "description": "+1.12% Spellvamp.",
         "name": "Lesser Quintessence of Spell Vamp",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "black"
         }
      },
      "5317": {
         "id": 5317,
         "description": "+1 armor",
         "name": "Greater Seal of Armor",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "yellow"
         }
      },
      "5406": {
         "id": 5406,
         "description": "+1.5% increased health.",
         "name": "Greater Quintessence of Percent Health",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "black"
         }
      },
      "5125": {
         "id": 5125,
         "description": "+1.32% attack speed",
         "name": "Mark of Attack Speed",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "red"
         }
      },
      "5405": {
         "id": 5405,
         "description": "+1.17% increased health.",
         "name": "Quintessence of Percent Health",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "black"
         }
      },
      "5319": {
         "id": 5319,
         "description": "+0.74 magic resist",
         "name": "Greater Seal of Magic Resist",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "yellow"
         }
      },
      "5124": {
         "id": 5124,
         "description": "+0.1 attack damage per level (+1.89 at champion level 18)",
         "name": "Mark of Scaling Attack Damage",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "red"
         }
      },
      "5311": {
         "id": 5311,
         "description": "+0.42% critical chance",
         "name": "Greater Seal of Critical Chance",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "yellow"
         }
      },
      "5108": {
         "id": 5108,
         "description": "+0.16 health regen / 5 sec. per level (+2.88 at champion level 18)",
         "name": "Lesser Quintessence of Scaling Health Regeneration",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "black"
         }
      },
      "5106": {
         "id": 5106,
         "description": "+0.21 magic resist per level (+3.78 at champion level 18)",
         "name": "Lesser Quintessence of Scaling Magic Resist",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "black"
         }
      },
      "5107": {
         "id": 5107,
         "description": "+1.5 health regen / 5 sec.",
         "name": "Lesser Quintessence of Health Regeneration",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "black"
         }
      },
      "5104": {
         "id": 5104,
         "description": "+0.21 armor per level (+3.78 at champion level 18)",
         "name": "Lesser Quintessence of Scaling Armor",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "black"
         }
      },
      "5105": {
         "id": 5105,
         "description": "+2.22 magic resist",
         "name": "Lesser Quintessence of Magic Resist",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "black"
         }
      },
      "5007": {
         "id": 5007,
         "description": "+0.52% critical chance",
         "name": "Lesser Mark of Critical Chance",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "red"
         }
      },
      "5005": {
         "id": 5005,
         "description": "+1.24% critical damage",
         "name": "Lesser Mark of Critical Damage",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "red"
         }
      },
      "5213": {
         "id": 5213,
         "description": "+1.75 attack damage",
         "name": "Quintessence of Attack Damage",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "black"
         }
      },
      "5210": {
         "id": 5210,
         "description": "+0.05 mana regen / 5 sec. per level (+0.9 at champion level 18)",
         "name": "Seal of Scaling Mana Regeneration",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "yellow"
         }
      },
      "5009": {
         "id": 5009,
         "description": "+0.72 armor penetration",
         "name": "Lesser Mark of Armor Penetration",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "red"
         }
      },
      "5206": {
         "id": 5206,
         "description": "+0.08 ability power per level (+1.44 at champion level 18)",
         "name": "Seal of Scaling Ability Power",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "yellow"
         }
      },
      "5011": {
         "id": 5011,
         "description": "+1.93 health",
         "name": "Lesser Mark of Health",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "red"
         }
      },
      "5205": {
         "id": 5205,
         "description": "+0.46 ability power",
         "name": "Seal of Ability Power",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "yellow"
         }
      },
      "5203": {
         "id": 5203,
         "description": "-0.29% cooldowns",
         "name": "Seal of Cooldown Reduction",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "yellow"
         }
      },
      "5015": {
         "id": 5015,
         "description": "+0.43 magic resist",
         "name": "Lesser Mark of Magic Resist",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "red"
         }
      },
      "5209": {
         "id": 5209,
         "description": "+0.32 mana regen / 5 sec.",
         "name": "Seal of Mana Regeneration",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "yellow"
         }
      },
      "5208": {
         "id": 5208,
         "description": "+0.91 mana per level (+16.38 at champion level 18)",
         "name": "Seal of Scaling Mana",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "yellow"
         }
      },
      "5013": {
         "id": 5013,
         "description": "+0.51 armor",
         "name": "Lesser Mark of Armor",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "red"
         }
      },
      "5207": {
         "id": 5207,
         "description": "+5.36 mana",
         "name": "Seal of Mana",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "yellow"
         }
      },
      "5012": {
         "id": 5012,
         "description": "+0.3 health per level (+5.4 at champion level 18)",
         "name": "Lesser Mark of Scaling Health",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "red"
         }
      },
      "5309": {
         "id": 5309,
         "description": "+0.78% critical damage",
         "name": "Greater Seal of Critical Damage",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "yellow"
         }
      },
      "5114": {
         "id": 5114,
         "description": "+0.24 ability power per level (+4.32 at champion level 18)",
         "name": "Lesser Quintessence of Scaling Ability Power",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "black"
         }
      },
      "5113": {
         "id": 5113,
         "description": "+2.75 ability power",
         "name": "Lesser Quintessence of Ability Power",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "black"
         }
      },
      "5307": {
         "id": 5307,
         "description": "+0.76% attack speed",
         "name": "Greater Seal of Attack Speed",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "yellow"
         }
      },
      "5112": {
         "id": 5112,
         "description": "-0.15% cooldowns per level (-2.8% at champion level 18)",
         "name": "Lesser Quintessence of Scaling Cooldown Reduction",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "black"
         }
      },
      "5306": {
         "id": 5306,
         "description": "+0.06 attack damage per level (+1.09 at champion level 18)",
         "name": "Greater Seal of Scaling Attack Damage",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "yellow"
         }
      },
      "5111": {
         "id": 5111,
         "description": "-1.4% cooldowns",
         "name": "Lesser Quintessence of Cooldown Reduction",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "black"
         }
      },
      "5305": {
         "id": 5305,
         "description": "+0.43 attack damage",
         "name": "Greater Seal of Attack Damage",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "yellow"
         }
      },
      "5303": {
         "id": 5303,
         "description": "+0.63 magic penetration",
         "name": "Greater Glyph of Magic Penetration",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "blue"
         }
      },
      "5302": {
         "id": 5302,
         "description": "+0.06 mana regen / 5 sec. per level (+1.2 at champion level 18)",
         "name": "Greater Glyph of Scaling Mana Regeneration",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "blue"
         }
      },
      "5300": {
         "id": 5300,
         "description": "+1.42 mana per level (+25.56 at champion level 18)",
         "name": "Greater Glyph of Scaling Mana",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "blue"
         }
      },
      "5301": {
         "id": 5301,
         "description": "+0.33 mana regen / 5 sec.",
         "name": "Greater Glyph of Mana Regeneration",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "blue"
         }
      },
      "5200": {
         "id": 5200,
         "description": "+0.09 health regen / 5 sec. per level (+1.62 at champion level 18)",
         "name": "Seal of Scaling Health Regeneration",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "yellow"
         }
      },
      "5002": {
         "id": 5002,
         "description": "+0.08 attack damage per level (+1.35 at champion level 18)",
         "name": "Lesser Mark of Scaling Attack Damage",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "red"
         }
      },
      "5001": {
         "id": 5001,
         "description": "+0.53 attack damage",
         "name": "Lesser Mark of Attack Damage",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "red"
         }
      },
      "5003": {
         "id": 5003,
         "description": "+0.94% attack speed",
         "name": "Lesser Mark of Attack Speed",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "red"
         }
      },
      "5101": {
         "id": 5101,
         "description": "+14.5 health",
         "name": "Lesser Quintessence of Health",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "black"
         }
      },
      "5103": {
         "id": 5103,
         "description": "+2.37 armor",
         "name": "Lesser Quintessence of Armor",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "black"
         }
      },
      "5102": {
         "id": 5102,
         "description": "+1.5 health per level (+27 at champion level 18)",
         "name": "Lesser Quintessence of Scaling Health",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "black"
         }
      },
      "5168": {
         "id": 5168,
         "description": "+0.13 magic resist per level (+2.34 at champion level 18)",
         "name": "Glyph of Scaling Magic Resist",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "blue"
         }
      },
      "5169": {
         "id": 5169,
         "description": "+0.21 health regen / 5 sec.",
         "name": "Glyph of Health Regeneration",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "blue"
         }
      },
      "5167": {
         "id": 5167,
         "description": "+1.04 magic resist",
         "name": "Glyph of Magic Resist",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "blue"
         }
      },
      "5164": {
         "id": 5164,
         "description": "+0.42 health per level (+7.56 at champion level 18)",
         "name": "Glyph of Scaling Health",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "blue"
         }
      },
      "5165": {
         "id": 5165,
         "description": "+0.55 armor",
         "name": "Glyph of Armor",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "blue"
         }
      },
      "5163": {
         "id": 5163,
         "description": "+2.08 health",
         "name": "Glyph of Health",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "blue"
         }
      },
      "5021": {
         "id": 5021,
         "description": "-0.11% cooldowns",
         "name": "Lesser Mark of Cooldown Reduction",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "red"
         }
      },
      "5025": {
         "id": 5025,
         "description": "+3.28 mana",
         "name": "Lesser Mark of Mana",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "red"
         }
      },
      "5026": {
         "id": 5026,
         "description": "+0.65 mana per level (+11.7 at champion level 18)",
         "name": "Lesser Mark of Scaling Mana",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "red"
         }
      },
      "5023": {
         "id": 5023,
         "description": "+0.33 ability power",
         "name": "Lesser Mark of Ability Power",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "red"
         }
      },
      "5024": {
         "id": 5024,
         "description": "+0.06 ability power per level (+1.08 at champion level 18)",
         "name": "Lesser Mark of Scaling Ability Power",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "red"
         }
      },
      "5016": {
         "id": 5016,
         "description": "+0.04 magic resist per level (+0.72 at champion level 18)",
         "name": "Lesser Mark of Scaling Magic Resist",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "red"
         }
      },
      "5159": {
         "id": 5159,
         "description": "+0.22% critical chance",
         "name": "Glyph of Critical Chance",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "blue"
         }
      },
      "5177": {
         "id": 5177,
         "description": "+8.75 mana",
         "name": "Glyph of Mana",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "blue"
         }
      },
      "5178": {
         "id": 5178,
         "description": "+1.1 mana per level (+19.8 at champion level 18)",
         "name": "Glyph of Scaling Mana",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "blue"
         }
      },
      "5179": {
         "id": 5179,
         "description": "+0.26 mana regen / 5 sec.",
         "name": "Glyph of Mana Regeneration",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "blue"
         }
      },
      "5173": {
         "id": 5173,
         "description": "-0.67% cooldowns",
         "name": "Glyph of Cooldown Reduction",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "blue"
         }
      },
      "5174": {
         "id": 5174,
         "description": "-0.07% cooldowns per level (-1.3% at champion level 18)",
         "name": "Glyph of Scaling Cooldown Reduction",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "blue"
         }
      },
      "5175": {
         "id": 5175,
         "description": "+0.92 ability power",
         "name": "Glyph of Ability Power",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "blue"
         }
      },
      "5176": {
         "id": 5176,
         "description": "+0.13 ability power per level (+2.34 at champion level 18)",
         "name": "Glyph of Scaling Ability Power",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "blue"
         }
      },
      "5031": {
         "id": 5031,
         "description": "+0.16 attack damage",
         "name": "Lesser Glyph of Attack Damage",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "blue"
         }
      },
      "5032": {
         "id": 5032,
         "description": "+0.02 attack damage per level (+0.36 at champion level 18)",
         "name": "Lesser Glyph of Scaling Attack Damage",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "blue"
         }
      },
      "5033": {
         "id": 5033,
         "description": "+0.35% attack speed",
         "name": "Lesser Glyph of Attack Speed",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "blue"
         }
      },
      "5035": {
         "id": 5035,
         "description": "+0.31% critical damage",
         "name": "Lesser Glyph of Critical Damage",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "blue"
         }
      },
      "5037": {
         "id": 5037,
         "description": "+0.15% critical chance",
         "name": "Lesser Glyph of Critical Chance",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "blue"
         }
      },
      "10001": {
         "id": 10001,
         "description": "+2.23% critical damage",
         "name": "Razer Mark of Precision",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "red"
         }
      },
      "5027": {
         "id": 5027,
         "description": "+0.15 mana regen / 5 sec.",
         "name": "Lesser Mark of Mana Regeneration",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "red"
         }
      },
      "10002": {
         "id": 10002,
         "description": "+1.5% movement speed",
         "name": "Razer Quintessence of Speed",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "black"
         }
      },
      "5029": {
         "id": 5029,
         "description": "+0.49 magic penetration",
         "name": "Lesser Mark of Magic Penetration",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "red"
         }
      },
      "5418": {
         "id": 5418,
         "description": "+1.79 Armor Penetration / +1.4 Magic Penetration",
         "name": "Greater Quintessence of Hybrid Penetration",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "black"
         }
      },
      "5143": {
         "id": 5143,
         "description": "-0.16% cooldowns",
         "name": "Mark of Cooldown Reduction",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "red"
         }
      },
      "5416": {
         "id": 5416,
         "description": "+0.99 Armor Penetration / +0.78 Magic Penetration",
         "name": "Lesser Quintessence of Hybrid Penetration",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "black"
         }
      },
      "5417": {
         "id": 5417,
         "description": "+1.39 Armor Penetration / +1.09 Magic Penetration",
         "name": "Quintessence of Hybrid Penetration",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "black"
         }
      },
      "5146": {
         "id": 5146,
         "description": "+0.08 ability power per level (+1.44 at champion level 18)",
         "name": "Mark of Scaling Ability Power",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "red"
         }
      },
      "5414": {
         "id": 5414,
         "description": "+0.39% Health.",
         "name": "Seal of Percent Health",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "yellow"
         }
      },
      "5147": {
         "id": 5147,
         "description": "+4.59 mana",
         "name": "Mark of Mana",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "red"
         }
      },
      "5415": {
         "id": 5415,
         "description": "+0.5% Health.",
         "name": "Greater Seal of Percent Health",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "yellow"
         }
      },
      "5412": {
         "id": 5412,
         "description": "+1.5% Life Steal.",
         "name": "Greater Quintessence of Life Steal",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "black"
         }
      },
      "5145": {
         "id": 5145,
         "description": "+0.46 ability power",
         "name": "Mark of Ability Power",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "red"
         }
      },
      "5413": {
         "id": 5413,
         "description": "+0.28% Health.",
         "name": "Lesser Seal of Percent Health",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "yellow"
         }
      },
      "5047": {
         "id": 5047,
         "description": "+0.15 health regen / 5 sec.",
         "name": "Lesser Glyph of Health Regeneration",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "blue"
         }
      },
      "5045": {
         "id": 5045,
         "description": "+0.74 magic resist",
         "name": "Lesser Glyph of Magic Resist",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "blue"
         }
      },
      "5046": {
         "id": 5046,
         "description": "+0.09 magic resist per level (+1.68 at champion level 18)",
         "name": "Lesser Glyph of Scaling Magic Resist",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "blue"
         }
      },
      "5043": {
         "id": 5043,
         "description": "+0.39 armor",
         "name": "Lesser Glyph of Armor",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "blue"
         }
      },
      "5041": {
         "id": 5041,
         "description": "+1.49 health",
         "name": "Lesser Glyph of Health",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "blue"
         }
      },
      "5042": {
         "id": 5042,
         "description": "+0.3 health per level (+5.4 at champion level 18)",
         "name": "Lesser Glyph of Scaling Health",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "blue"
         }
      },
      "5138": {
         "id": 5138,
         "description": "+0.06 magic resist per level (+1.08 at champion level 18)",
         "name": "Mark of Scaling Magic Resist",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "red"
         }
      },
      "5137": {
         "id": 5137,
         "description": "+0.6 magic resist",
         "name": "Mark of Magic Resist",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "red"
         }
      },
      "5151": {
         "id": 5151,
         "description": "+0.68 magic penetration",
         "name": "Mark of Magic Penetration",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "red"
         }
      },
      "5153": {
         "id": 5153,
         "description": "+0.22 attack damage",
         "name": "Glyph of Attack Damage",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "blue"
         }
      },
      "5051": {
         "id": 5051,
         "description": "-0.47% cooldowns",
         "name": "Lesser Glyph of Cooldown Reduction",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "blue"
         }
      },
      "5154": {
         "id": 5154,
         "description": "+0.03 attack damage per level (+0.57 at champion level 18)",
         "name": "Glyph of Scaling Attack Damage",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "blue"
         }
      },
      "5155": {
         "id": 5155,
         "description": "+0.5% attack speed",
         "name": "Glyph of Attack Speed",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "blue"
         }
      },
      "5157": {
         "id": 5157,
         "description": "+0.43% critical damage",
         "name": "Glyph of Critical Damage",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "blue"
         }
      },
      "5056": {
         "id": 5056,
         "description": "+0.79 mana per level (+14.22 at champion level 18)",
         "name": "Lesser Glyph of Scaling Mana",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "blue"
         }
      },
      "5057": {
         "id": 5057,
         "description": "+0.19 mana regen / 5 sec.",
         "name": "Lesser Glyph of Mana Regeneration",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "blue"
         }
      },
      "5058": {
         "id": 5058,
         "description": "+0.04 mana regen / 5 sec. per level (+0.67 at champion level 18)",
         "name": "Lesser Glyph of Scaling Mana Regeneration",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "blue"
         }
      },
      "5059": {
         "id": 5059,
         "description": "+0.35 magic penetration",
         "name": "Lesser Glyph of Magic Penetration",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "blue"
         }
      },
      "5052": {
         "id": 5052,
         "description": "-0.05% cooldowns per level (-0.93% at champion level 18)",
         "name": "Lesser Glyph of Scaling Cooldown Reduction",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "blue"
         }
      },
      "5053": {
         "id": 5053,
         "description": "+0.66 ability power",
         "name": "Lesser Glyph of Ability Power",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "blue"
         }
      },
      "5054": {
         "id": 5054,
         "description": "+0.1 ability power per level (+1.8 at champion level 18)",
         "name": "Lesser Glyph of Scaling Ability Power",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "blue"
         }
      },
      "5055": {
         "id": 5055,
         "description": "+6.25 mana",
         "name": "Lesser Glyph of Mana",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "blue"
         }
      },
      "5149": {
         "id": 5149,
         "description": "+0.2 mana regen / 5 sec.",
         "name": "Mark of Mana Regeneration",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "red"
         }
      },
      "5148": {
         "id": 5148,
         "description": "+0.91 mana per level (+16.38 at champion level 18)",
         "name": "Mark of Scaling Mana",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "red"
         }
      },
      "5065": {
         "id": 5065,
         "description": "+0.43% critical damage",
         "name": "Lesser Seal of Critical Damage",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "yellow"
         }
      },
      "5259": {
         "id": 5259,
         "description": "+0.77 magic resist",
         "name": "Greater Mark of Magic Resist",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "red"
         }
      },
      "5063": {
         "id": 5063,
         "description": "+0.42% attack speed",
         "name": "Lesser Seal of Attack Speed",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "yellow"
         }
      },
      "5067": {
         "id": 5067,
         "description": "+0.23% critical chance",
         "name": "Lesser Seal of Critical Chance",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "yellow"
         }
      },
      "5062": {
         "id": 5062,
         "description": "+0.03 attack damage per level (+0.61 at champion level 18)",
         "name": "Lesser Seal of Scaling Attack Damage",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "yellow"
         }
      },
      "5061": {
         "id": 5061,
         "description": "+0.24 attack damage",
         "name": "Lesser Seal of Attack Damage",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "yellow"
         }
      },
      "5260": {
         "id": 5260,
         "description": "+0.07 magic resist per level (+1.26 at champion level 18)",
         "name": "Greater Mark of Scaling Magic Resist",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "red"
         }
      },
      "5267": {
         "id": 5267,
         "description": "+0.59 ability power",
         "name": "Greater Mark of Ability Power",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "red"
         }
      },
      "5268": {
         "id": 5268,
         "description": "+0.1 ability power per level (+1.8 at champion level 18)",
         "name": "Greater Mark of Scaling Ability Power",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "red"
         }
      },
      "5265": {
         "id": 5265,
         "description": "-0.2% cooldowns",
         "name": "Greater Mark of Cooldown Reduction",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "red"
         }
      },
      "5075": {
         "id": 5075,
         "description": "+0.41 magic resist",
         "name": "Lesser Seal of Magic Resist",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "yellow"
         }
      },
      "5074": {
         "id": 5074,
         "description": "+0.09 armor per level (+1.68 at champion level 18)",
         "name": "Lesser Seal of Scaling Armor",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "yellow"
         }
      },
      "5269": {
         "id": 5269,
         "description": "+5.91 mana",
         "name": "Greater Mark of Mana",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "red"
         }
      },
      "5077": {
         "id": 5077,
         "description": "+0.31 health regen / 5 sec.",
         "name": "Lesser Seal of Health Regeneration",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "yellow"
         }
      },
      "5076": {
         "id": 5076,
         "description": "+0.05 magic resist per level (+0.9 at champion level 18)",
         "name": "Lesser Seal of Scaling Magic Resist",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "yellow"
         }
      },
      "5078": {
         "id": 5078,
         "description": "+0.06 health regen / 5 sec. per level (+1.08 at champion level 18)",
         "name": "Lesser Seal of Scaling Health Regeneration",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "yellow"
         }
      },
      "5071": {
         "id": 5071,
         "description": "+4.48 health",
         "name": "Lesser Seal of Health",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "yellow"
         }
      },
      "5073": {
         "id": 5073,
         "description": "+0.56 armor",
         "name": "Lesser Seal of Armor",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "yellow"
         }
      },
      "5072": {
         "id": 5072,
         "description": "+0.75 health per level (+13.44 at champion level 18)",
         "name": "Lesser Seal of Scaling Health",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "yellow"
         }
      },
      "5270": {
         "id": 5270,
         "description": "+1.17 mana per level (+21.06 at champion level 18)",
         "name": "Greater Mark of Scaling Mana",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "red"
         }
      },
      "5271": {
         "id": 5271,
         "description": "+0.26 mana regen / 5 sec.",
         "name": "Greater Mark of Mana Regeneration",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "red"
         }
      },
      "5273": {
         "id": 5273,
         "description": "+0.87 magic penetration",
         "name": "Greater Mark of Magic Penetration",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "red"
         }
      },
      "5275": {
         "id": 5275,
         "description": "+0.28 attack damage",
         "name": "Greater Glyph of Attack Damage",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "blue"
         }
      },
      "5276": {
         "id": 5276,
         "description": "+0.04 attack damage per level (+0.73 at champion level 18)",
         "name": "Greater Glyph of Scaling Attack Damage",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "blue"
         }
      },
      "5277": {
         "id": 5277,
         "description": "+0.64% attack speed",
         "name": "Greater Glyph of Attack Speed",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "blue"
         }
      },
      "5279": {
         "id": 5279,
         "description": "+0.56% critical damage",
         "name": "Greater Glyph of Critical Damage",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "blue"
         }
      },
      "5088": {
         "id": 5088,
         "description": "+0.036 mana regen / 5 sec. per level (+0.65 at champion level 18)",
         "name": "Lesser Seal of Scaling Mana Regeneration",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "yellow"
         }
      },
      "5183": {
         "id": 5183,
         "description": "+0.33 attack damage",
         "name": "Seal of Attack Damage",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "yellow"
         }
      },
      "5087": {
         "id": 5087,
         "description": "+0.23 mana regen / 5 sec.",
         "name": "Lesser Seal of Mana Regeneration",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "yellow"
         }
      },
      "5086": {
         "id": 5086,
         "description": "+0.65 mana per level (+11.7 at champion level 18)",
         "name": "Lesser Seal of Scaling Mana",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "yellow"
         }
      },
      "5181": {
         "id": 5181,
         "description": "+0.49 magic penetration",
         "name": "Glyph of Magic Penetration",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "blue"
         }
      },
      "5085": {
         "id": 5085,
         "description": "+3.83 mana",
         "name": "Lesser Seal of Mana",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "yellow"
         }
      },
      "5180": {
         "id": 5180,
         "description": "+0.05 mana regen / 5 sec. per level (+0.94 at champion level 18)",
         "name": "Glyph of Scaling Mana Regeneration",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "blue"
         }
      },
      "5084": {
         "id": 5084,
         "description": "+0.06 ability power per level (+1.08 at champion level 18)",
         "name": "Lesser Seal of Scaling Ability Power",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "yellow"
         }
      },
      "5187": {
         "id": 5187,
         "description": "+0.61% critical damage",
         "name": "Seal of Critical Damage",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "yellow"
         }
      },
      "5083": {
         "id": 5083,
         "description": "+0.33 ability power",
         "name": "Lesser Seal of Ability Power",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "yellow"
         }
      },
      "5185": {
         "id": 5185,
         "description": "+0.59% attack speed",
         "name": "Seal of Attack Speed",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "yellow"
         }
      },
      "5081": {
         "id": 5081,
         "description": "-0.2% cooldowns",
         "name": "Lesser Seal of Cooldown Reduction",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "yellow"
         }
      },
      "5184": {
         "id": 5184,
         "description": "+0.05 attack damage per level (+0.85 at champion level 18)",
         "name": "Seal of Scaling Attack Damage",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "yellow"
         }
      },
      "5189": {
         "id": 5189,
         "description": "+0.32% critical chance",
         "name": "Seal of Critical Chance",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "yellow"
         }
      },
      "5281": {
         "id": 5281,
         "description": "+0.28% critical chance",
         "name": "Greater Glyph of Critical Chance",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "blue"
         }
      },
      "5289": {
         "id": 5289,
         "description": "+1.34 magic resist",
         "name": "Greater Glyph of Magic Resist",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "blue"
         }
      },
      "5287": {
         "id": 5287,
         "description": "+0.7 armor",
         "name": "Greater Glyph of Armor",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "blue"
         }
      },
      "5285": {
         "id": 5285,
         "description": "+2.67 health",
         "name": "Greater Glyph of Health",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "blue"
         }
      },
      "5286": {
         "id": 5286,
         "description": "+0.54 health per level (+9.72 at champion level 18)",
         "name": "Greater Glyph of Scaling Health",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "blue"
         }
      },
      "5097": {
         "id": 5097,
         "description": "+1.03% critical chance",
         "name": "Lesser Quintessence of Critical Chance",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "black"
         }
      },
      "5099": {
         "id": 5099,
         "description": "+1.42 armor penetration",
         "name": "Lesser Quintessence of Armor Penetration",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "black"
         }
      },
      "5194": {
         "id": 5194,
         "description": "+1.04 health per level (+18.72 at champion level 18)",
         "name": "Seal of Scaling Health",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "yellow"
         }
      },
      "5193": {
         "id": 5193,
         "description": "+6.24 health",
         "name": "Seal of Health",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "yellow"
         }
      },
      "5093": {
         "id": 5093,
         "description": "+2.52% attack speed",
         "name": "Lesser Quintessence of Attack Speed",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "black"
         }
      },
      "5196": {
         "id": 5196,
         "description": "+0.13 armor per level (+2.34 at champion level 18)",
         "name": "Seal of Scaling Armor",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "yellow"
         }
      },
      "5092": {
         "id": 5092,
         "description": "+0.14 attack damage per level (+2.52 at champion level 18)",
         "name": "Lesser Quintessence of Scaling Attack Damage",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "black"
         }
      },
      "5195": {
         "id": 5195,
         "description": "+0.78 armor",
         "name": "Seal of Armor",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "yellow"
         }
      },
      "5095": {
         "id": 5095,
         "description": "+2.48% critical damage",
         "name": "Lesser Quintessence of Critical Damage",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "black"
         }
      },
      "5198": {
         "id": 5198,
         "description": "+0.08 magic resist per level (+1.44 at champion level 18)",
         "name": "Seal of Scaling Magic Resist",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "yellow"
         }
      },
      "5197": {
         "id": 5197,
         "description": "+0.58 magic resist",
         "name": "Seal of Magic Resist",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "yellow"
         }
      },
      "5199": {
         "id": 5199,
         "description": "+0.43 health regen / 5 sec.",
         "name": "Seal of Health Regeneration",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "yellow"
         }
      },
      "5091": {
         "id": 5091,
         "description": "+1.25 attack damage",
         "name": "Lesser Quintessence of Attack Damage",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "black"
         }
      },
      "5290": {
         "id": 5290,
         "description": "+0.16 magic resist per level (+3 at champion level 18)",
         "name": "Greater Glyph of Scaling Magic Resist",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "blue"
         }
      },
      "5291": {
         "id": 5291,
         "description": "+0.27 health regen / 5 sec.",
         "name": "Greater Glyph of Health Regeneration",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "blue"
         }
      },
      "8001": {
         "id": 8001,
         "description": "+2% critical damage",
         "name": "Mark of the Crippling Candy Cane",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "red"
         }
      },
      "8002": {
         "id": 8002,
         "description": "+0.62% critical chance",
         "name": "Lesser Mark of the Yuletide Tannenbaum ",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "red"
         }
      },
      "8003": {
         "id": 8003,
         "description": "-0.75% cooldowns",
         "name": "Glyph of the Special Stocking",
         "rune": {
            "isRune": True,
            "tier": "2",
            "type": "blue"
         }
      },
      "8005": {
         "id": 8005,
         "description": "+0.12 ability power per level (+2.16 at champion level 18)",
         "name": "Lesser Glyph of the Gracious Gift",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "blue"
         }
      },
      "8006": {
         "id": 8006,
         "description": "+0.72 health per level (+12.96 at champion level 18)",
         "name": "Lesser Seal of the Stout Snowman",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "yellow"
         }
      },
      "8007": {
         "id": 8007,
         "description": "+1.13% attack speed",
         "name": "Lesser Mark of Alpine Attack Speed",
         "rune": {
            "isRune": True,
            "tier": "1",
            "type": "red"
         }
      },
      "5298": {
         "id": 5298,
         "description": "+0.17 ability power per level (+3.06 at champion level 18)",
         "name": "Greater Glyph of Scaling Ability Power",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "blue"
         }
      },
      "5299": {
         "id": 5299,
         "description": "+11.25 mana",
         "name": "Greater Glyph of Mana",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "blue"
         }
      },
      "5295": {
         "id": 5295,
         "description": "-0.83% cooldowns",
         "name": "Greater Glyph of Cooldown Reduction",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "blue"
         }
      },
      "5296": {
         "id": 5296,
         "description": "-0.09% cooldowns per level (-1.67% at champion level 18)",
         "name": "Greater Glyph of Scaling Cooldown Reduction",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "blue"
         }
      },
      "5297": {
         "id": 5297,
         "description": "+1.19 ability power",
         "name": "Greater Glyph of Ability Power",
         "rune": {
            "isRune": True,
            "tier": "3",
            "type": "blue"
         }
      }
   }
