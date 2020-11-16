from django.db import models


class PackageInfo(models.Model):
    package_id = models.AutoField(primary_key=True)
    package_name = models.CharField(max_length=255)

    def __str__(self):
        return self.package_name


class ControlUnit(models.Model):
    control_unit_id = models.IntegerField(primary_key=True)
    control_unit_name = models.CharField(max_length=255)

    def __str__(self):
        return self.control_unit_name


class SFC_SW(models.Model):
    sfc_sw_id = models.IntegerField(primary_key=True)
    sfc_sw_name = models.CharField(max_length=255)
    sfc_description = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.sfc_sw_name


class ConfigInfo(models.Model):
    responsible_team_id = models.AutoField(primary_key=True)
    payload = models.CharField(max_length=255)
    sfc_sw_id = models.ForeignKey(SFC_SW, to_field='sfc_sw_id', on_delete=models.SET_NULL, null=True)
    control_unit_id = models.ForeignKey(ControlUnit, to_field='control_unit_id', on_delete=models.CASCADE)

    def __str__(self):
        return self.responsible_team_id


class SoftwareEngineer(models.Model):
    email = models.CharField(max_length=255, default='')
    team_contact = models.CharField(max_length=255, default='')
    responsible_team = models.CharField(max_length=255)
    responsible_team_id = models.ForeignKey(ConfigInfo, to_field='responsible_team_id', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.responsible_team


class PackageVersionInfo(models.Model):
    package_version_id = models.AutoField(primary_key=True)
    package_version_name = models.CharField(max_length=255)
    package_id = models.ForeignKey(PackageInfo, to_field='package_id', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.package_version_name


class PackageSW(models.Model):
    sw_ecm = models.CharField(max_length=255)
    sw_etn = models.CharField(max_length=255)
    sw_assembly = models.CharField(max_length=255)
    package_version_id = models.ForeignKey(PackageVersionInfo, to_field='package_version_id', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.sw_ecm
