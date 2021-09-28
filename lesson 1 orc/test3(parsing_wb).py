import requests

def get_data():
   # headers = {
  #      "accept": "*/*"
  #      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
  #  }

    for i in range(1, 3):
        url = f"https://images.wbstatic.net/c516x688/new/12750000/12751383-{i}.jpg"
        req = requests.get(url=url)
        response = req.content

        with open(f"media/{i}.jpg", "wb") as file:
            file.write(response)
            print(f"Downloaded {i}")


def main():
    get_data()


if __name__ == '__main__':
    main()