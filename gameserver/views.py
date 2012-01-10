from django.conf.urls.defaults import *
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.template.defaultfilters import slugify
from gameserver.models import Team, Player, Answer
import urllib
import urllib2
import urlparse
import string

@login_required
def home(request):
    return render_to_response('home.html', context_instance=RequestContext(request))

@login_required
def gameResults(request):
    team_list = Team.objects.all()
    firstCheckIn = Team.objects.order_by('checkIn')[0]
    lastCheckIn = Team.objects.order_by('-checkIn')[0]
    highestScoreTeam = Team.objects.order_by('totalScore')[0]
    lowestScoreTeam = Team.objects.order_by('-totalScore')[0]
    numberOfTeams = Team.objects.count()
    
    return render_to_response('game-results.html',
        {'team_list': team_list,
         'firstCheckIn':firstCheckIn,
         'lastCheckIn':lastCheckIn,
         'highestScoreTeam':highestScoreTeam,
         'lowestScoreTeam': lowestScoreTeam,
         'numberOfTeams': numberOfTeams
        },
        context_instance=RequestContext(request)
    )

@login_required
def teamResults(request, slug):
    context = {'team': get_object_or_404(Team, slug=slug)}
    team = get_object_or_404(Team, slug=slug)
    answer_list = Answer.objects.filter(team=team)
    player_list = Player.objects.filter(team=team)
    
    
    return render_to_response('team-results.html',
        {'answer_list': answer_list, 'player_list': player_list},
        context_instance=RequestContext(request, context)
    )


def teamData(request): #include team ID later?
    #possible refactoring just need really good naming convention    
    #q = request.GET
    #q.lists()
    
    teamNumber = request.GET.get('teamNumber')
    teamName = request.GET.get('teamName')
    teamID = request.GET.get('teamID')
    slug = slugify(teamName) #need to write a way to create this
    players = request.GET.get('players')
    emails = request.GET.get('emails')
    answers = request.GET.get('answers')
    scores = request.GET.get('scores')
    
    #save the team info
    def _save_team(teamName, teamID):
        newData = Team(name=teamName, slug=slug, teamID=teamID, teamNumber=teamNumber, totalScore=0)
        return newData
    
    newTeam = _save_team(teamName, teamID)
    newTeam.save()
    
    #get unique obj for current team
    team = Team.objects.get(name=teamName)    #save answers given
    answer = answers.split(',')
    score = scores.split(',')
    count = 0
    total = 0
    
    for a, s in zip(answer, score):
        count += 1
        newData = Answer(team=team, question=count, answerGiven=a, pointsAwarded=s)
        newData.save()
        try:
            sInt = int(s)
            total += sInt
        except ValueError:
            total += 0

    #save totals    
    team.totalScore = total
    team.save()
    
    #save players
    name = players.split(',')
    email = emails.split(',')
    
    
    for n, e in zip(name, email):
        newData = Player(name=n, email=e, team=team)
        newData.save()
    
    #respond to the iPads
    response = HttpResponse('{success:0}')
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
    response['Access-Control-Max-Age'] = 1000
    response['Access-Control-Allow-Headers'] = '*'
    
    return response

    