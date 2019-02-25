import requests


class User:
    def __init__(self, userJson, statusJson):
        self.firstName = userJson['firstName']
        self.lastName = userJson['lastName']
        self.country = userJson['country']
        self.city = userJson['city']
        self.organization = userJson['organization']
        self.handle = userJson['handle']
        self.titlePhoto = userJson['titlePhoto']
        self.avatar = userJson['avatar']
        self.rating = userJson['rating']
        self.rank = userJson['rank']
        self.maxRating = userJson['maxRating']
        self.maxRank = userJson['maxRank']
        self.submissions = [Submission(json) for json in statusJson]

    def __str__(self):
        return "Name: {} / Submitions: {}" .format(
            self.firstName, len(self.submissions))


class Submission:
    def __init__(self, json):
        self.id = json['id']
        self.contestId = json['contestId']
        self.participantType = json['author']['participantType']
        self.verdict = json['verdict']
        self.testset = json['testset']
        self.problem = Problem(json['problem'])


class Problem:
    def __init__(self, json):
        print(json)
        self.contestId = json['contestId']
        self.index = json['index']
        self.name = json['name']
        if 'points' in json:
            self.points = json['points']
        self.tags = json['tags']


def httpGet(query):
    resp = requests.get(query)
    if resp.status_code != 200:
        raise Exception('GET /tasks/ {}'.format(resp.status_code))
    return resp.json()['result']


class UserService:
    __INFO__ = 'http://codeforces.com/api/user.info?handles='
    __STATUS__ = 'http://codeforces.com/api/user.status?handle='

    def get(handle):
        userJson = httpGet(UserService.__INFO__ + handle)[0]
        statusJson = httpGet(UserService.__STATUS__ + handle)
        return User(userJson, statusJson)


def data():
    resp = requests.get('http://codeforces.com/api/user.info?handles=tsebayoth')
    if resp.status_code != 200:
        raise Exception('GET /tasks/ {}'.format(resp.status_code))
    return resp.json()


if __name__ == '__main__':
    print(UserService.get('tsebayoth'))
