from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=50, unique=True)
    short_description = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.name


class Difficulty(models.TextChoices):
    EASY = "EASY", "Easy"
    MEDIUM = "MEDIUM", "Medium"
    HARD = "HARD", "Hard"


class Resource(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(max_length=100, unique=True)
    description = models.TextField(max_length=200, blank=True, null=True)
    difficulty = models.CharField(max_length=10, choices=Difficulty.choices)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Problem(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(max_length=100, unique=True)
    description = models.TextField(max_length=200, blank=True, null=True)
    difficulty = models.CharField(max_length=10, choices=Difficulty.choices)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CodeLanguage(models.TextChoices):
    PYTHON = "python", "Python"
    CPP = "cpp", "C++"


class CodeSnippet(models.Model):
    name = models.CharField(max_length=100)
    language = models.CharField(
        max_length=10,
        choices=CodeLanguage.choices,
        default=CodeLanguage.CPP
    )
    code = models.TextField()

    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.get_language_display()})"
