import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = 'true'

import django
django.setup()

from django.contrib.auth.models import User
from accounts.models import UserProfile
from personnel.models import Species, Career, Skill, Talent, Weapon, Armor, Gear, PersonnelFile
from missions.models import Mission, Objective
from diplomacy.models import Faction, Relation, Planet
from intel.models import Article
from newsfeed.models import NewsArticle


def create_users():
    gm, _ = User.objects.get_or_create(username='tribunis', defaults={'email': 'tribunis@keleres.gov'})
    gm.set_password('keleres123')
    gm.save()
    UserProfile.objects.get_or_create(user=gm, defaults={'role': 'gm', 'callsign': 'Tribunii Prime'})

    agent, _ = User.objects.get_or_create(username='agent1', defaults={'email': 'agent1@keleres.gov'})
    agent.set_password('agent123')
    agent.save()
    UserProfile.objects.get_or_create(user=agent, defaults={'role': 'player', 'callsign': 'Eclipse'})

    print("Users created: tribunis / keleres123 (GM), agent1 / agent123 (Player)")


def create_species():
    species_data = [
        {'name': 'Human', 'homeworld': 'Earth (Terra)', 'typical_characteristics': '+1 Intellect, +1 Presence'},
        {'name': 'Sardakk N\'orr', 'homeworld': 'Rescul', 'typical_characteristics': '+2 Brawn, -1 Intellect'},
        {'name': 'Xxcha', 'homeworld': 'Arretze', 'typical_characteristics': '+2 Willpower, +1 Intellect'},
        {'name': 'Mentak', 'homeworld': 'Moll Primus', 'typical_characteristics': '+1 Agility, +1 Cunning'},
        {'name': 'Argent Flight', 'homeworld': 'Aerilon', 'typical_characteristics': '+1 Agility, +1 Presence'},
        {'name': 'Hacan', 'homeworld': 'Retillion', 'typical_characteristics': '+1 Cunning, +1 Presence'},
        {'name': 'Jol-Nar', 'homeworld': 'Jol Nar', 'typical_characteristics': '+2 Intellect, -1 Brawn'},
        {'name': 'Letnev', 'homeworld': 'Arc Prime', 'typical_characteristics': '+1 Brawn, +1 Willpower'},
        {'name': 'Sol', 'homeworld': 'Jord', 'typical_characteristics': '+1 Brawn, +1 Presence'},
        {'name': 'L1Z1X', 'homeworld': 'L1Z1X', 'typical_characteristics': '+1 Brawn, +1 Intellect'},
        {'name': 'Mahact', 'homeworld': 'Ixth', 'typical_characteristics': '+1 Intellect, +1 Willpower'},
        {'name': 'Vuil\'raith', 'homeworld': 'The Creep', 'typical_characteristics': '+2 Brawn, -1 Presence'},
    ]
    for data in species_data:
        Species.objects.get_or_create(**data)
    print(f"Created {Species.objects.count()} species")


def create_skills():
    skills_data = [
        # General skills
        ('Astrogation', 'intellect', 'general'), ('Athletics', 'brawn', 'general'),
        ('Charm', 'presence', 'general'), ('Coercion', 'willpower', 'general'),
        ('Computers', 'intellect', 'general'), ('Cool', 'presence', 'general'),
        ('Coordination', 'agility', 'general'), ('Deception', 'cunning', 'general'),
        ('Discipline', 'willpower', 'general'), ('Leadership', 'presence', 'general'),
        ('Mechanics', 'intellect', 'general'), ('Medicine', 'intellect', 'general'),
        ('Negotiation', 'presence', 'general'), ('Perception', 'cunning', 'general'),
        ('Piloting (Space)', 'agility', 'general'), ('Piloting (Planetary)', 'agility', 'general'),
        ('Resilience', 'brawn', 'general'), ('Skulduggery', 'cunning', 'general'),
        ('Stealth', 'agility', 'general'), ('Streetwise', 'cunning', 'general'),
        ('Survival', 'cunning', 'general'), ('Vigilance', 'willpower', 'general'),
        # Combat skills
        ('Brawl', 'brawn', 'combat'), ('Gunnery', 'agility', 'combat'),
        ('Melee', 'brawn', 'combat'), ('Ranged (Heavy)', 'agility', 'combat'),
        ('Ranged (Light)', 'agility', 'combat'),
        # Knowledge skills
        ('Core Worlds', 'intellect', 'knowledge'), ('Education', 'intellect', 'knowledge'),
        ('Lore', 'intellect', 'knowledge'), ('Outer Rim', 'intellect', 'knowledge'),
        ('Technology', 'intellect', 'knowledge'), ('Warfare', 'intellect', 'knowledge'),
        ('Xenology', 'intellect', 'knowledge'),
    ]
    for name, characteristic, category in skills_data:
        Skill.objects.get_or_create(name=name, defaults={'characteristic': characteristic, 'category': category})
    print(f"Created {Skill.objects.count()} skills")


