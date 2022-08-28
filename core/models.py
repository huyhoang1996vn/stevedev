from django.db import models
from datetime import date

from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

# Create your models here.


class DateTimeModel(models.Model):
    created_date = models.DateTimeField(
        _("Created Date"), auto_now_add=True, editable=False
    )
    modified_date = models.DateTimeField(
        _("Modified Date"), auto_now=True, editable=False
    )

    class Meta:
        abstract = True


class Role(models.Model):
    STUDENT = "STUDENT"
    LIBRARIAN = "LIBRARIAN"

    ROLE_CHOICES = (
        ("STUDENT", STUDENT),
        ("LIBRARIAN", LIBRARIAN),
    )
    name = models.CharField(choices=ROLE_CHOICES, max_length=255, default="STUDENT")

    def __str__(self):
        return "%s" % (self.name)


class User(AbstractUser):
    role = models.ForeignKey("Role", on_delete=models.PROTECT, null=True, blank=True)


class Title(DateTimeModel):
    name = models.CharField(_("Name"), max_length=255)
    number_of_copy = models.IntegerField(_("Number of copy"), default=0)
    number_available = models.IntegerField(_("Number of available book"), default=0)

    def __str__(self):
        return "%s" % (self.name)

    class Meta:
        verbose_name = _("Title")


class Book(DateTimeModel):
    serial = models.CharField(_("Serial"), max_length=255)
    title = models.ForeignKey("Title", on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return "%s Serial %s" % (self.name, self.serial)

    @property
    def name(instance):
        return instance.title.name

    class Meta:
        verbose_name = _("Book")




class BookTracking(DateTimeModel):
    borrow_day = models.DateField(_("Borrow day"), default=date.today)
    return_day = models.DateField(_("Return day"))
    is_renew = models.BooleanField(_("Is renew"), default=False)
    student = models.ForeignKey(
        "User", on_delete=models.PROTECT, related_name="student_tracking"
    )
    librarian = models.ForeignKey(
        "User", on_delete=models.PROTECT, related_name="libratian_tracking"
    )
    book = models.ForeignKey("Book", on_delete=models.PROTECT)
    is_return = models.BooleanField(_("Is return"), default=False)

    def __str__(self):
        return "%s" % (self.student)

    class Meta:
        verbose_name = _("BookTracking")
