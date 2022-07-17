# coding: utf8
import requests

def computeLenOfString(str):
    length = 0
    while(str[length] != '\0'):
        length = length + 1
    print(length)

def download_img(img_url, api_token,filename):
    print(img_url)
    header = {"Authorization": "Bearer " + api_token}  # 设置http header，视情况加需要的条目，这里的token是用来鉴权的一种方式
    r = requests.get(img_url, headers=header, stream=True)
    # print(r.status_code)  # 返回状态码
    if r.status_code == 200:
        open('D:\\Program Files (x86)\\PyCharm Community Edition 2020.1.1\\PaQuChuYiJiaoCai\\pics\\'+filename,'wb').write(r.content)  # 将内容写入图片
        # print("done")
    del r

if __name__ == '__main__':
    size = 207
    for i in range(1, size+1):
        str_indexi = str(i);
        if len(str_indexi) == 1:
            str_indexi = '00' + str_indexi
        elif len(str_indexi) == 2:
            str_indexi = '0' + str_indexi
        elif len(str_indexi) == 3:
            str_indexi = str_indexi
        img_url = 'http://www.shuxue9.com/beishida/cz7s/ebook/' + str_indexi +'.jpg'
        api_token = "fklasjfljasdlkfjlasjflasjfljhasdljflsdjflkjsadljfljsda"
        download_img(img_url, api_token,str_indexi +'.jpg')
    print('Finished!');