import sys
from pymongo import MongoClient

client = MongoClient()
db = client.uterus

def getQuotes():
    quotes = []
    more=True
    while more:
        new_quote = {}
        new_quote['quote'] = raw_input("quote: ")
        new_quote['author'] = raw_input("author: ")
        quotes.append(new_quote)
        more = raw_input("Do you have more quotes (y/n): ").lower()
        if more=='n' or more=='no':
            more=False
        else:
            more=True
    return quotes


def getPubs():
    pubs = []
    more=True
    while more:
        new_pub = {}
        new_pub['type'] = raw_input("type of publication: ")
        new_pub['author'] = raw_input("author: ")
        new_pub['title'] = raw_input("title: ")
        new_pub['url'] = raw_input("url: ")
        pubs.append(new_pub)
        more = raw_input("Do you have more publications (y/n): ").lower()
        if more=='n' or more=='no':
            more=False
        else:
            more=True
    return pubs

def getArgument(arg):
    argument = {}
    argument['title'] = raw_input(arg + " title: ")
    argument['text'] = raw_input(arg + " text: ")
    return argument


def getData():
    data = {}
    data['stance_id'] = raw_input("stance_id (url redirect): ")
    data['name'] = raw_input("name of this stance: ")
    data['query'] = raw_input("query for news: ")
    
    #anti abortion
    anti = {}
    anti['text'] = raw_input("anti summary: ")
    print "Please enter quotes for anti-abortion at prompt."
    anti['quotes'] = getQuotes()
    print "Please enter publications for anti-abortion at prompt."
    anti['publications'] = getPubs()
    data['anti'] = anti
    
    #rebuttal
    rebuttal = {}
    rebuttal['text'] = raw_input("rebuttal summary: ")
    print "Please enter quotes for rebuttal at prompt."
    rebuttal['quotes'] = getQuotes()
    print "Please enter publications for rebuttal at prompt."
    rebuttal['publications'] = getPubs()
    data['rebuttal'] = rebuttal
    
    #rhetoric
    data['pathos'] = getArgument('pathos')
    data['ethos'] = getArgument('ethos')
    data['logos'] = getArgument('logos')
    
    #sources
    print "Please enter your sources at prompt."
    data['sources'] = getPubs()
    return data


def printData(data):
    print 'stance_id: '+data['stance_id']
    print 'name: '+data['name']
    print 'query: '+data['query']
    print 'anti-abortion:'
    print ' summary: '+data['anti']['text']
    print ' quotes:'
    for qa in data['anti']['quotes']:
        print '    "'+qa['quote']+'" - '+qa['author']
    print ' publications:'
    for pa in data['anti']['publications']:
        print '    type: '+pa['type']+', title: '+pa['title']+', author: '+pa['author']+', url: '+pa['url']
    print 'rebuttal:'
    print ' summary: '+data['rebuttal']['text']
    print ' quotes:'
    for qr in data['rebuttal']['quotes']:
        print '    "'+qr['quote']+'" - '+qr['author']
    print ' publications:'
    for pr in data['rebuttal']['publications']:
        print '    type: '+pr['type']+', title: '+pr['title']+', author: '+pr['author']+', url: '+pr['url']
    print 'ethos:'
    print data['ethos']['title']+': '+data['ethos']['text']
    print 'pathos:'
    print data['pathos']['title']+': '+data['pathos']['text']
    print 'logos:'
    print data['logos']['title']+': '+data['logos']['text']
    print 'sources:'
    for source in data['sources']:
        print '  type: '+source['type']+', title: '+source['title']+', author: '+source['author']+', url: '+source['url']


def addNewDataDoc():
    correct = False
    while not correct:
        data = getData()
        print "\nPlease verify the data you have entered."
        printData(data)
        correct = raw_input("\nDoes this look correct to you (y/n)? ").lower()
        if correct=='n' or correct=='no':
            correct = False
        else:
            correct = True
    db.stances.insert(data)




def main():
    more = True
    while more:
        addNewDataDoc()
        more = raw_input('Do you have another doc to add (y/n)? ')
        if more=='n' or more=='no':
            more=False
        else:
            more=True




if __name__ == "__main__":
    main()
