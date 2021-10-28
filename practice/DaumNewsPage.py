# Daum News에서 페이지를 돌면서 뉴스 기사의 제목과 본문을 수집

import requests
from bs4 import BeautifulSoup
page = 1
i = 0
for page_number in range(1,4):
    url = 'https://news.daum.net/breakingnews/digital?page={}'.format(page_number)
    # 실제 URL 주소
    # ? 기준 뒤에 오는 값: 주소 X. 웹서버 넘겨주는 입력값
    result = requests.get(url)  # 소스 코드 긁어온 것


    doc = BeautifulSoup(result.text,'html.parser')  # 소스코드를 BeautifulSoup에 준 것. html.parser로 읽음
    url_list = doc.select('ul.list_news2  a.link_txt')
    # print(url_list)
    # print('=====================================================')

    for url in url_list:
        i += 1 #New Count
        print('## NEWS -> {}번 #########################'.format(i))
        new_url = url['href']
        print('# URL: {}'.format(new_url))
        result = requests.get(new_url)

        doc = BeautifulSoup(result.text, 'html.parser')
        title = doc.select('h3.tit_view')[0].get_text()  # get_text(): <tag>text</tag>에서 tag를 빼고, text만 빼옴.
        contents = doc.select('section p')
        contents.pop()  # 기자 정보 삭제

        content = ''  # 본문 총합
        for info in contents:
            content += info.get_text()

        print('##################################################################')
        print('# 뉴스 제목: {}'.format(title))
        print('##################################################################################')
        print('# 뉴스 본문: {}'.format(content))

