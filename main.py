import json
import requests

def main():
    response = requests.get("https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow")
    for question in response.json()['items']:
        if question['answer_count'] == 0:
            print(question['title'])
            print(question['link'])
        else:
            print("Question has been answered")
        print()


if __name__ == '__main__':
    main()
