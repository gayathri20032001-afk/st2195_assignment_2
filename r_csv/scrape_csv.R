# 1. Load the library
library(rvest)

# 2. Use the EXACT URL (No spaces)
url <- "https://en.wikipedia.org/wiki/Delimiter-separated_values"

# 3. Read the website
webpage <- read_html(url)

# 4. Extract the CSV text from the <pre> tag
# This is the secret step that makes it work!
csv_text <- webpage %>% 
  html_element("pre") %>% 
  html_text()

# 5. Save the file (We save it as wiki_data.csv)
writeLines(csv_text, "wiki_data.csv")

# 6. Read it back to show it worked
my_data <- read.csv(text = csv_text)
print(my_data)

