#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'nictaporuk@yandex.ru'
__copyright__ = 'Copyright 2015 NickTaporuk'
__version__ = '0.0.1'

from sqlalchemy import *
from xml.etree import ElementTree
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper
from sqlalchemy.orm import sessionmaker
from datetime import datetime,date
import unicodedata

metadata = MetaData()

def db_connect(name='root', passw = 'root', host = 'localhost', db = '2shans_local'):
    mysql = "mysql+pymysql://%s:%s@%s/%s?charset=utf8" % (name, passw, host, db)
    return create_engine(mysql, echo=False).connect()

"""
класс Films_info
"""
mt = MetaData()

films_info = Table('films_info', mt,
              Column('id', Integer, primary_key=True),
                                    Column('ivi_id', Integer),
                                    Column('name_rus', Integer),
                                    Column('name_eng', Integer),
                                    Column('name_ukr', Integer),
                                    Column('sites', VARCHAR(255), default=null),# ivi parse
                                    Column('episode_name_rus', VARCHAR(255)),# ivi parse
                                    Column('episode_name_eng', VARCHAR(255)),# ivi parse
                                    Column('episode_name_ukr', VARCHAR(255)),# ivi parse
                                    Column('poster', VARCHAR(255), default=null), # film img
                                    Column('season', Integer),
                                    Column('episode', Integer),
                                    Column('imdb_raiting', VARCHAR(45)),
                                    Column('kinopoisk_raiting', VARCHAR(45)),
                                    Column('origin_country', VARCHAR(45)),
                                    Column('money_budget', VARCHAR(255)),
                                    Column('premiere_world', TIMESTAMP()))


class Films_info(object):
    __tablename__ = 'films_info'
    id = Column(Integer, primary_key=True)
    def __init__(self, ivi_id, name_rus, name_eng, name_ukr, sites, episode_name_rus, episode_name_eng, episode_name_ukr, poster, season, episode, imdb_raiting, kinopoisk_raiting, origin_country, money_budget, premiere_world):
        self.ivi_id = ivi_id
        self.name_rus = name_rus
        self.name_eng = name_eng
        self.name_ukr = name_ukr
        self.sites = sites
        self.episode_name_rus = episode_name_rus
        self.episode_name_eng = episode_name_eng
        self.episode_name_ukr = episode_name_ukr
        self.poster = poster
        self.season = season
        self.episode = episode
        self.imdb_raiting = imdb_raiting
        self.kinopoisk_raiting = kinopoisk_raiting
        self.origin_country = origin_country
        self.money_budget = money_budget
        self.premiere_world = premiere_world

mapper(Films_info, films_info)

"""
end Films_info class
"""


URL = '/var/www/pythonParser/ivi'

# films
def parse_films():
    # return '%s/films_test.xml' % URL
    return '%s/films1.xml' % URL

