# Generated by Django 4.1.7 on 2023-03-10 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pol", "0004_brand_sub_category"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="p1",
            new_name="p1_en",
        ),
        migrations.RenameField(
            model_name="product",
            old_name="p2",
            new_name="p1_ru",
        ),
        migrations.RenameField(
            model_name="product",
            old_name="p3",
            new_name="p1_uz",
        ),
        migrations.RenameField(
            model_name="product",
            old_name="p4",
            new_name="p2_en",
        ),
        migrations.RenameField(
            model_name="product",
            old_name="p5",
            new_name="p2_ru",
        ),
        migrations.AddField(
            model_name="product",
            name="p2_uz",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="p3_en",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="p3_ru",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="p3_uz",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="p4_en",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="p4_ru",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="p4_uz",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="p5_en",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="p5_ru",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="p5_uz",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
