from django.db import models


class Controller(models.Model):
    controller_id = models.AutoField(primary_key=True)
    controller_name = models.CharField(max_length=255)

    def __str__(self):
        return self.controller_name


class SourceAddr(models.Model):
    tla_id = models.AutoField(primary_key=True)
    TLA_source_addr = models.CharField(max_length=255)
    IsMaster = models.CharField(max_length=255)
    EnggDef = models.CharField(max_length=255)
    controller_id = models.ForeignKey(Controller, to_field='controller_id', on_delete=models.CASCADE)

    def __str__(self):
        return self.TLA_source_addr


class MultipleVersions(models.Model):
    multiple_version_id = models.AutoField(primary_key=True)
    multiple_version_name = models.CharField(max_length=255)

    def __str__(self):
        return self.multiple_version_name


class Hardware(models.Model):
    hardware_id = models.AutoField(primary_key=True)
    hardware_name = models.CharField(max_length=255)
    hardware_change = models.CharField(max_length=10, null=True)
    SCP_changed = models.CharField(max_length=10, null=True)
    Diagnose_address_changed = models.CharField(max_length=10, null=True)
    controller_id = models.ForeignKey(Controller, to_field='controller_id', on_delete=models.CASCADE)
    multiple_version_id = models.ForeignKey(MultipleVersions, to_field='multiple_version_id', on_delete=models.CASCADE)

    def __str__(self):
        return self.hardware_name


class Software(models.Model):
    id = models.AutoField(primary_key=True)
    software_id = models.IntegerField()
    software_part = models.CharField(max_length=255)
    software_filename = models.CharField(max_length=255)
    software_version = models.CharField(max_length=255)
    remarks = models.CharField(max_length=255)
    controller_id = models.ForeignKey(Controller, to_field='controller_id', on_delete=models.CASCADE)
    multiple_version_id = models.ForeignKey(MultipleVersions, to_field='multiple_version_id', on_delete=models.CASCADE)
    hardware_id = models.ForeignKey(Hardware, to_field='hardware_id', on_delete=models.SET_NULL, null=True)
    tla_id = models.ForeignKey(SourceAddr, to_field="tla_id", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.software_part


class Payload(models.Model):
    pid = models.AutoField(primary_key=True)
    payload_id = models.CharField(max_length=30)
    payload_changed = models.CharField(max_length=10, null=True)
    source_addr_change = models.CharField(max_length=10, null=True)
    controller_id = models.ForeignKey(Controller, to_field='controller_id', on_delete=models.CASCADE)
    multiple_version_id = models.ForeignKey(MultipleVersions, to_field='multiple_version_id', on_delete=models.CASCADE)
    hardware_id = models.ForeignKey(Hardware, to_field='hardware_id', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.payload_changed
