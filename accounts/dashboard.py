from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from personnel.models import PersonnelFile
from missions.models import Mission
from logistics.models import GearRequest
from diplomacy.models import Relation
from newsfeed.models import NewsArticle
from intel.models import Article


@login_required
def dashboard(request):
    is_gm = request.user.profile.is_gm()

    active_missions = Mission.objects.filter(status='active').count()
    pending_gear = GearRequest.objects.filter(status='pending').count()

    try:
        my_file = request.user.personnel_file
        my_missions = my_file.missions.filter(status='active').count()
    except:
        my_file = None
        my_missions = 0

    recent_news = NewsArticle.objects.filter(is_published=True)[:5]
    relations = Relation.objects.select_related('faction').all().order_by('level')
    recent_articles = Article.objects.filter(published=True)[:5]

    context = {
        'is_gm': is_gm,
        'active_missions': active_missions,
        'pending_gear': pending_gear,
        'my_file': my_file,
        'my_missions': my_missions,
        'recent_news': recent_news,
        'relations': relations,
        'recent_articles': recent_articles,
    }
    return render(request, 'dashboard.html', context)
