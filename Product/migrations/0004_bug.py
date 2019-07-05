# Generated by Django 2.0.6 on 2019-07-04 09:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Product', '0003_apitest_apiteststep'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bug_name', models.CharField(max_length=64, verbose_name='bug名称')),
                ('bug_detail', models.CharField(max_length=200, verbose_name='bug详情')),
                ('bug_status', models.CharField(choices=[('激活', '激活'), ('已解决', '已解决'), ('已关闭', '已关闭')], default='激活', max_length=200, null=True, verbose_name='bug状态')),
                ('bug_level', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], default='3', max_length=200, verbose_name='bug等级')),
                ('bug_assign', models.CharField(max_length=200, verbose_name='分配给')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('bug_creater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='bug创建人')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Product.Product')),
            ],
            options={
                'verbose_name': 'bug管理',
                'verbose_name_plural': 'bug管理',
                'db_table': 'Bug',
            },
        ),
    ]
