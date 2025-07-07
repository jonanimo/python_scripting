from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Visit the product page (replace with any Amazon product URL)
url = "https://www.amazon.com/Pre-Alcohol-Refreshed-Science-Backed-Probiotic-Travel-Friendly/dp/B0BX7C6H99/ref=pd_hp_d_btf_rpt_sd_biaws_c_2?_encoding=UTF8&dd=Bj8nJURg0R3qtxKUUV5a29NGzeC2M1AGI-JCm90QnS4%2C&ddc_refnmnt=free&pd_rd_i=B0BX7C6H99&pd_rd_w=ZYadd&content-id=amzn1.sym.b8fbc812-bed0-4266-bf60-df0c3c067ef0&pf_rd_p=b8fbc812-bed0-4266-bf60-df0c3c067ef0&pf_rd_r=H105HM4B14QVV539BKR3&pd_rd_wg=XR8Gl&pd_rd_r=8b183d61-6005-4df6-8dd6-5b2a837ca58c&th=1"  # Example: Echo Dot
driver.get(url)

# Wait for the page to load
time.sleep(2)

# Extract product title
try:
    title = driver.find_element(By.ID, "productTitle").text.strip()
except:
    title = "Title not found"

# Extract price
try:
    price = driver.find_element(By.CLASS_NAME, "a-offscreenfdsf").text.strip()
except:
    price = "Price not found"

# Print results
print("Product:", title)
print("Price:", price)

# Close the browser
driver.quit()