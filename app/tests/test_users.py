from pprint import pprint
import requests

TEST_USER = {
    "first_name": "Jane",
    "last_name": "Doe",
    "hobbies": "Various",
    "active": 1
}

URL = "http://127.0.0.1:5000/users"


def test_user_creation():
    out = requests.post(URL, json=TEST_USER)
    if out.status_code == 201:
        out_json = out.json()
        pprint(out.json())
        return out_json["new_id"]
    else:
        print("Something went wrong while creating a user.")    


def test_user_deactivate():
    out = requests.delet("%s/2" % URL)
    if out.status_code == 200:
        pprint(out.text)
    else:
        print("Someting went wrong while trying to deactivate a user.")


if __name__=="__main__":
    new_id = test_user_creation()
    if new_id > 0:
        test_user_deactivate(new_id)