# -*- encoding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import os

#*LiveBanka*

def download_main():
    list_of_pages=[
        "http://katalogoskiniton.com/prothema/690",
        "http://katalogoskiniton.com/prothema/693",
        "http://katalogoskiniton.com/prothema/694",
        "http://katalogoskiniton.com/prothema/695",
        "http://katalogoskiniton.com/prothema/697",
        "http://katalogoskiniton.com/prothema/698",
        "http://katalogoskiniton.com/prothema/699"
        ]
    for page in list_of_pages:
        connection = urllib2.urlopen (page)
        html_page = BeautifulSoup(connection, 'html.parser')
        file = open('main/' + page[-3:] + '.html', 'w+')
        file.write(html_page.encode("utf-8"))
        connection.close()
        file.close()
        print page[-3:] +" Done"
    print "FUNCTION DOWNLOAD_MAIN [DONE]"



def download_sub():
    for file in os.listdir(os.path.join("main")):
        sub_connection = urllib2.urlopen ('file:///' + os.path.abspath('main/'+file))
        sub_html_page = BeautifulSoup(sub_connection , 'html.parser')
        id_container = sub_html_page.find("div", { "id" : "part1_id" })
        phone_numbers_links = id_container.find_all("a")
        for phone_numbers_link in phone_numbers_links:
            phone_sub_page = 'http://katalogoskiniton.com/' + phone_numbers_link.get('href')
            phone_sub_connection = urllib2.urlopen(phone_sub_page)
            phone_sub_html_page = BeautifulSoup(phone_sub_connection, 'html.parser')
            sub_file_name = phone_numbers_link.getText()[:6]
            sub_file = open('sub/'+sub_file_name + '.html','w+')
            sub_file.write(phone_sub_html_page.encode("utf-8"))
            sub_file.close()
            print sub_file_name , " Done"
    print 'FUNCTION DOWNLOAD_SUB [DONE]'

def get_numbers():
    numbers = open('numbers.txt','w+')
    for subfile in os.listdir(os.path.join('sub')):
        phone_page = urllib2.urlopen('file:///'+ os.path.abspath('sub/') + '/' + subfile )
        phone_html_page = BeautifulSoup(phone_page , 'html.parser')
        phone_container  = phone_html_page.find("div", { "id" : "part2_id" })
        numbers_links = phone_container.find_all('a')
        for link in numbers_links:
            numbers.write(link.getText() + '\n')
            print '[DONE]' , link.getText()
    numbers.close()
    print 'FUNCTION GET_NUMBERS [DONE]'


print "*LiveBanka*"
download_main()
download_sub()
get_numbers()
