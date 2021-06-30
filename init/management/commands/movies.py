import random

from django.core.management.base import BaseCommand
from django.utils import timezone

from movies.models import Movie, AudienceRating, Tag, Actor, Director, Genre, Type, Image


class Command(BaseCommand):

    def handle(self, *args, **options):
        audience_ratings = [a.id for a in AudienceRating.objects.all()]
        tags = [t.id for t in Tag.objects.all()]
        actors = [a.id for a in Actor.objects.all()]
        directors = [d.id for d in Director.objects.all()]
        genres = [g.id for g in Genre.objects.all()]
        types = [t.id for t in Type.objects.all()]
        movies = [
            "크루엘라",
            "분노의 질주 : 더 얼티메이트",
            "캐시트럭",
            "미스피츠",
            "극장판 귀멸의 칼날: 무한열차편",
            "컨저링3: 악마가 시켰다",
            "뱅드림! 로젤리아 에피소드Ⅰ: 약속",
            "낫아웃"
        ]
        images = [
            "https://img.megabox.co.kr/SharedImg/2021/06/17/gD32uTBzzyhwn3jfo0Dreen21yOreg1G_420.jpg",
            "https://img.megabox.co.kr/SharedImg/2021/06/08/Q5Y9atPdJb9iBFrXioDhutbYXYKrym0J_420.jpg",
            "https://img.megabox.co.kr/SharedImg/2021/06/25/jTfTukBff6HNvvlmQdKaggWKdztTEfsT_420.jpg",
            "https://img.megabox.co.kr/SharedImg/2021/05/12/J7vthd2FWEXswHD67dL2rQrMW4uhJQUF_420.jpg",
            "https://img.megabox.co.kr/SharedImg/2021/06/11/x3UYeEs3EarcB4f5VfBSoySRtAAhvuvw_420.jpg",
            "https://img.megabox.co.kr/SharedImg/2021/06/10/3xVKOmh4Iykg9nMdGqkA3hwCMUhk3UjS_420.jpg",
            "https://img.megabox.co.kr/SharedImg/2021/06/15/wb0WDanD2YotcwWpCfpJw70RdGgSKNCY_420.jpg",
            "https://img.megabox.co.kr/SharedImg/2021/06/16/7EcZgh6z5Myiy3MJT97KN5lQJgs8xwRF_420.jpg"
        ]
        back_images = [
            "https://img.megabox.co.kr/SharedImg/2021/05/03/qQLnqQbHy4OK9tWeDWl18VxXuL6Unxsi_380.jpg",
            "https://img.megabox.co.kr/SharedImg/2021/04/27/pmA4YuR5jkq3Ovd9XGSUGQFYBiUyVpUd_380.jpg",
            "https://img.megabox.co.kr/SharedImg/2021/05/03/tJsg5q31GMZzH6YB6uvJgguaP0xR3ZFQ_380.jpg",
            "https://img.megabox.co.kr/SharedImg/2021/05/03/tEgFFSZAIKq8tDGzlM3S90xFCQKpTWSq_380.jpg",
            "https://img.megabox.co.kr/SharedImg/2021/05/03/W6CsCFmjy8VTMOEroE37H9ZxiOA0kBe1_380.jpg",
            "https://img.megabox.co.kr/SharedImg/2021/05/10/yJVRlCIAkU35wMXPsLBkXf2pUcLdM9rZ_380.jpg",
            "https://img.megabox.co.kr/SharedImg/2021/05/10/aQLVjdGskUAsvfL23WkGXT0dS3Gwj62K_380.jpg",
            "https://img.megabox.co.kr/SharedImg/2021/05/10/KQWXnPq0p3x6Il9VaIWDQb3UfXJUZUlS_380.jpg"
        ]

        days = [
            timezone.now(),
            timezone.now() + timezone.timedelta(days=1),
            timezone.now() + timezone.timedelta(days=2),
            timezone.now() + timezone.timedelta(days=3),
            timezone.now() + timezone.timedelta(days=4),
            timezone.now() + timezone.timedelta(days=5),
            timezone.now() + timezone.timedelta(days=6),
            timezone.now() + timezone.timedelta(days=7),
            timezone.now() + timezone.timedelta(days=8),
            timezone.now() + timezone.timedelta(days=9),
            timezone.now() + timezone.timedelta(days=10),
            timezone.now() + timezone.timedelta(days=11),
            timezone.now() + timezone.timedelta(days=12),
            timezone.now() + timezone.timedelta(days=13),
            timezone.now() + timezone.timedelta(days=14),
            timezone.now() + timezone.timedelta(days=15),
            timezone.now() - timezone.timedelta(days=1),
            timezone.now() - timezone.timedelta(days=2),
            timezone.now() - timezone.timedelta(days=3),
            timezone.now() - timezone.timedelta(days=4),
            timezone.now() - timezone.timedelta(days=5),
            timezone.now() - timezone.timedelta(days=6),
            timezone.now() - timezone.timedelta(days=7),
        ]

        for i in range(100):
            date = random.choice(days)
            a = random.choice(audience_ratings)
            t = random.choices(tags, k=2)
            ac = random.choices(actors, k=5)
            d = random.choices(directors, k=1)
            g = random.choices(genres, k=2)
            ty = random.choices(types, k=2)
            m = random.choice(movies)

            movie = Movie.objects.create(
                title=m,
                english_title="Cruella",
                content="처음부터 난 알았어. 내가 특별하단 걸\
                \
                  그게 불편한 인간들도 있겠지만 모두의 비위를 맞출 수는 없잖아?\
                  그러다 보니 결국, 학교를 계속 다닐 수가 없었지\
                \
                  우여곡절 런던에 오게 된 나, 에스텔라는 재스퍼와 호레이스를 운명처럼 만났고\
                  나의 뛰어난 패션 감각을 이용해 완벽한 변장과 빠른 손놀림으로 런던 거리를 싹쓸이 했어\
                \
                  도둑질이 지겹게 느껴질 때쯤, 꿈에 그리던 리버티 백화점에 낙하산(?)으로 들어가게 됐어\
                  거리를 떠돌았지만 패션을 향한 나의 열정만큼은 언제나 진심이었거든\
                \
                  근데 이게 뭐야, 옷에는 손도 못 대보고 하루 종일 바닥 청소라니\
                  인내심에 한계를 느끼고 있을 때, 런던 패션계를 꽉 쥐고 있는 남작 부인이 나타났어\
                  천재는 천재를 알아보는 법! 난 남작 부인의 브랜드 디자이너로 들어가게 되었지\
                \
                  꿈을 이룰 것 같았던 순간도 잠시, 세상에 남작 부인이 ‘그런 사람’이었을 줄이야…\
                \
                  그래서 난 내가 누군지 보여주기로 했어\
                  잘가, 에스텔라\
                \
                  난 이제 크루엘라야!",
                opening_date=date,
                running_time=133,
                ticketing_rate='0.0',
                audience_rating_id=a,
                like_count=0
            )

            movie.tag.clear()
            movie.tag.add(*t)
            movie.actor.clear()
            movie.actor.add(*ac)
            movie.director.clear()
            movie.director.add(*d)
            movie.genre.clear()
            movie.genre.add(*g)
            movie.type.clear()
            movie.type.add(*ty)

        for movie in Movie.objects.all():
            main_image = random.choice(images)
            back_image = random.choice(back_images)
            etc = random.choices(back_images, k=3)

            Image.objects.create(
                movie=movie,
                url=main_image,
                type=1
            )
            Image.objects.create(
                movie=movie,
                url=back_image,
                type=2
            )
            for i in etc:
                Image.objects.create(
                    movie=movie,
                    url=i,
                    type=3
                )
