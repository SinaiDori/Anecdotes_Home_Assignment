from api_requests import get, post
import json


def collect_evidence(posts_url, auth_url, token, limit):
    user_details = collect_user_details(auth_url, token)
    print(json.dumps(user_details, indent=4))
    posts = collect_posts(posts_url, limit=limit)
    print(json.dumps(posts['posts'], indent=4))
    posts_with_comments = collect_posts_and_comments(posts_url, limit=limit)
    print(json.dumps(posts_with_comments, indent=4))


def collect_user_details(auth_url, token):
    return get(auth_url, headers={'Authorization': f'Bearer {token}'})


def collect_posts(posts_url, limit):
    return get(posts_url, params={'limit': limit})


def collect_posts_and_comments(posts_url, limit):
    posts = collect_posts(posts_url, limit)
    posts_list = posts["posts"]
    for post in posts_list:
        comments_url = f'{posts_url}/{post["id"]}/comments'
        response = get(comments_url)
        comments = response["comments"]
        post["comments"] = comments

    return posts_list
