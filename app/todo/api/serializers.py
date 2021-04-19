from rest_framework import serializers
from app.todo.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        field = ["id", "task", "completed", "timestamp", "updated", "user"]
