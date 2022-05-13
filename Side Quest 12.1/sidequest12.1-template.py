#
# CS1010X --- Programming Methodology
#
# Sidequest 12.1 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

import json

# Reading json file
def read_json(filename):
    """
    Reads a json file and returns a list of modules
    To find out more about json, please google ;)

    For example, cs1010x-fbdata.json contains:

    {
       "members": {
          "data": [
             {
                "name": "Aadit Kamat",
                "id": "1003982836283025"
             },
             {
                "name": "Rakshit Gogia",
                "id": "10204299775189027"
             },
             ...
          ]
       },
       "description": "This is the official FB Group for ...",
       "name": "CS1010X",
       "feed": {
          "data": [
             {
                "message": "Might be useful for the business analytics ...",
                "from": {
                   "name": "Ben Leong",
                   "id": "10152805891837166"
                },
                "name": "Machine Learning with Python - BDU"
                "id": "409054432560329_1002582839874149",
                "likes": {
                   "data": [
                      {
                         "id": "10208170707289199",
                         "name": "Lim Kian Hwee"
                      },
                      {
                         "id": "10204292869386114",
                         "name": "Siidheesh Theivasigamani"
                      },
                      ...
                   ]
                },
                ...
             },
             ...
          ]
       },
       "id": "409054432560329"
    }

    """
    datafile = open(filename, "r", encoding="utf-8")
    return json.loads(datafile.read())


# CS1010X Facebook Group Data as a dictionary object
fb_data = read_json("cs1010x-fbdata.json")

##########
# Task a #
##########


def count_comments(data):
    list_of_dict = data["feed"]["data"]
    count = 0
    for event in list_of_dict:
        if "comments" in event.keys():
            thread = event["comments"]["data"]
            for x in thread:
                count += 1
    return count


# print("Number of Comments in CS1010X: ", count_comments(fb_data))

##########
# Task b #
##########


def count_likes(data):
    # Returns the total number of likes (in feed posts and comments)
    list_of_dict = data["feed"]["data"]
    count = 0
    for event in list_of_dict:
        if "likes" in event.keys():
            thread = event["likes"]["data"]
            for x in thread:
                count += 1
        if "comments" in event.keys():
            thread = event["comments"]["data"]
            for x in thread:
                count += x["like_count"]
    return count


# print("Number of Likes in CS1010X: ", count_likes(fb_data))

##########
# Task c #
##########


def create_member_dict(data):
    # Lookup table where key is id and value is member data object
    list_of_dict = data["members"]["data"]
    store = {}
    for member in list_of_dict:
        mid = {}
        for key in member:
            if key != "id":
                mid[key] = member[key]
        store[member["id"]] = mid
    return store


member_dict = create_member_dict(fb_data)
# print(member_dict["10205702832196255"])
# print(member_dict["1047989225246155"])


# Q: Why did we choose the id of the member data object to be the key?
# A: Because id is unique

# Q: It is inappropriate to use the name as the key. What will happen if we use the name as the key of member_dict?
# A: What if someone had the same name, it will overwrite the original

##########
# Task d #
##########


def posts_freq(data):
    # Returns a dict where key is fb_id and value is number of posts in feed
    list_of_dict = data["feed"]["data"]
    store = {}
    for post in list_of_dict:
        if post["from"]["id"] in store.keys():
            store[post["from"]["id"]] += 1
        else:
            store[post["from"]["id"]] = 1
    return store


# print("Posts Frequency: ", posts_freq(fb_data))

##########
# Task e #
##########


def comments_freq(data):
    # Returns a dict where key is fb_id and value is number of comments in feed
    list_of_dict = data["feed"]["data"]
    store = {}
    for event in list_of_dict:
        if "comments" in event.keys():
            thread = event["comments"]["data"]
            for comment in thread:
                if comment["from"]["id"] in store.keys():
                    store[comment["from"]["id"]] += 1
                else:
                    store[comment["from"]["id"]] = 1
    return store


# print("Comments Frequency: ", comments_freq(fb_data))

##########
# Task f #
##########


def likes_freq(data):
    # Returns a dict where key is fb_id and value is number of likes in feed
    list_of_dict = data["feed"]["data"]
    store = {}
    for event in list_of_dict:
        if "likes" in event.keys():
            thread = event["likes"]["data"]
            for comment in thread:
                if comment["id"] in store.keys():
                    store[comment["id"]] += 1
                else:
                    store[comment["id"]] = 1
    return store


# print("Likes Frequency: ", likes_freq(fb_data))

##########
# Task g #
##########


def popularity_score(data):
    # Returns a dict where key is fb_id and value is the number of likes
    # a person's posts and comments have
    def add_likes(idx, number):
        if idx in store.keys():
            store[idx] += number
        else:
            store[idx] = number
        pass

    list_of_dict = data["feed"]["data"]
    store = {}
    for post in list_of_dict:
        poster = post["from"]["id"]
        if "likes" in post.keys():
            add_likes(poster, len(post["likes"]["data"]))
        if "comments" in post.keys():
            comments = post["comments"]["data"]
            for comment in comments:
                if comment["like_count"] > 0:
                    add_likes(comment["from"]["id"], comment["like_count"])
    return store


