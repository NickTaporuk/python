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

def db_connect(name='root', passw = 'root', host = 'localhost', db = '2shans_local'):
    mysql = "mysql+pymysql://%s:%s@%s/%s?charset=utf8" % (name, passw, host, db)
    return create_engine(mysql, echo=False).connect()

"""
Tests table
"""
person = Table('person', metadata, Column('id', Integer, primary_key=True), Column('name', String(25), nullable=False),Column('date_create', DateTime, default=datetime.now()))

class Person(object):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    date_create = Column(DateTime, default=datetime.now())

    def __init__(self, name, date_create):
        self.name           = name
        self.date_create    = date_create

    def __repr__(self):
        return "<Person('%s','%s')>" % ( self.name, self.date_create)

mapper(Person, person)

"""
end table
"""

"""
класс Недвижимости
"""
mt = MetaData()

estate = Table('estate', mt, Column('id', Integer, primary_key=True),
                                    Column('city', VARCHAR(255), default=null),
                                    Column('area', VARCHAR(255), default=null),
                                    Column('street', VARCHAR(255), default=null),
                                    Column('home', VARCHAR(255), default=null),
                                    Column('storey', SmallInteger(), default=null),
                                    Column('link', VARCHAR(255), default=null),
                                    Column('yardage', Integer(), default=null),
                                    Column('state_object', Text(), default=null),
                                    Column('date_placement', Integer(), default=null),
                                    Column('date_parsing', Integer(), default=null),
                                    Column('price', Integer(), default=null),
                                    Column('currency', VARCHAR(4), default=null),
)

class Estate(object):
    __tablename__ = 'estate'
    id = Column(Integer, primary_key=True)
    def __init__(self, city, area, street, home, storey, link, yardage, state_object, comment, date_placement, date_parsing, price, currency):
        # self.id             = id
        self.city           = city
        self.area           = area
        self.street         = street
        self.home           = home
        self.storey           = storey
        self.link           = link
        self.yardage        = yardage
        self.state_object   = state_object
        self.comment        = comment
        self.date_placement = date_placement
        self.date_parsing   = date_parsing
        self.price          = price
        self.currency       = currency

    def __repr__(self):
        return "<Estate('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')>" % (self.city, self.area, self.street, self.home, self.storey, self.link, self.yardage, self.state_object, self.comment, self.date_placement, self.date_parsing, self.price, self.currency)

mapper(Estate, estate)

"""
end Estate class
"""

"""
класс Genre
"""
mt = MetaData()

genre = Table('films_genres', mt,
              Column('id', Integer, primary_key=True),
                                    Column('ivi_id', Integer),
                                    Column('name_rus', VARCHAR(255)),
                                    Column('category_id', VARCHAR(255), default=null),
                                    Column('genre_link', VARCHAR(255), default=null),)

class Genre(object):
    __tablename__ = 'films_genres'
    id = Column(Integer, primary_key=True)
    def __init__(self, ivi_id, name_rus, category_id, genre_link):
        self.ivi_id = ivi_id
        self.name_rus = name_rus
        self.category_id = category_id
        self.genre_link = genre_link

    # def __repr__(self):
        # return "<Estate('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')>" % (self.city, self.area, self.street, self.home, self.storey, self.link, self.yardage, self.state_object, self.comment, self.date_placement, self.date_parsing, self.price, self.currency)

mapper(Genre, genre)

"""
end Genre class
"""
"""
класс films_team_parts(type persons)
"""
mt = MetaData()

films_team_parts = Table('films_team_parts', mt,
              Column('id', Integer, primary_key=True),
                                    # Column('ivi_id', Integer),
                                    Column('name_rus', VARCHAR(255)),
                                    Column('name_eng', VARCHAR(255)),
                                    Column('name_ukr', VARCHAR(255)),)

class Films_team_parts(object):
    __tablename__ = 'films_genres'
    id = Column(Integer, primary_key=True)
    def __init__(self, name_rus, name_eng, name_ukr):
        self.name_rus = name_rus
        self.name_eng = name_eng
        self.name_ukr = name_ukr

