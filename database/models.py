from django.db import models


# Create your models here.
class accounts(models.Model):
    uuid = models.IntegerField(primary_key=True, unique=True)
    admin = models.IntegerField(null=True, unique=False)
    account = models.CharField(max_length=255, null=False, unique=True)
    password = models.CharField(max_length=255, null=False, unique=False)
    username = models.CharField(max_length=255, null=False, unique=False)

    def __str__(self):
        message = '%s' % (self.uid)
        return message


class departments(models.Model):
    did = models.IntegerField(primary_key=True, unique=True)
    dname = models.CharField(max_length=255, null=False, unique=False)
    dmajor = models.CharField(max_length=255, null=False, unique=False)

    def __str__(self):
        message = '%s' % (self.suid)
        return message


class students(models.Model):
    suid = models.IntegerField(primary_key=True, unique=True)
    sgrade = models.IntegerField(null=False, unique=False)
    sdid = models.ForeignKey(departments, models.CASCADE)
    suuid = models.ForeignKey(accounts, models.CASCADE)

    def __str__(self):
        message = '%s' % (self.suid)
        return message


class teachers(models.Model):
    tuid = models.IntegerField(primary_key=True, unique=True)
    tdid = models.ForeignKey(departments, models.CASCADE)
    tuuid = models.ForeignKey(accounts, models.CASCADE)

    def __str__(self):
        message = '%s' % (self.tid)
        return message


class rooms(models.Model):
    rid = models.IntegerField(primary_key=True, unique=True)
    rtime = models.IntegerField(null=False, unique=False)
    rname = models.CharField(max_length=255, null=False, unique=False)
    rbuilding = models.CharField(max_length=255, null=False, unique=False)

    def __str__(self):
        message = '%s' % (self.rid)
        return message


class courses(models.Model):
    cid = models.IntegerField(primary_key=True, unique=True)
    ctuid = models.ForeignKey(teachers, models.CASCADE)
    cname = models.CharField(max_length=255, null=False, unique=False)
    crid = models.ForeignKey(rooms, models.CASCADE)  # 

    def __str__(self):
        message = '%s' % (self.wid)
        return message


class scores(models.Model):
    sid = models.IntegerField(primary_key=True, unique=True)
    scid = models.ForeignKey(courses, models.CASCADE)
    suid = models.ForeignKey(students, models.CASCADE)
    score = models.FloatField(null=True, unique=False)

    def __str__(self):
        message = '%s' % (self.wid)
        return message


class plan(models.Model):
    pid = models.IntegerField(primary_key=True, unique=True)
    pcid = models.ForeignKey(courses, models.CASCADE)
    pdid = models.ForeignKey(departments, models.CASCADE)
    psgrade = models.IntegerField(null=True, unique=False)

    def __str__(self):
        message = '%s' % (self.wid)
        return message
