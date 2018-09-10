from django.db import models

# Create your models here.
class LegacyUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    public_id = models.CharField(max_length=25, blank=True, null=True)
    department_id = models.PositiveIntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(max_length=16, blank=True, null=True)
    email = models.CharField(max_length=150, blank=True, null=True)
    password = models.CharField(max_length=200, blank=True, null=True)
    default_language = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=5, blank=True, null=True)
    week_starts = models.CharField(max_length=3, blank=True, null=True)
    module_email_time = models.PositiveIntegerField(blank=True, null=True)
    preferred_contact = models.CharField(max_length=25, blank=True, null=True)
    reset_token = models.CharField(max_length=200, blank=True, null=True)
    reset_date = models.DateTimeField(blank=True, null=True)
    invite_date = models.DateField(blank=True, null=True)
    invite_sent = models.IntegerField()
    can_annotate = models.IntegerField(blank=True, null=True)
    is_remote_only = models.IntegerField(blank=True, null=True)
    is_archived = models.IntegerField(blank=True, null=True)
    is_dummy = models.IntegerField(blank=True, null=True)
    is_trial = models.IntegerField(blank=True, null=True)
    is_beta = models.IntegerField()
    requires_daily_reset = models.IntegerField(blank=True, null=True)
    requires_attn = models.IntegerField(blank=True, null=True)
    course_complete = models.DateField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    email_update = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
