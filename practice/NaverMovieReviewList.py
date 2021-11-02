# NaverMovieReviewList.py
# -> Naver 영화 (1개 선택) 리뷰 정보 수집(review, score, writer, date)

# import pprint
import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=206657&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page=1'
result = requests.get(url)
# print(result.text)

doc = BeautifulSoup(result.text, 'html.parser')
# print(doc) 여기까진 소스코드가 출력됨.
review_list = doc.select('div.score_result ul li')
# select 가 코드에서부터 태그를 이용하여 정보를 수집하게 하는 듯

for i, one in enumerate(review_list):
    print('## USER -> {} ##################################'.format(i+1))

    # 평점 정보 수집
    score = one.select('div.star_score em')[0].get_text()

    # 리뷰 정보 수집
    review = one.select('div.score_reple p span')

    j = 0
    if len(review) == 2:  # +관람객
        j = 1
    if len(review) == 3:
        j = 2
    review_txt = review[j].get_text().strip()

    # 작성자 정보 수집
    original_writer = one.select('div.score_reple dt em')[0].get_text().strip()

    idx_end = original_writer.find('(')
    writer = original_writer[:idx_end]
    # 날짜 정보 수집
    original_date = one.select('div.score_reple dt em')[1].get_text()
    date = original_date[:10]

    print(':: REVIEW: {}'.format(review_txt))
    print(':: SCORE: {}'.format(score))
    print(':: WRITER: {}'.format(writer))
    print(':: DATE: {}'.format(date))
