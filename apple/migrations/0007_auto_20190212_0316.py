# Generated by Django 2.1.4 on 2019-02-11 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apple', '0006_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='cerdas_cermat_point',
            field=models.IntegerField(default=0, verbose_name='Cerdas Cermat Point'),
        ),
        migrations.AlterField(
            model_name='player',
            name='cs_go_point',
            field=models.IntegerField(default=0, verbose_name='CS:GO Point'),
        ),
        migrations.AlterField(
            model_name='player',
            name='ctr_free_play_point',
            field=models.IntegerField(default=0, verbose_name='CTR (Free Play) Point'),
        ),
        migrations.AlterField(
            model_name='player',
            name='ctr_tournament_point',
            field=models.IntegerField(default=0, verbose_name='CTR (Tournament) Point'),
        ),
        migrations.AlterField(
            model_name='player',
            name='guitar_hero_point',
            field=models.IntegerField(default=0, verbose_name='Guitar Hero Point'),
        ),
        migrations.AlterField(
            model_name='player',
            name='physical_game_point',
            field=models.IntegerField(default=0, verbose_name='Physical Game Point'),
        ),
        migrations.AlterField(
            model_name='player',
            name='ranking_1_point',
            field=models.IntegerField(default=0, verbose_name='Ranking 1 Point'),
        ),
        migrations.AlterField(
            model_name='player',
            name='winning_eleven_point',
            field=models.IntegerField(default=0, verbose_name='Winning Eleven Point'),
        ),
    ]