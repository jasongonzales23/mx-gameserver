# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Team.teamNumber'
        db.add_column('gameserver_team', 'teamNumber', self.gf('django.db.models.fields.CharField')(default=0, max_length=30), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Team.teamNumber'
        db.delete_column('gameserver_team', 'teamNumber')


    models = {
        'gameserver.answer': {
            'Meta': {'object_name': 'Answer'},
            'answerGiven': ('django.db.models.fields.TextField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pointsAwarded': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'question': ('django.db.models.fields.IntegerField', [], {'max_length': '5'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gameserver.Team']"})
        },
        'gameserver.player': {
            'Meta': {'object_name': 'Player'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gameserver.Team']"})
        },
        'gameserver.team': {
            'Meta': {'object_name': 'Team'},
            'checkIn': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 1, 4, 20, 6, 26, 916363)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'teamID': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'teamNumber': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['gameserver']
