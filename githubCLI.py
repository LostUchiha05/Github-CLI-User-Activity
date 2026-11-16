import requests

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('username',type=str,help="Enter the Username")
parser.add_argument('-c','--commands',choices=['events','repo'],help="Can Choice which to be shown")
parser.add_argument('-l','--limit',type=int,help="Limit fo how much to be seen")
args = parser.parse_args()






def get_user_repos(username,limit):
    git_url=f'https://api.github.com/users/{username}/repos'
    response = requests.get(git_url)
    print("----------------------")

    if response.status_code == 200:
        git_response = response.json()

        repos_to_show = git_response[:limit] if limit else git_response
        for repo in repos_to_show:
            pretty_name = repo['name'].replace('-', ' ').replace('_', ' ').title()
            print(pretty_name,"-",repo["description"],end="\n")
            print("--------------")
    elif response.status_code == 404:
        print(f"Error: The GitHub username '{username}' does not exist.")
    else:
        print(f"Error: Failed to fetch data (Status Code: {response.status_code}")

def get_user_events(username,limit):
    git_url = f"https://api.github.com/users/{username}/events"
    response = requests.get(git_url)
    print("----------------------")

    if response.status_code == 200:
        git_response = response.json()

        events_to_show = git_response[:limit] if limit else git_response
        for event in events_to_show:
            print(f"Event Type:{event['type']} on repo {event['repo']['name']}")
            print("--------------")
    elif response.status_code == 404:
        print(f"Error: The GitHub username '{username}' does not exist.")
    else:
        print(f"Error Accquired Status Code:{response.status_code}")



if (args.commands == 'repo'):
    get_user_repos(args.username,args.limit)
elif(args.commands == 'events'):
    get_user_events(args.username,args.limit)
