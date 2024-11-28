from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CompVsMicro(models.Model):
    concentration = models.FloatField(blank=True, null=True)
    concentration_units = models.CharField(max_length=255, blank=True, null=True)
    experiment_type = models.CharField(max_length=255, blank=True, null=True)
    original_value = models.CharField(max_length=63, blank=True, null=True)
    units = models.CharField(max_length=255, blank=True, null=True)
    interpretation_value = models.FloatField(blank=True, null=True)
    compound = models.ForeignKey('Compounds', models.DO_NOTHING, blank=True, null=True)
    micro = models.ForeignKey('Microorganisms', models.DO_NOTHING, blank=True, null=True)
    publication = models.ForeignKey('Publications', models.DO_NOTHING, blank=True, null=True)
    test_method_id = models.IntegerField(blank=True, null=True)
    method_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comp_vs_micro'


class Compounds(models.Model):
    name = models.CharField(max_length=255)
    class_field = models.IntegerField(db_column='class', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    pubchem_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compounds'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MicroVsPlants(models.Model):
    plant = models.ForeignKey('Plants', models.DO_NOTHING, blank=True, null=True)
    micro = models.ForeignKey('Microorganisms', models.DO_NOTHING, blank=True, null=True)
    publication = models.ForeignKey('Publications', models.DO_NOTHING, blank=True, null=True)
    concentration = models.FloatField(blank=True, null=True)
    concentration_sd = models.FloatField(blank=True, null=True)
    concentration_se = models.FloatField(blank=True, null=True)
    concentration_units = models.CharField(max_length=255, blank=True, null=True)
    repetitions = models.IntegerField(blank=True, null=True)
    experiment_type = models.CharField(max_length=255, blank=True, null=True)
    original_value = models.CharField(max_length=63, blank=True, null=True)
    sd = models.FloatField(blank=True, null=True)
    se = models.FloatField(blank=True, null=True)
    units = models.CharField(max_length=255, blank=True, null=True)
    interpretation_value = models.FloatField(blank=True, null=True)
    add_info = models.TextField(blank=True, null=True)
    method_name = models.CharField(max_length=255, blank=True, null=True)
    method_type = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'micro_vs_plants'


class Microorganisms(models.Model):
    name = models.CharField(max_length=255)
    name_alt = models.CharField(max_length=255, blank=True, null=True)
    add_info = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'microorganisms'
        unique_together = (('name', 'name_alt', 'add_info'),)


class Plants(models.Model):
    common_name = models.CharField(max_length=255, blank=True, null=True)
    scientific_name = models.CharField(max_length=255, blank=True, null=True)
    part = models.CharField(max_length=63, blank=True, null=True)
    origin = models.TextField(blank=True, null=True)
    add_info = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plants'


class Publications(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    authors = models.CharField(max_length=255, blank=True, null=True)
    publication_year = models.SmallIntegerField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'publications'


class Extracts(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'extracts'


class ExtractsMicroImpact(models.Model):
    extract = models.ForeignKey(Extracts, models.DO_NOTHING, blank=True, null=True)
    micro = models.ForeignKey('MicroorganismsForImpact', models.DO_NOTHING, blank=True, null=True)
    num_of_experiments = models.IntegerField(blank=True, null=True)
    num_of_impacts = models.IntegerField(blank=True, null=True)
    avg_impact = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'extracts_micro_impact'

class MicroorganismsForImpact(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'microorganisms_for_impact'
