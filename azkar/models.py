from django.db import models

class Azkar(models.Model):
    category = models.CharField(max_length=255, null=True, blank=True)
    sub_category = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    before = models.TextField(null=True, blank=True)
    after = models.TextField(null=True, blank=True)
    count = models.IntegerField(default=1, null=True, blank=True)
    reward = models.TextField(null=True, blank=True)
    when = models.CharField(max_length=255, null=True, blank=True)
    where = models.CharField(max_length=255, null=True, blank=True)
    why = models.TextField(null=True, blank=True)
    source = models.TextField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    language = models.CharField(max_length=10, default="ar", null=True, blank=True)
    icon_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.content or "Unnamed Azkar"

class DatabaseVersion(models.Model):
    version = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Version {self.version} - Updated {self.updated_at}"