def create_factions():
    factions_data = [
        {'name': 'Sol Federation', 'homeworld': 'Jord', 'government': 'republic', 'technology': 'advanced'},
        {'name': 'Sardakk N\'orr', 'homeworld': 'Rescul', 'government': 'hive', 'technology': 'advanced'},
        {'name': 'Xxcha Kingdom', 'homeworld': 'Arretze', 'government': 'theocracy', 'technology': 'advanced'},
        {'name': 'Mentak Coalition', 'homeworld': 'Moll Primus', 'government': 'oligarchy', 'technology': 'advanced'},
        {'name': 'Argent Flight', 'homeworld': 'Aerilon', 'government': 'republic', 'technology': 'advanced'},
        {'name': 'Hacan Emporium', 'homeworld': 'Retillion', 'government': 'corporate', 'technology': 'advanced'},
        {'name': 'Jol-Nar Institutes', 'homeworld': 'Jol Nar', 'government': 'oligarchy', 'technology': 'ancient'},
        {'name': 'Barony of Letnev', 'homeworld': 'Arc Prime', 'government': 'empire', 'technology': 'advanced'},
        {'name': 'L1Z1X Mindnet', 'homeworld': 'L1Z1X', 'government': 'hive', 'technology': 'ancient'},
        {'name': 'Mahact Gene-Sorcerers', 'homeworld': 'Ixth', 'government': 'empire', 'technology': 'ancient'},
    ]
    for data in factions_data:
        Faction.objects.get_or_create(**data)
    print(f"Created {Faction.objects.count()} factions")


def create_planets():
    planets_data = [
        {'name': 'Mecatol Rex', 'sector': 'Imperial Core', 'climate': 'temperate', 'resources': 'cultural', 'population': '48 billion'},
        {'name': 'Jord', 'sector': 'Sol System', 'climate': 'temperate', 'resources': 'agricultural', 'population': '12 billion'},
        {'name': 'Arc Prime', 'sector': 'Letnev Sector', 'climate': 'barren', 'resources': 'mineral', 'population': '8 billion'},
        {'name': 'Retillion', 'sector': 'Hacan Trade Routes', 'climate': 'temperate', 'resources': 'technological', 'population': '6 billion'},
        {'name': 'Jol Nar', 'sector': 'Jol Nar Nebula', 'climate': 'ocean', 'resources': 'technological', 'population': '3 billion'},
        {'name': 'Moll Primus', 'sector': 'Mentak Drift', 'climate': 'arid', 'resources': 'mineral', 'population': '4 billion'},
        {'name': 'Arretze', 'sector': 'Xxcha Sovereign', 'climate': 'temperate', 'resources': 'agricultural', 'population': '5 billion'},
        {'name': 'Rescul', 'sector': 'N\'orr Domain', 'climate': 'barren', 'resources': 'mineral', 'population': '2 billion'},
        {'name': 'Aerilon', 'sector': 'Argent Pass', 'climate': 'temperate', 'resources': 'strategic', 'population': '1.5 billion'},
        {'name': 'Ixth', 'sector': 'Lost Space', 'climate': 'volcanic', 'resources': 'energy', 'population': 'Unknown'},
    ]
    faction_map = {f.name: f for f in Faction.objects.all()}
    for data in planets_data:
        faction_name = data.pop('faction', None)
        planet, _ = Planet.objects.get_or_create(name=data['name'], defaults=data)
        if faction_name and faction_name in faction_map:
            planet.controlling_faction = faction_map[faction_name]
            planet.save()
    print(f"Created {Planet.objects.count()} planets")


