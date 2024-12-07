import json

import requests

import time
import pandas as pd

sleeptime = 5  # 休眠时间



# 浏览器访问伪装
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.37',
}





def getJDProdComment(page_range,product_id):
    all_comments = pd.DataFrame(columns=['评论', '时间', '评分'])
    for i in range(int(page_range)):
        comments_url = f'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId={str(product_id)}&pageSize=10&score=0&sortType=5&isShadowSku=0&fold=1&page={str(i)}'
        response = requests.get(comments_url, headers=headers)
        print(response.text)
        if response:
            content = response.text.strip('fetchJSON_comment98();')
            comments_data = json.loads(content)

            if comments_data:
                for comment in comments_data['comments']:
                    all_comments.loc[len(all_comments)] = [comment['content'], comment['creationTime'], comment['score']]
                    print(comment['creationTime'])
                if len(comments_data['comments'])==0 :
                    all_comments.to_csv('all_comments.csv', index=False)
                    return all_comments




            time.sleep(sleeptime)

if __name__ == '__main__':
    getJDProdComment(500,100000001429)



