def get_atm_address():
    import requests
    atm_url="https://www.post.gov.tw/post/internet/Templates/getOpenDataFile.jsp?vkey=85422E4D-6133-4404-851E-08EC2077A162"
    response = requests.get(atm_url)
    if response.status_code == 200:
        csv_text = response.text
        print(csv_text)
        return None
    else:
        print(f"下載失敗{response.status_code}");
        return None
