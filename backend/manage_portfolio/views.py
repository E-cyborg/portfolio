from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse , HttpRequest
from manage_portfolio.models import Profile, Project, Experience, Achievements, Skill
from django.core.paginator import Paginator


def main_page(request):
    profile_list = Profile.objects.all().order_by('id') 
    paginator = Paginator(profile_list, 9) 
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'main_page.html', {'page_obj': page_obj})

def home(request, id):  
    profile = get_object_or_404(Profile, id=id)

    overview = {
        f"{Project.objects.filter(owner=profile).count()}+": "Projects Built",
        "1st": "DUT hackathon",
    }

    projects = Project.objects.filter(owner=profile)
    skills = Skill.objects.filter(owner=profile)
    achievements = Achievements.objects.all()
    experiences = Experience.objects.filter(owner=profile)

    return render(
        request,
        "index.html",
        {
            "profile": profile,
            "overview": overview,
            "projects": projects,
            "skills": skills,
            "achievements": achievements,
            "experiences": experiences,
        },
    )

def project_view(request, id):
    profile = get_object_or_404(Profile, id=id)

    projects = Project.objects.filter(owner=profile)

    return render(
        request,
        "project.html",
        {
            "projects": projects,
            "profile": profile,
        },
    )



# from django.shortcuts import render
# from manage_portfolio.models import Profile, Project, Experience,Achievements,Skill

# def home(request,id):
#     if id:

#         profile = Profile.objects.filter(id=id).first()

#         overview = {
#             f"{Project.objects.count()}+":"Projects Built",
#             "1st":"DUT hackathon",
#         }



#         return render(request, "index.html", {
#                                             "profile":profile,
#                                             "overview":overview,
#                                             "projects":Project.objects.all(),
#                                             "skills":Skill.objects.all(),
#                                             "Achievements":Achievements.objects.all(),
#                                             "experiences": Experience.objects.all(),})
#     else:
#         return 

# def project_view(request,id):
#     profile = Profile.objects.filter(id=id).first()

#     projects = Project.objects.all()
#     return render(request, "project.html", {"projects": projects,"profile":profile,})











# item -overview 



# import requests
# from datetime import datetime

# # Replace these with your own values
# github_token = "your-personal-access-token"
# username = "your-username"
# repository = "your-repository"

# # Get commits for repository
# url = f"https://api.github.com/repos/{username}/{repository}/commits"
# headers = {"Authorization": f"Bearer {github_token}"}
# response = requests.get(url, headers=headers)

# if response.status_code == 200:
#     data = response.json()
#     commit_count_per_day = {}

#     # Loop through each commit
#     for commit in data:
#         # Extract created_at timestamp
#         created_at = datetime.fromisoformat(commit["created_at"])

#         # Convert to day of the year (1-366)
#         day_of_year = created_at.timetuple().tm_yday

#         if day_of_year not in commit_count_per_day:
#             commit_count_per_day[day_of_year] = 0

#         # Increment count
#         commit_count_per_day[day_of_year] += 1

#     # Display results on portfolio page
#     print("Commits per Day:")
#     for day, count in sorted(commit_count_per_day.items()):
#         print(f"Day {day}: {count}")
# else:
#     print("Error:", response.status_code)
