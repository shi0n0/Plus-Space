from rest_framework import serializers
from app.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'password', 'confirm_password')  # パスワード確認用のフィールドを追加

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError('パスワードが一致しません')
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')  # パスワード確認用のフィールドは不要なので削除
        return super().create(validated_data)