mapper(Films_team_parts, films_team_parts)

"""
end Genre class
"""

"""
класс films_team(persons)
"""
mt = MetaData()

films_team = Table('films_team', mt,
              Column('id', Integer, primary_key=True),
                                    Column('ivi_id', Integer),
                                    Column('name_rus', VARCHAR(255)),
                                    Column('name_eng', VARCHAR(255)),
                                    Column('name_ukr', VARCHAR(255)),
                                    Column('biography_rus', VARCHAR(255)),
                                    Column('biography_eng', VARCHAR(255)),
                                    Column('biography_ukr', VARCHAR(255)),
                                    Column('poster', VARCHAR(255)),
                                    Column('best', Integer),)

class Films_team(object):
    __tablename__ = 'films_team'
    id = Column(Integer, primary_key=True)
    def __init__(self, ivi_id, name_rus, name_eng, name_ukr, biography_rus, biography_ukr, biography_eng, poster, best):
        self.ivi_id = ivi_id
        self.name_rus = name_rus
        self.name_eng = name_eng
        self.name_ukr = name_ukr
        self.biography_rus = biography_rus
        self.biography_ukr = biography_ukr
        self.biography_eng = biography_eng
        self.poster = poster
        self.best = best

mapper(Films_team, films_team)

"""
end Genre class
"""

"""
класс Country
"""
mt = MetaData()

country = Table('films_countries', mt,
              Column('id', Integer, primary_key=True),
                                    Column('ivi_id', Integer),
                                    Column('name_rus', VARCHAR(255)),
                                    Column('name_eng', VARCHAR(255)),
                                    Column('name_ukr', VARCHAR(255)))

class Country(object):
    __tablename__ = 'films_countries'
    id = Column(Integer, primary_key=True)
    def __init__(self, ivi_id, name_rus, name_eng, name_ukr):
    # def __init__(self, ivi_id, category_id, genre_link):
        self.ivi_id = ivi_id
        self.name_rus = name_rus
        self.name_eng = name_eng
        self.name_ukr = name_ukr

    # def __repr__(self):
        # return "<Estate('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')>" % (self.city, self.area, self.street, self.home, self.storey, self.link, self.yardage, self.state_object, self.comment, self.date_placement, self.date_parsing, self.price, self.currency)

mapper(Country, country)

"""
end Genre class
"""

"""
класс Category
"""
mt = MetaData()

category = Table('films_category', mt,
              Column('id', Integer, primary_key=True),
                                    Column('ivi_id', Integer),
                                    Column('title', VARCHAR(255)),
                                    Column('descriptions', VARCHAR(255), default=null),
                                    Column('link', VARCHAR(255), default=null),)


class Category(object):
    __tablename__ = 'films_category'
    id = Column(Integer, primary_key=True)
    def __init__(self, ivi_id, title, descriptions, link):
    # def __init__(self, ivi_id, descriptions, link):
        self.ivi_id           = ivi_id
        self.title            = title
        self.descriptions     = descriptions
        self.link             = link

    # def __repr__(self):
        # return "<Estate('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')>" % (self.city, self.area, self.street, self.home, self.storey, self.link, self.yardage, self.state_object, self.comment, self.date_placement, self.date_parsing, self.price, self.currency)

mapper(Category, category)

"""
end Category class
"""

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
                                    Column('premiere_world', VARCHAR(255)))


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

"""
класс Films_summary
"""
mt = MetaData()

films_summary = Table('films_summary', mt,
              Column('id', Integer, primary_key=True),
                                    Column('film_id', Integer),
                                    Column('person_id', Integer),
                                    Column('genre_id', Integer),
                                    Column('country_id', Integer),
                                    Column('part_id', Integer),
                                    Column('films_site', VARCHAR(45)))


class Films_summary(object):
    __tablename__ = 'films_summary'
    id = Column(Integer, primary_key=True)
    def __init__(self, film_id, person_id, genre_id, country_id, part_id, films_site):
        self.film_id = film_id
        self.person_id = person_id
        self.genre_id = genre_id
        self.country_id = country_id
        self.part_id = part_id
        self.films_site = films_site

