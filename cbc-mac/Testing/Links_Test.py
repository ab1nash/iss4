import requests
# Code to check whether the basic links are working or not

BASE_URL = "http://127.0.0.1:5000"  # LOCAL HOST


def checkServer():
    timeout = 5
    try:
        _ = requests.get(BASE_URL, timeout=timeout)
        print("Server responding as expected!!")
        return True
    except requests.ConnectionError:
        print("Server is not Connected")
        return False


links = [
    "/Introduction",
    "/Theory",
    "/Objective",
    "/Experiment",
    "/Quizzes",
    "/Procedure",
    "/Manual",
    "/Further"]

for current in links:
    response = requests.get(BASE_URL + current)
    assert response.status_code == 200, current
    code = str(response.status_code)
    print(current[1:-5] + " : ")
    print("status code=" + code + "; Link responding as expected!!\n")


print("All links are functional")
