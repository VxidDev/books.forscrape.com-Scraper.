from bs4 import BeautifulSoup
import requests , csv , subprocess
from colorama import Fore , Style , init 

init()

while True:
    try:
        price_limit = float(input("Please enter a price limit in GBP: "))
        minimum_rating = int(input("Please select a minimum rating(1 - 5): "))
        if minimum_rating > 5 or minimum_rating < 1:
            raise ValueError("min rating over 5 or less than 1.")
        break
    except ValueError as e:
        if str(e) in "min rating over 5 or less than 1.":
            print("Min. Rating must be over 0 and less than 5!")
        else:
            print("Input must be a number!") 

file = open("results.csv" , "w" , encoding="utf-8-sig")
writer = csv.writer(file)
writer.writerow(["Name " , " Price " , " Availability "])

ratings = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

total_scraped = 0
total_skipped = 0

for i in range(1 , 51):
    website_link = "https://books.toscrape.com/"
    request = requests.get(f"{website_link}catalogue/page-{i}.html")
    if request.status_code == 200:
        if request.headers.get("Content-Type") == "text/html":
            html = BeautifulSoup(request.text , 'lxml')
            items = html.find_all("article" , attrs={"class" : "product_pod"})
            books_skipped = 0
            books_scraped = 0
            for item in items:
                product_name = item.find("h3").find("a")["title"].strip()
                price = item.find("div" , {"class" : "product_price"}).find("p" , {"class" : "price_color"}).text
                availability = item.find("div" , {"class" : "product_price"}).find("p" , {"class" : "instock availability"}).text
                link = item.find("div" , attrs={"class" : "image_container"}).find("a")["href"]
                rating = ratings[str(item.find("p" , attrs={"class" : "star-rating"})["class"]).split()[1].strip("]").strip("'")]
                if float(str(price).split("£")[1]) < price_limit and rating >= minimum_rating:
                    writer.writerow([str(product_name).strip() + " ", " " + str(rating) + "/5 " + " " + str(price).strip() + " ", " " + str(availability).strip() + " " , f" {website_link}" + str(link).strip() + " "])
                    books_scraped += 1
                else:
                    books_skipped += 1
        else:
            pass
    else:
        print(f"Error: {request.status_code}")
    total_scraped += books_scraped
    total_skipped += books_skipped
    subprocess.run("clear")
    print(f"{Style.BRIGHT + Fore.WHITE}Scraped{Fore.GREEN} {i} {Fore.WHITE}page.{Style.RESET_ALL}")
    print(f"{Style.BRIGHT + Fore.WHITE}Books {Fore.GREEN}scraped{Fore.WHITE}: {books_scraped}\nBooks {Fore.RED}skipped{Fore.WHITE}: {books_skipped}" + Style.RESET_ALL)

file.close()
subprocess.run("clear")
print(f"{Style.BRIGHT + Fore.GREEN}Done!{Fore.WHITE} results at 'results.csv'.\n \
      \nStatistics: \
      \nAmount of books that {Fore.GREEN}matched{Fore.WHITE} the filters: {Fore.GREEN}{total_scraped}{Fore.WHITE}\nAmount of books {Fore.RED}skipped{Fore.WHITE}: {total_skipped}\n")