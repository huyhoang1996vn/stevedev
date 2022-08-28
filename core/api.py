# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView

from .models import *
from .serializers import *


class IsLibratianAuthenticated(IsAuthenticated):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.role.name == Role.LIBRARIAN


class IsStudentAuthenticated(IsAuthenticated):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.role.name == Role.STUDENT


@api_view(["GET"])
@permission_classes((AllowAny,))
def get_book(request):
    try:
        req_query = request.query_params.get("name", None)
        if not req_query:
            return Response(
                {"code": 400, "message": _(
                    "name is required."), "fields": "name"},
                status=400,
            )
        title = Title.objects.filter(name__contains=req_query)
        serializers = TitleSerializer(title, many=True)
        return Response(serializers.data)

    except Exception as e:
        print("e", e)
        return Response(
            {"code": 500, "message": _(
                "Internal server error."), "fields": ""},
            status=500,
        )


class BookTrackingCreateAPI(CreateAPIView):
    queryset = BookTracking.objects.all()
    permission_classes = (IsLibratianAuthenticated,)
    serializer_class = BookTrackingSerializer


@api_view(["POST"])
@permission_classes((IsLibratianAuthenticated,))
def return_book(request):
    try:
        book_id = request.data.get("book", None)
        student_id = request.data.get("student", None)
        if book_id and student_id:
            try:
                track = BookTracking.objects.get(
                    book__id=book_id, student__id=student_id, is_return=False
                )
            except BookTracking.DoesNotExist as e:
                return Response(
                    {
                        "code": 400,
                        "message": _("Not found this book and this student"),
                        "fields": "",
                    },
                    status=400,
                )
            track.return_date = datetime.today().date()
            track.is_return = True
            track.save()
            return Response({"code": 200, "message": _("success")})
    except Exception as e:
        print("e", e)
        return Response(
            {"code": 500, "message": _(
                "Internal server error."), "fields": ""},
            status=500,
        )


@api_view(["GET"])
@permission_classes((IsLibratianAuthenticated| IsStudentAuthenticated,))
def get_book_tracking(request):
    try:
        if request.user.role.name == Role.LIBRARIAN:
            student = request.query_params.get("student", None)
            if not student:
                return Response(
                    {
                        "code": 400,
                        "message": _("student is required."),
                        "fields": "name",
                    },
                    status=400,
                )
        else:
            student = request.user.id

        track = BookTracking.objects.filter(student__id=student)
        serializer = BookTrackingSerializer(track, many=True)
        return Response(serializer.data)
    except Exception as e:
        print("e", e)
        return Response(
            {"code": 500, "message": _(
                "Internal server error."), "fields": ""},
            status=500,
        )


@api_view(["POST"])
@permission_classes((IsStudentAuthenticated,))
def renew_tracking(request):
    try:
        book_id = request.data.get("book", None)
        student_id = request.user.id
        if book_id and student_id:
            try:
                track = BookTracking.objects.get(
                    book__id=book_id,
                    student__id=student_id,
                    is_return=False,
                    is_renew=False,
                )
            except BookTracking.DoesNotExist as e:
                return Response(
                    {
                        "code": 400,
                        "message": _("Not valid with this book and this student"),
                        "fields": "",
                    },
                    status=400,
                )
            track.return_day = track.return_day + timedelta(days=30)
            track.is_renew = True
            track.save()
            return Response({"code": 200, "message": _("success")})
    except Exception as e:
        print("e", e)
        return Response(
            {"code": 500, "message": _(
                "Internal server error."), "fields": ""},
            status=500,
        )
