import json

#followers json
with open('followers.json') as file:
    followers_json = json.load(file)

#following json
with open('following.json') as file:
    following_json = json.load(file)

#list that contains the users that don't follow back
following_list = []

#loop through the following list and add the users to the following_list
for following in following_json["relationships_following"]:
    following_list.append(following["string_list_data"][0]["value"])

#loop through the followers list and remove the users that follow back
for follower in followers_json["relationships_followers"]:
    if follower["string_list_data"][0]["value"] in following_list:
        following_list.remove(follower["string_list_data"][0]["value"])

#print the users that don't follow back
for user in following_list:
    print(user)