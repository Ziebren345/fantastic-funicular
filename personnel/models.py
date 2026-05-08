from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Species(models.Model):
    name = models.CharField(max_length=100, unique=True)
    homeworld = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    typical_characteristics = models.CharField(max_length=200, blank=True, help_text="e.g. +1 Intellect, +1 Willpower")
    special_abilities = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Species'


class Career(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Talent(models.Model):
    name = models.CharField(max_length=100)
    rank = models.PositiveSmallIntegerField(default=1)
    description = models.TextField(blank=True)
    activation = models.CharField(max_length=100, blank=True, help_text="Passive, Active (Incident), etc.")

    def __str__(self):
        return f"{self.name} (R{self.rank})"

    class Meta:
        ordering = ['name', 'rank']


class Weapon(models.Model):
    name = models.CharField(max_length=200)
    skill = models.CharField(max_length=100, blank=True, help_text="e.g. Ranged (Light), Gunnery")
    damage = models.PositiveSmallIntegerField(default=0)
    crit = models.PositiveSmallIntegerField(default=3, help_text="Critical rating")
    range = models.CharField(max_length=50, blank=True, help_text="Engaged, Short, Medium, Long, Extreme")
    special = models.CharField(max_length=200, blank=True, help_text="Special qualities")
    encumbrance = models.PositiveSmallIntegerField(default=1)
    price = models.CharField(max_length=100, blank=True)
    rarity = models.PositiveSmallIntegerField(default=0)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Armor(models.Model):
    name = models.CharField(max_length=200)
    defense = models.PositiveSmallIntegerField(default=0)
    soak = models.PositiveSmallIntegerField(default=0)
    encumbrance = models.PositiveSmallIntegerField(default=1)
    price = models.CharField(max_length=100, blank=True)
    rarity = models.PositiveSmallIntegerField(default=0)
    special = models.CharField(max_length=200, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Armor'


class Gear(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    encumbrance = models.PositiveSmallIntegerField(default=1)
    price = models.CharField(max_length=100, blank=True)
    rarity = models.PositiveSmallIntegerField(default=0)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name


class PersonnelFile(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('injured', 'Injured / Recovering'),
        ('mia', 'Missing in Action'),
        ('kia', 'Killed in Action'),
        ('retired', 'Retired'),
        ('suspended', 'Suspended'),
    ]

    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='personnel_file')
    name = models.CharField(max_length=200, help_text="Character name")
    callsign = models.CharField(max_length=100, blank=True)
    species = models.ForeignKey(Species, on_delete=models.SET_NULL, null=True, blank=True)
    career = models.ForeignKey(Career, on_delete=models.SET_NULL, null=True, blank=True)
    specializations = models.CharField(max_length=300, blank=True, help_text="Career specializations")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')

    portrait = models.ImageField(upload_to='personnel/', blank=True)
    age = models.PositiveSmallIntegerField(default=0, blank=True)
    height = models.CharField(max_length=50, blank=True)
    weight = models.CharField(max_length=50, blank=True)
    appearance = models.TextField(blank=True)
    background = models.TextField(blank=True)

    brawn = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    agility = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    intellect = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    cunning = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    willpower = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    presence = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])

    wound_threshold = models.PositiveSmallIntegerField(default=10)
    current_wounds = models.PositiveSmallIntegerField(default=0)
    strain_threshold = models.PositiveSmallIntegerField(default=10)
    current_strain = models.PositiveSmallIntegerField(default=0)
    soak = models.PositiveSmallIntegerField(default=0, help_text="Brawn + armor soak")
    defense_ranged = models.PositiveSmallIntegerField(default=0)
    defense_melee = models.PositiveSmallIntegerField(default=0)

    experience_available = models.PositiveIntegerField(default=0)
    experience_total = models.PositiveIntegerField(default=0)

    motivation_type = models.CharField(max_length=100, blank=True, help_text="e.g. Cause, Relationship, Personal")
    motivation_description = models.TextField(blank=True)
    duty = models.CharField(max_length=200, blank=True, help_text="What drives this agent for the Keleres")

    weapons = models.ManyToManyField(Weapon, blank=True)
    armor = models.ManyToManyField(Armor, blank=True)
    gear = models.ManyToManyField(Gear, blank=True)
    talents = models.ManyToManyField(Talent, blank=True)
    credits = models.IntegerField(default=0, help_text="Universal credits")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} \"{self.callsign}\" - {self.species or 'Unknown'}"

    @property
    def soak_value(self):
        brawn_soak = self.brawn
        armor_soak = sum(a.soak for a in self.armor.all()) if self.pk else 0
        return brawn_soak + armor_soak

    class Meta:
        verbose_name = 'Personnel File'
        verbose_name_plural = 'Personnel Files'


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('general', 'General'),
        ('combat', 'Combat'),
        ('knowledge', 'Knowledge'),
    ]
    CHARACTERISTIC_CHOICES = [
        ('brawn', 'Brawn'),
        ('agility', 'Agility'),
        ('intellect', 'Intellect'),
        ('cunning', 'Cunning'),
        ('willpower', 'Willpower'),
        ('presence', 'Presence'),
    ]

    name = models.CharField(max_length=100, unique=True)
    characteristic = models.CharField(max_length=20, choices=CHARACTERISTIC_CHOICES)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='general')
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.get_characteristic_display()})"


class PersonnelSkill(models.Model):
    personnel = models.ForeignKey(PersonnelFile, on_delete=models.CASCADE, related_name='skills')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    rank = models.PositiveSmallIntegerField(default=0)
    is_career = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.personnel.name} - {self.skill.name} ({self.rank})"

    class Meta:
        unique_together = ['personnel', 'skill']
        verbose_name = 'Personnel Skill'
        verbose_name_plural = 'Personnel Skills'
