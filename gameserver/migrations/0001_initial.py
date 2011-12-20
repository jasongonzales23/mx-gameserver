# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Team'
        db.create_table('gameserver_team', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('teamID', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('checkIn', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 12, 4, 17, 36, 48, 308850))),
        ))
        db.send_create_signal('gameserver', ['Team'])

        # Adding model 'Player'
        db.create_table('gameserver_player', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=255)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gameserver.Team'])),
        ))
        db.send_create_signal('gameserver', ['Player'])

        # Adding model 'Answer'
        db.create_table('gameserver_answer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gameserver.Team'])),
            ('question', self.gf('django.db.models.fields.IntegerField')(max_length=5)),
            ('answerGiven', self.gf('django.db.models.fields.TextField')(max_length=255)),
            ('pointsAwarded', self.gf('django.db.models.fields.IntegerField')(max_length=5)),
        ))
        db.send_create_signal('gameserver', ['Answer'])


    def backwards(self, orm):
        
        # Deleting model 'Team'
        db.delete_table('gameserver_team')

        # Deleting model 'Player'
        db.delete_table('gameserver_player')

        # Deleting model 'Answer'
        db.delete_table('gameserver_answer')


    models = {
        'gameserver.answer': {
            'Meta': {'object_name': 'Answer'},
            'answerGiven': ('django.db.models.fields.TextField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pointsAwarded': ('django.db.models.fields.IntegerField', [], {'max_length': '5'}),
            'question': ('django.db.models.fields.IntegerField', [], {'max_length': '5'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gameserver.Team']"})
        },
        'gameserver.player': {
            'Meta': {'object_name': 'Player'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gameserver.Team']"})
        },
        'gameserver.team': {
            'Meta': {'object_name': 'Team'},
            'checkIn': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 12, 4, 17, 36, 48, 308850)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'teamID': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['gameserver']
