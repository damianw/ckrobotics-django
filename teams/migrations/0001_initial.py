# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Robot'
        db.create_table(u'teams_robot', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'teams', ['Robot'])

        # Adding model 'Member'
        db.create_table(u'teams_member', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('join_date', self.gf('django.db.models.fields.DateField')()),
            ('current', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('grad_year', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'teams', ['Member'])

        # Adding model 'Team'
        db.create_table(u'teams_team', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('founded_date', self.gf('django.db.models.fields.DateField')()),
            ('primarygroup', self.gf('django.db.models.fields.related.ForeignKey')(related_name='primaryteams', to=orm['auth.Group'])),
        ))
        db.send_create_signal(u'teams', ['Team'])

        # Adding M2M table for field members on 'Team'
        db.create_table(u'teams_team_members', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('team', models.ForeignKey(orm[u'teams.team'], null=False)),
            ('member', models.ForeignKey(orm[u'teams.member'], null=False))
        ))
        db.create_unique(u'teams_team_members', ['team_id', 'member_id'])

        # Adding M2M table for field groups on 'Team'
        db.create_table(u'teams_team_groups', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('team', models.ForeignKey(orm[u'teams.team'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(u'teams_team_groups', ['team_id', 'group_id'])

        # Adding M2M table for field robots on 'Team'
        db.create_table(u'teams_team_robots', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('team', models.ForeignKey(orm[u'teams.team'], null=False)),
            ('robot', models.ForeignKey(orm[u'teams.robot'], null=False))
        ))
        db.create_unique(u'teams_team_robots', ['team_id', 'robot_id'])


    def backwards(self, orm):
        # Deleting model 'Robot'
        db.delete_table(u'teams_robot')

        # Deleting model 'Member'
        db.delete_table(u'teams_member')

        # Deleting model 'Team'
        db.delete_table(u'teams_team')

        # Removing M2M table for field members on 'Team'
        db.delete_table('teams_team_members')

        # Removing M2M table for field groups on 'Team'
        db.delete_table('teams_team_groups')

        # Removing M2M table for field robots on 'Team'
        db.delete_table('teams_team_robots')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'league': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'teams.member': {
            'Meta': {'object_name': 'Member'},
            'current': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'grad_year': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'join_date': ('django.db.models.fields.DateField', [], {}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'teams.robot': {
            'Meta': {'object_name': 'Robot'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'teams.team': {
            'Meta': {'object_name': 'Team'},
            'founded_date': ('django.db.models.fields.DateField', [], {}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'teams'", 'symmetrical': 'False', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'teams'", 'blank': 'True', 'to': u"orm['teams.Member']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'primarygroup': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'primaryteams'", 'to': u"orm['auth.Group']"}),
            'robots': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['teams.Robot']", 'symmetrical': 'False', 'blank': 'True'})
        }
    }

    complete_apps = ['teams']