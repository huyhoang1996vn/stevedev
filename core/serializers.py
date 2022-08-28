from datetime import datetime, timedelta
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import *
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _


class TitleSerializer(ModelSerializer):
    return_day = SerializerMethodField()

    def get_return_day(self, obj):
        if obj.number_available <= 0:
            data = BookTracking.objects.filter(book__title=obj)
            return BookTrackingSerializer(data).data

    class Meta:
        model = Title
        fields = "__all__"


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class BookTrackingSerializer(ModelSerializer):
    def to_internal_value(self, data):
        if "request" in self.context:
            user = self.context["request"].user
            data["librarian"] = user.id
        return super(BookTrackingSerializer, self).to_internal_value(data)

    def validate_book(self, value):
        if BookTracking.objects.filter(book=value, is_return=False).exists():
            raise serializers.ValidationError(_("This book is borrowed."))
        return value

    def validate_student(self, value):
        user = User.objects.filter(username=value).first()
        if user and user.role.name == Role.STUDENT:
            return value
        raise serializers.ValidationError(_("Invalid student."))

    def validate_return_day(self, value):
        if value < datetime.today().date():
            raise serializers.ValidationError(_("Invalid return day."))
        if (value - datetime.today().date()).days > 30:
            raise serializers.ValidationError(_("Invalid return day."))
        return value

    class Meta:
        model = BookTracking
        fields = "__all__"
