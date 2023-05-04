# Generated by Django 3.2.16 on 2023-04-18 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccountType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('maximum_withdrawal_amount', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=120, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserBankAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_no', models.PositiveIntegerField(unique=True)),
                ('gender', models.CharField(choices=[('0', 'Male'), ('1', 'Female')], max_length=1)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('account_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.bankaccounttype')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bank.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(max_length=512)),
                ('city', models.CharField(max_length=256)),
                ('postal_code', models.PositiveIntegerField()),
                ('country', models.CharField(max_length=256)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bank.user')),
            ],
        ),
    ]