mapper(Films_summary, films_summary)

"""
end Films_info class
"""

# e = db_connect()

# print table.select().limit(1)
# print e.execute(table.select().limit(1), name='NickTaporuk')
# metadata.create_all(e)

# Session = sessionmaker(bind=e)
# session = Session()
# person = Person(name='Tests')
# session.add(Person('Tests1', datetime.now()))
# session.add(Estate('Tests1', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1))
# print session.new
# session.commit()
# print datetime.now()
"""
==========================================================================================
"""

"""

"""

URL = '/var/www/pythonParser/ivi'
# Жанры
def parse_genres():
    return '%s/genre.xml' % URL

# Роль участника фильма
def parse_role_persons():
    return '%s/persons_type.xml' % URL

# категории фильмов
def parse_category():
    return '%s/category.xml' % URL

# актёры
def parse_actors():
    return '%s/actors.xml' % URL

# cтраны
def parse_countries():
    return '%s/countries.xml' % URL
# type persons
def parse_type_persons():
    return '%s/persons_type.xml' % URL

# type persons
def parse_persons():
    # return '%s/dff87a6bd3d42f12bbbaed83b49664' % URL
    return '%s/persons1.xml' % URL
    # return '%s/persons2.xml' % URL
    # return '%s/persons3.xml' % URL
    # return '%s/persons4.xml' % URL
    # return '%s/persons5.xml' % URL
    # return '%s/persons6.xml' % URL
    # return '%s/persons7.xml' % URL
    # return '%s/persons8.xml' % URL
    # return '%s/persons9.xml' % URL
    # return '%s/persons10.xml' % URL
    # return '%s/persons11.xml' % URL
    # return '%s/persons12.xml' % URL
    # return '%s/persons13.xml' % URL
    # return '%s/persons14.xml' % URL
    # return '%s/persons15.xml' % URL
    # return '%s/persons16.xml' % URL
    # return '%s/persons17.xml' % URL

# films
def parse_films():
    # return '%s/films_test.xml' % URL
    # return '%s/films1.xml' % URL
    # print '%s/films2.xml' % URL
    return '%s/films2.xml' % URL
    # return '%s/films3.xml' % URL
    # return '%s/films4.xml' % URL
    # return '%s/films5.xml' % URL
    # return '%s/f  ilms6.xml' % URL
    # return '%s/dff87a6bd3d42f12bbbaed83b49664' % URL

def parseIviXml_Category(link):
    with open(link, 'rt') as f:
        """
            Название
            ID
            LINK
        """
        ivi_id = []
        title = []
        description = []
        link = []
        """
            End
        """
        tree = ElementTree.parse(f)
        for node in tree.iter('id'):
            # print node.tag,node.text, node.attrib
            ivi_id.append(node.text)

        for node in tree.iter('title'):
            title.append(node.text)

        for node in tree.iter('description'):
            description.append(node.text)

        for node in tree.iter('hru'):
            # print node.tag,node.text, node.attrib
            link.append(node.text)

        return zip(ivi_id, title, description, link)

def parseIviXml_Genre(link):
    with open(link, 'rt') as f:
        """
            Название
            ID
            LINK
        """
        id = []
        category_id = []
        title = []
        description = []
        hru = []
        """
            End
        """
        tree = ElementTree.parse(f)

        for node in tree.iter('id'):
            # print node.tag,node.text, node.attrib
            id.append(node.text)

        for node in tree.iter('category_id'):
            category_id.append(node.text)

        for node in tree.iter('title'):
            title.append(node.text)


        for node in tree.iter('hru'):
            hru.append(node.text)

        return zip(id, title, category_id, hru)