def create_relations():
    for faction in Faction.objects.all():
        Relation.objects.get_or_create(faction=faction, defaults={'level': 'neutral', 'trend': 'Stable'})
    # Special cases
    try:
        sol = Faction.objects.get(name='Sol Federation')
        r = Relation.objects.get(faction=sol)
        r.level = 'friendly'
        r.trend = 'Improving'
        r.save()
    except:
        pass
    print(f"Created {Relation.objects.count()} relations")


def create_news():
    news_data = [
        {'headline': 'Council Keleres Announces New Tribunii Appointments',
         'body': 'In a landmark session, the Galactic Council has confirmed three new Tribunii to lead the Keleres. The appointment signals renewed commitment to galactic security in the face of rising threats from beyond known space.',
         'importance': 'major', 'author_name': 'V. L. Corrin, Keleres Press', 'is_published': True},
        {'headline': 'Mahact Sightings Reported Near Ixth System',
         'body': 'Patrol vessels in the Ixth system have reported unusual energy signatures consistent with Mahact gene-sorcerer activity. The Keleres advises all non-essential traffic to avoid the sector until further notice.',
         'importance': 'breaking', 'author_name': 'Keleres Early Warning', 'is_published': True},
        {'headline': 'Trade Summit on Mecatol Rex Postponed',
         'body': 'The highly anticipated Galactic Trade Summit has been postponed indefinitely due to security concerns. Hacan mediators express disappointment but vow to reschedule.',
         'importance': 'notable', 'author_name': 'Interstellar News Network', 'is_published': True},
        {'headline': 'Keleres Relief Convoy Reaches Outer Rim Colonies',
         'body': 'A Keleres humanitarian convoy has successfully delivered supplies to three Outer Rim colonies affected by the recent pirate activity. Operations continue under the protection of Keleres escort vessels.',
         'importance': 'notable', 'author_name': 'Keleres Logistics Command', 'is_published': True},
        {'headline': 'L1Z1X Mindnet: Diplomatic Channels Remain Open',
         'body': 'Despite rising tensions, the Keleres confirms that communication channels with the L1Z1X Mindnet remain operational. Analysts debate the significance of recent fleet movements near the border.',
         'importance': 'major', 'author_name': 'Strategic Intelligence Office', 'is_published': True},
    ]
    for data in news_data:
        NewsArticle.objects.get_or_create(headline=data['headline'], defaults=data)
    print(f"Created {NewsArticle.objects.count()} news articles")


