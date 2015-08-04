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
from datetime import datetime
import unicodedata

metadata = MetaData()
URL = '/var/www/pythonParser/ivi'

def db_connect(name='root', passw = 'root', host = 'localhost', db = '2shans_local'):
    mysql = "mysql+pymysql://%s:%s@%s/%s?charset=utf8" % (name, passw, host, db)
    return create_engine(mysql, echo=False).connect()

# films
def parse_films():
    # return '%s/films_test.xml' % URL
    return '%s/films1.xml' % URL
    # return '%s/dff87a6bd3d42f12bbbaed83b49664' % URL

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
                                    Column('money_budget', VARCHAR(255)))


class Films_info(object):
    __tablename__ = 'films_info'
    id = Column(Integer, primary_key=True)
    def __init__(self, ivi_id, name_rus, name_eng, name_ukr, sites, episode_name_rus, episode_name_eng, episode_name_ukr, poster, season, episode, imdb_raiting, kinopoisk_raiting, origin_country, money_budget):
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

mapper(Films_info, films_info)

"""
end Films_info class
"""
e = db_connect(db='2shans_local')

def main():
    # pass
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
        url = []
        tags = []
        season  = []
        episode = []
        imdb_raiting = []
        kinopoisk_rating = []
        money_budget = []
        compilation = []

        # fl = parseIviXml_Films(parse_films())
        # print len(ct)
        # for ctg in fl:
        for node in tree.findall('contents'):
            for nd in node.findall('content'):
                # print nd.__dict__['_children']['compilation']
                # id
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
                        # print 'imdb_rating:'
                        # print imdb_raiting

                for n in nd.findall('kinopoisk_rating'):
                    # print 'id'
                    # print n.text
                    if n.text == None:
                        kinopoisk_rating.append(0)
                    else:
                        kinopoisk_rating.append(n.text)
                #title
                # print nd.__dict__['_children']

                for n in nd.findall('compilation'):
                    # print n.__dict__['_children']
                    # print n.text
                    if n.text == None:
                        for nt in nd.findall('title'):
                            # print 'compilation title:', nt.text
                            if nt.text == None:
                                compilation.append('0')
                            else:
                                compilation.append(nt.text)
                    else:
                        # print 'compilation:', n.text
                        compilation.append(n.text)

                #origin_country
                for n in nd.findall('origin_country'):
                    # print 'origin_country'
                    # print n.text
                    if n.text == None:
                        country.append(0)
                    else:
                        country.append(n.text)

                #origin_country
                for n in nd.findall('season'):
                    # print 'season'
                    # print n.text
                    if n.text == None:
                        season.append(0)
                    else:
                        season.append(n.text)
                    # print season
                for n in nd.findall('episode'):
                    # print 'episode:'
                    # print n.text
                    if n.text == None:
                        episode.append(0)
                    else:
                        episode.append(n.text)
                    # print season

                #
                for n in nd.findall('content_genres'):
                    for b in n.findall('content_genre'):
                        # films id
                        for a in b.findall('content_id'):
                            # print 'content_id'
                            # print a.text
                            film_id_summary.append(a.text)
                        # films id
                        for a in b.findall('content_genre_id'):
                            # print 'content_genre_id:'
                            # print a.text
                            content_genres.append(a.text)

                for n in nd.findall('persons'):
                    for p in n.findall('person'):
                        for person_ids in p.findall('person_id'):
                            # print person_ids.text
                            person_id.append(person_ids.text)

                        for person_id in p.findall('person_type_id'):
                            # print person_id.text
                            person_type_id.append(person_id.text)

                for posters in nd.findall('posters'):
                    # print 'posters:', posters.__dict__['_children']
                    if not posters.__dict__['_children']:
                        # print posters.__dict__['_children']
                        url.append('0')
                        continue
                    # print 'posters', type(posters)
                    else:
                        for poster in posters.findall('poster'):
                            # print 'poster:', poster.__dict__
                            # print 'poster', type(poster)
                            for files in poster.findall('files'):
                                # print 'file', files.__dict__
                                # print 'files', type(files)
                                for file in files.findall('file'):
                                    # print 'file', file.__dict__
                                    # print 'file', file.find('./url').text
                                    # print 'file', getattr(file,'attrib')
                                    for urll in file.findall('url'):
                                        # print 'urlll:', type(urll.text)
                                        # print 'urlll:', getattr(urll,'text')
                                        if urll.text == None:
                                            url.append('0')
                                        else:
                                            url.append(urll.text)


                for tagses in nd.findall('tagses'):
                    for tag in tagses.findall('tags'):
                        tags.append(tag.text)

    # films_info = zip(id, title, url, season, episode, imdb_raiting, kinopoisk_rating, country, money_budget)
    # films_summary_user = zip(film_id_summary, person_id, person_type_id)
    # films_summary_genres = zip(film_id_summary,content_genres)
    # print len(url)
    for i, fi in enumerate(id):
        pass
        # for f in fi:
        # print i, len(url)
        flms = Films_info(id[i], compilation[i], compilation[i], compilation[i], 'ivi', title[i].encode('utf-8'), title[i].encode('utf-8'), title[i].encode('utf-8'), url[i], season[i], episode[i], imdb_raiting[i], kinopoisk_rating[i], country[i], money_budget[i])
        Session = sessionmaker(bind=e)
        session = Session()
        session.add(flms)
        session.commit()

if __name__ == '__main__':
    main()