def parseIviXml_Films(link):
    with open(link, 'rt') as f:
        tree = ElementTree.parse(f)
        """
            Название
            ID
            LINK
        """
        id = []
        category_id = []
        title = []
        description = []
        hru = []
        """
            End
        """

        for node in tree.iter('id'):
            # print node.tag,node.text, node.attrib
            id.append(node.text)

        for node in tree.iter('category_id'):
            category_id.append(node.text)

        for node in tree.iter('title'):
            title.append(node.text)

        # for node in tree.iter('description'):
        #     description.append(node.text)

        for node in tree.iter('hru'):
            hru.append(node.text)

        return zip(id, title, category_id, hru)


def insert_genre(data):
    # gs = Genre(data[0], data[1], data[2], data[3])
    # data[1].encode('utf-8')
    # data[1].decode('latin-1')
    # st = da
    # ta[1].decode('utf-8')
    st = data[1]

    # print st
    # otherString = unicode(data[1], 'utf-8')
    # print st
    # print type(st)
    if type(st) == type(str()):
    #     print st
    #     gs = Genre(data[0], st, '1', '1')
    #     e = db_connect()

        # Session = sessionmaker(bind=e)
        # session = Session()
        # session.add(Genre(1, '1', '1', '1'))
        # session.add(Genre(data[0], data[1], '1', '1'))
        # session.add(gs)
        # session.commit()
        pass
    else:
        pass
        # print data[1]
        # dd = data[1].encode('utf-8')
        # dd = data[1]
        # tt = st.decode('utf-8')
        # print type(st)
        # print (tt)
        # """
        # gs = Genre(data[0], dd, '1', '1')
        # e = db_connect()

        # Session = sessionmaker(bind=e)
        # session = Session()
        # session.add(Genre(1, '1', '1', '1'))
        # session.add(Genre(data[0], data[1], '1', '1'))
        # session.add(gs)
        # session.commit()
        # """
    # print session
    #     pass


