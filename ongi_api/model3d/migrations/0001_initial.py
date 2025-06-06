# Generated by Django 5.1.6 on 2025-03-06 13:28

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artifacts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Model3D',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('model_url', models.TextField()),
                ('thumbnail_url', models.TextField(blank=True, null=True)),
                ('file_format', models.CharField(choices=[('obj', 'OBJ'), ('glb', 'GLB'), ('gltf', 'GLTF'), ('fbx', 'FBX'), ('stl', 'STL'), ('other', '기타')], max_length=10)),
                ('poly_count', models.IntegerField(blank=True, null=True)),
                ('file_size', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('pending', '대기 중'), ('processing', '처리 중'), ('completed', '완료'), ('failed', '실패')], default='pending', max_length=20)),
                ('processing_time', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('artifact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='models', to='artifacts.artifact')),
            ],
            options={
                'verbose_name': '3D Model',
                'verbose_name_plural': '3D Models',
                'db_table': 'model3d',
            },
        ),
        migrations.CreateModel(
            name='ModelTexture',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('texture_url', models.TextField()),
                ('texture_type', models.CharField(choices=[('diffuse', 'Diffuse'), ('normal', 'Normal'), ('specular', 'Specular'), ('roughness', 'Roughness'), ('metallic', 'Metallic'), ('ao', 'Ambient Occlusion'), ('emissive', 'Emissive'), ('other', '기타')], default='diffuse', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='textures', to='model3d.model3d')),
            ],
            options={
                'db_table': 'model_textures',
            },
        ),
    ]
