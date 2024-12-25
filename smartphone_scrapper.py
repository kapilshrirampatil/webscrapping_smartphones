# Importing important libraries
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import time
import os
import requests

#  Define the path to store the data and the file name
path = r"D:\webscrapping_projects\smartphone_data"

file_name = 'smartphone.json'

# Check if the JSON file already exists, if so, load the data into a DataFrame
if os.path.exists(os.path.join(path,file_name)):
    print("filepath is present")
    df = pd.read_json(os.path.join(path,file_name))
    page_number = df['page_number'].max()  # Get the last scraped page number
else:

    # If the path doesn't exist, create the directory
    if not os.path.exists(path):
        print('directory is not present')
        directory = os.makedirs(path)
    df = pd.DataFrame()
    page_number = 1    # Start scraping from the first page

# Loop to scrape data from multiple pages (from current page to page 42)
for i in range(page_number,42):

    # Define the headers for the request to mimic a browser request
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}

    # Make the request to the Flipkart search page for smartphones (page i)
    webpage = requests.get(f'https://www.flipkart.com/search?q=smartphones&page={i}',headers=header).text

     # Parse the page content using BeautifulSoup
    soup = BeautifulSoup(webpage,'html5lib')


    # Initialize lists to store scraped data
    images             = []
    name               = []
    average_rating     = []
    rating_review_comb = []
    ratings            = []
    reviews            = []
    ram                = []
    display_sp         = []
    fp_rr_cam          = []
    battery_power      = []
    processors         = []
    warranty_period    = []
    overall_price      = []
    discounted_price   = []


    # Loop through each product listed on the page
    for j in soup.find_all('div',class_ = '_75nlfW'):

        # Extract image URL and name of the product
        img = j.find('img',class_ = "DByuf4")
        image = img.get('src').strip()
        image_name = img.get('alt').strip()

        # Extract average rating and total ratings & reviews
        ave_rating = j.find('div',class_ = 'XQDdHH').text.strip()
        rating_reviews = j.find('span',class_ = 'Wphh3N').text.strip()
        rating = rating_reviews.split("&")[0].strip()
        review = rating_reviews.split("&")[1].strip()

        # Extract the product features such as RAM, Display, Camera, Battery, etc
        features = j.find_all('li',class_ = 'J+igdf')

        try:

            # Get the individual feature details
            ram_storage = features[0].text.strip()
            display = features[1].text.strip()
            camera = features[2].text.strip()
            battery = features[3].text.strip()
            processor = features[4].text.strip()
            warranty = features[5].text.strip()
            actual_price = j.find('div',class_ = 'yRaY8j ZYYwLA').text.strip()
            price = j.find('div',class_ = 'Nx9bqj _4b5DiR').text.strip()
        
        except:
            ram_storage  = ''
            display      = ''
            camera       = ''
            battery      = ''
            processor    = ''
            warranty     = ''
            actual_price = ""
            price        = ''

        # Append the extracted data to respective lists
        images.append(image)
        name.append(image_name)
        average_rating.append(ave_rating)
        rating_review_comb.append(rating_reviews)
        ratings.append(rating)
        reviews.append(review)
        ram.append(ram_storage)
        display_sp.append(display)
        fp_rr_cam.append(camera)
        battery_power.append(battery)
        processors.append(processor)
        warranty_period.append(warranty)
        overall_price.append(actual_price)
        discounted_price.append(price)

    # Create a temporary DataFrame for the current page data
    temp_df = pd.DataFrame({'Image':images,
                            'Name':name,
                            'Average_Ratings': average_rating,
                            'Rating & Reviews': rating_review_comb,
                            'Total Ratings': ratings,
                            'Total Reviews': reviews,
                            'Rams & Storage':ram,
                            'Display': display_sp,
                            'Camera': fp_rr_cam,
                            'Battery Capacity':battery_power,
                            'Processor':processors,
                            'Warranty Period': warranty_period,
                            'Actual Price':overall_price,
                            'Discounted Price':discounted_price,
                            'page_number':i})


    # Concatenate the new data with the existing data    
    df= pd.concat([df,temp_df],axis = 0,ignore_index=True)

    #  Save the updated data to a JSON file
    df.to_json(os.path.join(path,file_name))
    print(f'page_number {i} is done')

    # Sleep to prevent overwhelming the website with too many requests in a short period
    time.sleep(np.random.choice(range(2,5)))