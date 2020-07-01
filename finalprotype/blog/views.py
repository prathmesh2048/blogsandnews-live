from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


def blog_listing(request):
    final_postings = []
    list_for_base = ['http://thedronegirl.com/', 'http://thedronegirl.com/page/2/', 'http://thedronegirl.com/page/3/',
                     'http://thedronegirl.com/page/4/', 'http://thedronegirl.com/page/5/', ]
    for things in list_for_base:
        page = requests.get(things)
        soup = BeautifulSoup(page.text, 'html.parser')
        links = soup.find('div', class_='front-page-content').find_all('article', class_='rsrc-archive col-md-6')
        for i in links:
            first_block = i.find('div', class_='featured-thumbnail col-md-12')
            for_link = first_block.find('a').get('href')
            for_img = first_block.find('a').find('img').get('src')
            # print(for_img)
            # print(for_link)
            second_block = i.find('div', class_='home-header col-md-12')
            heading = second_block.find('header').find('h2', class_='page-header').text
            date = second_block.find('header').find('p', class_='post-meta text-left').find('time').text
            para = second_block.find('div', class_='entry-summary').text
            # print(heading)
            # print(date)
            # print(para)
            final_postings.append((for_img, for_link, heading, date, para))

    template = 'blog/blog_list.html'
    context = {
        'data': final_postings,
    }
    return render(request, template, context)


def blog_home_page(request):
    context = {}
    template = 'blog/video.html'
    return render(request, template, context)


def blog_detail(request):
    link = request.POST.get('link')
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    content = soup.find('div', class_='row rsrc-content')

    # code for content of the blog
    content1 = content.find('div', class_='entry-content')
    data = content1.find_all('p')
    content_data = []
    for i in data:
        content_p = i.text
        content_data.append(content_p)
    # code for content of the blog ends here !

    # code for heading and date
    heading = content.find('header').h1.text
    date = content.find('header').find('p').find('time').text
    # print(date)
    # code for heading and date ends here !

    # code for cover image
    img = soup.find('div', class_='single-thumbnail row').find('img').get('src')
    # print(img)
    # code for cover image ends here !

    # code for finding all images in the content
    content1 = content.find('div', class_='entry-content')
    try:
        imgs = content1.find_all('img')
        set1 = set()
        for j in imgs:
            set1.add(j.get('src'))
        print(set1)
    except:
        set1 = set()
        # code for finding all images in the content ends here !
    template = 'blog/blog_detail.html'
    context = {
        'link': link,
        'content_data': content_data,
        'heading': heading,
        'date': date,
        'img': img,
        'set1': set1
            }
    return render(request, template, context)