def create_intel():
    article_data = [
        {'title': 'The Mahact Gene-Sorcerers: Threat Assessment',
         'category': 'threat', 'classification': 'classified',
         'content': 'The Mahact Gene-Sorcerers, ancient masters of genetic manipulation and psychic domination, represent one of the most significant existential threats to galactic civilization. Originating from the lost planet Ixth, they were believed extinct after the Twilight Wars.\n\nRecent evidence suggests that Mahact cells remain active throughout the galaxy, conducting experiments and recruiting followers among disaffected populations. Their ability to manipulate the genetic code of living beings allows them to create monstrous hybrids and control individuals against their will.\n\nKeleres operatives are advised to exercise extreme caution when investigating Mahact activity. Direct confrontation is not recommended without significant tactical support.'},
        {'title': 'Planet Profile: Mecatol Rex',
         'category': 'planet', 'classification': 'public',
         'content': 'Mecatol Rex, the ancient capital of the fallen Empire, remains the political and cultural heart of known space. Home to the Galactic Council, this city-world houses tens of billions of sentient beings from every known species.\n\nThe Keleres headquarters, Custodia Vigilia, is located in the heart of Mecatol City. The planet serves as neutral ground for diplomatic negotiations and is protected by mutual agreement of all major factions.\n\nKey locations include the Imperial Palace (now the Council Chamber), the Spire, and the undercity levels where countless refugees and criminals operate beyond the reach of authorities.'},
        {'title': 'Species Profile: Hacan',
         'category': 'species', 'classification': 'restricted',
         'content': 'The Hacan are a feline species known throughout the galaxy as master traders and negotiators. Their homeworld, Retillion, is a hub of commerce that rivals even Mecatol Rex in economic importance.\n\nHacan culture revolves around trade and commerce. They view economic transactions as the highest form of social interaction and generally prefer negotiation to conflict. However, their neutrality in military matters should not be mistaken for weakness — the Hacan military, while rarely deployed, is well-funded and equipped.\n\nKeleres agents working with Hacan interests should note their emphasis on formal contracts and reputation. A Hacan\'s word is their bond, and they expect the same from their partners.'},
        {'title': 'Technology: War Sun Development',
         'category': 'technology', 'classification': 'top_secret',
         'content': 'INTELLIGENCE REPORT — CLASSIFIED\n\nRumors persist of a new War Sun program being covertly funded by an unknown coalition of factions. War Suns, the most powerful warships ever constructed, were instrumental in the original Empire\'s dominance.\n\nA single War Sun is capable of devastating an entire planetary system. The construction of even one would represent a dramatic shift in the galactic balance of power.\n\nThe Keleres is actively investigating these rumors. Any confirmed intelligence regarding War Sun development should be reported immediately to the Tribunii.'},
        {'title': 'Historical Record: The Twilight Wars',
         'category': 'history', 'classification': 'restricted',
         'content': 'The Twilight Wars marked the final collapse of the Lazax Empire and plunged known space into centuries of conflict. The wars were characterized by widespread use of genetic weapons, psychic warfare, and the deployment of world-ending technologies.\n\nThe Mahact Gene-Sorcerers rose to prominence during this period, exploiting the chaos to expand their influence. It was only through the united efforts of the Great Civilizations that they were eventually contained.\n\nThe legacy of the Twilight Wars continues to shape galactic politics. Many of the current factions territories were established during the wars, and old grievances still influence diplomatic relations.'},
    ]
    for data in article_data:
        Article.objects.get_or_create(title=data['title'], defaults=data)
    print(f"Created {Article.objects.count()} intel articles")


def create_sample_mission():
    mission, _ = Mission.objects.get_or_create(
        codename='OPERATION SHIELDWEAVER',
        defaults={
            'title': 'Investigate Mahact Activity on the Outer Rim',
            'classification': 'classified',
            'status': 'active',
            'threat_level': 'High',
            'location': 'Outer Rim - Sector 7-Gamma',
            'briefing': 'Intelligence suggests Mahact gene-sorcerers have established a research facility on an uncharted moon in Sector 7-Gamma. Your team is to infiltrate the facility, gather intelligence on their operations, and report back.\n\nThis is a reconnaissance mission only. Direct engagement is not authorized without explicit Tribunii approval.\n\nContact will be established via encrypted channel at the rally point in the Hylar system. Extraction is scheduled for 72 hours after insertion.',
        }
    )
    Objective.objects.get_or_create(
        mission=mission, order=1,
        defaults={'description': 'Infiltrate the Outer Rim sector and locate the Mahact research facility', 'is_primary': True}
    )
    Objective.objects.get_or_create(
        mission=mission, order=2,
        defaults={'description': 'Extract data on Mahact genetic research', 'is_primary': True}
    )
    Objective.objects.get_or_create(
        mission=mission, order=3,
        defaults={'description': 'Identify key Mahact personnel', 'is_primary': False}
    )
    Objective.objects.get_or_create(
        mission=mission, order=4,
        defaults={'description': 'Return to extraction point with intelligence', 'is_primary': True}
    )
    print(f"Created mission: {mission.codename}")


if __name__ == '__main__':
    print("Seeding database with Keleres universe data...")
    create_users()
    create_species()
    create_skills()
    create_factions()
    create_planets()
    create_relations()
    create_news()
    create_intel()
    create_sample_mission()
    print("\nDatabase seeding complete!")
    print("Login credentials:")
    print("  GM:     tribunis / keleres123")
    print("  Agent:  agent1 / agent123")
