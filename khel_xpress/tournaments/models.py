from django.db import models

class Tournament(models.Model):
    GAME_TYPE_CHOICES = [
        ('sports', 'Sports'),
        ('esports', 'E-Sports'),
    ]

    SPORTS_CHOICES = [
        ('cricket', 'Cricket'),
        ('football', 'Football'),
        ('basketball', 'Basketball'),
        ('volleyball', 'Volleyball'),
        ('hockey', 'Hockey'),
        ('tennis', 'Tennis'),
        ('badminton', 'Badminton'),
        ('chess', 'Chess'),
    ]

    ESPORTS_CHOICES = [
        ('counter_strike', 'Counter-Strike'),
        ('dota_2', 'Dota 2'),
        ('league_of_legends', 'League of Legends'),
        ('fortnite', 'Fortnite'),
        ('pubg', 'PUBG'),
        ('valorant', 'Valorant'),
        ('fifa', 'FIFA'),
        ('call_of_duty', 'Call of Duty'),
    ]

    TOURNAMENT_LEVEL_CHOICES = [
        ('district', 'District level'),
        ('state', 'State level'),
        ('national', 'National level'),
        ('school', 'School or University level'),
    ]

    AGE_CATEGORY_CHOICES = [
        ('under_14', 'Under 14'),
        ('under_16', 'Under 16'),
        ('under_19', 'Under 19'),
        ('under_23', 'Under 23'),
    ]

    TEAM_ENTRY_CHOICES = [
        ('direct', 'Direct Entry'),
        ('trial', 'On the trial basis'),
    ]

    GENDER_CATEGORY_CHOICES = [
        ('mixed', 'Mixed'),
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    PARTICIPANT_TYPE_CHOICES = [
        ('teams', 'Teams'),
        ('individuals', 'Individuals'),
    ]

    game_type = models.CharField(max_length=20, choices=GAME_TYPE_CHOICES)
    sports_game = models.CharField(max_length=50, choices=SPORTS_CHOICES, null=True, blank=True)
    esports_game = models.CharField(max_length=50, choices=ESPORTS_CHOICES, null=True, blank=True)

    tournament_name = models.CharField(max_length=100)
    tournament_level = models.CharField(max_length=50, choices=TOURNAMENT_LEVEL_CHOICES)
    organizer_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

    venue_name = models.CharField(max_length=100)
    num_teams = models.IntegerField(null=True, blank=True)
    num_individuals = models.IntegerField(null=True, blank=True)

    state_id = models.IntegerField(default=0)
    state_name = models.CharField(max_length=100, default='Unknown')
    district_id = models.IntegerField(default=0)
    district_name = models.CharField(max_length=100, default='Unknown')
    city = models.CharField(max_length=50)

    tournament_poster = models.ImageField(upload_to='tournament_posters/', null=True, blank=True)

    stay_facility = models.CharField(max_length=50, default='match_time')
    food_facility = models.CharField(max_length=50, default='not_provided')
    travel_charge = models.CharField(max_length=50, default='not_provided')
    team_dress = models.CharField(max_length=50, default='not_provided')

    entry_fee = models.CharField(max_length=10, default='no')
    entry_fee_amount = models.IntegerField(null=True, blank=True)

    age_limit = models.CharField(max_length=10, default='no')
    age_category = models.CharField(max_length=20, choices=AGE_CATEGORY_CHOICES, null=True, blank=True)

    winner_runner_image = models.ImageField(upload_to='winner_runner_images/', null=True, blank=True)
    ground_image = models.ImageField(upload_to='ground_images/', null=True, blank=True)
    tournament_video = models.FileField(upload_to='tournament_videos/', null=True, blank=True)

    team_entry = models.CharField(max_length=20, choices=TEAM_ENTRY_CHOICES, default='direct')

    prize_pool_available = models.CharField(max_length=10, choices=[('yes', 'Yes'), ('no', 'No')], default='no')
    prize_pool = models.PositiveIntegerField(null=True, blank=True)

    participant_type = models.CharField(max_length=20, choices=PARTICIPANT_TYPE_CHOICES, null=True, blank=True)
    gender_category = models.CharField(max_length=10, choices=GENDER_CATEGORY_CHOICES, default='mixed')
    rules_document = models.FileField(upload_to='rules_documents/', null=True, blank=True)
    winner_prize = models.TextField(null=True, blank=True)
    runner_prize = models.TextField(null=True, blank=True)
    player_tournament = models.TextField(null=True, blank=True)
    player_match = models.TextField(null=True, blank=True)
    other_prizes = models.TextField(null=True, blank=True)

    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    registration_deadline = models.DateField(null=True, blank=True)

    contact_email = models.EmailField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.tournament_name
    



class Registration(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    player_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    team_name = models.CharField(max_length=100, null=True, blank=True)
    team_members = models.IntegerField(null=True, blank=True)
    additional_info = models.TextField(null=True, blank=True)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.player_name} - {self.tournament.tournament_name}"