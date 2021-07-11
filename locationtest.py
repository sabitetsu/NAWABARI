import requests
def get_location_test():
    geo_request_url = 'https://get.geojs.io/v1/ip/geo.json'
    geo_data = requests.get(geo_request_url).json()
    #print(geo_data['latitude'])
    #print(geo_data['longitude'])
    input_data = geo_data["latitude"] + " " + geo_data["longitude"] + "\n"
    text = ""#空箱設置(エラーを回避するため)
    try:
        with open("locat_data.txt") as f_:
            text = f_.readlines()
    except:
        pass

    f = open("locat_data.txt","a",encoding = "UTF-8")
    try:
        #含んでたら飛ばす処理
        flag = False#含んでいない
        for i in text:
            if i == input_data:
                flag = True
                break
        if not(flag):#含いなかったら
            f.writelines(input_data)
    finally:
        print(text)
        f.close()

if __name__ == "__main__":
    get_location_test()