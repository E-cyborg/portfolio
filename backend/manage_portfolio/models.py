from django.db import models

class Profile(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=200)
    bio = models.TextField()
    about = models.TextField()
    about_extra = models.TextField(blank=True)
    email = models.EmailField()
    github = models.URLField()
    linkedin = models.URLField()
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True)
    connect_text = models.TextField(blank=True)
    connect_heading = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    github_url = models.URLField()
    tech = models.CharField(max_length=300)
    order = models.IntegerField(default=0)

    def tech_list(self):
        return [t.strip() for t in self.tech.split(',')]

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']

class Experience(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    date_range = models.CharField(max_length=50)
    description = models.TextField()
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title} @ {self.company}"

    class Meta:
        ordering = ['order']

class Skill(models.Model):
    RATING_CHOICES = [
        (1, '⭐'),
        (2, '⭐⭐'),
        (3, '⭐⭐⭐'),
        (4, '⭐⭐⭐⭐'),
        (5, '⭐⭐⭐⭐⭐'),
    ]
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    highlight = models.BooleanField(default=False)
    rating = models.IntegerField(choices=RATING_CHOICES, default=3)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-rating']


        
class Achievements(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.TextField()
    position = models.TextField()
    describe = models.TextField()

    class Meta:
        verbose_name_plural = "Achievements"
        ordering = ["-name"]