# print("Popularity Score: ", popularity_score(fb_data))

##########
# Task h #
##########


def member_stats(data):
    # Expand the member dict to include the keys:
    # 'posts_count', 'comments_count' and 'likes_count'
    members = create_member_dict(data)
    post_dict = posts_freq(data)
    comment_dict = comments_freq(data)
    likes_dict = likes_freq(data)
    for key in members.keys():
        if key in post_dict.keys():
            members[key]["posts_count"] = post_dict[key]
        else:
            members[key]["posts_count"] = 0
        if key in comment_dict.keys():
            members[key]["comments_count"] = comment_dict[key]
        else:
            members[key]["comments_count"] = 0
        if key in likes_dict.keys():
            members[key]["likes_count"] = likes_dict[key]
        else:
            members[key]["likes_count"] = 0

    return members


members = create_member_dict(fb_data)
stats = member_stats(fb_data)
# print(stats["10152805891837166"])

##########
# Task i #
##########


def activity_score(data):
    stats = member_stats(data)
    store = {}
    for key in stats.keys():
        store[key] = (
            3 * stats[key]["posts_count"]
            + 2 * stats[key]["comments_count"]
            + stats[key]["likes_count"]
        )
    return store


scores = activity_score(fb_data)
# print(scores["10153020766393769"]) # => 30
# print(scores["857756387629369"]) # => 8


##########
# Task j #
##########


def active_members_of_type(data, k, type_fn):
    # This is a higher order function, where type is a function and
    # can be either posts_freq, comments_freq, likes_freq, etc
    # and filters out the pairs that have frequency >= k
    member_dict = create_member_dict(data)
    store = type_fn(data)

    result = []
    for key in store.keys():
        score = store[key]
        if key not in member_dict.keys():
            continue
        if score >= k:
            result.append([member_dict[key]["name"], score])
    result.sort(key=lambda x: x[0], reverse=False)
    result.sort(key=lambda x: x[1], reverse=True)
    return result


print(active_members_of_type(fb_data, 2, posts_freq))

print(active_members_of_type(fb_data, 20, comments_freq))

print(active_members_of_type(fb_data, 40, likes_freq))

print(active_members_of_type(fb_data, 20, popularity_score))

print(active_members_of_type(fb_data, 80, activity_score))


########### DO NOT REMOVE THE TEST BELOW ###########


def gradeit():
    print("\n*** Facebook Stalker Autograding ***")
    print("==================")
    answers = json.loads(open("grading.json", "r", encoding="utf-8").read())
    total, correct = 0, 0

    def pass_or_fail(code, answer):
        nonlocal total
        total += 1
        if code == answer:
            nonlocal correct
            correct += 1
            return "Passed!"
        else:
            return "Failed."

    print(
        "Testing count_comments... ",
        pass_or_fail(count_comments(fb_data), answers["count_comments"]),
    )
    print(
        "Testing count_likes... ",
        pass_or_fail(count_likes(fb_data), answers["count_likes"]),
    )
    print(
        "Testing create_member_dict... ",
        pass_or_fail(create_member_dict(fb_data), answers["create_member_dict"]),
    )
    print(
        "Testing posts_freq... ",
        pass_or_fail(posts_freq(fb_data), answers["posts_freq"]),
    )
    print(
        "Testing comments_freq... ",
        pass_or_fail(comments_freq(fb_data), answers["comments_freq"]),
    )
    print(
        "Testing likes_freq... ",
        pass_or_fail(likes_freq(fb_data), answers["likes_freq"]),
    )
    print(
        "Testing popularity_score... ",
        pass_or_fail(popularity_score(fb_data), answers["popularity_score"]),
    )
    print(
        "Testing member_stats... ",
        pass_or_fail(member_stats(fb_data), answers["member_stats"]),
    )
    print(
        "Testing activity_score... ",
        pass_or_fail(activity_score(fb_data), answers["activity_score"]),
    )
    print(
        "Testing members with >= 1 posts... ",
        pass_or_fail(
            active_members_of_type(fb_data, 1, posts_freq), answers["active_posters"]
        ),
    )
    print(
        "Testing members with >= 4 comments... ",
        pass_or_fail(
            active_members_of_type(fb_data, 4, comments_freq),
            answers["active_commenters"],
        ),
    )
    print(
        "Testing members with >= 4 likes... ",
        pass_or_fail(
            active_members_of_type(fb_data, 4, likes_freq), answers["active_likers"]
        ),
    )
    print(
        "Testing members who have >= 3 likes... ",
        pass_or_fail(
            active_members_of_type(fb_data, 3, popularity_score), answers["popular"]
        ),
    )
    print(
        "Testing members with an activity score of >= 10... ",
        pass_or_fail(
            active_members_of_type(fb_data, 10, activity_score),
            answers["overall_active"],
        ),
    )
    print("==================")
    print("Grades: " + str(correct) + "/" + str(total) + "\n")


gradeit()
