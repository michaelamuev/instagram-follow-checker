#FUNCTION

import json
import os

def extract_usernames(json_data):
    """Safely extract usernames from standard Instagram JSON structure."""
    if isinstance(json_data, dict):
        # Try to find the first key that maps to a list of profile entries
        for key in json_data:
            if isinstance(json_data[key], list):
                entries = json_data[key]
                break
        else:
            raise ValueError("No list found in JSON dictionary.")
    elif isinstance(json_data, list):
        entries = json_data
    else:
        raise ValueError("Unexpected JSON format")

    # Extract usernames
    usernames = set()
    for entry in entries:
        try:
            usernames.add(entry['string_list_data'][0]['value'])
        except (KeyError, IndexError, TypeError):
            continue  # Skip malformed entries

    return usernames

def analyze_instagram_followers(base_path='./connections/followers_and_following'):  #change directory/filename if needed
    followers_path = os.path.join(base_path, 'followers_1.json')
    following_path = os.path.join(base_path, 'following.json')

    # Load and parse followers
    with open(followers_path, 'r', encoding='utf-8') as f:
        followers_data = json.load(f)
        followers = extract_usernames(followers_data)

    # Load and parse following
    with open(following_path, 'r', encoding='utf-8') as f:
        following_data = json.load(f)
        following = extract_usernames(following_data)

    not_following_back = sorted(following - followers)

    return sorted(following), sorted(followers), not_following_back


# CALL SECTION- after the script above is run
if __name__ == "__main__":
    following, followers, not_following_back = analyze_instagram_followers()

    print("\nAccounts you follow that don’t follow you back:")
    print("-" * 45)

    if not_following_back:
        for user in not_following_back:
            print(user)

