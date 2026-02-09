from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def doctorsview(request):
    doctorsview={
  "login": "MohsinJawad5253",
  "id": 239805867,
  "node_id": "U_kgDODkslqw",
  "avatar_url": "https://avatars.githubusercontent.com/u/239805867?v=4",
  "gravatar_id": "",
  "url": "https://api.github.com/users/MohsinJawad5253",
  "html_url": "https://github.com/MohsinJawad5253",
  "followers_url": "https://api.github.com/users/MohsinJawad5253/followers",
  "following_url": "https://api.github.com/users/MohsinJawad5253/following{/other_user}",
  "gists_url": "https://api.github.com/users/MohsinJawad5253/gists{/gist_id}",
  "starred_url": "https://api.github.com/users/MohsinJawad5253/starred{/owner}{/repo}",
  "subscriptions_url": "https://api.github.com/users/MohsinJawad5253/subscriptions",
  "organizations_url": "https://api.github.com/users/MohsinJawad5253/orgs",
  "repos_url": "https://api.github.com/users/MohsinJawad5253/repos",
  "events_url": "https://api.github.com/users/MohsinJawad5253/events{/privacy}",
  "received_events_url": "https://api.github.com/users/MohsinJawad5253/received_events",
  "type": "User",
  "user_view_type": "public",
  "site_admin": "false",
  "name": 0,
  "company": 0,
  "blog": "",
  "location": 0,
  "email": 0,
  "hireable": 0,
  "bio": 0,
  "twitter_username": 0,
  "public_repos": 5,
  "public_gists": 0,
  "followers": 0,
  "following": 0,
  "created_at": "2025-10-23T13:30:14Z",
  "updated_at": "2026-01-14T09:43:10Z"
   }
    print(doctorsview)
    return JsonResponse(doctorsview)