e = db_connect()
def main():
    pass
    with open(parse_films(), 'rt') as f:
        tree = ElementTree.parse(f)
        id = []
        title = []
        country = []
        content_genres = []
        content_genres = []
        film_id_summary = []
        person_type_id = []
        person_id =[]
        persons = []
        persons_summary = []
        url = []
        tags = []
        season  = []
        episode = []
        imdb_raiting = []
        kinopoisk_rating = []
        money_budget = []
        release_date = []
        compilation = []
        # """
        # fl = parseIviXml_Films(parse_films())
        # print len(ct)
        # for ctg in fl:
        for node in tree.findall('compilations'):
            for nd in node.findall('compilation'):
                # print nd.__dict__['_children']['compilation']
                # id
                # """
                for n in nd.findall('id'):
                    # print 'id'
                    # print n.text
                    if n.text == None:
                        id.append(0)
                    else:
                        id.append(n.text)
            # print 'imdb_raiting:'

                for n in nd.findall('imdb_rating'):
                    if n.text == None:
                        imdb_raiting.append(0)
                    else:
                        imdb_raiting.append(n.text)
                # release_date
                for n in nd.findall('first_series_date'):
                    if n.text == None:
                        # release_date.append(datetime.strptime(datetime.today(), "%Y-%m-%d"))
                        # print date.today()
                        release_date.append(date.today())
                    else:
                        release_date.append(n.text)

                for n in nd.findall('title'):
                    if n.text == None:
                        title.append(0)
                    else:
                        title.append(n.text)
                        # print 'imdb_rating:'
                        # print imdb_raiting
                for n in nd.findall('production_budget'):
                    if n.text == None:
                        money_budget.append(0)
                    else:
                        money_budget.append(n.text)

                for n in nd.findall('kinopoisk_rating'):
                    # print 'id'
                    # print n.text
                    if n.text == None:
                        kinopoisk_rating.append(0)
                    else:
                        kinopoisk_rating.append(n.text)
                #title
                # print nd.__dict__['_children']

                for nt in nd.findall('title'):
                    if nt.text == None:
                        compilation.append('0')
                    else:
                        compilation.append(nt.text)

                #origin_country
                for n in nd.findall('orig_country'):
                    if n.text == None:
                        country.append(0)
                    else:
                        country.append(n.text)

                #origin_country
                # for n in nd.findall('season'):
                #     if n.text == None:
                #         season.append(0)
                #     else:
                #         season.append(n.text)
                #
                # for n in nd.findall('episode'):
                #     if n.text == None:
                #         episode.append(0)
                #     else:
                #         episode.append(n.text)

                for n in nd.findall('content_genres'):
                    for b in n.findall('content_genre'):
                        for a in b.findall('content_id'):
                            film_id_summary.append(a.text)
                        for a in b.findall('content_genre_id'):
                            content_genres.append(a.text)
                """
                for i, n in enumerate(nd.findall('persons')):
                    print i
                    for p in n.findall('person'):
                        for person_ids in p.findall('person_id'):
                            # print 'person_id.text:', person_ids.text
                            if person_ids.text == None:
                                person_id.append(0)
                            else:
                                person_id.append(person_ids.text)

                        for person_type_ids in p.findall('person_type_id'):
                            # print 'person_type_id:', person_type_ids.text
                            if person_type_ids.text == None:
                                person_type_id.append(0)
                            else:
                                person_type_id.append(person_type_ids.text)
                    persons_summary.append([person_id, person_type_id])

                """

                for posters in nd.findall('posters'):
                    # print 'posters:', posters.__dict__['_children']
                    if not posters.__dict__['_children']:
                        url.append('0')
                        continue
                    else:
                        for poster in posters.findall('poster'):
                            for files in poster.findall('files'):
                                for file in files.findall('file'):
                                    for urll in file.findall('url'):
                                        if urll.text == None:
                                            url.append('0')
                                        else:
                                            url.append(urll.text)


                for tagses in nd.findall('tagses'):
                    for tag in tagses.findall('tags'):
                        tags.append(tag.text)
                # """

        # print len(id)
        # print len(compilation)
        # print len(title)
        # print len(url)
        # print len(imdb_raiting)
        # print len(kinopoisk_rating)
        # print len(money_budget)
        # print len(release_date)
        # print len(country)


        for i, fi in enumerate(id):
            pass
            # print id[i], compilation[i], url[i], money_budget[i], release_date[i]
            # print str(release_date[i])
            flms = Films_info(id[i], compilation[i], compilation[i], compilation[i], 'ivi', title[i], title[i], title[i], url[i], 0, 0, imdb_raiting[i], kinopoisk_rating[i], country[i], money_budget[i], str(release_date[i]))
        #     flms_genre = Films_summary(film_id_summary[i], 0, content_genres[i], 0, 0, 'ivi')
            Session = sessionmaker(bind=e)
            session = Session()
            # session.add(flms_genre) # genres
            session.add(flms)
            session.commit()

if __name__ == '__main__':
    main()