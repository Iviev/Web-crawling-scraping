# Homework 7: Web Scraping & Crawling
[Google document](https://docs.google.com/document/d/1R7brlJZ5RxRPHROxIkNBASIBMNiufqSnUxKNg-19FLo/edit?usp=sharing)


## Homework Objectives
* Become competent with website structure and crawling page
* Understanding user agent concept and how to utilize it in the request

## Supporting Material
* Beautifulsoup Document
    * https://www.crummy.com/software/BeautifulSoup/bs4/doc
* UMSI faculty website 
    * https://www.si.umich.edu/directory
    * https://www.si.umich.edu/directory?rid=4
    * https://www.si.umich.edu/directory?rid=All

## Starter Files
We have provided you with the following files:
* hw7_part1.py
* hw7_part2.py
* hw7_ec1.py
* hw7_ec2.py

Please use these python files as a template to add your code. You can chose to use functions or not.


## Part 1 (15 points): Crawling the UMSI member (faculty, phD, staff) website with cache

Define an additional function called `get_umsi_data`. The function should access each page of the directory, get the HTML associated with it, and create a dictionary named `umsi_titles` whose keys are the names of each person in the UMSI directory, each of which is associated value is that person's title and their emails, e.g. "PhD Student" and ackerm@umich.edu or "Associate Dean of Research and Arthur F. Thurnau Professor of Information, School of Information" and eadar@umich.edu.
Then write out the dictionary to a file `directory_dict.json`. You might execute get_umsi_data multiple times and aggregate all the return dictionaries a dictionary.
For example, `my_dict_1 = {‘key1’: ‘value1’}` and `my_dict_2 = {‘key2’: ‘value2’}`, then the aggregate result would be `my_dict = {‘key1’: ‘value1’, ‘key2’: ‘value2’}`


### Note:
* To get data from the UMSI site, you must have the headers parameter like so in your request, so that you will not get blocked by the site:  requests.get(base_url, headers={'User-Agent': 'SI_CLASS'})
* **Please crawl one single page and make sure that works before crawling all pages**
* **Please implement cache** to prevent overwhelming crawling of the UMSI website. (The overwhelming crawling might shut down the website and then you cannot check the crawling program. **The deadline will not be extended because of the shut down problem.** Please see every query as a critical one.)
* **Start as early as possible** to prevent the above situation.
* You could crawl a single page to check your caching works and then crawling the rest of the pages.
* If you want to crawl a certain page, the url has page as its parameters. e.g. https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=All&page=11 
You could copy paste the above url and have a sense about the relationship between the url and the web page. You could also change the number after `page=#` to see what’s going on.
We will test your code with the same website page thus it’s okay to utilize the url provided above. Yet **don’t hardcode the inputs** of the function `get_umsi_data`.
* The content of names, titles, and emails in the sample json files are fake.

### Sample Command:
```$ python hw6_part1.py ```

### Sample `directory_dict.json`:
```
{
“Lindsay Blackwell”: {“title”: “PhD Student”, “email”: eadar@umich.edu},

“David Bloom”: {“title”: “Adjunct Clinical Associate Professor of Information, School of Information”, “email”: “ackerm@umich.edu” },
…
}
```



## Part 2 (5 points): Analyze the data from part 1

With the directory_dict.json you have in part 1, this program should search the data you crawl to find the number of PhD students in the directory.

### Sample Command:
`$ python hw6_part2.py`

### Sample output:
`The number of PhD students: 123`

### Note:
The number in the sample out is not correct yet it should be a number.


## Extra Credit 1 (2 points) Crawling headlines, authors, and time from Detroit Free Press

Get the first 10 headlines with authors and times from Detroit Free Press (https://www.freep.com/news/). 
Create a csv file freep.csv with each row as a news and the column includes headline, authors, and times. 

### Note:
* Ignore the banner just crawl the news below the text, “HEADLINES Updated 11:30 a.m. EST ”.
* The headline show on the homepage (https://www.freep.com/news/) will be different from a particular news page. Please get the headline in the home page.
* For the time, just published date and not include the updated date
* If there are multiple authors, it’s okay to just write one author (perhaps with “and”)
* There might have type other than news (photo gallery, for example) You just skip those type. It’s okay to have less than 10 because of skipping some news.


### Sample Command:
`$ python hw6_ec1.py`

### Sample CSV File:
```
Satellite image shows snowstorm over Michigan, Brian Manzullo, “2:41 p.m. ET Feb. 9, 2018”
Great Lakes face highest ice coverage in years, Brian Manzullo, “10:09 a.m. ET Feb. 9, 2018”
Mich. reps want to ban conversion therapy, Aleanna Siacon, “11:33 a.m. ET Feb. 9, 2018”
...
```

### Note:
* The time information is one column in the csv file.


## Extra Credit 2 (2 points): Ann Arbor Boards & Commissions

Crawl Ann Arbor Boards & Commissions and get a list of individuals ranked from most to least in terms of the number of boards and commissions they’re on. Each department has a page listing the name of individuals. You need to crawl the department listed on the Ann Arbor Boards & Commissions (https://a2gov.legistar.com/Departments.aspx). Please write out the result to file AABC.txt, in which each line contains a person name.

### Note: 
* Ann Arbor Boards & Commissions
** (https://a2gov.legistar.com/Departments.aspx) 
* It might take a while to run this program. **You can reduce the number to reduce the time** while you’re testing your code. For example, run the first 5 departments to see whether the code works. Then run the all departments to have the correct answer. **You might also implement cache** for the quicker process. (The cache is not required yet highly recommended.)

* If you find there’s a space before ‘VACANCY’, that’s because the data of the website. You don’t need to do additional handling.

### Sample Command:
`$ python hw7_ec2.py`

### Sample `AABC.txt` File:
```
 VACANCY
Jane Lumm
Jack Eaton
Graydon Krapohl
Anne Bannister
Chuck Warpehoski
...
```

## What to turn in on Canvas
A screenshot of your github repository after the last push to github (as done in previous homeworks)


## Reminder:
Be sure to commit everything (and push!) to your GitHub repo. At a minimum, your repo should include the following files, which you have modified:
* hw7_part1.py
* hw7_part2.py
* (optional) hw7_ec1.py
* (optional) hw7_ec2.py
* README.md

<!-- Add anything for your program here -->
