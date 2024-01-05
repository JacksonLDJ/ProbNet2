# Generated by Django 4.2.7 on 2024-01-05 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=256)),
                ('location', models.CharField(max_length=256)),
                ('contact_name', models.CharField(max_length=256)),
                ('contact_position', models.CharField(max_length=256)),
                ('contact_number', models.CharField(max_length=256)),
                ('initial_ip_range', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Device_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IP_Address', models.GenericIPAddressField()),
                ('created_on', models.DateTimeField(auto_now=True, help_text='Time and date this was created')),
                ('updated_on', models.DateTimeField(auto_now=True, help_text='Time and date this was updated')),
                ('MAC_Address', models.CharField(max_length=256)),
                ('Hardware_Details', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OS_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=256)),
                ('vendor', models.CharField(max_length=256)),
                ('osfamily', models.CharField(max_length=256)),
                ('osgen', models.CharField(max_length=256)),
                ('accuracy', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Port',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('protocol', models.CharField(max_length=256)),
                ('portid', models.PositiveSmallIntegerField()),
                ('reason', models.CharField(max_length=256)),
                ('reason_ttl', models.CharField(max_length=256)),
                ('device_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ports', to='core.device_data')),
            ],
        ),
        migrations.CreateModel(
            name='Netsweeper_Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=256)),
                ('mac_address', models.CharField(max_length=256)),
                ('hostname', models.CharField(max_length=256)),
                ('vendor', models.CharField(max_length=256)),
                ('state', models.CharField(max_length=256)),
                ('customer_data', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='netsweeper_customers', to='core.customer_data')),
            ],
        ),
        migrations.AddField(
            model_name='device_data',
            name='Operating_System',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.os_info'),
        ),
        migrations.AddField(
            model_name='device_data',
            name='customer_data',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customers', to='core.customer_data'),
        ),
    ]
