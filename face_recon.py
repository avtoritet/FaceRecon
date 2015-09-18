import unirest
import urllib

# X-Mashape-Key
KEY = ""

# URL of image
un_url = 'http://www.thewrap.com/wp-content/uploads/2014/04/Mexican-Wolverine-22-Jump-Street.jpg'

# Make the URL URL-friendly
url = urllib.quote_plus(un_url)

# Construct request
response = unirest.get("https://faceplusplus-faceplusplus.p.mashape.com/detection/detect?attribute=glass%2Cpose%2Cgender%2Cage%2Crace%2Csmiling&url=" + url,
  headers={
    "X-Mashape-Key": KEY,
    "Accept": "application/json"
  }
)

data = response.body

# Print face info [Debug]
# print data['face']

# Retrieve face attributes
gender = data['face'][0]['attribute']['gender']['value']
age = str(data['face'][0]['attribute']['age']['value'])
glass = data['face'][0]['attribute']['glass']['value']
race = data['face'][0]['attribute']['race']['value']
smiling = str(data['face'][0]['attribute']['smiling']['value'])

# OUTPUT
print "Gender: " + gender
print "Age: " + age
print "Glasses: " + glass
print "Race: " + race
print "Smiling: " + smiling