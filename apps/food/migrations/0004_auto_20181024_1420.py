# Generated by Django 2.1.1 on 2018-10-24 14:20

import datetime

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('food', '0003_auto_20180930_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorymodel',
            name='name',
            field=models.CharField(help_text='食材名称', max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='directionmodel',
            name='detail',
            field=models.CharField(help_text='该步骤的详情描述', max_length=512),
        ),
        migrations.AlterField(
            model_name='directionmodel',
            name='recipe',
            field=models.ForeignKey(help_text='所属的食材', on_delete=django.db.models.deletion.CASCADE,
                                    related_name='directions', to='food.RecipeModel'),
        ),
        migrations.AlterField(
            model_name='directionmodel',
            name='sequence',
            field=models.IntegerField(help_text='制作步骤的顺序'),
        ),
        migrations.AlterField(
            model_name='ingredientmodel',
            name='detail',
            field=models.CharField(help_text='食材详细描述', max_length=256),
        ),
        migrations.AlterField(
            model_name='recipemodel',
            name='categories',
            field=models.ManyToManyField(help_text='食材', to='food.CategoryModel'),
        ),
        migrations.AlterField(
            model_name='recipemodel',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='添加的时间'),
        ),
        migrations.AlterField(
            model_name='recipemodel',
            name='desc',
            field=models.CharField(blank=True, help_text='描述', max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='recipemodel',
            name='ingredients',
            field=models.ManyToManyField(help_text='食材的详细', to='food.IngredientModel'),
        ),
        migrations.AlterField(
            model_name='recipemodel',
            name='r_id',
            field=models.AutoField(help_text='菜谱id', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='recipemodel',
            name='title',
            field=models.CharField(help_text='菜谱名称', max_length=256, unique=True),
        ),
    ]
