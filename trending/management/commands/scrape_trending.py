from django.core.management.base import BaseCommand
from trending.models import TrendingRepo
import requests
from bs4 import BeautifulSoup

class Command(BaseCommand):
    help = 'Scrape GitHub trending repos and save to DB'

    def handle(self, *args, **kwargs):
        url = 'https://github.com/trending'
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, 'html.parser')


        for repo in soup.select('article.Box-row'):
            name = repo.h2.text.strip().replace('\n', '').replace(' ', '')
            link = 'https://github.com' + repo.h2.a['href']
            desc_tag = repo.p
            description = desc_tag.text.strip() if desc_tag else ''
            star_tag = repo.select_one('a.Link--muted[href$="/stargazers"]')
            stars = int(star_tag.text.strip().replace(',', '')) if star_tag else 0
            lang_tag = repo.find('span', itemprop='programmingLanguage')
            language = lang_tag.text.strip() if lang_tag else ''

            TrendingRepo.objects.create(
                name=name,
                url=link,
                description=description,
                stars=stars,
                language=language
            )

        self.stdout.write(self.style.SUCCESS('Trending repos scraped successfully.'))