"""
==========================================================================================
"""
e = db_connect()
def main():
    pass
    """
    # GENRE PARSE
    gr = parseIviXml_Genre(parse_genres())
    for gnr in gr:
        # insert_genre(gnr)
        # print gnr[1]
        # set_data_to_file('TESTS.TXT',gnr[1].encode('utf-8'))
        test = Genre(gnr[0], gnr[1].encode('utf-8'), gnr[2].encode('utf-8'), gnr[3].encode('utf-8'))
        e = db_connect()
        Session = sessionmaker(bind=e)
        session = Session()
        session.add(test)
        session.commit()
    """

    """
    # Category PARSE
    ct = parseIviXml_Category(parse_category())
    # print len(ct)
    for ctg in ct:
    #     print ctg
        if ctg[2] == None:
            # for ctr in ct:
                # c = []
            test = Category(ctg[0], ctg[1].encode('utf-8'), 0, ctg[3].encode('utf-8'))
            e = db_connect()
            Session = sessionmaker(bind=e)
            session = Session()
            session.add(test)
            session.commit()

        else:
            test = Category(ctg[0], ctg[1].encode('utf-8'), ctg[2].encode('utf-8'), ctg[3].encode('utf-8'))
            e = db_connect()
            Session = sessionmaker(bind=e)
            session = Session()
            session.add(test)
            session.commit()
    """
    # """
    # Films PARSE
    # print parse_films()
    # print parse_films()
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

        # fl = parseIviXml_Films(parse_films())
        # print len(ct)
        # for ctg in fl:
        for node in tree.findall('contents'):
            # print 111
            for g, nd in enumerate(node.findall('content')):
                # print nd.__dict__['_children']['compilation']
                # id
                for nff in nd.findall('sharing_disabled'):
                    print nff.text
                    if nff.text == '0':
                        for n in nd.findall('id'):
                            # print 'id'
                            # print n.text
                            if n.text == None:
                                id.append(0)
                            else:
                                id.append(n.text)
                        # """
                        # print 'imdb_raiting:'

                        for n in nd.findall('imdb_rating'):
                            if n.text == None:
                                imdb_raiting.append(0)
                            else:
                                imdb_raiting.append(n.text)
                        # release_date
                        for n in nd.findall('release_date'):
                            if n.text == None:
                                release_date.append(0)
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
                        """

                        for n in nd.findall('persons'):
                            for i, p in enumerate(n.findall('person')):
                                for j, person_ids in enumerate(p.findall('person_id')):
                                    # print person_ids.text
                                    if person_ids.text == None:
                                        # person_id.append(0)
                                        # persons_summary[g][i][j].append({'person_id', 0})
                                        pass
                                    else:
                                        pass
                                        # print g
                                        # person_id.append(person_ids.text)
                                        # person_summary.append([i, person_ids.text])
                                        # persons_summary[g][i][j].append({'person_id', person_ids.text})
                                        # persons_summary.append([g, [i, {'person_id', person_ids.text}]])

                                for j, person_type_ids in enumerate(p.findall('person_type_id')):
                                    # print person_id.text
                                    if person_type_ids.text == None:
                                        pass
                                        # person_type_id.append(0)
                                        # persons_summary.append([g, [i, {'person_type_id', 0}]])
                                        # persons_summary[g][i][j].append({'person_type_id', 0})
                                    else:
                                        pass
                                        # person_type_id.append(person_type_ids.text)
                                        # persons_summary.append([g, [i, {'person_type_id', person_type_ids.text}]])
                                        # persons_summary[g][i][j].append({'person_type_id', person_type_ids.text})
                                # print len(person_id)
                                # print len(person_type_id)
                                # persons_summary.append([person_id, person_type_id])

                        # """

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
                                # pass
                                # print tag.text
                        # """

        # print tags
        #
    # print len(id)
    # print len(persons_summary)
    # for i, fi in enumerate(id): # films_info
    # for i, fi in enumerate(persons_summary):
        # pass
        # print i, len(persons_summary[i]), '\n'
        # print i, persons_summary[i], '\n'
        """
            persons summary to db
        """
        # for j, p in enumerate(persons_summary[i][0]):
        #     print j, len(persons_summary[i][j]), '\n'
        #     print j, id[i]
            # print j, persons_summary[i][0][j]
            # print j, persons_summary[i][1][j]
            # flms_genre = Films_summary(id[i], persons_summary[i][0][j], 0, 0, persons_summary[i][1][j], 'ivi')
            # Session = sessionmaker(bind=e)
            # session = Session()
            # session.add(flms_genre)
            # session.commit()
            # pass
        # for f in fi:
    # print len(release_date)
    print len(id)
    # print len(compilation)
    # print len(title)
    # print len(url)
    for i, fi in enumerate(id):
        flms = Films_info(id[i], compilation[i], compilation[i], compilation[i], 'ivi', title[i].encode('utf-8'), title[i].encode('utf-8'), title[i].encode('utf-8'), url[i], season[i], episode[i], imdb_raiting[i], kinopoisk_rating[i], country[i], money_budget[i], release_date[i])
        # flms_genre = Films_summary(film_id_summary[i], 0, content_genres[i], 0, 0, 'ivi')
        Session = sessionmaker(bind=e)
        session = Session()
        # session.add(flms_genre) # genres
        session.add(flms)
        session.commit()
    # """

    """
    if ctg[2] == None:
        # for ctr in ct:
            # c = []
        test = Category(ctg[0], ctg[1].encode('utf-8'), 0, ctg[3].encode('utf-8'))
        e = db_connect()
        Session = sessionmaker(bind=e)
        session = Session()
        session.add(test)
        session.commit()

    else:
        test = Category(ctg[0], ctg[1].encode('utf-8'), ctg[2].encode('utf-8'), ctg[3].encode('utf-8'))
        e = db_connect()
        Session = sessionmaker(bind=e)
        session = Session()
        session.add(test)
        session.commit()
    """

    """
        parse Country
    """
    """

    with open(parse_countries(), 'rt') as f:
        tree = ElementTree.parse(f)
        ivi_id = []
        title = []

        for node in tree.findall('countries'):
            for nd in node.findall('country'):
                # print nd.__dict__['_children']['compilation']
                # id
                for n in nd.findall('id'):
                    # print 'id'
                    print n.text
                    if n.text == None:
                        ivi_id.append(0)
                    else:
                        ivi_id.append(n.text)
                for n in nd.findall('title'):
                    # print 'id'
                    print n.text
                    if n.text == None:
                        title.append(0)
                    else:
                        title.append(n.text)

    for i, fi in enumerate(ivi_id):

        cntr = Country(ivi_id[i], title[i], title[i], title[i])
        Session = sessionmaker(bind=e)
        session = Session()
        session.add(cntr)
        session.commit()
    """

    """
        parse Films_team_parts(Type person to films)
    """
    """

    with open(parse_type_persons(), 'rt') as f:
        tree = ElementTree.parse(f)
        person_type = []

        for node in tree.findall('persons_type'):
            # print node
            for nd in node.findall('person_type'):
                for n in nd.findall('title'):
                    # print 'id'
                    # print n.text
                    if n.text == None:
                        person_type.append(0)
                    else:
                        person_type.append(n.text)

    for i, fi in enumerate(person_type):

        cntr = Films_team_parts(person_type[i], person_type[i], person_type[i])
        Session = sessionmaker(bind=e)
        session = Session()
        session.add(cntr)
        session.commit()
    """

    """
        parse persons(Type persons)
    """
    """

    with open(parse_persons(), 'rt') as f:
        tree = ElementTree.parse(f)
        ivi_id = []
        url = []
        name = []
        eng_title = []
        best = []
        person_type = []
        bio = []

        for node in tree.findall('persons'):
            # print node
            for nd in node.findall('person'):
                for n in nd.findall('id'):
            #         print 'id'
            #         print n.text
                    if n.text == None:
                        ivi_id.append(0)
                    else:
                        ivi_id.append(n.text)

                for n in nd.findall('posters'):
                    if not n.__dict__['_children']:
                        # print n
                        url.append('0')
                        continue
                    else:
                        for file in n.findall('file'):
                            for urls in file.findall('url'):
                                # print 'urls:', urls.__dict__    # print 'id'
                                # print urls.text
                                if urls.text == None:
                                    url.append('0')
                                else:
                                    url.append(urls.text)

                            # if len(url_buffer) > 1:
                            #     print url_buffer
                            #     url.append(url_buffer[0])
                            # else:
                            #     url.append(url_buffer)

                for names in nd.findall('name'):
                    # print names.text
                    if names.text == None:
                        name.append('0')
                    else:
                        name.append(names.text)

                for star in nd.findall('is_star'):
                    # print star.text
                    if star.text == None:
                        best.append(0)
                    else:
                        best.append(star.text)

                for eng_titles in nd.findall('eng_title'):
                    # print eng_titles.text
                    if eng_titles.text == None:
                        eng_title.append('0')
                    else:
                        eng_title.append(eng_titles.text)

                for bios in nd.findall('bio'):
                    # print bios.text.replace('[html]', '').replace('[/html]', '')
                    if bios.text == None:
                        bio.append('0')
                    else:
                        bio.append(bios.text.replace('[html]', '').replace('[/html]', ''))

    # print len(name)
    # print len(ivi_id)
    # print len(url)
    # print len(best)
    # print len(bio)
    # print len(eng_title)
    name_eng = ''
    for i, fi in enumerate(ivi_id):
        # print url[i]
        # pass
        if(eng_title[i] == '0'):
            name_eng = name[i]
        else:
            name_eng = eng_title[i]
        cntr = Films_team(ivi_id[i], name[i].encode('utf-8'), name_eng.encode('utf-8'), name[i].encode('utf-8'), bio[i].encode('utf-8'), bio[i].encode('utf-8'), bio[i].encode('utf-8'), url[i].encode('utf-8'), best[i])
        Session = sessionmaker(bind=e)
        session = Session()
        session.add(cntr)
        session.commit()
    # """


def set_data_to_file(name, string, action = 'w'):
    infile = open(name, action)#дозапись - a,запись-w...
    infile.write(str(string))

if __name__ == '__main__':
    main()

# main()
