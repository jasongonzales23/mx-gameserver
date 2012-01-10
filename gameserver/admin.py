from django.contrib import admin
from gameserver.models import Team, Player, Answer
    
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'teamNumber', 'teamID', 'checkIn') #, 'score'
    
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'team')

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question','answerGiven', 'pointsAwarded', 'team')

admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Answer, AnswerAdmin) 