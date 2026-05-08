from django.db import models


class Faction(models.Model):
    GOVERNMENT_CHOICES = [
        ('republic', 'Republic'),
        ('empire', 'Empire'),
        ('theocracy', 'Theocracy'),
        ('oligarchy', 'Oligarchy'),
        ('corporate', 'Corporate State'),
        ('hive', 'Hive Mind'),
        ('anarchy', 'Anarchic'),
        ('unknown', 'Unknown'),
    ]
    TECH_CHOICES = [
        ('primitive', 'Primitive'),
        ('industrial', 'Industrial'),
        ('spacefaring', 'Spacefaring'),
        ('advanced', 'Advanced'),
        ('ancient', 'Ancient'),
        ('unknown', 'Unknown'),
    ]

    name = models.CharField(max_length=200, unique=True)
    homeworld = models.CharField(max_length=200, blank=True)
    government = models.CharField(max_length=20, choices=GOVERNMENT_CHOICES, default='unknown')
    technology = models.CharField(max_length=20, choices=TECH_CHOICES, default='unknown')
    description = models.TextField(blank=True)
    culture_notes = models.TextField(blank=True)
    known_allies = models.CharField(max_length=500, blank=True)
    known_enemies = models.CharField(max_length=500, blank=True)
    symbol = models.ImageField(upload_to='factions/', blank=True)

    def __str__(self):
        return self.name


class Relation(models.Model):
    LEVEL_CHOICES = [
        ('hostile', 'Hostile'),
        ('unfriendly', 'Unfriendly'),
        ('neutral', 'Neutral'),
        ('friendly', 'Friendly'),
        ('allied', 'Allied'),
    ]

    faction = models.OneToOneField(Faction, on_delete=models.CASCADE, related_name='relation')
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='neutral')
    trend = models.CharField(max_length=50, blank=True, help_text="e.g. Improving, Deteriorating, Stable")
    notes = models.TextField(blank=True)
    trade_active = models.BooleanField(default=False)
    military_treaty = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.faction.name}: {self.get_level_display()}"

    class Meta:
        verbose_name_plural = 'Relations'


class RelationLog(models.Model):
    relation = models.ForeignKey(Relation, on_delete=models.CASCADE, related_name='logs')
    timestamp = models.DateTimeField(auto_now_add=True)
    entry = models.TextField()
    effect = models.CharField(max_length=100, blank=True, help_text="e.g. +1 toward Friendly")

    def __str__(self):
        return f"{self.relation.faction.name} - {self.timestamp.date()}"

    class Meta:
        ordering = ['-timestamp']


class Planet(models.Model):
    CLIMATE_CHOICES = [
        ('temperate', 'Temperate'),
        ('arid', 'Arid'),
        ('frozen', 'Frozen'),
        ('jungle', 'Jungle'),
        ('ocean', 'Ocean'),
        ('volcanic', 'Volcanic'),
        ('gas_giant', 'Gas Giant'),
        ('barren', 'Barren'),
        ('artificial', 'Artificial'),
    ]
    RESOURCE_CHOICES = [
        ('mineral', 'Mineral Rich'),
        ('agricultural', 'Agricultural'),
        ('technological', 'Technological'),
        ('cultural', 'Cultural'),
        ('strategic', 'Strategic Location'),
        ('energy', 'Energy Rich'),
        ('none', 'None / Depleted'),
    ]

    name = models.CharField(max_length=200, unique=True)
    sector = models.CharField(max_length=200, blank=True)
    climate = models.CharField(max_length=20, choices=CLIMATE_CHOICES, default='temperate')
    resources = models.CharField(max_length=20, choices=RESOURCE_CHOICES, default='none')
    controlling_faction = models.ForeignKey(Faction, on_delete=models.SET_NULL, null=True, blank=True, related_name='planets')
    population = models.CharField(max_length=100, blank=True, help_text="Estimated population")
    description = models.TextField(blank=True)
    points_of_interest = models.TextField(blank=True)
    image = models.ImageField(upload_to='planets/', blank=True)
    x_coord = models.FloatField(default=0, blank=True)
    y_coord = models.FloatField(default=0, blank=True)

    def __str__(self):
        return f"{self.name} ({self.sector})" if self.sector else self.name
